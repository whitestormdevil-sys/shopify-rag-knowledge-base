---
source: https://shopify.dev/docs/api/liquid/objects/form
---

Information about a form created by a [`form` tag](/docs/api/liquid/tags/form).

## Properties

[Anchor to](/docs/api/liquid/objects/form#form-address1) 

address1**address1** [string](/docs/api/liquid/basics#string)

:   The first address line associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-address2) 

address2**address2** [string](/docs/api/liquid/basics#string)

:   The second address line associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-author) 

author**author** [string](/docs/api/liquid/basics#string)

:   The name of the author of the article comment.

    This property is exclusive to the [`new_comment` form](/docs/api/liquid/tags/form#form-new_comment).

[Anchor to](/docs/api/liquid/objects/form#form-body) 

body**body** [string](/docs/api/liquid/basics#string)

:   The content of the contact submission or article comment.

    This property is exclusive to the [`contact`](/docs/api/liquid/tags/form#form-contact) and [`new_comment`](/docs/api/liquid/tags/form#form-new_comment)
    forms.

[Anchor to](/docs/api/liquid/objects/form#form-city) 

city**city** [string](/docs/api/liquid/basics#string)

:   The city associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-company) 

company**company** [string](/docs/api/liquid/basics#string)

:   The company associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-country) 

country**country** [string](/docs/api/liquid/basics#string)

:   The country associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-email) 

email**email** [string](/docs/api/liquid/basics#string)

:   The email associated with the form.

    This property is exclusive to the following forms:

    * [`contact`](/docs/api/liquid/tags/form#form-contact)
    * [`create_customer`](/docs/api/liquid/tags/form#form-create_customer)
    * [`customer`](/docs/api/liquid/tags/form#form-customer)
    * [`customer_login`](/docs/api/liquid/tags/form#form-customer_login)
    * [`new_comment`](/docs/api/liquid/tags/form#form-new_comment)
    * [`recover_customer_password`](/docs/api/liquid/tags/form#form-recover_customer_password)
    * [`product`](/docs/api/liquid/tags/form#form-product)

[Anchor to](/docs/api/liquid/objects/form#form-errors) 

errors**errors** [form\_errors](/docs/api/liquid/objects/form_errors)

:   Any errors from the form.

    If there are no errors, then `nil` is returned.

    Tip

    You can apply the [`default_errors` filter](/docs/api/liquid/filters/default_errors) to `form.errors` to output default
    error messages without having to loop through the array.

    **Tip:**

    You can apply the [`default_errors` filter](/docs/api/liquid/filters/default_errors) to `form.errors` to output default
    error messages without having to loop through the array.

    **Tip:** You can apply the <a href="/docs/api/liquid/filters/default\_errors"><code><span class="PreventFireFoxApplyingGapToWBR">default<wbr/>\_errors</span></code> filter</a> to <code>form.errors</code> to output default
    error messages without having to loop through the array.

[Anchor to](/docs/api/liquid/objects/form#form-first_name) 

first\_name**first\_name** [string](/docs/api/liquid/basics#string)

:   The first name associated with the customer or address.

    This property is exclusive to the [`create_customer`](/docs/api/liquid/tags/form#form-create_customer) and
    [`customer_address`](/docs/api/liquid/tags/form#form-customer_address) forms.

[Anchor to](/docs/api/liquid/objects/form#form-id) 

id**id** [string](/docs/api/liquid/basics#string)

:   The ID of the form.

[Anchor to](/docs/api/liquid/objects/form#form-last_name) 

last\_name**last\_name** [string](/docs/api/liquid/basics#string)

:   The last name associated with the customer or address.

    This property is exclusive to the [`create_customer`](/docs/api/liquid/tags/form#form-create_customer) and
    [`customer_address`](/docs/api/liquid/tags/form#form-customer_address) forms.

[Anchor to](/docs/api/liquid/objects/form#form-message) 

message**message** [string](/docs/api/liquid/basics#string)

:   The personalized message intended for the recipient.

    This property is exclusive to the [`product` form](/docs/api/liquid/tags/form#form-product).

[Anchor to](/docs/api/liquid/objects/form#form-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The nickname of the gift card recipient.

    This property is exclusive to the [`product` form](/docs/api/liquid/tags/form#form-product).

[Anchor to](/docs/api/liquid/objects/form#form-password_needed) 

password\_needed**password\_needed** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true`.

    This property is exclusive to the [`customer_login` form](/docs/api/liquid/tags/form#form-customer_login).

[Anchor to](/docs/api/liquid/objects/form#form-phone) 

phone**phone** [string](/docs/api/liquid/basics#string)

:   The phone number associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-posted_successfully?) 

posted\_successfully?**posted\_successfully?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the form was submitted successfully. Returns `false` if there were errors.

    Note

    The [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address) always returns `true`.

    **Note:**

    The [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address) always returns `true`.

    **Note:** The <a href="/docs/api/liquid/tags/form#form-customer\_address"><code><span class="PreventFireFoxApplyingGapToWBR">customer<wbr/>\_address</span></code> form</a> always returns <code>true</code>.

[Anchor to](/docs/api/liquid/objects/form#form-province) 

province**province** [string](/docs/api/liquid/basics#string)

:   The province associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-set_as_default_checkbox) 

set\_as\_default\_checkbox**set\_as\_default\_checkbox** [string](/docs/api/liquid/basics#string)

:   Renders an HTML checkbox that can submit the address as the customer's default address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

[Anchor to](/docs/api/liquid/objects/form#form-zip) 

zip**zip** [string](/docs/api/liquid/basics#string)

:   The zip or postal code associated with the address.

    This property is exclusive to the [`customer_address` form](/docs/api/liquid/tags/form#form-customer_address).

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

"address1": "12 Phoenix Feather Alley",

"address2": "1",

"author": null,

"body": null,

"city": "Calgary",

"company": null,

"country": "Canada",

"email": null,

"errors": null,

"first\_name": "Cornelius",

"id": "new",

"last\_name": "Potionmaker",

"password\_needed?": false,

"phone": "44 131 496 0905",

"posted\_successfully?": true,

"province": "Alberta",

"set\_as\_default\_checkbox": "<input type='checkbox' id='address\_default\_address\_new' name='address[default]' value='1'>",

"zip": "T1X 0L4"

}

##### Example

```liquid
{
  "address1": "12 Phoenix Feather Alley",
  "address2": "1",
  "author": null,
  "body": null,
  "city": "Calgary",
  "company": null,
  "country": "Canada",
  "email": null,
  "errors": null,
  "first_name": "Cornelius",
  "id": "new",
  "last_name": "Potionmaker",
  "password_needed?": false,
  "phone": "44 131 496 0905",
  "posted_successfully?": true,
  "province": "Alberta",
  "set_as_default_checkbox": "<input type='checkbox' id='address_default_address_new' name='address[default]' value='1'>",
  "zip": "T1X 0L4"
}
```

Was this section helpful?

YesNo