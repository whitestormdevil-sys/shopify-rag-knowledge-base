---
source: https://shopify.dev/docs/api/liquid/filters/money_without_currency
---

9

1

number | money\_without\_currency

returns [string](/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting), without the currency symbol.

9

1

{{ product.price | money\_without\_currency }}

##### Code

```liquid
{{ product.price | money_without_currency }}
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

10.00

##### Output

```liquid
10.00
```

Was this page helpful?

YesNo