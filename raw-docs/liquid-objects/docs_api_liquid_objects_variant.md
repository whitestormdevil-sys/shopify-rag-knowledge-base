---
source: https://shopify.dev/docs/api/liquid/objects/variant
---

A [product variant](https://help.shopify.com/manual/products/variants).

## Properties

[Anchor to](/docs/api/liquid/objects/variant#variant-available) 

available**available** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant is available. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/variant#variant-barcode) 

barcode**barcode** [string](/docs/api/liquid/basics#string)

:   The barcode of the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-compare_at_price) 

compare\_at\_price**compare\_at\_price** [number](/docs/api/liquid/basics#number)

:   The **compare at** price of the variant in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/variant#variant-featured_image) 

featured\_image**featured\_image** [image](/docs/api/liquid/objects/image)

:   The image attached to the variant.

    Note

    This is the same value as [`variant.image`](/docs/api/liquid/objects/variant#variant-image).

    **Note:**

    This is the same value as [`variant.image`](/docs/api/liquid/objects/variant#variant-image).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/variant#variant-image"><code>variant.image</code></a>.

[Anchor to](/docs/api/liquid/objects/variant#variant-featured_media) 

featured\_media**featured\_media** [media](/docs/api/liquid/objects/media)

:   The first media object attached to the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-image) 

image**image** [image](/docs/api/liquid/objects/image)

:   The image attached to the variant.

    Note

    This is the same value as [`variant.featured_image`](/docs/api/liquid/objects/variant#variant-featured_image).

    **Note:**

    This is the same value as [`variant.featured_image`](/docs/api/liquid/objects/variant#variant-featured_image).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/variant#variant-featured\_image"><code><span class="PreventFireFoxApplyingGapToWBR">variant.featured<wbr/>\_image</span></code></a>.

[Anchor to](/docs/api/liquid/objects/variant#variant-incoming) 

incoming**incoming** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant has incoming inventory. Returns `false` if not.

    Incoming inventory information is populated by [inventory transfers](https://help.shopify.com/manual/products/inventory/transfers),
    [purchase orders](https://help.shopify.com/manual/products/inventory/purchase-orders), and
    [third-party apps](/docs/apps/fulfillment/inventory-management-apps).

[Anchor to](/docs/api/liquid/objects/variant#variant-inventory_management) 

inventory\_management**inventory\_management** [string](/docs/api/liquid/basics#string)

:   The inventory management service of the variant.

    If inventory isn't tracked, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/variant#variant-inventory_policy) 

inventory\_policy**inventory\_policy** [string](/docs/api/liquid/basics#string) from a set of values

:   Whether the variant should continue to be sold when it's out of stock.

    Tip

    To learn about why merchants might want to continue selling products when they're out of stock, visit the
    [Shopify Help Center](https://help.shopify.com/manual/products/inventory/getting-started-with-inventory/selling-when-out-of-stock).

    **Tip:**

    To learn about why merchants might want to continue selling products when they're out of stock, visit the
    [Shopify Help Center](https://help.shopify.com/manual/products/inventory/getting-started-with-inventory/selling-when-out-of-stock).

    **Tip:** To learn about why merchants might want to continue selling products when they&#39;re out of stock, visit the
    <a href="https://help.shopify.com/manual/products/inventory/getting-started-with-inventory/selling-when-out-of-stock">Shopify Help Center</a>.

    | Possible values | Description |
    | --- | --- |
    | continue | Continue selling when the variant is out of stock. |
    | deny | Stop selling when the variant is out of stock. |

[Anchor to](/docs/api/liquid/objects/variant#variant-inventory_quantity) 

inventory\_quantity**inventory\_quantity** [number](/docs/api/liquid/basics#number)

:   The inventory quantity of the variant.

    If inventory isn't tracked, then the number of items sold is returned.

[Anchor to](/docs/api/liquid/objects/variant#variant-matched) 

matched**matched** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant has been matched by a [storefront filter](https://shopify.dev/themes/navigation-search/filtering/storefront-filtering)
    or no filters are applied.
    Returns `false` if it hasn't.

[Anchor to](/docs/api/liquid/objects/variant#variant-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the variant.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/variant#variant-next_incoming_date) 

next\_incoming\_date**next\_incoming\_date** [string](/docs/api/liquid/basics#string)

:   The arrival date for the next incoming inventory of the variant.

    Incoming inventory information is populated by [inventory transfers](https://help.shopify.com/manual/products/inventory/transfers),
    [purchase orders](https://help.shopify.com/manual/products/inventory/purchase-orders), and
    [third-party apps](/docs/apps/fulfillment/inventory-management-apps).

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the date.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the date.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the date.

[Anchor to](/docs/api/liquid/objects/variant#variant-options) 

options**options** [product\_option\_value](/docs/api/liquid/objects/product_option_value)

:   The values of the variant for each [product option](/docs/api/liquid/objects/product_option).

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the options of each variant

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

    {% for variant in product.variants -%}

    {%- capture options -%}

    {% for option in variant.options -%}

    {{ option }}{%- unless forloop.last -%}/{%- endunless -%}

    {%- endfor %}

    {%- endcapture -%}

    {{ variant.id }}: {{ options }}

    {%- endfor %}

    ##### Code

    ```liquid
    {% for variant in product.variants -%}
      {%- capture options -%}
        {% for option in variant.options -%}
          {{ option }}{%- unless forloop.last -%}/{%- endunless -%}
        {%- endfor %}
      {%- endcapture -%}
      
      {{ variant.id }}: {{ options }}
    {%- endfor %}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "variants": [
          {
            "id": 39897499729985,
            "options": [
              "S",
              "Low"
            ]
          },
          {
            "id": 39897499762753,
            "options": [
              "S",
              "Medium"
            ]
          },
          {
            "id": 39897499795521,
            "options": [
              "S",
              "High"
            ]
          },
          {
            "id": 39897499828289,
            "options": [
              "M",
              "Low"
            ]
          },
          {
            "id": 39897499861057,
            "options": [
              "M",
              "Medium"
            ]
          },
          {
            "id": 39897499893825,
            "options": [
              "M",
              "High"
            ]
          },
          {
            "id": 39897499926593,
            "options": [
              "L",
              "Low"
            ]
          },
          {
            "id": 39897499959361,
            "options": [
              "L",
              "Medium"
            ]
          },
          {
            "id": 39897499992129,
            "options": [
              "L",
              "High"
            ]
          }
        ]
      }
    }
    ```

    ## Output

    99

    1

    2

    3

    4

    5

    6

    7

    8

    9

    10

    11

    12

    13

    14

    15

    16

    17

    39897499729985: S/Low

    39897499762753: S/Medium

    39897499795521: S/High

    39897499828289: M/Low

    39897499861057: M/Medium

    39897499893825: M/High

    39897499926593: L/Low

    39897499959361: L/Medium

    39897499992129: L/High

    ##### Output

    ```liquid
    39897499729985: S/Low

    39897499762753: S/Medium

    39897499795521: S/High

    39897499828289: M/Low

    39897499861057: M/Medium

    39897499893825: M/High

    39897499926593: L/Low

    39897499959361: L/Medium

    39897499992129: L/High
    ```

[Anchor to](/docs/api/liquid/objects/variant#variant-price) 

price**price** [number](/docs/api/liquid/basics#number)

:   The price of the variant in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/variant#variant-product) 

product**product** [product](/docs/api/liquid/objects/product)

:   The parent product of the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-quantity_price_breaks) 

quantity\_price\_breaks**quantity\_price\_breaks** array of [quantity\_price\_break](/docs/api/liquid/objects/quantity_price_break)

:   Returns `quantity_price_break` objects for the variant in the current customer context.

[Anchor to](/docs/api/liquid/objects/variant#variant-quantity_price_breaks_configured?) 

quantity\_price\_breaks\_configured?**quantity\_price\_breaks\_configured?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant has any quantity price breaks available in the current customer context.
    Returns `false` if it doesn't.

[Anchor to](/docs/api/liquid/objects/variant#variant-quantity_rule) 

quantity\_rule**quantity\_rule** [quantity\_rule](/docs/api/liquid/objects/quantity_rule)

:   The quantity rule for the variant.

    If no rule exists, then a default value is returned.

    This rule can be set as part of a [B2B catalog](https://help.shopify.com/manual/b2b/catalogs/quantity-pricing).

    Note

    The default quantity rule is `min=1,max=null,increment=1`.

    **Note:**

    The default quantity rule is `min=1,max=null,increment=1`.

    **Note:** The default quantity rule is <code>min=1,max=null,increment=1</code>.

[Anchor to](/docs/api/liquid/objects/variant#variant-requires_selling_plan) 

requires\_selling\_plan**requires\_selling\_plan** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant's product is set to require a `selling_plan` when being added to the cart. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/variant#variant-requires_shipping) 

requires\_shipping**requires\_shipping** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant requires shipping. Returns `false` if it doesn't.

[Anchor to](/docs/api/liquid/objects/variant#variant-selected) 

selected**selected** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant is currently selected. Returns `false` if it's not.

    Note

    The selected variant is determined by the `variant` URL parameter. This URL parameter is available on product pages URLs only.

    **Note:**

    The selected variant is determined by the `variant` URL parameter. This URL parameter is available on product pages URLs only.

    **Note:** The selected variant is determined by the <code>variant</code> URL parameter. This URL parameter is available on product pages URLs only.

[Anchor to](/docs/api/liquid/objects/variant#variant-selected_selling_plan_allocation) 

selected\_selling\_plan\_allocation**selected\_selling\_plan\_allocation** [selling\_plan\_allocation](/docs/api/liquid/objects/selling_plan_allocation)

:   The selected `selling_plan_allocation`.

    If no selling plan is selected, then `nil` is returned.

    Note

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:**

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:** The selected selling plan is determined by the <code><span class="PreventFireFoxApplyingGapToWBR">selling<wbr/>\_plan</span></code> URL parameter.

[Anchor to](/docs/api/liquid/objects/variant#variant-selling_plan_allocations) 

selling\_plan\_allocations**selling\_plan\_allocations** array of [selling\_plan\_allocation](/docs/api/liquid/objects/selling_plan_allocation)

:   The `selling_plan_allocation` objects for the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-sku) 

sku**sku** [string](/docs/api/liquid/basics#string)

:   The SKU of the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-store_availabilities) 

store\_availabilities**store\_availabilities** array of [store\_availability](/docs/api/liquid/objects/store_availability)

:   The store availabilities for the variant.

    The array is defined in only the following cases:

    * `variant.selected` is `true`
    * The variant is the product's first available variant. For example, `product.first_available_variant` or `product.selected_or_first_available_variant`.

[Anchor to](/docs/api/liquid/objects/variant#variant-taxable) 

taxable**taxable** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if taxes should be charged on the variant. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/variant#variant-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   A concatenation of each variant option, separated by a `/`.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    The variant title

    9

    1

    {{ product.variants.first.title }}

    ##### Code

    ```liquid
    {{ product.variants.first.title }}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "variants": [
          {
            "title": "S / Low"
          },
          {
            "title": "S / Medium"
          },
          {
            "title": "S / High"
          },
          {
            "title": "M / Low"
          },
          {
            "title": "M / Medium"
          },
          {
            "title": "M / High"
          },
          {
            "title": "L / Low"
          },
          {
            "title": "L / Medium"
          },
          {
            "title": "L / High"
          }
        ]
      }
    }
    ```

    ## Output

    9

    1

    S / Low

    ##### Output

    ```liquid
    S / Low
    ```

[Anchor to](/docs/api/liquid/objects/variant#variant-unit_price) 

unit\_price**unit\_price** [number](/docs/api/liquid/basics#number)

:   The [unit price](https://help.shopify.com/manual/products/details/product-pricing/unit-pricing#add-unit-prices-to-your-product)
    of the variant in the currency's subunit.

    The price reflects any discounts that are applied to the line item. The value is output in the customer's local
    (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use the [`unit_price_with_measurement` filter](/docs/api/liquid/filters/unit_price_with_measurement) with this
    property and the `variant.unit_price_measurement` property to output a formatted unit price with measurement.

    **Tip:**

    Use the [`unit_price_with_measurement` filter](/docs/api/liquid/filters/unit_price_with_measurement) with this
    property and the `variant.unit_price_measurement` property to output a formatted unit price with measurement.

    **Tip:** Use the <a href="/docs/api/liquid/filters/unit\_price\_with\_measurement"><code><span class="PreventFireFoxApplyingGapToWBR">unit<wbr/>\_price<wbr/>\_with<wbr/>\_measurement</span></code> filter</a> with this
    property and the <code><span class="PreventFireFoxApplyingGapToWBR">variant.unit<wbr/>\_price<wbr/>\_measurement</span></code> property to output a formatted unit price with measurement.

    To learn about how to display unit prices in your theme, refer to [Unit pricing](/themes/pricing-payments/unit-pricing).

[Anchor to](/docs/api/liquid/objects/variant#variant-unit_price_measurement) 

unit\_price\_measurement**unit\_price\_measurement** [unit\_price\_measurement](/docs/api/liquid/objects/unit_price_measurement)

:   The unit price measurement of the variant.

    To learn about how to display unit prices in your theme, refer to [Unit pricing](/themes/pricing-payments/unit-pricing).

    Tip

    Use the [`unit_price_with_measurement` filter](/docs/api/liquid/filters/unit_price_with_measurement) with the
    `variant.unit_price` property and this property to output a formatted unit price with measurement.

    **Tip:**

    Use the [`unit_price_with_measurement` filter](/docs/api/liquid/filters/unit_price_with_measurement) with the
    `variant.unit_price` property and this property to output a formatted unit price with measurement.

    **Tip:** Use the <a href="/docs/api/liquid/filters/unit\_price\_with\_measurement"><code><span class="PreventFireFoxApplyingGapToWBR">unit<wbr/>\_price<wbr/>\_with<wbr/>\_measurement</span></code> filter</a> with the
    <code><span class="PreventFireFoxApplyingGapToWBR">variant.unit<wbr/>\_price</span></code> property and this property to output a formatted unit price with measurement.

[Anchor to](/docs/api/liquid/objects/variant#variant-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The URL of the variant.

    Variant URLs use the following structure:

    ```liquid
    /products/[product-handle]?variant=[variant-id]
    ```

[Anchor to](/docs/api/liquid/objects/variant#variant-weight) 

weight**weight** [number](/docs/api/liquid/basics#number)

:   The weight of the variant in grams.

    Tip

    Use the [`weight_with_unit`](/docs/api/liquid/filters/weight_with_unit) filter to format the weight in
    [the store's format](https://www.shopify.com/admin/settings/general).

    Use `variant.weight_in_unit` to output the weight in the unit configured on the variant.

    **Tip:**

    Use the [`weight_with_unit`](/docs/api/liquid/filters/weight_with_unit) filter to format the weight in
    [the store's format](https://www.shopify.com/admin/settings/general).

    Use `variant.weight_in_unit` to output the weight in the unit configured on the variant.

    **Tip:** Use the <a href="/docs/api/liquid/filters/weight\_with\_unit"><code><span class="PreventFireFoxApplyingGapToWBR">weight<wbr/>\_with<wbr/>\_unit</span></code></a> filter to format the weight in
    <a href="https://www.shopify.com/admin/settings/general">the store&#39;s format</a>.</p>
    <p>Use <code><span class="PreventFireFoxApplyingGapToWBR">variant.weight<wbr/>\_in<wbr/>\_unit</span></code> to output the weight in the unit configured on the variant.

[Anchor to](/docs/api/liquid/objects/variant#variant-weight_in_unit) 

weight\_in\_unit**weight\_in\_unit** [number](/docs/api/liquid/basics#number)

:   The weight of the variant in the unit specified by `variant.weight_unit`.

    Tip

    To output this weight, use this property, and the `variant.weight_unit` property, with the [`weight_with_unit` filter](/docs/api/liquid/filters/weight_with_unit).

    **Tip:**

    To output this weight, use this property, and the `variant.weight_unit` property, with the [`weight_with_unit` filter](/docs/api/liquid/filters/weight_with_unit).

    **Tip:** To output this weight, use this property, and the <code><span class="PreventFireFoxApplyingGapToWBR">variant.weight<wbr/>\_unit</span></code> property, with the <a href="/docs/api/liquid/filters/weight\_with\_unit"><code><span class="PreventFireFoxApplyingGapToWBR">weight<wbr/>\_with<wbr/>\_unit</span></code> filter</a>.

[Anchor to](/docs/api/liquid/objects/variant#variant-weight_unit) 

weight\_unit**weight\_unit** [string](/docs/api/liquid/basics#string)

:   The unit for the weight of the variant.

    Tip

    To output the weight of a variant in this unit, use this property, and the `variant.weight_in_unit` property, with the
    [`weight_with_unit` filter](/docs/api/liquid/filters/weight_with_unit).

    **Tip:**

    To output the weight of a variant in this unit, use this property, and the `variant.weight_in_unit` property, with the
    [`weight_with_unit` filter](/docs/api/liquid/filters/weight_with_unit).

    **Tip:** To output the weight of a variant in this unit, use this property, and the <code><span class="PreventFireFoxApplyingGapToWBR">variant.weight<wbr/>\_in<wbr/>\_unit</span></code> property, with the
    <a href="/docs/api/liquid/filters/weight\_with\_unit"><code><span class="PreventFireFoxApplyingGapToWBR">weight<wbr/>\_with<wbr/>\_unit</span></code> filter</a>.

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/variant#variant-option1) 

option1**option1** [string](/docs/api/liquid/basics#string) Deprecated

:   The value of the variant for the first product option.

    If there's no first product option, then `nil` is returned.

    Deprecated

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

    **Deprecated:**

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

[Anchor to](/docs/api/liquid/objects/variant#variant-option2) 

option2**option2** [string](/docs/api/liquid/basics#string) Deprecated

:   The value of the variant for the second product option.

    If there's no second product option, then `nil` is returned.

    Deprecated

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

    **Deprecated:**

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

[Anchor to](/docs/api/liquid/objects/variant#variant-option3) 

option3**option3** [string](/docs/api/liquid/basics#string) Deprecated

:   The value of the variant for the third product option.

    If there's no third product option, then `nil` is returned.

    Deprecated

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

    **Deprecated:**

    Deprecated. Prefer to use [`variant.options`](/docs/api/liquid/objects/variant#variant-options) instead.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

{

"available": true,

"barcode": "",

"compare\_at\_price": null,

"featured\_image": null,

"featured\_media": null,

"id": 39897499729985,

"image": null,

"incoming": false,

"inventory\_management": "shopify",

"inventory\_policy": "deny",

"inventory\_quantity": 5,

"matched": true,

"metafields": {},

"next\_incoming\_date": null,

"option1": "S",

"option2": "Low",

"option3": null,

"options": [],

"price": "10.00",

"product": {},

"quantity\_price\_breaks": [],

"quantity\_rule": {},

"requires\_selling\_plan": false,

"requires\_shipping": true,

"selected": false,

"selected\_selling\_plan\_allocation": null,

"selling\_plan\_allocations": [],

"sku": "",

"store\_availabilities": [],

"taxable": true,

"title": "S / Low",

"unit\_price": null,

"unit\_price\_measurement": null,

"url": {},

"weight": 500,

"weight\_in\_unit": 500,

"weight\_unit": "g"

}

##### Example

```liquid
{
  "available": true,
  "barcode": "",
  "compare_at_price": null,
  "featured_image": null,
  "featured_media": null,
  "id": 39897499729985,
  "image": null,
  "incoming": false,
  "inventory_management": "shopify",
  "inventory_policy": "deny",
  "inventory_quantity": 5,
  "matched": true,
  "metafields": {},
  "next_incoming_date": null,
  "option1": "S",
  "option2": "Low",
  "option3": null,
  "options": [],
  "price": "10.00",
  "product": {},
  "quantity_price_breaks": [],
  "quantity_rule": {},
  "requires_selling_plan": false,
  "requires_shipping": true,
  "selected": false,
  "selected_selling_plan_allocation": null,
  "selling_plan_allocations": [],
  "sku": "",
  "store_availabilities": [],
  "taxable": true,
  "title": "S / Low",
  "unit_price": null,
  "unit_price_measurement": null,
  "url": {},
  "weight": 500,
  "weight_in_unit": 500,
  "weight_unit": "g"
}
```

Was this section helpful?

YesNo