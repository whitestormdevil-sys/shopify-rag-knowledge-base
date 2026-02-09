---
source: https://shopify.dev/docs/api/liquid/filters/prepend
---

9

1

string | prepend: string

returns [string](/docs/api/liquid/basics#string)

Adds a given string to the beginning of a string.

9

1

2

3

{%- assign origin = request.origin -%}

{{ product.url | prepend: origin }}

##### Code

```liquid
{%- assign origin = request.origin -%}

{{ product.url | prepend: origin }}
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