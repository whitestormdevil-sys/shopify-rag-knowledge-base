---
source: https://shopify.dev/docs/api/liquid/filters/default
---

9

1

variable | default: variable

Sets a default value for any variable whose value is one of the following:

* [`empty`](/docs/api/liquid/basics#empty)
* [`false`](/docs/api/liquid/basics#truthy-and-falsy)
* [`nil`](/docs/api/liquid/basics#nil)

9

1

{{ product.selected\_variant.url | default: product.url }}

##### Code

```liquid
{{ product.selected_variant.url | default: product.url }}
```

##### Data

```liquid
{
  "product": {
    "selected_variant": null,
    "url": "/products/health-potion"
  }
}
```

## Output

9

1

/products/health-potion

##### Output

```liquid
/products/health-potion
```

[Anchor to allow\_false](/docs/api/liquid/filters/default#default-allow_false)

### allow\_false

9

1

variable | default: variable, allow\_false: boolean

By default, the `default` filter's value will be used in place of `false` values. You can use the `allow_false` parameter to allow variables to return `false` instead of the default value.

9

1

2

3

{%- assign display\_price = false -%}

{{ display\_price | default: true, allow\_false: true }}

##### Code

```liquid
{%- assign display_price = false -%}

{{ display_price | default: true, allow_false: true }}
```

## Output

9

1

false

##### Output

```liquid
false
```

Was this page helpful?

YesNo