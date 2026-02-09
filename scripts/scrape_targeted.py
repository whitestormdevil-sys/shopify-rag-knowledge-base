#!/usr/bin/env python3
"""Targeted scrape for weak RAG topics — fills knowledge gaps identified in 218-query test."""

import os
import re
import time
import json
import hashlib
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

RAW_DOCS = Path(__file__).parent.parent / "raw-docs"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

# === TARGETED URLS FOR WEAK TOPICS ===

TARGETS = {
    # Shopify Flow
    "flow-docs": [
        "https://shopify.dev/docs/apps/flow",
        "https://shopify.dev/docs/apps/flow/actions",
        "https://shopify.dev/docs/apps/flow/triggers",
        "https://shopify.dev/docs/apps/flow/conditions",
        "https://shopify.dev/docs/apps/flow/actions/create-action",
        "https://shopify.dev/docs/apps/flow/triggers/create-trigger",
        "https://shopify.dev/docs/apps/flow/reference",
        "https://shopify.dev/docs/apps/flow/migrate",
    ],
    
    # Shopify Pixels & Customer Events
    "pixels-analytics": [
        "https://shopify.dev/docs/api/web-pixels-api",
        "https://shopify.dev/docs/api/web-pixels-api/standard-events",
        "https://shopify.dev/docs/api/web-pixels-api/pixel-events",
        "https://shopify.dev/docs/api/web-pixels-api/emitting-data",
        "https://shopify.dev/docs/apps/marketing/pixels",
        "https://shopify.dev/docs/apps/marketing/pixels/getting-started",
        "https://shopify.dev/docs/api/customer-events",
        "https://shopify.dev/docs/apps/marketing",
    ],
    
    # Subscription APIs
    "subscriptions-docs": [
        "https://shopify.dev/docs/apps/selling-strategies/subscriptions",
        "https://shopify.dev/docs/apps/selling-strategies/subscriptions/getting-started",
        "https://shopify.dev/docs/apps/selling-strategies/subscriptions/modeling",
        "https://shopify.dev/docs/apps/selling-strategies/subscriptions/contracts",
        "https://shopify.dev/docs/apps/selling-strategies/purchase-options/deferred",
        "https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan",
        "https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlanGroup",
        "https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionContract",
    ],
    
    # Markets & Internationalization
    "markets-i18n": [
        "https://shopify.dev/docs/apps/markets",
        "https://shopify.dev/docs/apps/markets/overview",
        "https://shopify.dev/docs/apps/markets/currency",
        "https://shopify.dev/docs/apps/markets/localization",
        "https://shopify.dev/docs/themes/markets",
        "https://shopify.dev/docs/themes/markets/multiple-currencies-languages",
        "https://shopify.dev/docs/api/liquid/objects/localization",
        "https://shopify.dev/docs/api/liquid/objects/market",
        "https://shopify.dev/docs/api/liquid/objects/country",
        "https://shopify.dev/docs/api/liquid/objects/currency",
    ],
    
    # Theme App Extensions (deeper)
    "theme-app-ext": [
        "https://shopify.dev/docs/apps/online-store/theme-app-extensions",
        "https://shopify.dev/docs/apps/online-store/theme-app-extensions/getting-started",
        "https://shopify.dev/docs/apps/online-store/theme-app-extensions/configuration",
        "https://shopify.dev/docs/apps/online-store/theme-app-extensions/extensions-framework",
        "https://shopify.dev/docs/apps/online-store/app-blocks",
        "https://shopify.dev/docs/apps/online-store/theme-app-extensions/best-practices",
    ],
    
    # Section Groups & Online Store 2.0
    "os2-sections": [
        "https://shopify.dev/docs/themes/architecture/section-groups",
        "https://shopify.dev/docs/themes/architecture/sections",
        "https://shopify.dev/docs/themes/architecture/templates",
        "https://shopify.dev/docs/themes/architecture/layouts",
        "https://shopify.dev/docs/themes/architecture/config",
        "https://shopify.dev/docs/themes/architecture",
        "https://shopify.dev/docs/themes/getting-started/customize",
        "https://shopify.dev/docs/themes/tools/online-editor",
    ],
    
    # Authentication & OAuth
    "auth-oauth": [
        "https://shopify.dev/docs/apps/build/authentication-authorization",
        "https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens",
        "https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens",
        "https://shopify.dev/docs/apps/build/authentication-authorization/client-secret",
        "https://shopify.dev/docs/api/admin-rest/latest/resources/access-scope",
    ],
    
    # Ajax Cart API (specific endpoints)
    "ajax-cart-api": [
        "https://shopify.dev/docs/api/ajax/reference/cart",
        "https://shopify.dev/docs/api/ajax/reference/product",
        "https://shopify.dev/docs/api/ajax/reference/product-recommendations",
        "https://shopify.dev/docs/api/ajax",
        "https://shopify.dev/docs/api/ajax/reference",
    ],
    
    # Performance & Best Practices
    "perf-best-practices": [
        "https://shopify.dev/docs/themes/best-practices/performance",
        "https://shopify.dev/docs/themes/best-practices/performance/lazy-loading",
        "https://shopify.dev/docs/themes/best-practices/performance/platform",
        "https://shopify.dev/docs/themes/best-practices",
        "https://shopify.dev/docs/themes/best-practices/accessibility",
        "https://shopify.dev/docs/themes/best-practices/seo",
        "https://shopify.dev/docs/themes/store/requirements",
    ],
    
    # CSS & Styling patterns (from Dawn source + docs)
    "css-styling": [
        "https://shopify.dev/docs/themes/best-practices/performance/css",
        "https://shopify.dev/docs/themes/architecture/assets",
        "https://shopify.dev/docs/themes/pricing",
        "https://shopify.dev/docs/api/liquid/tags/style",
        "https://shopify.dev/docs/api/liquid/tags/javascript",
    ],
    
    # Online Store Editor API
    "editor-api": [
        "https://shopify.dev/docs/themes/tools/online-editor",
        "https://shopify.dev/docs/themes/architecture/sections/section-schema",
        "https://shopify.dev/docs/themes/architecture/sections/section-schema/input-settings",
        "https://shopify.dev/docs/themes/architecture/sections/section-schema/sidebar-settings",
        "https://shopify.dev/docs/themes/architecture/config/settings-schema",
    ],
}


def scrape_page(url: str, retries: int = 2) -> str:
    """Fetch and convert a page to markdown."""
    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            if resp.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            if resp.status_code != 200:
                return ""
            
            soup = BeautifulSoup(resp.text, "html.parser")
            
            # Remove nav, footer, scripts
            for tag in soup.find_all(["nav", "footer", "script", "style", "header"]):
                tag.decompose()
            
            # Try to find main content
            main = (soup.find("main") or soup.find("article") or 
                    soup.find(class_=re.compile(r"content|article|docs")) or soup.body)
            
            if not main:
                return ""
            
            markdown = md(str(main), heading_style="ATX", code_language="liquid")
            
            # Add frontmatter
            frontmatter = f"---\nsource: {url}\n---\n\n"
            return frontmatter + markdown.strip()
            
        except Exception as e:
            if attempt < retries:
                time.sleep(2)
            continue
    return ""


def main():
    print("=" * 60)
    print("  TARGETED SCRAPE — Filling RAG Knowledge Gaps")
    print("=" * 60)
    
    total_scraped = 0
    total_failed = 0
    results = {}
    
    for category, urls in TARGETS.items():
        cat_dir = RAW_DOCS / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        
        scraped = 0
        failed = 0
        
        print(f"\n📂 {category} ({len(urls)} URLs)")
        
        for url in urls:
            # Generate filename from URL
            slug = url.replace("https://shopify.dev/", "").replace("/", "_")
            filename = f"{slug}.md"
            filepath = cat_dir / filename
            
            # Skip if already exists and has content
            if filepath.exists() and filepath.stat().st_size > 500:
                print(f"  ⏭️  {filename[:60]} (exists)")
                scraped += 1
                continue
            
            content = scrape_page(url)
            
            if content and len(content) > 200:
                filepath.write_text(content, encoding="utf-8")
                print(f"  ✅ {filename[:60]} ({len(content):,} chars)")
                scraped += 1
                time.sleep(0.5)  # Be nice
            else:
                print(f"  ❌ {filename[:60]} (empty/failed)")
                failed += 1
                time.sleep(1)
        
        total_scraped += scraped
        total_failed += failed
        results[category] = {"scraped": scraped, "failed": failed, "total": len(urls)}
    
    print("\n" + "=" * 60)
    print(f"  ✅ SCRAPING COMPLETE")
    print(f"  Scraped: {total_scraped} | Failed: {total_failed}")
    print("=" * 60)
    
    # Save results
    results_path = RAW_DOCS / "targeted_scrape_results.json"
    results_path.write_text(json.dumps(results, indent=2))
    print(f"\n📋 Results: {results_path}")


if __name__ == "__main__":
    main()
