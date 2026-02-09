#!/usr/bin/env python3
"""Enhanced Search — Query analysis, hybrid search (dense + BM25), 
multi-collection routing, cross-encoder reranking, parent-child expansion."""

import re
import json
import math
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

from qdrant_client import QdrantClient
from qdrant_client.models import (
    NamedVector, NamedSparseVector, SparseVector,
    Filter, FieldCondition, MatchValue, MatchAny,
    SearchRequest, FusionQuery, Prefetch, Query,
)
from fastembed import TextEmbedding

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from indexer.build_index import SimpleBM25Vectorizer, COLLECTIONS

# ============ CONFIG ============
QDRANT_PATH = Path(__file__).parent.parent.parent / "qdrant_enhanced"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
TOP_K_INITIAL = 30  # Per collection
TOP_K_FINAL = 10   # After reranking
RRF_K = 60  # Reciprocal Rank Fusion constant


# ============ QUERY ANALYSIS ============

@dataclass
class AnalyzedQuery:
    original: str
    intent: str  # reference | how_to | debug | code_gen | architecture | comparison
    target_collections: list = field(default_factory=list)
    entities: dict = field(default_factory=dict)
    expanded_queries: list = field(default_factory=list)
    filters: dict = field(default_factory=dict)


# Intent classification keywords
INTENT_PATTERNS = {
    "reference": [
        r"what (?:is|are|does)", r"list (?:all|the)", r"properties of",
        r"return[s]?\b", r"attributes", r"documentation for", r"docs for",
        r"reference for", r"object\b", r"filter\b", r"tag\b",
    ],
    "how_to": [
        r"how (?:do|can|to|would)", r"create a", r"build a", r"make a",
        r"implement", r"add a", r"set up", r"configure", r"generate",
        r"write a", r"example of", r"tutorial",
    ],
    "debug": [
        r"why (?:is|does|doesn)", r"not working", r"error", r"issue",
        r"problem", r"nil\b", r"blank\b", r"undefined", r"broken",
        r"fix\b", r"bug\b", r"wrong\b", r"failing",
    ],
    "code_gen": [
        r"generate", r"create (?:a |the )?(?:section|template|snippet|theme)",
        r"build (?:a |the )?(?:section|template|snippet|theme)",
        r"code for", r"liquid for", r"write (?:a |the )?(?:section|template)",
    ],
    "architecture": [
        r"structure", r"organize", r"architecture", r"best (?:way|practice)",
        r"should i use", r"pattern for", r"approach",
    ],
    "comparison": [
        r"vs\b", r"versus", r"difference between", r"compare",
        r"which (?:is|should)", r"or\b.*\?",
    ],
}

# Collection routing by intent
INTENT_COLLECTION_MAP = {
    "reference": ["liquid_reference", "api_reference"],
    "how_to": ["theme_patterns", "code_examples", "best_practices"],
    "debug": ["troubleshooting", "liquid_reference", "best_practices"],
    "code_gen": ["code_examples", "theme_patterns", "liquid_reference"],
    "architecture": ["theme_patterns", "best_practices", "code_examples"],
    "comparison": ["liquid_reference", "best_practices", "troubleshooting"],
}

# Entity patterns for query expansion
SHOPIFY_SYNONYMS = {
    "cart drawer": ["ajax cart", "side cart", "cart slider", "mini cart", "cart/add.js"],
    "product page": ["product template", "product.liquid", "product section", "PDP"],
    "collection page": ["collection template", "collection grid", "product grid"],
    "variant": ["product variant", "option selector", "variant picker"],
    "swatches": ["color swatches", "variant swatches", "option swatches", "color picker"],
    "quick add": ["quick buy", "add to cart button", "quick shop"],
    "mega menu": ["navigation menu", "multi-level menu", "dropdown menu"],
    "metafield": ["custom data", "metafields", "product.metafields"],
    "image": ["product image", "image_url", "responsive image", "srcset"],
    "search": ["predictive search", "search results", "search.json"],
    "pagination": ["paginate", "infinite scroll", "load more"],
    "money": ["price", "money filter", "currency", "money_with_currency"],
}


def analyze_query(query: str) -> AnalyzedQuery:
    """Analyze user query to determine intent, entities, and routing."""
    query_lower = query.lower().strip()
    
    # 1. Classify intent
    intent_scores = {}
    for intent, patterns in INTENT_PATTERNS.items():
        score = sum(1 for p in patterns if re.search(p, query_lower))
        intent_scores[intent] = score
    
    intent = max(intent_scores, key=intent_scores.get) if max(intent_scores.values()) > 0 else "how_to"
    
    # 2. Route to collections
    target_collections = INTENT_COLLECTION_MAP.get(intent, COLLECTIONS[:3])
    
    # If query mentions specific API/technical terms, add those collections
    if any(term in query_lower for term in ["graphql", "rest api", "admin api", "storefront api"]):
        if "api_reference" not in target_collections:
            target_collections.insert(0, "api_reference")
    if any(term in query_lower for term in ["liquid", "object", "filter", "tag", "{%", "{{"]):
        if "liquid_reference" not in target_collections:
            target_collections.insert(0, "liquid_reference")
    if any(term in query_lower for term in ["dawn", "theme code", "source code", ".liquid"]):
        if "code_examples" not in target_collections:
            target_collections.insert(0, "code_examples")
    if any(term in query_lower for term in ["error", "nil", "bug", "not working", "issue"]):
        if "troubleshooting" not in target_collections:
            target_collections.insert(0, "troubleshooting")
    
    # Limit to top 3 collections
    target_collections = target_collections[:3]
    
    # 3. Extract entities
    from chunkers.smart_chunker import detect_entities
    entities = detect_entities(query)
    
    # 4. Expand query with synonyms
    expanded = [query]
    for term, synonyms in SHOPIFY_SYNONYMS.items():
        if term in query_lower:
            for syn in synonyms[:2]:
                expanded.append(query_lower.replace(term, syn))
    
    # Add entity-based expansion
    if entities["objects"]:
        expanded.append(f"Shopify Liquid {' '.join(entities['objects'][:3])}")
    if entities["filters"]:
        expanded.append(f"Liquid filter {' '.join(entities['filters'][:3])}")
    
    # Deduplicate
    expanded = list(dict.fromkeys(expanded))[:4]
    
    return AnalyzedQuery(
        original=query,
        intent=intent,
        target_collections=target_collections,
        entities=entities,
        expanded_queries=expanded,
    )


# ============ HYBRID SEARCH ============

@dataclass
class SearchResult:
    text: str
    score: float
    collection: str
    metadata: dict
    parent_text: Optional[str] = None  # Expanded parent context


class EnhancedSearchEngine:
    """Multi-collection hybrid search with reranking."""
    
    def __init__(self, qdrant_path: str = None, lazy_load: bool = False):
        self.qdrant_path = qdrant_path or str(QDRANT_PATH)
        self._client = None
        self._embed_model = None
        self._bm25 = None
        self._reranker = None
        if not lazy_load:
            self._init_all()
    
    def _init_all(self):
        self._get_client()
        self._get_embed_model()
        self._get_bm25()
    
    def _get_client(self):
        if self._client is None:
            self._client = QdrantClient(path=self.qdrant_path)
        return self._client
    
    def _get_embed_model(self):
        if self._embed_model is None:
            self._embed_model = TextEmbedding(model_name=EMBEDDING_MODEL)
        return self._embed_model
    
    def _get_bm25(self):
        if self._bm25 is None:
            self._bm25 = SimpleBM25Vectorizer()
            vocab_path = Path(self.qdrant_path) / "bm25_vocab.json"
            if vocab_path.exists():
                self._bm25.load(vocab_path)
        return self._bm25
    
    def _get_reranker(self):
        """Lazy-load reranker model."""
        if self._reranker is None:
            try:
                from fastembed import TextCrossEncoder
                self._reranker = TextCrossEncoder(model_name="Xenova/ms-marco-MiniLM-L-6-v2")
            except Exception:
                self._reranker = False  # Mark as unavailable
        return self._reranker if self._reranker is not False else None
    
    def search(self, query: str, top_k: int = TOP_K_FINAL, 
               use_reranker: bool = True, expand_parents: bool = True) -> list:
        """
        Full enhanced search pipeline:
        1. Analyze query
        2. Hybrid search across target collections
        3. RRF fusion
        4. Optional reranking
        5. Optional parent expansion
        """
        # 1. Analyze
        analyzed = analyze_query(query)
        
        # 2. Search each target collection with multiple queries
        all_results = []
        
        for collection in analyzed.target_collections:
            try:
                results = self._hybrid_search_collection(
                    collection, analyzed.expanded_queries, TOP_K_INITIAL
                )
                all_results.extend(results)
            except Exception as e:
                continue
        
        if not all_results:
            return []
        
        # 3. Deduplicate and RRF fusion
        fused = self._rrf_fusion(all_results)
        
        # 4. Rerank with cross-encoder
        if use_reranker:
            reranker = self._get_reranker()
            if reranker:
                fused = self._rerank(query, fused, top_k * 3)
        
        # 5. Expand parents (if child matched, also return parent context)
        if expand_parents:
            fused = self._expand_parents(fused)
        
        # 6. Return top K
        return fused[:top_k]
    
    def _hybrid_search_collection(self, collection: str, queries: list, 
                                   top_k: int) -> list:
        """Hybrid dense + sparse search on a single collection."""
        client = self._get_client()
        embed_model = self._get_embed_model()
        bm25 = self._get_bm25()
        
        all_results = []
        
        for query in queries:
            # Dense embedding
            dense_vector = list(embed_model.embed([query]))[0].tolist()
            
            # Sparse BM25 vector
            sp_indices, sp_values = bm25.transform(query)
            
            # Dense search
            try:
                dense_results = client.query_points(
                    collection_name=collection,
                    query=dense_vector,
                    using="dense",
                    limit=top_k,
                )
                for r in dense_results.points:
                    all_results.append(SearchResult(
                        text=r.payload.get("text", ""),
                        score=r.score,
                        collection=collection,
                        metadata=r.payload,
                    ))
            except Exception:
                pass
            
            # Sparse search
            if sp_indices:
                try:
                    sparse_results = client.query_points(
                        collection_name=collection,
                        query=SparseVector(indices=sp_indices, values=sp_values),
                        using="bm25",
                        limit=top_k,
                    )
                    for r in sparse_results.points:
                        all_results.append(SearchResult(
                            text=r.payload.get("text", ""),
                            score=r.score * 0.3,  # Weight sparse lower
                            collection=collection,
                            metadata=r.payload,
                        ))
                except Exception:
                    pass
        
        return all_results
    
    def _rrf_fusion(self, results: list) -> list:
        """Reciprocal Rank Fusion to merge results from multiple searches."""
        # Group by text hash to deduplicate
        text_scores = {}
        
        for rank, result in enumerate(sorted(results, key=lambda x: -x.score)):
            text_hash = hash(result.text[:200])
            rrf_score = 1.0 / (RRF_K + rank + 1)
            
            if text_hash in text_scores:
                text_scores[text_hash]["score"] += rrf_score
            else:
                text_scores[text_hash] = {
                    "result": result,
                    "score": rrf_score,
                }
        
        # Sort by fused score
        fused = []
        for data in sorted(text_scores.values(), key=lambda x: -x["score"]):
            result = data["result"]
            result.score = data["score"]
            fused.append(result)
        
        return fused
    
    def _rerank(self, query: str, results: list, top_k: int) -> list:
        """Cross-encoder reranking for more accurate scoring."""
        reranker = self._get_reranker()
        if not reranker or not results:
            return results[:top_k]
        
        # Prepare pairs
        candidates = results[:min(len(results), 50)]  # Rerank top 50
        texts = [r.text for r in candidates]
        
        try:
            # Score all pairs
            scores = list(reranker.rerank(query, texts))
            
            # Sort by reranker score
            scored = list(zip(candidates, scores))
            scored.sort(key=lambda x: -x[1].score)
            
            reranked = []
            for result, score_obj in scored[:top_k]:
                result.score = score_obj.score
                reranked.append(result)
            
            return reranked
        except Exception as e:
            return results[:top_k]
    
    def _expand_parents(self, results: list) -> list:
        """If a child chunk matched, fetch its parent for full context."""
        client = self._get_client()
        
        for result in results:
            parent_id = result.metadata.get("parent_id")
            if parent_id and result.metadata.get("chunk_type") == "child":
                try:
                    parent_results = client.scroll(
                        collection_name=result.collection,
                        scroll_filter=Filter(
                            must=[
                                FieldCondition(
                                    key="chunk_type",
                                    match=MatchValue(value="parent"),
                                ),
                            ]
                        ),
                        limit=50,
                    )
                    for point in parent_results[0]:
                        if result.text[:80] in point.payload.get("text", ""):
                            result.parent_text = point.payload["text"]
                            break
                except Exception:
                    pass
        
        return results
    
    def search_formatted(self, query: str, top_k: int = 5) -> str:
        """Search and return formatted results for display."""
        analyzed = analyze_query(query)
        results = self.search(query, top_k=top_k)
        
        output = []
        output.append(f"🔍 Query: {query}")
        output.append(f"📊 Intent: {analyzed.intent}")
        output.append(f"🎯 Collections: {', '.join(analyzed.target_collections)}")
        output.append(f"🔗 Entities: {json.dumps(analyzed.entities, indent=None)}")
        output.append(f"📝 Results: {len(results)}")
        output.append("-" * 50)
        
        for i, r in enumerate(results, 1):
            output.append(f"\n{'='*40}")
            output.append(f"#{i} | Score: {r.score:.4f} | {r.collection}")
            output.append(f"File: {r.metadata.get('file_path', 'N/A')}")
            output.append(f"Type: {r.metadata.get('content_type', 'N/A')} | "
                         f"Complexity: {r.metadata.get('complexity', 'N/A')}")
            if r.metadata.get('topics'):
                output.append(f"Topics: {', '.join(r.metadata['topics'][:5])}")
            if r.metadata.get('source_url'):
                output.append(f"Source: {r.metadata['source_url']}")
            output.append(f"\n{r.text[:500]}{'...' if len(r.text) > 500 else ''}")
            
            if r.parent_text and r.parent_text != r.text:
                output.append(f"\n[Parent context: {len(r.parent_text)} chars available]")
        
        return "\n".join(output)
