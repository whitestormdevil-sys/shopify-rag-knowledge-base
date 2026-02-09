---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/products
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Returns a list of the shop's products. For storefront search, use the [`search`](https://shopify.dev/docs/api/storefront/latest/queries/search) query.

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* sortKey (ProductSortKeys)

[Anchor to after](/docs/api/storefront/latest/queries/products#arguments-after)after •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come after the specified cursor.

[Anchor to before](/docs/api/storefront/latest/queries/products#arguments-before)before •[String](/docs/api/storefront/latest/scalars/String)
:   Returns the elements that come before the specified cursor.

[Anchor to first](/docs/api/storefront/latest/queries/products#arguments-first)first •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the first `n` elements from the list.

[Anchor to last](/docs/api/storefront/latest/queries/products#arguments-last)last •[Int](/docs/api/storefront/latest/scalars/Int)
:   Returns up to the last `n` elements from the list.

[Anchor to query](/docs/api/storefront/latest/queries/products#arguments-query)query •[String](/docs/api/storefront/latest/scalars/String)
:   You can apply one or multiple filters to a query.
    Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-available_for_sale) available\_for\_sale •
    :   Filter by products that have at least one product variant available for sale.

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-created_at) created\_at •
    :   Filter by the date and time when the product was created.

    Example:

    * `created_at:>'2020-10-21T23:39:20Z'`
    * `created_at:<now`
    * `created_at:<=2024`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-product_type) product\_type •
    :   Filter by a comma-separated list of [product types](https://help.shopify.com/en/manual/products/details/product-type).

    Example:

    * `product_type:snowboard`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-tag) tag •
    :   Filter products by the product [`tags`](https://shopify.dev/docs/api/storefront/latest/objects/Product#field-tags) field.

    Example:

    * `tag:my_tag`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-tag_not) tag\_not •
    :   Filter by products that don't have the specified product [tags](https://shopify.dev/docs/api/storefront/latest/objects/Product#field-tags).

    Example:

    * `tag_not:my_tag`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-title) title •
    :   Filter by the product [`title`](https://shopify.dev/docs/api/storefront/latest/objects/Product#field-title) field.

    Example:

    * `title:The Minimal Snowboard`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-updated_at) updated\_at •
    :   Filter by the date and time when the product was last updated.

    Example:

    * `updated_at:>'2020-10-21T23:39:20Z'`
    * `updated_at:<now`
    * `updated_at:<=2024`

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-variants.price) variants.price •
    :   Filter by the price of the product's variants.

    [Anchor to](/docs/api/storefront/latest/queries/products#argument-query-filter-vendor) vendor •
    :   Filter by the product [`vendor`](https://shopify.dev/docs/api/storefront/latest/objects/Product#field-vendor) field.

    Example:

    * `vendor:Snowdevil`
    * `vendor:Snowdevil OR vendor:Icedevil`

[Anchor to reverse](/docs/api/storefront/latest/queries/products#arguments-reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/storefront/latest/queries/products#arguments-sortKey)sortKey •[ProductSortKeys](/docs/api/storefront/latest/enums/ProductSortKeys) Default:ID
:   Sort the underlying list by the given key.

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/products#possible-returns)Possible returns

* edges ([ProductEdge!]!)
* filters ([Filter!]!)
* nodes ([Product!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/storefront/latest/queries/products#returns-edges)edges •[[ProductEdge!]!](/docs/api/storefront/latest/objects/ProductEdge) non-null
:   A list of edges.

    Show fields

[Anchor to filters](/docs/api/storefront/latest/queries/products#returns-filters)filters •[[Filter!]!](/docs/api/storefront/latest/objects/Filter) non-null
:   A list of available filters.

    Show fields

[Anchor to nodes](/docs/api/storefront/latest/queries/products#returns-nodes)nodes •[[Product!]!](/docs/api/storefront/latest/objects/Product) non-null
:   A list of the nodes contained in ProductEdge.

    Show fields

[Anchor to pageInfo](/docs/api/storefront/latest/queries/products#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/storefront/latest/objects/PageInfo) non-null
:   Information to aid in pagination.

    Show fields

---

Was this section helpful?

YesNo