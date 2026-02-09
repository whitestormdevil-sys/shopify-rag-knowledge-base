---
source: https://shopify.dev/docs/api/liquid/objects/discount
---

A discount applied to a cart, line item, or order.

deprecated

Deprecated because not all discount types and details are captured.

The `discount` object has been replaced by the [`discount_allocation`](/docs/api/liquid/objects/discount_allocation) and
[`discount_application`](/docs/api/liquid/objects/discount_application) objects.

**deprecated:**

Deprecated because not all discount types and details are captured.

The `discount` object has been replaced by the [`discount_allocation`](/docs/api/liquid/objects/discount_allocation) and
[`discount_application`](/docs/api/liquid/objects/discount_application) objects.

## Properties

[Anchor to](/docs/api/liquid/objects/discount#discount-amount) 

amount**amount** [number](/docs/api/liquid/basics#number)

:   The amount of the discount in the currency's subunit.

    Note

    This is the same value as [`discount.total_amount`](/docs/api/liquid/objects/discount#discount-total_amount).

    **Note:**

    This is the same value as [`discount.total_amount`](/docs/api/liquid/objects/discount#discount-total_amount).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-total\_amount"><code><span class="PreventFireFoxApplyingGapToWBR">discount.total<wbr/>\_amount</span></code></a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount#discount-code) 

code**code** [string](/docs/api/liquid/basics#string)

:   The customer-facing name of the discount.

    Note

    This is the same value as [`discount.title`](/docs/api/liquid/objects/discount#discount-title).

    **Note:**

    This is the same value as [`discount.title`](/docs/api/liquid/objects/discount#discount-title).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-title"><code>discount.title</code></a>.

[Anchor to](/docs/api/liquid/objects/discount#discount-savings) 

savings**savings** [number](/docs/api/liquid/basics#number)

:   The amount of the discount as a negative value, in the currency's subunit.

    Note

    This is the same value as [`discount.total_savings`](/docs/api/liquid/objects/discount#discount-total_savings).
    The value is output in the customer's local (presentment) currency.

    **Note:**

    This is the same value as [`discount.total_savings`](/docs/api/liquid/objects/discount#discount-total_savings).
    The value is output in the customer's local (presentment) currency.

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-total\_savings"><code><span class="PreventFireFoxApplyingGapToWBR">discount.total<wbr/>\_savings</span></code></a>.
    The value is output in the customer&#39;s local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount#discount-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The customer-facing name of the discount.

    Note

    This is the same value as [`discount.code`](/docs/api/liquid/objects/discount#discount-code).

    **Note:**

    This is the same value as [`discount.code`](/docs/api/liquid/objects/discount#discount-code).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-code"><code>discount.code</code></a>.

[Anchor to](/docs/api/liquid/objects/discount#discount-total_amount) 

total\_amount**total\_amount** [number](/docs/api/liquid/basics#number)

:   The amount of the discount in the currency's subunit.

    Note

    This is the same value as [`discount.amount`](/docs/api/liquid/objects/discount#discount-amount).

    **Note:**

    This is the same value as [`discount.amount`](/docs/api/liquid/objects/discount#discount-amount).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-amount"><code>discount.amount</code></a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount#discount-total_savings) 

total\_savings**total\_savings** [number](/docs/api/liquid/basics#number)

:   The amount of the discount as a negative value, in the currency's subunit.

    Note

    This is the same value as [`discount.savings`](/docs/api/liquid/objects/discount#discount-savings).
    The value is output in the customer's local (presentment) currency.

    **Note:**

    This is the same value as [`discount.savings`](/docs/api/liquid/objects/discount#discount-savings).
    The value is output in the customer's local (presentment) currency.

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/discount#discount-savings"><code>discount.savings</code></a>.
    The value is output in the customer&#39;s local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount#discount-type) 

type**type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of the discount.

    | Possible values |
    | --- |
    | FixedAmountDiscount |
    | PercentageDiscount |
    | ShippingDiscount |

9

1

2

3

4

5

6

7

8

9

{

"amount": "40.00",

"code": "DIY",

"savings": "-40.00",

"title": "DIY",

"total\_amount": "40.00",

"total\_savings": "-40.00",

"type": "PercentageDiscount"

}

##### Example

```liquid
{
  "amount": "40.00",
  "code": "DIY",
  "savings": "-40.00",
  "title": "DIY",
  "total_amount": "40.00",
  "total_savings": "-40.00",
  "type": "PercentageDiscount"
}
```

Was this section helpful?

YesNo