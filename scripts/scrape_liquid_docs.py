#!/usr/bin/env python3
"""Scrape Shopify Liquid documentation from shopify.dev"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json
import os
import time
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://shopify.dev"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

RAW_DOCS = Path(__file__).parent.parent / "raw-docs"

# Liquid documentation pages to scrape
LIQUID_PAGES = {
    "liquid-docs": [
        "/docs/api/liquid",
        "/docs/api/liquid/basics",
        "/docs/api/liquid/basics/types",
        "/docs/api/liquid/basics/operators",
        "/docs/api/liquid/basics/truthy-and-falsy",
        "/docs/api/liquid/basics/whitespace",
        "/docs/api/liquid/basics/handle",
    ],
    "liquid-objects": [
        "/docs/api/liquid/objects",
        "/docs/api/liquid/objects/product",
        "/docs/api/liquid/objects/collection",
        "/docs/api/liquid/objects/cart",
        "/docs/api/liquid/objects/shop",
        "/docs/api/liquid/objects/customer",
        "/docs/api/liquid/objects/order",
        "/docs/api/liquid/objects/variant",
        "/docs/api/liquid/objects/image",
        "/docs/api/liquid/objects/metafield",
        "/docs/api/liquid/objects/page",
        "/docs/api/liquid/objects/blog",
        "/docs/api/liquid/objects/article",
        "/docs/api/liquid/objects/comment",
        "/docs/api/liquid/objects/link",
        "/docs/api/liquid/objects/linklist",
        "/docs/api/liquid/objects/section",
        "/docs/api/liquid/objects/block",
        "/docs/api/liquid/objects/settings",
        "/docs/api/liquid/objects/template",
        "/docs/api/liquid/objects/theme",
        "/docs/api/liquid/objects/request",
        "/docs/api/liquid/objects/content_for_header",
        "/docs/api/liquid/objects/content_for_layout",
        "/docs/api/liquid/objects/form",
        "/docs/api/liquid/objects/paginate",
        "/docs/api/liquid/objects/search",
        "/docs/api/liquid/objects/tablerow",
        "/docs/api/liquid/objects/forloop",
        "/docs/api/liquid/objects/address",
        "/docs/api/liquid/objects/company",
        "/docs/api/liquid/objects/company_address",
        "/docs/api/liquid/objects/company_location",
        "/docs/api/liquid/objects/discount",
        "/docs/api/liquid/objects/discount_allocation",
        "/docs/api/liquid/objects/discount_application",
        "/docs/api/liquid/objects/fulfillment",
        "/docs/api/liquid/objects/gift_card",
        "/docs/api/liquid/objects/line_item",
        "/docs/api/liquid/objects/money",
        "/docs/api/liquid/objects/policy",
        "/docs/api/liquid/objects/shipping_method",
        "/docs/api/liquid/objects/store_availability",
        "/docs/api/liquid/objects/tax_line",
        "/docs/api/liquid/objects/transaction",
        "/docs/api/liquid/objects/unit_price_measurement",
        "/docs/api/liquid/objects/video",
        "/docs/api/liquid/objects/video_source",
        "/docs/api/liquid/objects/media",
        "/docs/api/liquid/objects/model",
        "/docs/api/liquid/objects/model_source",
        "/docs/api/liquid/objects/predictive_search",
        "/docs/api/liquid/objects/recommendations",
        "/docs/api/liquid/objects/color",
        "/docs/api/liquid/objects/font",
        "/docs/api/liquid/objects/filter",
        "/docs/api/liquid/objects/filter_value",
        "/docs/api/liquid/objects/country",
        "/docs/api/liquid/objects/currency",
        "/docs/api/liquid/objects/locale",
        "/docs/api/liquid/objects/market",
        "/docs/api/liquid/objects/selling_plan",
        "/docs/api/liquid/objects/selling_plan_allocation",
        "/docs/api/liquid/objects/selling_plan_group",
        "/docs/api/liquid/objects/quantity_rule",
    ],
    "liquid-filters-tags": [
        "/docs/api/liquid/filters",
        "/docs/api/liquid/filters/abs",
        "/docs/api/liquid/filters/append",
        "/docs/api/liquid/filters/at_least",
        "/docs/api/liquid/filters/at_most",
        "/docs/api/liquid/filters/capitalize",
        "/docs/api/liquid/filters/ceil",
        "/docs/api/liquid/filters/compact",
        "/docs/api/liquid/filters/concat",
        "/docs/api/liquid/filters/date",
        "/docs/api/liquid/filters/default",
        "/docs/api/liquid/filters/divided_by",
        "/docs/api/liquid/filters/downcase",
        "/docs/api/liquid/filters/escape",
        "/docs/api/liquid/filters/escape_once",
        "/docs/api/liquid/filters/first",
        "/docs/api/liquid/filters/floor",
        "/docs/api/liquid/filters/join",
        "/docs/api/liquid/filters/json",
        "/docs/api/liquid/filters/last",
        "/docs/api/liquid/filters/lstrip",
        "/docs/api/liquid/filters/map",
        "/docs/api/liquid/filters/minus",
        "/docs/api/liquid/filters/modulo",
        "/docs/api/liquid/filters/newline_to_br",
        "/docs/api/liquid/filters/plus",
        "/docs/api/liquid/filters/prepend",
        "/docs/api/liquid/filters/remove",
        "/docs/api/liquid/filters/remove_first",
        "/docs/api/liquid/filters/replace",
        "/docs/api/liquid/filters/replace_first",
        "/docs/api/liquid/filters/reverse",
        "/docs/api/liquid/filters/round",
        "/docs/api/liquid/filters/rstrip",
        "/docs/api/liquid/filters/size",
        "/docs/api/liquid/filters/slice",
        "/docs/api/liquid/filters/sort",
        "/docs/api/liquid/filters/sort_natural",
        "/docs/api/liquid/filters/split",
        "/docs/api/liquid/filters/strip",
        "/docs/api/liquid/filters/strip_html",
        "/docs/api/liquid/filters/strip_newlines",
        "/docs/api/liquid/filters/times",
        "/docs/api/liquid/filters/truncate",
        "/docs/api/liquid/filters/truncatewords",
        "/docs/api/liquid/filters/uniq",
        "/docs/api/liquid/filters/upcase",
        "/docs/api/liquid/filters/url_decode",
        "/docs/api/liquid/filters/url_encode",
        "/docs/api/liquid/filters/where",
        # Shopify-specific filters
        "/docs/api/liquid/filters/asset_url",
        "/docs/api/liquid/filters/asset_img_url",
        "/docs/api/liquid/filters/img_url",
        "/docs/api/liquid/filters/image_url",
        "/docs/api/liquid/filters/image_tag",
        "/docs/api/liquid/filters/stylesheet_tag",
        "/docs/api/liquid/filters/script_tag",
        "/docs/api/liquid/filters/money",
        "/docs/api/liquid/filters/money_with_currency",
        "/docs/api/liquid/filters/money_without_trailing_zeros",
        "/docs/api/liquid/filters/money_without_currency",
        "/docs/api/liquid/filters/url_for_type",
        "/docs/api/liquid/filters/url_for_vendor",
        "/docs/api/liquid/filters/link_to",
        "/docs/api/liquid/filters/link_to_type",
        "/docs/api/liquid/filters/link_to_vendor",
        "/docs/api/liquid/filters/within",
        "/docs/api/liquid/filters/pluralize",
        "/docs/api/liquid/filters/customer_login_link",
        "/docs/api/liquid/filters/customer_logout_link",
        "/docs/api/liquid/filters/customer_register_link",
        "/docs/api/liquid/filters/payment_type_img_url",
        "/docs/api/liquid/filters/shopify_asset_url",
        "/docs/api/liquid/filters/global_asset_url",
        "/docs/api/liquid/filters/file_url",
        "/docs/api/liquid/filters/file_img_url",
        "/docs/api/liquid/filters/t",
        "/docs/api/liquid/filters/weight_with_unit",
        "/docs/api/liquid/filters/format_address",
        "/docs/api/liquid/filters/highlight",
        "/docs/api/liquid/filters/metafield_tag",
        "/docs/api/liquid/filters/metafield_text",
        "/docs/api/liquid/filters/external_video_tag",
        "/docs/api/liquid/filters/external_video_url",
        "/docs/api/liquid/filters/model_viewer_tag",
        "/docs/api/liquid/filters/video_tag",
        "/docs/api/liquid/filters/media_tag",
        "/docs/api/liquid/filters/color_to_rgb",
        "/docs/api/liquid/filters/color_to_hsl",
        "/docs/api/liquid/filters/color_to_hex",
        "/docs/api/liquid/filters/color_extract",
        "/docs/api/liquid/filters/color_brightness",
        "/docs/api/liquid/filters/color_modify",
        "/docs/api/liquid/filters/color_lighten",
        "/docs/api/liquid/filters/color_darken",
        "/docs/api/liquid/filters/color_saturate",
        "/docs/api/liquid/filters/color_desaturate",
        "/docs/api/liquid/filters/color_mix",
        "/docs/api/liquid/filters/color_difference",
        "/docs/api/liquid/filters/brightness_difference",
        "/docs/api/liquid/filters/color_contrast",
        "/docs/api/liquid/filters/font_modify",
        "/docs/api/liquid/filters/font_face",
        "/docs/api/liquid/filters/font_url",
        # Tags
        "/docs/api/liquid/tags",
        "/docs/api/liquid/tags/if",
        "/docs/api/liquid/tags/elsif",
        "/docs/api/liquid/tags/else",
        "/docs/api/liquid/tags/unless",
        "/docs/api/liquid/tags/case",
        "/docs/api/liquid/tags/for",
        "/docs/api/liquid/tags/break",
        "/docs/api/liquid/tags/continue",
        "/docs/api/liquid/tags/cycle",
        "/docs/api/liquid/tags/tablerow",
        "/docs/api/liquid/tags/assign",
        "/docs/api/liquid/tags/capture",
        "/docs/api/liquid/tags/increment",
        "/docs/api/liquid/tags/decrement",
        "/docs/api/liquid/tags/echo",
        "/docs/api/liquid/tags/liquid",
        "/docs/api/liquid/tags/raw",
        "/docs/api/liquid/tags/render",
        "/docs/api/liquid/tags/include",
        "/docs/api/liquid/tags/section",
        "/docs/api/liquid/tags/sections",
        "/docs/api/liquid/tags/layout",
        "/docs/api/liquid/tags/comment",
        "/docs/api/liquid/tags/form",
        "/docs/api/liquid/tags/paginate",
        "/docs/api/liquid/tags/style",
        "/docs/api/liquid/tags/javascript",
        "/docs/api/liquid/tags/schema",
    ],
}

# Theme development & best practices
THEME_PAGES = {
    "patterns-best-practices": [
        "/docs/themes",
        "/docs/themes/getting-started",
        "/docs/themes/architecture",
        "/docs/themes/architecture/layouts",
        "/docs/themes/architecture/templates",
        "/docs/themes/architecture/sections",
        "/docs/themes/architecture/blocks",
        "/docs/themes/architecture/config",
        "/docs/themes/architecture/locales",
        "/docs/themes/architecture/assets",
        "/docs/themes/architecture/snippets",
        "/docs/themes/best-practices",
        "/docs/themes/best-practices/performance",
        "/docs/themes/best-practices/responsive-design",
        "/docs/themes/tools/cli",
        "/docs/themes/pricing",
        "/docs/themes/store/requirements",
    ],
    "accessibility": [
        "/docs/themes/best-practices/accessibility",
    ],
    "json-schemas": [
        "/docs/themes/architecture/config/settings-schema",
        "/docs/themes/architecture/config/settings-data",
        "/docs/themes/architecture/sections/section-schema",
    ],
}


def fetch_page(url):
    """Fetch a page and return parsed content"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  ❌ Failed to fetch {url}: {e}")
        return None


def extract_content(html, url):
    """Extract main content from Shopify docs page"""
    soup = BeautifulSoup(html, "html.parser")

    # Remove nav, header, footer, sidebar
    for tag in soup.find_all(["nav", "header", "footer", "aside"]):
        tag.decompose()

    # Try to find main content area
    main = soup.find("main") or soup.find("article") or soup.find(
        "div", class_=lambda c: c and ("content" in c or "article" in c)
    )

    if not main:
        main = soup.find("body")

    if not main:
        return None

    # Convert to markdown
    content = md(str(main), heading_style="ATX", code_language="liquid")

    # Add metadata header
    header = f"---\nsource: {url}\n---\n\n"

    return header + content.strip()


def scrape_category(category, paths, base_dir):
    """Scrape all pages in a category"""
    output_dir = base_dir / category
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for path in paths:
        url = BASE_URL + path
        filename = path.strip("/").replace("/", "_") + ".md"
        output_file = output_dir / filename

        # Skip if already scraped
        if output_file.exists() and output_file.stat().st_size > 100:
            print(f"  ⏭️  Already exists: {filename}")
            results.append({"url": url, "file": str(output_file), "status": "cached"})
            continue

        print(f"  📥 Fetching: {path}")
        html = fetch_page(url)
        if html:
            content = extract_content(html, url)
            if content and len(content) > 50:
                output_file.write_text(content, encoding="utf-8")
                results.append(
                    {
                        "url": url,
                        "file": str(output_file),
                        "status": "ok",
                        "size": len(content),
                    }
                )
                print(f"  ✅ Saved: {filename} ({len(content)} chars)")
            else:
                results.append({"url": url, "file": str(output_file), "status": "empty"})
                print(f"  ⚠️  Empty content: {filename}")
        else:
            results.append({"url": url, "status": "failed"})

        time.sleep(0.5)  # Be polite

    return results


def main():
    print("🚀 Starting Shopify Liquid documentation scrape\n")

    all_results = {}

    # Scrape Liquid docs
    print("📚 Scraping Liquid documentation...")
    for category, paths in LIQUID_PAGES.items():
        print(f"\n📂 Category: {category} ({len(paths)} pages)")
        results = scrape_category(category, paths, RAW_DOCS)
        all_results[category] = results

    # Scrape theme docs
    print("\n📚 Scraping Theme documentation...")
    for category, paths in THEME_PAGES.items():
        print(f"\n📂 Category: {category} ({len(paths)} pages)")
        results = scrape_category(category, paths, RAW_DOCS)
        all_results[category] = results

    # Summary
    print("\n" + "=" * 60)
    print("📊 SCRAPE SUMMARY")
    print("=" * 60)
    total_ok = 0
    total_failed = 0
    total_cached = 0
    for cat, results in all_results.items():
        ok = sum(1 for r in results if r["status"] == "ok")
        failed = sum(1 for r in results if r["status"] == "failed")
        cached = sum(1 for r in results if r["status"] == "cached")
        empty = sum(1 for r in results if r["status"] == "empty")
        total_ok += ok
        total_failed += failed
        total_cached += cached
        print(f"  {cat}: ✅{ok} ⏭️{cached} ⚠️{empty} ❌{failed}")

    print(f"\nTotal: ✅{total_ok} new | ⏭️{total_cached} cached | ❌{total_failed} failed")

    # Save manifest
    manifest_path = RAW_DOCS / "scrape_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n📋 Manifest saved to: {manifest_path}")


if __name__ == "__main__":
    main()
