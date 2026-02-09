#!/usr/bin/env python3
"""FastAPI service for the Enhanced RAG search layer."""

from fastapi import FastAPI, Query as QueryParam
from pydantic import BaseModel
from typing import Optional
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

app = FastAPI(
    title="ShopifyAI Enhanced RAG",
    description="Multi-collection hybrid search for Shopify knowledge",
    version="1.0.0",
)

# Lazy-load engine
_engine = None

def get_engine():
    global _engine
    if _engine is None:
        from search.engine import EnhancedSearchEngine
        _engine = EnhancedSearchEngine()
    return _engine


class SearchRequest(BaseModel):
    query: str
    top_k: int = 10
    use_reranker: bool = True
    expand_parents: bool = True
    collections: Optional[list] = None  # Override auto-routing


class SearchResponse(BaseModel):
    query: str
    intent: str
    collections_searched: list
    results: list
    total_results: int


@app.get("/")
def root():
    return {"service": "ShopifyAI Enhanced RAG", "status": "running"}


@app.get("/health")
def health():
    engine = get_engine()
    client = engine._get_client()
    collections = {}
    for col in ["liquid_reference", "code_examples", "theme_patterns", 
                 "api_reference", "troubleshooting", "best_practices"]:
        try:
            info = client.get_collection(col)
            collections[col] = info.points_count
        except:
            collections[col] = 0
    
    return {
        "status": "healthy",
        "collections": collections,
        "total_points": sum(collections.values()),
    }


@app.post("/search", response_model=SearchResponse)
def search(req: SearchRequest):
    engine = get_engine()
    
    from search.engine import analyze_query
    analyzed = analyze_query(req.query)
    
    results = engine.search(
        query=req.query,
        top_k=req.top_k,
        use_reranker=req.use_reranker,
        expand_parents=req.expand_parents,
    )
    
    return SearchResponse(
        query=req.query,
        intent=analyzed.intent,
        collections_searched=analyzed.target_collections,
        results=[
            {
                "rank": i + 1,
                "score": round(r.score, 4),
                "collection": r.collection,
                "text": r.text,
                "file_path": r.metadata.get("file_path", ""),
                "content_type": r.metadata.get("content_type", ""),
                "complexity": r.metadata.get("complexity", ""),
                "topics": r.metadata.get("topics", []),
                "source_url": r.metadata.get("source_url", ""),
                "parent_text": r.parent_text[:2000] if r.parent_text else None,
            }
            for i, r in enumerate(results)
        ],
        total_results=len(results),
    )


@app.get("/search/quick")
def search_quick(q: str = QueryParam(..., description="Search query"),
                 k: int = QueryParam(5, description="Number of results")):
    """Quick search endpoint — GET for easy testing."""
    engine = get_engine()
    formatted = engine.search_formatted(q, top_k=k)
    return {"formatted": formatted}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)
