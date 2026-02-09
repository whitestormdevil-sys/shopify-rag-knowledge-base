---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/products
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Retrieves a list of [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
in a store. Products are the items that merchants can sell in their store.

Use the `products` query when you need to:

* Build a browsing interface for a product catalog.
* Create product [searching](https://shopify.dev/docs/api/usage/search-syntax), [sorting](https://shopify.dev/docs/api/admin-graphql/latest/queries/products#arguments-sortKey), and [filtering](https://shopify.dev/docs/api/admin-graphql/latest/queries/products#arguments-query) experiences.
* Implement product recommendations.
* Sync product data with external systems.

The `products` query supports [pagination](https://shopify.dev/docs/api/usage/pagination-graphql)
to handle large product catalogs and [saved searches](https://shopify.dev/docs/api/admin-graphql/latest/queries/products#arguments-savedSearchId)
for frequently used product queries.

The `products` query returns products with their associated metadata, including:

* Basic product information (for example, title, description, vendor, and type)
* Product options and product variants, with their prices and inventory
* Media attachments (for example, images and videos)
* SEO metadata
* Product categories and tags
* Product availability and publishing statuses

Learn more about working with [Shopify's product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/product-model-components).

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* savedSearchId (ID)
* sortKey (ProductSortKeys)

[Anchor to after](/docs/api/admin-graphql/latest/queries/products#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/products#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/products#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/products#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/products#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-default) default •string
    :   Filter by a case-insensitive search of multiple fields in a document.

    Example:

    * `query=Bob Norman`
    * `query=title:green hoodie`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-barcode) barcode •string
    :   Filter by the product variant [`barcode`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-barcode) field.

    Example:

    * `barcode:ABC-abc-1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-bundles) bundles •boolean
    :   Filter by a [product bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles). A product bundle is a set of two or more related products, which are commonly offered at a discount.

    Example:

    * `bundles:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-category_id) category\_id •string
    :   Filter by the product [category ID](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-category) (`product.category.id`). A product category is the category of a product from [Shopify's Standard Product Taxonomy](https://shopify.github.io/product-taxonomy/releases/unstable/?categoryId=sg-4-17-2-17).

    Example:

    * `category_id:sg-4-17-2-17`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-collection_id) collection\_id •id
    :   Filter by the collection [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Collection#field-id) field.

    Example:

    * `collection_id:108179161409`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-combined_listing_role) combined\_listing\_role •string
    :   Filter by the role of the product in a [combined listing](https://shopify.dev/apps/build/product-merchandising/combined-listings).

    Valid values:

    * `parent`
    * `child`
    * `no_role`

    Example:

    * `combined_listing_role:parent`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-created_at) created\_at •time
    :   Filter by the date and time when the product was created.

    Example:

    * `created_at:>'2020-10-21T23:39:20Z'`
    * `created_at:<now`
    * `created_at:<='2024'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-delivery_profile_id) delivery\_profile\_id •id
    :   Filter by the delivery profile [`id`](https://shopify.dev/api/admin-graphql/latest/objects/DeliveryProfile#field-id) field.

    Example:

    * `delivery_profile_id:108179161409`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-error_feedback) error\_feedback •string
    :   Filter by products with publishing errors.

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-gift_card) gift\_card •boolean
    :   Filter by the product [`isGiftCard`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-isgiftcard) field.

    Example:

    * `gift_card:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-handle) handle •string
    :   Filter by a comma-separated list of product [handles](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-handle).

    Example:

    * `handle:the-minimal-snowboard`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-has_only_composites) has\_only\_composites •boolean
    :   Filter by products that have only composite variants.

    Example:

    * `has_only_composites:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-has_only_default_variant) has\_only\_default\_variant •boolean
    :   Filter by products that have only a default variant. A default variant is the only variant if no other variants are specified.

    Example:

    * `has_only_default_variant:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-has_variant_with_components) has\_variant\_with\_components •boolean
    :   Filter by products that have variants with associated components.

    Example:

    * `has_variant_with_components:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-inventory_total) inventory\_total •integer
    :   Filter by inventory count.

    Example:

    * `inventory_total:0`
    * `inventory_total:>150`
    * `inventory_total:>=200`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-is_price_reduced) is\_price\_reduced •boolean
    :   Filter by products that have a reduced price. For more information, refer to the [`CollectionRule`](https://shopify.dev/api/admin-graphql/latest/objects/CollectionRule) object.

    Example:

    * `is_price_reduced:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
    :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

    Example:

    * `metafields.custom.on_sale:true`
    * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-out_of_stock_somewhere) out\_of\_stock\_somewhere •boolean
    :   Filter by products that are out of stock in at least one location.

    Example:

    * `out_of_stock_somewhere:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-price) price •bigdecimal
    :   Filter by the product variant [`price`](https://shopify.dev/api/admin-graphql/latest/objects/Productvariant#field-price) field.

    Example:

    * `price:100.57`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-product_configuration_owner) product\_configuration\_owner •string
    :   Filter by the app [`id`](https://shopify.dev/api/admin-graphql/latest/objects/App#field-id) field.

    Example:

    * `product_configuration_owner:10001`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-product_publication_status) product\_publication\_status •string
    :   Filter by channel approval process status of the resource on a channel, such as the online store. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.app) (`Channel.app.id`) and one of the valid values. For simple visibility checks, use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) instead.

    Valid values:

    * `* {channel_app_id}-approved`
    * `* {channel_app_id}-rejected`
    * `* {channel_app_id}-needs_action`
    * `* {channel_app_id}-awaiting_review`
    * `* {channel_app_id}-published`
    * `* {channel_app_id}-demoted`
    * `* {channel_app_id}-scheduled`
    * `* {channel_app_id}-provisionally_published`

    Example:

    * `product_publication_status:189769876-approved`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-product_type) product\_type •string
    :   Filter by a comma-separated list of [product types](https://help.shopify.com/manual/products/details/product-type).

    Example:

    * `product_type:snowboard`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-publication_ids) publication\_ids •string
    :   Filter by a comma-separated list of publication IDs that are associated with the product.

    Example:

    * `publication_ids:184111530305,184111694145`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) publishable\_status •string
    :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

    Valid values:

    * `* {channel_app_id}-unset`
    * `* {channel_app_id}-pending`
    * `* {channel_app_id}-approved`
    * `* {channel_app_id}-not_approved`

    Example:

    * `publishable_status:580111-unset`
    * `publishable_status:580111-pending`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-published_at) published\_at •time
    :   Filter by the date and time when the product was published to the online store and other sales channels.

    Example:

    * `published_at:>2020-10-21T23:39:20Z`
    * `published_at:<now`
    * `published_at:<=2024`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-published_status) published\_status •string
    :   Filter resources by their visibility and publication state on a channel. Online store channel filtering: - `online_store_channel`: Returns all resources in the online store channel, regardless of publication status. - `published`/`visible`: Returns resources that are published to the online store. - `unpublished`: Returns resources that are not published to the online store. Channel-specific filtering using the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) with suffixes: - `{channel_app_id}-published`: Returns resources published to the specified channel. - `{channel_app_id}-visible`: Same as `{channel_app_id}-published` (kept for backwards compatibility). - `{channel_app_id}-intended`: Returns resources added to the channel but not yet published. - `{channel_app_id}-hidden`: Returns resources not added to the channel or not published. Other: - `unavailable`: Returns resources not published to any channel.

    Valid values:

    * `online_store_channel`
    * `published`
    * `visible`
    * `unpublished`
    * `* {channel_app_id}-published`
    * `* {channel_app_id}-visible`
    * `* {channel_app_id}-intended`
    * `* {channel_app_id}-hidden`
    * `unavailable`

    Example:

    * `published_status:online_store_channel`
    * `published_status:published`
    * `published_status:580111-published`
    * `published_status:580111-hidden`
    * `published_status:unavailable`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-sku) sku •string
    :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

    Example:

    * `sku:XYZ-12345`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-status) status •string
    :   Filter by a comma-separated list of statuses. You can use statuses to manage inventory. Shopify only displays products with an `ACTIVE` status in online stores, sales channels, and apps.

    Valid values:

    * `active` Default
    * `archived`
    * `draft`

    Example:

    * `status:active,draft`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-tag) tag •string
    :   Filter objects by the `tag` field.

    Example:

    * `tag:my_tag`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-tag_not) tag\_not •string
    :   Filter by objects that don’t have the specified tag.

    Example:

    * `tag_not:my_tag`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-title) title •string
    :   Filter by the product [`title`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-title) field.

    Example:

    * `title:The Minimal Snowboard`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-updated_at) updated\_at •time
    :   Filter by the date and time when the product was last updated.

    Example:

    * `updated_at:>'2020-10-21T23:39:20Z'`
    * `updated_at:<now`
    * `updated_at:<='2024'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-variant_id) variant\_id •id
    :   Filter by the product variant [`id`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-id) field.

    Example:

    * `variant_id:45779434701121`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-variant_title) variant\_title •string
    :   Filter by the product variant [`title`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-title) field.

    Example:

    * `variant_title:'Special ski wax'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/products#argument-query-filter-vendor) vendor •string
    :   Filter by the origin or source of the product. Learn more about [vendors and managing vendor information](https://help.shopify.com/manual/products/managing-vendor-info).

    Example:

    * `vendor:Snowdevil`
    * `vendor:Snowdevil OR vendor:Icedevil`

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/products#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to savedSearchId](/docs/api/admin-graphql/latest/queries/products#arguments-savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
    The search’s query string is used as the query argument.

[Anchor to sortKey](/docs/api/admin-graphql/latest/queries/products#arguments-sortKey)sortKey •[ProductSortKeys](/docs/api/admin-graphql/latest/enums/ProductSortKeys) Default:ID
:   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/products#possible-returns)Possible returns

* edges ([ProductEdge!]!)
* nodes ([Product!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/products#returns-edges)edges •[[ProductEdge!]!](/docs/api/admin-graphql/latest/objects/ProductEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/products#returns-nodes)nodes •[[Product!]!](/docs/api/admin-graphql/latest/objects/Product) non-null
:   A list of nodes that are contained in ProductEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/products#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo