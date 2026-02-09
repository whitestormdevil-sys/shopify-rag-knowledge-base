---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/blogs
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

List of the shop's blogs.

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* sortKey (BlogSortKeys)

[Anchor to after](/docs/api/storefront/latest/queries/blogs#arguments-after)after •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come after the specified cursor.

[Anchor to before](/docs/api/storefront/latest/queries/blogs#arguments-before)before •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come before the specified cursor.

[Anchor to first](/docs/api/storefront/latest/queries/blogs#arguments-first)first •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the first `n` elements from the list.

[Anchor to last](/docs/api/storefront/latest/queries/blogs#arguments-last)last •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the last `n` elements from the list.

[Anchor to query](/docs/api/storefront/latest/queries/blogs#arguments-query)query •[String](/docs/api/storefront/latest/scalars/String)
:   Apply one or multiple filters to the query.
    Refer to the detailed [search syntax](https://shopify.dev/api/usage/search-syntax) for more information about using filters.

    Show filters

    [Anchor to](/docs/api/storefront/latest/queries/blogs#argument-query-filter-created_at) created\_at •

    [Anchor to](/docs/api/storefront/latest/queries/blogs#argument-query-filter-handle) handle •

    [Anchor to](/docs/api/storefront/latest/queries/blogs#argument-query-filter-title) title •

    [Anchor to](/docs/api/storefront/latest/queries/blogs#argument-query-filter-updated_at) updated\_at •

[Anchor to reverse](/docs/api/storefront/latest/queries/blogs#arguments-reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/storefront/latest/queries/blogs#arguments-sortKey)sortKey •[BlogSortKeys](/docs/api/storefront/latest/enums/BlogSortKeys) Default:ID
:   Sort the underlying list by the given key.

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/blogs#possible-returns)Possible returns

* edges ([BlogEdge!]!)
* nodes ([Blog!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/storefront/latest/queries/blogs#returns-edges)edges •[[BlogEdge!]!](/docs/api/storefront/latest/objects/BlogEdge) non-null
:   A list of edges.

    Show fields

[Anchor to nodes](/docs/api/storefront/latest/queries/blogs#returns-nodes)nodes •[[Blog!]!](/docs/api/storefront/latest/objects/Blog) non-null
:   A list of the nodes contained in BlogEdge.

    Show fields

[Anchor to pageInfo](/docs/api/storefront/latest/queries/blogs#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/storefront/latest/objects/PageInfo) non-null
:   Information to aid in pagination.

    Show fields

---

Was this section helpful?

YesNo