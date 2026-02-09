---
source: https://shopify.dev/docs/api/liquid/filters/money_without_trailing_zeros
---

9

1

number | money\_without\_trailing\_zeros

returns [string](/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), excluding the decimal separator
(either `.` or `,`) and trailing zeros.

If the price has a non-zero decimal value, then the output is the same as the [`money` filter](/docs/api/liquid/filters#money).

9

1

{{ product.price | money\_without\_trailing\_zeros }}

##### Code

```liquid
{{ product.price | money_without_trailing_zeros }}
```

##### Data

```liquid
{
  "product": {
    "price": "10.00"
  }
}
```

## Output

9

1

$10

##### Output

```liquid
$10
```

Was this page helpful?

YesNo