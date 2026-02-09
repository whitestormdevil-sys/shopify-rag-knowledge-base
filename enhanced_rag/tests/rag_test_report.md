# Enhanced RAG Search Engine — Comprehensive Test Report

**Generated:** 2026-02-09 12:45:42
**Total Queries:** 218
**Execution Time:** 93.5s (0.43s/query)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Overall Pass Rate** (RELEVANT + PARTIAL) | **91.7%** (200/218) |
| RELEVANT | 125 (57.3%) |
| PARTIAL | 75 (34.4%) |
| IRRELEVANT | 18 (8.3%) |
| NO_RESULTS | 0 (0.0%) |
| ERRORS | 0 |
| **Avg Relevance Score** | **0.693** (0-1 scale) |
| **Avg Top-1 Search Score** | **0.0641** |
| Queries/Second | 2.3 |

### Rating Distribution
```
🟢 RELEVANT     ████████████████████████████░░░░░░░░░░░░░░░░░░░░░░ 125 (57.3%)
🟡 PARTIAL      █████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  75 (34.4%)
🔴 IRRELEVANT   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  18 (8.3%)
⚫ NO_RESULTS   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0 (0.0%)
```

## Per-Category Breakdown

| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |
|----------|-------|----------|---------|------------|------------|-----------|-----------|
| Liquid Reference | 32 | 30 (94%) | 2 (6%) | 0 (0%) | 0 | **100%** | 0.893 |
| Theme Development | 31 | 24 (77%) | 7 (23%) | 0 (0%) | 0 | **100%** | 0.723 |
| Product Pages | 21 | 17 (81%) | 4 (19%) | 0 (0%) | 0 | **100%** | 0.817 |
| Troubleshooting | 22 | 14 (64%) | 8 (36%) | 0 (0%) | 0 | **100%** | 0.729 |
| Code Generation | 17 | 5 (29%) | 11 (65%) | 1 (6%) | 0 | **94%** | 0.575 |
| Cart/Checkout | 21 | 9 (43%) | 9 (43%) | 3 (14%) | 0 | **86%** | 0.620 |
| Advanced | 21 | 12 (57%) | 6 (29%) | 3 (14%) | 0 | **86%** | 0.664 |
| Styling/CSS | 16 | 0 (0%) | 13 (81%) | 3 (19%) | 0 | **81%** | 0.485 |
| APIs | 21 | 13 (62%) | 4 (19%) | 4 (19%) | 0 | **81%** | 0.697 |
| Performance | 16 | 1 (6%) | 11 (69%) | 4 (25%) | 0 | **75%** | 0.488 |

### Liquid Reference
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.893
- **Avg Search Score:** 0.0952

### Theme Development
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.723
- **Avg Search Score:** 0.0546

### Product Pages
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.817
- **Avg Search Score:** 0.0591

### Troubleshooting
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.729
- **Avg Search Score:** 0.0516

### Code Generation
- **Pass Rate:** 94%
- **Avg Relevance Score:** 0.575
- **Avg Search Score:** 0.0880
- **Issues (1):**
  - ❌ `Generate a multi-column section with icons` → IRRELEVANT (Only 1/5 keywords found; Expected ['code_examples', 'theme_patterns'], got ['api_reference', 'api_reference', 'api_reference']; Top score: 0.0725)

### Cart/Checkout
- **Pass Rate:** 86%
- **Avg Relevance Score:** 0.620
- **Avg Search Score:** 0.0481
- **Issues (3):**
  - ❌ `How to implement a free shipping progress bar?` → IRRELEVANT (Only 1/6 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0310)
  - ❌ `How to use the cart/update.js endpoint?` → IRRELEVANT (2/5 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubleshooting', 'troubleshooting', 'troubleshooting']; Top score: 0.0325)
  - ❌ `How to create a cart page with editable quantities?` → IRRELEVANT (Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0987)

### Advanced
- **Pass Rate:** 86%
- **Avg Relevance Score:** 0.664
- **Avg Search Score:** 0.0524
- **Issues (3):**
  - ❌ `How to use metaobjects in Shopify?` → IRRELEVANT (Only 1/5 keywords found; Expected ['theme_patterns', 'api_reference'], got ['troubleshooting', 'troubleshooting', 'liquid_reference']; Top score: 0.0333)
  - ❌ `How to implement store locator functionality?` → IRRELEVANT (Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liquid_reference', 'api_reference', 'api_reference']; Top score: 0.0325)
  - ❌ `How to use online store editor customization API?` → IRRELEVANT (2/5 keywords matched; Expected ['api_reference'], got ['liquid_reference', 'liquid_reference', 'troubleshooting']; Top score: 0.0401)

### Styling/CSS
- **Pass Rate:** 81%
- **Avg Relevance Score:** 0.485
- **Avg Search Score:** 0.0552
- **Issues (3):**
  - ❌ `How to use flexbox for Shopify layouts?` → IRRELEVANT (2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0463)
  - ❌ `How to add hover effects to product cards?` → IRRELEVANT (3/6 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubleshooting', 'api_reference', 'api_reference']; Top score: 0.0237)
  - ❌ `How to use media queries in Shopify themes?` → IRRELEVANT (Only 1/5 keywords found; Expected ['theme_patterns', 'best_practices'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0619)

### APIs
- **Pass Rate:** 81%
- **Avg Relevance Score:** 0.697
- **Avg Search Score:** 0.0562
- **Issues (4):**
  - ❌ `What is the Shopify Admin API?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'liquid_reference', 'code_examples']; Top score: 0.0620)
  - ❌ `How to use the Shopify GraphQL Admin API?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0320)
  - ❌ `What is the Shopify REST Admin API?` → IRRELEVANT (Only 1/6 keywords found; Expected ['api_reference'], got ['liquid_reference', 'liquid_reference', 'code_examples']; Top score: 0.0560)
  - ❌ `How to fetch metaobjects via the API?` → IRRELEVANT (3/5 keywords matched; Expected ['api_reference'], got ['troubleshooting', 'troubleshooting', 'troubleshooting']; Top score: 0.0290)

### Performance
- **Pass Rate:** 75%
- **Avg Relevance Score:** 0.488
- **Avg Search Score:** 0.0738
- **Issues (4):**
  - ❌ `How to improve Core Web Vitals for a Shopify store?` → IRRELEVANT (Only 2/7 keywords found; Expected ['best_practices'], got ['liquid_reference', 'api_reference', 'troubleshooting']; Top score: 0.0276)
  - ❌ `How to defer non-critical CSS in Shopify?` → IRRELEVANT (3/5 keywords matched; Expected ['best_practices'], got ['liquid_reference', 'troubleshooting', 'liquid_reference']; Top score: 0.0288)
  - ❌ `How to reduce Liquid render time?` → IRRELEVANT (2/5 keywords matched; Expected ['best_practices'], got ['api_reference', 'api_reference', 'liquid_reference']; Top score: 0.0405)
  - ❌ `How to minimize layout shifts in Shopify?` → IRRELEVANT (Only 1/5 keywords found; Expected ['best_practices'], got ['liquid_reference', 'api_reference', 'liquid_reference']; Top score: 0.0310)

## Top 20 Best-Performing Queries

| # | Score | Rating | Category | Query |
|---|-------|--------|----------|-------|
| 1 | 1.000 | RELEVANT | Liquid Reference | How do I use the forloop object in Liquid? |
| 2 | 1.000 | RELEVANT | Liquid Reference | What is the money_with_currency filter in Liquid? |
| 3 | 1.000 | RELEVANT | Liquid Reference | What does the split filter do in Liquid? |
| 4 | 1.000 | RELEVANT | Liquid Reference | How to use the where filter in Liquid? |
| 5 | 1.000 | RELEVANT | Liquid Reference | What is the image_url filter? |
| 6 | 1.000 | RELEVANT | Liquid Reference | Explain the date filter in Liquid |
| 7 | 1.000 | RELEVANT | Liquid Reference | How to use the assign tag in Liquid? |
| 8 | 1.000 | RELEVANT | Liquid Reference | What is the capture tag used for? |
| 9 | 1.000 | RELEVANT | Liquid Reference | How to use the increment and decrement tags? |
| 10 | 1.000 | RELEVANT | Liquid Reference | What is the tablerow tag in Liquid? |
| 11 | 1.000 | RELEVANT | Liquid Reference | How do Liquid comment tags work? |
| 12 | 1.000 | RELEVANT | Liquid Reference | How to use the url_encode filter? |
| 13 | 1.000 | RELEVANT | Liquid Reference | What is the handle property in Shopify Liquid? |
| 14 | 1.000 | RELEVANT | Liquid Reference | How to iterate over a collection's products in Liquid? |
| 15 | 1.000 | RELEVANT | Liquid Reference | What is the all_products object? |
| 16 | 1.000 | RELEVANT | Liquid Reference | How to use the map filter in Liquid? |
| 17 | 1.000 | RELEVANT | Liquid Reference | How does the content_for_header tag work? |
| 18 | 1.000 | RELEVANT | Liquid Reference | How to use the slice filter in Liquid? |
| 19 | 1.000 | RELEVANT | Theme Development | How to create a predictive search in Shopify? |
| 20 | 1.000 | RELEVANT | Product Pages | How to create a variant picker with swatches? |

## Top 20 Worst-Performing Queries

| # | Score | Rating | Category | Query | Reason |
|---|-------|--------|----------|-------|--------|
| 1 | 0.214 | IRRELEVANT | Performance | How to improve Core Web Vitals for a Shopify store? | Only 2/7 keywords found; Expected ['best_practices'], got ['liquid_reference', ' |
| 2 | 0.267 | IRRELEVANT | Cart/Checkout | How to implement a free shipping progress bar? | Only 1/6 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq |
| 3 | 0.280 | IRRELEVANT | APIs | How to use the Shopify GraphQL Admin API? | Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l |
| 4 | 0.280 | IRRELEVANT | Performance | How to minimize layout shifts in Shopify? | Only 1/5 keywords found; Expected ['best_practices'], got ['liquid_reference', ' |
| 5 | 0.280 | IRRELEVANT | Advanced | How to use metaobjects in Shopify? | Only 1/5 keywords found; Expected ['theme_patterns', 'api_reference'], got ['tro |
| 6 | 0.280 | IRRELEVANT | Advanced | How to implement store locator functionality? | Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq |
| 7 | 0.300 | IRRELEVANT | Styling/CSS | How to add hover effects to product cards? | 3/6 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubl |
| 8 | 0.340 | IRRELEVANT | APIs | How to fetch metaobjects via the API? | 3/5 keywords matched; Expected ['api_reference'], got ['troubleshooting', 'troub |
| 9 | 0.340 | IRRELEVANT | Performance | How to defer non-critical CSS in Shopify? | 3/5 keywords matched; Expected ['best_practices'], got ['liquid_reference', 'tro |
| 10 | 0.360 | IRRELEVANT | Cart/Checkout | How to use the cart/update.js endpoint? | 2/5 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubl |
| 11 | 0.360 | IRRELEVANT | Styling/CSS | How to use flexbox for Shopify layouts? | 2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liq |
| 12 | 0.360 | IRRELEVANT | Performance | How to reduce Liquid render time? | 2/5 keywords matched; Expected ['best_practices'], got ['api_reference', 'api_re |
| 13 | 0.360 | IRRELEVANT | Advanced | How to use online store editor customization API? | 2/5 keywords matched; Expected ['api_reference'], got ['liquid_reference', 'liqu |
| 14 | 0.367 | IRRELEVANT | APIs | What is the Shopify REST Admin API? | Only 1/6 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l |
| 15 | 0.380 | IRRELEVANT | Cart/Checkout | How to create a cart page with editable quantities? | Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq |
| 16 | 0.380 | IRRELEVANT | APIs | What is the Shopify Admin API? | Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l |
| 17 | 0.380 | IRRELEVANT | Styling/CSS | How to use media queries in Shopify themes? | Only 1/5 keywords found; Expected ['theme_patterns', 'best_practices'], got ['li |
| 18 | 0.380 | IRRELEVANT | Code Generation | Generate a multi-column section with icons | Only 1/5 keywords found; Expected ['code_examples', 'theme_patterns'], got ['api |
| 19 | 0.400 | PARTIAL | Theme Development | How to create a custom section in Shopify? | Only 1/4 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq |
| 20 | 0.400 | PARTIAL | Theme Development | How to create a custom template in Shopify? | Only 1/4 keywords found; Expected ['theme_patterns'], got ['code_examples', 'liq |

## Intent Detection Analysis

| Detected Intent | Count | Avg Relevance Score |
|-----------------|-------|---------------------|
| how_to | 159 | 0.661 |
| reference | 43 | 0.782 |
| debug | 16 | 0.776 |

## Collection Usage Analysis

| Collection | Times Targeted | Times in Results | Avg Score |
|------------|---------------|-----------------|-----------|
| liquid_reference | 218 | 353 | 0.0539 |
| api_reference | 135 | 120 | 0.0534 |
| troubleshooting | 135 | 91 | 0.0402 |
| theme_patterns | 67 | 57 | 0.0455 |
| code_examples | 50 | 28 | 0.0387 |
| best_practices | 16 | 5 | 0.0471 |

## Identified Gaps & Weak Areas

### Irrelevant Results (18 queries)

These queries returned results that don't match the topic:
- `How to implement a free shipping progress bar?` → got `liquid_reference`, expected `['theme_patterns', 'code_examples']`
- `How to use the cart/update.js endpoint?` → got `troubleshooting`, expected `['theme_patterns', 'code_examples']`
- `How to create a cart page with editable quantities?` → got `liquid_reference`, expected `['theme_patterns', 'code_examples']`
- `What is the Shopify Admin API?` → got `liquid_reference`, expected `['api_reference']`
- `How to use the Shopify GraphQL Admin API?` → got `liquid_reference`, expected `['api_reference']`
- `What is the Shopify REST Admin API?` → got `liquid_reference`, expected `['api_reference']`
- `How to fetch metaobjects via the API?` → got `troubleshooting`, expected `['api_reference']`
- `How to use flexbox for Shopify layouts?` → got `liquid_reference`, expected `['theme_patterns']`
- `How to add hover effects to product cards?` → got `troubleshooting`, expected `['theme_patterns', 'code_examples']`
- `How to use media queries in Shopify themes?` → got `liquid_reference`, expected `['theme_patterns', 'best_practices']`
- `How to improve Core Web Vitals for a Shopify store?` → got `liquid_reference`, expected `['best_practices']`
- `How to defer non-critical CSS in Shopify?` → got `liquid_reference`, expected `['best_practices']`
- `How to reduce Liquid render time?` → got `api_reference`, expected `['best_practices']`
- `How to minimize layout shifts in Shopify?` → got `liquid_reference`, expected `['best_practices']`
- `How to use metaobjects in Shopify?` → got `troubleshooting`, expected `['theme_patterns', 'api_reference']`
- `How to implement store locator functionality?` → got `liquid_reference`, expected `['theme_patterns', 'code_examples']`
- `How to use online store editor customization API?` → got `liquid_reference`, expected `['api_reference']`
- `Generate a multi-column section with icons` → got `api_reference`, expected `['code_examples', 'theme_patterns']`

### Queries with Weak Keyword Matching (18 queries)

Results were returned but didn't contain expected keywords:
- `How to implement a free shipping progress bar?` (score: 0.267) — Only 1/6 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq
- `How to use the cart/update.js endpoint?` (score: 0.360) — 2/5 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubl
- `How to create a cart page with editable quantities?` (score: 0.380) — Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['liq
- `What is the Shopify Admin API?` (score: 0.380) — Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l
- `How to use the Shopify GraphQL Admin API?` (score: 0.280) — Only 1/5 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l
- `What is the Shopify REST Admin API?` (score: 0.367) — Only 1/6 keywords found; Expected ['api_reference'], got ['liquid_reference', 'l
- `How to fetch metaobjects via the API?` (score: 0.340) — 3/5 keywords matched; Expected ['api_reference'], got ['troubleshooting', 'troub
- `How to use flexbox for Shopify layouts?` (score: 0.360) — 2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liq
- `How to add hover effects to product cards?` (score: 0.300) — 3/6 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['troubl
- `How to use media queries in Shopify themes?` (score: 0.380) — Only 1/5 keywords found; Expected ['theme_patterns', 'best_practices'], got ['li
- `How to improve Core Web Vitals for a Shopify store?` (score: 0.214) — Only 2/7 keywords found; Expected ['best_practices'], got ['liquid_reference', '
- `How to defer non-critical CSS in Shopify?` (score: 0.340) — 3/5 keywords matched; Expected ['best_practices'], got ['liquid_reference', 'tro
- `How to reduce Liquid render time?` (score: 0.360) — 2/5 keywords matched; Expected ['best_practices'], got ['api_reference', 'api_re
- `How to minimize layout shifts in Shopify?` (score: 0.280) — Only 1/5 keywords found; Expected ['best_practices'], got ['liquid_reference', '
- `How to use metaobjects in Shopify?` (score: 0.280) — Only 1/5 keywords found; Expected ['theme_patterns', 'api_reference'], got ['tro
- ... and 3 more

## Recommendations for Improvement

1. **Add content for underrepresented topics**: The following terms appear frequently in failing queries: `api` (5x), `admin` (3x), `rest` (2x), `graphql` (2x), `metaobject` (2x), `layout` (2x), `free` (1x), `shipping` (1x), `progress` (1x), `cart/update` (1x)
2. **Rebalance collection weights**: `liquid_reference` dominates results (54% of all top results). Other collections may be underrepresented.
3. **Add query expansion for Shopify-specific terms**: Many queries use terminology (e.g., 'Dawn theme', 'Online Store 2.0', 'checkout extensibility') that may not match document text exactly. Expand the synonym dictionary.
4. **Consider chunk size optimization**: Some results return code-heavy chunks that lack surrounding explanation. Ensure parent context is available for code-only chunks.

## Full Results Table

| # | Query | Intent | Collections | Score | Rating |
|---|-------|--------|-------------|-------|--------|
| 1 | What properties does the product object have in Liquid? | reference | liquid_reference, api_reference | 0.760 | RELEVANT |
| 2 | How do I use the forloop object in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 3 | What is the money_with_currency filter in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 4 | List all Liquid string filters | reference | liquid_reference, api_reference | 0.667 | RELEVANT |
| 5 | What does the split filter do in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 6 | How to use the where filter in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 7 | What is the collection object in Liquid? | reference | liquid_reference, api_reference | 0.940 | RELEVANT |
| 8 | How to access product.metafields in Liquid? | how_to | liquid_reference, theme_patterns | 0.800 | RELEVANT |
| 9 | What are Liquid control flow tags? | reference | liquid_reference, api_reference | 0.667 | RELEVANT |
| 10 | How does the paginate tag work in Liquid? | reference | liquid_reference, api_reference | 0.800 | RELEVANT |
| 11 | What is the image_url filter? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 12 | Explain the date filter in Liquid | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 13 | What properties does the variant object have? | reference | liquid_reference, api_reference | 0.733 | RELEVANT |
| 14 | How to use the assign tag in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 15 | What is the capture tag used for? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 16 | How to use the increment and decrement tags? | how_to | liquid_reference, theme_patterns | 1.000 | RELEVANT |
| 17 | What is the tablerow tag in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 18 | How do Liquid comment tags work? | how_to | liquid_reference, theme_patterns | 1.000 | RELEVANT |
| 19 | What is the raw tag in Liquid? | reference | liquid_reference, api_reference | 0.900 | RELEVANT |
| 20 | What does the default filter do? | reference | liquid_reference, api_reference | 0.800 | RELEVANT |
| 21 | How to use the url_encode filter? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 22 | What is the handle property in Shopify Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 23 | How to iterate over a collection's products in Liquid? | how_to | liquid_reference, theme_patterns | 1.000 | RELEVANT |
| 24 | What is the all_products object? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 25 | How to use the map filter in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 26 | What is the linklists object? | reference | liquid_reference, api_reference | 0.940 | RELEVANT |
| 27 | How to access the current page info in Liquid? | how_to | liquid_reference, theme_patterns | 0.700 | RELEVANT |
| 28 | What are the request object properties? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 29 | How does the content_for_header tag work? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 30 | What are Liquid math filters? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 31 | How to use the slice filter in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 32 | What is the shop object in Liquid? | reference | liquid_reference, api_reference | 0.680 | RELEVANT |
| 33 | How to create a custom section in Shopify? | how_to | liquid_reference, theme_patterns | 0.400 | PARTIAL |
| 34 | What is the section schema in Shopify themes? | reference | liquid_reference, api_reference | 0.700 | RELEVANT |
| 35 | How do templates work in Shopify Online Store 2.0? | how_to | liquid_reference, theme_patterns | 0.800 | RELEVANT |
| 36 | How to create a custom template in Shopify? | how_to | liquid_reference, theme_patterns | 0.400 | PARTIAL |
| 37 | What is the difference between sections and snippets? | reference | liquid_reference, api_reference | 0.620 | PARTIAL |
| 38 | How to use dynamic sources in section settings? | how_to | liquid_reference, theme_patterns | 0.760 | RELEVANT |
| 39 | How does the render tag differ from include? | reference | liquid_reference, api_reference | 0.820 | RELEVANT |
| 40 | How to create section blocks in Shopify? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 41 | What layout files are available in Shopify themes? | how_to | liquid_reference, theme_patterns | 0.800 | RELEVANT |
| 42 | How to add custom settings to a theme? | how_to | liquid_reference, theme_patterns | 0.840 | RELEVANT |
| 43 | How to create a predictive search in Shopify? | how_to | liquid_reference, theme_patterns | 1.000 | RELEVANT |
| 44 | What are theme app extensions? | reference | liquid_reference, api_reference | 0.520 | PARTIAL |
| 45 | How to use app blocks in Shopify themes? | how_to | liquid_reference, theme_patterns | 0.820 | RELEVANT |
| 46 | How to structure a Shopify theme directory? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 47 | How do locales work in Shopify themes? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 48 | How to add translations to a Shopify theme? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 49 | What are section groups in Online Store 2.0? | reference | liquid_reference, api_reference | 0.460 | PARTIAL |
| 50 | How to use metafield definitions in themes? | how_to | liquid_reference, theme_patterns | 0.760 | RELEVANT |
| 51 | How do I create a dropdown menu in Shopify? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 52 | How to add a custom font to a Shopify theme? | how_to | liquid_reference, theme_patterns | 0.700 | RELEVANT |
| 53 | How to make a Shopify section with multiple block types? | how_to | liquid_reference, theme_patterns | 0.700 | RELEVANT |
| 54 | How to add settings_schema.json settings? | how_to | liquid_reference, theme_patterns | 0.700 | RELEVANT |
| 55 | How do theme presets work? | how_to | liquid_reference, theme_patterns | 0.660 | RELEVANT |
| 56 | How to use the stylesheet tag in sections? | reference | liquid_reference, api_reference | 0.700 | RELEVANT |
| 57 | How to implement a product quick view? | how_to | liquid_reference, theme_patterns | 0.820 | RELEVANT |
| 58 | What is Dawn theme and how is it structured? | reference | code_examples, liquid_reference | 0.740 | RELEVANT |
| 59 | How to create an announcement bar section? | how_to | liquid_reference, theme_patterns | 0.740 | RELEVANT |
| 60 | How to implement a slideshow section? | how_to | liquid_reference, theme_patterns | 0.740 | RELEVANT |
| 61 | How to use CSS variables in Shopify themes? | how_to | liquid_reference, theme_patterns | 0.440 | PARTIAL |
| 62 | What is the assets directory used for in Shopify? | reference | code_examples, liquid_reference | 0.460 | PARTIAL |
| 63 | How to add a newsletter signup form? | how_to | liquid_reference, theme_patterns | 0.820 | RELEVANT |
| 64 | How to implement an AJAX cart in Shopify? | how_to | liquid_reference, theme_patterns | 0.633 | PARTIAL |
| 65 | How to create a cart drawer in Shopify? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 66 | How to add line item properties to cart items? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 67 | How to use the cart/add.js endpoint? | how_to | liquid_reference, theme_patterns | 0.480 | PARTIAL |
| 68 | What is the cart object in Liquid? | reference | code_examples, liquid_reference | 0.680 | RELEVANT |
| 69 | How to implement quantity selectors for cart items? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 70 | How to add a gift message to cart? | how_to | liquid_reference, theme_patterns | 0.460 | PARTIAL |
| 71 | How to use cart attributes in Shopify? | reference | code_examples, liquid_reference | 0.600 | PARTIAL |
| 72 | How to implement a free shipping progress bar? | how_to | liquid_reference, theme_patterns | 0.267 | IRRELEVANT |
| 73 | How do checkout extensions work in Shopify? | how_to | liquid_reference, theme_patterns | 0.900 | RELEVANT |
| 74 | How to redirect to checkout after adding to cart? | how_to | liquid_reference, theme_patterns | 0.520 | PARTIAL |
| 75 | What is the cart/change.js endpoint? | reference | code_examples, liquid_reference | 0.620 | PARTIAL |
| 76 | How to display cart totals dynamically? | how_to | liquid_reference, theme_patterns | 0.460 | PARTIAL |
| 77 | How to implement upsells in the cart? | how_to | liquid_reference, theme_patterns | 0.580 | PARTIAL |
| 78 | How to calculate shipping rates in the cart? | how_to | liquid_reference, theme_patterns | 0.660 | RELEVANT |
| 79 | How to handle cart errors in Shopify? | how_to | troubleshooting, liquid_reference | 0.660 | RELEVANT |
| 80 | How to add a discount code field to the cart? | how_to | troubleshooting, liquid_reference | 0.740 | RELEVANT |
| 81 | How to implement a mini cart popup? | how_to | troubleshooting, liquid_reference | 0.580 | PARTIAL |
| 82 | How to use the cart/update.js endpoint? | how_to | troubleshooting, liquid_reference | 0.360 | IRRELEVANT |
| 83 | How to create a cart page with editable quantities? | how_to | troubleshooting, liquid_reference | 0.380 | IRRELEVANT |
| 84 | How does the cart template work in Online Store 2.0? | how_to | troubleshooting, liquid_reference | 0.740 | RELEVANT |
| 85 | How to display product variants on the product page? | how_to | troubleshooting, liquid_reference | 0.920 | RELEVANT |
| 86 | How to create a variant picker with swatches? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 87 | How to display product metafields on the product page? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 88 | How to add structured data / JSON-LD to product pages? | how_to | troubleshooting, liquid_reference | 0.867 | RELEVANT |
| 89 | How to implement a product image gallery? | how_to | troubleshooting, liquid_reference | 0.920 | RELEVANT |
| 90 | How to show related products on the product page? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 91 | How to change the product image when a variant is selected? | how_to | troubleshooting, liquid_reference | 0.920 | RELEVANT |
| 92 | How to display product reviews on the product page? | how_to | troubleshooting, liquid_reference | 0.460 | PARTIAL |
| 93 | How to show product availability (in stock/out of stock)? | how_to | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 94 | How to implement a product zoom feature? | how_to | troubleshooting, liquid_reference | 0.680 | RELEVANT |
| 95 | How to display product tags in Shopify? | how_to | troubleshooting, liquid_reference | 0.440 | PARTIAL |
| 96 | How to add a size chart to a product page? | how_to | troubleshooting, liquid_reference | 0.920 | RELEVANT |
| 97 | How to show compare at prices? | how_to | troubleshooting, liquid_reference | 0.800 | RELEVANT |
| 98 | How to implement product tabs for description and details? | how_to | troubleshooting, liquid_reference | 0.740 | RELEVANT |
| 99 | How to display product media (3D models, video)? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 100 | How to handle products with many variants in Liquid? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 101 | How to create a product page with a sticky add to cart? | how_to | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 102 | How to use product.selected_or_first_available_variant? | how_to | troubleshooting, liquid_reference | 0.800 | RELEVANT |
| 103 | How to show product inventory quantity? | how_to | troubleshooting, liquid_reference | 0.820 | RELEVANT |
| 104 | How to implement wishlist functionality? | how_to | troubleshooting, liquid_reference | 0.580 | PARTIAL |
| 105 | How to add custom product badges (sale, new, bestseller)? | how_to | troubleshooting, liquid_reference | 0.400 | PARTIAL |
| 106 | What is the Shopify Admin API? | reference | code_examples, liquid_reference | 0.380 | IRRELEVANT |
| 107 | How to use the Storefront API? | how_to | api_reference, troubleshooting | 0.740 | RELEVANT |
| 108 | How to fetch products with the Storefront API? | how_to | api_reference, troubleshooting | 0.520 | PARTIAL |
| 109 | How to use the Ajax API in Shopify? | how_to | api_reference, troubleshooting | 0.900 | RELEVANT |
| 110 | What webhooks are available in Shopify? | how_to | api_reference, troubleshooting | 0.840 | RELEVANT |
| 111 | How to authenticate with the Shopify API? | how_to | api_reference, troubleshooting | 0.567 | PARTIAL |
| 112 | How to create a product using the Admin API? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 113 | What is the Section Rendering API? | reference | code_examples, liquid_reference | 0.833 | RELEVANT |
| 114 | How to use the product recommendations endpoint? | how_to | api_reference, troubleshooting | 1.000 | RELEVANT |
| 115 | How to use the Shopify GraphQL Admin API? | how_to | api_reference, troubleshooting | 0.280 | IRRELEVANT |
| 116 | How to get customer data from the Storefront API? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 117 | How to handle pagination in the Admin API? | how_to | api_reference, troubleshooting | 0.800 | RELEVANT |
| 118 | What is the Shopify REST Admin API? | reference | code_examples, liquid_reference | 0.367 | IRRELEVANT |
| 119 | How to use metafield APIs? | how_to | api_reference, troubleshooting | 0.680 | RELEVANT |
| 120 | How to listen for order webhooks? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 121 | How to use the search.json endpoint? | how_to | api_reference, troubleshooting | 1.000 | RELEVANT |
| 122 | How to use multipass for SSO? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 123 | How to fetch collections via Storefront API? | how_to | api_reference, troubleshooting | 0.900 | RELEVANT |
| 124 | How to use the Shopify Cart API? | how_to | api_reference, troubleshooting | 0.400 | PARTIAL |
| 125 | How to fetch metaobjects via the API? | how_to | api_reference, troubleshooting | 0.340 | IRRELEVANT |
| 126 | How to create a draft order via Admin API? | how_to | api_reference, troubleshooting | 1.000 | RELEVANT |
| 127 | How to make a responsive product grid in Shopify? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 128 | How to use CSS Grid for a Shopify collection page? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 129 | How to add animations to a Shopify theme? | how_to | api_reference, troubleshooting | 0.460 | PARTIAL |
| 130 | How to implement dark mode in a Shopify theme? | how_to | api_reference, troubleshooting | 0.400 | PARTIAL |
| 131 | How to customize the Dawn theme CSS? | how_to | api_reference, troubleshooting | 0.440 | PARTIAL |
| 132 | How to use Tailwind CSS with Shopify? | how_to | api_reference, troubleshooting | 0.520 | PARTIAL |
| 133 | How to make a sticky header in Shopify? | how_to | api_reference, troubleshooting | 0.520 | PARTIAL |
| 134 | How to add a custom scrollbar style? | how_to | api_reference, troubleshooting | 0.440 | PARTIAL |
| 135 | How to implement a hamburger menu for mobile? | how_to | api_reference, troubleshooting | 0.520 | PARTIAL |
| 136 | How to style the Shopify cart page? | how_to | api_reference, troubleshooting | 0.540 | PARTIAL |
| 137 | How to create a responsive hero banner? | how_to | api_reference, troubleshooting | 0.460 | PARTIAL |
| 138 | How to use flexbox for Shopify layouts? | how_to | api_reference, troubleshooting | 0.360 | IRRELEVANT |
| 139 | How to add hover effects to product cards? | how_to | api_reference, troubleshooting | 0.300 | IRRELEVANT |
| 140 | How to customize form styles in Shopify? | how_to | api_reference, troubleshooting | 0.567 | PARTIAL |
| 141 | How to implement a masonry grid layout? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 142 | How to use media queries in Shopify themes? | how_to | api_reference, troubleshooting | 0.380 | IRRELEVANT |
| 143 | How to lazy load images in Shopify? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 144 | How to preload critical resources in Shopify? | how_to | api_reference, troubleshooting | 0.540 | PARTIAL |
| 145 | How to improve Core Web Vitals for a Shopify store? | how_to | api_reference, troubleshooting | 0.214 | IRRELEVANT |
| 146 | How to use the Section Rendering API for performance? | how_to | api_reference, troubleshooting | 0.567 | PARTIAL |
| 147 | How to reduce JavaScript bundle size in Shopify? | how_to | api_reference, troubleshooting | 0.500 | PARTIAL |
| 148 | How to optimize images in Shopify themes? | how_to | api_reference, troubleshooting | 0.500 | PARTIAL |
| 149 | How to defer non-critical CSS in Shopify? | how_to | api_reference, troubleshooting | 0.340 | IRRELEVANT |
| 150 | What is the best way to load third-party scripts in Shopify? | reference | code_examples, liquid_reference | 0.460 | PARTIAL |
| 151 | How to implement responsive images with srcset? | how_to | api_reference, troubleshooting | 0.700 | RELEVANT |
| 152 | How to use native lazy loading in Shopify themes? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 153 | How to reduce Liquid render time? | how_to | api_reference, troubleshooting | 0.360 | IRRELEVANT |
| 154 | How to cache Shopify API responses? | how_to | api_reference, troubleshooting | 0.420 | PARTIAL |
| 155 | How to use content_for_header efficiently? | how_to | api_reference, troubleshooting | 0.600 | PARTIAL |
| 156 | How to minimize layout shifts in Shopify? | how_to | api_reference, troubleshooting | 0.280 | IRRELEVANT |
| 157 | How to optimize collection page loading speed? | how_to | api_reference, troubleshooting | 0.460 | PARTIAL |
| 158 | How to use async/defer for JavaScript in Shopify? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 159 | Why is my Liquid variable returning nil? | debug | troubleshooting, liquid_reference | 0.810 | RELEVANT |
| 160 | How to debug Liquid code in Shopify? | how_to | api_reference, troubleshooting | 0.430 | PARTIAL |
| 161 | Why is my section not showing up in the theme editor? | debug | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 162 | Why is my product form not submitting? | debug | troubleshooting, liquid_reference | 0.820 | RELEVANT |
| 163 | How to fix 'Liquid error: Memory limits exceeded'? | debug | troubleshooting, liquid_reference | 0.440 | PARTIAL |
| 164 | Why are my theme changes not appearing? | how_to | api_reference, troubleshooting | 0.580 | PARTIAL |
| 165 | How to fix 'Too many redirects' error in Shopify? | debug | troubleshooting, liquid_reference | 0.610 | PARTIAL |
| 166 | Why is my JavaScript not working in Shopify? | debug | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 167 | How to fix broken images in a Shopify theme? | debug | troubleshooting, liquid_reference | 0.840 | RELEVANT |
| 168 | Why is the add to cart button not working? | debug | troubleshooting, liquid_reference | 0.740 | RELEVANT |
| 169 | Why is my Shopify section schema invalid? | debug | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 170 | How to fix '404 Not Found' for theme assets? | how_to | api_reference, troubleshooting | 0.640 | PARTIAL |
| 171 | Why does my Liquid for loop show nothing? | debug | troubleshooting, liquid_reference | 0.467 | PARTIAL |
| 172 | How to fix CORS errors with the Shopify API? | debug | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 173 | Why are my metafields not showing up? | how_to | api_reference, troubleshooting | 0.680 | RELEVANT |
| 174 | How to troubleshoot slow Shopify theme performance? | how_to | api_reference, troubleshooting | 0.560 | PARTIAL |
| 175 | Why is my variant picker not updating the price? | debug | troubleshooting, liquid_reference | 0.760 | RELEVANT |
| 176 | How to fix 'Argument error in tag for' in Liquid? | debug | troubleshooting, liquid_reference | 0.820 | RELEVANT |
| 177 | Why is my Shopify form showing validation errors? | debug | troubleshooting, liquid_reference | 0.970 | RELEVANT |
| 178 | How to debug the Shopify Ajax API responses? | how_to | api_reference, troubleshooting | 0.740 | RELEVANT |
| 179 | Why is my collection filter not working? | debug | troubleshooting, liquid_reference | 1.000 | RELEVANT |
| 180 | How to fix undefined JavaScript errors in Shopify? | debug | troubleshooting, liquid_reference | 0.540 | PARTIAL |
| 181 | How to use metaobjects in Shopify? | how_to | api_reference, troubleshooting | 0.280 | IRRELEVANT |
| 182 | How do Shopify Markets work? | how_to | api_reference, troubleshooting | 0.620 | PARTIAL |
| 183 | How to implement B2B features in Shopify? | how_to | api_reference, troubleshooting | 0.760 | RELEVANT |
| 184 | How to use Shopify Multipass for authentication? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 185 | How to create app blocks for Shopify themes? | how_to | api_reference, troubleshooting | 0.520 | PARTIAL |
| 186 | How to build a theme app extension? | how_to | api_reference, troubleshooting | 0.540 | PARTIAL |
| 187 | How to use Shopify Functions for discounts? | how_to | api_reference, troubleshooting | 0.920 | RELEVANT |
| 188 | How to implement custom storefronts with Hydrogen? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 189 | How to use the Customer Account API? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 190 | How to implement multi-currency in Shopify? | how_to | api_reference, troubleshooting | 0.900 | RELEVANT |
| 191 | How to use Shopify Flow for automation? | how_to | api_reference, troubleshooting | 0.680 | RELEVANT |
| 192 | How to implement product bundles in Shopify? | how_to | api_reference, troubleshooting | 0.440 | PARTIAL |
| 193 | How to use the Shopify CLI for theme development? | how_to | api_reference, troubleshooting | 0.500 | PARTIAL |
| 194 | How to create a custom storefront with the Storefront API? | how_to | api_reference, troubleshooting | 0.920 | RELEVANT |
| 195 | How to implement subscription products in Shopify? | how_to | api_reference, troubleshooting | 0.580 | PARTIAL |
| 196 | How to use Shopify Pixels for analytics? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 197 | How to implement customer-specific pricing? | how_to | api_reference, troubleshooting | 0.820 | RELEVANT |
| 198 | How to use the Shopify Checkout Extensibility? | how_to | api_reference, troubleshooting | 0.740 | RELEVANT |
| 199 | How to implement store locator functionality? | how_to | api_reference, troubleshooting | 0.280 | IRRELEVANT |
| 200 | How to use online store editor customization API? | how_to | api_reference, troubleshooting | 0.360 | IRRELEVANT |
| 201 | How to create a headless Shopify storefront? | how_to | api_reference, troubleshooting | 0.800 | RELEVANT |
| 202 | Build me a product card section with image, title, and price | how_to | api_reference, troubleshooting | 0.700 | RELEVANT |
| 203 | Generate a Liquid snippet for a star rating display | how_to | api_reference, troubleshooting | 0.510 | PARTIAL |
| 204 | Create a section for a hero banner with text overlay | how_to | api_reference, troubleshooting | 0.583 | PARTIAL |
| 205 | Build me a color swatch variant picker in Liquid | how_to | api_reference, troubleshooting | 0.683 | RELEVANT |
| 206 | Generate a Liquid template for a FAQ page | how_to | api_reference, troubleshooting | 0.590 | PARTIAL |
| 207 | Create a section for featured collections grid | how_to | api_reference, troubleshooting | 0.700 | RELEVANT |
| 208 | Build me an AJAX add to cart form | how_to | api_reference, troubleshooting | 0.517 | PARTIAL |
| 209 | Generate a responsive image gallery with thumbnails | how_to | api_reference, troubleshooting | 0.590 | PARTIAL |
| 210 | Create a section for customer testimonials | how_to | api_reference, troubleshooting | 0.590 | PARTIAL |
| 211 | Build me a mega menu navigation | how_to | api_reference, troubleshooting | 0.510 | PARTIAL |
| 212 | Generate a product comparison table in Liquid | how_to | api_reference, troubleshooting | 0.510 | PARTIAL |
| 213 | Create a section for an image with text layout | how_to | api_reference, troubleshooting | 0.670 | RELEVANT |
| 214 | Build me a collection filter sidebar | reference | code_examples, liquid_reference | 0.570 | PARTIAL |
| 215 | Generate a Liquid snippet for breadcrumb navigation | how_to | api_reference, troubleshooting | 0.410 | PARTIAL |
| 216 | Create a custom product page template with tabs | how_to | api_reference, troubleshooting | 0.670 | RELEVANT |
| 217 | Build me a newsletter popup modal | how_to | api_reference, troubleshooting | 0.590 | PARTIAL |
| 218 | Generate a multi-column section with icons | how_to | api_reference, troubleshooting | 0.380 | IRRELEVANT |

---
*Report generated by test_rag_comprehensive.py on 2026-02-09 12:45:42*