#!/usr/bin/env python3
"""
RAG v4 Test Runner
==================
Runs the same 218 queries against 47,843 chunks with rebalanced engine weights.

v4 changes:
- Debug intent: troubleshooting weight 1.0, best_practices 0.3, theme_patterns 0.2
- how_to intent: code_examples 1.0, theme_patterns 0.9, best_practices 0.6
- Diversity cap: 40% max per collection (was 60%)
- New topic boosts: error, not working, fix, nil, cors, invalid, memory limit,
  authenticat, oauth, subscription, headless, selling plan
"""

import json
import time
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Setup paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from enhanced_rag.search.engine import EnhancedSearchEngine, analyze_query
from enhanced_rag.tests.test_rag_comprehensive import TEST_QUERIES, rate_relevance

# ============ CONFIG ============
QDRANT_PATH = str(PROJECT_ROOT / "qdrant_enhanced")
OUTPUT_DIR = Path(__file__).parent
JSON_OUT = OUTPUT_DIR / "rag_test_results_v4.json"
REPORT_OUT = OUTPUT_DIR / "rag_test_report_v4.md"

# Previous version stats for comparison
V1_STATS = {"pass_rate": 95.0, "relevant": 165, "partial": 42, "irrelevant": 11, "no_results": 0, "avg_score": 0.758, "chunks": 42744}
V2_STATS = {"pass_rate": 95.0, "relevant": 165, "partial": 42, "irrelevant": 11, "no_results": 0, "avg_score": 0.758, "chunks": 42744}
V3_STATS = {"pass_rate": 93.6, "relevant": 156, "partial": 48, "irrelevant": 14, "no_results": 0, "avg_score": 0.750, "chunks": 47843}


def run_test():
    print(f"{'=' * 60}", flush=True)
    print(f"RAG v4 Test — Rebalanced engine weights", flush=True)
    print(f"Started: {datetime.now().isoformat()}", flush=True)
    print(f"Total queries: {len(TEST_QUERIES)}", flush=True)
    print(f"Qdrant path: {QDRANT_PATH}", flush=True)
    print(f"{'=' * 60}", flush=True)

    # Load index stats
    stats_path = PROJECT_ROOT / "qdrant_enhanced" / "index_stats.json"
    index_stats = {}
    if stats_path.exists():
        with open(stats_path) as f:
            index_stats = json.load(f)
        print(f"\nIndex: {index_stats.get('total_chunks', '?')} chunks across {len(index_stats.get('collections', {}))} collections")
        for col, info in index_stats.get("collections", {}).items():
            print(f"  {col}: {info['total']} chunks ({info['parents']} parents, {info['children']} children)", flush=True)

    # Initialize engine
    print(f"\nInitializing search engine...", flush=True)
    engine = EnhancedSearchEngine(qdrant_path=QDRANT_PATH)
    print("Engine initialized.\n", flush=True)

    # Run queries
    all_results = []
    category_stats = defaultdict(lambda: {
        "total": 0, "relevant": 0, "partial": 0, "irrelevant": 0,
        "no_results": 0, "scores": [], "search_scores": []
    })

    start_time = time.time()

    for i, (query, category, expected_kw, expected_cols) in enumerate(TEST_QUERIES):
        try:
            analyzed = analyze_query(query)
            results = engine.search(query, top_k=5, use_reranker=False, expand_parents=False)
            rating, score, reason = rate_relevance(query, expected_kw, expected_cols, results, category)

            top_results = []
            for r in results[:3]:
                top_results.append({
                    "score": r.score,
                    "collection": r.collection,
                    "file_path": r.metadata.get("file_path", "N/A"),
                    "text_preview": r.text[:200],
                    "content_type": r.metadata.get("content_type", "N/A"),
                    "topics": r.metadata.get("topics", [])[:5],
                })

            result_entry = {
                "index": i + 1,
                "query": query,
                "category": category,
                "expected_keywords": expected_kw,
                "expected_collections": expected_cols,
                "detected_intent": analyzed.intent,
                "target_collections": analyzed.target_collections,
                "expanded_queries": analyzed.expanded_queries,
                "num_results": len(results),
                "top_results": top_results,
                "rating": rating,
                "relevance_score": round(score, 4),
                "reason": reason,
            }
            all_results.append(result_entry)

            # Update stats
            stats = category_stats[category]
            stats["total"] += 1
            stats["scores"].append(score)
            if results:
                stats["search_scores"].append(results[0].score)
            stats[rating.lower()] = stats.get(rating.lower(), 0) + 1

            status = {"RELEVANT": "✅", "PARTIAL": "⚠️", "IRRELEVANT": "❌", "NO_RESULTS": "🔴"}
            print(f"  [{i+1:3d}/{len(TEST_QUERIES)}] {status.get(rating, '?')} {rating:12s} ({score:.2f}) | {category:20s} | {query[:60]}", flush=True)

        except Exception as e:
            print(f"  [{i+1:3d}/{len(TEST_QUERIES)}] 💥 ERROR | {category:20s} | {query[:60]} -> {e}")
            all_results.append({
                "index": i + 1, "query": query, "category": category,
                "expected_keywords": expected_kw, "expected_collections": expected_cols,
                "detected_intent": "error", "target_collections": [], "expanded_queries": [],
                "num_results": 0, "top_results": [], "rating": "ERROR",
                "relevance_score": 0.0, "reason": str(e),
            })
            stats = category_stats[category]
            stats["total"] += 1
            stats["irrelevant"] += 1
            stats["scores"].append(0.0)

    elapsed = time.time() - start_time
    print(f"\n{'=' * 60}")
    print(f"Completed in {elapsed:.1f}s ({elapsed/len(TEST_QUERIES):.2f}s/query)")
    print(f"{'=' * 60}\n")

    # Save JSON
    with open(JSON_OUT, "w") as f:
        json.dump({
            "version": "v4",
            "timestamp": datetime.now().isoformat(),
            "total_queries": len(TEST_QUERIES),
            "total_chunks": index_stats.get("total_chunks", 47843),
            "elapsed_seconds": round(elapsed, 1),
            "engine_changes": {
                "debug_intent": "troubleshooting=1.0, best_practices=0.3, theme_patterns=0.2",
                "how_to_intent": "code_examples=1.0, theme_patterns=0.9, best_practices=0.6",
                "diversity_cap": "40% max per collection (was 60%)",
                "new_topic_boosts": ["error", "not working", "fix", "nil", "cors", "invalid",
                                     "memory limit", "authenticat", "oauth", "subscription",
                                     "headless", "selling plan"],
            },
            "results": all_results,
        }, f, indent=2)
    print(f"JSON saved: {JSON_OUT}")

    # Generate report
    report = generate_v4_report(all_results, category_stats, elapsed, index_stats)
    with open(REPORT_OUT, "w") as f:
        f.write(report)
    print(f"Report saved: {REPORT_OUT}")

    # Quick summary
    total = len(all_results)
    rel = sum(1 for r in all_results if r["rating"] == "RELEVANT")
    par = sum(1 for r in all_results if r["rating"] == "PARTIAL")
    irr = sum(1 for r in all_results if r["rating"] == "IRRELEVANT")
    no_res = sum(1 for r in all_results if r["rating"] == "NO_RESULTS")
    avg = sum(r['relevance_score'] for r in all_results) / total
    print(f"\n🎯 PASS RATE: {(rel+par)/total*100:.1f}% ({rel} relevant + {par} partial / {total})")
    print(f"   RELEVANT:   {rel}  |  PARTIAL: {par}  |  IRRELEVANT: {irr}  |  NO_RESULTS: {no_res}")
    print(f"   Avg score:  {avg:.3f}")
    print(f"\n   v3→v4 Δ:  pass rate {(rel+par)/total*100 - V3_STATS['pass_rate']:+.1f}%  |  "
          f"relevant {rel - V3_STATS['relevant']:+d}  |  irrelevant {irr - V3_STATS['irrelevant']:+d}  |  "
          f"avg score {avg - V3_STATS['avg_score']:+.3f}")


def generate_v4_report(all_results, category_stats, elapsed, index_stats):
    lines = []
    total = len(all_results)
    relevant = sum(1 for r in all_results if r["rating"] == "RELEVANT")
    partial = sum(1 for r in all_results if r["rating"] == "PARTIAL")
    irrelevant = sum(1 for r in all_results if r["rating"] == "IRRELEVANT")
    no_results = sum(1 for r in all_results if r["rating"] == "NO_RESULTS")
    errors = sum(1 for r in all_results if r["rating"] == "ERROR")
    avg_score = sum(r["relevance_score"] for r in all_results) / total
    pass_rate = (relevant + partial) / total * 100

    search_scores = [r["top_results"][0]["score"] for r in all_results if r["top_results"]]
    avg_search_score = sum(search_scores) / len(search_scores) if search_scores else 0

    # Header
    lines.append("# RAG v4 Test Report — Rebalanced Engine Weights")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Total Queries:** {total}")
    lines.append(f"**Total Chunks:** {index_stats.get('total_chunks', 47843)}")
    lines.append(f"**Execution Time:** {elapsed:.1f}s ({elapsed/total:.2f}s/query)")
    lines.append(f"**Settings:** `use_reranker=False, expand_parents=False, top_k=5`")
    lines.append("")

    # Engine changes
    lines.append("### v4 Engine Changes")
    lines.append("")
    lines.append("| Change | Detail |")
    lines.append("|--------|--------|")
    lines.append("| **Debug intent** | troubleshooting=1.0, best_practices ↓ 0.3, theme_patterns ↓ 0.2 |")
    lines.append("| **how_to intent** | code_examples ↑ 1.0, theme_patterns ↓ 0.9, best_practices ↓ 0.6 |")
    lines.append("| **Diversity cap** | 40% max per collection (was 60%) |")
    lines.append("| **New topic boosts** | error, not working, fix, nil, cors, invalid, memory limit, authenticat, oauth, subscription, headless, selling plan |")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| **Overall Pass Rate** (RELEVANT + PARTIAL) | **{pass_rate:.1f}%** ({relevant + partial}/{total}) |")
    lines.append(f"| RELEVANT | {relevant} ({relevant/total*100:.1f}%) |")
    lines.append(f"| PARTIAL | {partial} ({partial/total*100:.1f}%) |")
    lines.append(f"| IRRELEVANT | {irrelevant} ({irrelevant/total*100:.1f}%) |")
    lines.append(f"| NO_RESULTS | {no_results} ({no_results/total*100:.1f}%) |")
    lines.append(f"| ERRORS | {errors} |")
    lines.append(f"| **Avg Relevance Score** | **{avg_score:.3f}** (0-1 scale) |")
    lines.append(f"| **Avg Top-1 Search Score** | **{avg_search_score:.4f}** |")
    lines.append(f"| Queries/Second | {total/elapsed:.1f} |")
    lines.append("")

    # Rating distribution
    lines.append("### Rating Distribution")
    lines.append("```")
    bar_width = 50
    for label, count, emoji in [
        ("RELEVANT", relevant, "🟢"), ("PARTIAL", partial, "🟡"),
        ("IRRELEVANT", irrelevant, "🔴"), ("NO_RESULTS", no_results, "⚫"),
    ]:
        bar_len = int(count / total * bar_width) if total else 0
        lines.append(f"{emoji} {label:12s} {'█' * bar_len}{'░' * (bar_width - bar_len)} {count:3d} ({count/total*100:.1f}%)")
    lines.append("```")
    lines.append("")

    # ===== V1 → V2 → V3 → V4 COMPARISON =====
    lines.append("## Version Comparison: v1 → v2 → v3 → v4")
    lines.append("")
    v4 = {"pass_rate": pass_rate, "relevant": relevant, "partial": partial, "irrelevant": irrelevant, "no_results": no_results, "avg_score": avg_score, "chunks": index_stats.get("total_chunks", 47843)}

    lines.append("| Metric | v1 | v2 | v3 | v4 | v3→v4 Δ |")
    lines.append("|--------|----|----|----|----|--------:|")
    lines.append(f"| **Chunks Indexed** | {V1_STATS['chunks']:,} | {V2_STATS['chunks']:,} | {V3_STATS['chunks']:,} | {v4['chunks']:,} | ±0 |")
    lines.append(f"| **Pass Rate** | {V1_STATS['pass_rate']:.1f}% | {V2_STATS['pass_rate']:.1f}% | {V3_STATS['pass_rate']:.1f}% | {v4['pass_rate']:.1f}% | {v4['pass_rate']-V3_STATS['pass_rate']:+.1f}% |")
    lines.append(f"| RELEVANT | {V1_STATS['relevant']} | {V2_STATS['relevant']} | {V3_STATS['relevant']} | {v4['relevant']} | {v4['relevant']-V3_STATS['relevant']:+d} |")
    lines.append(f"| PARTIAL | {V1_STATS['partial']} | {V2_STATS['partial']} | {V3_STATS['partial']} | {v4['partial']} | {v4['partial']-V3_STATS['partial']:+d} |")
    lines.append(f"| IRRELEVANT | {V1_STATS['irrelevant']} | {V2_STATS['irrelevant']} | {V3_STATS['irrelevant']} | {v4['irrelevant']} | {v4['irrelevant']-V3_STATS['irrelevant']:+d} |")
    lines.append(f"| NO_RESULTS | {V1_STATS['no_results']} | {V2_STATS['no_results']} | {V3_STATS['no_results']} | {v4['no_results']} | {v4['no_results']-V3_STATS['no_results']:+d} |")
    lines.append(f"| **Avg Score** | {V1_STATS['avg_score']:.3f} | {V2_STATS['avg_score']:.3f} | {V3_STATS['avg_score']:.3f} | {v4['avg_score']:.3f} | {v4['avg_score']-V3_STATS['avg_score']:+.3f} |")
    lines.append("")

    # Trend summary
    lines.append("### Trend Summary")
    lines.append("")
    delta_pass = v4['pass_rate'] - V3_STATS['pass_rate']
    delta_irr = v4['irrelevant'] - V3_STATS['irrelevant']
    delta_score = v4['avg_score'] - V3_STATS['avg_score']
    if delta_pass > 0:
        lines.append(f"✅ **Pass rate improved** by {delta_pass:+.1f}% (v3: {V3_STATS['pass_rate']:.1f}% → v4: {v4['pass_rate']:.1f}%)")
    elif delta_pass < 0:
        lines.append(f"⚠️ **Pass rate decreased** by {delta_pass:+.1f}% (v3: {V3_STATS['pass_rate']:.1f}% → v4: {v4['pass_rate']:.1f}%)")
    else:
        lines.append(f"➡️ **Pass rate unchanged** at {v4['pass_rate']:.1f}%")
    if delta_irr < 0:
        lines.append(f"✅ **Irrelevant reduced** by {abs(delta_irr)} (v3: {V3_STATS['irrelevant']} → v4: {v4['irrelevant']})")
    elif delta_irr > 0:
        lines.append(f"⚠️ **Irrelevant increased** by {delta_irr} (v3: {V3_STATS['irrelevant']} → v4: {v4['irrelevant']})")
    if delta_score > 0:
        lines.append(f"✅ **Avg score improved** by {delta_score:+.3f}")
    elif delta_score < 0:
        lines.append(f"⚠️ **Avg score decreased** by {delta_score:+.3f}")
    lines.append("")

    # Per-category breakdown
    lines.append("## Per-Category Breakdown")
    lines.append("")
    lines.append("| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |")
    lines.append("|----------|-------|----------|---------|------------|------------|-----------|-----------|")

    sorted_cats = sorted(category_stats.items(),
                        key=lambda x: (x[1]["relevant"] + x[1]["partial"]) / max(x[1]["total"], 1),
                        reverse=True)

    for cat, stats in sorted_cats:
        cat_pass = (stats["relevant"] + stats["partial"]) / max(stats["total"], 1) * 100
        cat_avg = sum(stats["scores"]) / max(len(stats["scores"]), 1)
        lines.append(
            f"| {cat} | {stats['total']} | "
            f"{stats['relevant']} ({stats['relevant']/max(stats['total'],1)*100:.0f}%) | "
            f"{stats['partial']} ({stats['partial']/max(stats['total'],1)*100:.0f}%) | "
            f"{stats['irrelevant']} ({stats['irrelevant']/max(stats['total'],1)*100:.0f}%) | "
            f"{stats['no_results']} | "
            f"**{cat_pass:.0f}%** | {cat_avg:.3f} |"
        )
    lines.append("")

    # Per-category details
    for cat, stats in sorted_cats:
        lines.append(f"### {cat}")
        cat_results = [r for r in all_results if r["category"] == cat]
        cat_avg = sum(stats["scores"]) / max(len(stats["scores"]), 1)
        cat_pass = (stats["relevant"] + stats["partial"]) / max(stats["total"], 1) * 100

        lines.append(f"- **Pass Rate:** {cat_pass:.0f}%")
        lines.append(f"- **Avg Relevance Score:** {cat_avg:.3f}")
        if stats["search_scores"]:
            lines.append(f"- **Avg Search Score:** {sum(stats['search_scores'])/len(stats['search_scores']):.4f}")

        failures = [r for r in cat_results if r["rating"] in ("IRRELEVANT", "NO_RESULTS")]
        if failures:
            lines.append(f"- **Issues ({len(failures)}):**")
            for f in failures[:5]:
                lines.append(f"  - ❌ `{f['query'][:70]}` → {f['rating']} ({f['reason']})")
        lines.append("")

    # Intent Detection
    lines.append("## Intent Detection Analysis")
    lines.append("")
    intent_stats = defaultdict(lambda: {"total": 0, "relevant": 0, "partial": 0, "irrelevant": 0, "scores": []})
    for r in all_results:
        intent_stats[r["detected_intent"]]["total"] += 1
        intent_stats[r["detected_intent"]]["scores"].append(r["relevance_score"])
        intent_stats[r["detected_intent"]][r["rating"].lower()] = \
            intent_stats[r["detected_intent"]].get(r["rating"].lower(), 0) + 1

    lines.append("| Detected Intent | Count | Pass Rate | Avg Score | Irrelevant |")
    lines.append("|-----------------|-------|-----------|-----------|------------|")
    for intent, data in sorted(intent_stats.items(), key=lambda x: -x[1]["total"]):
        avg = sum(data["scores"]) / max(len(data["scores"]), 1)
        ipass = (data.get("relevant", 0) + data.get("partial", 0)) / max(data["total"], 1) * 100
        lines.append(f"| {intent} | {data['total']} | {ipass:.0f}% | {avg:.3f} | {data.get('irrelevant', 0)} |")
    lines.append("")

    expected_intents = {"how_to", "reference", "debug", "code_gen", "comparison", "architecture"}
    detected = set(intent_stats.keys())
    missing = expected_intents - detected
    if missing:
        lines.append(f"⚠️ **Missing intents:** {', '.join(missing)}")
    else:
        lines.append(f"✅ **All 6 intents detected:** {', '.join(sorted(detected & expected_intents))}")
    lines.append("")

    # Collection Distribution in Results
    lines.append("## Collection Distribution in Results")
    lines.append("")
    col_stats = defaultdict(lambda: {"targeted": 0, "in_results": 0, "in_top1": 0, "scores": []})
    for r in all_results:
        for c in r["target_collections"]:
            col_stats[c]["targeted"] += 1
        for idx, tr in enumerate(r["top_results"]):
            col_stats[tr["collection"]]["in_results"] += 1
            col_stats[tr["collection"]]["scores"].append(tr["score"])
            if idx == 0:
                col_stats[tr["collection"]]["in_top1"] += 1

    lines.append("| Collection | Times Targeted | Times in Top-3 | Times in Top-1 | Avg Score |")
    lines.append("|------------|---------------|----------------|----------------|-----------|")
    for col, data in sorted(col_stats.items(), key=lambda x: -x[1]["in_results"]):
        avg = sum(data["scores"]) / max(len(data["scores"]), 1)
        lines.append(f"| {col} | {data['targeted']} | {data['in_results']} | {data['in_top1']} | {avg:.4f} |")

    # Also show chunk counts per collection
    if index_stats.get("collections"):
        lines.append("")
        lines.append("### Collection Sizes")
        lines.append("")
        lines.append("| Collection | Total Chunks | Parents | Children |")
        lines.append("|------------|-------------|---------|----------|")
        for col, info in sorted(index_stats["collections"].items(), key=lambda x: -x[1]["total"]):
            lines.append(f"| {col} | {info['total']:,} | {info['parents']} | {info['children']:,} |")
    lines.append("")

    # Collection distribution per-result pie (text approx)
    lines.append("### Collection Share in Top-3 Results")
    lines.append("```")
    total_appearances = sum(d["in_results"] for d in col_stats.values())
    for col, data in sorted(col_stats.items(), key=lambda x: -x[1]["in_results"]):
        pct = data["in_results"] / max(total_appearances, 1) * 100
        bar_len = int(pct / 2)
        lines.append(f"  {col:25s} {'█' * bar_len}{'░' * (25 - bar_len)} {data['in_results']:3d} ({pct:.1f}%)")
    lines.append("```")
    lines.append("")

    # Remaining IRRELEVANT queries
    irrelevant_queries = [r for r in all_results if r["rating"] == "IRRELEVANT"]
    lines.append(f"## Remaining IRRELEVANT Queries ({len(irrelevant_queries)})")
    lines.append("")
    if irrelevant_queries:
        lines.append("| # | Query | Category | Intent | Expected Collections | Got Collections | Score | Reason |")
        lines.append("|---|-------|----------|--------|---------------------|----------------|-------|--------|")
        for idx, r in enumerate(irrelevant_queries, 1):
            got_cols = [tr["collection"] for tr in r["top_results"][:3]]
            lines.append(
                f"| {idx} | {r['query'][:55]} | {r['category']} | {r['detected_intent']} | "
                f"{r['expected_collections']} | {got_cols} | "
                f"{r['relevance_score']:.3f} | {r['reason'][:55]} |"
            )
    else:
        lines.append("🎉 **No irrelevant queries!**")
    lines.append("")

    # Regressions from v3 (queries that were RELEVANT/PARTIAL in v3 but are now IRRELEVANT)
    lines.append("## v3 → v4 Changes Detail")
    lines.append("")
    lines.append("*Compare with v3 JSON results for per-query regression analysis.*")
    lines.append("")

    # Top 20 Best
    lines.append("## Top 20 Best-Performing Queries")
    lines.append("")
    sorted_best = sorted(all_results, key=lambda x: x["relevance_score"], reverse=True)[:20]
    lines.append("| # | Score | Rating | Category | Query |")
    lines.append("|---|-------|--------|----------|-------|")
    for i, r in enumerate(sorted_best, 1):
        lines.append(f"| {i} | {r['relevance_score']:.3f} | {r['rating']} | {r['category']} | {r['query'][:80]} |")
    lines.append("")

    # Top 20 Worst
    lines.append("## Top 20 Worst-Performing Queries")
    lines.append("")
    sorted_worst = sorted(all_results, key=lambda x: x["relevance_score"])[:20]
    lines.append("| # | Score | Rating | Category | Query | Reason |")
    lines.append("|---|-------|--------|----------|-------|--------|")
    for i, r in enumerate(sorted_worst, 1):
        lines.append(f"| {i} | {r['relevance_score']:.3f} | {r['rating']} | {r['category']} | {r['query'][:55]} | {r['reason'][:70]} |")
    lines.append("")

    # Full Results
    lines.append("## Full Results Table")
    lines.append("")
    lines.append("| # | Query | Intent | Collections | Score | Rating |")
    lines.append("|---|-------|--------|-------------|-------|--------|")
    for r in all_results:
        cols = ", ".join(r["target_collections"][:2])
        q = r["query"][:65].replace("|", "\\|")
        lines.append(f"| {r['index']} | {q} | {r['detected_intent']} | {cols} | {r['relevance_score']:.3f} | {r['rating']} |")
    lines.append("")

    lines.append("---")
    lines.append(f"*Report generated by run_v4_test.py on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    return "\n".join(lines)


if __name__ == "__main__":
    run_test()
