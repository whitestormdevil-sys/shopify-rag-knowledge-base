---
source: https://shopify.dev/docs/api/liquid/filters/weight_with_unit
---

9

1

number | weight\_with\_unit

returns [string](/docs/api/liquid/basics#string)

Generates a formatted weight for a [`variant` object](/docs/api/liquid/objects/variant#variant-weight). The weight unit is
set in the [general settings](https://www.shopify.com/admin/settings/general) in the Shopify admin.

9

1

2

3

{%- assign variant = product.variants.first -%}

{{ variant.weight | weight\_with\_unit }}

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit }}
```

##### Data

```liquid
{
  "product": {
    "variants": [
      {
        "weight": 200
      },
      {
        "weight": 200
      },
      {
        "weight": 400
      },
      {
        "weight": 200
      }
    ]
  }
}
```

## Output

9

1

0.2 kg

##### Output

```liquid
0.2 kg
```

[Anchor to Override the default unit](/docs/api/liquid/filters/weight_with_unit#weight_with_unit-override-the-default-unit)

### Override the default unit

9

1

number | weight\_with\_unit: variable

You can specify a unit to override the default from the general settings.

9

1

2

3

{%- assign variant = product.variants.first -%}

{{ variant.weight | weight\_with\_unit: variant.weight\_unit }}

##### Code

```liquid
{%- assign variant = product.variants.first -%}

{{ variant.weight | weight_with_unit: variant.weight_unit }}
```

##### Data

```liquid
{
  "product": {
    "variants": [
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      },
      {
        "weight": 400,
        "weight_unit": "g"
      },
      {
        "weight": 200,
        "weight_unit": "g"
      }
    ]
  }
}
```

## Output

9

1

200 g

##### Output

```liquid
200 g
```

Was this page helpful?

YesNo