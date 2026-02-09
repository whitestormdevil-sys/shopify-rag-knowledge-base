---
source: https://shopify.dev/docs/api/liquid/objects/shipping_method
---

Information about the shipping method for an order.

## Properties

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-discount_allocations) 

discount\_allocations**discount\_allocations** array of [discount\_allocation](/docs/api/liquid/objects/discount_allocation)

:   The discount allocations that apply to the shipping method.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the shipping method.

    Note

    The price of the shipping method is appended to handle.

    **Note:**

    The price of the shipping method is appended to handle.

    **Note:** The price of the shipping method is appended to handle.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-id) 

id**id** [string](/docs/api/liquid/basics#string)

:   The ID of the shipping method.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-original_price) 

original\_price**original\_price** [number](/docs/api/liquid/basics#number)

:   The price of the shipping method in the currency's subunit, before discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-price_with_discounts) 

price\_with\_discounts**price\_with\_discounts** [number](/docs/api/liquid/basics#number)

:   The price of the shipping method in the currency's subunit, after discounts have been applied, including order level discounts.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-tax_lines) 

tax\_lines**tax\_lines** array of [tax\_line](/docs/api/liquid/objects/tax_line)

:   The tax lines for the shipping method.

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the shipping method.

    In most contexts, the shipping method title appears in the customer's preferred language. However, in the context of an
    [order](/docs/api/liquid/objects/order), the shipping method title appears in the language that the customer checked out in.

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/shipping_method#shipping_method-price) 

price**price** [number](/docs/api/liquid/basics#number) Deprecated

:   The price of the shipping method in the currency's subunit, after discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

    Deprecated

    Deprecated because the price did not include order level discounts.

    The `shipping_line.price` property has been replaced by [`shipping_line.price_with_discounts`](/docs/api/liquid/objects/shipping_method#shipping_method-price_with_discounts).

    **Deprecated:**

    Deprecated because the price did not include order level discounts.

    The `shipping_line.price` property has been replaced by [`shipping_line.price_with_discounts`](/docs/api/liquid/objects/shipping_method#shipping_method-price_with_discounts).

9

1

2

3

4

5

6

7

8

9

{

"handle": "shopify-Standard-0.00",

"id": "shopify-Standard-0.00",

"original\_price": "0.00",

"price": "0.00",

"price\_with\_discounts": "0.00",

"tax\_lines": [],

"title": "Standard"

}

##### Example

```liquid
{
  "handle": "shopify-Standard-0.00",
  "id": "shopify-Standard-0.00",
  "original_price": "0.00",
  "price": "0.00",
  "price_with_discounts": "0.00",
  "tax_lines": [],
  "title": "Standard"
}
```

Was this section helpful?

YesNo