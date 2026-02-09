---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/search
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

List of the search results.

* after (String)
* before (String)
* first (Int)
* last (Int)
* prefix (SearchPrefixQueryType)
* productFilters ([ProductFilter!])
* query (String!)
* reverse (Boolean)
* sortKey (SearchSortKeys)
* types ([SearchType!])
* unavailableProducts (SearchUnavailableProductsType)

[Anchor to after](/docs/api/storefront/latest/queries/search#arguments-after)after •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come after the specified cursor.

[Anchor to before](/docs/api/storefront/latest/queries/search#arguments-before)before •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come before the specified cursor.

[Anchor to first](/docs/api/storefront/latest/queries/search#arguments-first)first •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the first `n` elements from the list.

[Anchor to last](/docs/api/storefront/latest/queries/search#arguments-last)last •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the last `n` elements from the list.

[Anchor to prefix](/docs/api/storefront/latest/queries/search#arguments-prefix)prefix •[SearchPrefixQueryType](/docs/api/storefront/latest/enums/SearchPrefixQueryType)
:   Specifies whether to perform a partial word match on the last search term.

    Show enum values

[Anchor to productFilters](/docs/api/storefront/latest/queries/search#arguments-productFilters)productFilters •[[ProductFilter!]](/docs/api/storefront/latest/input-objects/ProductFilter)
:   Returns a subset of products matching all product filters.

    The input must not contain more than `250` values.

    Show input fields

[Anchor to query](/docs/api/storefront/latest/queries/search#arguments-query)query •[String!](/docs/api/storefront/latest/scalars/String) required
:   The search query.

[Anchor to reverse](/docs/api/storefront/latest/queries/search#arguments-reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/storefront/latest/queries/search#arguments-sortKey)sortKey •[SearchSortKeys](/docs/api/storefront/latest/enums/SearchSortKeys) Default:RELEVANCE
:   Sort the underlying list by the given key.

    Show enum values

[Anchor to types](/docs/api/storefront/latest/queries/search#arguments-types)types •[[SearchType!]](/docs/api/storefront/latest/enums/SearchType)
:   The types of resources to search for.

    The input must not contain more than `250` values.

    Show enum values

[Anchor to unavailableProducts](/docs/api/storefront/latest/queries/search#arguments-unavailableProducts)unavailableProducts •[SearchUnavailableProductsType](/docs/api/storefront/latest/enums/SearchUnavailableProductsType)
:   Specifies how unavailable products or variants are displayed in the search results.

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/search#possible-returns)Possible returns

* edges ([SearchResultItemEdge!]!)
* nodes ([SearchResultItem!]!)
* pageInfo (PageInfo!)
* productFilters ([Filter!]!)
* totalCount (Int!)

[Anchor to edges](/docs/api/storefront/latest/queries/search#returns-edges)edges •[[SearchResultItemEdge!]!](/docs/api/storefront/latest/objects/SearchResultItemEdge) non-null
:   A list of edges.

    Show fields

[Anchor to nodes](/docs/api/storefront/latest/queries/search#returns-nodes)nodes •[[SearchResultItem!]!](/docs/api/storefront/latest/unions/SearchResultItem) non-null
:   A list of the nodes contained in SearchResultItemEdge.

    Show union types

[Anchor to pageInfo](/docs/api/storefront/latest/queries/search#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/storefront/latest/objects/PageInfo) non-null
:   Information to aid in pagination.

    Show fields

[Anchor to productFilters](/docs/api/storefront/latest/queries/search#returns-productFilters)productFilters •[[Filter!]!](/docs/api/storefront/latest/objects/Filter) non-null
:   A list of available filters.

    Show fields

[Anchor to totalCount](/docs/api/storefront/latest/queries/search#returns-totalCount)totalCount •[Int!](/docs/api/storefront/latest/scalars/Int) non-null
:   The total number of results.

---

Was this section helpful?

YesNo