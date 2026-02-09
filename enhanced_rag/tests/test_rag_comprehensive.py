#!/usr/bin/env python3
"""
Comprehensive RAG Search Engine Test Suite
==========================================
Runs 200+ real-world Shopify developer queries through the Enhanced RAG search engine,
evaluates result quality, and produces a detailed report.
"""

import json
import time
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from enhanced_rag.search.engine import EnhancedSearchEngine, analyze_query

# ============ TEST QUERIES ============
# Each query has: (query_text, category, expected_keywords, expected_collections)

TEST_QUERIES = [
    # ============================================================
    # LIQUID REFERENCE (30+)
    # ============================================================
    ("What properties does the product object have in Liquid?", "Liquid Reference",
     ["product", "title", "description", "price", "variants"], ["liquid_reference"]),
    ("How do I use the forloop object in Liquid?", "Liquid Reference",
     ["forloop", "index", "first", "last", "length"], ["liquid_reference"]),
    ("What is the money_with_currency filter in Liquid?", "Liquid Reference",
     ["money_with_currency", "filter", "price", "currency"], ["liquid_reference"]),
    ("List all Liquid string filters", "Liquid Reference",
     ["append", "capitalize", "downcase", "replace", "strip", "filter"], ["liquid_reference"]),
    ("What does the split filter do in Liquid?", "Liquid Reference",
     ["split", "filter", "string", "array", "delimiter"], ["liquid_reference"]),
    ("How to use the where filter in Liquid?", "Liquid Reference",
     ["where", "filter", "array", "property"], ["liquid_reference"]),
    ("What is the collection object in Liquid?", "Liquid Reference",
     ["collection", "products", "title", "description", "handle"], ["liquid_reference"]),
    ("How to access product.metafields in Liquid?", "Liquid Reference",
     ["metafield", "product", "namespace", "key"], ["liquid_reference"]),
    ("What are Liquid control flow tags?", "Liquid Reference",
     ["if", "elsif", "else", "unless", "case", "when"], ["liquid_reference"]),
    ("How does the paginate tag work in Liquid?", "Liquid Reference",
     ["paginate", "page_size", "current_page", "pages"], ["liquid_reference"]),
    ("What is the image_url filter?", "Liquid Reference",
     ["image_url", "width", "height", "crop", "filter"], ["liquid_reference"]),
    ("Explain the date filter in Liquid", "Liquid Reference",
     ["date", "filter", "format", "strftime"], ["liquid_reference"]),
    ("What properties does the variant object have?", "Liquid Reference",
     ["variant", "price", "sku", "title", "available", "option"], ["liquid_reference"]),
    ("How to use the assign tag in Liquid?", "Liquid Reference",
     ["assign", "variable", "tag"], ["liquid_reference"]),
    ("What is the capture tag used for?", "Liquid Reference",
     ["capture", "tag", "variable", "string"], ["liquid_reference"]),
    ("How to use the increment and decrement tags?", "Liquid Reference",
     ["increment", "decrement", "counter", "tag"], ["liquid_reference"]),
    ("What is the tablerow tag in Liquid?", "Liquid Reference",
     ["tablerow", "table", "row", "cols"], ["liquid_reference"]),
    ("How do Liquid comment tags work?", "Liquid Reference",
     ["comment", "tag", "liquid"], ["liquid_reference"]),
    ("What is the raw tag in Liquid?", "Liquid Reference",
     ["raw", "tag", "escape", "liquid"], ["liquid_reference"]),
    ("What does the default filter do?", "Liquid Reference",
     ["default", "filter", "nil", "fallback"], ["liquid_reference"]),
    ("How to use the url_encode filter?", "Liquid Reference",
     ["url_encode", "filter", "encode", "url"], ["liquid_reference"]),
    ("What is the handle property in Shopify Liquid?", "Liquid Reference",
     ["handle", "url", "slug", "product", "collection"], ["liquid_reference"]),
    ("How to iterate over a collection's products in Liquid?", "Liquid Reference",
     ["for", "collection", "products", "product"], ["liquid_reference"]),
    ("What is the all_products object?", "Liquid Reference",
     ["all_products", "handle", "product", "global"], ["liquid_reference"]),
    ("How to use the map filter in Liquid?", "Liquid Reference",
     ["map", "filter", "array", "property"], ["liquid_reference"]),
    ("What is the linklists object?", "Liquid Reference",
     ["linklists", "linklist", "menu", "navigation", "link"], ["liquid_reference"]),
    ("How to access the current page info in Liquid?", "Liquid Reference",
     ["page", "template", "request", "canonical_url"], ["liquid_reference"]),
    ("What are the request object properties?", "Liquid Reference",
     ["request", "host", "path", "page_type", "locale"], ["liquid_reference"]),
    ("How does the content_for_header tag work?", "Liquid Reference",
     ["content_for_header", "head", "layout", "scripts"], ["liquid_reference"]),
    ("What are Liquid math filters?", "Liquid Reference",
     ["plus", "minus", "times", "divided_by", "modulo", "math"], ["liquid_reference"]),
    ("How to use the slice filter in Liquid?", "Liquid Reference",
     ["slice", "filter", "string", "array", "offset"], ["liquid_reference"]),
    ("What is the shop object in Liquid?", "Liquid Reference",
     ["shop", "name", "url", "domain", "currency"], ["liquid_reference"]),

    # ============================================================
    # THEME DEVELOPMENT (30+)
    # ============================================================
    ("How to create a custom section in Shopify?", "Theme Development",
     ["section", "schema", "blocks", "settings"], ["theme_patterns", "code_examples"]),
    ("What is the section schema in Shopify themes?", "Theme Development",
     ["schema", "settings", "blocks", "presets", "section"], ["theme_patterns"]),
    ("How do templates work in Shopify Online Store 2.0?", "Theme Development",
     ["template", "json", "sections", "2.0"], ["theme_patterns"]),
    ("How to create a custom template in Shopify?", "Theme Development",
     ["template", "json", "custom", "alternate"], ["theme_patterns"]),
    ("What is the difference between sections and snippets?", "Theme Development",
     ["section", "snippet", "render", "include", "difference"], ["theme_patterns"]),
    ("How to use dynamic sources in section settings?", "Theme Development",
     ["dynamic", "source", "settings", "metafield", "section"], ["theme_patterns"]),
    ("How does the render tag differ from include?", "Theme Development",
     ["render", "include", "snippet", "scope", "variable"], ["theme_patterns", "liquid_reference"]),
    ("How to create section blocks in Shopify?", "Theme Development",
     ["block", "section", "schema", "type", "settings"], ["theme_patterns"]),
    ("What layout files are available in Shopify themes?", "Theme Development",
     ["layout", "theme.liquid", "password", "checkout"], ["theme_patterns"]),
    ("How to add custom settings to a theme?", "Theme Development",
     ["settings_schema", "settings", "input", "type", "label"], ["theme_patterns"]),
    ("How to create a predictive search in Shopify?", "Theme Development",
     ["predictive", "search", "ajax", "suggest", "results"], ["theme_patterns", "code_examples"]),
    ("What are theme app extensions?", "Theme Development",
     ["app", "extension", "block", "embed", "theme"], ["theme_patterns", "best_practices"]),
    ("How to use app blocks in Shopify themes?", "Theme Development",
     ["app", "block", "extension", "section", "theme"], ["theme_patterns"]),
    ("How to structure a Shopify theme directory?", "Theme Development",
     ["assets", "config", "layout", "sections", "templates", "snippets", "locales"], ["theme_patterns"]),
    ("How do locales work in Shopify themes?", "Theme Development",
     ["locale", "translation", "t", "json", "language"], ["theme_patterns"]),
    ("How to add translations to a Shopify theme?", "Theme Development",
     ["translation", "locale", "t", "json", "string"], ["theme_patterns"]),
    ("What are section groups in Online Store 2.0?", "Theme Development",
     ["section", "group", "header", "footer", "json"], ["theme_patterns"]),
    ("How to use metafield definitions in themes?", "Theme Development",
     ["metafield", "definition", "type", "namespace", "key"], ["theme_patterns"]),
    ("How do I create a dropdown menu in Shopify?", "Theme Development",
     ["menu", "dropdown", "navigation", "linklist", "nested"], ["theme_patterns", "code_examples"]),
    ("How to add a custom font to a Shopify theme?", "Theme Development",
     ["font", "font-face", "woff", "asset", "css"], ["theme_patterns", "best_practices"]),
    ("How to make a Shopify section with multiple block types?", "Theme Development",
     ["section", "block", "type", "schema", "settings"], ["theme_patterns"]),
    ("How to add settings_schema.json settings?", "Theme Development",
     ["settings_schema", "json", "settings", "theme"], ["theme_patterns"]),
    ("How do theme presets work?", "Theme Development",
     ["preset", "section", "schema", "default", "template"], ["theme_patterns"]),
    ("How to use the stylesheet tag in sections?", "Theme Development",
     ["stylesheet", "css", "section", "style", "tag"], ["theme_patterns"]),
    ("How to implement a product quick view?", "Theme Development",
     ["quick", "view", "modal", "product", "ajax"], ["theme_patterns", "code_examples"]),
    ("What is Dawn theme and how is it structured?", "Theme Development",
     ["dawn", "theme", "shopify", "reference", "structure"], ["theme_patterns", "code_examples"]),
    ("How to create an announcement bar section?", "Theme Development",
     ["announcement", "bar", "section", "banner", "message"], ["theme_patterns", "code_examples"]),
    ("How to implement a slideshow section?", "Theme Development",
     ["slideshow", "slider", "carousel", "section", "swiper"], ["theme_patterns", "code_examples"]),
    ("How to use CSS variables in Shopify themes?", "Theme Development",
     ["css", "variable", "custom", "property", "root"], ["theme_patterns", "best_practices"]),
    ("What is the assets directory used for in Shopify?", "Theme Development",
     ["assets", "css", "javascript", "image", "directory"], ["theme_patterns"]),
    ("How to add a newsletter signup form?", "Theme Development",
     ["newsletter", "form", "email", "subscribe", "signup"], ["theme_patterns", "code_examples"]),

    # ============================================================
    # CART/CHECKOUT (20+)
    # ============================================================
    ("How to implement an AJAX cart in Shopify?", "Cart/Checkout",
     ["ajax", "cart", "fetch", "add", "json", "cart/add"], ["theme_patterns", "code_examples"]),
    ("How to create a cart drawer in Shopify?", "Cart/Checkout",
     ["cart", "drawer", "side", "slide", "ajax"], ["theme_patterns", "code_examples"]),
    ("How to add line item properties to cart items?", "Cart/Checkout",
     ["line", "item", "properties", "cart", "custom"], ["theme_patterns", "liquid_reference"]),
    ("How to use the cart/add.js endpoint?", "Cart/Checkout",
     ["cart/add", "ajax", "api", "fetch", "json"], ["theme_patterns", "code_examples"]),
    ("What is the cart object in Liquid?", "Cart/Checkout",
     ["cart", "items", "total_price", "item_count", "properties"], ["liquid_reference"]),
    ("How to implement quantity selectors for cart items?", "Cart/Checkout",
     ["quantity", "selector", "cart", "update", "change"], ["theme_patterns", "code_examples"]),
    ("How to add a gift message to cart?", "Cart/Checkout",
     ["gift", "message", "cart", "note", "attribute"], ["theme_patterns"]),
    ("How to use cart attributes in Shopify?", "Cart/Checkout",
     ["cart", "attribute", "note", "property"], ["liquid_reference", "theme_patterns"]),
    ("How to implement a free shipping progress bar?", "Cart/Checkout",
     ["free", "shipping", "progress", "bar", "threshold", "cart"], ["theme_patterns", "code_examples"]),
    ("How do checkout extensions work in Shopify?", "Cart/Checkout",
     ["checkout", "extension", "ui", "api"], ["theme_patterns", "api_reference"]),
    ("How to redirect to checkout after adding to cart?", "Cart/Checkout",
     ["checkout", "redirect", "cart", "add", "submit"], ["theme_patterns"]),
    ("What is the cart/change.js endpoint?", "Cart/Checkout",
     ["cart/change", "update", "quantity", "line", "ajax"], ["theme_patterns", "code_examples"]),
    ("How to display cart totals dynamically?", "Cart/Checkout",
     ["cart", "total", "dynamic", "ajax", "price"], ["theme_patterns", "code_examples"]),
    ("How to implement upsells in the cart?", "Cart/Checkout",
     ["upsell", "cart", "recommend", "cross-sell", "product"], ["theme_patterns"]),
    ("How to calculate shipping rates in the cart?", "Cart/Checkout",
     ["shipping", "rate", "calculator", "cart", "estimate"], ["theme_patterns", "code_examples"]),
    ("How to handle cart errors in Shopify?", "Cart/Checkout",
     ["cart", "error", "handle", "stock", "quantity"], ["troubleshooting", "theme_patterns"]),
    ("How to add a discount code field to the cart?", "Cart/Checkout",
     ["discount", "code", "cart", "coupon", "apply"], ["theme_patterns", "code_examples"]),
    ("How to implement a mini cart popup?", "Cart/Checkout",
     ["mini", "cart", "popup", "modal", "ajax"], ["theme_patterns", "code_examples"]),
    ("How to use the cart/update.js endpoint?", "Cart/Checkout",
     ["cart/update", "ajax", "quantities", "update", "json"], ["theme_patterns", "code_examples"]),
    ("How to create a cart page with editable quantities?", "Cart/Checkout",
     ["cart", "page", "quantity", "edit", "form"], ["theme_patterns", "code_examples"]),
    ("How does the cart template work in Online Store 2.0?", "Cart/Checkout",
     ["cart", "template", "json", "section", "2.0"], ["theme_patterns"]),

    # ============================================================
    # PRODUCT PAGES (20+)
    # ============================================================
    ("How to display product variants on the product page?", "Product Pages",
     ["variant", "option", "select", "product", "picker"], ["theme_patterns", "code_examples"]),
    ("How to create a variant picker with swatches?", "Product Pages",
     ["swatch", "variant", "color", "picker", "option"], ["theme_patterns", "code_examples"]),
    ("How to display product metafields on the product page?", "Product Pages",
     ["metafield", "product", "display", "template"], ["theme_patterns", "liquid_reference"]),
    ("How to add structured data / JSON-LD to product pages?", "Product Pages",
     ["structured", "data", "json-ld", "schema", "seo", "product"], ["theme_patterns", "best_practices"]),
    ("How to implement a product image gallery?", "Product Pages",
     ["image", "gallery", "product", "thumbnail", "slider"], ["theme_patterns", "code_examples"]),
    ("How to show related products on the product page?", "Product Pages",
     ["related", "recommend", "product", "collection"], ["theme_patterns", "code_examples"]),
    ("How to change the product image when a variant is selected?", "Product Pages",
     ["variant", "image", "change", "select", "product"], ["theme_patterns", "code_examples"]),
    ("How to display product reviews on the product page?", "Product Pages",
     ["review", "rating", "product", "app", "star"], ["theme_patterns"]),
    ("How to show product availability (in stock/out of stock)?", "Product Pages",
     ["available", "stock", "inventory", "product", "variant"], ["theme_patterns", "liquid_reference"]),
    ("How to implement a product zoom feature?", "Product Pages",
     ["zoom", "image", "product", "magnify", "hover"], ["theme_patterns", "code_examples"]),
    ("How to display product tags in Shopify?", "Product Pages",
     ["tag", "product", "display", "filter", "collection"], ["liquid_reference", "theme_patterns"]),
    ("How to add a size chart to a product page?", "Product Pages",
     ["size", "chart", "product", "modal", "popup"], ["theme_patterns"]),
    ("How to show compare at prices?", "Product Pages",
     ["compare_at_price", "sale", "discount", "price"], ["liquid_reference", "theme_patterns"]),
    ("How to implement product tabs for description and details?", "Product Pages",
     ["tab", "description", "detail", "product", "accordion"], ["theme_patterns", "code_examples"]),
    ("How to display product media (3D models, video)?", "Product Pages",
     ["media", "3d", "model", "video", "product", "media_type"], ["theme_patterns", "liquid_reference"]),
    ("How to handle products with many variants in Liquid?", "Product Pages",
     ["variant", "product", "option", "combination", "limit"], ["theme_patterns", "liquid_reference"]),
    ("How to create a product page with a sticky add to cart?", "Product Pages",
     ["sticky", "add", "cart", "button", "fixed", "product"], ["theme_patterns", "code_examples"]),
    ("How to use product.selected_or_first_available_variant?", "Product Pages",
     ["selected_or_first_available_variant", "variant", "product", "default"], ["liquid_reference"]),
    ("How to show product inventory quantity?", "Product Pages",
     ["inventory", "quantity", "stock", "product", "variant"], ["liquid_reference", "theme_patterns"]),
    ("How to implement wishlist functionality?", "Product Pages",
     ["wishlist", "save", "favorite", "product", "list"], ["theme_patterns", "code_examples"]),
    ("How to add custom product badges (sale, new, bestseller)?", "Product Pages",
     ["badge", "sale", "new", "product", "tag", "label"], ["theme_patterns", "code_examples"]),

    # ============================================================
    # APIS (20+)
    # ============================================================
    ("What is the Shopify Admin API?", "APIs",
     ["admin", "api", "rest", "graphql", "resource"], ["api_reference"]),
    ("How to use the Storefront API?", "APIs",
     ["storefront", "api", "graphql", "token", "access"], ["api_reference"]),
    ("How to fetch products with the Storefront API?", "APIs",
     ["storefront", "api", "product", "query", "graphql"], ["api_reference"]),
    ("How to use the Ajax API in Shopify?", "APIs",
     ["ajax", "api", "cart", "product", "json", "fetch"], ["api_reference", "theme_patterns"]),
    ("What webhooks are available in Shopify?", "APIs",
     ["webhook", "topic", "event", "order", "product"], ["api_reference"]),
    ("How to authenticate with the Shopify API?", "APIs",
     ["auth", "token", "api", "key", "oauth", "access"], ["api_reference"]),
    ("How to create a product using the Admin API?", "APIs",
     ["product", "create", "admin", "api", "graphql"], ["api_reference"]),
    ("What is the Section Rendering API?", "APIs",
     ["section", "rendering", "api", "ajax", "fetch", "render"], ["api_reference", "theme_patterns"]),
    ("How to use the product recommendations endpoint?", "APIs",
     ["recommend", "product", "api", "endpoint", "related"], ["api_reference", "theme_patterns"]),
    ("How to use the Shopify GraphQL Admin API?", "APIs",
     ["graphql", "admin", "api", "query", "mutation"], ["api_reference"]),
    ("How to get customer data from the Storefront API?", "APIs",
     ["customer", "storefront", "api", "token", "query"], ["api_reference"]),
    ("How to handle pagination in the Admin API?", "APIs",
     ["pagination", "cursor", "admin", "api", "page", "next"], ["api_reference"]),
    ("What is the Shopify REST Admin API?", "APIs",
     ["rest", "admin", "api", "endpoint", "resource", "json"], ["api_reference"]),
    ("How to use metafield APIs?", "APIs",
     ["metafield", "api", "create", "update", "graphql"], ["api_reference"]),
    ("How to listen for order webhooks?", "APIs",
     ["order", "webhook", "listen", "create", "paid"], ["api_reference"]),
    ("How to use the search.json endpoint?", "APIs",
     ["search", "json", "endpoint", "api", "predictive"], ["api_reference", "theme_patterns"]),
    ("How to use multipass for SSO?", "APIs",
     ["multipass", "sso", "token", "customer", "login"], ["api_reference"]),
    ("How to fetch collections via Storefront API?", "APIs",
     ["collection", "storefront", "api", "graphql", "query"], ["api_reference"]),
    ("How to use the Shopify Cart API?", "APIs",
     ["cart", "api", "add", "update", "json", "ajax"], ["api_reference", "theme_patterns"]),
    ("How to fetch metaobjects via the API?", "APIs",
     ["metaobject", "api", "graphql", "fetch", "query"], ["api_reference"]),
    ("How to create a draft order via Admin API?", "APIs",
     ["draft", "order", "admin", "api", "create"], ["api_reference"]),

    # ============================================================
    # STYLING/CSS (15+)
    # ============================================================
    ("How to make a responsive product grid in Shopify?", "Styling/CSS",
     ["responsive", "grid", "product", "css", "media"], ["theme_patterns", "code_examples"]),
    ("How to use CSS Grid for a Shopify collection page?", "Styling/CSS",
     ["css", "grid", "collection", "layout", "responsive"], ["theme_patterns", "code_examples"]),
    ("How to add animations to a Shopify theme?", "Styling/CSS",
     ["animation", "css", "transition", "keyframe", "effect"], ["theme_patterns"]),
    ("How to implement dark mode in a Shopify theme?", "Styling/CSS",
     ["dark", "mode", "theme", "css", "color", "scheme"], ["theme_patterns", "best_practices"]),
    ("How to customize the Dawn theme CSS?", "Styling/CSS",
     ["dawn", "css", "custom", "style", "override"], ["code_examples", "theme_patterns"]),
    ("How to use Tailwind CSS with Shopify?", "Styling/CSS",
     ["tailwind", "css", "utility", "class", "shopify"], ["theme_patterns", "best_practices"]),
    ("How to make a sticky header in Shopify?", "Styling/CSS",
     ["sticky", "header", "fixed", "position", "scroll"], ["theme_patterns", "code_examples"]),
    ("How to add a custom scrollbar style?", "Styling/CSS",
     ["scrollbar", "css", "custom", "style", "webkit"], ["theme_patterns"]),
    ("How to implement a hamburger menu for mobile?", "Styling/CSS",
     ["hamburger", "menu", "mobile", "responsive", "navigation"], ["theme_patterns", "code_examples"]),
    ("How to style the Shopify cart page?", "Styling/CSS",
     ["cart", "style", "css", "page", "design"], ["theme_patterns", "code_examples"]),
    ("How to create a responsive hero banner?", "Styling/CSS",
     ["hero", "banner", "responsive", "section", "image"], ["theme_patterns", "code_examples"]),
    ("How to use flexbox for Shopify layouts?", "Styling/CSS",
     ["flexbox", "flex", "layout", "css", "align"], ["theme_patterns"]),
    ("How to add hover effects to product cards?", "Styling/CSS",
     ["hover", "effect", "product", "card", "css", "transition"], ["theme_patterns", "code_examples"]),
    ("How to customize form styles in Shopify?", "Styling/CSS",
     ["form", "style", "css", "input", "button", "custom"], ["theme_patterns"]),
    ("How to implement a masonry grid layout?", "Styling/CSS",
     ["masonry", "grid", "layout", "css", "columns"], ["theme_patterns", "code_examples"]),
    ("How to use media queries in Shopify themes?", "Styling/CSS",
     ["media", "query", "responsive", "breakpoint", "css"], ["theme_patterns", "best_practices"]),

    # ============================================================
    # PERFORMANCE (15+)
    # ============================================================
    ("How to lazy load images in Shopify?", "Performance",
     ["lazy", "load", "image", "loading", "defer"], ["best_practices", "theme_patterns"]),
    ("How to preload critical resources in Shopify?", "Performance",
     ["preload", "critical", "css", "font", "resource"], ["best_practices"]),
    ("How to improve Core Web Vitals for a Shopify store?", "Performance",
     ["core", "web", "vitals", "lcp", "cls", "fid", "performance"], ["best_practices"]),
    ("How to use the Section Rendering API for performance?", "Performance",
     ["section", "rendering", "api", "ajax", "partial", "performance"], ["best_practices", "theme_patterns"]),
    ("How to reduce JavaScript bundle size in Shopify?", "Performance",
     ["javascript", "bundle", "size", "defer", "async", "performance"], ["best_practices"]),
    ("How to optimize images in Shopify themes?", "Performance",
     ["image", "optimize", "webp", "srcset", "size", "performance"], ["best_practices"]),
    ("How to defer non-critical CSS in Shopify?", "Performance",
     ["defer", "css", "critical", "render", "blocking"], ["best_practices"]),
    ("What is the best way to load third-party scripts in Shopify?", "Performance",
     ["third-party", "script", "async", "defer", "performance"], ["best_practices"]),
    ("How to implement responsive images with srcset?", "Performance",
     ["srcset", "responsive", "image", "sizes", "width"], ["best_practices", "theme_patterns"]),
    ("How to use native lazy loading in Shopify themes?", "Performance",
     ["native", "lazy", "loading", "attribute", "image"], ["best_practices"]),
    ("How to reduce Liquid render time?", "Performance",
     ["liquid", "render", "time", "performance", "optimize"], ["best_practices"]),
    ("How to cache Shopify API responses?", "Performance",
     ["cache", "api", "response", "performance", "store"], ["best_practices"]),
    ("How to use content_for_header efficiently?", "Performance",
     ["content_for_header", "performance", "head", "script"], ["best_practices"]),
    ("How to minimize layout shifts in Shopify?", "Performance",
     ["layout", "shift", "cls", "aspect-ratio", "placeholder"], ["best_practices"]),
    ("How to optimize collection page loading speed?", "Performance",
     ["collection", "page", "speed", "performance", "optimize"], ["best_practices"]),
    ("How to use async/defer for JavaScript in Shopify?", "Performance",
     ["async", "defer", "javascript", "script", "load"], ["best_practices"]),

    # ============================================================
    # TROUBLESHOOTING (20+)
    # ============================================================
    ("Why is my Liquid variable returning nil?", "Troubleshooting",
     ["nil", "variable", "undefined", "scope", "assign"], ["troubleshooting", "liquid_reference"]),
    ("How to debug Liquid code in Shopify?", "Troubleshooting",
     ["debug", "liquid", "inspect", "log", "output"], ["troubleshooting"]),
    ("Why is my section not showing up in the theme editor?", "Troubleshooting",
     ["section", "editor", "schema", "preset", "missing"], ["troubleshooting"]),
    ("Why is my product form not submitting?", "Troubleshooting",
     ["form", "submit", "product", "error", "cart"], ["troubleshooting"]),
    ("How to fix 'Liquid error: Memory limits exceeded'?", "Troubleshooting",
     ["memory", "limit", "error", "liquid", "loop"], ["troubleshooting"]),
    ("Why are my theme changes not appearing?", "Troubleshooting",
     ["change", "appear", "cache", "clear", "publish"], ["troubleshooting"]),
    ("How to fix 'Too many redirects' error in Shopify?", "Troubleshooting",
     ["redirect", "error", "loop", "ssl", "domain"], ["troubleshooting"]),
    ("Why is my JavaScript not working in Shopify?", "Troubleshooting",
     ["javascript", "error", "script", "console", "not working"], ["troubleshooting"]),
    ("How to fix broken images in a Shopify theme?", "Troubleshooting",
     ["image", "broken", "error", "url", "asset"], ["troubleshooting"]),
    ("Why is the add to cart button not working?", "Troubleshooting",
     ["add to cart", "button", "not working", "error", "form"], ["troubleshooting"]),
    ("Why is my Shopify section schema invalid?", "Troubleshooting",
     ["schema", "invalid", "json", "error", "section"], ["troubleshooting"]),
    ("How to fix '404 Not Found' for theme assets?", "Troubleshooting",
     ["404", "asset", "not found", "file", "url"], ["troubleshooting"]),
    ("Why does my Liquid for loop show nothing?", "Troubleshooting",
     ["for", "loop", "empty", "nothing", "array", "nil"], ["troubleshooting"]),
    ("How to fix CORS errors with the Shopify API?", "Troubleshooting",
     ["cors", "error", "api", "origin", "header"], ["troubleshooting"]),
    ("Why are my metafields not showing up?", "Troubleshooting",
     ["metafield", "showing", "display", "nil", "access"], ["troubleshooting"]),
    ("How to troubleshoot slow Shopify theme performance?", "Troubleshooting",
     ["slow", "performance", "debug", "render", "speed"], ["troubleshooting", "best_practices"]),
    ("Why is my variant picker not updating the price?", "Troubleshooting",
     ["variant", "picker", "price", "update", "javascript"], ["troubleshooting"]),
    ("How to fix 'Argument error in tag for' in Liquid?", "Troubleshooting",
     ["argument", "error", "tag", "for", "liquid"], ["troubleshooting"]),
    ("Why is my Shopify form showing validation errors?", "Troubleshooting",
     ["form", "validation", "error", "required", "input"], ["troubleshooting"]),
    ("How to debug the Shopify Ajax API responses?", "Troubleshooting",
     ["debug", "ajax", "api", "response", "console"], ["troubleshooting"]),
    ("Why is my collection filter not working?", "Troubleshooting",
     ["collection", "filter", "tag", "not working", "link"], ["troubleshooting"]),
    ("How to fix undefined JavaScript errors in Shopify?", "Troubleshooting",
     ["undefined", "javascript", "error", "variable", "null"], ["troubleshooting"]),

    # ============================================================
    # ADVANCED (20+)
    # ============================================================
    ("How to use metaobjects in Shopify?", "Advanced",
     ["metaobject", "definition", "entry", "custom", "data"], ["theme_patterns", "api_reference"]),
    ("How do Shopify Markets work?", "Advanced",
     ["market", "international", "currency", "language", "region"], ["theme_patterns", "best_practices"]),
    ("How to implement B2B features in Shopify?", "Advanced",
     ["b2b", "wholesale", "company", "price", "list"], ["theme_patterns", "api_reference"]),
    ("How to use Shopify Multipass for authentication?", "Advanced",
     ["multipass", "token", "sso", "customer", "auth"], ["api_reference"]),
    ("How to create app blocks for Shopify themes?", "Advanced",
     ["app", "block", "extension", "schema", "theme"], ["theme_patterns"]),
    ("How to build a theme app extension?", "Advanced",
     ["theme", "app", "extension", "block", "embed"], ["theme_patterns"]),
    ("How to use Shopify Functions for discounts?", "Advanced",
     ["function", "discount", "custom", "extension", "wasm"], ["api_reference"]),
    ("How to implement custom storefronts with Hydrogen?", "Advanced",
     ["hydrogen", "react", "storefront", "custom", "headless"], ["api_reference"]),
    ("How to use the Customer Account API?", "Advanced",
     ["customer", "account", "api", "login", "profile"], ["api_reference"]),
    ("How to implement multi-currency in Shopify?", "Advanced",
     ["multi-currency", "currency", "market", "money", "locale"], ["theme_patterns", "liquid_reference"]),
    ("How to use Shopify Flow for automation?", "Advanced",
     ["flow", "automation", "trigger", "action", "workflow"], ["api_reference"]),
    ("How to implement product bundles in Shopify?", "Advanced",
     ["bundle", "product", "group", "discount", "combine"], ["theme_patterns", "code_examples"]),
    ("How to use the Shopify CLI for theme development?", "Advanced",
     ["cli", "theme", "dev", "serve", "push", "pull"], ["best_practices"]),
    ("How to create a custom storefront with the Storefront API?", "Advanced",
     ["custom", "storefront", "api", "headless", "react"], ["api_reference"]),
    ("How to implement subscription products in Shopify?", "Advanced",
     ["subscription", "recurring", "selling", "plan", "product"], ["api_reference"]),
    ("How to use Shopify Pixels for analytics?", "Advanced",
     ["pixel", "analytics", "tracking", "event", "custom"], ["api_reference"]),
    ("How to implement customer-specific pricing?", "Advanced",
     ["customer", "pricing", "tag", "discount", "b2b"], ["theme_patterns", "api_reference"]),
    ("How to use the Shopify Checkout Extensibility?", "Advanced",
     ["checkout", "extensibility", "ui", "extension", "custom"], ["api_reference"]),
    ("How to implement store locator functionality?", "Advanced",
     ["store", "locator", "map", "location", "google"], ["theme_patterns", "code_examples"]),
    ("How to use online store editor customization API?", "Advanced",
     ["editor", "customization", "api", "inspector", "section"], ["api_reference"]),
    ("How to create a headless Shopify storefront?", "Advanced",
     ["headless", "storefront", "api", "react", "next", "custom"], ["api_reference"]),

    # ============================================================
    # CODE GENERATION (15+)
    # ============================================================
    ("Build me a product card section with image, title, and price", "Code Generation",
     ["product", "card", "section", "image", "title", "price"], ["code_examples", "theme_patterns"]),
    ("Generate a Liquid snippet for a star rating display", "Code Generation",
     ["star", "rating", "snippet", "liquid", "display"], ["code_examples"]),
    ("Create a section for a hero banner with text overlay", "Code Generation",
     ["hero", "banner", "section", "text", "overlay", "image"], ["code_examples", "theme_patterns"]),
    ("Build me a color swatch variant picker in Liquid", "Code Generation",
     ["color", "swatch", "variant", "picker", "liquid", "option"], ["code_examples"]),
    ("Generate a Liquid template for a FAQ page", "Code Generation",
     ["faq", "template", "accordion", "question", "answer"], ["code_examples", "theme_patterns"]),
    ("Create a section for featured collections grid", "Code Generation",
     ["featured", "collection", "grid", "section", "product"], ["code_examples", "theme_patterns"]),
    ("Build me an AJAX add to cart form", "Code Generation",
     ["ajax", "add", "cart", "form", "fetch", "json"], ["code_examples"]),
    ("Generate a responsive image gallery with thumbnails", "Code Generation",
     ["responsive", "image", "gallery", "thumbnail", "product"], ["code_examples"]),
    ("Create a section for customer testimonials", "Code Generation",
     ["testimonial", "review", "section", "customer", "quote"], ["code_examples", "theme_patterns"]),
    ("Build me a mega menu navigation", "Code Generation",
     ["mega", "menu", "navigation", "dropdown", "multi-level"], ["code_examples", "theme_patterns"]),
    ("Generate a product comparison table in Liquid", "Code Generation",
     ["comparison", "table", "product", "feature", "liquid"], ["code_examples"]),
    ("Create a section for an image with text layout", "Code Generation",
     ["image", "text", "section", "layout", "side"], ["code_examples", "theme_patterns"]),
    ("Build me a collection filter sidebar", "Code Generation",
     ["filter", "sidebar", "collection", "tag", "facet"], ["code_examples", "theme_patterns"]),
    ("Generate a Liquid snippet for breadcrumb navigation", "Code Generation",
     ["breadcrumb", "navigation", "snippet", "liquid", "link"], ["code_examples"]),
    ("Create a custom product page template with tabs", "Code Generation",
     ["product", "template", "tab", "custom", "description"], ["code_examples", "theme_patterns"]),
    ("Build me a newsletter popup modal", "Code Generation",
     ["newsletter", "popup", "modal", "email", "subscribe"], ["code_examples"]),
    ("Generate a multi-column section with icons", "Code Generation",
     ["multi-column", "section", "icon", "column", "feature"], ["code_examples", "theme_patterns"]),
]


# ============ RELEVANCE EVALUATION ============

def rate_relevance(query_text, expected_keywords, expected_collections, results, category):
    """
    Automatically rate the relevance of search results for a query.
    Returns: (rating, score, reason)
    - rating: RELEVANT, PARTIAL, IRRELEVANT, NO_RESULTS
    - score: 0.0 to 1.0
    - reason: explanation string
    """
    if not results:
        return "NO_RESULTS", 0.0, "No results returned"
    
    top_result = results[0]
    top_3_text = " ".join(r.text.lower() for r in results[:3])
    top_3_collections = [r.collection for r in results[:3]]
    
    # Score components
    keyword_score = 0.0
    collection_score = 0.0
    result_score = 0.0
    reasons = []
    
    # 1. Keyword matching (up to 0.4)
    query_lower = query_text.lower()
    keywords_found = 0
    keywords_total = len(expected_keywords)
    for kw in expected_keywords:
        if kw.lower() in top_3_text:
            keywords_found += 1
    
    if keywords_total > 0:
        keyword_score = (keywords_found / keywords_total) * 0.4
        if keywords_found == 0:
            reasons.append(f"No expected keywords found in results")
        elif keywords_found < keywords_total * 0.3:
            reasons.append(f"Only {keywords_found}/{keywords_total} keywords found")
        else:
            reasons.append(f"{keywords_found}/{keywords_total} keywords matched")
    
    # 2. Collection matching (up to 0.3)
    collection_match = False
    for ec in expected_collections:
        if ec in top_3_collections:
            collection_match = True
            break
    
    if collection_match:
        collection_score = 0.3
        reasons.append("Collection match ✓")
    else:
        reasons.append(f"Expected {expected_collections}, got {top_3_collections}")
    
    # 3. Result quality score (up to 0.3)
    top_score_val = top_result.score if top_result.score else 0.0
    # RRF scores are typically 0.01-0.1 range
    if top_score_val > 0.05:
        result_score = 0.3
    elif top_score_val > 0.03:
        result_score = 0.2
    elif top_score_val > 0.01:
        result_score = 0.1
    else:
        result_score = 0.05
    reasons.append(f"Top score: {top_score_val:.4f}")
    
    # 4. Category-specific checks
    if category == "Liquid Reference":
        # Check for specific Liquid objects/filters/tags
        specific_terms = [kw for kw in expected_keywords if kw not in 
                          ["filter", "tag", "liquid", "property", "object", "shopify"]]
        specific_found = sum(1 for t in specific_terms if t.lower() in top_3_text)
        if specific_terms:
            specificity = specific_found / len(specific_terms)
            if specificity > 0.5:
                keyword_score = min(keyword_score + 0.1, 0.4)
                reasons.append(f"Specific Liquid terms found: {specific_found}/{len(specific_terms)}")
    
    elif category == "Troubleshooting":
        # Check for error/debug related content
        error_terms = ["error", "fix", "issue", "debug", "problem", "solution", "resolve",
                       "troubleshoot", "not working", "nil", "undefined"]
        error_found = sum(1 for t in error_terms if t in top_3_text)
        if error_found >= 2:
            keyword_score = min(keyword_score + 0.05, 0.4)
            reasons.append(f"Error-related content found")
    
    elif category == "Code Generation":
        # Check for actual code content
        code_indicators = ["<", "{%", "{{", "function", "const", "var", "class", 
                          "def", "section", "schema", "liquid"]
        code_found = sum(1 for t in code_indicators if t in top_3_text)
        if code_found >= 2:
            keyword_score = min(keyword_score + 0.05, 0.4)
            reasons.append(f"Code content found")
    
    # Total score
    total_score = keyword_score + collection_score + result_score
    
    # Determine rating
    if total_score >= 0.65:
        rating = "RELEVANT"
    elif total_score >= 0.4:
        rating = "PARTIAL"
    else:
        rating = "IRRELEVANT"
    
    return rating, total_score, "; ".join(reasons)


# ============ MAIN TEST RUNNER ============

def run_comprehensive_test():
    """Run all test queries and generate report."""
    
    print(f"=" * 60)
    print(f"Enhanced RAG Comprehensive Test Suite")
    print(f"Started: {datetime.now().isoformat()}")
    print(f"Total queries: {len(TEST_QUERIES)}")
    print(f"=" * 60)
    
    # Initialize engine with the test copy to avoid lock issues
    qdrant_path = str(PROJECT_ROOT / "qdrant_test_copy")
    print(f"\nInitializing search engine from {qdrant_path}...")
    engine = EnhancedSearchEngine(qdrant_path=qdrant_path)
    print("Engine initialized.\n")
    
    # Results storage
    all_results = []
    category_stats = defaultdict(lambda: {
        "total": 0, "relevant": 0, "partial": 0, "irrelevant": 0, 
        "no_results": 0, "scores": [], "search_scores": []
    })
    
    start_time = time.time()
    
    for i, (query, category, expected_kw, expected_cols) in enumerate(TEST_QUERIES):
        try:
            # Analyze query
            analyzed = analyze_query(query)
            
            # Search
            results = engine.search(
                query, 
                top_k=5, 
                use_reranker=False, 
                expand_parents=False
            )
            
            # Rate relevance
            rating, score, reason = rate_relevance(
                query, expected_kw, expected_cols, results, category
            )
            
            # Capture top 3 results details
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
            
            # Update category stats
            stats = category_stats[category]
            stats["total"] += 1
            stats["scores"].append(score)
            if results:
                stats["search_scores"].append(results[0].score)
            
            if rating == "RELEVANT":
                stats["relevant"] += 1
            elif rating == "PARTIAL":
                stats["partial"] += 1
            elif rating == "IRRELEVANT":
                stats["irrelevant"] += 1
            else:
                stats["no_results"] += 1
            
            # Progress output
            status = {"RELEVANT": "✅", "PARTIAL": "⚠️", "IRRELEVANT": "❌", "NO_RESULTS": "🔴"}
            print(f"  [{i+1:3d}/{len(TEST_QUERIES)}] {status.get(rating, '?')} {rating:12s} ({score:.2f}) | {category:20s} | {query[:60]}...")
            
        except Exception as e:
            print(f"  [{i+1:3d}/{len(TEST_QUERIES)}] 💥 ERROR | {category:20s} | {query[:60]}... -> {e}")
            all_results.append({
                "index": i + 1,
                "query": query,
                "category": category,
                "expected_keywords": expected_kw,
                "expected_collections": expected_cols,
                "detected_intent": "error",
                "target_collections": [],
                "expanded_queries": [],
                "num_results": 0,
                "top_results": [],
                "rating": "ERROR",
                "relevance_score": 0.0,
                "reason": str(e),
            })
            stats = category_stats[category]
            stats["total"] += 1
            stats["irrelevant"] += 1
            stats["scores"].append(0.0)
    
    elapsed = time.time() - start_time
    print(f"\n{'=' * 60}")
    print(f"Completed in {elapsed:.1f} seconds ({elapsed/len(TEST_QUERIES):.2f}s per query)")
    print(f"{'=' * 60}\n")
    
    # Save raw JSON
    json_path = Path(__file__).parent / "rag_test_results.json"
    with open(json_path, "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_queries": len(TEST_QUERIES),
            "elapsed_seconds": round(elapsed, 1),
            "results": all_results,
        }, f, indent=2)
    print(f"Raw JSON saved to: {json_path}")
    
    # Generate Markdown report
    report = generate_report(all_results, category_stats, elapsed)
    report_path = Path(__file__).parent / "rag_test_report.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Report saved to: {report_path}")
    
    return all_results, category_stats


def generate_report(all_results, category_stats, elapsed):
    """Generate comprehensive Markdown report."""
    
    lines = []
    
    # ===== HEADER =====
    lines.append("# Enhanced RAG Search Engine — Comprehensive Test Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Total Queries:** {len(all_results)}")
    lines.append(f"**Execution Time:** {elapsed:.1f}s ({elapsed/len(all_results):.2f}s/query)")
    lines.append("")
    
    # ===== EXECUTIVE SUMMARY =====
    lines.append("## Executive Summary")
    lines.append("")
    
    total = len(all_results)
    relevant = sum(1 for r in all_results if r["rating"] == "RELEVANT")
    partial = sum(1 for r in all_results if r["rating"] == "PARTIAL")
    irrelevant = sum(1 for r in all_results if r["rating"] == "IRRELEVANT")
    no_results = sum(1 for r in all_results if r["rating"] == "NO_RESULTS")
    errors = sum(1 for r in all_results if r["rating"] == "ERROR")
    
    avg_score = sum(r["relevance_score"] for r in all_results) / total if total else 0
    pass_rate = (relevant + partial) / total * 100 if total else 0
    
    avg_search_score = 0
    search_scores = [r["top_results"][0]["score"] for r in all_results if r["top_results"]]
    if search_scores:
        avg_search_score = sum(search_scores) / len(search_scores)
    
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
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
    
    # Rating distribution bar
    lines.append("### Rating Distribution")
    lines.append("```")
    bar_width = 50
    for label, count, emoji in [
        ("RELEVANT", relevant, "🟢"),
        ("PARTIAL", partial, "🟡"),
        ("IRRELEVANT", irrelevant, "🔴"),
        ("NO_RESULTS", no_results, "⚫"),
    ]:
        bar_len = int(count / total * bar_width) if total else 0
        lines.append(f"{emoji} {label:12s} {'█' * bar_len}{'░' * (bar_width - bar_len)} {count:3d} ({count/total*100:.1f}%)")
    lines.append("```")
    lines.append("")
    
    # ===== PER-CATEGORY BREAKDOWN =====
    lines.append("## Per-Category Breakdown")
    lines.append("")
    lines.append("| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |")
    lines.append("|----------|-------|----------|---------|------------|------------|-----------|-----------|")
    
    # Sort categories by pass rate
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
        
        # Show failing queries in this category
        failures = [r for r in cat_results if r["rating"] in ("IRRELEVANT", "NO_RESULTS")]
        if failures:
            lines.append(f"- **Issues ({len(failures)}):**")
            for f in failures[:5]:
                lines.append(f"  - ❌ `{f['query'][:70]}` → {f['rating']} ({f['reason']})")
        lines.append("")
    
    # ===== TOP 20 BEST =====
    lines.append("## Top 20 Best-Performing Queries")
    lines.append("")
    sorted_best = sorted(all_results, key=lambda x: x["relevance_score"], reverse=True)[:20]
    lines.append("| # | Score | Rating | Category | Query |")
    lines.append("|---|-------|--------|----------|-------|")
    for i, r in enumerate(sorted_best, 1):
        lines.append(f"| {i} | {r['relevance_score']:.3f} | {r['rating']} | {r['category']} | {r['query'][:80]} |")
    lines.append("")
    
    # ===== TOP 20 WORST =====
    lines.append("## Top 20 Worst-Performing Queries")
    lines.append("")
    sorted_worst = sorted(all_results, key=lambda x: x["relevance_score"])[:20]
    lines.append("| # | Score | Rating | Category | Query | Reason |")
    lines.append("|---|-------|--------|----------|-------|--------|")
    for i, r in enumerate(sorted_worst, 1):
        lines.append(f"| {i} | {r['relevance_score']:.3f} | {r['rating']} | {r['category']} | {r['query'][:60]} | {r['reason'][:80]} |")
    lines.append("")
    
    # ===== INTENT ANALYSIS =====
    lines.append("## Intent Detection Analysis")
    lines.append("")
    intent_stats = defaultdict(lambda: {"total": 0, "correct_intents": []})
    for r in all_results:
        intent_stats[r["detected_intent"]]["total"] += 1
        intent_stats[r["detected_intent"]]["correct_intents"].append(r["relevance_score"])
    
    lines.append("| Detected Intent | Count | Avg Relevance Score |")
    lines.append("|-----------------|-------|---------------------|")
    for intent, data in sorted(intent_stats.items(), key=lambda x: -x[1]["total"]):
        avg = sum(data["correct_intents"]) / max(len(data["correct_intents"]), 1)
        lines.append(f"| {intent} | {data['total']} | {avg:.3f} |")
    lines.append("")
    
    # ===== COLLECTION USAGE =====
    lines.append("## Collection Usage Analysis")
    lines.append("")
    col_stats = defaultdict(lambda: {"targeted": 0, "in_results": 0, "avg_score": []})
    for r in all_results:
        for c in r["target_collections"]:
            col_stats[c]["targeted"] += 1
        for tr in r["top_results"]:
            col_stats[tr["collection"]]["in_results"] += 1
            col_stats[tr["collection"]]["avg_score"].append(tr["score"])
    
    lines.append("| Collection | Times Targeted | Times in Results | Avg Score |")
    lines.append("|------------|---------------|-----------------|-----------|")
    for col, data in sorted(col_stats.items(), key=lambda x: -x[1]["in_results"]):
        avg = sum(data["avg_score"]) / max(len(data["avg_score"]), 1)
        lines.append(f"| {col} | {data['targeted']} | {data['in_results']} | {avg:.4f} |")
    lines.append("")
    
    # ===== GAPS ANALYSIS =====
    lines.append("## Identified Gaps & Weak Areas")
    lines.append("")
    
    # Find categories with low pass rates
    weak_cats = [(cat, stats) for cat, stats in category_stats.items() 
                 if (stats["relevant"] + stats["partial"]) / max(stats["total"], 1) < 0.7]
    if weak_cats:
        lines.append("### Categories with <70% Pass Rate")
        for cat, stats in weak_cats:
            rate = (stats["relevant"] + stats["partial"]) / max(stats["total"], 1) * 100
            lines.append(f"- **{cat}**: {rate:.0f}% pass rate")
        lines.append("")
    
    # Find queries with NO_RESULTS
    no_result_queries = [r for r in all_results if r["rating"] == "NO_RESULTS"]
    if no_result_queries:
        lines.append("### Queries with No Results")
        for r in no_result_queries:
            lines.append(f"- `{r['query']}`")
        lines.append("")
    
    # Find queries rated IRRELEVANT
    irrelevant_queries = [r for r in all_results if r["rating"] == "IRRELEVANT"]
    if irrelevant_queries:
        lines.append(f"### Irrelevant Results ({len(irrelevant_queries)} queries)")
        lines.append("")
        lines.append("These queries returned results that don't match the topic:")
        for r in irrelevant_queries:
            top_col = r["top_results"][0]["collection"] if r["top_results"] else "N/A"
            lines.append(f"- `{r['query'][:70]}` → got `{top_col}`, expected `{r['expected_collections']}`")
        lines.append("")
    
    # Find topics with weak keyword matching
    weak_kw = [r for r in all_results if r["relevance_score"] < 0.4 and r["rating"] != "NO_RESULTS"]
    if weak_kw:
        lines.append(f"### Queries with Weak Keyword Matching ({len(weak_kw)} queries)")
        lines.append("")
        lines.append("Results were returned but didn't contain expected keywords:")
        for r in weak_kw[:15]:
            lines.append(f"- `{r['query'][:70]}` (score: {r['relevance_score']:.3f}) — {r['reason'][:80]}")
        if len(weak_kw) > 15:
            lines.append(f"- ... and {len(weak_kw) - 15} more")
        lines.append("")
    
    # ===== RECOMMENDATIONS =====
    lines.append("## Recommendations for Improvement")
    lines.append("")
    
    # Generate data-driven recommendations
    recommendations = []
    
    # Check collection coverage
    for cat, stats in category_stats.items():
        rate = (stats["relevant"] + stats["partial"]) / max(stats["total"], 1) * 100
        if rate < 60:
            recommendations.append(
                f"**Improve {cat} coverage**: Only {rate:.0f}% pass rate. "
                f"Consider adding more {cat.lower()}-specific documents to the knowledge base."
            )
    
    # Check for specific topic gaps
    topic_gaps = defaultdict(int)
    for r in all_results:
        if r["rating"] in ("IRRELEVANT", "NO_RESULTS"):
            for kw in r["expected_keywords"][:3]:
                topic_gaps[kw] += 1
    
    if topic_gaps:
        top_gaps = sorted(topic_gaps.items(), key=lambda x: -x[1])[:10]
        gap_terms = ", ".join(f"`{g[0]}` ({g[1]}x)" for g in top_gaps)
        recommendations.append(
            f"**Add content for underrepresented topics**: The following terms appear frequently in "
            f"failing queries: {gap_terms}"
        )
    
    # Check intent classification
    for intent, data in intent_stats.items():
        avg = sum(data["correct_intents"]) / max(len(data["correct_intents"]), 1)
        if avg < 0.5 and data["total"] >= 5:
            recommendations.append(
                f"**Improve `{intent}` intent handling**: Average relevance score is only {avg:.3f} "
                f"across {data['total']} queries. Review collection routing for this intent."
            )
    
    # Check if reranker would help
    low_score_high_results = [r for r in all_results 
                               if r["num_results"] >= 3 and r["relevance_score"] < 0.5]
    if len(low_score_high_results) > len(all_results) * 0.2:
        recommendations.append(
            f"**Enable reranker for production**: {len(low_score_high_results)} queries ({len(low_score_high_results)/len(all_results)*100:.0f}%) "
            f"returned results but with low relevance. A cross-encoder reranker could significantly "
            f"improve result ordering."
        )
    
    # Check collection balance
    col_result_counts = defaultdict(int)
    for r in all_results:
        for tr in r["top_results"]:
            col_result_counts[tr["collection"]] += 1
    
    total_results = sum(col_result_counts.values())
    for col, count in col_result_counts.items():
        pct = count / max(total_results, 1) * 100
        if pct > 50:
            recommendations.append(
                f"**Rebalance collection weights**: `{col}` dominates results ({pct:.0f}% of all top results). "
                f"Other collections may be underrepresented."
            )
    
    # General recommendations
    recommendations.append(
        "**Add query expansion for Shopify-specific terms**: Many queries use terminology "
        "(e.g., 'Dawn theme', 'Online Store 2.0', 'checkout extensibility') that may not match "
        "document text exactly. Expand the synonym dictionary."
    )
    recommendations.append(
        "**Consider chunk size optimization**: Some results return code-heavy chunks that lack "
        "surrounding explanation. Ensure parent context is available for code-only chunks."
    )
    
    for i, rec in enumerate(recommendations, 1):
        lines.append(f"{i}. {rec}")
    lines.append("")
    
    # ===== FULL RESULTS TABLE =====
    lines.append("## Full Results Table")
    lines.append("")
    lines.append("| # | Query | Intent | Collections | Score | Rating |")
    lines.append("|---|-------|--------|-------------|-------|--------|")
    for r in all_results:
        cols = ", ".join(r["target_collections"][:2])
        q = r["query"][:65].replace("|", "\\|")
        lines.append(
            f"| {r['index']} | {q} | {r['detected_intent']} | {cols} | "
            f"{r['relevance_score']:.3f} | {r['rating']} |"
        )
    lines.append("")
    
    # Footer
    lines.append("---")
    lines.append(f"*Report generated by test_rag_comprehensive.py on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    
    return "\n".join(lines)


if __name__ == "__main__":
    run_comprehensive_test()
