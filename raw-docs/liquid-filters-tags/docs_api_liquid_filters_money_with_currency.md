---
source: https://shopify.dev/docs/api/liquid/filters/money_with_currency
---

9

1

number | money\_with\_currency

returns [string](/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

9

1

{{ product.price | money\_with\_currency }}

##### Code

```liquid
{{ product.price | money_with_currency }}
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

$10.00 CAD

##### Output

```liquid
$10.00 CAD
```

Was this page helpful?

YesNo