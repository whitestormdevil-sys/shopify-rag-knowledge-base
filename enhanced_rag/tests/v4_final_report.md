# V4 Final Validation Report — Independent Audit

**Date:** 2026-02-09 16:06 UTC
**Total Queries:** 300
**Total Time:** 299.3s (1.0 queries/sec)
**Engine Config:** top_k=5, use_reranker=False, expand_parents=False
**Grading:** Top-3 results only, strict topic word-boundary matching

## Executive Summary

| Metric | Value |
|--------|-------|
| **RELEVANT** | 157 (52.3%) |
| **PARTIAL** | 129 (43.0%) |
| **IRRELEVANT** | 14 (4.7%) |
| **NO_RESULTS** | 0 (0.0%) |
| **Pass Rate (RELEVANT+PARTIAL)** | **95.3%** |
| **Strict Pass (RELEVANT only)** | **52.3%** |
| **Average Score (0-3)** | **2.48** |
| **Avg Query Time** | 997ms |

### Verdict

🟡 **CONDITIONALLY READY** — Good pass rate but strict relevance needs improvement.

## Per-Category Breakdown

| Category | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |
|----------|-------|----------|---------|------------|------------|-----------|-----------|
| APIs | 25 | 18 | 6 | 1 | 0 | 96% | 2.68 |
| Advanced Features | 25 | 9 | 14 | 2 | 0 | 92% | 2.28 |
| CSS & Styling | 20 | 12 | 8 | 0 | 0 | 100% | 2.60 |
| Cart & Checkout | 25 | 11 | 14 | 0 | 0 | 100% | 2.44 |
| Code Generation | 20 | 10 | 10 | 0 | 0 | 100% | 2.50 |
| Collections & Search | 20 | 8 | 11 | 1 | 0 | 95% | 2.35 |
| Edge Cases | 20 | 6 | 11 | 3 | 0 | 85% | 2.15 |
| Liquid Advanced | 20 | 14 | 5 | 1 | 0 | 95% | 2.65 |
| Liquid Basics | 30 | 17 | 10 | 3 | 0 | 90% | 2.47 |
| Performance | 20 | 11 | 9 | 0 | 0 | 100% | 2.55 |
| Product & Variants | 25 | 13 | 11 | 1 | 0 | 96% | 2.48 |
| Theme Architecture | 25 | 16 | 8 | 1 | 0 | 96% | 2.60 |
| Troubleshooting | 25 | 12 | 12 | 1 | 0 | 96% | 2.44 |

## Per-Difficulty Breakdown

| Difficulty | Total | Relevant | Partial | Irrelevant | No Results | Pass Rate | Avg Score |
|------------|-------|----------|---------|------------|------------|-----------|-----------|
| easy | 61 | 34 | 20 | 7 | 0 | 89% | 2.44 |
| medium | 154 | 80 | 71 | 3 | 0 | 98% | 2.50 |
| hard | 85 | 43 | 38 | 4 | 0 | 95% | 2.46 |

## Intent Detection Statistics

| Intent | Count | Relevant | Partial | Irrelevant | Pass Rate | Avg Score |
|--------|-------|----------|---------|------------|-----------|-----------|
| how_to | 213 | 110 | 92 | 11 | 95% | 2.46 |
| reference | 31 | 20 | 9 | 2 | 94% | 2.58 |
| debug | 29 | 13 | 16 | 0 | 100% | 2.45 |
| code_gen | 13 | 7 | 6 | 0 | 100% | 2.54 |
| comparison | 11 | 6 | 5 | 0 | 100% | 2.55 |
| architecture | 3 | 1 | 1 | 1 | 67% | 2.00 |

## Collection Distribution in Results

How often each collection appears in top-3 results:

| Collection | Appearances in Top-3 | #1 Result | % of Total Top-3 |
|------------|---------------------|-----------|------------------|
| theme_patterns | 412 | 132 | 45.8% |
| liquid_reference | 150 | 54 | 16.7% |
| code_examples | 109 | 34 | 12.1% |
| api_reference | 107 | 45 | 11.9% |
| best_practices | 78 | 24 | 8.7% |
| troubleshooting | 44 | 11 | 4.9% |

### Expected vs Actual Collection Match Rate

How often the expected collection(s) appear in top-3:

| Expected Collection | Times Expected | Times Found in Top-3 | Hit Rate |
|---------------------|---------------|---------------------|----------|
| api_reference | 66 | 41 | 62% |
| best_practices | 41 | 19 | 46% |
| code_examples | 112 | 46 | 41% |
| liquid_reference | 99 | 49 | 49% |
| theme_patterns | 118 | 105 | 89% |
| troubleshooting | 40 | 24 | 60% |

## Top 20 Worst Queries

Sorted by grade (worst first), then by topic miss count:

### 1. Q88: How to handle products with more than 3 options?
- **Grade:** IRRELEVANT
- **Category:** Product & Variants | **Difficulty:** hard
- **Detected Intent:** how_to
- **Expected Topics:** ['option', 'variant', 'combined_listing', 'line_item']
- **Topics Found:** []
- **Topics Missing:** ['option', 'variant', 'combined_listing', 'line_item']
- **Expected Collections:** ['liquid_reference', 'troubleshooting']
- **Actual Top-3 Collections:** ['code_examples', 'best_practices', 'best_practices']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [option, variant, combined_listing, line_item] not found in top-3 result text | Expected collections ['liquid_reference', 'troubleshooting'] not in top-3 (got ['code_examples', 'best_practices', 'best_practices']) | Collection mismatch: expected ['liquid_reference', 'troubleshooting'] but got ['code_examples', 'best_practices']
- **Top result snippet:** `### Step 1: Set up the Shopify Subscriptions app  1. Install the [Shopify Subscriptions app](https://apps.shopify.com/shopify-subscriptions). 2. In yo...`

### 2. Q146: What is the Shopify Admin REST API?
- **Grade:** IRRELEVANT
- **Category:** APIs | **Difficulty:** easy
- **Detected Intent:** reference
- **Expected Topics:** ['admin', 'rest', 'api', 'shopify', 'endpoint']
- **Topics Found:** ['api']
- **Topics Missing:** ['admin', 'rest', 'shopify', 'endpoint']
- **Expected Collections:** ['api_reference']
- **Actual Top-3 Collections:** ['liquid_reference', 'liquid_reference', 'liquid_reference']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [admin, rest, shopify, endpoint] not found in top-3 result text | Expected collections ['api_reference'] not in top-3 (got ['liquid_reference', 'liquid_reference', 'liquid_reference']) | Collection mismatch: expected ['api_reference'] but got ['liquid_reference']
- **Top result snippet:** `Ask assistant  ## [Anchor to What is a template language?](/docs/api/liquid#what-is-a-template-language)What is a template language?...`

### 3. Q294: How to import React components into a Shopify Liquid theme?
- **Grade:** IRRELEVANT
- **Category:** Edge Cases | **Difficulty:** hard
- **Detected Intent:** how_to
- **Expected Topics:** ['react', 'liquid', 'component', 'javascript']
- **Topics Found:** ['liquid']
- **Topics Missing:** ['react', 'component', 'javascript']
- **Expected Collections:** ['code_examples', 'best_practices']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [react, component, javascript] not found in top-3 result text | Expected collections ['code_examples', 'best_practices'] not in top-3 (got ['theme_patterns', 'theme_patterns', 'theme_patterns']) | Collection mismatch: expected ['code_examples', 'best_practices'] but got ['theme_patterns']
- **Top result snippet:** `Use the following process to emulate the tests that Shopify runs to determine an online store's speed score. Shopify runs a similar test against theme...`

### 4. Q10: What is the default filter and when should I use it?
- **Grade:** IRRELEVANT
- **Category:** Liquid Basics | **Difficulty:** easy
- **Detected Intent:** architecture
- **Expected Topics:** ['default', 'filter', 'nil', 'fallback']
- **Topics Found:** ['filter']
- **Topics Missing:** ['default', 'nil', 'fallback']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['best_practices', 'best_practices', 'best_practices']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [default, nil, fallback] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['best_practices', 'best_practices', 'best_practices']) | Intent classified as 'architecture' — may have misrouted | Collection mismatch: expected ['liquid_reference'] but got ['best_practices']
- **Top result snippet:** `**Faceted search filtering** - Use [search filtering](/docs/storefronts/themes/navigation-search/filtering) so that customers can filter on collection...`

### 5. Q15: How does the increment tag work?
- **Grade:** IRRELEVANT
- **Category:** Liquid Basics | **Difficulty:** easy
- **Detected Intent:** how_to
- **Expected Topics:** ['increment', 'decrement', 'counter', 'tag']
- **Topics Found:** ['increment']
- **Topics Missing:** ['decrement', 'counter', 'tag']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['theme_patterns', 'best_practices', 'code_examples']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [decrement, counter, tag] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['theme_patterns', 'best_practices', 'code_examples']) | Collection mismatch: expected ['liquid_reference'] but got ['theme_patterns', 'code_examples', 'best_practices']
- **Top result snippet:** `Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https...`

### 6. Q29: How to get the current URL in Liquid?
- **Grade:** IRRELEVANT
- **Category:** Liquid Basics | **Difficulty:** medium
- **Detected Intent:** how_to
- **Expected Topics:** ['request', 'url', 'canonical_url', 'path']
- **Topics Found:** ['url']
- **Topics Missing:** ['request', 'canonical_url', 'path']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['api_reference', 'code_examples', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [request, canonical_url, path] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['api_reference', 'code_examples', 'theme_patterns']) | Collection mismatch: expected ['liquid_reference'] but got ['api_reference', 'code_examples', 'theme_patterns']
- **Top result snippet:** `Explore how functions process input data and generate operations.  Function anatomy  Explore how functions process input data and generate operations....`

### 7. Q40: How to use metafield_tag and metafield_text filters?
- **Grade:** IRRELEVANT
- **Category:** Liquid Advanced | **Difficulty:** medium
- **Detected Intent:** how_to
- **Expected Topics:** ['metafield_tag', 'metafield_text', 'filter', 'render']
- **Topics Found:** ['filter']
- **Topics Missing:** ['metafield_tag', 'metafield_text', 'render']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [metafield_tag, metafield_text, render] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['theme_patterns', 'theme_patterns', 'theme_patterns']) | Collection mismatch: expected ['liquid_reference'] but got ['theme_patterns']
- **Top result snippet:** `If payment method logos are output, then use the `enabled_payment_types` property of the [`shop` object](/docs/api/liquid/objects/shop), and the [`pay...`

### 8. Q72: What is the config directory used for?
- **Grade:** IRRELEVANT
- **Category:** Theme Architecture | **Difficulty:** easy
- **Detected Intent:** reference
- **Expected Topics:** ['config', 'settings_data', 'settings_schema']
- **Topics Found:** []
- **Topics Missing:** ['config', 'settings_data', 'settings_schema']
- **Expected Collections:** ['theme_patterns']
- **Actual Top-3 Collections:** ['liquid_reference', 'liquid_reference', 'api_reference']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [config, settings_data, settings_schema] not found in top-3 result text | Expected collections ['theme_patterns'] not in top-3 (got ['liquid_reference', 'liquid_reference', 'api_reference']) | Collection mismatch: expected ['theme_patterns'] but got ['liquid_reference', 'api_reference']
- **Top result snippet:** `## [Anchor to Modifying output with filters](/docs/api/liquid#modifying-output-with-filters)Modifying output with filters  Liquid filters modify the o...`

### 9. Q226: My theme changes aren't appearing after save - why?
- **Grade:** IRRELEVANT
- **Category:** Troubleshooting | **Difficulty:** medium
- **Detected Intent:** how_to
- **Expected Topics:** ['cache', 'change', 'save', 'preview']
- **Topics Found:** ['save']
- **Topics Missing:** ['cache', 'change', 'preview']
- **Expected Collections:** ['troubleshooting']
- **Actual Top-3 Collections:** ['best_practices', 'theme_patterns', 'best_practices']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [cache, change, preview] not found in top-3 result text | Expected collections ['troubleshooting'] not in top-3 (got ['best_practices', 'theme_patterns', 'best_practices']) | Collection mismatch: expected ['troubleshooting'] but got ['theme_patterns', 'best_practices']
- **Top result snippet:** `## [Anchor to Why build for Flow](/docs/apps/build/flow#why-build-for-flow)Why build for Flow  Building for Flow can help you to increase the value of...`

### 10. Q245: How to use checkout extensibility?
- **Grade:** IRRELEVANT
- **Category:** Advanced Features | **Difficulty:** hard
- **Detected Intent:** how_to
- **Expected Topics:** ['checkout', 'extensibility', 'ui', 'extension']
- **Topics Found:** ['checkout']
- **Topics Missing:** ['extensibility', 'ui', 'extension']
- **Expected Collections:** ['api_reference']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [extensibility, ui, extension] not found in top-3 result text | Expected collections ['api_reference'] not in top-3 (got ['theme_patterns', 'theme_patterns', 'theme_patterns']) | Collection mismatch: expected ['api_reference'] but got ['theme_patterns']
- **Top result snippet:** `Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https...`

### 11. Q253: How to use the Shopify Admin Extensions API?
- **Grade:** IRRELEVANT
- **Category:** Advanced Features | **Difficulty:** hard
- **Detected Intent:** how_to
- **Expected Topics:** ['admin', 'extension', 'api', 'ui']
- **Topics Found:** ['api']
- **Topics Missing:** ['admin', 'extension', 'ui']
- **Expected Collections:** ['api_reference']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [admin, extension, ui] not found in top-3 result text | Expected collections ['api_reference'] not in top-3 (got ['theme_patterns', 'theme_patterns', 'theme_patterns']) | Collection mismatch: expected ['api_reference'] but got ['theme_patterns']
- **Top result snippet:** `Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https...`

### 12. Q137: How to show product count per collection?
- **Grade:** IRRELEVANT
- **Category:** Collections & Search | **Difficulty:** easy
- **Detected Intent:** how_to
- **Expected Topics:** ['collection', 'products_count', 'count']
- **Topics Found:** ['collection']
- **Topics Missing:** ['products_count', 'count']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['code_examples', 'code_examples', 'theme_patterns']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [products_count, count] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['code_examples', 'code_examples', 'theme_patterns']) | Collection mismatch: expected ['liquid_reference'] but got ['theme_patterns', 'code_examples']
- **Top result snippet:** `export default function Collection() {   const {collection} = useLoaderData<typeof loader>();    return (     <div className="collection">       <h1>{...`

### 13. Q285: {{ }}
- **Grade:** IRRELEVANT
- **Category:** Edge Cases | **Difficulty:** easy
- **Detected Intent:** how_to
- **Expected Topics:** ['liquid', 'output', 'tag']
- **Topics Found:** ['liquid']
- **Topics Missing:** ['output', 'tag']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['code_examples', 'api_reference', 'code_examples']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [output, tag] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['code_examples', 'api_reference', 'code_examples']) | Collection mismatch: expected ['liquid_reference'] but got ['api_reference', 'code_examples']
- **Top result snippet:** `{   "sections": {     "main": {       "type": "main-order"     }   },   "order": [     "main"   ] }...`

### 14. Q290: image_url
- **Grade:** IRRELEVANT
- **Category:** Edge Cases | **Difficulty:** easy
- **Detected Intent:** how_to
- **Expected Topics:** ['image_url', 'filter', 'cdn']
- **Topics Found:** ['image_url']
- **Topics Missing:** ['filter', 'cdn']
- **Expected Collections:** ['liquid_reference']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'code_examples']
- **Collections Found:** []
- **Results Returned:** 5
- **WHY:** Missing topics [filter, cdn] not found in top-3 result text | Expected collections ['liquid_reference'] not in top-3 (got ['theme_patterns', 'theme_patterns', 'code_examples']) | Collection mismatch: expected ['liquid_reference'] but got ['theme_patterns', 'code_examples']
- **Top result snippet:** `All images require the `alt` attribute. Themes must use [`image.alt`](/docs/api/liquid/objects/image#image-alt) or [`image_url | image_tag: alt: strin...`

### 15. Q100: product.metafields.custom.my_field returns nil why???
- **Grade:** PARTIAL
- **Category:** Product & Variants | **Difficulty:** medium
- **Detected Intent:** debug
- **Expected Topics:** ['metafield', 'nil', 'product', 'definition', 'namespace']
- **Topics Found:** []
- **Topics Missing:** ['metafield', 'nil', 'product', 'definition', 'namespace']
- **Expected Collections:** ['troubleshooting', 'liquid_reference']
- **Actual Top-3 Collections:** ['troubleshooting', 'troubleshooting', 'troubleshooting']
- **Collections Found:** ['troubleshooting']
- **Results Returned:** 5
- **WHY:** Missing topics [metafield, nil, product, definition, namespace] not found in top-3 result text
- **Top result snippet:** `server.use(router.allowedMethods());   server.use(router.routes());   server.listen(port, () => {     console.log(`> Ready on http://localhost:${port}...`

### 16. Q178: How to use flexbox for Shopify layouts?
- **Grade:** PARTIAL
- **Category:** CSS & Styling | **Difficulty:** medium
- **Detected Intent:** how_to
- **Expected Topics:** ['flexbox', 'layout', 'css', 'align', 'justify']
- **Topics Found:** []
- **Topics Missing:** ['flexbox', 'layout', 'css', 'align', 'justify']
- **Expected Collections:** ['theme_patterns', 'code_examples']
- **Actual Top-3 Collections:** ['theme_patterns', 'theme_patterns', 'theme_patterns']
- **Collections Found:** ['theme_patterns']
- **Results Returned:** 5
- **WHY:** Missing topics [flexbox, layout, css, align, justify] not found in top-3 result text
- **Top result snippet:** `Flexible layouts that look intentional: Layouts are designed deliberately to remain visually appealing, organized, and balanced, even when content len...`

### 17. Q223: Why is my variant picker not updating the price?
- **Grade:** PARTIAL
- **Category:** Troubleshooting | **Difficulty:** hard
- **Detected Intent:** debug
- **Expected Topics:** ['variant', 'picker', 'price', 'javascript', 'change']
- **Topics Found:** []
- **Topics Missing:** ['variant', 'picker', 'price', 'javascript', 'change']
- **Expected Collections:** ['troubleshooting', 'code_examples']
- **Actual Top-3 Collections:** ['troubleshooting', 'troubleshooting', 'troubleshooting']
- **Collections Found:** ['troubleshooting']
- **Results Returned:** 5
- **WHY:** Missing topics [variant, picker, price, javascript, change] not found in top-3 result text
- **Top result snippet:** `server.use(router.allowedMethods());   server.use(router.routes());   server.listen(port, () => {     console.log(`> Ready on http://localhost:${port}...`

### 18. Q237: How do Shopify Markets work for internationalization?
- **Grade:** PARTIAL
- **Category:** Advanced Features | **Difficulty:** hard
- **Detected Intent:** how_to
- **Expected Topics:** ['market', 'international', 'currency', 'language', 'locale']
- **Topics Found:** []
- **Topics Missing:** ['market', 'international', 'currency', 'language', 'locale']
- **Expected Collections:** ['best_practices', 'api_reference']
- **Actual Top-3 Collections:** ['best_practices', 'liquid_reference', 'theme_patterns']
- **Collections Found:** ['best_practices']
- **Results Returned:** 5
- **WHY:** Missing topics [market, international, currency, language, locale] not found in top-3 result text
- **Top result snippet:** `## [Anchor to How do subscriptions work?](/docs/apps/build/purchase-options/subscriptions#how-do-subscriptions-work)How do subscriptions work?  Subscr...`

### 19. Q259: How to use Shopify Scripts (deprecated) vs Functions?
- **Grade:** PARTIAL
- **Category:** Advanced Features | **Difficulty:** hard
- **Detected Intent:** comparison
- **Expected Topics:** ['scripts', 'functions', 'deprecated', 'discount', 'migration']
- **Topics Found:** []
- **Topics Missing:** ['scripts', 'functions', 'deprecated', 'discount', 'migration']
- **Expected Collections:** ['api_reference', 'best_practices']
- **Actual Top-3 Collections:** ['best_practices', 'theme_patterns', 'best_practices']
- **Collections Found:** ['best_practices']
- **Results Returned:** 5
- **WHY:** Missing topics [scripts, functions, deprecated, discount, migration] not found in top-3 result text | Intent classified as 'comparison' — may have misrouted
- **Top result snippet:** `Shopify Dev Assistant VS Code Extension  Access AI-powered Shopify development help directly within Visual Studio Code, with automatic GraphQL query e...`

### 20. Q222: How to fix 404 errors for theme assets?
- **Grade:** PARTIAL
- **Category:** Troubleshooting | **Difficulty:** medium
- **Detected Intent:** debug
- **Expected Topics:** ['404', 'asset', 'missing', 'url', 'file']
- **Topics Found:** []
- **Topics Missing:** ['404', 'asset', 'missing', 'url', 'file']
- **Expected Collections:** ['troubleshooting']
- **Actual Top-3 Collections:** ['troubleshooting', 'liquid_reference', 'troubleshooting']
- **Collections Found:** ['troubleshooting']
- **Results Returned:** 5
- **WHY:** Missing topics [404, asset, missing, url, file] not found in top-3 result text
- **Top result snippet:** `## Q: Date Math / Manipulation in Liquid Template Filter **Score:** 27 | https://stackoverflow.com/questions/21056965/date-math-manipulation-in-liquid...`


## Identified Knowledge Gaps

Topics that consistently fail across multiple queries:

| Missing Topic | Fail Count | Example Query IDs |
|---------------|------------|-------------------|
| tag | 2 | [15, 285] |
| admin | 2 | [146, 253] |
| ui | 2 | [245, 253] |
| extension | 2 | [245, 253] |
| default | 1 | [10] |
| nil | 1 | [10] |
| fallback | 1 | [10] |
| decrement | 1 | [15] |
| counter | 1 | [15] |
| request | 1 | [29] |
| canonical_url | 1 | [29] |
| path | 1 | [29] |
| metafield_tag | 1 | [40] |
| metafield_text | 1 | [40] |
| render | 1 | [40] |
| config | 1 | [72] |
| settings_data | 1 | [72] |
| settings_schema | 1 | [72] |
| option | 1 | [88] |
| variant | 1 | [88] |
| combined_listing | 1 | [88] |
| line_item | 1 | [88] |
| products_count | 1 | [137] |
| count | 1 | [137] |
| rest | 1 | [146] |

### Weakest Categories

- 🟢 **Edge Cases**: 85% pass rate
- 🟢 **Liquid Basics**: 90% pass rate
- 🟢 **Advanced Features**: 92% pass rate
- 🟢 **Liquid Advanced**: 95% pass rate
- 🟢 **Collections & Search**: 95% pass rate
- 🟢 **Theme Architecture**: 96% pass rate
- 🟢 **Product & Variants**: 96% pass rate
- 🟢 **APIs**: 96% pass rate
- 🟢 **Troubleshooting**: 96% pass rate
- 🟢 **Cart & Checkout**: 100% pass rate
- 🟢 **CSS & Styling**: 100% pass rate
- 🟢 **Performance**: 100% pass rate
- 🟢 **Code Generation**: 100% pass rate

## Collection Routing Analysis

Cases where the search routed to wrong collections:

Total routing mismatches (expected not in top-3): **14** out of 14 failed queries

Most common mis-routes:

| Expected → Got | Count |
|----------------|-------|
| liquid_reference → code_examples | 6 |
| liquid_reference → theme_patterns | 5 |
| liquid_reference → best_practices | 3 |
| liquid_reference → api_reference | 2 |
| troubleshooting → best_practices | 2 |
| api_reference → theme_patterns | 2 |
| theme_patterns → liquid_reference | 1 |
| theme_patterns → api_reference | 1 |
| troubleshooting → code_examples | 1 |
| api_reference → liquid_reference | 1 |
| troubleshooting → theme_patterns | 1 |
| code_examples → theme_patterns | 1 |
| best_practices → theme_patterns | 1 |

## Performance (Query Latency)

- **Min:** 24ms
- **P50:** 958ms
- **P90:** 1604ms
- **P99:** 1826ms
- **Max:** 2397ms
- **Mean:** 997ms

## Overall Verdict

### Score: 2.48/3.00 — Pass Rate: 95.3%

🟡 **CONDITIONALLY READY** — Good pass rate but strict relevance needs improvement.

### Strengths

- ✅ **Liquid Basics** (90% pass rate)
- ✅ **Liquid Advanced** (95% pass rate)
- ✅ **Theme Architecture** (96% pass rate)
- ✅ **Product & Variants** (96% pass rate)
- ✅ **Cart & Checkout** (100% pass rate)
- ✅ **Collections & Search** (95% pass rate)
- ✅ **APIs** (96% pass rate)
- ✅ **CSS & Styling** (100% pass rate)
- ✅ **Performance** (100% pass rate)
- ✅ **Troubleshooting** (96% pass rate)
- ✅ **Advanced Features** (92% pass rate)
- ✅ **Code Generation** (100% pass rate)
- ✅ **Edge Cases** (85% pass rate)

### Weaknesses

- No categories below 60% pass rate (encouraging)

### Recommendations

- Improve collection routing — 14 queries went to completely wrong collections
- Top missing topics: tag, admin, ui — may need content enrichment


---
*Report generated by validate_v4_final.py — independent, unbiased assessment*