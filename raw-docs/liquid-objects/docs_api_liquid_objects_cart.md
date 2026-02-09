---
source: https://shopify.dev/docs/api/liquid/objects/cart
---

A customer’s cart.

## Properties

[Anchor to](/docs/api/liquid/objects/cart#cart-attributes) 

attributes**attributes**

:   Additional attributes entered by the customer with the cart.

    To learn more about capturing cart attributes, refer to the [`cart` template](/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Capture cart attributes

    To capture a cart attribute, include an HTML input with an attribute of `name="attributes[attribute-name]"` within the cart `<form>`.

    9

    1

    2

    <label>What do you want engraved on your cauldron?</label>

    <input type="text" name="attributes[cauldron-engraving]" value="{{ cart.attributes.cauldron-engraving }}" />

    ```liquid
    What do you want engraved on your cauldron?
    ```

    ---

    Tip

    You can add a double underscore `__` prefix to an attribute name to make it private. Private attributes behave like other cart attributes, except that they can't be read from Liquid or the Ajax API.
    You can use them for data that doesn't affect the page rendering, which allows for more effective page caching.

    **Tip:**

    You can add a double underscore `__` prefix to an attribute name to make it private. Private attributes behave like other cart attributes, except that they can't be read from Liquid or the Ajax API.
    You can use them for data that doesn't affect the page rendering, which allows for more effective page caching.

    **Tip:** You can add a double underscore <code>\_\_</code> prefix to an attribute name to make it private. Private attributes behave like other cart attributes, except that they can&#39;t be read from Liquid or the Ajax API.
    You can use them for data that doesn&#39;t affect the page rendering, which allows for more effective page caching.

    ---

[Anchor to](/docs/api/liquid/objects/cart#cart-cart_level_discount_applications) 

cart\_level\_discount\_applications**cart\_level\_discount\_applications** array of [discount\_application](/docs/api/liquid/objects/discount_application)

:   The cart-specific discount applications for the cart.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Display cart-level discount applications

    9

    1

    2

    3

    4

    {% for discount\_application in cart.cart\_level\_discount\_applications %}

    Discount name: {{ discount\_application.title }}

    Savings: -{{ discount\_application.total\_allocated\_amount | money }}

    {% endfor %}

    ##### Code

    ```liquid
    {% for discount_application in cart.cart_level_discount_applications %}
      Discount name: {{ discount_application.title }}
      Savings: -{{ discount_application.total_allocated_amount | money }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "cart": {
        "cart_level_discount_applications": [
          {
            "title": "Ingredient Sale",
            "total_allocated_amount": "42.24"
          }
        ]
      }
    }
    ```

    ## Output

    9

    1

    2

    Discount name: Ingredient Sale

    Savings: -$42.24

    ##### Output

    ```liquid
    Discount name: Ingredient Sale
      Savings: -$42.24
    ```

[Anchor to](/docs/api/liquid/objects/cart#cart-checkout_charge_amount) 

checkout\_charge\_amount**checkout\_charge\_amount** [number](/docs/api/liquid/basics#number)

:   The amount that the customer will be charged at checkout in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/cart#cart-currency) 

currency**currency**

:   The currency of the cart.

    If the store uses multi-currency, then this is the same as the customer's local
    (presentment) currency. Otherwise, it's the same as the store currency.

    Tip

    You can output the store's available currencies using [`shop.enabled_currencies`](/docs/api/liquid/objects/shop#shop-enabled_currencies).

    **Tip:**

    You can output the store's available currencies using [`shop.enabled_currencies`](/docs/api/liquid/objects/shop#shop-enabled_currencies).

    **Tip:** You can output the store&#39;s available currencies using <a href="/docs/api/liquid/objects/shop#shop-enabled\_currencies"><code><span class="PreventFireFoxApplyingGapToWBR">shop.enabled<wbr/>\_currencies</span></code></a>.

[Anchor to](/docs/api/liquid/objects/cart#cart-discount_applications) 

discount\_applications**discount\_applications** array of [discount\_application](/docs/api/liquid/objects/discount_application)

:   The discount applications for the cart.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Display discount applications

    9

    1

    2

    3

    4

    {% for discount\_application in cart.discount\_applications %}

    Discount name: {{ discount\_application.title }}

    Savings: -{{ discount\_application.total\_allocated\_amount | money }}

    {% endfor %}

    ##### Code

    ```liquid
    {% for discount_application in cart.discount_applications %}
      Discount name: {{ discount_application.title }}
      Savings: -{{ discount_application.total_allocated_amount | money }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "cart": {
        "discount_applications": [
          {
            "title": "Bloodroot discount!",
            "total_allocated_amount": "2.50"
          },
          {
            "title": "Ingredient Sale",
            "total_allocated_amount": "42.24"
          }
        ]
      }
    }
    ```

    ## Output

    9

    1

    2

    3

    4

    5

    Discount name: Bloodroot discount!

    Savings: -$2.50

    Discount name: Ingredient Sale

    Savings: -$42.24

    ##### Output

    ```liquid
    Discount name: Bloodroot discount!
      Savings: -$2.50

      Discount name: Ingredient Sale
      Savings: -$42.24
    ```

[Anchor to](/docs/api/liquid/objects/cart#cart-duties_included) 

duties\_included**duties\_included** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if duties are included in the prices of products in the cart. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/cart#cart-empty?) 

empty?**empty?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if there are no items in the cart. Return's `false` if there are.

[Anchor to](/docs/api/liquid/objects/cart#cart-item_count) 

item\_count**item\_count** [number](/docs/api/liquid/basics#number)

:   The number of items in the cart.

[Anchor to](/docs/api/liquid/objects/cart#cart-items) 

items**items** array of [line\_item](/docs/api/liquid/objects/line_item)

:   The line items in the cart.

[Anchor to](/docs/api/liquid/objects/cart#cart-items_subtotal_price) 

items\_subtotal\_price**items\_subtotal\_price** [number](/docs/api/liquid/basics#number)

:   The total price of all of the items in the cart in the currency's subunit, after any line item discounts. This
    doesn't include taxes (unless taxes are included in the prices), cart discounts, or shipping costs.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/cart#cart-note) 

note**note** [string](/docs/api/liquid/basics#string)

:   Additional information captured with the cart.

    To learn more about capturing cart notes, refer to the [`cart` template](/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Capture cart notes

    To capture a cart note, include an HTML input such as a `<textarea>` with an attribute of `name="note"` within the cart `<form>`.

    9

    1

    2

    <label>Gift note:</label>

    <textarea name="note"></textarea>

    ```liquid
    Gift note:
    ```

    ---

    Note

    There can only be one instance of `{{ cart.note }}` on the cart page. If there are multiple instances,
    then the one that comes latest in the Document Object Model (DOM) will be submitted with the form.

    **Note:**

    There can only be one instance of `{{ cart.note }}` on the cart page. If there are multiple instances,
    then the one that comes latest in the Document Object Model (DOM) will be submitted with the form.

    **Note:** There can only be one instance of <code>{{ cart.note }}</code> on the cart page. If there are multiple instances,
    then the one that comes latest in the Document Object Model (DOM) will be submitted with the form.

    ---

[Anchor to](/docs/api/liquid/objects/cart#cart-original_total_price) 

original\_total\_price**original\_total\_price** [number](/docs/api/liquid/basics#number)

:   The total price of all of the items in the cart in the currency's subunit, before discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/cart#cart-requires_shipping) 

requires\_shipping**requires\_shipping** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if any of the products in the cart require shipping. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/cart#cart-taxes_included) 

taxes\_included**taxes\_included** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if taxes are included in the prices of products in the cart. Returns `false` if not.

    This can be set in a store’s [tax settings](https://www.shopify.com/admin/settings/taxes).

    If the store includes or exclude tax [based on the customer’s country](https://help.shopify.com/manual/taxes/location#include-or-exclude-tax-based-on-your-customers-country),
    then the value reflects the tax requirements of the customer’s country.

[Anchor to](/docs/api/liquid/objects/cart#cart-total_discount) 

total\_discount**total\_discount** [number](/docs/api/liquid/basics#number)

:   The total amount of all discounts (the amount saved) for the cart in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/cart#cart-total_price) 

total\_price**total\_price** [number](/docs/api/liquid/basics#number)

:   The total price of all of the items in the cart in the currency's subunit, after discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/cart#cart-total_weight) 

total\_weight**total\_weight** [number](/docs/api/liquid/basics#number)

:   The total weight of all of the items in the cart in grams.

    Tip

    Use the [`weight_with_unit`](/docs/api/liquid/filters/weight_with_unit) filter to format the weight in
    [the store's format](https://www.shopify.com/admin/settings/general), or override the default unit.

    **Tip:**

    Use the [`weight_with_unit`](/docs/api/liquid/filters/weight_with_unit) filter to format the weight in
    [the store's format](https://www.shopify.com/admin/settings/general), or override the default unit.

    **Tip:** Use the <a href="/docs/api/liquid/filters/weight\_with\_unit"><code><span class="PreventFireFoxApplyingGapToWBR">weight<wbr/>\_with<wbr/>\_unit</span></code></a> filter to format the weight in
    <a href="https://www.shopify.com/admin/settings/general">the store&#39;s format</a>, or override the default unit.

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/cart#cart-discounts) 

discounts**discounts** array of [discount](/docs/api/liquid/objects/discount) Deprecated

:   The discounts applied to the cart.

    Deprecated

    Deprecated because not all discount types and details are available.

    The `cart.discounts` property has been replaced by [`cart.discount_applications`](/docs/api/liquid/objects/cart#cart-discount_applications).

    **Deprecated:**

    Deprecated because not all discount types and details are available.

    The `cart.discounts` property has been replaced by [`cart.discount_applications`](/docs/api/liquid/objects/cart#cart-discount_applications).

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

{

"attributes": {},

"cart\_level\_discount\_applications": [],

"checkout\_charge\_amount": "380.25",

"currency": {},

"discount\_applications": [],

"discounts": [],

"duties\_included": false,

"empty?": false,

"item\_count": 2,

"items": [],

"items\_subtotal\_price": "422.49",

"note": "Hello this is a note",

"original\_total\_price": "424.99",

"requires\_shipping": true,

"taxes\_included": false,

"total\_discount": "44.74",

"total\_price": "380.25",

"total\_weight": 0

}

##### Example

```liquid
{
  "attributes": {},
  "cart_level_discount_applications": [],
  "checkout_charge_amount": "380.25",
  "currency": {},
  "discount_applications": [],
  "discounts": [],
  "duties_included": false,
  "empty?": false,
  "item_count": 2,
  "items": [],
  "items_subtotal_price": "422.49",
  "note": "Hello this is a note",
  "original_total_price": "424.99",
  "requires_shipping": true,
  "taxes_included": false,
  "total_discount": "44.74",
  "total_price": "380.25",
  "total_weight": 0
}
```

[Anchor to](/docs/api/liquid/objects/cart#template-using) 

## Templates using cart

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecart template

Theme architecture

cart template](/themes/architecture/templates/cart)

Was this section helpful?

YesNo