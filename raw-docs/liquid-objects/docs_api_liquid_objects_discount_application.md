---
source: https://shopify.dev/docs/api/liquid/objects/discount_application
---

Information about the intent of a discount.

To learn about how to display discounts in your theme, refer to [Discounts](/themes/pricing-payments/discounts).

## Properties

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-target_selection) 

target\_selection**target\_selection** [string](/docs/api/liquid/basics#string) from a set of values

:   The selection method for line items or shipping lines to be discounted.

    Note

    Whether the selection method applies to line items or shipping lines depends on the discount's
    [target type](/docs/api/liquid/objects/discount_application#discount_application-target_type).

    **Note:**

    Whether the selection method applies to line items or shipping lines depends on the discount's
    [target type](/docs/api/liquid/objects/discount_application#discount_application-target_type).

    **Note:** Whether the selection method applies to line items or shipping lines depends on the discount&#39;s
    <a href="/docs/api/liquid/objects/discount\_application#discount\_application-target\_type">target type</a>.

    | Possible values | Description |
    | --- | --- |
    | all | The discount applies to all line items or shipping lines. |
    | entitled | The discount applies to a specific set of line items or shipping lines based on some criteria. |
    | explicit | The discount applies to a specific line item or shipping line. |

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-target_type) 

target\_type**target\_type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of item that the discount applies to.

    | Possible values |
    | --- |
    | line\_item |
    | shipping\_line |

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The customer-facing name of the discount.

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-total_allocated_amount) 

total\_allocated\_amount**total\_allocated\_amount** [number](/docs/api/liquid/basics#number)

:   The total amount of the discount in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-type) 

type**type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of the discount.

    | Possible values |
    | --- |
    | automatic |
    | discount\_code |
    | manual |
    | script |

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-value) 

value**value** [number](/docs/api/liquid/basics#number)

:   The value of the discount.

    How this value is interpreted depends on the [value type](/docs/api/liquid/objects/discount_application#discount_application-value_type) of the
    discount. The following table outlines what the value represents for each value type:

    | Value type | Value |
    | --- | --- |
    | `fixed_amount` | The amount of the discount in the currency's subunit. |
    | `percentage` | The percent amount of the discount. |

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/discount_application#discount_application-value_type) 

value\_type**value\_type** [string](/docs/api/liquid/basics#string) from a set of values

:   The value type of the discount.

    | Possible values |
    | --- |
    | fixed\_amount |
    | percentage |

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

"target\_selection": "explicit",

"target\_type": "line\_item",

"title": "Bloodroot discount!",

"total\_allocated\_amount": "2.50",

"type": "script",

"value": "2.5",

"value\_type": "fixed\_amount"

}

##### Example

```liquid
{
  "target_selection": "explicit",
  "target_type": "line_item",
  "title": "Bloodroot discount!",
  "total_allocated_amount": "2.50",
  "type": "script",
  "value": "2.5",
  "value_type": "fixed_amount"
}
```

Was this section helpful?

YesNo