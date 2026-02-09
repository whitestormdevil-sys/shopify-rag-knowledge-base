# RAG v3 Test Report — Re-indexed with New Data

**Generated:** 2026-02-09 13:46:26
**Total Queries:** 218
**Total Chunks:** 47843 (up from 42,744 in v1/v2)
**Execution Time:** 218.3s (1.00s/query)
**Settings:** `use_reranker=False, expand_parents=False, top_k=5`

## Executive Summary

| Metric | Value |
|--------|-------|
| **Overall Pass Rate** (RELEVANT + PARTIAL) | **93.6%** (204/218) |
| RELEVANT | 156 (71.6%) |
| PARTIAL | 48 (22.0%) |
| IRRELEVANT | 14 (6.4%) |
| NO_RESULTS | 0 (0.0%) |
| ERRORS | 0 |
| **Avg Relevance Score** | **0.750** (0-1 scale) |
| **Avg Top-1 Search Score** | **0.0716** |
| Queries/Second | 1.0 |

### Rating Distribution
```
🟢 RELEVANT     ███████████████████████████████████░░░░░░░░░░░░░░░ 156 (71.6%)
🟡 PARTIAL      ███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  48 (22.0%)
🔴 IRRELEVANT   ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  14 (6.4%)
⚫ NO_RESULTS   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0 (0.0%)
```

## Version Comparison: v1 → v2 → v3

| Metric | v1 | v2 | v3 | v2→v3 Δ |
|--------|----|----|----|---------:|
| **Chunks Indexed** | 42,744 | 42,744 | 47,843 | +5,099 |
| **Pass Rate** | 95.0% | 95.0% | 93.6% | -1.4% |
| RELEVANT | 165 | 165 | 156 | -9 |
| PARTIAL | 42 | 42 | 48 | +6 |
| IRRELEVANT | 11 | 11 | 14 | +3 |
| NO_RESULTS | 0 | 0 | 0 | +0 |
| **Avg Score** | 0.758 | 0.758 | 0.750 | -0.008 |

## Per-Category Breakdown

| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |
|----------|-------|----------|---------|------------|------------|-----------|-----------|
| Theme Development | 31 | 28 (90%) | 3 (10%) | 0 (0%) | 0 | **100%** | 0.795 |
| Cart/Checkout | 21 | 14 (67%) | 7 (33%) | 0 (0%) | 0 | **100%** | 0.719 |
| Product Pages | 21 | 16 (76%) | 5 (24%) | 0 (0%) | 0 | **100%** | 0.806 |
| Styling/CSS | 16 | 15 (94%) | 1 (6%) | 0 (0%) | 0 | **100%** | 0.842 |
| Liquid Reference | 32 | 21 (66%) | 10 (31%) | 1 (3%) | 0 | **97%** | 0.765 |
| Code Generation | 17 | 13 (76%) | 3 (18%) | 1 (6%) | 0 | **94%** | 0.787 |
| Performance | 16 | 10 (62%) | 5 (31%) | 1 (6%) | 0 | **94%** | 0.764 |
| APIs | 21 | 18 (86%) | 1 (5%) | 2 (10%) | 0 | **90%** | 0.800 |
| Advanced | 21 | 10 (48%) | 7 (33%) | 4 (19%) | 0 | **81%** | 0.614 |
| Troubleshooting | 22 | 11 (50%) | 6 (27%) | 5 (23%) | 0 | **77%** | 0.619 |

### Theme Development
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.795
- **Avg Search Score:** 0.0615

### Cart/Checkout
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.719
- **Avg Search Score:** 0.0542

### Product Pages
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.806
- **Avg Search Score:** 0.0821

### Styling/CSS
- **Pass Rate:** 100%
- **Avg Relevance Score:** 0.842
- **Avg Search Score:** 0.0680

### Liquid Reference
- **Pass Rate:** 97%
- **Avg Relevance Score:** 0.765
- **Avg Search Score:** 0.0904
- **Issues (1):**
  - ❌ `How to access the current page info in Liquid?` → IRRELEVANT (Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_patterns', 'theme_patterns', 'code_examples']; Top score: 0.0411)

### Code Generation
- **Pass Rate:** 94%
- **Avg Relevance Score:** 0.787
- **Avg Search Score:** 0.0865
- **Issues (1):**
  - ❌ `Generate a Liquid snippet for a star rating display` → IRRELEVANT (3/5 keywords matched; Expected ['code_examples'], got ['theme_patterns', 'theme_patterns', 'best_practices']; Top score: 0.0289; Code content found)

### Performance
- **Pass Rate:** 94%
- **Avg Relevance Score:** 0.764
- **Avg Search Score:** 0.0924
- **Issues (1):**
  - ❌ `How to cache Shopify API responses?` → IRRELEVANT (2/5 keywords matched; Expected ['best_practices'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0495)

### APIs
- **Pass Rate:** 90%
- **Avg Relevance Score:** 0.800
- **Avg Search Score:** 0.0715
- **Issues (2):**
  - ❌ `How to authenticate with the Shopify API?` → IRRELEVANT (Only 1/6 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0516)
  - ❌ `How to listen for order webhooks?` → IRRELEVANT (2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'code_examples']; Top score: 0.0415)

### Advanced
- **Pass Rate:** 81%
- **Avg Relevance Score:** 0.614
- **Avg Search Score:** 0.0537
- **Issues (4):**
  - ❌ `How to use Shopify Multipass for authentication?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0441)
  - ❌ `How to use Shopify Functions for discounts?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0413)
  - ❌ `How to implement custom storefronts with Hydrogen?` → IRRELEVANT (2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0293)
  - ❌ `How to implement subscription products in Shopify?` → IRRELEVANT (Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patterns', 'theme_patterns', 'theme_patterns']; Top score: 0.0460)

### Troubleshooting
- **Pass Rate:** 77%
- **Avg Relevance Score:** 0.619
- **Avg Search Score:** 0.0581
- **Issues (5):**
  - ❌ `How to fix 'Liquid error: Memory limits exceeded'?` → IRRELEVANT (3/5 keywords matched; Expected ['troubleshooting'], got ['best_practices', 'best_practices', 'best_practices']; Top score: 0.0295)
  - ❌ `Why is my JavaScript not working in Shopify?` → IRRELEVANT (No expected keywords found in results; Expected ['troubleshooting'], got ['best_practices', 'best_practices', 'best_practices']; Top score: 0.0390)
  - ❌ `Why is my Shopify section schema invalid?` → IRRELEVANT (2/5 keywords matched; Expected ['troubleshooting'], got ['best_practices', 'theme_patterns', 'theme_patterns']; Top score: 0.0361)
  - ❌ `Why does my Liquid for loop show nothing?` → IRRELEVANT (2/6 keywords matched; Expected ['troubleshooting'], got ['best_practices', 'best_practices', 'liquid_reference']; Top score: 0.0458)
  - ❌ `How to fix CORS errors with the Shopify API?` → IRRELEVANT (Only 1/5 keywords found; Expected ['troubleshooting'], got ['best_practices', 'best_practices', 'best_practices']; Top score: 0.0406)

## Intent Detection Analysis

| Detected Intent | Count | Avg Relevance Score |
|-----------------|-------|---------------------|
| how_to | 143 | 0.752 |
| reference | 30 | 0.811 |
| debug | 22 | 0.619 |
| code_gen | 19 | 0.795 |
| comparison | 3 | 0.687 |
| architecture | 1 | 0.829 |

✅ **All 6 intents detected:** architecture, code_gen, comparison, debug, how_to, reference

## Collection Distribution in Results

| Collection | Times Targeted | Times in Results | Hit Rate | Avg Score |
|------------|---------------|-----------------|----------|-----------|
| theme_patterns | 173 | 326 | 188% | 0.0596 |
| best_practices | 188 | 118 | 63% | 0.0543 |
| liquid_reference | 174 | 88 | 51% | 0.0631 |
| api_reference | 74 | 62 | 84% | 0.0569 |
| code_examples | 214 | 46 | 21% | 0.0496 |
| troubleshooting | 24 | 14 | 58% | 0.0567 |

### Collection Sizes (v3 Index)

| Collection | Total Chunks | Parents | Children |
|------------|-------------|---------|----------|
| api_reference | 19,279 | 1085 | 18,194 |
| code_examples | 15,049 | 697 | 14,352 |
| best_practices | 6,971 | 602 | 6,369 |
| liquid_reference | 3,622 | 535 | 3,087 |
| theme_patterns | 1,629 | 192 | 1,437 |
| troubleshooting | 1,293 | 214 | 1,079 |

## Remaining IRRELEVANT Queries (14)

| # | Query | Category | Expected Collections | Got Collections | Score | Reason |
|---|-------|----------|---------------------|----------------|-------|--------|
| 1 | How to access the current page info in Liquid? | Liquid Reference | ['liquid_reference'] | ['theme_patterns', 'theme_patterns', 'code_examples'] | 0.300 | Only 1/4 keywords found; Expected ['liquid_reference'], got  |
| 2 | How to authenticate with the Shopify API? | APIs | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.367 | Only 1/6 keywords found; Expected ['api_reference'], got ['t |
| 3 | How to listen for order webhooks? | APIs | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'code_examples'] | 0.360 | 2/5 keywords matched; Expected ['api_reference'], got ['them |
| 4 | How to cache Shopify API responses? | Performance | ['best_practices'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.360 | 2/5 keywords matched; Expected ['best_practices'], got ['the |
| 5 | How to fix 'Liquid error: Memory limits exceeded'? | Troubleshooting | ['troubleshooting'] | ['best_practices', 'best_practices', 'best_practices'] | 0.340 | 3/5 keywords matched; Expected ['troubleshooting'], got ['be |
| 6 | Why is my JavaScript not working in Shopify? | Troubleshooting | ['troubleshooting'] | ['best_practices', 'best_practices', 'best_practices'] | 0.200 | No expected keywords found in results; Expected ['troublesho |
| 7 | Why is my Shopify section schema invalid? | Troubleshooting | ['troubleshooting'] | ['best_practices', 'theme_patterns', 'theme_patterns'] | 0.360 | 2/5 keywords matched; Expected ['troubleshooting'], got ['be |
| 8 | Why does my Liquid for loop show nothing? | Troubleshooting | ['troubleshooting'] | ['best_practices', 'best_practices', 'liquid_reference'] | 0.333 | 2/6 keywords matched; Expected ['troubleshooting'], got ['be |
| 9 | How to fix CORS errors with the Shopify API? | Troubleshooting | ['troubleshooting'] | ['best_practices', 'best_practices', 'best_practices'] | 0.280 | Only 1/5 keywords found; Expected ['troubleshooting'], got [ |
| 10 | How to use Shopify Multipass for authentication? | Advanced | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.280 | Only 1/5 keywords found; Expected ['api_reference'], got ['t |
| 11 | How to use Shopify Functions for discounts? | Advanced | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.280 | Only 1/5 keywords found; Expected ['api_reference'], got ['t |
| 12 | How to implement custom storefronts with Hydrogen? | Advanced | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.260 | 2/5 keywords matched; Expected ['api_reference'], got ['them |
| 13 | How to implement subscription products in Shopify? | Advanced | ['api_reference'] | ['theme_patterns', 'theme_patterns', 'theme_patterns'] | 0.280 | Only 1/5 keywords found; Expected ['api_reference'], got ['t |
| 14 | Generate a Liquid snippet for a star rating display | Code Generation | ['code_examples'] | ['theme_patterns', 'theme_patterns', 'best_practices'] | 0.390 | 3/5 keywords matched; Expected ['code_examples'], got ['them |

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
| 9 | 1.000 | RELEVANT | Liquid Reference | How to use the url_encode filter? |
| 10 | 1.000 | RELEVANT | Liquid Reference | What is the handle property in Shopify Liquid? |
| 11 | 1.000 | RELEVANT | Liquid Reference | What is the all_products object? |
| 12 | 1.000 | RELEVANT | Liquid Reference | What are Liquid math filters? |
| 13 | 1.000 | RELEVANT | Theme Development | How do locales work in Shopify themes? |
| 14 | 1.000 | RELEVANT | Theme Development | How to make a Shopify section with multiple block types? |
| 15 | 1.000 | RELEVANT | Theme Development | How to add settings_schema.json settings? |
| 16 | 1.000 | RELEVANT | Cart/Checkout | How do checkout extensions work in Shopify? |
| 17 | 1.000 | RELEVANT | Product Pages | How to create a variant picker with swatches? |
| 18 | 1.000 | RELEVANT | Product Pages | How to show product availability (in stock/out of stock)? |
| 19 | 1.000 | RELEVANT | Product Pages | How to create a product page with a sticky add to cart? |
| 20 | 1.000 | RELEVANT | APIs | How to use the Ajax API in Shopify? |

## Top 20 Worst-Performing Queries

| # | Score | Rating | Category | Query | Reason |
|---|-------|--------|----------|-------|--------|
| 1 | 0.200 | IRRELEVANT | Troubleshooting | Why is my JavaScript not working in Shopify? | No expected keywords found in results; Expected ['troubleshooting'], g |
| 2 | 0.260 | IRRELEVANT | Advanced | How to implement custom storefronts with Hydrogen? | 2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns |
| 3 | 0.280 | IRRELEVANT | Troubleshooting | How to fix CORS errors with the Shopify API? | Only 1/5 keywords found; Expected ['troubleshooting'], got ['best_prac |
| 4 | 0.280 | IRRELEVANT | Advanced | How to use Shopify Multipass for authentication? | Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patte |
| 5 | 0.280 | IRRELEVANT | Advanced | How to use Shopify Functions for discounts? | Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patte |
| 6 | 0.280 | IRRELEVANT | Advanced | How to implement subscription products in Shopify? | Only 1/5 keywords found; Expected ['api_reference'], got ['theme_patte |
| 7 | 0.300 | IRRELEVANT | Liquid Reference | How to access the current page info in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_pa |
| 8 | 0.333 | IRRELEVANT | Troubleshooting | Why does my Liquid for loop show nothing? | 2/6 keywords matched; Expected ['troubleshooting'], got ['best_practic |
| 9 | 0.340 | IRRELEVANT | Troubleshooting | How to fix 'Liquid error: Memory limits exceeded'? | 3/5 keywords matched; Expected ['troubleshooting'], got ['best_practic |
| 10 | 0.360 | IRRELEVANT | APIs | How to listen for order webhooks? | 2/5 keywords matched; Expected ['api_reference'], got ['theme_patterns |
| 11 | 0.360 | IRRELEVANT | Performance | How to cache Shopify API responses? | 2/5 keywords matched; Expected ['best_practices'], got ['theme_pattern |
| 12 | 0.360 | IRRELEVANT | Troubleshooting | Why is my Shopify section schema invalid? | 2/5 keywords matched; Expected ['troubleshooting'], got ['best_practic |
| 13 | 0.367 | IRRELEVANT | APIs | How to authenticate with the Shopify API? | Only 1/6 keywords found; Expected ['api_reference'], got ['theme_patte |
| 14 | 0.390 | IRRELEVANT | Code Generation | Generate a Liquid snippet for a star rating display | 3/5 keywords matched; Expected ['code_examples'], got ['theme_patterns |
| 15 | 0.400 | PARTIAL | Liquid Reference | How to use the where filter in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_pa |
| 16 | 0.400 | PARTIAL | Liquid Reference | How to access product.metafields in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_pa |
| 17 | 0.400 | PARTIAL | Liquid Reference | How does the paginate tag work in Liquid? | Only 1/4 keywords found; Expected ['liquid_reference'], got ['theme_pa |
| 18 | 0.400 | PARTIAL | Product Pages | How to show compare at prices? | Only 1/4 keywords found; Expected ['liquid_reference', 'theme_patterns |
| 19 | 0.400 | PARTIAL | Product Pages | How to implement wishlist functionality? | No expected keywords found in results; Collection match ✓; Top score:  |
| 20 | 0.400 | PARTIAL | Advanced | How to create a headless Shopify storefront? | 3/6 keywords matched; Expected ['api_reference'], got ['theme_patterns |

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
| 13 | What properties does the variant object have? | reference | liquid_reference, api_reference | 0.800 | RELEVANT |
| 14 | How to use the assign tag in Liquid? | how_to | theme_patterns, code_examples | 0.467 | PARTIAL |
| 15 | What is the capture tag used for? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 16 | How to use the increment and decrement tags? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 17 | What is the tablerow tag in Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 18 | How do Liquid comment tags work? | how_to | theme_patterns, code_examples | 0.533 | PARTIAL |
| 19 | What is the raw tag in Liquid? | reference | liquid_reference, api_reference | 0.900 | RELEVANT |
| 20 | What does the default filter do? | reference | liquid_reference, api_reference | 0.800 | RELEVANT |
| 21 | How to use the url_encode filter? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 22 | What is the handle property in Shopify Liquid? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 23 | How to iterate over a collection's products in Liquid? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 24 | What is the all_products object? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 25 | How to use the map filter in Liquid? | how_to | theme_patterns, code_examples | 0.500 | PARTIAL |
| 26 | What is the linklists object? | reference | liquid_reference, api_reference | 0.940 | RELEVANT |
| 27 | How to access the current page info in Liquid? | how_to | theme_patterns, code_examples | 0.300 | IRRELEVANT |
| 28 | What are the request object properties? | reference | liquid_reference, api_reference | 0.580 | PARTIAL |
| 29 | How does the content_for_header tag work? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 30 | What are Liquid math filters? | reference | liquid_reference, api_reference | 1.000 | RELEVANT |
| 31 | How to use the slice filter in Liquid? | how_to | theme_patterns, code_examples | 0.540 | PARTIAL |
| 32 | What is the shop object in Liquid? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 33 | How to create a custom section in Shopify? | code_gen | code_examples, theme_patterns | 0.900 | RELEVANT |
| 34 | What is the section schema in Shopify themes? | reference | liquid_reference, api_reference | 0.700 | RELEVANT |
| 35 | How do templates work in Shopify Online Store 2.0? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 36 | How to create a custom template in Shopify? | code_gen | code_examples, theme_patterns | 0.800 | RELEVANT |
| 37 | What is the difference between sections and snippets? | comparison | theme_patterns, best_practices | 0.740 | RELEVANT |
| 38 | How to use dynamic sources in section settings? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 39 | How does the render tag differ from include? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 40 | How to create section blocks in Shopify? | code_gen | code_examples, theme_patterns | 0.920 | RELEVANT |
| 41 | What layout files are available in Shopify themes? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 42 | How to add custom settings to a theme? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 43 | How to create a predictive search in Shopify? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 44 | What are theme app extensions? | reference | api_reference, liquid_reference | 0.740 | RELEVANT |
| 45 | How to use app blocks in Shopify themes? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 46 | How to structure a Shopify theme directory? | architecture | best_practices, theme_patterns | 0.829 | RELEVANT |
| 47 | How do locales work in Shopify themes? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 48 | How to add translations to a Shopify theme? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 49 | What are section groups in Online Store 2.0? | reference | liquid_reference, api_reference | 0.600 | PARTIAL |
| 50 | How to use metafield definitions in themes? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 51 | How do I create a dropdown menu in Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 52 | How to add a custom font to a Shopify theme? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 53 | How to make a Shopify section with multiple block types? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 54 | How to add settings_schema.json settings? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 55 | How do theme presets work? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 56 | How to use the stylesheet tag in sections? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 57 | How to implement a product quick view? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 58 | What is Dawn theme and how is it structured? | reference | liquid_reference, api_reference | 0.440 | PARTIAL |
| 59 | How to create an announcement bar section? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 60 | How to implement a slideshow section? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 61 | How to use CSS variables in Shopify themes? | how_to | theme_patterns, code_examples | 0.680 | RELEVANT |
| 62 | What is the assets directory used for in Shopify? | reference | liquid_reference, api_reference | 0.460 | PARTIAL |
| 63 | How to add a newsletter signup form? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 64 | How to implement an AJAX cart in Shopify? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 65 | How to create a cart drawer in Shopify? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 66 | How to add line item properties to cart items? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 67 | How to use the cart/add.js endpoint? | how_to | code_examples, theme_patterns | 0.440 | PARTIAL |
| 68 | What is the cart object in Liquid? | reference | liquid_reference, api_reference | 0.680 | RELEVANT |
| 69 | How to implement quantity selectors for cart items? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 70 | How to add a gift message to cart? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 71 | How to use cart attributes in Shopify? | reference | liquid_reference, api_reference | 0.900 | RELEVANT |
| 72 | How to implement a free shipping progress bar? | how_to | theme_patterns, code_examples | 0.633 | PARTIAL |
| 73 | How do checkout extensions work in Shopify? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 74 | How to redirect to checkout after adding to cart? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 75 | What is the cart/change.js endpoint? | reference | api_reference, liquid_reference | 0.620 | PARTIAL |
| 76 | How to display cart totals dynamically? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 77 | How to implement upsells in the cart? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 78 | How to calculate shipping rates in the cart? | how_to | theme_patterns, code_examples | 0.440 | PARTIAL |
| 79 | How to handle cart errors in Shopify? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 80 | How to add a discount code field to the cart? | how_to | theme_patterns, code_examples | 0.580 | PARTIAL |
| 81 | How to implement a mini cart popup? | how_to | theme_patterns, code_examples | 0.580 | PARTIAL |
| 82 | How to use the cart/update.js endpoint? | how_to | code_examples, theme_patterns | 0.700 | RELEVANT |
| 83 | How to create a cart page with editable quantities? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 84 | How does the cart template work in Online Store 2.0? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 85 | How to display product variants on the product page? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 86 | How to create a variant picker with swatches? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 87 | How to display product metafields on the product page? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 88 | How to add structured data / JSON-LD to product pages? | how_to | theme_patterns, code_examples | 0.867 | RELEVANT |
| 89 | How to implement a product image gallery? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 90 | How to show related products on the product page? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 91 | How to change the product image when a variant is selected? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 92 | How to display product reviews on the product page? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 93 | How to show product availability (in stock/out of stock)? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 94 | How to implement a product zoom feature? | how_to | theme_patterns, code_examples | 0.580 | PARTIAL |
| 95 | How to display product tags in Shopify? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 96 | How to add a size chart to a product page? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 97 | How to show compare at prices? | comparison | best_practices, liquid_reference | 0.400 | PARTIAL |
| 98 | How to implement product tabs for description and details? | how_to | theme_patterns, code_examples | 0.580 | PARTIAL |
| 99 | How to display product media (3D models, video)? | how_to | theme_patterns, code_examples | 0.933 | RELEVANT |
| 100 | How to handle products with many variants in Liquid? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 101 | How to create a product page with a sticky add to cart? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 102 | How to use product.selected_or_first_available_variant? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 103 | How to show product inventory quantity? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 104 | How to implement wishlist functionality? | how_to | code_examples, theme_patterns | 0.400 | PARTIAL |
| 105 | How to add custom product badges (sale, new, bestseller)? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 106 | What is the Shopify Admin API? | reference | api_reference, liquid_reference | 0.680 | RELEVANT |
| 107 | How to use the Storefront API? | how_to | api_reference, theme_patterns | 0.440 | PARTIAL |
| 108 | How to fetch products with the Storefront API? | how_to | api_reference, theme_patterns | 0.900 | RELEVANT |
| 109 | How to use the Ajax API in Shopify? | how_to | code_examples, theme_patterns | 1.000 | RELEVANT |
| 110 | What webhooks are available in Shopify? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 111 | How to authenticate with the Shopify API? | how_to | theme_patterns, code_examples | 0.367 | IRRELEVANT |
| 112 | How to create a product using the Admin API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 113 | What is the Section Rendering API? | reference | api_reference, liquid_reference | 0.933 | RELEVANT |
| 114 | How to use the product recommendations endpoint? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 115 | How to use the Shopify GraphQL Admin API? | how_to | api_reference, theme_patterns | 0.820 | RELEVANT |
| 116 | How to get customer data from the Storefront API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 117 | How to handle pagination in the Admin API? | how_to | api_reference, theme_patterns | 0.767 | RELEVANT |
| 118 | What is the Shopify REST Admin API? | reference | api_reference, liquid_reference | 0.933 | RELEVANT |
| 119 | How to use metafield APIs? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 120 | How to listen for order webhooks? | how_to | theme_patterns, code_examples | 0.360 | IRRELEVANT |
| 121 | How to use the search.json endpoint? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 122 | How to use multipass for SSO? | how_to | theme_patterns, code_examples | 0.820 | RELEVANT |
| 123 | How to fetch collections via Storefront API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 124 | How to use the Shopify Cart API? | how_to | theme_patterns, code_examples | 0.733 | RELEVANT |
| 125 | How to fetch metaobjects via the API? | how_to | theme_patterns, api_reference | 0.760 | RELEVANT |
| 126 | How to create a draft order via Admin API? | how_to | api_reference, theme_patterns | 1.000 | RELEVANT |
| 127 | How to make a responsive product grid in Shopify? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 128 | How to use CSS Grid for a Shopify collection page? | how_to | theme_patterns, code_examples | 0.900 | RELEVANT |
| 129 | How to add animations to a Shopify theme? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 130 | How to implement dark mode in a Shopify theme? | how_to | theme_patterns, code_examples | 0.800 | RELEVANT |
| 131 | How to customize the Dawn theme CSS? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 132 | How to use Tailwind CSS with Shopify? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 133 | How to make a sticky header in Shopify? | how_to | theme_patterns, code_examples | 0.500 | PARTIAL |
| 134 | How to add a custom scrollbar style? | how_to | theme_patterns, code_examples | 0.740 | RELEVANT |
| 135 | How to implement a hamburger menu for mobile? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 136 | How to style the Shopify cart page? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 137 | How to create a responsive hero banner? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 138 | How to use flexbox for Shopify layouts? | how_to | theme_patterns, code_examples | 0.760 | RELEVANT |
| 139 | How to add hover effects to product cards? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 140 | How to customize form styles in Shopify? | how_to | theme_patterns, code_examples | 0.833 | RELEVANT |
| 141 | How to implement a masonry grid layout? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 142 | How to use media queries in Shopify themes? | how_to | theme_patterns, best_practices | 0.920 | RELEVANT |
| 143 | How to lazy load images in Shopify? | how_to | best_practices, code_examples | 0.920 | RELEVANT |
| 144 | How to preload critical resources in Shopify? | how_to | best_practices, code_examples | 0.840 | RELEVANT |
| 145 | How to improve Core Web Vitals for a Shopify store? | how_to | best_practices, theme_patterns | 0.943 | RELEVANT |
| 146 | How to use the Section Rendering API for performance? | how_to | theme_patterns, best_practices | 0.933 | RELEVANT |
| 147 | How to reduce JavaScript bundle size in Shopify? | how_to | best_practices, code_examples | 0.933 | RELEVANT |
| 148 | How to optimize images in Shopify themes? | how_to | theme_patterns, best_practices | 0.433 | PARTIAL |
| 149 | How to defer non-critical CSS in Shopify? | how_to | code_examples, theme_patterns | 0.620 | PARTIAL |
| 150 | What is the best way to load third-party scripts in Shopify? | comparison | best_practices, liquid_reference | 0.920 | RELEVANT |
| 151 | How to implement responsive images with srcset? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 152 | How to use native lazy loading in Shopify themes? | how_to | best_practices, code_examples | 0.680 | RELEVANT |
| 153 | How to reduce Liquid render time? | how_to | best_practices, theme_patterns | 0.900 | RELEVANT |
| 154 | How to cache Shopify API responses? | how_to | theme_patterns, code_examples | 0.360 | IRRELEVANT |
| 155 | How to use content_for_header efficiently? | how_to | theme_patterns, code_examples | 0.600 | PARTIAL |
| 156 | How to minimize layout shifts in Shopify? | how_to | best_practices, theme_patterns | 0.600 | PARTIAL |
| 157 | How to optimize collection page loading speed? | how_to | theme_patterns, best_practices | 0.620 | PARTIAL |
| 158 | How to use async/defer for JavaScript in Shopify? | how_to | best_practices, code_examples | 0.920 | RELEVANT |
| 159 | Why is my Liquid variable returning nil? | debug | troubleshooting, best_practices | 0.760 | RELEVANT |
| 160 | How to debug Liquid code in Shopify? | debug | troubleshooting, best_practices | 0.520 | PARTIAL |
| 161 | Why is my section not showing up in the theme editor? | debug | troubleshooting, best_practices | 0.900 | RELEVANT |
| 162 | Why is my product form not submitting? | debug | troubleshooting, best_practices | 0.840 | RELEVANT |
| 163 | How to fix 'Liquid error: Memory limits exceeded'? | debug | troubleshooting, best_practices | 0.340 | IRRELEVANT |
| 164 | Why are my theme changes not appearing? | debug | troubleshooting, best_practices | 0.580 | PARTIAL |
| 165 | How to fix 'Too many redirects' error in Shopify? | debug | troubleshooting, best_practices | 0.710 | RELEVANT |
| 166 | Why is my JavaScript not working in Shopify? | debug | troubleshooting, best_practices | 0.200 | IRRELEVANT |
| 167 | How to fix broken images in a Shopify theme? | debug | troubleshooting, best_practices | 0.590 | PARTIAL |
| 168 | Why is the add to cart button not working? | debug | troubleshooting, best_practices | 0.970 | RELEVANT |
| 169 | Why is my Shopify section schema invalid? | debug | troubleshooting, liquid_reference | 0.360 | IRRELEVANT |
| 170 | How to fix '404 Not Found' for theme assets? | debug | troubleshooting, best_practices | 0.630 | PARTIAL |
| 171 | Why does my Liquid for loop show nothing? | debug | troubleshooting, best_practices | 0.333 | IRRELEVANT |
| 172 | How to fix CORS errors with the Shopify API? | debug | troubleshooting, best_practices | 0.280 | IRRELEVANT |
| 173 | Why are my metafields not showing up? | debug | troubleshooting, best_practices | 0.680 | RELEVANT |
| 174 | How to troubleshoot slow Shopify theme performance? | debug | best_practices, troubleshooting | 0.740 | RELEVANT |
| 175 | Why is my variant picker not updating the price? | debug | troubleshooting, best_practices | 0.680 | RELEVANT |
| 176 | How to fix 'Argument error in tag for' in Liquid? | debug | troubleshooting, best_practices | 0.820 | RELEVANT |
| 177 | Why is my Shopify form showing validation errors? | debug | troubleshooting, best_practices | 0.790 | RELEVANT |
| 178 | How to debug the Shopify Ajax API responses? | debug | troubleshooting, api_reference | 0.440 | PARTIAL |
| 179 | Why is my collection filter not working? | debug | troubleshooting, best_practices | 1.000 | RELEVANT |
| 180 | How to fix undefined JavaScript errors in Shopify? | debug | troubleshooting, best_practices | 0.460 | PARTIAL |
| 181 | How to use metaobjects in Shopify? | how_to | theme_patterns, code_examples | 0.840 | RELEVANT |
| 182 | How do Shopify Markets work? | how_to | best_practices, theme_patterns | 0.760 | RELEVANT |
| 183 | How to implement B2B features in Shopify? | how_to | best_practices, theme_patterns | 0.460 | PARTIAL |
| 184 | How to use Shopify Multipass for authentication? | how_to | theme_patterns, code_examples | 0.280 | IRRELEVANT |
| 185 | How to create app blocks for Shopify themes? | how_to | theme_patterns, code_examples | 1.000 | RELEVANT |
| 186 | How to build a theme app extension? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 187 | How to use Shopify Functions for discounts? | how_to | code_examples, theme_patterns | 0.280 | IRRELEVANT |
| 188 | How to implement custom storefronts with Hydrogen? | how_to | code_examples, theme_patterns | 0.260 | IRRELEVANT |
| 189 | How to use the Customer Account API? | how_to | theme_patterns, code_examples | 0.520 | PARTIAL |
| 190 | How to implement multi-currency in Shopify? | how_to | theme_patterns, code_examples | 0.920 | RELEVANT |
| 191 | How to use Shopify Flow for automation? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 192 | How to implement product bundles in Shopify? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 193 | How to use the Shopify CLI for theme development? | how_to | theme_patterns, code_examples | 0.700 | RELEVANT |
| 194 | How to create a custom storefront with the Storefront API? | how_to | api_reference, theme_patterns | 0.920 | RELEVANT |
| 195 | How to implement subscription products in Shopify? | how_to | theme_patterns, code_examples | 0.280 | IRRELEVANT |
| 196 | How to use Shopify Pixels for analytics? | how_to | theme_patterns, code_examples | 0.540 | PARTIAL |
| 197 | How to implement customer-specific pricing? | how_to | theme_patterns, code_examples | 0.660 | RELEVANT |
| 198 | How to use the Shopify Checkout Extensibility? | how_to | theme_patterns, code_examples | 0.620 | PARTIAL |
| 199 | How to implement store locator functionality? | how_to | code_examples, theme_patterns | 0.560 | PARTIAL |
| 200 | How to use online store editor customization API? | how_to | theme_patterns, code_examples | 0.620 | PARTIAL |
| 201 | How to create a headless Shopify storefront? | how_to | theme_patterns, code_examples | 0.400 | PARTIAL |
| 202 | Build me a product card section with image, title, and price | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 203 | Generate a Liquid snippet for a star rating display | code_gen | code_examples, theme_patterns | 0.390 | IRRELEVANT |
| 204 | Create a section for a hero banner with text overlay | code_gen | code_examples, theme_patterns | 0.817 | RELEVANT |
| 205 | Build me a color swatch variant picker in Liquid | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 206 | Generate a Liquid template for a FAQ page | code_gen | code_examples, theme_patterns | 0.730 | RELEVANT |
| 207 | Create a section for featured collections grid | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 208 | Build me an AJAX add to cart form | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 209 | Generate a responsive image gallery with thumbnails | code_gen | code_examples, theme_patterns | 0.460 | PARTIAL |
| 210 | Create a section for customer testimonials | code_gen | code_examples, theme_patterns | 0.710 | RELEVANT |
| 211 | Build me a mega menu navigation | code_gen | code_examples, theme_patterns | 0.810 | RELEVANT |
| 212 | Generate a product comparison table in Liquid | code_gen | code_examples, theme_patterns | 0.590 | PARTIAL |
| 213 | Create a section for an image with text layout | code_gen | code_examples, theme_patterns | 1.000 | RELEVANT |
| 214 | Build me a collection filter sidebar | code_gen | code_examples, theme_patterns | 0.920 | RELEVANT |
| 215 | Generate a Liquid snippet for breadcrumb navigation | code_gen | code_examples, theme_patterns | 0.890 | RELEVANT |
| 216 | Create a custom product page template with tabs | how_to | theme_patterns, code_examples | 0.890 | RELEVANT |
| 217 | Build me a newsletter popup modal | code_gen | code_examples, theme_patterns | 0.460 | PARTIAL |
| 218 | Generate a multi-column section with icons | code_gen | code_examples, theme_patterns | 0.710 | RELEVANT |

---
*Report generated by run_v3_test.py on 2026-02-09 13:46:26*