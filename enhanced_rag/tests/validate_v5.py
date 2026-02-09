#!/usr/bin/env python3
"""Run v5 validation with the new v3 engine. Fast — no sub-agent needed."""
import json, time, re, sys
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

print("Loading engine...", flush=True)
from search.engine import EnhancedSearchEngine, analyze_query

engine = EnhancedSearchEngine()
questions = json.load(open(Path(__file__).parent / "generated_questions.json"))

print(f"Running {len(questions)} queries (no reranker, no parent expansion)...", flush=True)

results = []
start = time.time()

for i, q in enumerate(questions):
    t0 = time.time()
    query = q["question"]
    analyzed = analyze_query(query)
    search_results = engine.search(query, top_k=5, use_reranker=False, expand_parents=False)
    elapsed = time.time() - t0
    
    # Extract top-3 info
    top3 = search_results[:3]
    top3_collections = [r.collection for r in top3]
    top3_texts = [r.text[:200] for r in top3]
    top3_scores = [r.score for r in top3]
    
    # Grade: topic matching in top-3 text
    combined_text = " ".join(t.lower() for t in [r.text for r in top3])
    expected_topics = q["expected_topics"]
    expected_collections = q["expected_collections"]
    
    topics_found = []
    for topic in expected_topics:
        # Word boundary matching
        pattern = r'\b' + re.escape(topic.lower()) + r'\b'
        if re.search(pattern, combined_text):
            topics_found.append(topic)
    
    collections_found = [c for c in expected_collections if c in top3_collections]
    
    n_topics = len(topics_found)
    n_expected_topics = len(expected_topics)
    has_collection = len(collections_found) > 0
    
    # Grading rules
    if len(search_results) == 0:
        grade = "NO_RESULTS"
        score = 0
    elif n_topics >= 3 and has_collection:
        grade = "RELEVANT"
        score = 3
    elif n_topics >= 2 or has_collection:
        grade = "PARTIAL"
        score = 2
    else:
        grade = "IRRELEVANT"
        score = 1
    
    result = {
        "id": q["id"],
        "question": query,
        "category": q["category"],
        "difficulty": q["difficulty"],
        "expected_topics": expected_topics,
        "expected_collections": expected_collections,
        "detected_intent": analyzed.intent,
        "entity_boost": getattr(analyzed, 'entity_boost_applied', ''),
        "collection_weights": {k: round(v, 2) for k, v in analyzed.collection_weights.items()},
        "num_results": len(search_results),
        "top3_collections": top3_collections,
        "top3_scores": [round(s, 4) for s in top3_scores],
        "topics_found": topics_found,
        "topics_found_count": n_topics,
        "collections_found": collections_found,
        "grade": grade,
        "score": score,
        "query_time_ms": round(elapsed * 1000),
    }
    results.append(result)
    
    if (i + 1) % 50 == 0:
        elapsed_total = time.time() - start
        print(f"  {i+1}/300 ({elapsed_total:.0f}s)", flush=True)

total_time = time.time() - start

# Save results
out_path = Path(__file__).parent / "v5_results.json"
out_path.write_text(json.dumps(results, indent=2))

# === Generate report ===
grades = Counter(r["grade"] for r in results)
scores = [r["score"] for r in results]
avg_score = sum(scores) / len(scores)

print(f"\n{'='*60}")
print(f"V5 VALIDATION COMPLETE — {total_time:.0f}s")
print(f"{'='*60}")
print(f"RELEVANT:   {grades['RELEVANT']:3d} ({grades['RELEVANT']/3:.1f}%)")
print(f"PARTIAL:    {grades['PARTIAL']:3d} ({grades['PARTIAL']/3:.1f}%)")
print(f"IRRELEVANT: {grades['IRRELEVANT']:3d} ({grades['IRRELEVANT']/3:.1f}%)")
print(f"NO_RESULTS: {grades['NO_RESULTS']:3d}")
print(f"Pass Rate:  {(grades['RELEVANT']+grades['PARTIAL'])/3:.1f}%")
print(f"Strict:     {grades['RELEVANT']/3:.1f}%")
print(f"Avg Score:  {avg_score:.2f}/3.00")

# Per-category
print(f"\n{'='*60}")
print("PER CATEGORY:")
cats = sorted(set(r["category"] for r in results))
for cat in cats:
    cat_results = [r for r in results if r["category"] == cat]
    cat_grades = Counter(r["grade"] for r in cat_results)
    n = len(cat_results)
    pass_rate = (cat_grades["RELEVANT"] + cat_grades["PARTIAL"]) / n * 100
    strict_rate = cat_grades["RELEVANT"] / n * 100
    avg = sum(r["score"] for r in cat_results) / n
    print(f"  {cat:25s}: {n:2d}q | Pass:{pass_rate:5.1f}% | Strict:{strict_rate:5.1f}% | Avg:{avg:.2f} | "
          f"R:{cat_grades['RELEVANT']} P:{cat_grades['PARTIAL']} I:{cat_grades['IRRELEVANT']}")

# Collection distribution
print(f"\n{'='*60}")
print("COLLECTION DISTRIBUTION (top-3):")
col_dist = Counter()
for r in results:
    for c in r["top3_collections"]:
        col_dist[c] += 1
total_slots = sum(col_dist.values())
for col, count in col_dist.most_common():
    print(f"  {col:25s}: {count:4d} ({count/total_slots*100:.1f}%)")

# Expected vs actual hit rate
print(f"\nEXPECTED COLLECTION HIT RATE:")
expected_counts = Counter()
expected_hits = Counter()
for r in results:
    for ec in r["expected_collections"]:
        expected_counts[ec] += 1
        if ec in r["top3_collections"]:
            expected_hits[ec] += 1
for col in sorted(expected_counts.keys()):
    rate = expected_hits[col] / expected_counts[col] * 100
    print(f"  {col:25s}: {expected_hits[col]:3d}/{expected_counts[col]:3d} ({rate:.0f}%)")

# IRRELEVANT details
irrelevant = [r for r in results if r["grade"] == "IRRELEVANT"]
if irrelevant:
    print(f"\n{'='*60}")
    print(f"IRRELEVANT QUERIES ({len(irrelevant)}):")
    for r in irrelevant:
        print(f"  Q{r['id']}: {r['question']}")
        print(f"    Intent: {r['detected_intent']} | Expected: {r['expected_collections']} | Got: {r['top3_collections']}")
        print(f"    Topics found: {r['topics_found']} / {r['expected_topics']}")
        if r['entity_boost']:
            print(f"    Boosts: {r['entity_boost']}")
        print()

print(f"\nResults saved to {out_path}")
