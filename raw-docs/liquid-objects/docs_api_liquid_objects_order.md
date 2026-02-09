---
source: https://shopify.dev/docs/api/liquid/objects/order
---

An [order](https://help.shopify.com/manual/orders).

## Properties

[Anchor to](/docs/api/liquid/objects/order#order-attributes) 

attributes**attributes**

:   The attributes on the order.

    If there are no attributes on the order, then `nil` is returned.

    Tip

    Attributes are [collected with the cart](https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    **Tip:**

    Attributes are [collected with the cart](https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    **Tip:** Attributes are <a href="https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes">collected with the cart</a>.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the attributes

    9

    1

    2

    3

    4

    5

    <ul>

    {% for attribute in order.attributes -%}

    <li><strong>{{ attribute.first }}:</strong> {{ attribute.last }}</li>

    {%- endfor %}

    </ul>

    ```liquid
    {% for attribute in order.attributes -%}* {{ attribute.first }}: {{ attribute.last }}
    {%- endfor %}
    ```

[Anchor to](/docs/api/liquid/objects/order#order-billing_address) 

billing\_address**billing\_address** [address](/docs/api/liquid/objects/address)

:   The billing address of the order.

[Anchor to](/docs/api/liquid/objects/order#order-cancel_reason) 

cancel\_reason**cancel\_reason** [string](/docs/api/liquid/basics#string) from a set of values

:   The reason that the order was cancelled.

    | Possible values | Description |
    | --- | --- |
    | customer | Customer changed/cancelled order |
    | declined | Payment declined |
    | fraud | Fraudulent order |
    | inventory | Items unavailable |
    | staff | Staff error |
    | other | Other |

[Anchor to](/docs/api/liquid/objects/order#order-cancel_reason_label) 

cancel\_reason\_label**cancel\_reason\_label** [string](/docs/api/liquid/basics#string)

:   The localized version of the [cancellation reason](/docs/api/liquid/objects/order#order-cancel_reason) for the order.

    Tip

    Use this property to output the cancellation reason on the storefront.

    **Tip:**

    Use this property to output the cancellation reason on the storefront.

    **Tip:** Use this property to output the cancellation reason on the storefront.

[Anchor to](/docs/api/liquid/objects/order#order-cancelled) 

cancelled**cancelled** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the order was cancelled. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/order#order-cancelled_at) 

cancelled\_at**cancelled\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the order was cancelled.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/order#order-cart_level_discount_applications) 

cart\_level\_discount\_applications**cart\_level\_discount\_applications** array of [discount\_application](/docs/api/liquid/objects/discount_application)

:   The discount applications that apply at the order level.

[Anchor to](/docs/api/liquid/objects/order#order-confirmation_number) 

confirmation\_number**confirmation\_number** [string](/docs/api/liquid/basics#string)

:   A randomly generated alpha-numeric identifier for the order that may be shown to the customer
    instead of the sequential order name. For example, "XPAV284CT", "R50KELTJP" or "35PKUN0UJ".
    This value isn't guaranteed to be unique.

[Anchor to](/docs/api/liquid/objects/order#order-created_at) 

created\_at**created\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the order was created.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/order#order-customer) 

customer**customer** [customer](/docs/api/liquid/objects/customer)

:   The customer that placed the order.

[Anchor to](/docs/api/liquid/objects/order#order-customer_order_url) 

customer\_order\_url**customer\_order\_url** [string](/docs/api/liquid/basics#string)

:   The URL for the new order details page.

    Customer accounts includes a list of Buyers Orders and an Order Details View.
    This liquid function exposes a URL to a specific Orders Details in customer accounts.
    [Setup process for the new order details page](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts)
    can be found in the help center.

[Anchor to](/docs/api/liquid/objects/order#order-customer_url) 

customer\_url**customer\_url** [string](/docs/api/liquid/basics#string)

:   The URL for the customer to view the order in their account.

[Anchor to](/docs/api/liquid/objects/order#order-discount_applications) 

discount\_applications**discount\_applications** array of [discount\_application](/docs/api/liquid/objects/discount_application)

:   All of the discount applications for the order and its line items.

[Anchor to](/docs/api/liquid/objects/order#order-email) 

email**email** [string](/docs/api/liquid/basics#string)

:   The email that's associated with the order.

    If no email is associated with the order, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/order#order-financial_status) 

financial\_status**financial\_status** [string](/docs/api/liquid/basics#string) from a set of values

:   The order's financial status.

    | Possible values |
    | --- |
    | authorized |
    | expired |
    | paid |
    | partially\_paid |
    | partially\_refunded |
    | pending |
    | refunded |
    | unpaid |
    | voided |

[Anchor to](/docs/api/liquid/objects/order#order-financial_status_label) 

financial\_status\_label**financial\_status\_label**

:   The localized version of the [financial status](/docs/api/liquid/objects/order#order-financial_status) of the order.

    Tip

    Use this property to output the financial status on the storefront.

    **Tip:**

    Use this property to output the financial status on the storefront.

    **Tip:** Use this property to output the financial status on the storefront.

[Anchor to](/docs/api/liquid/objects/order#order-fulfillment_status) 

fulfillment\_status**fulfillment\_status** [string](/docs/api/liquid/basics#string)

:   The fulfillment status of the order.

[Anchor to](/docs/api/liquid/objects/order#order-fulfillment_status_label) 

fulfillment\_status\_label**fulfillment\_status\_label** [string](/docs/api/liquid/basics#string) from a set of values

:   The localized version of the [fulfillment status](/docs/api/liquid/objects/order#order-fulfillment_status) of the order.

    Tip

    Use this property to output the fulfillment status on the storefront.

    **Tip:**

    Use this property to output the fulfillment status on the storefront.

    **Tip:** Use this property to output the fulfillment status on the storefront.

    | Possible values |
    | --- |
    | complete |
    | fulfilled |
    | partial |
    | restocked |
    | unfulfilled |

[Anchor to](/docs/api/liquid/objects/order#order-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the order.

[Anchor to](/docs/api/liquid/objects/order#order-item_count) 

item\_count**item\_count** [number](/docs/api/liquid/basics#number)

:   The number of items in the order.

[Anchor to](/docs/api/liquid/objects/order#order-line_items) 

line\_items**line\_items** array of [line\_item](/docs/api/liquid/objects/line_item)

:   The line items in the order.

[Anchor to](/docs/api/liquid/objects/order#order-line_items_subtotal_price) 

line\_items\_subtotal\_price**line\_items\_subtotal\_price** [number](/docs/api/liquid/basics#number)

:   The sum of the prices of all of the line items in the order in the currency's subunit, after any line item discounts have
    been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the order.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/order#order-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the order.

[Anchor to](/docs/api/liquid/objects/order#order-note) 

note**note** [string](/docs/api/liquid/basics#string)

:   The note on the order.

    If there's no note on the order, then `nil` is returned.

    Tip

    Notes are [collected with the cart](https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    **Tip:**

    Notes are [collected with the cart](https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes).

    **Tip:** Notes are <a href="https://shopify.dev/themes/architecture/templates/cart#support-cart-notes-and-attributes">collected with the cart</a>.

[Anchor to](/docs/api/liquid/objects/order#order-order_number) 

order\_number**order\_number** [number](/docs/api/liquid/basics#number)

:   The integer representation of the order [name](/docs/api/liquid/objects/order#order-name).

[Anchor to](/docs/api/liquid/objects/order#order-order_status_url) 

order\_status\_url**order\_status\_url** [string](/docs/api/liquid/basics#string)

:   The URL for the [**Order status** page](https://help.shopify.com/manual/orders/status-tracking) for the order.

[Anchor to](/docs/api/liquid/objects/order#order-phone) 

phone**phone** [string](/docs/api/liquid/basics#string)

:   The phone number associated with the order.

[Anchor to](/docs/api/liquid/objects/order#order-pickup_in_store?) 

pickup\_in\_store?**pickup\_in\_store?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the order is a store pickup order.

[Anchor to](/docs/api/liquid/objects/order#order-shipping_address) 

shipping\_address**shipping\_address** [address](/docs/api/liquid/objects/address)

:   The shipping address of the order.

[Anchor to](/docs/api/liquid/objects/order#order-shipping_methods) 

shipping\_methods**shipping\_methods** array of [shipping\_method](/docs/api/liquid/objects/shipping_method)

:   The shipping methods for the order.

[Anchor to](/docs/api/liquid/objects/order#order-shipping_price) 

shipping\_price**shipping\_price** [number](/docs/api/liquid/basics#number)

:   The shipping price of the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-subtotal_line_items) 

subtotal\_line\_items**subtotal\_line\_items** array of [line\_item](/docs/api/liquid/objects/line_item)

:   The non-tip line items in the order.

    Note

    These line items are used to calculate the the [subtotal price](/docs/api/liquid/objects/order#order-subtotal_price).

    **Note:**

    These line items are used to calculate the the [subtotal price](/docs/api/liquid/objects/order#order-subtotal_price).

    **Note:** These line items are used to calculate the the <a href="/docs/api/liquid/objects/order#order-subtotal\_price">subtotal price</a>.

[Anchor to](/docs/api/liquid/objects/order#order-subtotal_price) 

subtotal\_price**subtotal\_price** [number](/docs/api/liquid/basics#number)

:   The sum of the prices of the [subtotal line items](/docs/api/liquid/objects/order#order-subtotal_line_items) in the currency's subunit, after any line item or
    cart discounts have been applied.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   The [tags](https://help.shopify.com/manual/shopify-admin/productivity-tools/using-tags) on the order.

    The tags are returned in alphabetical order.

[Anchor to](/docs/api/liquid/objects/order#order-tax_lines) 

tax\_lines**tax\_lines** array of [tax\_line](/docs/api/liquid/objects/tax_line)

:   The tax lines on the order.

[Anchor to](/docs/api/liquid/objects/order#order-tax_price) 

tax\_price**tax\_price** [number](/docs/api/liquid/basics#number)

:   The total amount of taxes applied to the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-total_discounts) 

total\_discounts**total\_discounts** [number](/docs/api/liquid/basics#number)

:   The total amount of all discounts applied to the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-total_duties) 

total\_duties**total\_duties** [number](/docs/api/liquid/basics#number)

:   The sum of all duties applied to the line items in the order in the currency's subunit.

    If there are no duties, then `nil` is returned. The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-total_net_amount) 

total\_net\_amount**total\_net\_amount** [number](/docs/api/liquid/basics#number)

:   The net amount of the order in the currency's subunit.

    The amount is calculated after refunds are applied, so is equal to `order.total_price` minus `order.total_refunded_amount`.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-total_price) 

total\_price**total\_price** [number](/docs/api/liquid/basics#number)

:   The total price of the order in the currency's subunit.

    Note

    The total price is calculated before refunds are applied. Use [`order.total_net_amount`](/docs/api/liquid/objects/order#order-total_net_amount)
    to output the total minus any refunds.

    **Note:**

    The total price is calculated before refunds are applied. Use [`order.total_net_amount`](/docs/api/liquid/objects/order#order-total_net_amount)
    to output the total minus any refunds.

    **Note:** The total price is calculated before refunds are applied. Use <a href="/docs/api/liquid/objects/order#order-total\_net\_amount"><code><span class="PreventFireFoxApplyingGapToWBR">order.total<wbr/>\_net<wbr/>\_amount</span></code></a>
    to output the total minus any refunds.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-total_refunded_amount) 

total\_refunded\_amount**total\_refunded\_amount** [number](/docs/api/liquid/basics#number)

:   The total amount that's been refunded from the order in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/order#order-transactions) 

transactions**transactions** array of [transaction](/docs/api/liquid/objects/transaction)

:   The transactions of the order.

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/order#order-discounts) 

discounts**discounts** [discount](/docs/api/liquid/objects/discount) Deprecated

:   The discounts on the order.

    Deprecated

    Deprecated because not all discount types and details are captured.

    The `order.discounts` property has been replaced by [`order.discount_applications`](/docs/api/liquid/objects/order#order-discount_applications).

    **Deprecated:**

    Deprecated because not all discount types and details are captured.

    The `order.discounts` property has been replaced by [`order.discount_applications`](/docs/api/liquid/objects/order#order-discount_applications).

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

40

41

42

43

44

45

46

{

"attributes": {},

"billing\_address": {},

"cancel\_reason": null,

"cancel\_reason\_label": null,

"cancelled": false,

"cancelled\_at": null,

"cart\_level\_discount\_applications": [],

"confirmation\_number": "0YMJHPM8U",

"created\_at": "2022-04-29 11:15:46 -0400",

"customer": {},

"customer\_order\_url": "https://shopify.com/56174706753/account/orders/4295688749121?locale=en&region\_country=CA",

"customer\_url": "https://polinas-potent-potions.myshopify.com/account/orders/8be02e56c658bcd1f034d28c496fddd9",

"discount\_applications": [],

"discounts": null,

"email": "cornelius.potionmaker@gmail.com",

"financial\_status": "paid",

"financial\_status\_label": "Paid",

"fulfillment\_status": "partial",

"fulfillment\_status\_label": "Partial",

"id": 4295688749121,

"item\_count": 6,

"line\_items": [],

"line\_items\_subtotal\_price": "492.93",

"metafields": {},

"name": "#1001",

"note": null,

"order\_number": 1001,

"order\_status\_url": "https://polinas-potent-potions.myshopify.com/56174706753/orders/8be02e56c658bcd1f034d28c496fddd9/authenticate?key=4f9baf2b8ebd0f75ec73eb9bac6e4519",

"phone": null,

"pickup\_in\_store?": false,

"shipping\_address": {},

"shipping\_methods": [],

"shipping\_price": "0.00",

"subtotal\_line\_items": [],

"subtotal\_price": "492.93",

"tags": [],

"tax\_lines": [],

"tax\_price": "0.00",

"total\_discounts": "0.00",

"total\_duties": null,

"total\_net\_amount": "492.93",

"total\_price": "492.93",

"total\_refunded\_amount": "0.00",

"transactions": []

}

##### Example

```liquid
{
  "attributes": {},
  "billing_address": {},
  "cancel_reason": null,
  "cancel_reason_label": null,
  "cancelled": false,
  "cancelled_at": null,
  "cart_level_discount_applications": [],
  "confirmation_number": "0YMJHPM8U",
  "created_at": "2022-04-29 11:15:46 -0400",
  "customer": {},
  "customer_order_url": "https://shopify.com/56174706753/account/orders/4295688749121?locale=en&region_country=CA",
  "customer_url": "https://polinas-potent-potions.myshopify.com/account/orders/8be02e56c658bcd1f034d28c496fddd9",
  "discount_applications": [],
  "discounts": null,
  "email": "cornelius.potionmaker@gmail.com",
  "financial_status": "paid",
  "financial_status_label": "Paid",
  "fulfillment_status": "partial",
  "fulfillment_status_label": "Partial",
  "id": 4295688749121,
  "item_count": 6,
  "line_items": [],
  "line_items_subtotal_price": "492.93",
  "metafields": {},
  "name": "#1001",
  "note": null,
  "order_number": 1001,
  "order_status_url": "https://polinas-potent-potions.myshopify.com/56174706753/orders/8be02e56c658bcd1f034d28c496fddd9/authenticate?key=4f9baf2b8ebd0f75ec73eb9bac6e4519",
  "phone": null,
  "pickup_in_store?": false,
  "shipping_address": {},
  "shipping_methods": [],
  "shipping_price": "0.00",
  "subtotal_line_items": [],
  "subtotal_price": "492.93",
  "tags": [],
  "tax_lines": [],
  "tax_price": "0.00",
  "total_discounts": "0.00",
  "total_duties": null,
  "total_net_amount": "492.93",
  "total_price": "492.93",
  "total_refunded_amount": "0.00",
  "transactions": []
}
```

[Anchor to](/docs/api/liquid/objects/order#template-using) 

## Templates using order

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecustomers/order template

Theme architecture

customers/order template](/themes/architecture/templates/customers-order)

Was this section helpful?

YesNo