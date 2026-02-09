---
source: compiled-from-community-knowledge
---

# Shopify Liquid Gotchas & Edge Cases

## 1. Liquid Whitespace Issues
- Liquid tags output whitespace by default. Use `{%-` and `-%}` to strip whitespace.
- Forgetting whitespace control in loops can create massive HTML output with blank lines.
- `{{ ... }}` always outputs; `{% ... %}` is logic-only. Mixing them up causes silent errors.

## 2. Nil vs Empty vs Blank
- `nil` — variable doesn't exist or was never assigned
- `empty` — array/string exists but has no items/characters
- `blank` — nil, false, empty string, or string with only whitespace
- **Gotcha:** `if product.metafield` is truthy even if the metafield value is empty string. Use `if product.metafield != blank`.

## 3. String Comparison
- Liquid comparisons are case-sensitive: `"Hello" == "hello"` is false
- Use `| downcase` before comparing strings
- Number strings: `"10" > "9"` is false (string comparison). Convert with `| plus: 0` first.

## 4. Forloop Limits
- Shopify limits `for` loops to 50 iterations by default on collections
- Use `paginate` for larger sets
- Nested loops compound the limit issue
- `{% for product in collection.products limit: 250 %}` max is 50, not 250

## 5. Section Rendering
- Sections can only be rendered once per page (except in JSON templates)
- `{% section 'header' %}` in layout means you can't also have it in a template
- Section schema settings are scoped — they don't share state between sections
- Sections within sections (nested) are NOT supported

## 6. JSON Templates vs Liquid Templates
- JSON templates (`templates/*.json`) are the modern approach
- Liquid templates (`templates/*.liquid`) are legacy
- You can't mix: if `product.json` exists, `product.liquid` is ignored
- JSON templates give merchants section control; Liquid templates don't

## 7. Metafields
- `product.metafields.namespace.key` — always use full path
- Metafield types matter: `single_line_text_field` vs `multi_line_text_field` vs `rich_text_field`
- Rich text metafields return JSON, not HTML — use `| metafield_tag` filter
- **Gotcha:** Metafield values are cached for the page load; live updates won't reflect

## 8. Cart Operations
- Cart AJAX API and Liquid cart object can be out of sync
- After `cart/add.js`, you need to refresh the page or re-fetch cart via AJAX for Liquid to update
- Cart attributes have a 250 character limit per attribute
- Line item properties starting with `_` are hidden from customers

## 9. Image Handling
- `img_url` is deprecated — use `image_url` instead
- `image_url` accepts `width` and `height` params: `{{ image | image_url: width: 300 }}`
- Max image size from Shopify CDN: 5760x5760
- **Gotcha:** `image_url` without size params returns the original image (can be massive)
- Use `loading: 'lazy'` with `image_tag` for performance

## 10. Locale & Currency
- `shop.currency` is the store's default currency, not the customer's
- Use `cart.currency.iso_code` for the current cart currency
- `money` filter uses shop's default format; `money_with_currency` is safer for multi-currency
- **Gotcha:** Price is always in cents — `product.price` returns 1000 for $10.00

## 11. URL Handling
- `{{ 'style.css' | asset_url }}` — for files in assets/
- `{{ 'logo.png' | file_url }}` — for files uploaded via Settings > Files
- `{{ product.url }}` includes `/products/` prefix
- **Gotcha:** `within: collection` in URLs breaks if the collection handle changes
- Canonical URLs: always use `{{ canonical_url }}` to avoid duplicate content

## 12. Render vs Include
- `{% render %}` is preferred over `{% include %}` (deprecated)
- **Key difference:** `render` creates an isolated scope — parent variables aren't accessible
- Must pass variables explicitly: `{% render 'snippet', product: product %}`
- `include` shares the parent scope (but is deprecated and may be removed)

## 13. Schema Limitations
- Section `{% schema %}` must be valid JSON — no Liquid inside
- Schema `blocks` max: 50 per section
- Schema `settings` — no dynamic defaults (can't use Liquid in default values)
- Preset values in schema don't update existing installations when theme updates

## 14. Performance Pitfalls
- Avoid `{% for %}` inside `{% for %}` — O(n²) rendering
- `{{ 'all' | asset_url }}` loads ALL assets — never use it
- `content_for_header` is required and cannot be removed (contains analytics, etc.)
- Too many `{% render %}` calls (50+) slow down page rendering significantly
- Use `{% cache %}` (Shopify Online Store 2.0) where available

## 15. Predictive Search
- Returns max 10 results per resource type
- Available types: product, collection, article, page, query
- **Gotcha:** Results are influenced by the store's search settings, not just the query
- Must use AJAX — no Liquid equivalent for predictive search

## 16. Customer Accounts
- `customer` object is nil on non-account pages unless logged in
- New customer accounts (2023+) use a different URL structure
- **Gotcha:** `customer.tags` are lowercase in Liquid even if set as uppercase in admin

## 17. Pagination
- Default pagination: 50 items
- Max: 50 items per page
- `paginate.pages` returns total page count
- **Gotcha:** Pagination only works within `{% paginate %}` block — can't paginate arbitrary arrays

## 18. Ajax API vs Liquid
- Ajax Cart API returns JSON; Liquid renders HTML
- They can show different data if caching is involved
- Section Rendering API (`sections` param) bridges this gap
- **Gotcha:** `routes.cart_url` in Liquid vs `/cart.js` in AJAX — different formats

## 19. Theme Editor Compatibility
- Always provide sensible defaults in schema
- Use `{% if section.settings.image %}` before rendering — editor starts with nil
- Preview vs Live can show different results due to caching
- **Gotcha:** Theme editor loads ALL sections, even those not on the current template

## 20. Deprecated Features to Avoid
- `{% include %}` → use `{% render %}`
- `| img_url` → use `| image_url`
- `| asset_img_url` → use `| image_url` with `| asset_url`
- `{{ settings.style }}` old-style settings → use section settings
- Alternate templates (`.alternate.liquid`) → use JSON templates with sections
