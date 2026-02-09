#!/usr/bin/env python3
"""
V4 Final Validation — STRICT, INDEPENDENT assessment of the Enhanced RAG search engine.
Runs all 300 questions, grades results strictly, produces detailed reports.
"""

import json
import sys
import time
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

# Setup paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from enhanced_rag.search.engine import EnhancedSearchEngine, analyze_query


# ============ GRADING ============

GRADE_SCORES = {
    "RELEVANT": 3,
    "PARTIAL": 2,
    "IRRELEVANT": 1,
    "NO_RESULTS": 0,
}


def topic_matches_text(topic: str, text: str) -> bool:
    """
    Check if a topic keyword appears in text (case insensitive).
    Strict matching: requires word boundary or underscore-separated match.
    'product' matches 'product' or 'product.title' but NOT 'production'.
    """
    topic_lower = topic.lower().strip()
    text_lower = text.lower()

    # Direct word-boundary match
    # Allow word chars around underscores for Liquid-style identifiers like content_for_header
    pattern = r'(?<![a-z])' + re.escape(topic_lower) + r'(?![a-z])'
    if re.search(pattern, text_lower):
        return True

    # For multi-word topics, also try with underscores/hyphens
    if ' ' in topic_lower:
        variants = [
            topic_lower.replace(' ', '_'),
            topic_lower.replace(' ', '-'),
            topic_lower.replace(' ', ''),
        ]
        for v in variants:
            pattern = r'(?<![a-z])' + re.escape(v) + r'(?![a-z])'
            if re.search(pattern, text_lower):
                return True

    return False


def grade_result(question: dict, results: list) -> dict:
    """
    Grade search results for a question using STRICT criteria.
    Returns grade info dict.
    """
    if not results:
        return {
            "grade": "NO_RESULTS",
            "score": GRADE_SCORES["NO_RESULTS"],
            "topics_found": [],
            "topics_missing": question.get("expected_topics", []),
            "collections_found": [],
            "collections_missing": question.get("expected_collections", []),
            "reason": "No results returned",
        }

    expected_topics = question.get("expected_topics", [])
    expected_collections = question.get("expected_collections", [])

    # Only look at top-3 results for grading
    top3 = results[:3]

    # Combine text from top-3 results for topic matching
    combined_text = " ".join(r.text for r in top3)

    # Check topic matches
    topics_found = []
    topics_missing = []
    for topic in expected_topics:
        if topic_matches_text(topic, combined_text):
            topics_found.append(topic)
        else:
            topics_missing.append(topic)

    # Check collection matches in top-3
    result_collections = set(r.collection for r in top3)
    collections_found = [c for c in expected_collections if c in result_collections]
    collections_missing = [c for c in expected_collections if c not in result_collections]

    # Apply grading rules
    n_topics = len(topics_found)
    has_collection = len(collections_found) > 0

    if n_topics >= 3 and has_collection:
        grade = "RELEVANT"
        reason = f"Found {n_topics}/{len(expected_topics)} topics AND matching collection(s)"
    elif n_topics >= 2 or has_collection:
        grade = "PARTIAL"
        parts = []
        if n_topics >= 2:
            parts.append(f"{n_topics} topics matched")
        if has_collection:
            parts.append(f"collection(s) matched: {collections_found}")
        reason = "PARTIAL: " + "; ".join(parts)
    else:
        grade = "IRRELEVANT"
        reason = f"Only {n_topics} topic(s) matched, no expected collections in top-3"

    return {
        "grade": grade,
        "score": GRADE_SCORES[grade],
        "topics_found": topics_found,
        "topics_missing": topics_missing,
        "collections_found": collections_found,
        "collections_missing": collections_missing,
        "reason": reason,
    }


# ============ MAIN VALIDATION ============

def run_validation():
    print("=" * 60)
    print("V4 FINAL VALIDATION — STRICT INDEPENDENT ASSESSMENT")
    print("=" * 60)

    # Load questions
    questions_path = PROJECT_ROOT / "enhanced_rag" / "tests" / "generated_questions.json"
    with open(questions_path) as f:
        questions = json.load(f)
    print(f"\nLoaded {len(questions)} questions")

    # Initialize engine
    print("Initializing search engine...")
    t0 = time.time()
    engine = EnhancedSearchEngine()
    init_time = time.time() - t0
    print(f"Engine initialized in {init_time:.1f}s")

    # Run all queries
    results_data = []
    total = len(questions)
    start_time = time.time()

    for i, q in enumerate(questions):
        if (i + 1) % 25 == 0 or i == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (total - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1}/{total}] {rate:.1f} q/s, ETA {eta:.0f}s — {q['question'][:60]}...")

        query_start = time.time()

        # Analyze query for intent info
        analyzed = analyze_query(q["question"])

        # Search
        try:
            search_results = engine.search(
                q["question"],
                top_k=5,
                use_reranker=False,
                expand_parents=False,
            )
        except Exception as e:
            search_results = []
            print(f"  ERROR on q{q['id']}: {e}")

        query_time = time.time() - query_start

        # Grade
        grading = grade_result(q, search_results)

        # Build result record
        result_record = {
            "id": q["id"],
            "question": q["question"],
            "category": q.get("category", "Unknown"),
            "difficulty": q.get("difficulty", "unknown"),
            "expected_topics": q.get("expected_topics", []),
            "expected_collections": q.get("expected_collections", []),
            "detected_intent": analyzed.intent,
            "target_collections": analyzed.target_collections,
            "collection_weights": {k: round(v, 3) for k, v in analyzed.collection_weights.items()},
            "num_results": len(search_results),
            "result_collections": [r.collection for r in search_results],
            "top3_collections": [r.collection for r in search_results[:3]],
            "top3_scores": [round(r.score, 4) for r in search_results[:3]],
            "top3_snippets": [r.text[:200] for r in search_results[:3]],
            "grade": grading["grade"],
            "grade_score": grading["score"],
            "topics_found": grading["topics_found"],
            "topics_missing": grading["topics_missing"],
            "collections_found": grading["collections_found"],
            "collections_missing": grading["collections_missing"],
            "grade_reason": grading["reason"],
            "query_time_ms": round(query_time * 1000, 1),
        }
        results_data.append(result_record)

    total_time = time.time() - start_time
    print(f"\nCompleted {total} queries in {total_time:.1f}s ({total/total_time:.1f} q/s)")

    # Save raw results
    results_path = PROJECT_ROOT / "enhanced_rag" / "tests" / "v4_final_results.json"
    with open(results_path, "w") as f:
        json.dump(results_data, f, indent=2)
    print(f"Results saved to {results_path}")

    # Generate report
    report = generate_report(results_data, total_time)
    report_path = PROJECT_ROOT / "enhanced_rag" / "tests" / "v4_final_report.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Report saved to {report_path}")

    # Print summary
    grades = Counter(r["grade"] for r in results_data)
    print(f"\n{'='*40}")
    print(f"GRADE DISTRIBUTION:")
    for g in ["RELEVANT", "PARTIAL", "IRRELEVANT", "NO_RESULTS"]:
        print(f"  {g}: {grades.get(g, 0)}")
    pass_rate = (grades.get("RELEVANT", 0) + grades.get("PARTIAL", 0)) / len(results_data) * 100
    print(f"\nPASS RATE (RELEVANT+PARTIAL): {pass_rate:.1f}%")
    print(f"STRICT PASS (RELEVANT only): {grades.get('RELEVANT', 0) / len(results_data) * 100:.1f}%")


def generate_report(results: list, total_time: float) -> str:
    """Generate comprehensive markdown report."""
    lines = []

    # ---- Header ----
    lines.append("# V4 Final Validation Report — Independent Audit")
    lines.append(f"\n**Date:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"**Total Queries:** {len(results)}")
    lines.append(f"**Total Time:** {total_time:.1f}s ({len(results)/total_time:.1f} queries/sec)")
    lines.append(f"**Engine Config:** top_k=5, use_reranker=False, expand_parents=False")
    lines.append(f"**Grading:** Top-3 results only, strict topic word-boundary matching")

    # ---- Executive Summary ----
    lines.append("\n## Executive Summary\n")
    grades = Counter(r["grade"] for r in results)
    total = len(results)
    avg_score = sum(r["grade_score"] for r in results) / total

    relevant = grades.get("RELEVANT", 0)
    partial = grades.get("PARTIAL", 0)
    irrelevant = grades.get("IRRELEVANT", 0)
    no_results = grades.get("NO_RESULTS", 0)
    pass_rate = (relevant + partial) / total * 100
    strict_pass = relevant / total * 100

    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| **RELEVANT** | {relevant} ({relevant/total*100:.1f}%) |")
    lines.append(f"| **PARTIAL** | {partial} ({partial/total*100:.1f}%) |")
    lines.append(f"| **IRRELEVANT** | {irrelevant} ({irrelevant/total*100:.1f}%) |")
    lines.append(f"| **NO_RESULTS** | {no_results} ({no_results/total*100:.1f}%) |")
    lines.append(f"| **Pass Rate (RELEVANT+PARTIAL)** | **{pass_rate:.1f}%** |")
    lines.append(f"| **Strict Pass (RELEVANT only)** | **{strict_pass:.1f}%** |")
    lines.append(f"| **Average Score (0-3)** | **{avg_score:.2f}** |")
    lines.append(f"| **Avg Query Time** | {sum(r['query_time_ms'] for r in results)/total:.0f}ms |")

    # Verdict box
    lines.append("\n### Verdict\n")
    if strict_pass >= 70:
        verdict = "✅ **PRODUCTION READY** — Strong performance across the board."
    elif pass_rate >= 80:
        verdict = "🟡 **CONDITIONALLY READY** — Good pass rate but strict relevance needs improvement."
    elif pass_rate >= 60:
        verdict = "🟠 **NEEDS WORK** — Acceptable for beta, but significant gaps remain."
    elif pass_rate >= 40:
        verdict = "🔴 **NOT READY** — Too many missed or irrelevant results for production use."
    else:
        verdict = "⛔ **FAILING** — Fundamental issues with retrieval quality."
    lines.append(verdict)

    # ---- Per-Category Breakdown ----
    lines.append("\n## Per-Category Breakdown\n")
    categories = defaultdict(list)
    for r in results:
        categories[r["category"]].append(r)

    lines.append("| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |")
    lines.append("|----------|-------|----------|---------|------------|------------|-----------|-----------|")
    for cat in sorted(categories.keys()):
        items = categories[cat]
        n = len(items)
        g = Counter(r["grade"] for r in items)
        pr = (g.get("RELEVANT", 0) + g.get("PARTIAL", 0)) / n * 100
        avg = sum(r["grade_score"] for r in items) / n
        lines.append(
            f"| {cat} | {n} | {g.get('RELEVANT',0)} | {g.get('PARTIAL',0)} | "
            f"{g.get('IRRELEVANT',0)} | {g.get('NO_RESULTS',0)} | {pr:.0f}% | {avg:.2f} |"
        )

    # ---- Per-Difficulty Breakdown ----
    lines.append("\n## Per-Difficulty Breakdown\n")
    difficulties = defaultdict(list)
    for r in results:
        difficulties[r["difficulty"]].append(r)

    lines.append("| Difficulty | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |")
    lines.append("|------------|-------|----------|---------|------------|------------|-----------|-----------|")
    for diff in ["easy", "medium", "hard"]:
        if diff not in difficulties:
            continue
        items = difficulties[diff]
        n = len(items)
        g = Counter(r["grade"] for r in items)
        pr = (g.get("RELEVANT", 0) + g.get("PARTIAL", 0)) / n * 100
        avg = sum(r["grade_score"] for r in items) / n
        lines.append(
            f"| {diff} | {n} | {g.get('RELEVANT',0)} | {g.get('PARTIAL',0)} | "
            f"{g.get('IRRELEVANT',0)} | {g.get('NO_RESULTS',0)} | {pr:.0f}% | {avg:.2f} |"
        )

    # ---- Intent Detection Stats ----
    lines.append("\n## Intent Detection Statistics\n")
    intents = defaultdict(list)
    for r in results:
        intents[r["detected_intent"]].append(r)

    lines.append("| Intent | Count | Relevant | Partial | Irrelevant | Pass Rate | Avg Score |")
    lines.append("|--------|-------|----------|---------|------------|-----------|-----------|")
    for intent in sorted(intents.keys(), key=lambda x: -len(intents[x])):
        items = intents[intent]
        n = len(items)
        g = Counter(r["grade"] for r in items)
        pr = (g.get("RELEVANT", 0) + g.get("PARTIAL", 0)) / n * 100
        avg = sum(r["grade_score"] for r in items) / n
        lines.append(
            f"| {intent} | {n} | {g.get('RELEVANT',0)} | {g.get('PARTIAL',0)} | "
            f"{g.get('IRRELEVANT',0)} | {pr:.0f}% | {avg:.2f} |"
        )

    # ---- Collection Distribution ----
    lines.append("\n## Collection Distribution in Results\n")
    lines.append("How often each collection appears in top-3 results:\n")
    col_counts = Counter()
    col_top1 = Counter()
    for r in results:
        for c in r.get("top3_collections", []):
            col_counts[c] += 1
        if r.get("top3_collections"):
            col_top1[r["top3_collections"][0]] += 1

    lines.append("| Collection | Appearances in Top-3 | #1 Result | % of Total Top-3 |")
    lines.append("|------------|---------------------|-----------|------------------|")
    total_top3 = sum(col_counts.values())
    for col, count in col_counts.most_common():
        pct = count / total_top3 * 100 if total_top3 > 0 else 0
        lines.append(f"| {col} | {count} | {col_top1.get(col, 0)} | {pct:.1f}% |")

    # ---- Collection Match Analysis ----
    lines.append("\n### Expected vs Actual Collection Match Rate\n")
    lines.append("How often the expected collection(s) appear in top-3:\n")

    expected_col_stats = defaultdict(lambda: {"expected": 0, "found": 0})
    for r in results:
        for c in r["expected_collections"]:
            expected_col_stats[c]["expected"] += 1
            if c in r.get("collections_found", []):
                expected_col_stats[c]["found"] += 1

    lines.append("| Expected Collection | Times Expected | Times Found in Top-3 | Hit Rate |")
    lines.append("|---------------------|---------------|---------------------|----------|")
    for col in sorted(expected_col_stats.keys()):
        stats = expected_col_stats[col]
        hr = stats["found"] / stats["expected"] * 100 if stats["expected"] > 0 else 0
        lines.append(f"| {col} | {stats['expected']} | {stats['found']} | {hr:.0f}% |")

    # ---- Top 20 Worst Queries ----
    lines.append("\n## Top 20 Worst Queries\n")
    lines.append("Sorted by grade (worst first), then by topic miss count:\n")

    # Sort: NO_RESULTS first, then IRRELEVANT, then PARTIAL with most missing topics
    worst = sorted(results, key=lambda r: (
        r["grade_score"],
        -len(r["topics_missing"]),
        -len(r["collections_missing"]),
    ))

    for idx, r in enumerate(worst[:20], 1):
        lines.append(f"### {idx}. Q{r['id']}: {r['question']}")
        lines.append(f"- **Grade:** {r['grade']}")
        lines.append(f"- **Category:** {r['category']} | **Difficulty:** {r['difficulty']}")
        lines.append(f"- **Detected Intent:** {r['detected_intent']}")
        lines.append(f"- **Expected Topics:** {r['expected_topics']}")
        lines.append(f"- **Topics Found:** {r['topics_found']}")
        lines.append(f"- **Topics Missing:** {r['topics_missing']}")
        lines.append(f"- **Expected Collections:** {r['expected_collections']}")
        lines.append(f"- **Actual Top-3 Collections:** {r['top3_collections']}")
        lines.append(f"- **Collections Found:** {r['collections_found']}")
        lines.append(f"- **Results Returned:** {r['num_results']}")

        # WHY it failed
        reasons = []
        if r["num_results"] == 0:
            reasons.append("Zero results returned — total retrieval failure")
        if r["topics_missing"]:
            reasons.append(f"Missing topics [{', '.join(r['topics_missing'])}] not found in top-3 result text")
        if r["collections_missing"] and not r["collections_found"]:
            reasons.append(f"Expected collections {r['collections_missing']} not in top-3 (got {r['top3_collections']})")
        if r["detected_intent"] not in ["debug", "reference", "how_to"]:
            reasons.append(f"Intent classified as '{r['detected_intent']}' — may have misrouted")

        # Check if results came from wrong collections entirely
        expected_set = set(r["expected_collections"])
        actual_set = set(r["top3_collections"])
        if expected_set and not expected_set.intersection(actual_set):
            reasons.append(f"Collection mismatch: expected {list(expected_set)} but got {list(actual_set)}")

        lines.append(f"- **WHY:** {' | '.join(reasons) if reasons else 'Low relevance in returned content'}")
        if r["top3_snippets"]:
            snippet = r["top3_snippets"][0][:150].replace('\n', ' ')
            lines.append(f"- **Top result snippet:** `{snippet}...`")
        lines.append("")

    # ---- Knowledge Gaps ----
    lines.append("\n## Identified Knowledge Gaps\n")
    lines.append("Topics that consistently fail across multiple queries:\n")

    # Aggregate missing topics
    missing_topic_counts = Counter()
    missing_topic_queries = defaultdict(list)
    for r in results:
        if r["grade"] in ("IRRELEVANT", "NO_RESULTS"):
            for t in r["topics_missing"]:
                missing_topic_counts[t] += 1
                missing_topic_queries[t].append(r["id"])

    if missing_topic_counts:
        lines.append("| Missing Topic | Fail Count | Example Query IDs |")
        lines.append("|---------------|------------|-------------------|")
        for topic, count in missing_topic_counts.most_common(25):
            examples = missing_topic_queries[topic][:5]
            lines.append(f"| {topic} | {count} | {examples} |")
    else:
        lines.append("No consistently missing topics found (good sign!).")

    # Category-level gaps
    lines.append("\n### Weakest Categories\n")
    cat_scores = {}
    for cat, items in categories.items():
        n = len(items)
        g = Counter(r["grade"] for r in items)
        pr = (g.get("RELEVANT", 0) + g.get("PARTIAL", 0)) / n * 100
        cat_scores[cat] = pr

    for cat in sorted(cat_scores, key=cat_scores.get):
        pr = cat_scores[cat]
        emoji = "🔴" if pr < 50 else "🟠" if pr < 70 else "🟡" if pr < 85 else "🟢"
        lines.append(f"- {emoji} **{cat}**: {pr:.0f}% pass rate")

    # ---- Collection Routing Issues ----
    lines.append("\n## Collection Routing Analysis\n")
    lines.append("Cases where the search routed to wrong collections:\n")

    routing_mismatches = 0
    routing_details = defaultdict(int)
    for r in results:
        if r["grade"] in ("IRRELEVANT", "NO_RESULTS"):
            expected = set(r["expected_collections"])
            actual = set(r["top3_collections"])
            if expected and not expected.intersection(actual):
                routing_mismatches += 1
                for e in expected:
                    for a in actual:
                        routing_details[f"{e} → {a}"] += 1

    lines.append(f"Total routing mismatches (expected not in top-3): **{routing_mismatches}** "
                 f"out of {irrelevant + no_results} failed queries")

    if routing_details:
        lines.append("\nMost common mis-routes:\n")
        lines.append("| Expected → Got | Count |")
        lines.append("|----------------|-------|")
        for route, count in sorted(routing_details.items(), key=lambda x: -x[1])[:15]:
            lines.append(f"| {route} | {count} |")

    # ---- Query Time Distribution ----
    lines.append("\n## Performance (Query Latency)\n")
    times = sorted(r["query_time_ms"] for r in results)
    lines.append(f"- **Min:** {times[0]:.0f}ms")
    lines.append(f"- **P50:** {times[len(times)//2]:.0f}ms")
    lines.append(f"- **P90:** {times[int(len(times)*0.9)]:.0f}ms")
    lines.append(f"- **P99:** {times[int(len(times)*0.99)]:.0f}ms")
    lines.append(f"- **Max:** {times[-1]:.0f}ms")
    lines.append(f"- **Mean:** {sum(times)/len(times):.0f}ms")

    # ---- Overall Verdict ----
    lines.append("\n## Overall Verdict\n")
    lines.append(f"### Score: {avg_score:.2f}/3.00 — Pass Rate: {pass_rate:.1f}%\n")
    lines.append(verdict)

    lines.append("\n### Strengths\n")
    strong_cats = [cat for cat, pr in cat_scores.items() if pr >= 80]
    if strong_cats:
        for cat in strong_cats:
            lines.append(f"- ✅ **{cat}** ({cat_scores[cat]:.0f}% pass rate)")
    else:
        lines.append("- No categories above 80% pass rate")

    lines.append("\n### Weaknesses\n")
    weak_cats = [cat for cat, pr in cat_scores.items() if pr < 60]
    if weak_cats:
        for cat in weak_cats:
            lines.append(f"- ❌ **{cat}** ({cat_scores[cat]:.0f}% pass rate)")
    else:
        lines.append("- No categories below 60% pass rate (encouraging)")

    lines.append("\n### Recommendations\n")
    recommendations = []

    if no_results > 0:
        recommendations.append(f"- Fix {no_results} queries returning zero results — these are complete retrieval failures")
    if routing_mismatches > 5:
        recommendations.append(f"- Improve collection routing — {routing_mismatches} queries went to completely wrong collections")

    # Check for intent distribution issues
    for intent, items in intents.items():
        n = len(items)
        g = Counter(r["grade"] for r in items)
        pr = (g.get("RELEVANT", 0) + g.get("PARTIAL", 0)) / n * 100
        if pr < 60 and n >= 10:
            recommendations.append(f"- Intent '{intent}' has only {pr:.0f}% pass rate ({n} queries) — review routing logic")

    if missing_topic_counts:
        top_missing = missing_topic_counts.most_common(3)
        recommendations.append(f"- Top missing topics: {', '.join(t for t, _ in top_missing)} — may need content enrichment")

    for weak_cat in weak_cats:
        recommendations.append(f"- Category '{weak_cat}' needs attention — may lack indexed content or have poor chunking")

    if pass_rate < 80:
        recommendations.append("- Consider enabling reranker for production (this test ran without it)")
    if pass_rate < 60:
        recommendations.append("- Fundamental retrieval quality issues — review embedding model, chunking strategy, and collection routing")

    if not recommendations:
        recommendations.append("- System performing well — consider fine-tuning edge cases")

    lines.append("\n".join(recommendations))

    lines.append("\n\n---\n*Report generated by validate_v4_final.py — independent, unbiased assessment*")

    return "\n".join(lines)


if __name__ == "__main__":
    run_validation()
