---
source: https://shopify.dev/docs/api/liquid/objects/quantity_rule
---

A variant order quantity rule.

If no rule exists, then a default value is returned.

This rule can be set as part of a [B2B catalog](https://help.shopify.com/manual/b2b/catalogs/quantity-pricing).

---

Note

The default quantity rule is `min=1,max=null,increment=1`.

**Note:**

The default quantity rule is `min=1,max=null,increment=1`.

**Note:** The default quantity rule is <code>min=1,max=null,increment=1</code>.

---

## Properties

[Anchor to](/docs/api/liquid/objects/quantity_rule#quantity_rule-increment) 

increment**increment** [number](/docs/api/liquid/basics#number)

:   The number the order quantity can be incremented by. The default value is `1`.

[Anchor to](/docs/api/liquid/objects/quantity_rule#quantity_rule-max) 

max**max** [number](/docs/api/liquid/basics#number)

:   The maximum order quantity.

    If there is no maximum quantity, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/quantity_rule#quantity_rule-min) 

min**min** [number](/docs/api/liquid/basics#number)

:   The minimum order quantity. The default value is `1`.

9

1

2

3

4

5

{

"min": 5,

"max": 100,

"increment": 5

}

##### Example

```liquid
{
  "min": 5,
  "max": 100,
  "increment": 5
}
```

[Anchor to The variant order quantity rule](/docs/api/liquid/objects/quantity_rule#quantity_rule-the-variant-order-quantity-rule)

### The variant order quantity rule

9

1

{{ product.variants.first.quantity\_rule }}

##### Code

```liquid
{{ product.variants.first.quantity_rule }}
```

##### Data

```liquid
{
  "product": {
    "variants": [
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      },
      {
        "quantity_rule": {
          "min": 1,
          "max": null,
          "increment": 1
        }
      }
    ]
  }
}
```

## Output

9

1

{"min"=>1, "max"=>nil, "increment"=>1}

##### Output

```liquid
{"min"=>1, "max"=>nil, "increment"=>1}
```

Was this section helpful?

YesNo