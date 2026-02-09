---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/collections
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Retrieves a list of [collections](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection)
in a store. Collections are groups of [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
that merchants can organize for display in their [online store](https://shopify.dev/docs/apps/build/online-store) and
other [sales channels](https://shopify.dev/docs/apps/build/sales-channels).
For example, an athletics store might create different collections for running attire, shoes, and accessories.

Use the `collections` query when you need to:

* Build a browsing interface for a store's product groupings.
* Create collection searching, sorting, and filtering experiences (for example, by title, type, or published status).
* Sync collection data with external systems.
* Manage both custom ([manual](https://help.shopify.com/manual/products/collections/manual-shopify-collection))
  and smart ([automated](https://help.shopify.com/manual/products/collections/automated-collections)) collections.

The `collections` query supports [pagination](https://shopify.dev/docs/api/usage/pagination-graphql)
for large catalogs and [saved searches](https://shopify.dev/docs/api/admin-graphql/latest/queries/collections#arguments-savedSearchId)
for frequently used collection queries.

The `collections` query returns collections with their associated metadata, including:

* Basic collection information (title, description, handle, and type)
* Collection image and SEO metadata
* Product count and product relationships
* Collection rules (for smart collections)
* Publishing status and publication details
* Metafields and custom attributes

Learn more about [using metafields with smart collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* savedSearchId (ID)
* sortKey (CollectionSortKeys)

[Anchor to after](/docs/api/admin-graphql/latest/queries/collections#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/collections#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/collections#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/collections#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/collections#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-default) default •string
    :   Filter by a case-insensitive search of multiple fields in a document.

    Example:

    * `query=Bob Norman`
    * `query=title:green hoodie`

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-collection_type) collection\_type •string


    Valid values:

    * `custom`
    * `smart`

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-handle) handle •string

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-product_id) product\_id •id
    :   Filter by collections containing a product by its ID.

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-product_publication_status) product\_publication\_status •string
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

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-publishable_status) publishable\_status •string
    :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

    Valid values:

    * `* {channel_app_id}-unset`
    * `* {channel_app_id}-pending`
    * `* {channel_app_id}-approved`
    * `* {channel_app_id}-not_approved`

    Example:

    * `publishable_status:580111-unset`
    * `publishable_status:580111-pending`

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-published_at) published\_at •time
    :   Filter by the date and time when the collection was published to the Online Store.

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-published_status) published\_status •string
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

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-title) title •string

    [Anchor to](/docs/api/admin-graphql/latest/queries/collections#argument-query-filter-updated_at) updated\_at •time

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/collections#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to savedSearchId](/docs/api/admin-graphql/latest/queries/collections#arguments-savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
    The search’s query string is used as the query argument.

[Anchor to sortKey](/docs/api/admin-graphql/latest/queries/collections#arguments-sortKey)sortKey •[CollectionSortKeys](/docs/api/admin-graphql/latest/enums/CollectionSortKeys) Default:ID
:   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/collections#possible-returns)Possible returns

* edges ([CollectionEdge!]!)
* nodes ([Collection!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/collections#returns-edges)edges •[[CollectionEdge!]!](/docs/api/admin-graphql/latest/objects/CollectionEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/collections#returns-nodes)nodes •[[Collection!]!](/docs/api/admin-graphql/latest/objects/Collection) non-null
:   A list of nodes that are contained in CollectionEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/collections#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo