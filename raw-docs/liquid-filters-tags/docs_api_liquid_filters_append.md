---
source: https://shopify.dev/docs/api/liquid/filters/append
---

9

1

string | append: string

returns [string](/docs/api/liquid/basics#string)

Adds a given string to the end of a string.

9

1

2

3

{%- assign path = product.url -%}

{{ request.origin | append: path }}

##### Code

```liquid
{%-  assign path = product.url -%}

{{ request.origin | append: path }}
```

##### Data

```liquid
{
  "product": {
    "url": "/products/health-potion"
  },
  "request": {
    "origin": "https://polinas-potent-potions.myshopify.com"
  }
}
```

## Output

9

1

https://polinas-potent-potions.myshopify.com/products/health-potion

##### Output

```liquid
https://polinas-potent-potions.myshopify.com/products/health-potion
```

Was this page helpful?

YesNo