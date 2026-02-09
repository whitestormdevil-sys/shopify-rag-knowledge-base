---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/ProductVariant
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_products` access scope.

The `ProductVariant` object represents a version of a
[product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
that comes in more than one [option](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption),
such as size or color. For example, if a merchant sells t-shirts with options for size and color, then a small,
blue t-shirt would be one product variant and a large, blue t-shirt would be another.

Use the `ProductVariant` object to manage the full lifecycle and configuration of a product's variants. Common
use cases for using the `ProductVariant` object include:

* Tracking inventory for each variant
* Setting unique prices for each variant
* Assigning barcodes and SKUs to connect variants to fulfillment services
* Attaching variant-specific images and media
* Setting delivery and tax requirements
* Supporting product bundles, subscriptions, and selling plans

A `ProductVariant` is associated with a parent
[`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) object.
`ProductVariant` serves as the central link between a product's merchandising configuration, inventory,
pricing, fulfillment, and sales channels within the GraphQL Admin API schema. Each variant
can reference other GraphQL types such as:

* [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem): Used for inventory tracking
* [`Image`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Image): Used for variant-specific images
* [`SellingPlanGroup`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlanGroup): Used for subscriptions and selling plans

Learn more about [Shopify's product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/product-model-components).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/ProductVariant#fields)Fields

* availableForSale (Boolean!)
* barcode (String)
* compareAtPrice (Money)
* contextualPricing (ProductVariantContextualPricing!)
* createdAt (DateTime!)
* defaultCursor (String!)
* deliveryProfile (DeliveryProfile)
* displayName (String!)
* events (EventConnection!)
* id (ID!)
* inventoryItem (InventoryItem!)
* inventoryPolicy (ProductVariantInventoryPolicy!)
* inventoryQuantity (Int)
* legacyResourceId (UnsignedInt64!)
* media (MediaConnection!)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* position (Int!)
* price (Money!)
* product (Product!)
* productParents (ProductConnection!)
* productVariantComponents (ProductVariantComponentConnection!)
* requiresComponents (Boolean!)
* selectedOptions ([SelectedOption!]!)
* sellableOnlineQuantity (Int!)
* sellingPlanGroups (SellingPlanGroupConnection!)
* sellingPlanGroupsCount (Count)
* showUnitPrice (Boolean!)
* sku (String)
* taxable (Boolean!)
* title (String!)
* translations ([Translation!]!)
* unitPrice (MoneyV2)
* unitPriceMeasurement (UnitPriceMeasurement)
* updatedAt (DateTime!)

[Anchor to availableForSale](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.availableForSale)availableForSale •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the product variant is available for sale.

[Anchor to barcode](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.barcode)barcode •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The value of the barcode associated with the product.

[Anchor to compareAtPrice](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.compareAtPrice)compareAtPrice •[Money](/docs/api/admin-graphql/latest/scalars/Money)
:   The compare-at price of the variant in the default shop currency.

[Anchor to contextualPricing](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.contextualPricing)contextualPricing •[ProductVariantContextualPricing!](/docs/api/admin-graphql/latest/objects/ProductVariantContextualPricing) non-null
:   The pricing that applies for a customer in a given context. As of API version 2025-04, only active markets are considered in the price resolution.

    Show fields

    ### Arguments

    [Anchor to context](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.contextualPricing.arguments.context)context •[ContextualPricingContext!](/docs/api/admin-graphql/latest/input-objects/ContextualPricingContext) required
    :   The context used to generate contextual pricing for the variant.

        Show input fields

    ---

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the variant was created.

[Anchor to defaultCursor](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.defaultCursor)defaultCursor •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   A default [cursor](https://shopify.dev/api/usage/pagination-graphql) that returns the single next record, sorted ascending by ID.

[Anchor to deliveryProfile](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.deliveryProfile)deliveryProfile •[DeliveryProfile](/docs/api/admin-graphql/latest/objects/DeliveryProfile)
:   The [delivery profile](https://shopify.dev/api/admin-graphql/latest/objects/DeliveryProfile) for the variant.

    Show fields

[Anchor to displayName](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.displayName)displayName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   Display name of the variant, based on product's title + variant's title.

[Anchor to events](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events)events •[EventConnection!](/docs/api/admin-graphql/latest/connections/EventConnection) non-null
:   The paginated list of events associated with the host subject.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.sortKey)sortKey •[EventSortKeys](/docs/api/admin-graphql/latest/enums/EventSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.events.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-action) action •string
        :   The action that occured.

        Example:

        * `action:create`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-comments) comments •boolean
        :   Whether or not to include [comment-events](https://shopify.dev/api/admin-graphql/latest/objects/CommentEvent) in your search, passing `false` will exclude comment-events, any other value will include comment-events.

        Example:

        * `false`
        * `true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the event occurred. Event data is retained for 1 year.

        Example:

        * `created_at:>2025-10-21`
        * `created_at:<now`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-subject_type) subject\_type •string
        :   The resource type affected by this event. See [EventSubjectType](https://shopify.dev/api/admin-graphql/latest/enums/EventSubjectType) for possible values.

        Example:

        * `PRODUCT_VARIANT`
        * `PRODUCT`
        * `COLLECTION`

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to inventoryItem](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryItem)inventoryItem •[InventoryItem!](/docs/api/admin-graphql/latest/objects/InventoryItem) non-null
:   The inventory item, which is used to query for inventory information.

    Show fields

[Anchor to inventoryPolicy](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryPolicy)inventoryPolicy •[ProductVariantInventoryPolicy!](/docs/api/admin-graphql/latest/enums/ProductVariantInventoryPolicy) non-null
:   Whether customers are allowed to place an order for the product variant when it's out of stock.

    Show enum values

[Anchor to inventoryQuantity](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryQuantity)inventoryQuantity •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The total sellable quantity of the variant.

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to media](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media)media •[MediaConnection!](/docs/api/admin-graphql/latest/connections/MediaConnection) non-null
:   The media associated with the product variant.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.media.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to position](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.position)position •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-null
:   The order of the product variant in the list of product variants. The first position in the list is 1.

[Anchor to price](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.price)price •[Money!](/docs/api/admin-graphql/latest/scalars/Money) non-null
:   The price of the product variant in the default shop currency.

[Anchor to product](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.product)product •[Product!](/docs/api/admin-graphql/latest/objects/Product) non-null
:   The product that this variant belongs to.

    Show fields

[Anchor to productParents](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents)productParents •[ProductConnection!](/docs/api/admin-graphql/latest/connections/ProductConnection) non-null
:   A list of products that have product variants that contain this variant as a product component.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to query](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productParents.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-barcode) barcode •string
        :   Filter by the product variant [`barcode`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-barcode) field.

        Example:

        * `barcode:ABC-abc-1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-bundles) bundles •boolean
        :   Filter by a [product bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles). A product bundle is a set of two or more related products, which are commonly offered at a discount.

        Example:

        * `bundles:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-category_id) category\_id •string
        :   Filter by the product [category ID](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-category) (`product.category.id`). A product category is the category of a product from [Shopify's Standard Product Taxonomy](https://shopify.github.io/product-taxonomy/releases/unstable/?categoryId=sg-4-17-2-17).

        Example:

        * `category_id:sg-4-17-2-17`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-collection_id) collection\_id •id
        :   Filter by the collection [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Collection#field-id) field.

        Example:

        * `collection_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-combined_listing_role) combined\_listing\_role •string
        :   Filter by the role of the product in a [combined listing](https://shopify.dev/apps/build/product-merchandising/combined-listings).

        Valid values:

        * `parent`
        * `child`
        * `no_role`

        Example:

        * `combined_listing_role:parent`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the product was created.

        Example:

        * `created_at:>'2020-10-21T23:39:20Z'`
        * `created_at:<now`
        * `created_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-delivery_profile_id) delivery\_profile\_id •id
        :   Filter by the delivery profile [`id`](https://shopify.dev/api/admin-graphql/latest/objects/DeliveryProfile#field-id) field.

        Example:

        * `delivery_profile_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-error_feedback) error\_feedback •string
        :   Filter by products with publishing errors.

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-gift_card) gift\_card •boolean
        :   Filter by the product [`isGiftCard`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-isgiftcard) field.

        Example:

        * `gift_card:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-handle) handle •string
        :   Filter by a comma-separated list of product [handles](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-handle).

        Example:

        * `handle:the-minimal-snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-has_only_composites) has\_only\_composites •boolean
        :   Filter by products that have only composite variants.

        Example:

        * `has_only_composites:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-has_only_default_variant) has\_only\_default\_variant •boolean
        :   Filter by products that have only a default variant. A default variant is the only variant if no other variants are specified.

        Example:

        * `has_only_default_variant:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-has_variant_with_components) has\_variant\_with\_components •boolean
        :   Filter by products that have variants with associated components.

        Example:

        * `has_variant_with_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-inventory_total) inventory\_total •integer
        :   Filter by inventory count.

        Example:

        * `inventory_total:0`
        * `inventory_total:>150`
        * `inventory_total:>=200`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-is_price_reduced) is\_price\_reduced •boolean
        :   Filter by products that have a reduced price. For more information, refer to the [`CollectionRule`](https://shopify.dev/api/admin-graphql/latest/objects/CollectionRule) object.

        Example:

        * `is_price_reduced:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
        :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

        Example:

        * `metafields.custom.on_sale:true`
        * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-out_of_stock_somewhere) out\_of\_stock\_somewhere •boolean
        :   Filter by products that are out of stock in at least one location.

        Example:

        * `out_of_stock_somewhere:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-price) price •bigdecimal
        :   Filter by the product variant [`price`](https://shopify.dev/api/admin-graphql/latest/objects/Productvariant#field-price) field.

        Example:

        * `price:100.57`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_configuration_owner) product\_configuration\_owner •string
        :   Filter by the app [`id`](https://shopify.dev/api/admin-graphql/latest/objects/App#field-id) field.

        Example:

        * `product_configuration_owner:10001`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_publication_status) product\_publication\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_type) product\_type •string
        :   Filter by a comma-separated list of [product types](https://help.shopify.com/manual/products/details/product-type).

        Example:

        * `product_type:snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-publication_ids) publication\_ids •string
        :   Filter by a comma-separated list of publication IDs that are associated with the product.

        Example:

        * `publication_ids:184111530305,184111694145`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-published_at) published\_at •time
        :   Filter by the date and time when the product was published to the online store and other sales channels.

        Example:

        * `published_at:>2020-10-21T23:39:20Z`
        * `published_at:<now`
        * `published_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-published_status) published\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-status) status •string
        :   Filter by a comma-separated list of statuses. You can use statuses to manage inventory. Shopify only displays products with an `ACTIVE` status in online stores, sales channels, and apps.

        Valid values:

        * `active` Default
        * `archived`
        * `draft`

        Example:

        * `status:active,draft`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-title) title •string
        :   Filter by the product [`title`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-title) field.

        Example:

        * `title:The Minimal Snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the product was last updated.

        Example:

        * `updated_at:>'2020-10-21T23:39:20Z'`
        * `updated_at:<now`
        * `updated_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-variant_id) variant\_id •id
        :   Filter by the product variant [`id`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-id) field.

        Example:

        * `variant_id:45779434701121`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-variant_title) variant\_title •string
        :   Filter by the product variant [`title`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-title) field.

        Example:

        * `variant_title:'Special ski wax'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-vendor) vendor •string
        :   Filter by the origin or source of the product. Learn more about [vendors and managing vendor information](https://help.shopify.com/manual/products/managing-vendor-info).

        Example:

        * `vendor:Snowdevil`
        * `vendor:Snowdevil OR vendor:Icedevil`

    ---

[Anchor to productVariantComponents](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents)productVariantComponents •[ProductVariantComponentConnection!](/docs/api/admin-graphql/latest/connections/ProductVariantComponentConnection) non-null
:   A list of the product variant components.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.productVariantComponents.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to requiresComponents](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.requiresComponents)requiresComponents •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether a product variant requires components. The default value is `false`.
    If `true`, then the product variant can only be purchased as a parent bundle with components and it will be omitted
    from channels that don't support bundles.

[Anchor to selectedOptions](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.selectedOptions)selectedOptions •[[SelectedOption!]!](/docs/api/admin-graphql/latest/objects/SelectedOption) non-null
:   List of product options applied to the variant.

    Show fields

[Anchor to sellableOnlineQuantity](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellableOnlineQuantity)sellableOnlineQuantity •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-null
:   The total sellable quantity of the variant for online channels.
    This doesn't represent the total available inventory or capture
    [limitations based on customer location](https://help.shopify.com/manual/markets/inventory_and_fulfillment).

[Anchor to sellingPlanGroups](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups)sellingPlanGroups •[SellingPlanGroupConnection!](/docs/api/admin-graphql/latest/connections/SellingPlanGroupConnection) non-null
:   A list of all selling plan groups defined in the current shop associated with the product variant.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroups.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to sellingPlanGroupsCount](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroupsCount)sellingPlanGroupsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   Count of selling plan groups associated with the product variant.

    Show fields

[Anchor to showUnitPrice](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.showUnitPrice)showUnitPrice •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether to show the unit price for this product variant.

[Anchor to sku](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sku)sku •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A case-sensitive identifier for the product variant in the shop.
    Required in order to connect to a fulfillment service.

[Anchor to taxable](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.taxable)taxable •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether a tax is charged when the product variant is sold.

[Anchor to title](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.title)title •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The title of the product variant.

[Anchor to translations](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

[Anchor to unitPrice](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.unitPrice)unitPrice •[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)
:   The unit price value for the variant based on the variant measurement.

    Show fields

[Anchor to unitPriceMeasurement](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.unitPriceMeasurement)unitPriceMeasurement •[UnitPriceMeasurement](/docs/api/admin-graphql/latest/objects/UnitPriceMeasurement)
:   The unit price measurement for the variant.

    Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time (ISO 8601 format) when the product variant was last modified.

### Deprecated fields

* image (Image): deprecated
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated
* presentmentPrices (ProductVariantPricePairConnection!): deprecated
* sellingPlanGroupCount (Int!): deprecated
* storefrontId (StorefrontID!): deprecated
* taxCode (String): deprecated

[Anchor to image](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image)image •[Image](/docs/api/admin-graphql/latest/objects/Image) Deprecated
:   Show fields

    ### Arguments

    [Anchor to maxWidth](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image.arguments.maxWidth)maxWidth •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to maxHeight](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image.arguments.maxHeight)maxHeight •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to crop](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image.arguments.crop)crop •[CropRegion](/docs/api/admin-graphql/latest/enums/CropRegion) Deprecated
    :   Show enum values

    [Anchor to scale](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image.arguments.scale)scale •[Int](/docs/api/admin-graphql/latest/scalars/Int) DeprecatedDefault:1

    ---

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to presentmentPrices](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices)presentmentPrices •[ProductVariantPricePairConnection!](/docs/api/admin-graphql/latest/connections/ProductVariantPricePairConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to presentmentCurrencies](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.presentmentCurrencies)presentmentCurrencies •[[CurrencyCode!]](/docs/api/admin-graphql/latest/enums/CurrencyCode)
    :   The presentment currencies prices should return in.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.presentmentPrices.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to sellingPlanGroupCount](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanGroupCount)sellingPlanGroupCount •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-nullDeprecated

[Anchor to storefrontId](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.storefrontId)storefrontId •[StorefrontID!](/docs/api/admin-graphql/latest/scalars/StorefrontID) non-nullDeprecated

[Anchor to taxCode](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.taxCode)taxCode •[String](/docs/api/admin-graphql/latest/scalars/String) Deprecated

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/ProductVariant#queries)Queries

* productVariant (ProductVariant)
* productVariantByIdentifier (ProductVariant)
* productVariants (ProductVariantConnection!)

[Anchor to productVariant](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariant)[productVariant](/docs/api/admin-graphql/latest/queries/productVariant) •query
:   Retrieves a [product variant](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) by its ID.

    A product variant is a specific version of a
    [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) that comes in more than
    one [option](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption),
    such as size or color. For example, if a merchant sells t-shirts with options for size and color,
    then a small, blue t-shirt would be one product variant and a large, blue t-shirt would be another.

    Use the `productVariant` query when you need to:

    * Access essential product variant data (for example, title, price, image, and metafields).
    * Build product detail pages and manage inventory.
    * Handle international sales with localized pricing and content.
    * Manage product variants that are part of a bundle or selling plan.

    Learn more about working with [Shopify's product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/product-model-components).

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariant.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `ProductVariant` to return.

    ---

[Anchor to productVariantByIdentifier](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariantByIdentifier)[productVariantByIdentifier](/docs/api/admin-graphql/latest/queries/productVariantByIdentifier) •query
:   Return a product variant by an identifier.

    Show fields

    ### Arguments

    [Anchor to identifier](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariantByIdentifier.arguments.identifier)identifier •[ProductVariantIdentifierInput!](/docs/api/admin-graphql/latest/input-objects/ProductVariantIdentifierInput) required
    :   The identifier of the product variant.

        Show input fields

    ---

[Anchor to productVariants](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants)[productVariants](/docs/api/admin-graphql/latest/queries/productVariants) •query
:   Retrieves a list of [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant)
    associated with a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product).

    A product variant is a specific version of a product that comes in more than
    one [option](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption),
    such as size or color. For example, if a merchant sells t-shirts with options for size and color,
    then a small, blue t-shirt would be one product variant and a large, blue t-shirt would be another.

    Use the `productVariants` query when you need to:

    * Search for product variants by attributes such as SKU, barcode, or inventory quantity.
    * Filter product variants by attributes, such as whether they're gift cards or have custom metafields.
    * Fetch product variants for bulk operations, such as updating prices or inventory.
    * Preload data for product variants, such as inventory items, selected options, or associated products.

    The `productVariants` query supports [pagination](https://shopify.dev/docs/api/usage/pagination-graphql)
    to handle large product catalogs and [saved searches](https://shopify.dev/docs/api/admin-graphql/latest/queries/productVariants#arguments-savedSearchId)
    for frequently used product variant queries.

    The `productVariants` query returns product variants with their associated metadata, including:

    * Basic product variant information (for example, title, SKU, barcode, price, and inventory)
    * Media attachments (for example, images and videos)
    * Associated products, selling plans, bundles, and metafields

    Learn more about working with [Shopify's product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/product-model-components).

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.sortKey)sortKey •[ProductVariantSortKeys](/docs/api/admin-graphql/latest/enums/ProductVariantSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-barcode) barcode •string
        :   Filter by the product variant [`barcode`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-barcode) field.

        Example:

        * `barcode:ABC-abc-123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-collection) collection •string
        :   Filter by the [ID of the collection](https://shopify.dev/api/admin-graphql/latest/objects/Collection#field-id) that the product variant belongs to.

        Example:

        * `collection:465903092033`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-delivery_profile_id) delivery\_profile\_id •id
        :   Filter by the product variant [delivery profile ID](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-deliveryprofile) (`ProductVariant.deliveryProfile.id`).

        Example:

        * `delivery_profile_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-exclude_composite) exclude\_composite •boolean
        :   Filter by product variants that aren't composites.

        Example:

        * `exclude_composite:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-exclude_variants_with_components) exclude\_variants\_with\_components •boolean
        :   Filter by whether there are [components](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-product-fixed-bundle) that are associated with the product variants in a bundle.

        Example:

        * `exclude_variants_with_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-gift_card) gift\_card •boolean
        :   Filter by the product [`isGiftCard`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-isgiftcard) field.

        Example:

        * `gift_card:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-inventory_quantity) inventory\_quantity •integer
        :   Filter by an aggregate of inventory across all locations where the product variant is stocked.

        Example:

        * `inventory_quantity:10`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-location_id) location\_id •id
        :   Filter by the [location ID](https://shopify.dev/api/admin-graphql/latest/objects/Location#field-id) for the product variant.

        Example:

        * `location_id:88511152449`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-managed) managed •boolean
        :   Filter by whether there is fulfillment service tracking associated with the product variants.

        Example:

        * `managed:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-managed_by) managed\_by •string
        :   Filter by the fulfillment service that tracks the number of items in stock for the product variant.

        Example:

        * `managed_by:shopify`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-option1) option1 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option1:small`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-option2) option2 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option2:medium`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-option3) option3 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option3:large`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_id) product\_id •id
        :   Filter by the product [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-id) field.

        Example:

        * `product_id:8474977763649`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_ids) product\_ids •string
        :   Filter by a comma-separated list of product [IDs](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-id).

        Example:

        * `product_ids:8474977763649,8474977796417`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_publication_status) product\_publication\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_status) product\_status •string
        :   Filter by a comma-separated list of product [statuses](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-status).

        Example:

        * `product_status:ACTIVE,DRAFT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-product_type) product\_type •string
        :   Filter by the product type that's associated with the product variants.

        Example:

        * `product_type:snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-published_status) published\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-requires_components) requires\_components •boolean
        :   Filter by whether the product variant can only be purchased with components. [Learn more](https://shopify.dev/apps/build/product-merchandising/bundles#store-eligibility).

        Example:

        * `requires_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-taxable) taxable •boolean
        :   Filter by the product variant [`taxable`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-taxable) field.

        Example:

        * `taxable:false`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-title) title •string
        :   Filter by the product variant [`title`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-title) field.

        Example:

        * `title:ice`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-updated_at) updated\_at •time
        :   Filter by date and time when the product variant was updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/ProductVariant#argument-query-filter-vendor) vendor •string
        :   Filter by the origin or source of the product variant. Learn more about [vendors and managing vendor information](https://help.shopify.com/manual/products/managing-vendor-info).

        Example:

        * `vendor:Snowdevil`
        * `vendor:Snowdevil OR vendor:Icedevil`

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/ProductVariant#query-productVariants.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/ProductVariant#mutations)Mutations

* productVariantAppendMedia (ProductVariantAppendMediaPayload)
* productVariantDetachMedia (ProductVariantDetachMediaPayload)
* productVariantJoinSellingPlanGroups (ProductVariantJoinSellingPlanGroupsPayload)
* productVariantLeaveSellingPlanGroups (ProductVariantLeaveSellingPlanGroupsPayload)
* productVariantRelationshipBulkUpdate (ProductVariantRelationshipBulkUpdatePayload)
* productVariantsBulkCreate (ProductVariantsBulkCreatePayload)
* productVariantsBulkUpdate (ProductVariantsBulkUpdatePayload)
* quantityPricingByVariantUpdate (QuantityPricingByVariantUpdatePayload)

[Anchor to productVariantAppendMedia](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantAppendMedia)[productVariantAppendMedia](/docs/api/admin-graphql/latest/mutations/productVariantAppendMedia) •mutation
:   Appends existing media from a product to specific variants of that product, creating associations between media files and particular product options. This allows different variants to showcase relevant images or videos.

    For example, a t-shirt product might have color variants where each color variant displays only the images showing that specific color, helping customers see exactly what they're purchasing.

    Use `ProductVariantAppendMedia` to:

    * Associate specific images with product variants for accurate display
    * Build variant-specific media management in product interfaces
    * Implement automated media assignment based on variant attributes

    The operation links existing product media to variants without duplicating files, maintaining efficient media storage while enabling variant-specific displays.

    Learn more about [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant).

    Show payload

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantAppendMedia.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   Specifies the product associated to the media.

    [Anchor to variantMedia](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantAppendMedia.arguments.variantMedia)variantMedia •[[ProductVariantAppendMediaInput!]!](/docs/api/admin-graphql/latest/input-objects/ProductVariantAppendMediaInput) required
    :   A list of pairs of variants and media to be attached to the variants.

        Show input fields

    ---

[Anchor to productVariantDetachMedia](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantDetachMedia)[productVariantDetachMedia](/docs/api/admin-graphql/latest/mutations/productVariantDetachMedia) •mutation
:   Detaches media from product variants.

    Show payload

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantDetachMedia.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   Specifies the product to which the variants and media are associated.

    [Anchor to variantMedia](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantDetachMedia.arguments.variantMedia)variantMedia •[[ProductVariantDetachMediaInput!]!](/docs/api/admin-graphql/latest/input-objects/ProductVariantDetachMediaInput) required
    :   A list of pairs of variants and media to be deleted from the variants.

        Show input fields

    ---

[Anchor to productVariantJoinSellingPlanGroups](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantJoinSellingPlanGroups)[productVariantJoinSellingPlanGroups](/docs/api/admin-graphql/latest/mutations/productVariantJoinSellingPlanGroups) •mutation
:   Adds multiple selling plan groups to a product variant.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantJoinSellingPlanGroups.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product variant.

    [Anchor to sellingPlanGroupIds](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantJoinSellingPlanGroups.arguments.sellingPlanGroupIds)sellingPlanGroupIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The IDs of the selling plan groups to add.

    ---

[Anchor to productVariantLeaveSellingPlanGroups](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantLeaveSellingPlanGroups)[productVariantLeaveSellingPlanGroups](/docs/api/admin-graphql/latest/mutations/productVariantLeaveSellingPlanGroups) •mutation
:   Remove multiple groups from a product variant.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantLeaveSellingPlanGroups.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product variant.

    [Anchor to sellingPlanGroupIds](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantLeaveSellingPlanGroups.arguments.sellingPlanGroupIds)sellingPlanGroupIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The IDs of the selling plan groups to leave.

    ---

[Anchor to productVariantRelationshipBulkUpdate](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantRelationshipBulkUpdate)[productVariantRelationshipBulkUpdate](/docs/api/admin-graphql/latest/mutations/productVariantRelationshipBulkUpdate) •mutation
:   Creates new bundles, updates component quantities in existing bundles, and removes bundle components for one or multiple [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects.

    Each bundle variant can contain up to 30 component variants with specified quantities. After an app assigns components to a bundle, only that app can manage those components.

    ---

    Note

    For most use cases, use [`productBundleCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productBundleCreate) instead, which creates product fixed bundles. `productVariantRelationshipBulkUpdate` is for [variant fixed bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-variant-fixed-bundle), where each variant has its own component configuration.

    **Note:**

    For most use cases, use [`productBundleCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productBundleCreate) instead, which creates product fixed bundles. `productVariantRelationshipBulkUpdate` is for [variant fixed bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-variant-fixed-bundle), where each variant has its own component configuration.

    **Note:** For most use cases, use <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/productBundleCreate"><code><span class="PreventFireFoxApplyingGapToWBR">product<wbr/>Bundle<wbr/>Create</span></code></a> instead, which creates product fixed bundles. <code><span class="PreventFireFoxApplyingGapToWBR">product<wbr/>Variant<wbr/>Relationship<wbr/>Bulk<wbr/>Update</span></code> is for <a href="https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-variant-fixed-bundle">variant fixed bundles</a>, where each variant has its own component configuration.

    ---

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantRelationshipBulkUpdate.arguments.input)input •[[ProductVariantRelationshipUpdateInput!]!](/docs/api/admin-graphql/latest/input-objects/ProductVariantRelationshipUpdateInput) required
    :   The input options for the product variant being updated.

        Show input fields

    ---

[Anchor to productVariantsBulkCreate](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkCreate)[productVariantsBulkCreate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkCreate) •mutation
:   Creates multiple [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant)
    for a single [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) in one operation.
    You can run this mutation directly or as part of a [bulk operation](https://shopify.dev/docs/api/usage/bulk-operations/imports)
    for large-scale catalog updates.

    Use the `productVariantsBulkCreate` mutation to efficiently add new product variants—such as different sizes,
    colors, or materials—to an existing product. The mutation is helpful if you need to add product variants in bulk,
    such as importing from an external system.

    The mutation supports:

    * Creating variants with custom option values
    * Associating media (for example, images, videos, and 3D models) with the product or its variants
    * Handling complex product configurations

    ---

    Note

    By default, stores have a limit of 2048 product variants for each product.

    **Note:**

    By default, stores have a limit of 2048 product variants for each product.

    **Note:** By default, stores have a limit of 2048 product variants for each product.

    ---

    After creating variants, you can make additional changes using one of the following mutations:

    * [`productVariantsBulkUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate):
      Updates multiple product variants for a single product in one operation.
    * [`productSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet):
      Used to perform multiple operations on products, such as creating or modifying product options and variants.

    You can also specifically manage product options through related mutations:

    * [`productOptionsCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsCreate)
    * [`productOptionUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionUpdate)
    * [`productOptionsReorder`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsReorder)
    * [`productOptionsDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsDelete)

    Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model)
    and [adding product data](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/add-data).

    Show payload

    ### Arguments

    [Anchor to variants](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkCreate.arguments.variants)variants •[[ProductVariantsBulkInput!]!](/docs/api/admin-graphql/latest/input-objects/ProductVariantsBulkInput) required
    :   An array of product variants to be created.

        Show input fields

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkCreate.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product on which to create the variants.

    [Anchor to media](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkCreate.arguments.media)media •[[CreateMediaInput!]](/docs/api/admin-graphql/latest/input-objects/CreateMediaInput)
    :   List of new media to be added to the product.

        Show input fields

    [Anchor to strategy](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkCreate.arguments.strategy)strategy •[ProductVariantsBulkCreateStrategy](/docs/api/admin-graphql/latest/enums/ProductVariantsBulkCreateStrategy) Default:DEFAULT
    :   The strategy defines which behavior the mutation should observe, such as whether to keep or delete the standalone variant (when product has only a single or default variant) when creating new variants in bulk.

        Show enum values

    ---

[Anchor to productVariantsBulkUpdate](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkUpdate)[productVariantsBulkUpdate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate) •mutation
:   Updates multiple [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant)
    for a single [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) in one operation.
    You can run this mutation directly or as part of a [bulk operation](https://shopify.dev/docs/api/usage/bulk-operations/imports)
    for large-scale catalog updates.

    Use the `productVariantsBulkUpdate` mutation to efficiently modify product variants—such as different sizes,
    colors, or materials—associated with an existing product. The mutation is helpful if you need to update a
    product's variants in bulk, such as importing from an external system.

    The mutation supports:

    * Updating variants with custom option values
    * Associating media (for example, images, videos, and 3D models) with the product or its variants
    * Handling complex product configurations

    ---

    Note

    By default, stores have a limit of 2048 product variants for each product.

    **Note:**

    By default, stores have a limit of 2048 product variants for each product.

    **Note:** By default, stores have a limit of 2048 product variants for each product.

    ---

    After creating variants, you can make additional changes using the
    [`productSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet) mutation,
    which is used to perform multiple operations on products, such as creating or modifying product options and variants.

    You can also specifically manage product options through related mutations:

    * [`productOptionsCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsCreate)
    * [`productOptionUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionUpdate)
    * [`productOptionsReorder`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsReorder)
    * [`productOptionsDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsDelete)

    Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model)
    and [adding product data](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/add-data).

    Show payload

    ### Arguments

    [Anchor to variants](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkUpdate.arguments.variants)variants •[[ProductVariantsBulkInput!]!](/docs/api/admin-graphql/latest/input-objects/ProductVariantsBulkInput) required
    :   An array of product variants to update.

        Show input fields

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkUpdate.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product associated with the variants to update.

    [Anchor to media](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkUpdate.arguments.media)media •[[CreateMediaInput!]](/docs/api/admin-graphql/latest/input-objects/CreateMediaInput)
    :   List of new media to be added to the product.

        Show input fields

    [Anchor to allowPartialUpdates](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-productVariantsBulkUpdate.arguments.allowPartialUpdates)allowPartialUpdates •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   When partial updates are allowed, valid variant changes may be persisted even if some of
        the variants updated have invalid data and cannot be persisted.
        When partial updates are not allowed, any error will prevent all variants from updating.

    ---

[Anchor to quantityPricingByVariantUpdate](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-quantityPricingByVariantUpdate)[quantityPricingByVariantUpdate](/docs/api/admin-graphql/latest/mutations/quantityPricingByVariantUpdate) •mutation
:   Updates quantity pricing on a [`PriceList`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PriceList) for specific [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects. You can set fixed prices (see [`PriceListPrice`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PriceListPrice)), quantity rules, and quantity price breaks in a single operation.

    [`QuantityRule`](https://shopify.dev/docs/api/admin-graphql/latest/objects/QuantityRule) objects define minimum, maximum, and increment constraints for ordering. [`QuantityPriceBreak`](https://shopify.dev/docs/api/admin-graphql/latest/objects/QuantityPriceBreak) objects offer tiered pricing based on purchase volume.

    The mutation executes delete operations before create operations and doesn't allow partial updates.

    ---

    Note

    If any requested change fails, then the mutation doesn't apply any of the changes.

    **Note:**

    If any requested change fails, then the mutation doesn't apply any of the changes.

    **Note:** If any requested change fails, then the mutation doesn&#39;t apply any of the changes.

    ---

    Show payload

    ### Arguments

    [Anchor to priceListId](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-quantityPricingByVariantUpdate.arguments.priceListId)priceListId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the price list for which quantity pricing will be updated.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/ProductVariant#mutation-quantityPricingByVariantUpdate.arguments.input)input •[QuantityPricingByVariantUpdateInput!](/docs/api/admin-graphql/latest/input-objects/QuantityPricingByVariantUpdateInput) required
    :   The input data used to update the quantity pricing in the price list.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/ProductVariant#interfaces)Interfaces

* HasEvents
* HasMetafieldDefinitions
* HasMetafields
* HasPublishedTranslations
* LegacyInteroperability
* Navigable
* Node

[Anchor to HasEvents](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents) •interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

[Anchor to LegacyInteroperability](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability) •interface

[Anchor to Navigable](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-Navigable)[Navigable](/docs/api/admin-graphql/latest/interfaces/Navigable) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/ProductVariant#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo