# Enhanced RAG Search Engine — Comprehensive Test Report

**Generated:** 2026-02-09 12:57:46
**Total Queries:** 218
**Execution Time:** 197.3s (0.90s/query)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Overall Pass Rate** (RELEVANT + PARTIAL) | **95.0%** (207/218) |
| RELEVANT | 165 (75.7%) |
| PARTIAL | 42 (19.3%) |
| IRRELEVANT | 11 (5.0%) |
| NO_RESULTS | 0 (0.0%) |
| ERRORS | 0 |
| **Avg Relevance Score** | **0.758** (0-1 scale) |
| **Avg Top-1 Search Score** | **0.0627** |
| Queries/Second | 1.1 |

### Rating Distribution
```
🟢 RELEVANT     █████████████████████████████████████░░░░░░░░░░░░░ 165 (75.7%)
🟡 PARTIAL      █████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  42 (19.3%)
🔴 IRRELEVANT   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  11 (5.0%)
⚫ NO_RESULTS   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0 (0.0%)
```

## Per-Category Breakdown

| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |
|----------|-------|----------|---------|------------|------------|-----------|-----------|
| Liquid Reference | 32 | 24 (75%) | 8 (25%) | 0 (0%) | 0 | **100%** | 0.810 |
| Product Pages | 21 | 19 (90%) | 2 (10%) | 0 (0%) | 0 | **100%** | 0.840 |
| Styling/CSS | 16 | 13 (81%) | 3 (19%) | 0 (0%) | 0 | **100%** | 0.734 |
| Performance | 16 | 7 (44%) | 9 (56%) | 0 (0%) | 0 | **100%** | 0.691 |
| Code Generation | 17 | 14 (82%) | 3 (18%) | 0 (0%) | 0 | **100%** | 0.830 |
| Troubleshooting | 22 | 14 (64%) | 7 (32%) | 1 (5%) | 0 | **95%** | 0.711 |
| Cart/Checkout | 21 | 19 (90%) | 1 (5%) | 1 (5%) | 0 | **95%** | 0.756 |
| APIs | 21 | 19 (90%) | 1 (5%) | 1 (5%) | 0 | **95%** | 0.799 |
| Theme Development | 31 | 25 (81%) | 3 (10%) | 3 (10%) | 0 | **90%** | 0.765 |
| Advanced | 21 | 11 (52%) | 5 (24%) | 5 (24%) | 0 | **76%** | 0.609 |

### Liquid Reference
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.810
- **Avg Search Score:** 0.0840

### Product Pages
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.840
- **Avg Search Score:** 0.0729

### Styling/CSS
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.734
- **Avg Search Score:** 0.0495

### Performance
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.691
- **Avg Search Score:** 0.0733

### Code Generation
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.830
- **Avg Search Score:** 0.0756

### Troubleshooting
- **Pass Rate:** 95%
- **Avg Relevance Score:** 0.711
- **Avg Search Score:** 0.0519
- **Issues (1):**
  - ❌ `Why does my Liquid for loop show nothing?` → IRRELEVANT (2/6 keywords matched; Expected ['troubleshooting'], got ['theme_patterns', 'liquid_reference', 'theme_patterns']; Top score: 0.0429)

### Cart/Checkout
- **Pass Rate:** 95%
- **Avg Relevance Score:** 0.756
- **Avg Search Score:** 0.0513
- **Issues (1):**
  - ❌ `What is the cart/change.js endpoint?` → IRRELEVANT (Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['api_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0781)

### APIs
- **Pass Rate:** 95%
- **Avg Relevance Score:** 0.799
- **Avg Search Score:** 0.0649
- **Issues (1):**
  - ❌ `How to authenticate with the Shopify API?` → IRRELEVANT (Only 1/6 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0425)

### Theme Development
- **Pass Rate:** 90%
- **Avg Relevance Score:** 0.765
- **Avg Search Score:** 0.0549
- **Issues (3):**
  - ❌ `How to create a custom template in Shopify?` → IRRELEVANT (Only 1/4 keywords found; Expected ['theme_patterns'], got ['code_examples', 'code_examples', 'liquid_reference']; Top score: 0.0304)
  - ❌ `What are theme app extensions?` → IRRELEVANT (2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liquid_reference', 'api_reference', 'api_reference']; Top score: 0.0419)
  - ❌ `What are section groups in Online Store 2.0?` → IRRELEVANT (2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liquid_reference', 'liquid_reference']; Top score: 0.0427)

### Advanced
- **Pass Rate:** 76%
- **Avg Relevance Score:** 0.609
- **Avg Search Score:** 0.0436
- **Issues (5):**
  - ❌ `How do Shopify Markets work?` → IRRELEVANT (2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liquid_reference', 'code_examples', 'api_reference']; Top score: 0.0421)
  - ❌ `How to use Shopify Flow for automation?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'liquid_reference']; Top score: 0.0387)
  - ❌ `How to implement subscription products in Shopify?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0354)
  - ❌ `How to use Shopify Pixels for analytics?` → IRRELEVANT (2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0485)
  - ❌ `How to use online store editor customization API?` → IRRELEVANT (2/5 keywords matched; Expected ['api_reference'], got ['code_examples', 'theme_patterns', 'theme_patterns']; Top score: 0.0343)

## Top 20 Best-Performing Queries

| # | Score | Rating | Category | Query |
|---|-------|--------|----------|-------|
| 1 | 1.000 | RELEVANT | Liquid Reference | How do I use the forloop object in Liquid? |
| 2 | 1.000 | RELEVANT | Liquid Reference | What is the money_with_currency filter in Liquid? |
| 3 | 1.000 | RELEVANT | Liquid Reference | What does the split filter do in Liquid? |
| 4 | 1.000 | RELEVANT | Liquid Reference | What is the image_url filter? |
| 5 | 1.000 | RELEVANT | Liquid Reference | Explain the date filter in Liquid |
| 6 | 1.000 | RELEVANT | Liquid Reference | What is the capture tag used for? |
| 7 | 1.000 | RELEVANT | Liquid Reference | How to use the increment and decrement tags? |
| 8 | 1.000 | RELEVANT | Liquid Reference | What is the tablerow tag in Liquid? |
| 9 | 1.000 | RELEVANT | Liquid Reference | How do Liquid comment tags work? |
| 10 | 1.000 | RELEVANT | Liquid Reference | How to use the url_encode filter? |
| 11 | 1.000 | RELEVANT | Liquid Reference | What is the handle property in Shopify Liquid? |
| 12 | 1.000 | RELEVANT | Liquid Reference | What is the all_products object? |
| 13 | 1.000 | RELEVANT | Liquid Reference | What are Liquid math filters? |
| 14 | 1.000 | RELEVANT | Theme Development | How to create a custom section in Shopify? |
| 15 | 1.000 | RELEVANT | Theme Development | How to create section blocks in Shopify? |
| 16 | 1.000 | RELEVANT | Theme Development | How to create a predictive search in Shopify? |
| 17 | 1.000 | RELEVANT | Theme Development | How to add settings_schema.json settings? |
| 18 | 1.000 | RELEVANT | Cart/Checkout | How do checkout extensions work in Shopify? |
| 19 | 1.000 | RELEVANT | Product Pages | How to create a variant picker with swatches? |
| 20 | 1.000 | RELEVANT | Product Pages | How to show product availability (in stock/out of stock)? |

## Top 20 Worst-Performing Queries

| # | Score | Rating | Category | Query | Reason |
|---|-------|--------|----------|-------|--------|
| 1 | 0.267 | IRRELEVANT | APIs | How to authenticate with the Shopify API? | Only 1/6 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the |
| 2 | 0.280 | IRRELEVANT | Advanced | How to use Shopify Flow for automation? | Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the |
| 3 | 0.280 | IRRELEVANT | Advanced | How to implement subscription products in Shopify? | Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the |
| 4 | 0.300 | IRRELEVANT | Theme Development | How to create a custom template in Shopify? | Only 1/4 keywords found; Expected ['theme_patterns'], got ['code_examples', 'cod |
| 5 | 0.333 | IRRELEVANT | Troubleshooting | Why does my Liquid for loop show nothing? | 2/6 keywords matched; Expected ['troubleshooting'], got ['theme_patterns', 'liqu |
| 6 | 0.360 | IRRELEVANT | Theme Development | What are theme app extensions? | 2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liqui |
| 7 | 0.360 | IRRELEVANT | Theme Development | What are section groups in Online Store 2.0? | 2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liq |
| 8 | 0.360 | IRRELEVANT | Advanced | How do Shopify Markets work? | 2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liqui |
| 9 | 0.360 | IRRELEVANT | Advanced | How to use Shopify Pixels for analytics? | 2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns', 'theme_ |
| 10 | 0.360 | IRRELEVANT | Advanced | How to use online store editor customization API? | 2/5 keywords matched; Expected ['api_reference'], got ['code_examples', 'theme_p |
| 11 | 0.380 | IRRELEVANT | Cart/Checkout | What is the cart/change.js endpoint? | Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['api |
| 12 | 0.400 | PARTIAL | Liquid Reference | How to use the where filter in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_patterns', ' |
| 13 | 0.400 | PARTIAL | Liquid Reference | How to access product.metafields in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['best_practices', ' |
| 14 | 0.400 | PARTIAL | Liquid Reference | How does the paginate tag work in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['code_examples', 't |
| 15 | 0.440 | PARTIAL | Theme Development | What is Dawn theme and how is it structured? | 3/5 keywords matched; Expected ['theme_patterns', 'code_examples'], got ['liquid |
| 16 | 0.440 | PARTIAL | APIs | How to listen for order webhooks? | 3/5 keywords matched; Expected ['api_reference'], got ['best_practices', 'code_e |
| 17 | 0.440 | PARTIAL | Troubleshooting | How to fix 'Liquid error: Memory limits exceeded'? | 3/5 keywords matched; Expected ['troubleshooting'], got ['best_practices', 'best |
| 18 | 0.440 | PARTIAL | Troubleshooting | Why is my JavaScript not working in Shopify? | 3/5 keywords matched; Expected ['troubleshooting'], got ['liquid_reference', 'li |
| 19 | 0.460 | PARTIAL | Theme Development | What is the assets directory used for in Shopify? | 2/5 keywords matched; Expected ['theme_patterns'], got ['api_reference', 'liquid |
| 20 | 0.460 | PARTIAL | Troubleshooting | How to fix undefined JavaScript errors in Shopify? | 2/5 keywords matched; Expected ['troubleshooting'], got ['liquid_reference', 'be |

## Intent Detection Analysis

| Detected Intent | Count | Avg Relevance Score |
|-----------------|-------|---------------------|
| how_to | 143 | 0.753 |
| reference | 30 | 0.772 |
| debug | 21 | 0.729 |
| code_gen | 20 | 0.793 |
| comparison | 3 | 0.767 |
| architecture | 1 | 0.900 |

## Collection Usage Analysis

| Collection | Times Targeted | Times in Results | Avg Score |
|------------|---------------|-----------------|-----------|
| theme_patterns | 174 | 297 | 0.0506 |
| liquid_reference | 174 | 120 | 0.0564 |
| code_examples | 214 | 92 | 0.0483 |
| api_reference | 74 | 71 | 0.0515 |
| best_practices | 188 | 43 | 0.0438 |
| troubleshooting | 23 | 31 | 0.0449 |

## Identified Gaps & Weak Areas

### Irrelevant Results (11 queries)

These queries returned results that don't match the topic:
- `How to create a custom template in Shopify?` → got `code_examples`, expected `['theme_patterns']`
- `What are theme app extensions?` → got `liquid_reference`, expected `['theme_patterns', 'best_practices']`
- `What are section groups in Online Store 2.0?` → got `liquid_reference`, expected `['theme_patterns']`
- `What is the cart/change.js endpoint?` → got `api_reference`, expected `['theme_patterns', 'code_examples']`
- `How to authenticate with the Shopify API?` → got `theme_patterns`, expected `['api_reference']`
- `Why does my Liquid for loop show nothing?` → got `theme_patterns`, expected `['troubleshooting']`
- `How do Shopify Markets work?` → got `liquid_reference`, expected `['theme_patterns', 'best_practices']`
- `How to use Shopify Flow for automation?` → got `theme_patterns`, expected `['api_reference']`
- `How to implement subscription products in Shopify?` → got `theme_patterns`, expected `['api_reference']`
- `How to use Shopify Pixels for analytics?` → got `theme_patterns`, expected `['api_reference']`
- `How to use online store editor customization API?` → got `code_examples`, expected `['api_reference']`

### Queries with Weak Keyword Matching (11 queries)

Results were returned but didn't contain expected keywords:
- `How to create a custom template in Shopify?` (score: 0.300) — Only 1/4 keywords found; Expected ['theme_patterns'], got ['code_examples', 'cod
- `What are theme app extensions?` (score: 0.360) — 2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liqui
- `What are section groups in Online Store 2.0?` (score: 0.360) — 2/5 keywords matched; Expected ['theme_patterns'], got ['liquid_reference', 'liq
- `What is the cart/change.js endpoint?` (score: 0.380) — Only 1/5 keywords found; Expected ['theme_patterns', 'code_examples'], got ['api
- `How to authenticate with the Shopify API?` (score: 0.267) — Only 1/6 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the
- `Why does my Liquid for loop show nothing?` (score: 0.333) — 2/6 keywords matched; Expected ['troubleshooting'], got ['theme_patterns', 'liqu
- `How do Shopify Markets work?` (score: 0.360) — 2/5 keywords matched; Expected ['theme_patterns', 'best_practices'], got ['liqui
- `How to use Shopify Flow for automation?` (score: 0.280) — Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the
- `How to implement subscription products in Shopify?` (score: 0.280) — Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'the
- `How to use Shopify Pixels for analytics?` (score: 0.360) — 2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns', 'theme_
- `How to use online store editor customization API?` (score: 0.360) — 2/5 keywords matched; Expected ['api_reference'], got ['code_examples', 'theme_p

## Recommendations for Improvement

1. **Add content for underrepresented topics**: The following terms appear frequently in failing queries: `api` (2x), `template` (1x), `json` (1x), `custom` (1x), `app` (1x), `extension` (1x), `block` (1x), `section` (1x), `group` (1x), `header` (1x)
2. **Add query expansion for Shopify-specific terms**: Many queries use terminology (e.g., 'Dawn theme', 'Online Store 2.0', 'checkout extensibility') that may not match document text exactly. Expand the synonym dictionary.
3. **Consider chunk size optimization**: Some results return code-heavy chunks that lack surrounding explanation. Ensure parent context is available for code-only chunks.

## Full Results Table

| # | Query | Intent | Collections | Score | Rating |
|---|-------|--------|-------------|-------|--------|
| 1 | What properties does the product object have in Liquid? | reference | liquid_reference, api_reference | 0.760 | RELEVANT |
| 2 | How do I use the forloop object in Liquid? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 3 | What is the money_with_currency filter in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 4 | List all Liquid string filters | reference | liquid_reference, api_reference | 0.667 | RELEVANT |
| 5 | What does the split filter do in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 6 | How to use the where filter in Liquid? | how_to | theme_patterns, code_examples | 0.400 | PARTIAL |
| 7 | What is the collection object in Liquid? | reference | liquid_reference, api_reference | 0.940 | RELEVANT |
| 8 | How to access product.metafields in Liquid? | how_to | theme_patterns, code_examples | 0.400 | PARTIAL |
| 9 | What are Liquid control flow tags? | reference | liquid_reference, api_reference | 0.667 | RELEVANT |
| 10 | How does the paginate tag work in Liquid? | how_to | theme_patterns, code_examples | 0.400 | PARTIAL |
| 11 | What is the image_url filter? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 12 | Explain the date filter in Liquid | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 13 | What properties does the variant object have? | reference | liquid_reference, api_reference | 0.733 | RELEVANT |
| 14 | How to use the assign tag in Liquid? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 15 | What is the capture tag used for? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 16 | How to use the increment and decrement tags? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 17 | What is the tablerow tag in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 18 | How do Liquid comment tags work? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 19 | What is the raw tag in Liquid? | reference | liquid_reference, api_reference | 0.900 | RELEVANT |
| 20 | What does the default filter do? | reference | liquid_reference, api_reference | 0.800 | RELEVANT |
| 21 | How to use the url_encode filter? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 22 | What is the handle property in Shopify Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 23 | How to iterate over a collection's products in Liquid? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 24 | What is the all_products object? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 25 | How to use the map filter in Liquid? | how_to | theme_patterns, code_examples | 0.500 | PARTIAL |
| 26 | What is the linklists object? | reference | liquid_reference, api_reference | 0.940 | RELEVANT |
| 27 | How to access the current page info in Liquid? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 28 | What are the request object properties? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 29 | How does the content_for_header tag work? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 30 | What are Liquid math filters? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 31 | How to use the slice filter in Liquid? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 32 | What is the shop object in Liquid? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 33 | How to create a custom section in Shopify? | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 34 | What is the section schema in Shopify themes? | reference | liquid_reference, api_reference | 0.700 | RELEVANT |
| 35 | How do templates work in Shopify Online Store 2.0? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 36 | How to create a custom template in Shopify? | code_gen | code_examples, theme_patterns | 0.300 | IRRELEVANT |
| 37 | What is the difference between sections and snippets? | comparison | theme_patterns, best_practices | 0.740 | RELEVANT |
| 38 | How to use dynamic sources in section settings? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 39 | How does the render tag differ from include? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 40 | How to create section blocks in Shopify? | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 41 | What layout files are available in Shopify themes? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 42 | How to add custom settings to a theme? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 43 | How to create a predictive search in Shopify? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 44 | What are theme app extensions? | reference | api_reference, liquid_reference | 0.360 | IRRELEVANT |
| 45 | How to use app blocks in Shopify themes? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 46 | How to structure a Shopify theme directory? | architecture | best_practices, theme_patterns | 0.900 | RELEVANT |
| 47 | How do locales work in Shopify themes? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 48 | How to add translations to a Shopify theme? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 49 | What are section groups in Online Store 2.0? | reference | liquid_reference, api_reference | 0.360 | IRRELEVANT |
| 50 | How to use metafield definitions in themes? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 51 | How do I create a dropdown menu in Shopify? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 52 | How to add a custom font to a Shopify theme? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 53 | How to make a Shopify section with multiple block types? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 54 | How to add settings_schema.json settings? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 55 | How do theme presets work? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 56 | How to use the stylesheet tag in sections? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 57 | How to implement a product quick view? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 58 | What is Dawn theme and how is it structured? | reference | liquid_reference, api_reference | 0.440 | PARTIAL |
| 59 | How to create an announcement bar section? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 60 | How to implement a slideshow section? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 61 | How to use CSS variables in Shopify themes? | how_to | theme_patterns, code_examples | 0.680 | RELEVANT |
| 62 | What is the assets directory used for in Shopify? | reference | liquid_reference, api_reference | 0.460 | PARTIAL |
| 63 | How to add a newsletter signup form? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 64 | How to implement an AJAX cart in Shopify? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 65 | How to create a cart drawer in Shopify? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 66 | How to add line item properties to cart items? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 67 | How to use the cart/add.js endpoint? | how_to | code_examples, theme_patterns | 0.820 | RELEVANT |
| 68 | What is the cart object in Liquid? | reference | liquid_reference, api_reference | 0.680 | RELEVANT |
| 69 | How to implement quantity selectors for cart items? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 70 | How to add a gift message to cart? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 71 | How to use cart attributes in Shopify? | reference | liquid_reference, api_reference | 0.900 | RELEVANT |
| 72 | How to implement a free shipping progress bar? | how_to | theme_patterns, code_examples | 0.467 | PARTIAL |
| 73 | How do checkout extensions work in Shopify? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 74 | How to redirect to checkout after adding to cart? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 75 | What is the cart/change.js endpoint? | reference | api_reference, liquid_reference | 0.380 | IRRELEVANT |
| 76 | How to display cart totals dynamically? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 77 | How to implement upsells in the cart? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 78 | How to calculate shipping rates in the cart? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 79 | How to handle cart errors in Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 80 | How to add a discount code field to the cart? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 81 | How to implement a mini cart popup? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 82 | How to use the cart/update.js endpoint? | how_to | code_examples, theme_patterns | 0.820 | RELEVANT |
| 83 | How to create a cart page with editable quantities? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 84 | How does the cart template work in Online Store 2.0? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 85 | How to display product variants on the product page? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 86 | How to create a variant picker with swatches? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 87 | How to display product metafields on the product page? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 88 | How to add structured data / JSON-LD to product pages? | how_to | theme_patterns, code_examples | 0.867 | RELEVANT |
| 89 | How to implement a product image gallery? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 90 | How to show related products on the product page? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 91 | How to change the product image when a variant is selected? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 92 | How to display product reviews on the product page? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 93 | How to show product availability (in stock/out of stock)? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 94 | How to implement a product zoom feature? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 95 | How to display product tags in Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 96 | How to add a size chart to a product page? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 97 | How to show compare at prices? | comparison | best_practices, liquid_reference | 0.800 | RELEVANT |
| 98 | How to implement product tabs for description and details? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 99 | How to display product media (3D models, video)? | how_to | theme_patterns, code_examples | 0.933 | RELEVANT |
| 100 | How to handle products with many variants in Liquid? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 101 | How to create a product page with a sticky add to cart? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 102 | How to use product.selected_or_first_available_variant? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 103 | How to show product inventory quantity? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 104 | How to implement wishlist functionality? | how_to | code_examples, theme_patterns | 0.500 | PARTIAL |
| 105 | How to add custom product badges (sale, new, bestseller)? | how_to | theme_patterns, code_examples | 0.767 | RELEVANT |
| 106 | What is the Shopify Admin API? | reference | api_reference, liquid_reference | 0.680 | RELEVANT |
| 107 | How to use the Storefront API? | how_to | api_reference, theme_patterns | 0.840 | RELEVANT |
| 108 | How to fetch products with the Storefront API? | how_to | api_reference, theme_patterns | 0.900 | RELEVANT |
| 109 | How to use the Ajax API in Shopify? | how_to | code_examples, theme_patterns | 0.900 | RELEVANT |
| 110 | What webhooks are available in Shopify? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 111 | How to authenticate with the Shopify API? | how_to | theme_patterns, code_examples | 0.267 | IRRELEVANT |
| 112 | How to create a product using the Admin API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 113 | What is the Section Rendering API? | reference | api_reference, liquid_reference | 0.933 | RELEVANT |
| 114 | How to use the product recommendations endpoint? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 115 | How to use the Shopify GraphQL Admin API? | how_to | api_reference, theme_patterns | 0.820 | RELEVANT |
| 116 | How to get customer data from the Storefront API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 117 | How to handle pagination in the Admin API? | how_to | api_reference, theme_patterns | 0.767 | RELEVANT |
| 118 | What is the Shopify REST Admin API? | reference | api_reference, liquid_reference | 0.667 | RELEVANT |
| 119 | How to use metafield APIs? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 120 | How to listen for order webhooks? | how_to | theme_patterns, code_examples | 0.440 | PARTIAL |
| 121 | How to use the search.json endpoint? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 122 | How to use multipass for SSO? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 123 | How to fetch collections via Storefront API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 124 | How to use the Shopify Cart API? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 125 | How to fetch metaobjects via the API? | how_to | theme_patterns, api_reference | 0.760 | RELEVANT |
| 126 | How to create a draft order via Admin API? | how_to | api_reference, theme_patterns | 1.000 | RELEVANT |
| 127 | How to make a responsive product grid in Shopify? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 128 | How to use CSS Grid for a Shopify collection page? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 129 | How to add animations to a Shopify theme? | how_to | theme_patterns, code_examples | 0.580 | PARTIAL |
| 130 | How to implement dark mode in a Shopify theme? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 131 | How to customize the Dawn theme CSS? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 132 | How to use Tailwind CSS with Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 133 | How to make a sticky header in Shopify? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 134 | How to add a custom scrollbar style? | how_to | theme_patterns, code_examples | 0.480 | PARTIAL |
| 135 | How to implement a hamburger menu for mobile? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 136 | How to style the Shopify cart page? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 137 | How to create a responsive hero banner? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 138 | How to use flexbox for Shopify layouts? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 139 | How to add hover effects to product cards? | how_to | theme_patterns, code_examples | 0.767 | RELEVANT |
| 140 | How to customize form styles in Shopify? | how_to | theme_patterns, code_examples | 0.633 | PARTIAL |
| 141 | How to implement a masonry grid layout? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 142 | How to use media queries in Shopify themes? | how_to | theme_patterns, best_practices | 0.680 | RELEVANT |
| 143 | How to lazy load images in Shopify? | how_to | best_practices, code_examples | 1.000 | RELEVANT |
| 144 | How to preload critical resources in Shopify? | how_to | best_practices, code_examples | 0.540 | PARTIAL |
| 145 | How to improve Core Web Vitals for a Shopify store? | how_to | best_practices, theme_patterns | 0.943 | RELEVANT |
| 146 | How to use the Section Rendering API for performance? | how_to | theme_patterns, best_practices | 0.933 | RELEVANT |
| 147 | How to reduce JavaScript bundle size in Shopify? | how_to | best_practices, code_examples | 0.533 | PARTIAL |
| 148 | How to optimize images in Shopify themes? | how_to | theme_patterns, best_practices | 0.500 | PARTIAL |
| 149 | How to defer non-critical CSS in Shopify? | how_to | code_examples, theme_patterns | 0.520 | PARTIAL |
| 150 | What is the best way to load third-party scripts in Shopify? | comparison | best_practices, liquid_reference | 0.760 | RELEVANT |
| 151 | How to implement responsive images with srcset? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 152 | How to use native lazy loading in Shopify themes? | how_to | best_practices, code_examples | 0.680 | RELEVANT |
| 153 | How to reduce Liquid render time? | how_to | best_practices, theme_patterns | 0.600 | PARTIAL |
| 154 | How to cache Shopify API responses? | how_to | theme_patterns, code_examples | 0.520 | PARTIAL |
| 155 | How to use content_for_header efficiently? | how_to | theme_patterns, code_examples | 0.500 | PARTIAL |
| 156 | How to minimize layout shifts in Shopify? | how_to | best_practices, theme_patterns | 0.500 | PARTIAL |
| 157 | How to optimize collection page loading speed? | how_to | theme_patterns, best_practices | 0.620 | PARTIAL |
| 158 | How to use async/defer for JavaScript in Shopify? | how_to | best_practices, code_examples | 0.900 | RELEVANT |
| 159 | Why is my Liquid variable returning nil? | debug | troubleshooting, best_practices | 0.810 | RELEVANT |
| 160 | How to debug Liquid code in Shopify? | debug | troubleshooting, best_practices | 0.740 | RELEVANT |
| 161 | Why is my section not showing up in the theme editor? | debug | troubleshooting, best_practices | 1.000 | RELEVANT |
| 162 | Why is my product form not submitting? | debug | troubleshooting, best_practices | 0.970 | RELEVANT |
| 163 | How to fix 'Liquid error: Memory limits exceeded'? | debug | troubleshooting, best_practices | 0.440 | PARTIAL |
| 164 | Why are my theme changes not appearing? | debug | troubleshooting, best_practices | 0.580 | PARTIAL |
| 165 | How to fix 'Too many redirects' error in Shopify? | debug | troubleshooting, best_practices | 0.710 | RELEVANT |
| 166 | Why is my JavaScript not working in Shopify? | debug | troubleshooting, best_practices | 0.440 | PARTIAL |
| 167 | How to fix broken images in a Shopify theme? | debug | troubleshooting, best_practices | 0.760 | RELEVANT |
| 168 | Why is the add to cart button not working? | debug | troubleshooting, best_practices | 0.970 | RELEVANT |
| 169 | Why is my Shopify section schema invalid? | debug | troubleshooting, liquid_reference | 0.900 | RELEVANT |
| 170 | How to fix '404 Not Found' for theme assets? | debug | troubleshooting, best_practices | 0.630 | PARTIAL |
| 171 | Why does my Liquid for loop show nothing? | code_gen | code_examples, theme_patterns | 0.333 | IRRELEVANT |
| 172 | How to fix CORS errors with the Shopify API? | debug | troubleshooting, best_practices | 0.800 | RELEVANT |
| 173 | Why are my metafields not showing up? | debug | troubleshooting, best_practices | 0.680 | RELEVANT |
| 174 | How to troubleshoot slow Shopify theme performance? | debug | best_practices, troubleshooting | 0.560 | PARTIAL |
| 175 | Why is my variant picker not updating the price? | debug | troubleshooting, best_practices | 0.680 | RELEVANT |
| 176 | How to fix 'Argument error in tag for' in Liquid? | debug | troubleshooting, best_practices | 0.740 | RELEVANT |
| 177 | Why is my Shopify form showing validation errors? | debug | troubleshooting, best_practices | 0.790 | RELEVANT |
| 178 | How to debug the Shopify Ajax API responses? | debug | troubleshooting, api_reference | 0.640 | PARTIAL |
| 179 | Why is my collection filter not working? | debug | troubleshooting, best_practices | 1.000 | RELEVANT |
| 180 | How to fix undefined JavaScript errors in Shopify? | debug | troubleshooting, best_practices | 0.460 | PARTIAL |
| 181 | How to use metaobjects in Shopify? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 182 | How do Shopify Markets work? | how_to | best_practices, theme_patterns | 0.360 | IRRELEVANT |
| 183 | How to implement B2B features in Shopify? | how_to | best_practices, theme_patterns | 0.760 | RELEVANT |
| 184 | How to use Shopify Multipass for authentication? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 185 | How to create app blocks for Shopify themes? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 186 | How to build a theme app extension? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 187 | How to use Shopify Functions for discounts? | how_to | code_examples, theme_patterns | 0.820 | RELEVANT |
| 188 | How to implement custom storefronts with Hydrogen? | how_to | code_examples, theme_patterns | 0.740 | RELEVANT |
| 189 | How to use the Customer Account API? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 190 | How to implement multi-currency in Shopify? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 191 | How to use Shopify Flow for automation? | how_to | theme_patterns, code_examples | 0.280 | IRRELEVANT |
| 192 | How to implement product bundles in Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 193 | How to use the Shopify CLI for theme development? | how_to | theme_patterns, code_examples | 0.567 | PARTIAL |
| 194 | How to create a custom storefront with the Storefront API? | how_to | api_reference, theme_patterns | 1.000 | RELEVANT |
| 195 | How to implement subscription products in Shopify? | how_to | theme_patterns, code_examples | 0.280 | IRRELEVANT |
| 196 | How to use Shopify Pixels for analytics? | how_to | theme_patterns, code_examples | 0.360 | IRRELEVANT |
| 197 | How to implement customer-specific pricing? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 198 | How to use the Shopify Checkout Extensibility? | how_to | theme_patterns, code_examples | 0.520 | PARTIAL |
| 199 | How to implement store locator functionality? | how_to | code_examples, theme_patterns | 0.480 | PARTIAL |
| 200 | How to use online store editor customization API? | how_to | theme_patterns, code_examples | 0.360 | IRRELEVANT |
| 201 | How to create a headless Shopify storefront? | how_to | theme_patterns, code_examples | 0.467 | PARTIAL |
| 202 | Build me a product card section with image, title, and price | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 203 | Generate a Liquid snippet for a star rating display | code_gen | code_examples, theme_patterns | 0.800 | RELEVANT |
| 204 | Create a section for a hero banner with text overlay | code_gen | code_examples, theme_patterns | 0.817 | RELEVANT |
| 205 | Build me a color swatch variant picker in Liquid | code_gen | code_examples, theme_patterns | 0.983 | RELEVANT |
| 206 | Generate a Liquid template for a FAQ page | code_gen | code_examples, theme_patterns | 0.630 | PARTIAL |
| 207 | Create a section for featured collections grid | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 208 | Build me an AJAX add to cart form | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 209 | Generate a responsive image gallery with thumbnails | code_gen | code_examples, theme_patterns | 0.510 | PARTIAL |
| 210 | Create a section for customer testimonials | code_gen | code_examples, theme_patterns | 0.790 | RELEVANT |
| 211 | Build me a mega menu navigation | code_gen | code_examples, theme_patterns | 0.810 | RELEVANT |
| 212 | Generate a product comparison table in Liquid | code_gen | code_examples, theme_patterns | 0.670 | RELEVANT |
| 213 | Create a section for an image with text layout | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 214 | Build me a collection filter sidebar | code_gen | code_examples, theme_patterns | 0.920 | RELEVANT |
| 215 | Generate a Liquid snippet for breadcrumb navigation | code_gen | code_examples, theme_patterns | 0.890 | RELEVANT |
| 216 | Create a custom product page template with tabs | how_to | theme_patterns, code_examples | 0.890 | RELEVANT |
| 217 | Build me a newsletter popup modal | code_gen | code_examples, theme_patterns | 0.590 | PARTIAL |
| 218 | Generate a multi-column section with icons | code_gen | code_examples, theme_patterns | 0.810 | RELEVANT |

---
*Report generated by test_rag_comprehensive.py on 2026-02-09 12:57:46*