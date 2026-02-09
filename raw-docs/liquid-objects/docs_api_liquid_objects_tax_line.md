---
source: https://shopify.dev/docs/api/liquid/objects/tax_line
---

Information about a tax line of a checkout or order.

## Properties

[Anchor to](/docs/api/liquid/objects/tax_line#tax_line-price) 

price**price** [number](/docs/api/liquid/basics#number)

:   The tax amount in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/tax_line#tax_line-rate) 

rate**rate** [number](/docs/api/liquid/basics#number)

:   The decimal value of the tax rate.

[Anchor to](/docs/api/liquid/objects/tax_line#tax_line-rate_percentage) 

rate\_percentage**rate\_percentage** [number](/docs/api/liquid/basics#number)

:   The decimal value of the tax rate, as a percentage.

[Anchor to](/docs/api/liquid/objects/tax_line#tax_line-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the tax.

9

1

2

3

4

5

6

{

"price": 1901,

"rate": 0.05,

"rate\_percentage": 5,

"title": "GST"

}

##### Example

```liquid
{
  "price": 1901,
  "rate": 0.05,
  "rate_percentage": 5,
  "title": "GST"
}
```

Was this section helpful?

YesNo