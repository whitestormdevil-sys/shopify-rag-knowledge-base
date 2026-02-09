#!/usr/bin/env python3
"""Memory-efficient indexing — process files in streaming batches instead of loading all at once."""

import os
import gc
import json
import hashlib
from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from fastembed import TextEmbedding

RAW_DOCS = Path(__file__).parent.parent / "raw-docs"
QDRANT_PATH = Path(__file__).parent.parent / "qdrant_data"
COLLECTION_NAME = "shopify_knowledge"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
BATCH_SIZE = 32  # Smaller batches for memory

TEXT_EXTENSIONS = {".md", ".liquid", ".json", ".js", ".ts", ".tsx", ".rb", ".css", ".scss", ".txt"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "qdrant_data"}


def get_all_files(base_dir):
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in filenames:
            filepath = Path(root) / filename
            if filepath.suffix.lower() in TEXT_EXTENSIONS:
                files.append(filepath)
    return files


def read_file_safe(filepath):
    for encoding in ["utf-8", "latin-1", "cp1252"]:
        try:
            return filepath.read_text(encoding=encoding)
        except (UnicodeDecodeError, ValueError):
            continue
    return None


def get_splitter(ext):
    if ext == ".md":
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    elif ext in (".js", ".ts", ".tsx"):
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.JS, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    elif ext == ".liquid":
        return RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
            separators=["\n{%- ", "\n{% ", "\n\n", "\n", "{%", "{{", " "])
    elif ext == ".rb":
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.RUBY, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    else:
        return RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)


def extract_source_url(content):
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            for line in content[3:end].split("\n"):
                if line.strip().startswith("source:"):
                    return line.split("source:", 1)[1].strip()
    return None


def main():
    print("=" * 60)
    print("  SHOPIFY RAG — MEMORY-EFFICIENT INDEXING")
    print("=" * 60)
    
    files = get_all_files(RAW_DOCS)
    print(f"\n📂 Found {len(files)} files")
    
    # Init embedding model
    print(f"\n🧠 Loading model: {EMBEDDING_MODEL}")
    embed_model = TextEmbedding(model_name=EMBEDDING_MODEL)
    test_emb = list(embed_model.embed(["test"]))[0]
    dim = len(test_emb)
    print(f"   Dimension: {dim}")
    
    # Init Qdrant
    QDRANT_PATH.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(QDRANT_PATH))
    
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
    
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
    print(f"   Collection created: {COLLECTION_NAME}\n")
    
    # Process files in streaming batches
    point_id = 0
    total_chunks = 0
    batch_texts = []
    batch_payloads = []
    files_processed = 0
    
    for filepath in tqdm(files, desc="Processing"):
        content = read_file_safe(filepath)
        if not content or len(content.strip()) < 20:
            continue
        
        ext = filepath.suffix.lower()
        category = filepath.relative_to(RAW_DOCS).parts[0] if len(filepath.relative_to(RAW_DOCS).parts) > 0 else "uncategorized"
        source_url = extract_source_url(content)
        
        try:
            splitter = get_splitter(ext)
            chunks = splitter.split_text(content)
        except:
            continue
        
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 20:
                continue
            
            batch_texts.append(chunk)
            batch_payloads.append({
                "text": chunk,
                "file_path": str(filepath.relative_to(RAW_DOCS)),
                "file_name": filepath.name,
                "file_type": ext,
                "category": category,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "source_url": source_url or "",
            })
            
            # Flush batch
            if len(batch_texts) >= BATCH_SIZE:
                embeddings = list(embed_model.embed(batch_texts))
                points = []
                for emb, payload in zip(embeddings, batch_payloads):
                    points.append(PointStruct(id=point_id, vector=emb.tolist(), payload=payload))
                    point_id += 1
                
                client.upsert(collection_name=COLLECTION_NAME, points=points)
                total_chunks += len(batch_texts)
                batch_texts.clear()
                batch_payloads.clear()
                del embeddings, points
                gc.collect()
        
        files_processed += 1
    
    # Flush remaining
    if batch_texts:
        embeddings = list(embed_model.embed(batch_texts))
        points = []
        for emb, payload in zip(embeddings, batch_payloads):
            points.append(PointStruct(id=point_id, vector=emb.tolist(), payload=payload))
            point_id += 1
        client.upsert(collection_name=COLLECTION_NAME, points=points)
        total_chunks += len(batch_texts)
    
    # Verify
    info = client.get_collection(COLLECTION_NAME)
    print(f"\n\n✅ INDEXING COMPLETE!")
    print(f"   Files processed: {files_processed}")
    print(f"   Total chunks indexed: {total_chunks}")
    print(f"   Qdrant points: {info.points_count}")
    print(f"   Vector dim: {dim}")
    print(f"   Model: {EMBEDDING_MODEL}")
    
    # Save stats
    stats = {
        "collection": COLLECTION_NAME, "model": EMBEDDING_MODEL,
        "chunk_size": CHUNK_SIZE, "overlap": CHUNK_OVERLAP,
        "files": files_processed, "chunks": total_chunks,
        "points": info.points_count, "dimension": dim
    }
    (Path(__file__).parent.parent / "index_stats.json").write_text(json.dumps(stats, indent=2))
    print(f"\n📋 Stats saved to index_stats.json")


if __name__ == "__main__":
    main()
