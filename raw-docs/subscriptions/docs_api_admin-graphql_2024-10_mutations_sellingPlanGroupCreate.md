---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/sellingPlanGroupCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_products` access scope as well as any of `write_own_subscription_contracts`, `write_purchase_options` access scopes. Also: The user must have `manage_orders_information` permissions.

Creates a selling plan group that defines how products can be sold and purchased. A selling plan group represents a selling method such as "Subscribe and save", "Pre-order", or "Try before you buy" and contains one or more selling plans with specific billing, delivery, and pricing policies.

Use the [`resources`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#arguments-resources) argument to associate products or product variants with the group during creation. You can also add products later using [`sellingPlanGroupAddProducts`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProducts) or [`sellingPlanGroupAddProductVariants`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupAddProductVariants).

Learn more about [building selling plan groups](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan#step-1-create-a-selling-plan-group) or explore [examples of creating TBYB and other selling plan groups](https://shopify.dev/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate?example=create-a-tbyb-selling-plan-group).

* input (SellingPlanGroupInput!)
* resources (SellingPlanGroupResourceInput)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#arguments-input)input •[SellingPlanGroupInput!](/docs/api/admin-graphql/latest/input-objects/SellingPlanGroupInput) required
:   The properties of the new Selling Plan Group.

    Show input fields

[Anchor to resources](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#arguments-resources)resources •[SellingPlanGroupResourceInput](/docs/api/admin-graphql/latest/input-objects/SellingPlanGroupResourceInput)
:   The resources this Selling Plan Group should be applied to.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to SellingPlanGroupCreatePayload returns](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#returns)SellingPlanGroupCreatePayload returns

* sellingPlanGroup (SellingPlanGroup)
* userErrors ([SellingPlanGroupUserError!]!)

[Anchor to sellingPlanGroup](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#returns-sellingPlanGroup)sellingPlanGroup •[SellingPlanGroup](/docs/api/admin-graphql/latest/objects/SellingPlanGroup)
:   The created selling plan group object.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate#returns-userErrors)userErrors •[[SellingPlanGroupUserError!]!](/docs/api/admin-graphql/latest/objects/SellingPlanGroupUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo