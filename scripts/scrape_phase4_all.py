#!/usr/bin/env python3
"""Phase 4: Scrape ALL remaining Shopify docs - Ajax API, Section Rendering, 
Metaobjects, Customer Events, Web Pixels, Bulk Ops, Multipass, Markets, Flow,
App Proxy, SEO, Performance, CDN, B2B, Payments, Reviews, Migrations, POS, Email"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json
import time
from pathlib import Path

BASE_URL = "https://shopify.dev"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}
RAW_DOCS = Path(__file__).parent.parent / "raw-docs"


def fetch_page(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  ❌ {url}: {e}")
        return None


def extract_content(html, url):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["nav", "header", "footer", "aside"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.find(
        "div", class_=lambda c: c and ("content" in c or "article" in c)
    )
    if not main:
        main = soup.find("body")
    if not main:
        return None
    content = md(str(main), heading_style="ATX", code_language="liquid")
    return f"---\nsource: {url}\n---\n\n" + content.strip()


def scrape_category(category, paths):
    output_dir = RAW_DOCS / category
    output_dir.mkdir(parents=True, exist_ok=True)
    stats = {"ok": 0, "cached": 0, "failed": 0, "empty": 0}
    
    for path in paths:
        if path.startswith("http"):
            url = path
            filename = path.split("//")[1].replace("/", "_") + ".md"
        else:
            url = BASE_URL + path
            filename = path.strip("/").replace("/", "_") + ".md"
        
        output_file = output_dir / filename
        
        if output_file.exists() and output_file.stat().st_size > 100:
            stats["cached"] += 1
            continue
        
        html = fetch_page(url)
        if html:
            content = extract_content(html, url)
            if content and len(content) > 50:
                output_file.write_text(content, encoding="utf-8")
                stats["ok"] += 1
                print(f"  ✅ {filename[:60]} ({len(content)} chars)")
            else:
                stats["empty"] += 1
        else:
            stats["failed"] += 1
        time.sleep(0.3)
    
    return stats


# ==========================================
# ALL REMAINING CATEGORIES
# ==========================================

CATEGORIES = {
    # ---- CRITICAL: Ajax API & Section Rendering ----
    "ajax-api": [
        "/docs/api/ajax",
        "/docs/api/ajax/reference/cart",
        "/docs/api/ajax/reference/product",
        "/docs/api/ajax/reference/product-recommendations",
        "/docs/api/ajax/reference/predictive-search",
        "/docs/api/ajax/reference/section-rendering",
        "/docs/api/ajax/input-examples",
    ],
    
    # ---- CRITICAL: Metaobjects ----
    "metaobjects": [
        "/docs/apps/build/custom-data",
        "/docs/apps/build/custom-data/metafields",
        "/docs/apps/build/custom-data/metafields/definitions",
        "/docs/apps/build/custom-data/metafields/types",
        "/docs/apps/build/custom-data/metafields/manage-values",
        "/docs/apps/build/custom-data/metafields/access-metafields",
        "/docs/apps/build/custom-data/metaobjects",
        "/docs/apps/build/custom-data/metaobjects/getting-started",
        "/docs/apps/build/custom-data/metaobjects/manage-metaobjects",
        "/docs/apps/build/custom-data/metaobjects/access-metaobjects",
        "/docs/api/admin-graphql/2024-10/queries/metaobjects",
        "/docs/api/admin-graphql/2024-10/queries/metaobjectDefinitions",
        "/docs/api/admin-graphql/2024-10/mutations/metaobjectCreate",
        "/docs/api/admin-graphql/2024-10/mutations/metaobjectUpdate",
        "/docs/api/admin-graphql/2024-10/mutations/metaobjectDefinitionCreate",
    ],
    
    # ---- CRITICAL: Customer Events & Web Pixels ----
    "customer-events": [
        "/docs/api/customer-events",
        "/docs/api/customer-events/getting-started",
        "/docs/api/customer-events/reference",
        "/docs/api/customer-events/components",
        "/docs/api/web-pixels-api",
        "/docs/api/web-pixels-api/getting-started",
        "/docs/api/web-pixels-api/standard-events",
        "/docs/api/web-pixels-api/pixel-extension",
        "/docs/apps/build/marketing/pixels",
        "/docs/apps/build/marketing/pixels/getting-started",
    ],
    
    # ---- CRITICAL: Bulk Operations ----
    "bulk-operations": [
        "/docs/api/usage/bulk-operations",
        "/docs/api/usage/bulk-operations/queries",
        "/docs/api/usage/bulk-operations/mutations",
        "/docs/api/usage/bulk-operations/imports",
        "/docs/api/usage/bulk-operations/exports",
    ],
    
    # ---- CRITICAL: Multipass ----
    "multipass": [
        "/docs/api/multipass",
    ],
    
    # ---- CRITICAL: Markets (International) ----
    "markets": [
        "/docs/apps/build/markets",
        "/docs/apps/build/markets/currencies",
        "/docs/apps/build/markets/languages",
        "/docs/apps/build/markets/pricing",
        "/docs/themes/markets",
        "/docs/themes/markets/multiple-currencies-languages",
        "/docs/themes/markets/country-language-selection",
        "/docs/themes/markets/support-multiple-currencies",
        "/docs/api/liquid/objects/localization",
        "/docs/api/liquid/objects/market",
        "/docs/api/liquid/objects/country",
        "/docs/api/liquid/objects/currency",
    ],
    
    # ---- CRITICAL: Shopify Flow ----
    "flow": [
        "/docs/apps/build/flow",
        "/docs/apps/build/flow/actions",
        "/docs/apps/build/flow/triggers",
        "/docs/apps/build/flow/actions/build-actions",
        "/docs/apps/build/flow/triggers/build-triggers",
    ],
    
    # ---- IMPORTANT: App Proxy ----
    "app-proxy": [
        "/docs/apps/build/online-store/app-proxies",
        "/docs/apps/build/online-store/app-proxies/getting-started",
    ],
    
    # ---- IMPORTANT: Theme Patterns ----
    "theme-patterns": [
        "/docs/themes/product-merchandising/media",
        "/docs/themes/product-merchandising/media/images",
        "/docs/themes/product-merchandising/media/video",
        "/docs/themes/product-merchandising/media/3d-models",
        "/docs/themes/product-merchandising/variants",
        "/docs/themes/product-merchandising/recommendations",
        "/docs/themes/navigation-search",
        "/docs/themes/navigation-search/search",
        "/docs/themes/navigation-search/filtering",
        "/docs/themes/navigation-search/pagination",
        "/docs/themes/cart-checkout",
        "/docs/themes/cart-checkout/cart",
        "/docs/themes/cart-checkout/additional-scripts",
        "/docs/themes/customer-engagement",
        "/docs/themes/customer-engagement/customers",
        "/docs/themes/customer-engagement/social-media",
        "/docs/themes/trust-security",
        "/docs/themes/trust-security/cookies",
        "/docs/themes/trust-security/content-security-policy",
        "/docs/themes/pricing-payments",
        "/docs/themes/pricing-payments/prices",
        "/docs/themes/pricing-payments/purchase-options",
        "/docs/themes/pricing-payments/installments",
    ],
    
    # ---- IMPORTANT: SEO ----
    "seo": [
        "/docs/themes/seo",
        "/docs/themes/seo/seo-checklist",
        "/docs/themes/seo/schema-markup",
        "/docs/themes/seo/urls-and-redirects",
        "https://help.shopify.com/en/manual/promoting-marketing/seo",
    ],
    
    # ---- IMPORTANT: Performance ----
    "performance": [
        "/docs/themes/best-practices/performance",
        "/docs/themes/best-practices/performance/lazy-loading",
        "/docs/themes/best-practices/performance/reduce-javascript",
        "/docs/themes/best-practices/performance/optimize-images",
        "/docs/themes/best-practices/performance/optimize-fonts",
        "/docs/themes/best-practices/performance/storefront-performance",
        "/docs/themes/tools/lighthouse",
    ],
    
    # ---- IMPORTANT: CDN & Images ----
    "cdn-images": [
        "/docs/themes/best-practices/performance/optimize-images",
        "/docs/api/liquid/filters/image_url",
        "/docs/api/liquid/filters/image_tag",
        "/docs/api/liquid/objects/image",
    ],
    
    # ---- IMPORTANT: B2B ----
    "b2b": [
        "/docs/apps/build/b2b",
        "/docs/apps/build/b2b/getting-started",
        "/docs/apps/build/b2b/companies",
        "/docs/apps/build/b2b/catalogs",
        "/docs/apps/build/b2b/quantity-rules",
        "/docs/apps/build/b2b/volume-pricing",
        "/docs/themes/pricing-payments/b2b",
        "/docs/api/liquid/objects/company",
        "/docs/api/liquid/objects/company_location",
    ],
    
    # ---- IMPORTANT: Payments ----
    "payments": [
        "/docs/apps/build/payments",
        "/docs/apps/build/payments/payment-extensions",
        "/docs/apps/build/payments/getting-started",
        "/docs/api/admin-graphql/2024-10/objects/PaymentMethod",
        "/docs/api/admin-graphql/2024-10/objects/PaymentTerms",
    ],
    
    # ---- NICE-TO-HAVE: Review checklists ----
    "review-checklists": [
        "/docs/themes/store/requirements",
        "/docs/themes/store/requirements/performance",
        "/docs/themes/store/requirements/code",
        "/docs/themes/store/requirements/design",
        "/docs/themes/store/requirements/content",
        "/docs/themes/store/requirements/functionality",
        "/docs/themes/store/requirements/accessibility",
        "/docs/apps/store/requirements",
        "/docs/apps/store/requirements/security",
        "/docs/apps/store/requirements/performance",
        "/docs/apps/store/listing",
    ],
    
    # ---- NICE-TO-HAVE: Migrations ----
    "migrations": [
        "/docs/themes/migration",
        "/docs/themes/migration/online-store-2",
        "/docs/api/usage/versioning",
        "/docs/api/admin-graphql/migrate",
    ],
    
    # ---- NICE-TO-HAVE: Shopify Email ----
    "email-templates": [
        "/docs/apps/build/marketing/email",
    ],
    
    # ---- NICE-TO-HAVE: POS ----
    "pos": [
        "/docs/apps/build/pos",
        "/docs/apps/build/pos/getting-started",
        "/docs/api/pos-extensions",
    ],
    
    # ---- Auth & OAuth ----
    "auth": [
        "/docs/apps/build/authentication",
        "/docs/apps/build/authentication/access-tokens",
        "/docs/apps/build/authentication/access-tokens/token-exchange",
        "/docs/apps/build/authentication/access-tokens/offline-access-tokens",
        "/docs/apps/build/authentication/access-tokens/online-access-tokens",
        "/docs/apps/build/authentication/session-tokens",
        "/docs/api/usage/authentication",
        "/docs/api/usage/access-scopes",
    ],
    
    # ---- Subscriptions & Selling Plans ----
    "subscriptions": [
        "/docs/apps/build/purchase-options/subscriptions",
        "/docs/apps/build/purchase-options/subscriptions/getting-started",
        "/docs/apps/build/purchase-options/subscriptions/selling-plans",
        "/docs/apps/build/purchase-options/deferred-purchase-options",
        "/docs/api/admin-graphql/2024-10/mutations/sellingPlanGroupCreate",
        "/docs/api/admin-graphql/2024-10/objects/SellingPlan",
        "/docs/api/admin-graphql/2024-10/objects/SellingPlanGroup",
    ],
    
    # ---- Discounts ----
    "discounts": [
        "/docs/apps/build/discounts",
        "/docs/apps/build/discounts/build-discount-function",
        "/docs/api/admin-graphql/2024-10/mutations/discountCodeBasicCreate",
        "/docs/api/admin-graphql/2024-10/mutations/discountAutomaticBasicCreate",
        "/docs/api/admin-graphql/2024-10/objects/DiscountCodeNode",
        "/docs/api/admin-graphql/2024-10/objects/DiscountAutomaticNode",
    ],
    
    # ---- Theme App Extensions ----
    "theme-app-extensions": [
        "/docs/apps/build/online-store/theme-app-extensions",
        "/docs/apps/build/online-store/theme-app-extensions/getting-started",
        "/docs/apps/build/online-store/theme-app-extensions/configuration",
        "/docs/apps/build/online-store/theme-app-extensions/best-practices",
    ],
    
    # ---- Admin Extensions / UI Extensions ----
    "admin-extensions": [
        "/docs/apps/build/admin/admin-extensions",
        "/docs/apps/build/admin/admin-actions",
        "/docs/apps/build/admin/admin-blocks",
        "/docs/apps/build/admin/admin-links",
        "/docs/api/admin-extensions",
        "/docs/api/admin-extensions/components",
        "/docs/api/admin-extensions/extension-points",
    ],
    
    # ---- Fulfillment ----
    "fulfillment": [
        "/docs/apps/build/fulfillment",
        "/docs/apps/build/fulfillment/fulfillment-service-apps",
        "/docs/apps/build/fulfillment/manage-fulfillments",
        "/docs/apps/build/fulfillment/tracking-and-delivery",
        "/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreateV2",
        "/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder",
        "/docs/api/admin-graphql/2024-10/objects/Fulfillment",
    ],
}


def main():
    print("🚀 Phase 4: Scraping ALL remaining Shopify documentation\n")
    
    total_pages = sum(len(p) for p in CATEGORIES.values())
    print(f"📊 Total pages to scrape: {total_pages}")
    print(f"📊 Categories: {len(CATEGORIES)}\n")
    
    results = {}
    for category, paths in CATEGORIES.items():
        if not paths:
            continue
        print(f"\n📂 {category} ({len(paths)} pages)")
        stats = scrape_category(category, paths)
        results[category] = stats
        print(f"   → ✅{stats['ok']} ⏭️{stats['cached']} ⚠️{stats['empty']} ❌{stats['failed']}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 PHASE 4 FINAL SUMMARY")
    print("=" * 60)
    total_ok = sum(s["ok"] for s in results.values())
    total_cached = sum(s["cached"] for s in results.values())
    total_failed = sum(s["failed"] for s in results.values())
    total_empty = sum(s["empty"] for s in results.values())
    
    for cat, stats in results.items():
        print(f"  {cat}: ✅{stats['ok']} ⏭️{stats['cached']} ⚠️{stats['empty']} ❌{stats['failed']}")
    
    print(f"\nTotal: ✅{total_ok} new | ⏭️{total_cached} cached | ⚠️{total_empty} empty | ❌{total_failed} failed")
    
    manifest_path = RAW_DOCS / "scrape_manifest_phase4.json"
    with open(manifest_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n📋 Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
