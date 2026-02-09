#!/usr/bin/env python3
"""Index all RAG knowledge base files into Qdrant vector database.
Chunks documents, generates embeddings via FastEmbed, stores in Qdrant (local mode)."""

import os
import json
import hashlib
from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from fastembed import TextEmbedding

# ============ CONFIG ============
RAW_DOCS = Path(__file__).parent.parent / "raw-docs"
QDRANT_PATH = Path(__file__).parent.parent / "qdrant_data"
COLLECTION_NAME = "shopify_knowledge"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"  # 384 dimensions, fast & good quality
BATCH_SIZE = 64

# File extensions to process
TEXT_EXTENSIONS = {".md", ".liquid", ".json", ".js", ".ts", ".tsx", ".rb", ".css", ".scss", ".txt"}
# Skip these directories
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "qdrant_data"}


def get_all_files(base_dir):
    """Recursively get all indexable files"""
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        
        for filename in filenames:
            filepath = Path(root) / filename
            if filepath.suffix.lower() in TEXT_EXTENSIONS:
                files.append(filepath)
    return files


def read_file_safe(filepath):
    """Read file with encoding fallback"""
    for encoding in ["utf-8", "latin-1", "cp1252"]:
        try:
            return filepath.read_text(encoding=encoding)
        except (UnicodeDecodeError, ValueError):
            continue
    return None


def get_splitter_for_file(filepath):
    """Get appropriate text splitter based on file type"""
    ext = filepath.suffix.lower()
    
    if ext == ".md":
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
    elif ext in (".js", ".ts", ".tsx"):
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.JS,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
    elif ext == ".json":
        return RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", "},{", ",", " "],
        )
    elif ext == ".liquid":
        return RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n{%- ", "\n{% ", "\n\n", "\n", "{%", "{{", " "
            ],
        )
    elif ext == ".rb":
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.RUBY,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
    else:
        return RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )


def categorize_file(filepath, base_dir):
    """Determine category from file path"""
    relative = filepath.relative_to(base_dir)
    parts = relative.parts
    if len(parts) > 0:
        return parts[0]  # First directory = category
    return "uncategorized"


def extract_source_url(content):
    """Extract source URL from frontmatter if present"""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            frontmatter = content[3:end]
            for line in frontmatter.split("\n"):
                if line.strip().startswith("source:"):
                    return line.split("source:", 1)[1].strip()
    return None


def chunk_documents(files, base_dir):
    """Chunk all documents and prepare for embedding"""
    all_chunks = []
    skipped = 0
    errors = 0
    
    print(f"📄 Processing {len(files)} files...")
    
    for filepath in tqdm(files, desc="Chunking"):
        content = read_file_safe(filepath)
        if not content or len(content.strip()) < 20:
            skipped += 1
            continue
        
        try:
            category = categorize_file(filepath, base_dir)
            source_url = extract_source_url(content)
            splitter = get_splitter_for_file(filepath)
            chunks = splitter.split_text(content)
            
            for i, chunk in enumerate(chunks):
                if len(chunk.strip()) < 20:
                    continue
                
                # Create unique ID
                chunk_id = hashlib.md5(
                    f"{filepath}:{i}:{chunk[:100]}".encode()
                ).hexdigest()
                
                all_chunks.append({
                    "id": chunk_id,
                    "text": chunk,
                    "metadata": {
                        "file_path": str(filepath.relative_to(base_dir)),
                        "file_name": filepath.name,
                        "file_type": filepath.suffix,
                        "category": category,
                        "chunk_index": i,
                        "total_chunks": len(chunks),
                        "source_url": source_url or "",
                        "char_count": len(chunk),
                    }
                })
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"\n  ⚠️ Error processing {filepath.name}: {e}")
    
    print(f"\n📊 Chunking complete:")
    print(f"   Files processed: {len(files) - skipped - errors}")
    print(f"   Files skipped (too small): {skipped}")
    print(f"   Files with errors: {errors}")
    print(f"   Total chunks: {len(all_chunks)}")
    
    return all_chunks


def index_to_qdrant(chunks):
    """Generate embeddings and index into Qdrant"""
    
    # Initialize embedding model
    print(f"\n🧠 Loading embedding model: {EMBEDDING_MODEL}")
    embedding_model = TextEmbedding(model_name=EMBEDDING_MODEL)
    
    # Get embedding dimension from a test
    test_embedding = list(embedding_model.embed(["test"]))[0]
    embedding_dim = len(test_embedding)
    print(f"   Embedding dimension: {embedding_dim}")
    
    # Initialize Qdrant (local file storage)
    print(f"\n💾 Initializing Qdrant at: {QDRANT_PATH}")
    QDRANT_PATH.mkdir(parents=True, exist_ok=True)
    
    client = QdrantClient(path=str(QDRANT_PATH))
    
    # Recreate collection
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        print(f"   Deleted existing collection: {COLLECTION_NAME}")
    
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=embedding_dim,
            distance=Distance.COSINE,
        ),
    )
    print(f"   Created collection: {COLLECTION_NAME}")
    
    # Process in batches
    texts = [c["text"] for c in chunks]
    total_batches = (len(texts) + BATCH_SIZE - 1) // BATCH_SIZE
    
    print(f"\n🔄 Embedding & indexing {len(chunks)} chunks in {total_batches} batches...")
    
    point_id = 0
    for batch_start in tqdm(range(0, len(chunks), BATCH_SIZE), desc="Indexing", total=total_batches):
        batch_end = min(batch_start + BATCH_SIZE, len(chunks))
        batch_texts = texts[batch_start:batch_end]
        batch_chunks = chunks[batch_start:batch_end]
        
        # Generate embeddings
        embeddings = list(embedding_model.embed(batch_texts))
        
        # Create points
        points = []
        for i, (embedding, chunk) in enumerate(zip(embeddings, batch_chunks)):
            points.append(PointStruct(
                id=point_id,
                vector=embedding.tolist(),
                payload={
                    "text": chunk["text"],
                    **chunk["metadata"],
                }
            ))
            point_id += 1
        
        # Upsert to Qdrant
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
        )
    
    # Verify
    collection_info = client.get_collection(COLLECTION_NAME)
    print(f"\n✅ Indexing complete!")
    print(f"   Collection: {COLLECTION_NAME}")
    print(f"   Total points: {collection_info.points_count}")
    print(f"   Vector dimension: {embedding_dim}")
    print(f"   Distance metric: COSINE")
    print(f"   Storage: {QDRANT_PATH}")
    
    return collection_info.points_count


def save_index_stats(chunks, points_count):
    """Save indexing statistics"""
    stats = {
        "collection_name": COLLECTION_NAME,
        "embedding_model": EMBEDDING_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
        "total_chunks": len(chunks),
        "total_points": points_count,
        "categories": {},
    }
    
    for chunk in chunks:
        cat = chunk["metadata"]["category"]
        if cat not in stats["categories"]:
            stats["categories"][cat] = {"chunks": 0, "files": set()}
        stats["categories"][cat]["chunks"] += 1
        stats["categories"][cat]["files"].add(chunk["metadata"]["file_name"])
    
    # Convert sets to counts
    for cat in stats["categories"]:
        stats["categories"][cat]["files"] = len(stats["categories"][cat]["files"])
    
    stats_path = Path(__file__).parent.parent / "index_stats.json"
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"\n📋 Stats saved to: {stats_path}")


def main():
    print("=" * 60)
    print("  SHOPIFY RAG KNOWLEDGE BASE — INDEXING PIPELINE")
    print("=" * 60)
    print()
    
    # 1. Collect all files
    print("📂 Scanning files...")
    files = get_all_files(RAW_DOCS)
    print(f"   Found {len(files)} indexable files")
    
    # Show breakdown
    by_ext = {}
    for f in files:
        ext = f.suffix.lower()
        by_ext[ext] = by_ext.get(ext, 0) + 1
    for ext, count in sorted(by_ext.items(), key=lambda x: -x[1]):
        print(f"   {ext}: {count}")
    
    # 2. Chunk documents
    print()
    chunks = chunk_documents(files, RAW_DOCS)
    
    if not chunks:
        print("❌ No chunks generated. Aborting.")
        return
    
    # 3. Embed & index
    points_count = index_to_qdrant(chunks)
    
    # 4. Save stats
    save_index_stats(chunks, points_count)
    
    print("\n" + "=" * 60)
    print("  ✅ INDEXING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
