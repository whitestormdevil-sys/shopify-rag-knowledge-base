---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/inventoryItems
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Returns a list of inventory items.

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)

[Anchor to after](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/inventoryItems#argument-query-filter-created_at) created\_at •time

    [Anchor to](/docs/api/admin-graphql/latest/queries/inventoryItems#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/inventoryItems#argument-query-filter-sku) sku •string
    :   Filter by the inventory item [`sku`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

    Example:

    * `sku:XYZ-12345`

    [Anchor to](/docs/api/admin-graphql/latest/queries/inventoryItems#argument-query-filter-updated_at) updated\_at •time

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/inventoryItems#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/inventoryItems#possible-returns)Possible returns

* edges ([InventoryItemEdge!]!)
* nodes ([InventoryItem!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/inventoryItems#returns-edges)edges •[[InventoryItemEdge!]!](/docs/api/admin-graphql/latest/objects/InventoryItemEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/inventoryItems#returns-nodes)nodes •[[InventoryItem!]!](/docs/api/admin-graphql/latest/objects/InventoryItem) non-null
:   A list of nodes that are contained in InventoryItemEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/inventoryItems#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo