---
source: https://shopify.dev/docs/api/liquid/objects/selling_plan_allocation
---

Information about how a specific [selling plan](/apps/subscriptions/selling-plans) affects a line item.

To learn about how to support selling plans in your theme, refer to [Purchase options](/themes/pricing-payments/purchase-options).

## Properties

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-checkout_charge_amount) 

checkout\_charge\_amount**checkout\_charge\_amount** [number](/docs/api/liquid/basics#number)

:   The amount that the customer will be charged at checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-compare_at_price) 

compare\_at\_price**compare\_at\_price** [number](/docs/api/liquid/basics#number)

:   The **compare at** price of the selling plan allocation in the currency's subunit.

    The value of the **compare at** price is the line item's price without the selling plan applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-per_delivery_price) 

per\_delivery\_price**per\_delivery\_price** [number](/docs/api/liquid/basics#number)

:   The price for each delivery in the selling plan in the currency's subunit.

    If a selling plan includes multiple deliveries, then the `per_delivery_price` is the `price` divided by the number of
    deliveries.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price) 

price**price** [number](/docs/api/liquid/basics#number)

:   The price of the selling plan allocation in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-price_adjustments) 

price\_adjustments**price\_adjustments** array of [selling\_plan\_allocation\_price\_adjustment](/docs/api/liquid/objects/selling_plan_allocation_price_adjustment)

:   The selling plan allocation price adjustments.

    The maximum length of the array is two. If the associated selling plan doesn't create any price adjustments, then the
    array is empty.

    Each `selling_plan_allocation_price_adjustment` maps to a [`selling_plan_price_adjustment`](/docs/api/liquid/objects/selling_plan_price_adjustment)
    in the [`selling_plan.price_adjustments` array](/docs/api/liquid/objects/selling_plan#selling_plan-price_adjustments). The
    `selling_plan.price_adjustments` array contains the intent of the selling plan, and the
    `selling_plan_allocation.price_adjustments` array contains the resulting money amounts.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-remaining_balance_charge_amount) 

remaining\_balance\_charge\_amount**remaining\_balance\_charge\_amount** [number](/docs/api/liquid/basics#number)

:   The remaining amount for the customer to pay, in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-selling_plan) 

selling\_plan**selling\_plan** [selling\_plan](/docs/api/liquid/objects/selling_plan)

:   The selling plan that created the allocation.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-selling_plan_group_id) 

selling\_plan\_group\_id**selling\_plan\_group\_id** [string](/docs/api/liquid/basics#string)

:   The ID of the [`selling_plan_group`](/docs/api/liquid/objects/selling_plan_group) that the selling plan of the allocation belongs to.

[Anchor to](/docs/api/liquid/objects/selling_plan_allocation#selling_plan_allocation-unit_price) 

unit\_price**unit\_price** [number](/docs/api/liquid/basics#number)

:   The [unit price](/docs/api/liquid/objects/variant#variant-unit_price) of the variant associated with the selling plan, in the currency's subunit.

    If the variant doesn't have a unit price, then `nil` is returned.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

### Returned by

* [line\_item.selling\_plan\_allocation](/docs/api/liquid/objects/line_item#line_item-selling_plan_allocation)
* [variant.selling\_plan\_allocations](/docs/api/liquid/objects/variant#variant-selling_plan_allocations)
* [product.selected\_selling\_plan\_allocation](/docs/api/liquid/objects/product#product-selected_selling_plan_allocation)
* [product.selected\_or\_first\_available\_selling\_plan\_allocation](/docs/api/liquid/objects/product#product-selected_or_first_available_selling_plan_allocation)
* [variant.selected\_selling\_plan\_allocation](/docs/api/liquid/objects/variant#variant-selected_selling_plan_allocation)
* [remote\_product.selected\_selling\_plan\_allocation](/docs/api/liquid/objects/remote_product#remote_product-selected_selling_plan_allocation)
* [remote\_product.selected\_or\_first\_available\_selling\_plan\_allocation](/docs/api/liquid/objects/remote_product#remote_product-selected_or_first_available_selling_plan_allocation)

Was this section helpful?

YesNo