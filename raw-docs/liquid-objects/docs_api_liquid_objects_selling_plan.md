---
source: https://shopify.dev/docs/api/liquid/objects/selling_plan
---

Information about the intent of how a specific [selling plan](/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](/themes/pricing-payments/purchase-options).

## Properties

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-checkout_charge) 

checkout\_charge**checkout\_charge** [selling\_plan\_checkout\_charge](/docs/api/liquid/objects/selling_plan_checkout_charge)

:   The checkout charge of the selling plan.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-description) 

description**description** [string](/docs/api/liquid/basics#string)

:   The description of the selling plan.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-group_id) 

group\_id**group\_id** [string](/docs/api/liquid/basics#string)

:   The ID of the [`selling_plan_group`](/docs/api/liquid/objects/selling_plan_group) that the selling plan belongs to.

    Note

    The name is shown at checkout with the line item summary.

    **Note:**

    The name is shown at checkout with the line item summary.

    **Note:** The name is shown at checkout with the line item summary.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the selling plan.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the selling plan.

    Note

    The name is shown at checkout with the line item summary.

    **Note:**

    The name is shown at checkout with the line item summary.

    **Note:** The name is shown at checkout with the line item summary.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-options) 

options**options** array of [selling\_plan\_option](/docs/api/liquid/objects/selling_plan_option)

:   The selling plan options.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-price_adjustments) 

price\_adjustments**price\_adjustments** array of [selling\_plan\_price\_adjustment](/docs/api/liquid/objects/selling_plan_price_adjustment)

:   The selling plan price adjustments.

    The maximum length of the array is two. If the selling plan doesn't create any price adjustments, then the
    array is empty.

    Each `selling_plan_price_adjustment` maps to a [`selling_plan_allocation_price_adjustment`](/docs/api/liquid/objects/selling_plan_allocation_price_adjustment)
    in the [`selling_plan_allocation.price_adjustments` array](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments).
    The `selling_plan.price_adjustments` array contains the intent of the selling plan, and the
    `selling_plan_allocation.price_adjustments` contains the resulting money amounts.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-recurring_deliveries) 

recurring\_deliveries**recurring\_deliveries** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the selling plan includes multiple deliveries. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/selling_plan#selling_plan-selected) 

selected**selected** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the selling plan is currently selected. Returns `false` if not.

    Note

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:**

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:** The selected selling plan is determined by the <code><span class="PreventFireFoxApplyingGapToWBR">selling<wbr/>\_plan</span></code> URL parameter.

99

1

2

3

4

5

6

7

8

9

10

11

{

"checkout\_charge": {},

"description": null,

"group\_id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",

"id": 2595487809,

"name": "Deliver every week, 10% off",

"options": [],

"price\_adjustments": [],

"recurring\_deliveries": true,

"selected": true

}

##### Example

```liquid
{
  "checkout_charge": {},
  "description": null,
  "group_id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "id": 2595487809,
  "name": "Deliver every week, 10% off",
  "options": [],
  "price_adjustments": [],
  "recurring_deliveries": true,
  "selected": true
}
```

Was this section helpful?

YesNo