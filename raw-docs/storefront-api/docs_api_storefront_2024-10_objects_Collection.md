---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Collection
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_read_product_listings` access scope.

A collection represents a grouping of products that a shop owner can create to
organize them or make their shops easier to browse.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Collection#fields)Fields

* description (String!)
* descriptionHtml (HTML!)
* handle (String!)
* id (ID!)
* image (Image)
* metafield (Metafield)
* metafields ([Metafield]!)
* onlineStoreUrl (URL)
* products (ProductConnection!)
* seo (SEO!)
* title (String!)
* trackingParameters (String)
* updatedAt (DateTime!)

[Anchor to description](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.description)description •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   Stripped description of the collection, single line with HTML tags removed.

    Show arguments

    ### Arguments

    [Anchor to truncateAt](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.description.arguments.truncateAt)truncateAt •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Truncates a string after the given length.

    ---

[Anchor to descriptionHtml](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.descriptionHtml)descriptionHtml •[HTML!](/docs/api/storefront/latest/scalars/HTML) non-null
:   The description of the collection, complete with HTML formatting.

[Anchor to handle](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.handle)handle •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   A human-friendly unique string for the collection automatically generated from its title.
    Limit of 255 characters.

[Anchor to id](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to image](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.image)image •[Image](/docs/api/storefront/latest/objects/Image)
:   Image associated with the collection.

    Show fields

[Anchor to metafield](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to onlineStoreUrl](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.onlineStoreUrl)onlineStoreUrl •[URL](/docs/api/storefront/latest/scalars/URL)
:   The URL used for viewing the resource on the shop's Online Store. Returns `null` if the resource is currently not published to the Online Store sales channel.

[Anchor to products](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products)products •[ProductConnection!](/docs/api/storefront/latest/connections/ProductConnection) non-null
:   List of products in the collection.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.sortKey)sortKey •[ProductCollectionSortKeys](/docs/api/storefront/latest/enums/ProductCollectionSortKeys) Default:COLLECTION\_DEFAULT
    :   Sort the underlying list by the given key.

        Show enum values

    [Anchor to filters](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.products.arguments.filters)filters •[[ProductFilter!]](/docs/api/storefront/latest/input-objects/ProductFilter)
    :   Returns a subset of products matching all product filters.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to seo](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.seo)seo •[SEO!](/docs/api/storefront/latest/objects/SEO) non-null
:   The collection's SEO information.

    Show fields

[Anchor to title](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.title)title •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   The collection’s name. Limit of 255 characters.

[Anchor to trackingParameters](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.trackingParameters)trackingParameters •[String](/docs/api/storefront/latest/scalars/String)
:   URL parameters to be added to a page URL to track the origin of on-site search traffic for [analytics reporting](https://help.shopify.com/manual/reports-and-analytics/shopify-reports/report-types/default-reports/behaviour-reports). Returns a result when accessed through the [search](/docs/api/storefront/2026-01/queries/search) or [predictiveSearch](/docs/api/storefront/2026-01/queries/predictiveSearch) queries, otherwise returns null.

[Anchor to updatedAt](/docs/api/storefront/latest/objects/Collection#field-Collection.fields.updatedAt)updatedAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null
:   The date and time when the collection was last modified.

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/storefront/latest/objects/Collection#queries)Queries

* collection (Collection)
* collections (CollectionConnection!)
* collectionByHandle (Collection): deprecated

[Anchor to collection](/docs/api/storefront/latest/objects/Collection#query-collection)[collection](/docs/api/storefront/latest/queries/collection) •query
:   Fetch a specific `Collection` by one of its unique attributes.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/storefront/latest/objects/Collection#query-collection.arguments.id)id •[ID](/docs/api/storefront/latest/scalars/ID)
    :   The ID of the `Collection`.

    [Anchor to handle](/docs/api/storefront/latest/objects/Collection#query-collection.arguments.handle)handle •[String](/docs/api/storefront/latest/scalars/String)
    :   The handle of the `Collection`.

    ---

[Anchor to collections](/docs/api/storefront/latest/objects/Collection#query-collections)[collections](/docs/api/storefront/latest/queries/collections) •query
:   List of the shop’s collections.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.sortKey)sortKey •[CollectionSortKeys](/docs/api/storefront/latest/enums/CollectionSortKeys) Default:ID
    :   Sort the underlying list by the given key.

        Show enum values

    [Anchor to query](/docs/api/storefront/latest/objects/Collection#query-collections.arguments.query)query •[String](/docs/api/storefront/latest/scalars/String)
    :   Apply one or multiple filters to the query.
        Refer to the detailed [search syntax](https://shopify.dev/api/usage/search-syntax) for more information about using filters.

        Show filters

        [Anchor to](/docs/api/storefront/latest/objects/Collection#argument-query-filter-collection_type) collection\_type •

        [Anchor to](/docs/api/storefront/latest/objects/Collection#argument-query-filter-title) title •

        [Anchor to](/docs/api/storefront/latest/objects/Collection#argument-query-filter-updated_at) updated\_at •

    ---

[Anchor to collectionByHandle](/docs/api/storefront/latest/objects/Collection#query-collectionByHandle)[collectionByHandle](/docs/api/storefront/latest/queries/collectionByHandle) •query Deprecated
:   Show fields

    ### Arguments

    [Anchor to handle](/docs/api/storefront/latest/objects/Collection#query-collectionByHandle.arguments.handle)handle •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The handle of the collection.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/Collection#interfaces)Interfaces

* HasMetafields
* Node
* OnlineStorePublishable
* Trackable

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/Collection#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/storefront/latest/objects/Collection#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

[Anchor to OnlineStorePublishable](/docs/api/storefront/latest/objects/Collection#interface-OnlineStorePublishable)[OnlineStorePublishable](/docs/api/storefront/latest/interfaces/OnlineStorePublishable) •interface

[Anchor to Trackable](/docs/api/storefront/latest/objects/Collection#interface-Trackable)[Trackable](/docs/api/storefront/latest/interfaces/Trackable) •interface

---

Was this section helpful?

YesNo