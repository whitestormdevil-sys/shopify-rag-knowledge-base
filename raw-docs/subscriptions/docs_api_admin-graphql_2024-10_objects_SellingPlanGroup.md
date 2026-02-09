---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/SellingPlanGroup
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_products` access scope.

A selling method that defines how products can be sold through purchase options like subscriptions, pre-orders, or try-before-you-buy. Groups one or more [`SellingPlan`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan) objects that share the same selling method and options.

The group provides buyer-facing labels and merchant-facing descriptions for the selling method. Associates [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) and [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects with selling plan groups to offer them through these purchase options.

---

Caution

Selling plan groups and their associated records are automatically deleted 48 hours after a merchant uninstalls the [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) that created them. Back up these records if you need to restore them later.

**Caution:**

Selling plan groups and their associated records are automatically deleted 48 hours after a merchant uninstalls the [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) that created them. Back up these records if you need to restore them later.

**Caution:** Selling plan groups and their associated records are automatically deleted 48 hours after a merchant uninstalls the <a href="https://shopify.dev/docs/api/admin-graphql/latest/objects/App"><code>App</code></a> that created them. Back up these records if you need to restore them later.

---

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#fields)Fields

* appId (String)
* appliesToProduct (Boolean!)
* appliesToProductVariant (Boolean!)
* appliesToProductVariants (Boolean!)
* createdAt (DateTime!)
* description (String)
* id (ID!)
* merchantCode (String!)
* name (String!)
* options ([String!]!)
* position (Int)
* products (ProductConnection!)
* productsCount (Count)
* productVariants (ProductVariantConnection!)
* productVariantsCount (Count)
* sellingPlans (SellingPlanConnection!)
* summary (String)
* translations ([Translation!]!)

[Anchor to appId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appId)appId •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The ID for app, exposed in Liquid and product JSON.

[Anchor to appliesToProduct](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProduct)appliesToProduct •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the given product is directly associated to the selling plan group.

    Show arguments

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProduct.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product.

    ---

[Anchor to appliesToProductVariant](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProductVariant)appliesToProductVariant •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the given product variant is directly associated to the selling plan group.

    Show arguments

    ### Arguments

    [Anchor to productVariantId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProductVariant.arguments.productVariantId)productVariantId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product.

    ---

[Anchor to appliesToProductVariants](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProductVariants)appliesToProductVariants •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether any of the product variants of the given product are associated to the selling plan group.

    Show arguments

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.appliesToProductVariants.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product.

    ---

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the selling plan group was created.

[Anchor to description](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.description)description •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The merchant-facing description of the selling plan group.

[Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to merchantCode](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.merchantCode)merchantCode •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The merchant-facing label of the selling plan group.

[Anchor to name](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.name)name •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The buyer-facing label of the selling plan group.

[Anchor to options](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.options)options •[[String!]!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The values of all options available on the selling plan group. Selling plans are grouped together in Liquid when they're created by the same app, and have the same `selling_plan_group.name` and `selling_plan_group.options` values.

[Anchor to position](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.position)position •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The relative position of the selling plan group for display.

[Anchor to products](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products)products •[ProductConnection!](/docs/api/admin-graphql/latest/connections/ProductConnection) non-null
:   Products associated to the selling plan group.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.products.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to productsCount](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productsCount)productsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   A count of products associated to the selling plan group.

    Show fields

[Anchor to productVariants](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants)productVariants •[ProductVariantConnection!](/docs/api/admin-graphql/latest/connections/ProductVariantConnection) non-null
:   Product variants associated to the selling plan group.

    Show fields

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.productId)productId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters the product variants by a product ID.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariants.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to productVariantsCount](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariantsCount)productVariantsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   A count of product variants associated to the selling plan group.

    Show fields

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.productVariantsCount.arguments.productId)productId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of the product to scope the count to.

    ---

[Anchor to sellingPlans](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans)sellingPlans •[SellingPlanConnection!](/docs/api/admin-graphql/latest/connections/SellingPlanConnection) non-null
:   Selling plans associated to the selling plan group.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.sellingPlans.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to summary](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.summary)summary •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A summary of the policies associated to the selling plan group.

[Anchor to translations](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#field-SellingPlanGroup.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#queries)Queries

* sellingPlanGroup (SellingPlanGroup)
* sellingPlanGroups (SellingPlanGroupConnection!)

[Anchor to sellingPlanGroup](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroup)[sellingPlanGroup](/docs/api/admin-graphql/latest/queries/sellingPlanGroup) •query
:   Returns a `SellingPlanGroup` resource by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroup.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `SellingPlanGroup` to return.

    ---

[Anchor to sellingPlanGroups](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups)[sellingPlanGroups](/docs/api/admin-graphql/latest/queries/sellingPlanGroups) •query
:   Retrieves a paginated list of [`SellingPlanGroup`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlanGroup) objects that belong to the app making the API call. Selling plan groups are selling methods like subscriptions, preorders, or other purchase options that merchants offer to customers.

    Each group has one or more [`SellingPlan`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SellingPlan) objects that define specific billing and delivery schedules, pricing adjustments, and policies. Use the [`query`](https://shopify.dev/docs/api/admin-graphql/latest/queries/sellingPlanGroups#arguments-query) argument to search by name or filter results by other criteria.

    Learn more about [building selling plans](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans).

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.sortKey)sortKey •[SellingPlanGroupSortKeys](/docs/api/admin-graphql/latest/enums/SellingPlanGroupSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#query-sellingPlanGroups.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-app_id) app\_id •id


        Valid values:

        * `CURRENT` Default
        * `ALL`
        * `* (numeric app ID)`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-category) category •string
        :   A comma-separated list of categories.

        Valid values:

        * `SUBSCRIPTION`
        * `PRE_ORDER`
        * `TRY_BEFORE_YOU_BUY`
        * `OTHER`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-delivery_frequency) delivery\_frequency •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-name) name •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#argument-query-filter-percentage_off) percentage\_off •float

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutations)Mutations

* sellingPlanGroupAddProducts (SellingPlanGroupAddProductsPayload)
* sellingPlanGroupAddProductVariants (SellingPlanGroupAddProductVariantsPayload)
* sellingPlanGroupCreate (SellingPlanGroupCreatePayload)
* sellingPlanGroupUpdate (SellingPlanGroupUpdatePayload)

[Anchor to sellingPlanGroupAddProducts](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProducts)[sellingPlanGroupAddProducts](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProducts) •mutation
:   Adds multiple products to a selling plan group.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProducts.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the selling plan group.

    [Anchor to productIds](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProducts.arguments.productIds)productIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The IDs of the products to add.

    ---

[Anchor to sellingPlanGroupAddProductVariants](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProductVariants)[sellingPlanGroupAddProductVariants](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProductVariants) •mutation
:   Adds multiple product variants to a selling plan group.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProductVariants.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the selling plan group.

    [Anchor to productVariantIds](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupAddProductVariants.arguments.productVariantIds)productVariantIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The IDs of the product variants to add.

    ---

[Anchor to sellingPlanGroupCreate](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupCreate)[sellingPlanGroupCreate](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate) •mutation
:   Creates a selling plan group that defines how products can be sold and purchased. A selling plan group represents a selling method such as "Subscribe and save", "Pre-order", or "Try before you buy" and contains one or more selling plans with specific billing, delivery, and pricing policies.

    Use the [`resources`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#arguments-resources) argument to associate products or product variants with the group during creation. You can also add products later using [`sellingPlanGroupAddProducts`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProducts) or [`sellingPlanGroupAddProductVariants`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProductVariants).

    Learn more about [building selling plan groups](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan#step-1-create-a-selling-plan-group) or explore [examples of creating TBYB and other selling plan groups](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate?example=create-a-tbyb-selling-plan-group).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupCreate.arguments.input)input •[SellingPlanGroupInput!](/docs/api/admin-graphql/latest/input-objects/SellingPlanGroupInput) required
    :   The properties of the new Selling Plan Group.

        Show input fields

    [Anchor to resources](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupCreate.arguments.resources)resources •[SellingPlanGroupResourceInput](/docs/api/admin-graphql/latest/input-objects/SellingPlanGroupResourceInput)
    :   The resources this Selling Plan Group should be applied to.

        Show input fields

    ---

[Anchor to sellingPlanGroupUpdate](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupUpdate)[sellingPlanGroupUpdate](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupUpdate) •mutation
:   Update a Selling Plan Group.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The Selling Plan Group to update.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#mutation-sellingPlanGroupUpdate.arguments.input)input •[SellingPlanGroupInput!](/docs/api/admin-graphql/latest/input-objects/SellingPlanGroupInput) required
    :   The properties of the Selling Plan Group to update.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#interfaces)Interfaces

* HasPublishedTranslations
* Node

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/SellingPlanGroup#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo