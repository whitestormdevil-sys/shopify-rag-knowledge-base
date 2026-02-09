---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/SellingPlan
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_read_selling_plans` access scope.

Represents how products and variants can be sold and purchased.

## [Anchor to Fields](/docs/api/storefront/latest/objects/SellingPlan#fields)Fields

* billingPolicy (SellingPlanBillingPolicy)
* checkoutCharge (SellingPlanCheckoutCharge!)
* deliveryPolicy (SellingPlanDeliveryPolicy)
* description (String)
* id (ID!)
* metafield (Metafield)
* metafields ([Metafield]!)
* name (String!)
* options ([SellingPlanOption!]!)
* priceAdjustments ([SellingPlanPriceAdjustment!]!)
* recurringDeliveries (Boolean!)

[Anchor to billingPolicy](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.billingPolicy)billingPolicy •[SellingPlanBillingPolicy](/docs/api/storefront/latest/unions/SellingPlanBillingPolicy)
:   The billing policy for the selling plan.

    Show union types

[Anchor to checkoutCharge](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.checkoutCharge)checkoutCharge •[SellingPlanCheckoutCharge!](/docs/api/storefront/latest/objects/SellingPlanCheckoutCharge) non-null
:   The initial payment due for the purchase.

    Show fields

[Anchor to deliveryPolicy](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.deliveryPolicy)deliveryPolicy •[SellingPlanDeliveryPolicy](/docs/api/storefront/latest/unions/SellingPlanDeliveryPolicy)
:   The delivery policy for the selling plan.

    Show union types

[Anchor to description](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.description)description •[String](/docs/api/storefront/latest/scalars/String)
:   The description of the selling plan.

[Anchor to id](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to metafield](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to name](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.name)name •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

[Anchor to options](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.options)options •[[SellingPlanOption!]!](/docs/api/storefront/latest/objects/SellingPlanOption) non-null
:   The selling plan options available in the drop-down list in the storefront. For example, 'Delivery every week' or 'Delivery every 2 weeks' specifies the delivery frequency options for the product. Individual selling plans contribute their options to the associated selling plan group. For example, a selling plan group might have an option called `option1: Delivery every`. One selling plan in that group could contribute `option1: 2 weeks` with the pricing for that option, and another selling plan could contribute `option1: 4 weeks`, with different pricing.

    Show fields

[Anchor to priceAdjustments](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.priceAdjustments)priceAdjustments •[[SellingPlanPriceAdjustment!]!](/docs/api/storefront/latest/objects/SellingPlanPriceAdjustment) non-null
:   The price adjustments that a selling plan makes when a variant is purchased with a selling plan.

    Show fields

[Anchor to recurringDeliveries](/docs/api/storefront/latest/objects/SellingPlan#field-SellingPlan.fields.recurringDeliveries)recurringDeliveries •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Whether purchasing the selling plan will result in multiple deliveries.

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/SellingPlan#interfaces)Interfaces

* HasMetafields

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/SellingPlan#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

---

Was this section helpful?

YesNo