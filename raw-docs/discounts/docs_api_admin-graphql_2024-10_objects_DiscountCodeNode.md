---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/DiscountCodeNode
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires Apps must have `read_discounts` access scope.

The `DiscountCodeNode` object enables you to manage [code discounts](https://help.shopify.com/manual/discounts/discount-types#discount-codes) that are applied when customers enter a code at checkout. For example, you can offer discounts where customers have to enter a code to redeem an amount off discount on products, variants, or collections in a store. Or, you can offer discounts where customers have to enter a code to get free shipping. Merchants can create and share discount codes individually with customers.

Learn more about working with [Shopify's discount model](https://shopify.dev/docs/apps/build/discounts),
including related queries, mutations, limitations, and considerations.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#fields)Fields

* codeDiscount (DiscountCode!)
* events (EventConnection!)
* id (ID!)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated

[Anchor to codeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.codeDiscount)codeDiscount •[DiscountCode!](/docs/api/admin-graphql/latest/unions/DiscountCode) non-null
:   The underlying code discount object.

    Show union types

[Anchor to events](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events)events •[EventConnection!](/docs/api/admin-graphql/latest/connections/EventConnection) non-null
:   The paginated list of events associated with the host subject.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.sortKey)sortKey •[EventSortKeys](/docs/api/admin-graphql/latest/enums/EventSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.events.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-action) action •string
        :   The action that occured.

        Example:

        * `action:create`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-comments) comments •boolean
        :   Whether or not to include [comment-events](https://shopify.dev/api/admin-graphql/latest/objects/CommentEvent) in your search, passing `false` will exclude comment-events, any other value will include comment-events.

        Example:

        * `false`
        * `true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the event occurred. Event data is retained for 1 year.

        Example:

        * `created_at:>2025-10-21`
        * `created_at:<now`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-subject_type) subject\_type •string
        :   The resource type affected by this event. See [EventSubjectType](https://shopify.dev/api/admin-graphql/latest/enums/EventSubjectType) for possible values.

        Example:

        * `PRODUCT_VARIANT`
        * `PRODUCT`
        * `COLLECTION`

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#queries)Queries

* codeDiscountNode (DiscountCodeNode)
* codeDiscountNodeByCode (DiscountCodeNode)
* codeDiscountNodes (DiscountCodeNodeConnection!): deprecated

[Anchor to codeDiscountNode](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNode)[codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode) •query
:   Returns a [code discount](https://help.shopify.com/manual/discounts/discount-types#discount-codes) resource by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNode.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `DiscountCodeNode` to return.

    ---

[Anchor to codeDiscountNodeByCode](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodeByCode)[codeDiscountNodeByCode](/docs/api/admin-graphql/latest/queries/codeDiscountNodeByCode) •query
:   Retrieves a [code discount](https://help.shopify.com/manual/discounts/discount-types#discount-codes) by its discount code. The search is case-insensitive, enabling you to find discounts regardless of how customers enter the code.

    Returns a [`DiscountCodeNode`](https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountCodeNode) that contains the underlying discount details, which could be a basic [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount), a ["Buy X Get Y" (BXGY) discount](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y), a [free shipping discount](https://help.shopify.com/manual/discounts/discount-types/free-shipping), or an [app-provided discount](https://help.shopify.com/manual/discounts/discount-types/discounts-with-apps).

    Learn more about working with [Shopify's discount model](https://shopify.dev/docs/apps/build/discounts).

    Show fields

    ### Arguments

    [Anchor to code](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodeByCode.arguments.code)code •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The case-insensitive code of the `DiscountCodeNode` to return.

    ---

[Anchor to codeDiscountNodes](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes)[codeDiscountNodes](/docs/api/admin-graphql/latest/queries/codeDiscountNodes) •query Deprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.sortKey)sortKey •[CodeDiscountSortKeys](/docs/api/admin-graphql/latest/enums/CodeDiscountSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-combines_with) combines\_with •string
        :   Filter by the [discount classes](https://help.shopify.com/manual/discounts/combining-discounts/discount-combinations) that you can use in combination with [Shopify discount types](https://help.shopify.com/manual/discounts/discount-types).

        Valid values:

        * `order_discounts`
        * `product_discounts`
        * `shipping_discounts`

        Example:

        * `combines_with:product_discounts`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the discount was created.

        Example:

        * `created_at:>'2020-10-21T23:39:20Z'`
        * `created_at:<now`
        * `created_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-discount_type) discount\_type •string
        :   Filter by the [discount type](https://help.shopify.com/manual/discounts/discount-types).

        Valid values:

        * `bogo`
        * `fixed_amount`
        * `free_shipping`
        * `percentage`

        Example:

        * `discount_type:fixed_amount`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-ends_at) ends\_at •time
        :   Filter by the date and time when the discount expires and is no longer available for customer use.

        Example:

        * `ends_at:>'2020-10-21T23:39:20Z'`
        * `ends_at:<now`
        * `ends_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-starts_at) starts\_at •time
        :   Filter by the date and time, in the shop's timezone, when the discount becomes active and is available for customer use.

        Example:

        * `starts_at:>'2020-10-21T23:39:20Z'`
        * `starts_at:<now`
        * `starts_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-status) status •string
        :   Filter by the status of the discount.

        Valid values:

        * `active`
        * `expired`
        * `scheduled`

        Example:

        * `status:scheduled`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-times_used) times\_used •integer
        :   Filter by the number of times the discount has been used. For example, if a "Buy 3, Get 1 Free" t-shirt discount is automatically applied in 200 transactions, then the discount has been used 200 times.   
              
             This value is updated asynchronously. As a result, it might be different than the actual usage count.

        Example:

        * `times_used:0`
        * `times_used:>150`
        * `times_used:>=200`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-title) title •string
        :   Filter by the discount name that displays to customers.

        Example:

        * `title:Black Friday Sale`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-type) type •string
        :   Filter by the [discount type](https://help.shopify.com/manual/discounts/discount-types).

        Valid values:

        * `all`
        * `all_with_app`
        * `app`
        * `bxgy`
        * `fixed_amount`
        * `free_shipping`
        * `percentage`

        Example:

        * `type:percentage`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the discount was last updated.

        Example:

        * `updated_at:>'2020-10-21T23:39:20Z'`
        * `updated_at:<now`
        * `updated_at:<='2024'`

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#query-codeDiscountNodes.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutations)Mutations

* discountCodeActivate (DiscountCodeActivatePayload)
* discountCodeBasicCreate (DiscountCodeBasicCreatePayload)
* discountCodeBasicUpdate (DiscountCodeBasicUpdatePayload)
* discountCodeBxgyCreate (DiscountCodeBxgyCreatePayload)
* discountCodeBxgyUpdate (DiscountCodeBxgyUpdatePayload)
* discountCodeDeactivate (DiscountCodeDeactivatePayload)
* discountCodeFreeShippingCreate (DiscountCodeFreeShippingCreatePayload)
* discountCodeFreeShippingUpdate (DiscountCodeFreeShippingUpdatePayload)

[Anchor to discountCodeActivate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeActivate)[discountCodeActivate](/docs/api/admin-graphql/latest/mutations/discountCodeActivate) •mutation
:   Activates a previously created code discount, making it available for customers to use during checkout. This mutation transitions inactive discount codes into an active state where they can be applied to orders.

    For example, after creating a "SUMMER20" discount code but leaving it inactive during setup, merchants can activate it when ready to launch their summer promotion campaign.

    Use `DiscountCodeActivate` to:

    * Launch scheduled promotional campaigns
    * Reactivate previously paused discount codes
    * Enable discount codes after configuration changes
    * Control the timing of discount availability

    The mutation returns the updated discount code node with its new active status and handles any validation errors that might prevent activation, such as conflicting discount rules or invalid date ranges.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeActivate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the code discount to activate.

    ---

[Anchor to discountCodeBasicCreate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBasicCreate)[discountCodeBasicCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate) •mutation
:   Creates an [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount) that's applied on a cart and at checkout when a customer enters a code. Amount off discounts can be a percentage off or a fixed amount off.

    ---

    Note

    To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) mutation.

    **Note:**

    To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) mutation.

    **Note:** To create discounts that are automatically applied on a cart and at checkout, use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Basic<wbr/>Create</span></code></a> mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to basicCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBasicCreate.arguments.basicCodeDiscount)basicCodeDiscount •[DiscountCodeBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeBasicInput) required
    :   The input data used to create the discount code.

        Show input fields

    ---

[Anchor to discountCodeBasicUpdate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBasicUpdate)[discountCodeBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate) •mutation
:   Updates an [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount) that's applied on a cart and at checkout when a customer enters a code. Amount off discounts can be a percentage off or a fixed amount off.

    ---

    Note

    To update discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate) mutation.

    **Note:**

    To update discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate) mutation.

    **Note:** To update discounts that are automatically applied on a cart and at checkout, use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Basic<wbr/>Update</span></code></a> mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBasicUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the discount code to update.

    [Anchor to basicCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBasicUpdate.arguments.basicCodeDiscount)basicCodeDiscount •[DiscountCodeBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeBasicInput) required
    :   The input data used to update the discount code.

        Show input fields

    ---

[Anchor to discountCodeBxgyCreate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBxgyCreate)[discountCodeBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate) •mutation
:   Creates a
    [buy X get Y discount (BXGY)](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y)
    that's applied on a cart and at checkout when a customer enters a code.

    ---

    Note

    To create discounts that are automatically applied on a cart and at checkout, use the
    [`discountAutomaticBxgyCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate)
    mutation.

    **Note:**

    To create discounts that are automatically applied on a cart and at checkout, use the
    [`discountAutomaticBxgyCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate)
    mutation.

    **Note:** To create discounts that are automatically applied on a cart and at checkout, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Bxgy<wbr/>Create</span></code></a>
    mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to bxgyCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBxgyCreate.arguments.bxgyCodeDiscount)bxgyCodeDiscount •[DiscountCodeBxgyInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeBxgyInput) required
    :   The input data used to create the BXGY code discount.

        Show input fields

    ---

[Anchor to discountCodeBxgyUpdate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBxgyUpdate)[discountCodeBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate) •mutation
:   Updates a
    [buy X get Y discount (BXGY)](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y)
    that's applied on a cart and at checkout when a customer enters a code.

    ---

    Note

    To update discounts that are automatically applied on a cart and at checkout, use the
    [`discountAutomaticBxgyUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate)
    mutation.

    **Note:**

    To update discounts that are automatically applied on a cart and at checkout, use the
    [`discountAutomaticBxgyUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate)
    mutation.

    **Note:** To update discounts that are automatically applied on a cart and at checkout, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Bxgy<wbr/>Update</span></code></a>
    mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBxgyUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the BXGY code discount to update.

    [Anchor to bxgyCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeBxgyUpdate.arguments.bxgyCodeDiscount)bxgyCodeDiscount •[DiscountCodeBxgyInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeBxgyInput) required
    :   The input data used to update the BXGY code discount.

        Show input fields

    ---

[Anchor to discountCodeDeactivate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeDeactivate)[discountCodeDeactivate](/docs/api/admin-graphql/latest/mutations/discountCodeDeactivate) •mutation
:   Temporarily suspends a code discount without permanently removing it from the store. Deactivation allows merchants to pause promotional campaigns while preserving the discount configuration for potential future use.

    For example, when a flash sale needs to end immediately or a discount code requires temporary suspension due to inventory issues, merchants can deactivate it to stop new redemptions while keeping the discount structure intact.

    Use `DiscountCodeDeactivate` to:

    * Pause active promotional campaigns timely
    * Temporarily suspend problematic discount codes
    * Control discount availability during inventory shortages
    * Maintain discount history while stopping usage

    Deactivated discounts remain in the system and can be reactivated later, unlike deletion which persistently removes the code. Customers attempting to use deactivated codes will receive appropriate error messages.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeDeactivate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the code discount to deactivate.

    ---

[Anchor to discountCodeFreeShippingCreate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeFreeShippingCreate)[discountCodeFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingCreate) •mutation
:   Creates an [free shipping discount](https://help.shopify.com/manual/discounts/discount-types/free-shipping) that's applied on a cart and at checkout when a customer enters a code.

    ---

    Note

    To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticFreeShippingCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate) mutation.

    **Note:**

    To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticFreeShippingCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate) mutation.

    **Note:** To create discounts that are automatically applied on a cart and at checkout, use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Free<wbr/>Shipping<wbr/>Create</span></code></a> mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to freeShippingCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeFreeShippingCreate.arguments.freeShippingCodeDiscount)freeShippingCodeDiscount •[DiscountCodeFreeShippingInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeFreeShippingInput) required
    :   The input data used to create the discount code.

        Show input fields

    ---

[Anchor to discountCodeFreeShippingUpdate](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeFreeShippingUpdate)[discountCodeFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingUpdate) •mutation
:   Updates a [free shipping discount](https://help.shopify.com/manual/discounts/discount-types/free-shipping) that's applied on a cart and at checkout when a customer enters a code.

    ---

    Note

    To update a free shipping discount that's automatically applied on a cart and at checkout, use the [`discountAutomaticFreeShippingUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate) mutation.

    **Note:**

    To update a free shipping discount that's automatically applied on a cart and at checkout, use the [`discountAutomaticFreeShippingUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate) mutation.

    **Note:** To update a free shipping discount that&#39;s automatically applied on a cart and at checkout, use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Free<wbr/>Shipping<wbr/>Update</span></code></a> mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeFreeShippingUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the discount code to update.

    [Anchor to freeShippingCodeDiscount](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#mutation-discountCodeFreeShippingUpdate.arguments.freeShippingCodeDiscount)freeShippingCodeDiscount •[DiscountCodeFreeShippingInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeFreeShippingInput) required
    :   The input data used to update the discount code.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#interfaces)Interfaces

* HasEvents
* HasMetafieldDefinitions
* HasMetafields
* Node

[Anchor to HasEvents](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#interface-HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents) •interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo