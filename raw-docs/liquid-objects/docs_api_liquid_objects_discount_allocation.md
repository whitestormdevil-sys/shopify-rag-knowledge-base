---
source: https://shopify.dev/docs/api/liquid/objects/discount_allocation
---

Information about how a discount affects an item.

To learn about how to display discounts in your theme, refer to [Discounts](/themes/pricing-payments/discounts).

## Properties

[Anchor to](/docs/api/liquid/objects/discount_allocation#discount_allocation-amount) 

amount**amount** [number](/docs/api/liquid/basics#number)

:   The amount that the item is discounted by in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount_allocation#discount_allocation-discount_application) 

discount\_application**discount\_application** [discount\_application](/docs/api/liquid/objects/discount_application)

:   The discount application that applies the discount to the item.

9

1

2

3

4

{

"amount": "40.00",

"discount\_application": "DiscountApplicationDrop"

}

##### Example

```liquid
{
  "amount": "40.00",
  "discount_application": "DiscountApplicationDrop"
}
```

Was this section helpful?

YesNo