---
source: https://shopify.dev/docs/api/liquid/filters/money
---

9

1

number | money

returns [string](/docs/api/liquid/basics#string)

Formats a given price based on the store's [**HTML without currency** setting](https://help.shopify.com/manual/payments/currency-formatting).

9

1

{{ product.price | money }}

##### Code

```liquid
{{ product.price | money }}
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

$10.00

##### Output

```liquid
$10.00
```

Was this page helpful?

YesNo