#!/usr/bin/env python3
"""Enhanced Search v2 — Fixed intent detection, weighted multi-collection search,
smarter routing, expanded synonyms. Addresses all issues from 218-query test."""

import re
import json
import math
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from collections import defaultdict

from qdrant_client import QdrantClient
from qdrant_client.models import (
    NamedVector, NamedSparseVector, SparseVector,
    Filter, FieldCondition, MatchValue, MatchAny,
)
from fastembed import TextEmbedding

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from indexer.build_index import SimpleBM25Vectorizer, COLLECTIONS

# ============ CONFIG ============
QDRANT_PATH = Path(__file__).parent.parent.parent / "qdrant_enhanced"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
TOP_K_PER_COLLECTION = 15  # Fetch per collection
TOP_K_FINAL = 10
RRF_K = 60


# ============ QUERY ANALYSIS v2 ============

@dataclass
class AnalyzedQuery:
    original: str
    intent: str
    collection_weights: dict = field(default_factory=dict)  # {collection: weight}
    entities: dict = field(default_factory=dict)
    expanded_queries: list = field(default_factory=list)
    target_collections: list = field(default_factory=list)  # For display


# Intent patterns with PRIORITY WEIGHTS — higher = more specific = wins ties
INTENT_PATTERNS = {
    "debug": {  # HIGHEST priority — error/problem queries always win
        "weight": 3.5,
        "patterns": [
            r"why (?:is|does|doesn|are|won|can)", r"not working", r"\berror\b",
            r"\bissue\b", r"\bproblem\b", r"\bnil\b", r"\bblank\b",
            r"\bundefined\b", r"\bbroken\b", r"\bfix\b", r"\bbug\b",
            r"\bwrong\b", r"\bfailing\b", r"not (?:show|display|appear|render)",
            r"how to (?:fix|debug|troubleshoot|solve|resolve)",
            r"show(?:s|ing)? nothing", r"(?:returns?|gives?) (?:nil|null|empty|blank|nothing)",
            r"doesn.t (?:work|show|display|render|appear|load)",
        ],
    },
    "code_gen": {  # HIGH priority — explicit generation requests
        "weight": 3.0,
        "patterns": [
            r"^(?:build|generate|create|write|make) (?:me |a |the )?(?:section|template|snippet|theme|component|page|layout)",
            r"^(?:build|generate|create|write|make) (?:me |a |the )?(?:\w+ )?(?:section|template|snippet|component)",
            r"code for (?:a |the )?", r"liquid (?:code |snippet )?for",
            r"generate (?:a |the |me )?", r"build me ",
            r"create (?:a |the )?(?:custom |new )?(?:section|template|snippet|page|block)",
        ],
    },
    "comparison": {  # MEDIUM-HIGH priority
        "weight": 2.0,
        "patterns": [
            r"\bvs\.?\b", r"\bversus\b", r"difference between",
            r"\bcompare\b", r"which (?:is|should|one)",
            r"(?:better|best) (?:way|approach|method|option)",
            r"pros and cons", r"trade.?off",
        ],
    },
    "architecture": {  # MEDIUM priority
        "weight": 1.8,
        "patterns": [
            r"(?:best|recommended) (?:way|practice|approach|pattern)",
            r"how (?:to |should i )?(?:structure|organize|architect)",
            r"pattern for", r"approach (?:to|for)",
            r"should i use", r"when to use",
        ],
    },
    "reference": {  # MEDIUM-LOW priority
        "weight": 1.5,
        "patterns": [
            r"what (?:is|are|does) (?:the |a )?", r"list (?:all|the)",
            r"properties (?:of|for)", r"return[s]?\b",
            r"\battributes\b", r"documentation for", r"docs for",
            r"reference for", r"explain (?:the |a )?",
            r"what properties",
        ],
    },
    "how_to": {  # LOWEST priority — catch-all
        "weight": 1.0,
        "patterns": [
            r"how (?:do|can|to|would|should)", r"implement\b",
            r"set up\b", r"configure\b", r"example of",
            r"tutorial\b", r"add (?:a |the )?",
        ],
    },
}

# Collection weights per intent — ALL 6 collections searched, with different weights
INTENT_COLLECTION_WEIGHTS = {
    "reference": {
        "liquid_reference": 1.0, "api_reference": 0.9,
        "code_examples": 0.3, "theme_patterns": 0.2,
        "troubleshooting": 0.1, "best_practices": 0.2,
    },
    "how_to": {
        "theme_patterns": 0.9, "code_examples": 1.0, "best_practices": 0.6,
        "liquid_reference": 0.4, "api_reference": 0.4,
        "troubleshooting": 0.3,
    },
    "debug": {
        "troubleshooting": 1.0, "liquid_reference": 0.7, "code_examples": 0.5,
        "best_practices": 0.3, "theme_patterns": 0.2,
        "api_reference": 0.2,
    },
    "code_gen": {
        "code_examples": 1.0, "theme_patterns": 0.9, "liquid_reference": 0.7,
        "best_practices": 0.4, "api_reference": 0.2,
        "troubleshooting": 0.1,
    },
    "architecture": {
        "best_practices": 1.0, "theme_patterns": 0.9, "code_examples": 0.6,
        "liquid_reference": 0.3, "api_reference": 0.3,
        "troubleshooting": 0.2,
    },
    "comparison": {
        "best_practices": 1.0, "liquid_reference": 0.8, "theme_patterns": 0.7,
        "troubleshooting": 0.5, "code_examples": 0.4,
        "api_reference": 0.3,
    },
}

# Topic-based collection boosts — if query contains these terms, boost these collections
TOPIC_BOOSTS = {
    # Troubleshooting terms → boost troubleshooting hard
    "error": {"troubleshooting": +0.5, "theme_patterns": -0.3, "best_practices": -0.3},
    "not working": {"troubleshooting": +0.5, "theme_patterns": -0.3, "best_practices": -0.3},
    "fix": {"troubleshooting": +0.4, "theme_patterns": -0.2, "best_practices": -0.2},
    "nil": {"troubleshooting": +0.5, "liquid_reference": +0.3},
    "cors": {"troubleshooting": +0.5, "api_reference": +0.3},
    "invalid": {"troubleshooting": +0.4, "liquid_reference": +0.3},
    "debug": {"troubleshooting": +0.4, "code_examples": +0.2},
    "memory limit": {"troubleshooting": +0.5, "best_practices": +0.2},
    "show nothing": {"troubleshooting": +0.5, "liquid_reference": +0.3},
    
    # API queries → boost api_reference hard, suppress liquid_reference
    "admin api": {"api_reference": +0.5, "liquid_reference": -0.4},
    "graphql": {"api_reference": +0.5, "liquid_reference": -0.4},
    "rest api": {"api_reference": +0.5, "liquid_reference": -0.4},
    "storefront api": {"api_reference": +0.5, "liquid_reference": -0.3},
    "ajax api": {"api_reference": +0.4, "code_examples": +0.3},
    "webhook": {"api_reference": +0.5, "liquid_reference": -0.3},
    "api": {"api_reference": +0.3, "liquid_reference": -0.2},
    
    # Performance → boost best_practices
    "performance": {"best_practices": +0.5, "theme_patterns": +0.3},
    "core web vitals": {"best_practices": +0.6, "theme_patterns": +0.3},
    "lazy load": {"best_practices": +0.5, "code_examples": +0.3},
    "preload": {"best_practices": +0.5, "code_examples": +0.3},
    "speed": {"best_practices": +0.5, "theme_patterns": +0.3},
    "render time": {"best_practices": +0.5, "liquid_reference": +0.3},
    "bundle size": {"best_practices": +0.5, "code_examples": +0.3},
    "defer": {"best_practices": +0.5, "code_examples": +0.3},
    "layout shift": {"best_practices": +0.6},
    "optimize": {"best_practices": +0.4, "theme_patterns": +0.3},
    
    # CSS/Styling → boost theme_patterns and code_examples
    "css": {"theme_patterns": +0.4, "code_examples": +0.4, "liquid_reference": -0.3},
    "flexbox": {"theme_patterns": +0.5, "code_examples": +0.4, "liquid_reference": -0.4},
    "grid layout": {"theme_patterns": +0.5, "code_examples": +0.4},
    "media quer": {"theme_patterns": +0.5, "best_practices": +0.3, "liquid_reference": -0.3},
    "responsive": {"theme_patterns": +0.4, "code_examples": +0.3},
    "animation": {"theme_patterns": +0.4, "code_examples": +0.4},
    "hover": {"theme_patterns": +0.4, "code_examples": +0.4},
    "dark mode": {"theme_patterns": +0.5, "code_examples": +0.3},
    "tailwind": {"theme_patterns": +0.4, "code_examples": +0.5},
    "style": {"theme_patterns": +0.3, "code_examples": +0.2},
    "font": {"theme_patterns": +0.3, "code_examples": +0.2},
    
    # Liquid-specific → boost liquid_reference  
    "liquid object": {"liquid_reference": +0.5},
    "liquid filter": {"liquid_reference": +0.5},
    "liquid tag": {"liquid_reference": +0.5},
    "{{": {"liquid_reference": +0.4},
    "{%": {"liquid_reference": +0.4},
    "forloop": {"liquid_reference": +0.5},
    
    # Cart/Checkout → boost code_examples and theme_patterns
    "cart drawer": {"theme_patterns": +0.5, "code_examples": +0.4},
    "ajax cart": {"code_examples": +0.4, "theme_patterns": +0.4},
    "cart/add": {"api_reference": +0.4, "code_examples": +0.3},
    "cart/update": {"api_reference": +0.4, "code_examples": +0.3},
    "cart/change": {"api_reference": +0.4, "code_examples": +0.3},
    "checkout": {"api_reference": +0.3, "theme_patterns": +0.3},
    "shipping": {"theme_patterns": +0.3, "code_examples": +0.3},
    
    # Theme dev patterns → boost theme_patterns
    "section": {"theme_patterns": +0.3, "code_examples": +0.2},
    "template": {"theme_patterns": +0.3, "code_examples": +0.2},
    "snippet": {"theme_patterns": +0.3, "code_examples": +0.3},
    "dawn": {"code_examples": +0.5, "theme_patterns": +0.3},
    "schema": {"theme_patterns": +0.3, "liquid_reference": +0.3},
    
    # Advanced → specific boosts
    "metaobject": {"api_reference": +0.5, "theme_patterns": +0.3},
    "hydrogen": {"code_examples": +0.4, "api_reference": +0.3},
    "function": {"api_reference": +0.4, "code_examples": +0.3},
    "app block": {"theme_patterns": +0.4, "code_examples": +0.3},
    "app extension": {"theme_patterns": +0.4, "api_reference": +0.3},
    "multipass": {"api_reference": +0.5, "theme_patterns": -0.3},
    "b2b": {"api_reference": +0.4, "best_practices": +0.3},
    "market": {"api_reference": +0.3, "best_practices": +0.3},
    "authenticat": {"api_reference": +0.5, "theme_patterns": -0.3},
    "oauth": {"api_reference": +0.5, "theme_patterns": -0.3},
    "subscription": {"api_reference": +0.5, "theme_patterns": -0.2},
    "headless": {"api_reference": +0.4, "code_examples": +0.3},
    "selling plan": {"api_reference": +0.5},
}

# Expanded synonym dictionary
SHOPIFY_SYNONYMS = {
    # Cart
    "cart drawer": ["ajax cart", "side cart", "cart slider", "mini cart"],
    "cart page": ["cart template", "cart.liquid", "cart section"],
    "add to cart": ["cart/add.js", "ajax add to cart", "product form submit"],
    "cart update": ["cart/update.js", "update cart quantities"],
    
    # Product
    "product page": ["product template", "product.liquid", "product section", "PDP"],
    "variant": ["product variant", "option selector", "variant picker"],
    "swatches": ["color swatches", "variant swatches", "option swatches"],
    "quick add": ["quick buy", "add to cart button", "quick shop"],
    
    # Navigation
    "mega menu": ["navigation menu", "multi-level menu", "dropdown menu"],
    "hamburger menu": ["mobile menu", "drawer menu", "mobile navigation"],
    "breadcrumb": ["breadcrumbs", "breadcrumb navigation"],
    
    # Data
    "metafield": ["custom data", "metafields", "product.metafields"],
    "metaobject": ["metaobjects", "custom content type"],
    
    # Media
    "image": ["product image", "image_url", "responsive image", "srcset"],
    "gallery": ["image gallery", "product gallery", "carousel", "slider"],
    
    # Search & Filter
    "search": ["predictive search", "search results", "search.json"],
    "filter": ["collection filter", "faceted search", "product filter"],
    "pagination": ["paginate", "infinite scroll", "load more"],
    
    # Money & Price
    "money": ["price", "money filter", "currency", "money_with_currency"],
    "compare at price": ["sale price", "discount price", "original price"],
    
    # Styling
    "responsive": ["mobile responsive", "media queries", "breakpoints"],
    "dark mode": ["dark theme", "color scheme toggle", "light dark switch"],
    "animation": ["CSS animation", "transition effects", "scroll animation"],
    "hover effect": ["hover state", "mouseover effect", "hover animation"],
    
    # Performance
    "lazy load": ["lazy loading", "loading=lazy", "intersection observer"],
    "preload": ["preloading", "resource hints", "link rel preload"],
    "core web vitals": ["LCP", "CLS", "FID", "INP", "page speed"],
    
    # APIs
    "admin api": ["Admin REST API", "Admin GraphQL API", "Shopify API"],
    "storefront api": ["Storefront GraphQL", "headless commerce API"],
    "section rendering api": ["section rendering", "dynamic sections", "AJAX sections"],
}


def analyze_query(query: str) -> AnalyzedQuery:
    """Analyze query with weighted intent detection and smart collection routing."""
    query_lower = query.lower().strip()
    
    # 1. Weighted intent classification
    intent_scores = {}
    for intent, config in INTENT_PATTERNS.items():
        weight = config["weight"]
        match_count = sum(1 for p in config["patterns"] if re.search(p, query_lower))
        intent_scores[intent] = match_count * weight
    
    # Pick highest weighted score; default to how_to
    best_intent = max(intent_scores, key=intent_scores.get)
    if intent_scores[best_intent] == 0:
        best_intent = "how_to"
    
    # 2. Start with intent-based collection weights
    col_weights = dict(INTENT_COLLECTION_WEIGHTS.get(best_intent, INTENT_COLLECTION_WEIGHTS["how_to"]))
    
    # 3. Apply topic-based boosts
    for topic, boosts in TOPIC_BOOSTS.items():
        if topic in query_lower:
            for col, boost in boosts.items():
                col_weights[col] = max(0.0, min(1.5, col_weights.get(col, 0) + boost))
    
    # 4. Determine which collections to actually search (weight > 0.2)
    active_collections = {col: w for col, w in col_weights.items() if w > 0.2}
    if not active_collections:
        active_collections = col_weights  # Fallback to all
    
    # Sort by weight for display
    sorted_cols = sorted(active_collections.keys(), key=lambda c: -active_collections[c])
    
    # 5. Extract entities
    from chunkers.smart_chunker import detect_entities
    entities = detect_entities(query)
    
    # 6. Expand query with synonyms
    expanded = [query]
    for term, synonyms in SHOPIFY_SYNONYMS.items():
        if term in query_lower:
            for syn in synonyms[:2]:
                expanded.append(query_lower.replace(term, syn))
    
    # Entity-based expansion
    if entities["objects"]:
        expanded.append(f"Shopify Liquid {' '.join(entities['objects'][:3])}")
    if entities["filters"]:
        expanded.append(f"Liquid filter {' '.join(entities['filters'][:3])}")
    
    expanded = list(dict.fromkeys(expanded))[:4]
    
    return AnalyzedQuery(
        original=query,
        intent=best_intent,
        collection_weights=active_collections,
        entities=entities,
        expanded_queries=expanded,
        target_collections=sorted_cols[:4],  # Top 4 for display
    )


# ============ SEARCH RESULT ============

@dataclass
class SearchResult:
    text: str
    score: float
    collection: str
    metadata: dict
    parent_text: Optional[str] = None


# ============ SEARCH ENGINE v2 ============

class EnhancedSearchEngine:
    """Multi-collection weighted hybrid search with reranking."""
    
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
        if self._reranker is None:
            try:
                from fastembed import TextCrossEncoder
                self._reranker = TextCrossEncoder(model_name="Xenova/ms-marco-MiniLM-L-6-v2")
            except Exception:
                self._reranker = False
        return self._reranker if self._reranker is not False else None
    
    def search(self, query: str, top_k: int = TOP_K_FINAL,
               use_reranker: bool = True, expand_parents: bool = True) -> list:
        """Full pipeline: analyze → weighted multi-collection search → RRF → rerank → expand."""
        
        # 1. Analyze
        analyzed = analyze_query(query)
        
        # 2. Search ALL active collections with weights
        all_results = []
        for collection, weight in analyzed.collection_weights.items():
            if weight < 0.15:
                continue
            try:
                results = self._hybrid_search_collection(
                    collection, analyzed.expanded_queries, TOP_K_PER_COLLECTION
                )
                # Apply collection weight to scores
                for r in results:
                    r.score *= weight
                all_results.extend(results)
            except Exception:
                continue
        
        if not all_results:
            return []
        
        # 3. RRF fusion with diversity
        fused = self._rrf_fusion_diverse(all_results, analyzed.collection_weights)
        
        # 4. Rerank
        if use_reranker:
            reranker = self._get_reranker()
            if reranker:
                fused = self._rerank(query, fused, top_k * 3)
        
        # 5. Expand parents
        if expand_parents:
            fused = self._expand_parents(fused)
        
        return fused[:top_k]
    
    def _hybrid_search_collection(self, collection: str, queries: list,
                                   top_k: int) -> list:
        """Dense + sparse search on a single collection."""
        client = self._get_client()
        embed_model = self._get_embed_model()
        bm25 = self._get_bm25()
        
        all_results = []
        
        for query in queries:
            dense_vector = list(embed_model.embed([query]))[0].tolist()
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
                            score=r.score * 0.3,
                            collection=collection,
                            metadata=r.payload,
                        ))
                except Exception:
                    pass
        
        return all_results
    
    def _rrf_fusion_diverse(self, results: list, col_weights: dict) -> list:
        """RRF fusion with collection diversity enforcement."""
        # Group by text hash
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
        
        # Sort by score
        sorted_results = sorted(text_scores.values(), key=lambda x: -x["score"])
        
        # Diversity enforcement: no more than 40% from any single collection
        final = []
        col_counts = defaultdict(int)
        max_per_col = max(2, int(TOP_K_FINAL * 0.4))
        
        for data in sorted_results:
            result = data["result"]
            result.score = data["score"]
            
            if col_counts[result.collection] < max_per_col:
                final.append(result)
                col_counts[result.collection] += 1
            elif len(final) < TOP_K_FINAL * 3:
                # Still add but with penalty
                result.score *= 0.5
                final.append(result)
                col_counts[result.collection] += 1
        
        # Re-sort after diversity adjustment
        final.sort(key=lambda x: -x.score)
        return final
    
    def _rerank(self, query: str, results: list, top_k: int) -> list:
        """Cross-encoder reranking."""
        reranker = self._get_reranker()
        if not reranker or not results:
            return results[:top_k]
        
        candidates = results[:min(len(results), 50)]
        texts = [r.text for r in candidates]
        
        try:
            scores = list(reranker.rerank(query, texts))
            scored = list(zip(candidates, scores))
            scored.sort(key=lambda x: -x[1].score)
            
            reranked = []
            for result, score_obj in scored[:top_k]:
                result.score = score_obj.score
                reranked.append(result)
            return reranked
        except Exception:
            return results[:top_k]
    
    def _expand_parents(self, results: list) -> list:
        """Fetch parent context for child chunks."""
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
        """Search and return formatted results."""
        analyzed = analyze_query(query)
        results = self.search(query, top_k=top_k)
        
        output = []
        output.append(f"🔍 Query: {query}")
        output.append(f"📊 Intent: {analyzed.intent}")
        output.append(f"🎯 Collections: {', '.join(analyzed.target_collections)}")
        
        # Show weights
        weight_str = " | ".join(f"{c}:{w:.1f}" for c, w in 
                                sorted(analyzed.collection_weights.items(), key=lambda x: -x[1])[:4])
        output.append(f"⚖️ Weights: {weight_str}")
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
