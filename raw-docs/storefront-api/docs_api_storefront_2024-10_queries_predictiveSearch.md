---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/predictiveSearch
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

List of the predictive search results.

* limit (Int)
* limitScope (PredictiveSearchLimitScope)
* query (String!)
* searchableFields ([SearchableField!])
* types ([PredictiveSearchType!])
* unavailableProducts (SearchUnavailableProductsType)

[Anchor to limit](/docs/api/storefront/latest/queries/predictiveSearch#arguments-limit)limit •[Int](/docs/api/storefront/latest/scalars/Int)
:   Limits the number of results based on `limit_scope`. The value can range from 1 to 10, and the default is 10.

[Anchor to limitScope](/docs/api/storefront/latest/queries/predictiveSearch#arguments-limitScope)limitScope •[PredictiveSearchLimitScope](/docs/api/storefront/latest/enums/PredictiveSearchLimitScope)
:   Decides the distribution of results.

    Show enum values

[Anchor to query](/docs/api/storefront/latest/queries/predictiveSearch#arguments-query)query •[String!](/docs/api/storefront/latest/scalars/String) required
:   The search query.

[Anchor to searchableFields](/docs/api/storefront/latest/queries/predictiveSearch#arguments-searchableFields)searchableFields •[[SearchableField!]](/docs/api/storefront/latest/enums/SearchableField)
:   Specifies the list of resource fields to use for search. The default fields searched on are TITLE, PRODUCT\_TYPE, VARIANT\_TITLE, and VENDOR. For the best search experience, you should search on the default field set.

    The input must not contain more than `250` values.

    Show enum values

[Anchor to types](/docs/api/storefront/latest/queries/predictiveSearch#arguments-types)types •[[PredictiveSearchType!]](/docs/api/storefront/latest/enums/PredictiveSearchType)
:   The types of resources to search for.

    The input must not contain more than `250` values.

    Show enum values

[Anchor to unavailableProducts](/docs/api/storefront/latest/queries/predictiveSearch#arguments-unavailableProducts)unavailableProducts •[SearchUnavailableProductsType](/docs/api/storefront/latest/enums/SearchUnavailableProductsType)
:   Specifies how unavailable products are displayed in the search results.

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/predictiveSearch#possible-returns)Possible returns

* PredictiveSearchResult (PredictiveSearchResult)

[Anchor to PredictiveSearchResult](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult)PredictiveSearchResult •[PredictiveSearchResult](/docs/api/storefront/latest/objects/PredictiveSearchResult)
:   A predictive search result represents a list of products, collections, pages, articles, and query suggestions
    that matches the predictive search query.

    Show fields

    [Anchor to articles](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult.fields.articles)articles •[[Article!]!](/docs/api/storefront/latest/objects/Article) non-null
    :   The articles that match the search query.

        Show fields

    [Anchor to collections](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult.fields.collections)collections •[[Collection!]!](/docs/api/storefront/latest/objects/Collection) non-null
    :   The articles that match the search query.

        Show fields

    [Anchor to pages](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult.fields.pages)pages •[[Page!]!](/docs/api/storefront/latest/objects/Page) non-null
    :   The pages that match the search query.

        Show fields

    [Anchor to products](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult.fields.products)products •[[Product!]!](/docs/api/storefront/latest/objects/Product) non-null
    :   The products that match the search query.

        Show fields

    [Anchor to queries](/docs/api/storefront/latest/queries/predictiveSearch#returns-PredictiveSearchResult.fields.queries)queries •[[SearchQuerySuggestion!]!](/docs/api/storefront/latest/objects/SearchQuerySuggestion) non-null
    :   The query suggestions that are relevant to the search query.

        Show fields

---

Was this section helpful?

YesNo