---
source: https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_products` access scope.

How a product can be sold and purchased through recurring billing or deferred purchase options. Defines the specific terms for subscriptions, pre-orders, or try-before-you-buy offers, including when to bill customers, when to fulfill orders, and what pricing adjustments to apply.

Each selling plan has billing, delivery, and pricing policies that control the purchase experience. The plan's [`options`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.options) and [`category`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.category) help merchants organize and report on different selling strategies. Plans are grouped within a [`SellingPlanGroup`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlanGroup) that associates them with [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) and [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects.

---

Caution

Selling plans and associated records are automatically deleted 48 hours after a merchant uninstalls the [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) that created them. Back up these records if you need to restore them later.

**Caution:**

Selling plans and associated records are automatically deleted 48 hours after a merchant uninstalls the [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) that created them. Back up these records if you need to restore them later.

**Caution:** Selling plans and associated records are automatically deleted 48 hours after a merchant uninstalls the <a href="https://shopify.dev/docs/api/admin-graphql/latest/objects/App"><code>App</code></a> that created them. Back up these records if you need to restore them later.

---

Learn more about [selling plans](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/SellingPlan#fields)Fields

* billingPolicy (SellingPlanBillingPolicy!)
* category (SellingPlanCategory)
* createdAt (DateTime!)
* deliveryPolicy (SellingPlanDeliveryPolicy!)
* description (String)
* id (ID!)
* inventoryPolicy (SellingPlanInventoryPolicy)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* name (String!)
* options ([String!]!)
* position (Int)
* pricingPolicies ([SellingPlanPricingPolicy!]!)
* translations ([Translation!]!)
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated

[Anchor to billingPolicy](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.billingPolicy)billingPolicy •[SellingPlanBillingPolicy!](/docs/api/admin-graphql/latest/unions/SellingPlanBillingPolicy) non-null
:   A selling plan policy which describes the recurring billing details.

    Show union types

[Anchor to category](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.category)category •[SellingPlanCategory](/docs/api/admin-graphql/latest/enums/SellingPlanCategory)
:   The category used to classify the selling plan for reporting purposes.

    Show enum values

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the selling plan was created.

[Anchor to deliveryPolicy](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.deliveryPolicy)deliveryPolicy •[SellingPlanDeliveryPolicy!](/docs/api/admin-graphql/latest/unions/SellingPlanDeliveryPolicy) non-null
:   A selling plan policy which describes the delivery details.

    Show union types

[Anchor to description](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.description)description •[String](/docs/api/admin-graphql/latest/scalars/String)
:   Buyer facing string which describes the selling plan commitment.

[Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to inventoryPolicy](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.inventoryPolicy)inventoryPolicy •[SellingPlanInventoryPolicy](/docs/api/admin-graphql/latest/objects/SellingPlanInventoryPolicy)
:   When to reserve inventory for a selling plan.

    Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to name](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.name)name •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   A customer-facing description of the selling plan.

    If your store supports multiple currencies, then don't include country-specific pricing content, such as "Buy monthly, get 10$ CAD off". This field won't be converted to reflect different currencies.

[Anchor to options](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.options)options •[[String!]!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The values of all options available on the selling plan. Selling plans are grouped together in Liquid when they're created by the same app, and have the same `selling_plan_group.name` and `selling_plan_group.options` values.

[Anchor to position](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.position)position •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   Relative position of the selling plan for display. A lower position will be displayed before a higher position.

[Anchor to pricingPolicies](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.pricingPolicies)pricingPolicies •[[SellingPlanPricingPolicy!]!](/docs/api/admin-graphql/latest/unions/SellingPlanPricingPolicy) non-null
:   Selling plan pricing details.

    Show union types

[Anchor to translations](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/SellingPlan#field-SellingPlan.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlan#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

---

Was this section helpful?

YesNo

### Fields and connections with this object

* <->[SellingPlanConnection.nodes](/docs/api/admin-graphql/latest/connections/SellingPlanConnection#returns-nodes)
* {}[SellingPlanEdge.node](/docs/api/admin-graphql/latest/objects/SellingPlanEdge#field-SellingPlanEdge.fields.node)
* {}[SellingPlanGroup.sellingPlans](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans)

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/SellingPlan#interfaces)Interfaces

* HasMetafieldDefinitions
* HasMetafields
* HasPublishedTranslations
* Node

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/SellingPlan#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/SellingPlan#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/SellingPlan#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/SellingPlan#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo

### Implements

* ||-[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions)
* ||-[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields)
* ||-[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations)
* ||-[Node](/docs/api/admin-graphql/latest/interfaces/Node)