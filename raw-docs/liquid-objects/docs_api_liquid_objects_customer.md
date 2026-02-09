---
source: https://shopify.dev/docs/api/liquid/objects/customer
---

A [customer](https://help.shopify.com/manual/customers) of the store.

The `customer` object is directly accessible globally when a customer is logged in to their account. It's also defined in
the following contexts:

* The [`customers/account` template](/themes/architecture/templates/customers-account)
* The [`customers/addresses` template](/themes/architecture/templates/customers-addresses)
* The [`customers/order` template](/themes/architecture/templates/customers-order)
* When accessing [`checkout.customer`](/docs/api/liquid/objects/checkout#checkout-customer)
* When accessing [`gift_card.customer`](/docs/api/liquid/objects/gift_card#gift_card-customer)
* When accessing [`order.customer`](/docs/api/liquid/objects/order#order-customer)

Outside of the above contexts, if the customer isn't logged into their account, the `customer` object returns `nil`.

## Properties

[Anchor to](/docs/api/liquid/objects/customer#customer-accepts_marketing) 

accepts\_marketing**accepts\_marketing** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the customer accepts marketing. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/customer#customer-addresses) 

addresses**addresses** array of [address](/docs/api/liquid/objects/address)

:   All of the addresses associated with the customer.

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many addresses to show at once, up to a limit of 20.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many addresses to show at once, up to a limit of 20.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many addresses to show at once, up to a limit of 20.

[Anchor to](/docs/api/liquid/objects/customer#customer-addresses_count) 

addresses\_count**addresses\_count** [number](/docs/api/liquid/basics#number)

:   The number of addresses associated with the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-b2b?) 

b2b?**b2b?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the customer is a B2B customer. Returns `false` if not.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

[Anchor to](/docs/api/liquid/objects/customer#customer-company_available_locations) 

company\_available\_locations**company\_available\_locations** array of [company\_location](/docs/api/liquid/objects/company_location)

:   The company locations that the customer has access to, or can interact with.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many company locations to show at once, up to a limit of 100.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many company locations to show at once, up to a limit of 100.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many company locations to show at once, up to a limit of 100.

[Anchor to](/docs/api/liquid/objects/customer#customer-company_available_locations_count) 

company\_available\_locations\_count**company\_available\_locations\_count** [number](/docs/api/liquid/basics#number)

:   The number of company locations associated with the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-current_company) 

current\_company**current\_company** [company](/docs/api/liquid/objects/company)

:   The company that the customer is purchasing for.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

[Anchor to](/docs/api/liquid/objects/customer#customer-current_location) 

current\_location**current\_location** [company\_location](/docs/api/liquid/objects/company_location)

:   The currently selected company location.

    To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

[Anchor to](/docs/api/liquid/objects/customer#customer-default_address) 

default\_address**default\_address** [address](/docs/api/liquid/objects/address)

:   The default address of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-email) 

email**email** [string](/docs/api/liquid/basics#string)

:   The email of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-first_name) 

first\_name**first\_name** [string](/docs/api/liquid/basics#string)

:   The first name of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-has_account) 

has\_account**has\_account** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the email associated with the customer is tied to a
    [customer account](https://help.shopify.com/manual/customers/customer-accounts). Returns `false` if not.

    A customer can complete a checkout without making an account with the store. If the customer
    doesn't have an account with the store, then `customer.has_account` is `false` at checkout.

    During the checkout process, if the customer has an account with the store and enters an email associated
    with an account, then `customer.has_account` is `true`. The email is associated with the account regardless
    of whether the customer has logged into their account.

[Anchor to](/docs/api/liquid/objects/customer#customer-has_avatar?) 

has\_avatar?**has\_avatar?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if an avatar is associated with a customer. Returns `false` if not.

    A customer may have an avatar associated with their account, which can be displayed in the storefront.

    Tip

    Use with the [`avatar`](/docs/api/liquid/filters/avatar) filter to render the customer's avatar.

    **Tip:**

    Use with the [`avatar`](/docs/api/liquid/filters/avatar) filter to render the customer's avatar.

    **Tip:** Use with the <a href="/docs/api/liquid/filters/avatar"><code>avatar</code></a> filter to render the customer&#39;s avatar.

[Anchor to](/docs/api/liquid/objects/customer#customer-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-last_name) 

last\_name**last\_name** [string](/docs/api/liquid/basics#string)

:   The last name of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-last_order) 

last\_order**last\_order** [order](/docs/api/liquid/objects/order)

:   The last order placed by the customer, not including test orders.

[Anchor to](/docs/api/liquid/objects/customer#customer-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The full name of the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-orders) 

orders**orders** array of [order](/docs/api/liquid/objects/order)

:   All of the orders placed by the customer.

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many orders to show at once, up to a limit of 20.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many orders to show at once, up to a limit of 20.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many orders to show at once, up to a limit of 20.

[Anchor to](/docs/api/liquid/objects/customer#customer-orders_count) 

orders\_count**orders\_count** [number](/docs/api/liquid/basics#number)

:   The total number of orders that the customer has placed.

[Anchor to](/docs/api/liquid/objects/customer#customer-payment_methods) 

payment\_methods**payment\_methods** array of [customer\_payment\_method](/docs/api/liquid/objects/customer_payment_method)

:   The customer's saved payment methods.

[Anchor to](/docs/api/liquid/objects/customer#customer-phone) 

phone**phone** [string](/docs/api/liquid/basics#string)

:   The phone number of the customer.

    This phone number is only populated if the customer checks out using a phone number during checkout, opts in to SMS
    notifications, or if the merchant has manually entered it.

[Anchor to](/docs/api/liquid/objects/customer#customer-store_credit_account) 

store\_credit\_account**store\_credit\_account** [store\_credit\_account](/docs/api/liquid/objects/store_credit_account)

:   The store credit account associated with the customer.

    The account shown will be in the currency associated with the customer’s current context.
    For example, if a customer is browsing the storefront in the US market, their USD store credit account will be
    returned. If they do not have a USD store credit account `nil` will be returned.

[Anchor to](/docs/api/liquid/objects/customer#customer-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   The tags associated with the customer.

[Anchor to](/docs/api/liquid/objects/customer#customer-tax_exempt) 

tax\_exempt**tax\_exempt** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the customer is exempt from taxes. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/customer#customer-total_spent) 

total\_spent**total\_spent** [number](/docs/api/liquid/basics#number)

:   The total amount that the customer has spent on all orders in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

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

{

"accepts\_marketing": true,

"addresses": [],

"addresses\_count": 5,

"b2b?": false,

"company\_available\_locations": [],

"company\_available\_locations\_count": 1,

"current\_company": {},

"current\_location": null,

"default\_address": {},

"email": "cornelius.potionmaker@gmail.com",

"first\_name": "Cornelius",

"has\_account": true,

"has\_avatar?": false,

"id": 5625411010625,

"last\_name": "Potionmaker",

"last\_order": {},

"name": "Cornelius Potionmaker",

"orders": [],

"orders\_count": 1,

"payment\_methods": [],

"phone": "+441314960905",

"store\_credit\_account": {},

"tags": [

"newsletter"

],

"tax\_exempt": false,

"total\_spent": "56.00"

}

##### Example

```liquid
{
  "accepts_marketing": true,
  "addresses": [],
  "addresses_count": 5,
  "b2b?": false,
  "company_available_locations": [],
  "company_available_locations_count": 1,
  "current_company": {},
  "current_location": null,
  "default_address": {},
  "email": "cornelius.potionmaker@gmail.com",
  "first_name": "Cornelius",
  "has_account": true,
  "has_avatar?": false,
  "id": 5625411010625,
  "last_name": "Potionmaker",
  "last_order": {},
  "name": "Cornelius Potionmaker",
  "orders": [],
  "orders_count": 1,
  "payment_methods": [],
  "phone": "+441314960905",
  "store_credit_account": {},
  "tags": [
    "newsletter"
  ],
  "tax_exempt": false,
  "total_spent": "56.00"
}
```

[Anchor to Check whether the `customer` object is defined](/docs/api/liquid/objects/customer#customer-check-whether-the-customer-object-is-defined)

### Check whether the `customer` object is defined

When using the `customer` object outside of customer-specific templates or objects that specifically return a customer, you should check whether the `customer` object is defined.

9

1

2

3

{% if customer %}

Hello, {{ customer.first\_name }}!

{% endif %}

##### Code

```liquid
{% if customer %}
  Hello, {{ customer.first_name }}!
{% endif %}
```

##### Data

```liquid
{
  "customer": {
    "first_name": "Cornelius"
  }
}
```

## Output

9

1

Hello, Cornelius!

##### Output

```liquid
Hello, Cornelius!
```

[Anchor to](/docs/api/liquid/objects/customer#template-using) 

## Templates using customer

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecustomers/account template

Theme architecture

customers/account template](/themes/architecture/templates/customers-account)[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecustomers/addresses template

Theme architecture

customers/addresses template](/themes/architecture/templates/customers-addresses)[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecustomers/order template

Theme architecture

customers/order template](/themes/architecture/templates/customers-order)

Was this section helpful?

YesNo