#!/usr/bin/env python3
"""Enhanced Indexer — Multi-collection, hybrid search (dense + sparse), 
hierarchical chunks with rich metadata."""

import os
import gc
import json
import math
import hashlib
from pathlib import Path
from collections import defaultdict
from tqdm import tqdm

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, SparseVectorParams, SparseIndexParams,
    PointStruct, NamedVector, NamedSparseVector, SparseVector,
    PayloadSchemaType,
)
from fastembed import TextEmbedding

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from chunkers.smart_chunker import process_file, Chunk

# ============ CONFIG ============
RAW_DOCS = Path(__file__).parent.parent.parent / "raw-docs"
QDRANT_PATH = Path(__file__).parent.parent.parent / "qdrant_enhanced"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
EMBEDDING_DIM = 384
BATCH_SIZE = 32

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "qdrant_data", "qdrant_enhanced"}

COLLECTIONS = [
    "liquid_reference",
    "code_examples", 
    "theme_patterns",
    "api_reference",
    "troubleshooting",
    "best_practices",
]

TEXT_EXTENSIONS = {".md", ".liquid", ".json", ".js", ".ts", ".tsx", ".rb", ".css", ".scss", ".txt"}


# ============ BM25 SPARSE VECTORS ============

class SimpleBM25Vectorizer:
    """Simple BM25-inspired sparse vectorizer for hybrid search."""
    
    def __init__(self):
        self.vocab = {}
        self.idf = {}
        self.doc_count = 0
        self.avg_doc_len = 0
    
    def fit(self, texts: list):
        """Build vocabulary and compute IDF."""
        self.doc_count = len(texts)
        doc_freq = defaultdict(int)
        total_len = 0
        
        for text in texts:
            tokens = self._tokenize(text)
            total_len += len(tokens)
            unique_tokens = set(tokens)
            for token in unique_tokens:
                doc_freq[token] += 1
        
        self.avg_doc_len = total_len / max(self.doc_count, 1)
        
        # Build vocab (top 50k terms by doc frequency)
        sorted_terms = sorted(doc_freq.items(), key=lambda x: -x[1])[:50000]
        for idx, (term, df) in enumerate(sorted_terms):
            self.vocab[term] = idx
            # IDF with smoothing
            self.idf[term] = math.log((self.doc_count - df + 0.5) / (df + 0.5) + 1)
    
    def transform(self, text: str) -> tuple:
        """Convert text to sparse BM25 vector."""
        tokens = self._tokenize(text)
        doc_len = len(tokens)
        
        # Count term frequencies
        tf = defaultdict(int)
        for token in tokens:
            if token in self.vocab:
                tf[token] += 1
        
        # BM25 scoring
        k1 = 1.5
        b = 0.75
        indices = []
        values = []
        
        for term, freq in tf.items():
            idx = self.vocab[term]
            idf = self.idf.get(term, 0)
            tf_norm = (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * doc_len / max(self.avg_doc_len, 1)))
            score = idf * tf_norm
            if score > 0:
                indices.append(idx)
                values.append(round(score, 4))
        
        return indices, values
    
    def _tokenize(self, text: str) -> list:
        """Simple tokenization."""
        import re
        text = text.lower()
        # Keep underscores (important for Liquid: image_url, line_item, etc.)
        tokens = re.findall(r'[a-z][a-z0-9_]*', text)
        # Also add compound tokens split by underscore
        expanded = []
        for t in tokens:
            expanded.append(t)
            if "_" in t:
                expanded.extend(t.split("_"))
        return expanded
    
    def save(self, path: Path):
        data = {"vocab": self.vocab, "idf": self.idf, 
                "doc_count": self.doc_count, "avg_doc_len": self.avg_doc_len}
        path.write_text(json.dumps(data))
    
    def load(self, path: Path):
        data = json.loads(path.read_text())
        self.vocab = data["vocab"]
        self.idf = data["idf"]
        self.doc_count = data["doc_count"]
        self.avg_doc_len = data["avg_doc_len"]


# ============ FILE COLLECTION ============

def get_all_files(base_dir: Path) -> list:
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in filenames:
            filepath = Path(root) / filename
            if filepath.suffix.lower() in TEXT_EXTENSIONS:
                files.append(filepath)
    return files


# ============ MAIN INDEXER ============

def main():
    print("=" * 60)
    print("  ENHANCED RAG — MULTI-COLLECTION HYBRID INDEXER")
    print("=" * 60)
    
    # 1. Collect files
    print(f"\n📂 Scanning {RAW_DOCS}...")
    files = get_all_files(RAW_DOCS)
    print(f"   Found {len(files)} files")
    
    # 2. Smart chunk all files
    print("\n📄 Smart chunking all files...")
    all_chunks: list[Chunk] = []
    chunks_by_collection = defaultdict(list)
    
    for filepath in tqdm(files, desc="Chunking"):
        try:
            chunks = process_file(filepath, RAW_DOCS)
            for chunk in chunks:
                all_chunks.append(chunk)
                chunks_by_collection[chunk.collection].append(chunk)
        except Exception as e:
            pass  # Skip problematic files
    
    print(f"\n📊 Chunking complete: {len(all_chunks)} total chunks")
    for col, chunks in sorted(chunks_by_collection.items()):
        parents = sum(1 for c in chunks if c.chunk_type == "parent")
        children = sum(1 for c in chunks if c.chunk_type == "child")
        print(f"   {col}: {len(chunks)} chunks ({parents} parents, {children} children)")
    
    # 3. Build BM25 vocabulary from all chunks
    print("\n📝 Building BM25 vocabulary...")
    QDRANT_PATH.mkdir(parents=True, exist_ok=True)
    bm25 = SimpleBM25Vectorizer()
    all_texts = [c.text for c in all_chunks]
    bm25.fit(all_texts)
    print(f"   Vocabulary size: {len(bm25.vocab)}")
    bm25.save(QDRANT_PATH / "bm25_vocab.json")
    del all_texts
    gc.collect()
    
    # 4. Initialize embedding model
    print(f"\n🧠 Loading embedding model: {EMBEDDING_MODEL}")
    embed_model = TextEmbedding(model_name=EMBEDDING_MODEL)
    
    # 5. Initialize Qdrant
    QDRANT_PATH.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(QDRANT_PATH))
    
    # Create collections with hybrid vectors
    for col_name in COLLECTIONS:
        if client.collection_exists(col_name):
            client.delete_collection(col_name)
        
        client.create_collection(
            collection_name=col_name,
            vectors_config={
                "dense": VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE),
            },
            sparse_vectors_config={
                "bm25": SparseVectorParams(
                    index=SparseIndexParams(on_disk=False),
                ),
            },
        )
        
        # Create payload indexes for fast filtering
        client.create_payload_index(col_name, "chunk_type", PayloadSchemaType.KEYWORD)
        client.create_payload_index(col_name, "content_type", PayloadSchemaType.KEYWORD)
        client.create_payload_index(col_name, "category", PayloadSchemaType.KEYWORD)
        client.create_payload_index(col_name, "complexity", PayloadSchemaType.KEYWORD)
    
    print(f"   Created {len(COLLECTIONS)} collections with hybrid vectors")
    
    # 6. Index each collection
    total_indexed = 0
    
    for col_name in COLLECTIONS:
        chunks = chunks_by_collection.get(col_name, [])
        if not chunks:
            print(f"\n⏭️  {col_name}: no chunks")
            continue
        
        print(f"\n📥 Indexing {col_name}: {len(chunks)} chunks")
        
        point_id = 0
        for batch_start in tqdm(range(0, len(chunks), BATCH_SIZE), 
                                desc=f"  {col_name}", leave=False):
            batch_end = min(batch_start + BATCH_SIZE, len(chunks))
            batch = chunks[batch_start:batch_end]
            batch_texts = [c.text for c in batch]
            
            # Dense embeddings
            dense_embeddings = list(embed_model.embed(batch_texts))
            
            # Sparse BM25 vectors
            sparse_vectors = [bm25.transform(text) for text in batch_texts]
            
            # Create points
            points = []
            for i, (chunk, dense_emb, (sp_indices, sp_values)) in enumerate(
                zip(batch, dense_embeddings, sparse_vectors)
            ):
                payload = {
                    "text": chunk.text,
                    "chunk_type": chunk.chunk_type,
                    "parent_id": chunk.parent_id,
                    "content_type": chunk.content_type,
                    "file_path": chunk.file_path,
                    "file_name": chunk.file_name,
                    "file_type": chunk.file_type,
                    "category": chunk.category,
                    "source_url": chunk.source_url,
                    "topics": chunk.topics,
                    "related_objects": chunk.related_objects,
                    "related_filters": chunk.related_filters,
                    "complexity": chunk.complexity,
                    "char_count": chunk.char_count,
                }
                
                point = PointStruct(
                    id=point_id,
                    vector={
                        "dense": dense_emb.tolist(),
                    },
                    payload=payload,
                )
                
                # Add sparse vector only if non-empty
                if sp_indices:
                    point.vector["bm25"] = SparseVector(
                        indices=sp_indices,
                        values=sp_values,
                    )
                
                points.append(point)
                point_id += 1
            
            client.upsert(collection_name=col_name, points=points)
            total_indexed += len(points)
            
            del dense_embeddings, sparse_vectors, points
            gc.collect()
        
        # Collection stats
        info = client.get_collection(col_name)
        print(f"   ✅ {col_name}: {info.points_count} points indexed")
    
    # 7. Summary
    print("\n" + "=" * 60)
    print("  ✅ ENHANCED INDEXING COMPLETE")
    print("=" * 60)
    print(f"\n   Total chunks: {len(all_chunks)}")
    print(f"   Total indexed: {total_indexed}")
    print(f"   Collections: {len(COLLECTIONS)}")
    print(f"   Dense model: {EMBEDDING_MODEL}")
    print(f"   Sparse: BM25 (vocab: {len(bm25.vocab)})")
    print(f"   Storage: {QDRANT_PATH}")
    
    # Save stats
    stats = {
        "total_chunks": len(all_chunks),
        "total_indexed": total_indexed,
        "embedding_model": EMBEDDING_MODEL,
        "embedding_dim": EMBEDDING_DIM,
        "bm25_vocab_size": len(bm25.vocab),
        "collections": {},
    }
    for col_name in COLLECTIONS:
        chunks = chunks_by_collection.get(col_name, [])
        stats["collections"][col_name] = {
            "total": len(chunks),
            "parents": sum(1 for c in chunks if c.chunk_type == "parent"),
            "children": sum(1 for c in chunks if c.chunk_type == "child"),
        }
    
    stats_path = QDRANT_PATH / "index_stats.json"
    stats_path.write_text(json.dumps(stats, indent=2))
    print(f"\n📋 Stats: {stats_path}")


if __name__ == "__main__":
    main()
