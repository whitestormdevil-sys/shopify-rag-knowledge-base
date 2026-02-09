#!/usr/bin/env python3
"""Phase 2+3: Scrape Shopify Admin API, Storefront API, Webhooks, Functions, 
Checkout, App Bridge, Polaris, CLI, Hydrogen docs, Changelog, Tutorials"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json
import os
import time
from pathlib import Path

BASE_URL = "https://shopify.dev"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

RAW_DOCS = Path(__file__).parent.parent / "raw-docs"

# ========== PHASE 2: Admin API + Storefront API + Webhooks ==========

ADMIN_API_PAGES = {
    "admin-api": [
        # REST Admin API - core resources
        "/docs/api/admin-rest",
        "/docs/api/admin-rest/2024-10/resources/product",
        "/docs/api/admin-rest/2024-10/resources/product-variant",
        "/docs/api/admin-rest/2024-10/resources/product-image",
        "/docs/api/admin-rest/2024-10/resources/collection",
        "/docs/api/admin-rest/2024-10/resources/custom-collection",
        "/docs/api/admin-rest/2024-10/resources/smart-collection",
        "/docs/api/admin-rest/2024-10/resources/collect",
        "/docs/api/admin-rest/2024-10/resources/order",
        "/docs/api/admin-rest/2024-10/resources/draft-order",
        "/docs/api/admin-rest/2024-10/resources/customer",
        "/docs/api/admin-rest/2024-10/resources/customer-address",
        "/docs/api/admin-rest/2024-10/resources/inventory-item",
        "/docs/api/admin-rest/2024-10/resources/inventory-level",
        "/docs/api/admin-rest/2024-10/resources/location",
        "/docs/api/admin-rest/2024-10/resources/fulfillment",
        "/docs/api/admin-rest/2024-10/resources/fulfillment-order",
        "/docs/api/admin-rest/2024-10/resources/fulfillment-service",
        "/docs/api/admin-rest/2024-10/resources/transaction",
        "/docs/api/admin-rest/2024-10/resources/refund",
        "/docs/api/admin-rest/2024-10/resources/cart",
        "/docs/api/admin-rest/2024-10/resources/checkout",
        "/docs/api/admin-rest/2024-10/resources/theme",
        "/docs/api/admin-rest/2024-10/resources/asset",
        "/docs/api/admin-rest/2024-10/resources/page",
        "/docs/api/admin-rest/2024-10/resources/blog",
        "/docs/api/admin-rest/2024-10/resources/article",
        "/docs/api/admin-rest/2024-10/resources/comment",
        "/docs/api/admin-rest/2024-10/resources/redirect",
        "/docs/api/admin-rest/2024-10/resources/script-tag",
        "/docs/api/admin-rest/2024-10/resources/discount-code",
        "/docs/api/admin-rest/2024-10/resources/price-rule",
        "/docs/api/admin-rest/2024-10/resources/shop",
        "/docs/api/admin-rest/2024-10/resources/policy",
        "/docs/api/admin-rest/2024-10/resources/country",
        "/docs/api/admin-rest/2024-10/resources/province",
        "/docs/api/admin-rest/2024-10/resources/shipping-zone",
        "/docs/api/admin-rest/2024-10/resources/carrier-service",
        "/docs/api/admin-rest/2024-10/resources/metafield",
        "/docs/api/admin-rest/2024-10/resources/webhook",
        "/docs/api/admin-rest/2024-10/resources/event",
        "/docs/api/admin-rest/2024-10/resources/user",
        "/docs/api/admin-rest/2024-10/resources/gift-card",
        "/docs/api/admin-rest/2024-10/resources/marketing-event",
        "/docs/api/admin-rest/2024-10/resources/report",
        "/docs/api/admin-rest/2024-10/resources/tender-transaction",
        "/docs/api/admin-rest/2024-10/resources/abandoned-checkout",
        # GraphQL Admin API overview & key types
        "/docs/api/admin-graphql",
        "/docs/api/admin-graphql/getting-started",
        "/docs/api/admin-graphql/2024-10/queries/products",
        "/docs/api/admin-graphql/2024-10/queries/orders",
        "/docs/api/admin-graphql/2024-10/queries/customers",
        "/docs/api/admin-graphql/2024-10/queries/collections",
        "/docs/api/admin-graphql/2024-10/queries/inventoryItems",
        "/docs/api/admin-graphql/2024-10/mutations/productCreate",
        "/docs/api/admin-graphql/2024-10/mutations/productUpdate",
        "/docs/api/admin-graphql/2024-10/mutations/productDelete",
        "/docs/api/admin-graphql/2024-10/mutations/orderCreate",
        "/docs/api/admin-graphql/2024-10/mutations/orderUpdate",
        "/docs/api/admin-graphql/2024-10/mutations/customerCreate",
        "/docs/api/admin-graphql/2024-10/mutations/customerUpdate",
        "/docs/api/admin-graphql/2024-10/mutations/collectionCreate",
        "/docs/api/admin-graphql/2024-10/mutations/inventoryAdjustQuantities",
        "/docs/api/admin-graphql/2024-10/mutations/metafieldsSet",
        "/docs/api/admin-graphql/2024-10/mutations/discountCodeBasicCreate",
        "/docs/api/admin-graphql/2024-10/mutations/draftOrderCreate",
        "/docs/api/admin-graphql/2024-10/mutations/draftOrderComplete",
        "/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreateV2",
        "/docs/api/admin-graphql/2024-10/mutations/webhookSubscriptionCreate",
        "/docs/api/admin-graphql/2024-10/objects/Product",
        "/docs/api/admin-graphql/2024-10/objects/ProductVariant",
        "/docs/api/admin-graphql/2024-10/objects/Order",
        "/docs/api/admin-graphql/2024-10/objects/Customer",
        "/docs/api/admin-graphql/2024-10/objects/Collection",
        "/docs/api/admin-graphql/2024-10/objects/Metafield",
        "/docs/api/admin-graphql/2024-10/objects/InventoryItem",
        "/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder",
        "/docs/api/admin-graphql/2024-10/objects/Image",
        "/docs/api/admin-graphql/2024-10/objects/Shop",
    ],
}

STOREFRONT_API_PAGES = {
    "storefront-api": [
        "/docs/api/storefront",
        "/docs/api/storefront/getting-started",
        "/docs/api/storefront/2024-10/queries/products",
        "/docs/api/storefront/2024-10/queries/collections",
        "/docs/api/storefront/2024-10/queries/cart",
        "/docs/api/storefront/2024-10/queries/customer",
        "/docs/api/storefront/2024-10/queries/shop",
        "/docs/api/storefront/2024-10/queries/menu",
        "/docs/api/storefront/2024-10/queries/pages",
        "/docs/api/storefront/2024-10/queries/blogs",
        "/docs/api/storefront/2024-10/queries/articles",
        "/docs/api/storefront/2024-10/queries/localization",
        "/docs/api/storefront/2024-10/queries/search",
        "/docs/api/storefront/2024-10/queries/predictiveSearch",
        "/docs/api/storefront/2024-10/mutations/cartCreate",
        "/docs/api/storefront/2024-10/mutations/cartLinesAdd",
        "/docs/api/storefront/2024-10/mutations/cartLinesUpdate",
        "/docs/api/storefront/2024-10/mutations/cartLinesRemove",
        "/docs/api/storefront/2024-10/mutations/cartDiscountCodesUpdate",
        "/docs/api/storefront/2024-10/mutations/cartBuyerIdentityUpdate",
        "/docs/api/storefront/2024-10/mutations/customerCreate",
        "/docs/api/storefront/2024-10/mutations/customerAccessTokenCreate",
        "/docs/api/storefront/2024-10/objects/Product",
        "/docs/api/storefront/2024-10/objects/ProductVariant",
        "/docs/api/storefront/2024-10/objects/Collection",
        "/docs/api/storefront/2024-10/objects/Cart",
        "/docs/api/storefront/2024-10/objects/CartLine",
        "/docs/api/storefront/2024-10/objects/Customer",
        "/docs/api/storefront/2024-10/objects/Order",
        "/docs/api/storefront/2024-10/objects/Shop",
        "/docs/api/storefront/2024-10/objects/Metafield",
        "/docs/api/storefront/2024-10/objects/Image",
        "/docs/api/storefront/2024-10/objects/SellingPlan",
    ],
}

WEBHOOK_PAGES = {
    "webhooks": [
        "/docs/api/webhooks",
        "/docs/apps/build/webhooks",
        "/docs/apps/build/webhooks/subscribe",
        "/docs/apps/build/webhooks/mandatory-webhooks",
        "/docs/apps/build/webhooks/configuration",
    ],
}

# ========== PHASE 3: Functions, Checkout, App Bridge, Polaris, CLI ==========

FUNCTIONS_PAGES = {
    "functions-docs": [
        "/docs/apps/build/functions",
        "/docs/apps/build/functions/input-output",
        "/docs/apps/build/functions/monitoring",
        "/docs/api/functions",
        "/docs/api/functions/reference/product-discounts",
        "/docs/api/functions/reference/order-discounts",
        "/docs/api/functions/reference/shipping-discounts",
        "/docs/api/functions/reference/delivery-customization",
        "/docs/api/functions/reference/payment-customization",
        "/docs/api/functions/reference/cart-transform",
        "/docs/api/functions/reference/fulfillment-constraints",
        "/docs/api/functions/reference/order-routing-location-rule",
    ],
}

CHECKOUT_PAGES = {
    "checkout-docs": [
        "/docs/api/checkout-extensions",
        "/docs/api/checkout-extensions/getting-started",
        "/docs/api/checkout-extensions/components",
        "/docs/api/checkout-extensions/components/Banner",
        "/docs/api/checkout-extensions/components/BlockStack",
        "/docs/api/checkout-extensions/components/Button",
        "/docs/api/checkout-extensions/components/Checkbox",
        "/docs/api/checkout-extensions/components/Divider",
        "/docs/api/checkout-extensions/components/Heading",
        "/docs/api/checkout-extensions/components/Icon",
        "/docs/api/checkout-extensions/components/Image",
        "/docs/api/checkout-extensions/components/InlineLayout",
        "/docs/api/checkout-extensions/components/Link",
        "/docs/api/checkout-extensions/components/List",
        "/docs/api/checkout-extensions/components/Modal",
        "/docs/api/checkout-extensions/components/Select",
        "/docs/api/checkout-extensions/components/Spinner",
        "/docs/api/checkout-extensions/components/Text",
        "/docs/api/checkout-extensions/components/TextBlock",
        "/docs/api/checkout-extensions/components/TextField",
        "/docs/api/checkout-extensions/configuration",
        "/docs/api/checkout-extensions/extension-points",
        "/docs/apps/build/checkout",
        "/docs/apps/build/checkout/thank-you-order-status",
    ],
}

APP_BRIDGE_PAGES = {
    "app-bridge-docs": [
        "/docs/api/app-bridge",
        "/docs/api/app-bridge/previous-versions/app-bridge-from-cdn",
        "/docs/apps/build/app-extensions",
        "/docs/apps/build/admin",
    ],
}

POLARIS_PAGES = {
    "polaris-docs": [
        # We'll scrape from polaris.shopify.com
    ],
}

CLI_PAGES = {
    "cli-docs": [
        "/docs/api/shopify-cli",
        "/docs/api/shopify-cli/app",
        "/docs/api/shopify-cli/theme",
        "/docs/themes/tools/cli",
        "/docs/themes/tools/cli/commands",
    ],
}

HYDROGEN_PAGES = {
    "hydrogen-docs": [
        "/docs/storefronts/headless/hydrogen",
        "/docs/storefronts/headless/hydrogen/getting-started",
        "/docs/storefronts/headless/hydrogen/project-structure",
        "/docs/storefronts/headless/hydrogen/data-fetching",
        "/docs/storefronts/headless/hydrogen/routing",
        "/docs/storefronts/headless/hydrogen/content",
        "/docs/storefronts/headless/hydrogen/markets",
        "/docs/storefronts/headless/hydrogen/analytics",
        "/docs/storefronts/headless/hydrogen/caching",
        "/docs/storefronts/headless/hydrogen/seo",
        "/docs/storefronts/headless/hydrogen/authentication",
        "/docs/storefronts/headless/hydrogen/cart",
        "/docs/storefronts/headless/hydrogen/deployments",
    ],
}

TUTORIAL_PAGES = {
    "tutorials": [
        "/docs/apps/getting-started",
        "/docs/apps/getting-started/build-app-example",
        "/docs/apps/build",
        "/docs/apps/build/authentication",
        "/docs/apps/build/authentication/access-tokens",
        "/docs/apps/build/graphql",
        "/docs/apps/build/graphql/basics",
        "/docs/apps/build/graphql/migrate",
        "/docs/apps/build/online-store",
        "/docs/apps/build/online-store/theme-app-extensions",
        "/docs/apps/build/online-store/app-proxies",
        "/docs/apps/build/purchase-options",
        "/docs/apps/build/purchase-options/subscriptions",
        "/docs/apps/build/marketing",
        "/docs/apps/build/marketing/marketing-activities",
        "/docs/apps/build/customers",
        "/docs/apps/build/customers/customer-accounts",
        "/docs/apps/build/orders",
        "/docs/apps/build/orders/manage-orders",
        "/docs/apps/build/payments",
        "/docs/apps/build/fulfillment",
        "/docs/apps/build/flow",
        "/docs/apps/build/flow/actions",
        "/docs/apps/build/flow/triggers",
        "/docs/apps/store/requirements",
        "/docs/apps/store/listing",
        "/docs/apps/best-practices",
        "/docs/apps/best-practices/performance",
        "/docs/apps/best-practices/security",
    ],
}

CHANGELOG_PAGES = {
    "changelog": [
        "/docs/api/release-notes",
        "/docs/api/release-notes/2024-10",
        "/docs/api/release-notes/2024-07",
        "/docs/api/release-notes/2024-04",
        "/docs/api/release-notes/2024-01",
        "/docs/api/release-notes/2023-10",
        "/docs/api/release-notes/2023-07",
        "/docs/api/release-notes/2023-04",
        "/docs/api/usage",
        "/docs/api/usage/versioning",
        "/docs/api/usage/rate-limits",
        "/docs/api/usage/pagination",
        "/docs/api/usage/authentication",
        "/docs/api/usage/access-scopes",
    ],
}


def fetch_page(url):
    """Fetch a page and return parsed content"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  ❌ Failed: {url}: {e}")
        return None


def extract_content(html, url):
    """Extract main content from Shopify docs page"""
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
    header = f"---\nsource: {url}\n---\n\n"
    return header + content.strip()


def scrape_category(category, paths, base_dir):
    """Scrape all pages in a category"""
    output_dir = base_dir / category
    output_dir.mkdir(parents=True, exist_ok=True)
    stats = {"ok": 0, "cached": 0, "failed": 0, "empty": 0}
    
    for path in paths:
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
                print(f"  ✅ {filename} ({len(content)} chars)")
            else:
                stats["empty"] += 1
                print(f"  ⚠️  Empty: {filename}")
        else:
            stats["failed"] += 1
        
        time.sleep(0.3)
    
    return stats


def main():
    print("🚀 Phase 2+3: Extended Shopify Documentation Scrape\n")
    
    all_categories = {}
    all_categories.update(ADMIN_API_PAGES)
    all_categories.update(STOREFRONT_API_PAGES)
    all_categories.update(WEBHOOK_PAGES)
    all_categories.update(FUNCTIONS_PAGES)
    all_categories.update(CHECKOUT_PAGES)
    all_categories.update(APP_BRIDGE_PAGES)
    all_categories.update(CLI_PAGES)
    all_categories.update(HYDROGEN_PAGES)
    all_categories.update(TUTORIAL_PAGES)
    all_categories.update(CHANGELOG_PAGES)
    
    total_pages = sum(len(p) for p in all_categories.values())
    print(f"📊 Total pages to scrape: {total_pages}\n")
    
    results = {}
    for category, paths in all_categories.items():
        if not paths:
            continue
        print(f"\n📂 {category} ({len(paths)} pages)")
        stats = scrape_category(category, paths, RAW_DOCS)
        results[category] = stats
        print(f"   → ✅{stats['ok']} ⏭️{stats['cached']} ⚠️{stats['empty']} ❌{stats['failed']}")
    
    print("\n" + "=" * 60)
    print("📊 PHASE 2+3 SUMMARY")
    print("=" * 60)
    total_ok = sum(s["ok"] for s in results.values())
    total_cached = sum(s["cached"] for s in results.values())
    total_failed = sum(s["failed"] for s in results.values())
    total_empty = sum(s["empty"] for s in results.values())
    
    for cat, stats in results.items():
        print(f"  {cat}: ✅{stats['ok']} ⏭️{stats['cached']} ⚠️{stats['empty']} ❌{stats['failed']}")
    
    print(f"\nTotal: ✅{total_ok} new | ⏭️{total_cached} cached | ⚠️{total_empty} empty | ❌{total_failed} failed")
    
    # Update manifest
    manifest_path = RAW_DOCS / "scrape_manifest_phase2.json"
    with open(manifest_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n📋 Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
