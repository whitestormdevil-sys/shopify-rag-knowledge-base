---
source: https://shopify.dev/docs/api/liquid/objects/unit_price_measurement
---

Information about how units of a product variant are measured. It's used to calculate
[unit prices](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product).

## Properties

[Anchor to](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-measured_type) 

measured\_type**measured\_type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of unit measurement.

    | Possible values |
    | --- |
    | volume |
    | weight |
    | length |
    | area |
    | count |

[Anchor to](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-quantity_unit) 

quantity\_unit**quantity\_unit** [string](/docs/api/liquid/basics#string)

:   The unit of measurement used to measure the [`quantity_value`](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-quantity_value).

[Anchor to](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-quantity_value) 

quantity\_value**quantity\_value** [number](/docs/api/liquid/basics#number)

:   The quantity of the unit.

[Anchor to](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-reference_unit) 

reference\_unit**reference\_unit** [string](/docs/api/liquid/basics#string)

:   The unit of measurement used to measure the [`reference_value`](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-reference_value).

[Anchor to](/docs/api/liquid/objects/unit_price_measurement#unit_price_measurement-reference_value) 

reference\_value**reference\_value** [number](/docs/api/liquid/basics#number)

:   The quantity of the unit for the base unit price.

9

1

2

3

4

5

6

7

{

"measured\_type": "weight",

"quantity\_value": "500.0",

"quantity\_unit": "g",

"reference\_value": 1,

"reference\_unit": "kg"

}

##### Example

```liquid
{
  "measured_type": "weight",
  "quantity_value": "500.0",
  "quantity_unit": "g",
  "reference_value": 1,
  "reference_unit": "kg"
}
```

Was this section helpful?

YesNo