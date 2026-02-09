#!/usr/bin/env python3
"""Phase 5: Scrape top Shopify questions from Stack Overflow and community knowledge"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json
import time
from pathlib import Path

RAW_DOCS = Path(__file__).parent.parent / "raw-docs"
COMMUNITY_DIR = RAW_DOCS / "community"
COMMUNITY_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def scrape_stackoverflow():
    """Scrape top Shopify-tagged SO questions via API"""
    print("📚 Fetching top Stack Overflow Shopify questions...")
    
    tags = [
        "shopify", "shopify-liquid", "shopify-api", 
        "shopify-app", "shopify-theme", "shopify-hydrogen"
    ]
    
    all_questions = []
    
    for tag in tags:
        url = f"https://api.stackexchange.com/2.3/questions"
        params = {
            "order": "desc",
            "sort": "votes",
            "tagged": tag,
            "site": "stackoverflow",
            "pagesize": 50,
            "filter": "withbody",
        }
        
        try:
            resp = requests.get(url, params=params, timeout=30)
            data = resp.json()
            questions = data.get("items", [])
            print(f"  📥 {tag}: {len(questions)} questions")
            
            for q in questions:
                all_questions.append({
                    "title": q.get("title", ""),
                    "body": q.get("body", ""),
                    "score": q.get("score", 0),
                    "tags": q.get("tags", []),
                    "link": q.get("link", ""),
                    "answer_count": q.get("answer_count", 0),
                    "is_answered": q.get("is_answered", False),
                })
            
            time.sleep(1)  # Rate limit
        except Exception as e:
            print(f"  ❌ Failed {tag}: {e}")
    
    # Deduplicate by link
    seen = set()
    unique = []
    for q in all_questions:
        if q["link"] not in seen:
            seen.add(q["link"])
            unique.append(q)
    
    # Sort by score
    unique.sort(key=lambda x: x["score"], reverse=True)
    
    # Save as markdown
    output = "---\nsource: Stack Overflow - Top Shopify Questions\n---\n\n"
    output += "# Top Shopify Questions from Stack Overflow\n\n"
    
    for i, q in enumerate(unique[:200], 1):
        output += f"## {i}. {q['title']}\n"
        output += f"**Score:** {q['score']} | **Tags:** {', '.join(q['tags'])} | **Answered:** {q['is_answered']}\n"
        output += f"**Link:** {q['link']}\n\n"
        # Convert HTML body to markdown
        body_md = md(q["body"], heading_style="ATX") if q["body"] else ""
        output += body_md + "\n\n---\n\n"
    
    outfile = COMMUNITY_DIR / "stackoverflow_top_shopify.md"
    outfile.write_text(output, encoding="utf-8")
    print(f"  ✅ Saved {len(unique)} unique questions ({len(output)} chars)")
    
    # Also fetch top answers for the highest voted questions
    print("\n📚 Fetching top answers...")
    answers_output = "---\nsource: Stack Overflow - Top Shopify Answers\n---\n\n"
    answers_output += "# Top Shopify Answers from Stack Overflow\n\n"
    
    for q in unique[:50]:  # Top 50 questions
        qid = q["link"].split("/questions/")[1].split("/")[0] if "/questions/" in q["link"] else None
        if not qid:
            continue
        
        try:
            url = f"https://api.stackexchange.com/2.3/questions/{qid}/answers"
            params = {
                "order": "desc",
                "sort": "votes",
                "site": "stackoverflow",
                "filter": "withbody",
            }
            resp = requests.get(url, params=params, timeout=30)
            data = resp.json()
            answers = data.get("items", [])
            
            if answers:
                answers_output += f"## Q: {q['title']}\n"
                answers_output += f"**Score:** {q['score']} | {q['link']}\n\n"
                
                for a in answers[:2]:  # Top 2 answers per question
                    body_md = md(a.get("body", ""), heading_style="ATX")
                    answers_output += f"### Answer (Score: {a.get('score', 0)}, Accepted: {a.get('is_accepted', False)})\n"
                    answers_output += body_md + "\n\n"
                
                answers_output += "---\n\n"
            
            time.sleep(0.5)
        except Exception as e:
            print(f"  ⚠️  Failed answers for {qid}: {e}")
            continue
    
    outfile = COMMUNITY_DIR / "stackoverflow_top_answers.md"
    outfile.write_text(answers_output, encoding="utf-8")
    print(f"  ✅ Saved top answers ({len(answers_output)} chars)")


def scrape_polaris():
    """Scrape Shopify Polaris component docs"""
    print("\n📚 Scraping Polaris design system...")
    polaris_dir = RAW_DOCS / "polaris-docs"
    polaris_dir.mkdir(parents=True, exist_ok=True)
    
    # Core Polaris pages
    components = [
        "layout-and-structure/page", "layout-and-structure/card", 
        "layout-and-structure/layout", "layout-and-structure/box",
        "layout-and-structure/inline-stack", "layout-and-structure/block-stack",
        "layout-and-structure/divider", "layout-and-structure/bleed",
        "actions/button", "actions/button-group",
        "selection-and-input/text-field", "selection-and-input/select",
        "selection-and-input/checkbox", "selection-and-input/radio-button",
        "selection-and-input/choice-list", "selection-and-input/date-picker",
        "selection-and-input/drop-zone", "selection-and-input/filters",
        "tables/data-table", "tables/index-table",
        "lists/list", "lists/listbox", "lists/resource-list", "lists/resource-item",
        "navigation/navigation", "navigation/tabs", "navigation/pagination",
        "navigation/link", "navigation/top-bar",
        "overlays/modal", "overlays/popover", "overlays/tooltip",
        "feedback-indicators/banner", "feedback-indicators/badge",
        "feedback-indicators/toast", "feedback-indicators/spinner",
        "feedback-indicators/skeleton-body-text", "feedback-indicators/progress-bar",
        "typography/text",
        "images-and-icons/icon", "images-and-icons/thumbnail", "images-and-icons/avatar",
    ]
    
    base_url = "https://polaris.shopify.com/components"
    count = 0
    
    for comp in components:
        url = f"{base_url}/{comp}"
        filename = comp.replace("/", "_") + ".md"
        outfile = polaris_dir / filename
        
        if outfile.exists() and outfile.stat().st_size > 100:
            count += 1
            continue
        
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                for tag in soup.find_all(["nav", "header", "footer", "aside"]):
                    tag.decompose()
                main = soup.find("main") or soup.find("article") or soup.find("body")
                if main:
                    content = f"---\nsource: {url}\n---\n\n" + md(str(main), heading_style="ATX").strip()
                    outfile.write_text(content, encoding="utf-8")
                    count += 1
                    print(f"  ✅ {comp}")
            else:
                print(f"  ❌ {comp}: {resp.status_code}")
        except Exception as e:
            print(f"  ❌ {comp}: {e}")
        
        time.sleep(0.3)
    
    print(f"  📊 Polaris: {count}/{len(components)} components")


def main():
    print("🚀 Phase 5: Community Knowledge + Polaris\n")
    scrape_stackoverflow()
    scrape_polaris()
    print("\n✅ Phase 5 complete!")


if __name__ == "__main__":
    main()
