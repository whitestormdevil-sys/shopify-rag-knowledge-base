---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/DiscountAutomaticNode
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires Apps must have `read_discounts` access scope.

The `DiscountAutomaticNode` object enables you to manage [automatic discounts](https://help.shopify.com/manual/discounts/discount-types#automatic-discounts) that are applied when an order meets specific criteria. You can create amount off, free shipping, or buy X get Y automatic discounts. For example, you can offer customers a free shipping discount that applies when conditions are met. Or you can offer customers a buy X get Y discount that's automatically applied when customers spend a specified amount of money, or a specified quantity of products.

Learn more about working with [Shopify's discount model](https://shopify.dev/docs/apps/build/discounts),
including related queries, mutations, limitations, and considerations.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#fields)Fields

* automaticDiscount (DiscountAutomatic!)
* events (EventConnection!)
* id (ID!)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated

[Anchor to automaticDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.automaticDiscount)automaticDiscount •[DiscountAutomatic!](/docs/api/admin-graphql/latest/unions/DiscountAutomatic) non-null
:   A discount that's applied automatically when an order meets specific criteria. Learn more about [automatic discounts](https://help.shopify.com/manual/discounts/discount-types#automatic-discounts).

    Show union types

[Anchor to events](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events)events •[EventConnection!](/docs/api/admin-graphql/latest/connections/EventConnection) non-null
:   The paginated list of events associated with the host subject.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.sortKey)sortKey •[EventSortKeys](/docs/api/admin-graphql/latest/enums/EventSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.events.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-action) action •string
        :   The action that occured.

        Example:

        * `action:create`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-comments) comments •boolean
        :   Whether or not to include [comment-events](https://shopify.dev/api/admin-graphql/latest/objects/CommentEvent) in your search, passing `false` will exclude comment-events, any other value will include comment-events.

        Example:

        * `false`
        * `true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the event occurred. Event data is retained for 1 year.

        Example:

        * `created_at:>2025-10-21`
        * `created_at:<now`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-subject_type) subject\_type •string
        :   The resource type affected by this event. See [EventSubjectType](https://shopify.dev/api/admin-graphql/latest/enums/EventSubjectType) for possible values.

        Example:

        * `PRODUCT_VARIANT`
        * `PRODUCT`
        * `COLLECTION`

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#field-DiscountAutomaticNode.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-updated_at) updated\_at •time
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

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#queries)Queries

* automaticDiscountNode (DiscountAutomaticNode)
* automaticDiscountNodes (DiscountAutomaticNodeConnection!): deprecated

[Anchor to automaticDiscountNode](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNode)[automaticDiscountNode](/docs/api/admin-graphql/latest/queries/automaticDiscountNode) •query
:   Returns a `DiscountAutomaticNode` resource by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNode.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `DiscountAutomaticNode` to return.

    ---

[Anchor to automaticDiscountNodes](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes)[automaticDiscountNodes](/docs/api/admin-graphql/latest/queries/automaticDiscountNodes) •query Deprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.sortKey)sortKey •[AutomaticDiscountSortKeys](/docs/api/admin-graphql/latest/enums/AutomaticDiscountSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-status) status •string
        :   Filter by the discount status.

        Valid values:

        * `active`
        * `expired`
        * `scheduled`

        Example:

        * `status:scheduled`

        [Anchor to](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#argument-query-filter-type) type •string
        :   Filter by the [discount type](https://help.shopify.com/manual/discounts/discount-types).

        Valid values:

        * `all`
        * `all_with_app`
        * `app`
        * `bxgy`
        * `fixed_amount`
        * `percentage`

        Example:

        * `type:bxgy`

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#query-automaticDiscountNodes.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutations)Mutations

* discountAutomaticActivate (DiscountAutomaticActivatePayload)
* discountAutomaticBasicCreate (DiscountAutomaticBasicCreatePayload)
* discountAutomaticBasicUpdate (DiscountAutomaticBasicUpdatePayload)
* discountAutomaticBxgyCreate (DiscountAutomaticBxgyCreatePayload)
* discountAutomaticBxgyUpdate (DiscountAutomaticBxgyUpdatePayload)
* discountAutomaticDeactivate (DiscountAutomaticDeactivatePayload)
* discountAutomaticFreeShippingCreate (DiscountAutomaticFreeShippingCreatePayload)
* discountAutomaticFreeShippingUpdate (DiscountAutomaticFreeShippingUpdatePayload)

[Anchor to discountAutomaticActivate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticActivate)[discountAutomaticActivate](/docs/api/admin-graphql/latest/mutations/discountAutomaticActivate) •mutation
:   Activates an automatic discount.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticActivate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the automatic discount to activate.

    ---

[Anchor to discountAutomaticBasicCreate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBasicCreate)[discountAutomaticBasicCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) •mutation
:   Creates an
    [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount)
    that's automatically applied on a cart and at checkout.

    ---

    Note

    To create code discounts, use the
    [`discountCodeBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)
    mutation.

    **Note:**

    To create code discounts, use the
    [`discountCodeBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)
    mutation.

    **Note:** To create code discounts, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Code<wbr/>Basic<wbr/>Create</span></code></a>
    mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to automaticBasicDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBasicCreate.arguments.automaticBasicDiscount)automaticBasicDiscount •[DiscountAutomaticBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticBasicInput) required
    :   The input data used to create the automatic amount off discount.

        Show input fields

    ---

[Anchor to discountAutomaticBasicUpdate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBasicUpdate)[discountAutomaticBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate) •mutation
:   Updates an existing
    [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount)
    that's automatically applied on a cart and at checkout.

    ---

    Note

    To update code discounts, use the
    [`discountCodeBasicUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate)
    mutation instead.

    **Note:**

    To update code discounts, use the
    [`discountCodeBasicUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate)
    mutation instead.

    **Note:** To update code discounts, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Code<wbr/>Basic<wbr/>Update</span></code></a>
    mutation instead.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBasicUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the automatic amount off discount to update.

    [Anchor to automaticBasicDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBasicUpdate.arguments.automaticBasicDiscount)automaticBasicDiscount •[DiscountAutomaticBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticBasicInput) required
    :   The input data used to update the automatic amount off discount.

        Show input fields

    ---

[Anchor to discountAutomaticBxgyCreate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBxgyCreate)[discountAutomaticBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate) •mutation
:   Creates a
    [buy X get Y discount (BXGY)](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y)
    that's automatically applied on a cart and at checkout.

    ---

    Note

    To create code discounts, use the
    [`discountCodeBxgyCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate)
    mutation.

    **Note:**

    To create code discounts, use the
    [`discountCodeBxgyCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate)
    mutation.

    **Note:** To create code discounts, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Code<wbr/>Bxgy<wbr/>Create</span></code></a>
    mutation.

    ---

    Show payload

    ### Arguments

    [Anchor to automaticBxgyDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBxgyCreate.arguments.automaticBxgyDiscount)automaticBxgyDiscount •[DiscountAutomaticBxgyInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticBxgyInput) required
    :   The input data used to create the automatic BXGY discount.

        Show input fields

    ---

[Anchor to discountAutomaticBxgyUpdate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBxgyUpdate)[discountAutomaticBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate) •mutation
:   Updates an existing
    [buy X get Y discount (BXGY)](https://help.shopify.com/manual/discounts/discount-types/buy-x-get-y)
    that's automatically applied on a cart and at checkout.

    ---

    Note

    To update code discounts, use the
    [`discountCodeBxgyUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate)
    mutation instead.

    **Note:**

    To update code discounts, use the
    [`discountCodeBxgyUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate)
    mutation instead.

    **Note:** To update code discounts, use the
    <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Code<wbr/>Bxgy<wbr/>Update</span></code></a>
    mutation instead.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBxgyUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the automatic BXGY discount to update.

    [Anchor to automaticBxgyDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticBxgyUpdate.arguments.automaticBxgyDiscount)automaticBxgyDiscount •[DiscountAutomaticBxgyInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticBxgyInput) required
    :   The input data used to update the automatic BXGY discount.

        Show input fields

    ---

[Anchor to discountAutomaticDeactivate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticDeactivate)[discountAutomaticDeactivate](/docs/api/admin-graphql/latest/mutations/discountAutomaticDeactivate) •mutation
:   Deactivates an automatic discount.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticDeactivate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the automatic discount to deactivate.

    ---

[Anchor to discountAutomaticFreeShippingCreate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticFreeShippingCreate)[discountAutomaticFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate) •mutation
:   Creates automatic free shipping discounts that apply to qualifying orders without requiring discount codes. These promotions automatically activate when customers meet specified criteria, streamlining the checkout experience.

    For example, a store might create an automatic free shipping discount for orders over variable pricing to encourage larger purchases, or offer free shipping to specific customer segments during promotional periods.

    Use `DiscountAutomaticFreeShippingCreate` to:

    * Set up code-free shipping promotions
    * Create order value-based shipping incentives
    * Target specific customer groups with shipping benefits
    * Establish location-based shipping discounts

    The mutation validates discount configuration and returns the created automatic discount node along with any configuration errors that need resolution.

    Learn more about [automatic discounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode).

    Show payload

    ### Arguments

    [Anchor to freeShippingAutomaticDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticFreeShippingCreate.arguments.freeShippingAutomaticDiscount)freeShippingAutomaticDiscount •[DiscountAutomaticFreeShippingInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticFreeShippingInput) required
    :   The input data used to create the automatic free shipping discount.

        Show input fields

    ---

[Anchor to discountAutomaticFreeShippingUpdate](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticFreeShippingUpdate)[discountAutomaticFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate) •mutation
:   Updates existing automatic free shipping discounts, allowing merchants to modify promotion criteria, shipping destinations, and eligibility requirements without recreating the entire discount structure.

    For example, extending a holiday free shipping promotion to include additional countries, adjusting the minimum order value threshold, or expanding customer eligibility to include new segments.

    Use `DiscountAutomaticFreeShippingUpdate` to:

    * Modify shipping discount thresholds and criteria
    * Expand or restrict geographic availability
    * Update customer targeting and eligibility rules
    * Adjust promotion timing and activation periods

    Changes take effect immediately for new orders, while the mutation validates all modifications and reports any configuration conflicts through user errors.

    Learn more about [managing automatic discounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountAutomaticFreeShipping).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticFreeShippingUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the automatic free shipping discount to update.

    [Anchor to freeShippingAutomaticDiscount](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#mutation-discountAutomaticFreeShippingUpdate.arguments.freeShippingAutomaticDiscount)freeShippingAutomaticDiscount •[DiscountAutomaticFreeShippingInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticFreeShippingInput) required
    :   The input data used to update the automatic free shipping discount.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#interfaces)Interfaces

* HasEvents
* HasMetafieldDefinitions
* HasMetafields
* Node

[Anchor to HasEvents](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#interface-HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents) •interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo