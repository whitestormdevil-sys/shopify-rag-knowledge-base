---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/pages
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

List of the shop's pages.

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* sortKey (PageSortKeys)

[Anchor to after](/docs/api/storefront/latest/queries/pages#arguments-after)after •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come after the specified cursor.

[Anchor to before](/docs/api/storefront/latest/queries/pages#arguments-before)before •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come before the specified cursor.

[Anchor to first](/docs/api/storefront/latest/queries/pages#arguments-first)first •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the first `n` elements from the list.

[Anchor to last](/docs/api/storefront/latest/queries/pages#arguments-last)last •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the last `n` elements from the list.

[Anchor to query](/docs/api/storefront/latest/queries/pages#arguments-query)query •[String](/docs/api/storefront/latest/scalars/String)
:   Apply one or multiple filters to the query.
    Refer to the detailed [search syntax](https://shopify.dev/api/usage/search-syntax) for more information about using filters.

    Show filters

    [Anchor to](/docs/api/storefront/latest/queries/pages#argument-query-filter-created_at) created\_at •

    [Anchor to](/docs/api/storefront/latest/queries/pages#argument-query-filter-handle) handle •

    [Anchor to](/docs/api/storefront/latest/queries/pages#argument-query-filter-title) title •

    [Anchor to](/docs/api/storefront/latest/queries/pages#argument-query-filter-updated_at) updated\_at •

[Anchor to reverse](/docs/api/storefront/latest/queries/pages#arguments-reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/storefront/latest/queries/pages#arguments-sortKey)sortKey •[PageSortKeys](/docs/api/storefront/latest/enums/PageSortKeys) Default:ID
:   Sort the underlying list by the given key.

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/pages#possible-returns)Possible returns

* edges ([PageEdge!]!)
* nodes ([Page!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/storefront/latest/queries/pages#returns-edges)edges •[[PageEdge!]!](/docs/api/storefront/latest/objects/PageEdge) non-null
:   A list of edges.

    Show fields

[Anchor to nodes](/docs/api/storefront/latest/queries/pages#returns-nodes)nodes •[[Page!]!](/docs/api/storefront/latest/objects/Page) non-null
:   A list of the nodes contained in PageEdge.

    Show fields

[Anchor to pageInfo](/docs/api/storefront/latest/queries/pages#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/storefront/latest/objects/PageInfo) non-null
:   Information to aid in pagination.

    Show fields

---

Was this section helpful?

YesNo