---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Collection
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_products` access scope.

The `Collection` object represents a group of [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
that merchants can organize to make their stores easier to browse and help customers find related products.
Collections serve as the primary way to categorize and display products across
[online stores](https://shopify.dev/docs/apps/build/online-store),
[sales channels](https://shopify.dev/docs/apps/build/sales-channels), and marketing campaigns.

There are two types of collections:

* **[Custom (manual) collections](https://help.shopify.com/manual/products/collections/manual-shopify-collection)**: You specify the products to include in a collection.
* **[Smart (automated) collections](https://help.shopify.com/manual/products/collections/automated-collections)**: You define rules, and products matching those rules are automatically included in the collection.

The `Collection` object provides information to:

* Organize products by category, season, or promotion.
* Automate product grouping using rules (for example, by tag, type, or price).
* Configure product sorting and display order (for example, alphabetical, best-selling, price, or manual).
* Manage collection visibility and publication across sales channels.
* Add rich descriptions, images, and metadata to enhance discovery.

---

Note

Collections are unpublished by default. To make them available to customers,
use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
mutation after creation.

**Note:**

Collections are unpublished by default. To make them available to customers,
use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
mutation after creation.

**Note:** Collections are unpublished by default. To make them available to customers,
use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish"><code><span class="PreventFireFoxApplyingGapToWBR">publishable<wbr/>Publish</span></code></a>
mutation after creation.

---

Collections can be displayed in a store with Shopify's theme system through [Liquid templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
and can be customized with [template suffixes](https://shopify.dev/docs/storefronts/themes/architecture/templates/alternate-templates)
for unique layouts. They also support advanced features like translated content, resource feedback,
and contextual publication for location-based catalogs.

Learn about [using metafields with smart collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Collection#fields)Fields

* activeOperations (CollectionOperations!)
* availablePublicationsCount (Count)
* description (String!)
* descriptionHtml (HTML!)
* events (EventConnection!)
* feedback (ResourceFeedback)
* handle (String!)
* hasProduct (Boolean!)
* id (ID!)
* image (Image)
* legacyResourceId (UnsignedInt64!)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* products (ProductConnection!)
* productsCount (Count)
* publishedOnCurrentPublication (Boolean!)
* publishedOnPublication (Boolean!)
* resourcePublications (ResourcePublicationConnection!)
* resourcePublicationsCount (Count)
* resourcePublicationsV2 (ResourcePublicationV2Connection!)
* ruleSet (CollectionRuleSet)
* seo (SEO!)
* sortOrder (CollectionSortOrder!)
* templateSuffix (String)
* title (String!)
* translations ([Translation!]!)
* unpublishedPublications (PublicationConnection!)
* updatedAt (DateTime!)

[Anchor to activeOperations](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.activeOperations)activeOperations •[CollectionOperations!](/docs/api/admin-graphql/latest/objects/CollectionOperations) non-null
:   Collection duplicate operations involving this collection, either as a source (copying products from this collection to another) or a target (copying products to this collection from another).

    Show fields

[Anchor to availablePublicationsCount](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.availablePublicationsCount)availablePublicationsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   The number of
    [publications](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication)
    that a resource is published to, without
    [feedback errors](https://shopify.dev/docs/api/admin-graphql/latest/objects/ResourceFeedback).

    Show fields

[Anchor to description](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.description)description •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   A single-line, text-only description of the collection, stripped of any HTML tags and formatting that were included in the description.

    Show arguments

    ### Arguments

    [Anchor to truncateAt](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.description.arguments.truncateAt)truncateAt •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   Truncates a string after the given length.

    ---

[Anchor to descriptionHtml](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.descriptionHtml)descriptionHtml •[HTML!](/docs/api/admin-graphql/latest/scalars/HTML) non-null
:   The description of the collection, including any HTML tags and formatting. This content is typically displayed to customers, such as on an online store, depending on the theme.

[Anchor to events](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events)events •[EventConnection!](/docs/api/admin-graphql/latest/connections/EventConnection) non-null
:   The paginated list of events associated with the host subject.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.sortKey)sortKey •[EventSortKeys](/docs/api/admin-graphql/latest/enums/EventSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.events.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-action) action •string
        :   The action that occured.

        Example:

        * `action:create`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-comments) comments •boolean
        :   Whether or not to include [comment-events](https://shopify.dev/api/admin-graphql/latest/objects/CommentEvent) in your search, passing `false` will exclude comment-events, any other value will include comment-events.

        Example:

        * `false`
        * `true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the event occurred. Event data is retained for 1 year.

        Example:

        * `created_at:>2025-10-21`
        * `created_at:<now`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-subject_type) subject\_type •string
        :   The resource type affected by this event. See [EventSubjectType](https://shopify.dev/api/admin-graphql/latest/enums/EventSubjectType) for possible values.

        Example:

        * `PRODUCT_VARIANT`
        * `PRODUCT`
        * `COLLECTION`

    ---

[Anchor to feedback](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.feedback)feedback •[ResourceFeedback](/docs/api/admin-graphql/latest/objects/ResourceFeedback)
:   Information about the collection that's provided through resource feedback.

    Show fields

[Anchor to handle](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.handle)handle •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   A unique string that identifies the collection. If a handle isn't specified when a collection is created, it's automatically generated from the collection's original title, and typically includes words from the title separated by hyphens. For example, a collection that was created with the title `Summer Catalog 2022` might have the handle `summer-catalog-2022`.

    If the title is changed, the handle doesn't automatically change.

    The handle can be used in themes by the Liquid templating language to refer to the collection, but using the ID is preferred because it never changes.

[Anchor to hasProduct](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.hasProduct)hasProduct •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the collection includes the specified product.

    Show arguments

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.hasProduct.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product to check.

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image)image •[Image](/docs/api/admin-graphql/latest/objects/Image)
:   The image associated with the collection.

    Show fields

    ### Arguments

    [Anchor to maxWidth](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image.arguments.maxWidth)maxWidth •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to maxHeight](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image.arguments.maxHeight)maxHeight •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to crop](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image.arguments.crop)crop •[CropRegion](/docs/api/admin-graphql/latest/enums/CropRegion) Deprecated
    :   Show enum values

    [Anchor to scale](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image.arguments.scale)scale •[Int](/docs/api/admin-graphql/latest/scalars/Int) DeprecatedDefault:1

    ---

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to products](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products)products •[ProductConnection!](/docs/api/admin-graphql/latest/connections/ProductConnection) non-null
:   The products that are included in the collection.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.products.arguments.sortKey)sortKey •[ProductCollectionSortKeys](/docs/api/admin-graphql/latest/enums/ProductCollectionSortKeys) Default:COLLECTION\_DEFAULT
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    ---

[Anchor to productsCount](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.productsCount)productsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   The number of products in the collection.

    Show fields

[Anchor to publishedOnCurrentPublication](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnCurrentPublication)publishedOnCurrentPublication •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the resource is published to the app's
    [publication](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication).
    For example, the resource might be published to the app's online store channel.

[Anchor to publishedOnPublication](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnPublication)publishedOnPublication •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the resource is published to a specified
    [publication](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication).

    Show arguments

    ### Arguments

    [Anchor to publicationId](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnPublication.arguments.publicationId)publicationId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the publication to check. For example, `id: "gid://shopify/Publication/123"`.

    ---

[Anchor to resourcePublications](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications)resourcePublications •[ResourcePublicationConnection!](/docs/api/admin-graphql/latest/connections/ResourcePublicationConnection) non-null
:   The list of resources that are published to a
    [publication](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication).

    Show fields

    ### Arguments

    [Anchor to onlyPublished](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.onlyPublished)onlyPublished •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Whether to return only the resources that are currently published. If false, then also returns the resources that are scheduled to be published.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublications.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to resourcePublicationsCount](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsCount)resourcePublicationsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   The number of
    [publications](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication)
    that a resource is published to, without
    [feedback errors](https://shopify.dev/docs/api/admin-graphql/latest/objects/ResourceFeedback).

    Show fields

    ### Arguments

    [Anchor to onlyPublished](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsCount.arguments.onlyPublished)onlyPublished •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Include only the resource's publications that are published. If false, then return all the resource's publications including future publications.

    ---

[Anchor to resourcePublicationsV2](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2)resourcePublicationsV2 •[ResourcePublicationV2Connection!](/docs/api/admin-graphql/latest/connections/ResourcePublicationV2Connection) non-null
:   The list of resources that are either published or staged to be published to a
    [publication](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication).

    Show fields

    ### Arguments

    [Anchor to onlyPublished](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.onlyPublished)onlyPublished •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Whether to return only the resources that are currently published. If false, then also returns the resources that are scheduled or staged to be published.

    [Anchor to catalogType](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.catalogType)catalogType •[CatalogType](/docs/api/admin-graphql/latest/enums/CatalogType)
    :   Filter publications by catalog type.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.resourcePublicationsV2.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to ruleSet](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.ruleSet)ruleSet •[CollectionRuleSet](/docs/api/admin-graphql/latest/objects/CollectionRuleSet)
:   For a smart (automated) collection, specifies the rules that determine whether a product is included.

    Show fields

[Anchor to seo](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.seo)seo •[SEO!](/docs/api/admin-graphql/latest/objects/SEO) non-null
:   If the default SEO fields for page title and description have been modified, contains the modified information.

    Show fields

[Anchor to sortOrder](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.sortOrder)sortOrder •[CollectionSortOrder!](/docs/api/admin-graphql/latest/enums/CollectionSortOrder) non-null
:   The order in which the products in the collection are displayed by default in the Shopify admin and in sales channels, such as an online store.

    Show enum values

[Anchor to templateSuffix](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.templateSuffix)templateSuffix •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The suffix of the Liquid template being used to show the collection in an online store. For example, if the value is `custom`, then the collection is using the `collection.custom.liquid` template. If the value is `null`, then the collection is using the default `collection.liquid` template.

[Anchor to title](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.title)title •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The name of the collection. It's displayed in the Shopify admin and is typically displayed in sales channels, such as an online store.

[Anchor to translations](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

[Anchor to unpublishedPublications](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications)unpublishedPublications •[PublicationConnection!](/docs/api/admin-graphql/latest/connections/PublicationConnection) non-null
:   The list of [publications](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication)
    that the resource isn't published to.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedPublications.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) when the collection was last modified.

### Deprecated fields

* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated
* publicationCount (Int!): deprecated
* publications (CollectionPublicationConnection!): deprecated
* publishedOnChannel (Boolean!): deprecated
* publishedOnCurrentChannel (Boolean!): deprecated
* storefrontId (StorefrontID!): deprecated
* unpublishedChannels (ChannelConnection!): deprecated

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to publicationCount](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publicationCount)publicationCount •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-nullDeprecated
:   Show arguments

    ### Arguments

    [Anchor to onlyPublished](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publicationCount.arguments.onlyPublished)onlyPublished •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Include only the resource's publications that are published. If false, then return all the resource's publications including future publications.

    ---

[Anchor to publications](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications)publications •[CollectionPublicationConnection!](/docs/api/admin-graphql/latest/connections/CollectionPublicationConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to onlyPublished](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.onlyPublished)onlyPublished •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Whether or not to return only the collection publications that are published.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publications.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to publishedOnChannel](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnChannel)publishedOnChannel •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-nullDeprecated
:   Show arguments

    ### Arguments

    [Anchor to channelId](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnChannel.arguments.channelId)channelId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the channel to check.

    ---

[Anchor to publishedOnCurrentChannel](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.publishedOnCurrentChannel)publishedOnCurrentChannel •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-nullDeprecated

[Anchor to storefrontId](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.storefrontId)storefrontId •[StorefrontID!](/docs/api/admin-graphql/latest/scalars/StorefrontID) non-nullDeprecated

[Anchor to unpublishedChannels](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels)unpublishedChannels •[ChannelConnection!](/docs/api/admin-graphql/latest/connections/ChannelConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.unpublishedChannels.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/Collection#queries)Queries

* collection (Collection)
* collectionByIdentifier (Collection)
* collections (CollectionConnection!)
* collectionByHandle (Collection): deprecated

[Anchor to collection](/docs/api/admin-graphql/latest/objects/Collection#query-collection)[collection](/docs/api/admin-graphql/latest/queries/collection) •query
:   Retrieves a [collection](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection) by its ID.
    A collection represents a grouping of [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
    that merchants can display and sell as a group in their [online store](https://shopify.dev/docs/apps/build/online-store) and
    other [sales channels](https://shopify.dev/docs/apps/build/sales-channels).

    Use the `collection` query when you need to:

    * Manage collection publishing across sales channels
    * Access collection metadata and SEO information
    * Work with collection rules and product relationships

    A collection can be either a custom ([manual](https://help.shopify.com/manual/products/collections/manual-shopify-collection))
    collection where products are manually added, or a smart ([automated](https://help.shopify.com/manual/products/collections/automated-collections))
    collection where products are automatically included based on defined rules. Each collection has associated metadata including
    title, description, handle, image, and [metafields](https://shopify.dev/docs/apps/build/custom-data/metafields).

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Collection#query-collection.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `Collection` to return.

    ---

[Anchor to collectionByIdentifier](/docs/api/admin-graphql/latest/objects/Collection#query-collectionByIdentifier)[collectionByIdentifier](/docs/api/admin-graphql/latest/queries/collectionByIdentifier) •query
:   Return a collection by an identifier.

    Show fields

    ### Arguments

    [Anchor to identifier](/docs/api/admin-graphql/latest/objects/Collection#query-collectionByIdentifier.arguments.identifier)identifier •[CollectionIdentifierInput!](/docs/api/admin-graphql/latest/input-objects/CollectionIdentifierInput) required
    :   The identifier of the collection.

        Show input fields

    ---

[Anchor to collections](/docs/api/admin-graphql/latest/objects/Collection#query-collections)[collections](/docs/api/admin-graphql/latest/queries/collections) •query
:   Retrieves a list of [collections](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection)
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

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.sortKey)sortKey •[CollectionSortKeys](/docs/api/admin-graphql/latest/enums/CollectionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-collection_type) collection\_type •string


        Valid values:

        * `custom`
        * `smart`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-handle) handle •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-product_id) product\_id •id
        :   Filter by collections containing a product by its ID.

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-product_publication_status) product\_publication\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-published_at) published\_at •time
        :   Filter by the date and time when the collection was published to the Online Store.

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-published_status) published\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-title) title •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Collection#argument-query-filter-updated_at) updated\_at •time

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/Collection#query-collections.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

[Anchor to collectionByHandle](/docs/api/admin-graphql/latest/objects/Collection#query-collectionByHandle)[collectionByHandle](/docs/api/admin-graphql/latest/queries/collectionByHandle) •query Deprecated
:   Show fields

    ### Arguments

    [Anchor to handle](/docs/api/admin-graphql/latest/objects/Collection#query-collectionByHandle.arguments.handle)handle •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The handle of the collection.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/Collection#mutations)Mutations

* collectionAddProducts (CollectionAddProductsPayload)
* collectionCreate (CollectionCreatePayload)
* collectionDuplicate (CollectionDuplicatePayload)
* collectionUpdate (CollectionUpdatePayload)

[Anchor to collectionAddProducts](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionAddProducts)[collectionAddProducts](/docs/api/admin-graphql/latest/mutations/collectionAddProducts) •mutation
:   Adds multiple products to an existing collection in a single operation. This mutation provides an efficient way to bulk-manage collection membership without individual product updates.

    For example, when merchants create seasonal collections, they can add dozens of related products at once rather than updating each product individually. A clothing store might add all winter jackets to a "Winter Collection" in one operation.

    Use `CollectionAddProducts` to:

    * Bulk-add products to collections for efficient catalog management
    * Implement collection building tools in admin interfaces
    * Organize collection membership during bulk product operations
    * Reduce API calls when managing large product sets

    The mutation processes multiple product additions and returns success status along with any errors encountered during the operation. Products are added to the collection while preserving existing collection settings.

    This operation only works with manual collections where merchants explicitly choose which products to include. It will return an error if used with smart collections that automatically include products based on conditions.

    Learn more about [collection management](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionAddProducts.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the collection that's being updated. This can't be a smart collection.

    [Anchor to productIds](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionAddProducts.arguments.productIds)productIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The IDs of the products that are being added to the collection.
        If any of the products is already present in the input collection,
        then an error is raised and no products are added.

    ---

[Anchor to collectionCreate](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionCreate)[collectionCreate](/docs/api/admin-graphql/latest/mutations/collectionCreate) •mutation
:   Creates a [collection](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection)
    to group [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) together
    in the [online store](https://shopify.dev/docs/apps/build/online-store) and
    other [sales channels](https://shopify.dev/docs/apps/build/sales-channels).
    For example, an athletics store might create different collections for running attire, shoes, and accessories.

    There are two types of collections:

    * **[Custom (manual) collections](https://help.shopify.com/manual/products/collections/manual-shopify-collection)**: You specify the products to include in a collection.
    * **[Smart (automated) collections](https://help.shopify.com/manual/products/collections/automated-collections)**: You define rules, and products matching those rules are automatically
      included in the collection.

    Use the `collectionCreate` mutation when you need to:

    * Create a new collection for a product launch or campaign
    * Organize products by category, season, or promotion
    * Automate product grouping using rules (for example, by tag, type, or price)

    ---

    Note

    The created collection is unpublished by default. To make it available to customers,
    use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
    mutation after creation.

    **Note:**

    The created collection is unpublished by default. To make it available to customers,
    use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
    mutation after creation.

    **Note:** The created collection is unpublished by default. To make it available to customers,
    use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish"><code><span class="PreventFireFoxApplyingGapToWBR">publishable<wbr/>Publish</span></code></a>
    mutation after creation.

    ---

    Learn more about [using metafields with smart collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionCreate.arguments.input)input •[CollectionInput!](/docs/api/admin-graphql/latest/input-objects/CollectionInput) required
    :   The properties to use when creating the collection.

        Show input fields

    ---

[Anchor to collectionDuplicate](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionDuplicate)[collectionDuplicate](/docs/api/admin-graphql/latest/mutations/collectionDuplicate) •mutation
:   Duplicates a [collection](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection).

    An existing collection ID and new title are required.

    ## Publication Duplication

    Publications may be excluded by passing `copyPublications: false` in the input.

    ## Metafields

    Metafield values are not duplicated if the unique values capability is enabled.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionDuplicate.arguments.input)input •[CollectionDuplicateInput!](/docs/api/admin-graphql/latest/input-objects/CollectionDuplicateInput) required
    :   The input for duplicating a collection.

        Show input fields

    ---

[Anchor to collectionUpdate](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionUpdate)[collectionUpdate](/docs/api/admin-graphql/latest/mutations/collectionUpdate) •mutation
:   Updates a [collection](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection),
    modifying its properties, products, or publication settings. Collections help organize
    [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) together
    in the [online store](https://shopify.dev/docs/apps/build/online-store) and
    other [sales channels](https://shopify.dev/docs/apps/build/sales-channels).

    Use the `collectionUpdate` mutation to programmatically modify collections in scenarios such as:

    * Updating collection details, like title, description, or image
    * Modifying SEO metadata for better search visibility
    * Changing which products are included (using rule updates for smart collections)
    * Publishing or unpublishing collections across different sales channels
    * Updating custom data using [metafields](https://shopify.dev/docs/apps/build/custom-data/metafields)

    There are two types of collections with different update capabilities:

    * **[Custom (manual) collections](https://help.shopify.com/manual/products/collections/manual-shopify-collection)**: You can update collection properties, but rule sets can't be modified since products are manually selected.
    * **[Smart (automated) collections](https://help.shopify.com/manual/products/collections/automated-collections)**: You can update both collection properties and the rules that automatically determine which products are included.
      When updating [rule sets](https://shopify.dev/docs/api/admin-graphql/latest/objects/CollectionRuleConditions) for smart collections, the operation might be processed asynchronously. In these cases, the mutation returns a [`job`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Job) object that you can use to track the progress of the update.

    To publish or unpublish collections to specific sales channels, use the dedicated
    [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish) and
    [`publishableUnpublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishableUnpublish) mutations.

    Learn more about [using metafields with smart collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionUpdate.arguments.input)input •[CollectionInput!](/docs/api/admin-graphql/latest/input-objects/CollectionInput) required
    :   The updated properties for the collection.

        Show input fields

    ---

### Deprecated mutations

* collectionPublish (CollectionPublishPayload): deprecated
* collectionUnpublish (CollectionUnpublishPayload): deprecated

[Anchor to collectionPublish](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionPublish)[collectionPublish](/docs/api/admin-graphql/latest/mutations/collectionPublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionPublish.arguments.input)input •[CollectionPublishInput!](/docs/api/admin-graphql/latest/input-objects/CollectionPublishInput) required
    :   Specify a collection to publish and the sales channels to publish it to.

        Show input fields

    ---

[Anchor to collectionUnpublish](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionUnpublish)[collectionUnpublish](/docs/api/admin-graphql/latest/mutations/collectionUnpublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Collection#mutation-collectionUnpublish.arguments.input)input •[CollectionUnpublishInput!](/docs/api/admin-graphql/latest/input-objects/CollectionUnpublishInput) required
    :   Specify a collection to unpublish and the sales channels to remove it from.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Collection#interfaces)Interfaces

* HasEvents
* HasMetafieldDefinitions
* HasMetafields
* HasPublishedTranslations
* Node
* Publishable

[Anchor to HasEvents](/docs/api/admin-graphql/latest/objects/Collection#interface-HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents) •interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/Collection#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/Collection#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/Collection#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Collection#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

[Anchor to Publishable](/docs/api/admin-graphql/latest/objects/Collection#interface-Publishable)[Publishable](/docs/api/admin-graphql/latest/interfaces/Publishable) •interface

---

Was this section helpful?

YesNo