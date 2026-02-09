---
source: https://shopify.dev/docs/api/liquid/objects/company_location
---

A location of the [company](/docs/api/liquid/objects/company) that a [customer](/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

## Properties

[Anchor to](/docs/api/liquid/objects/company_location#company_location-company) 

company**company** [company](/docs/api/liquid/objects/company)

:   The company that the location is associated with.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-current?) 

current?**current?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the location is currently selected. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-external_id) 

external\_id**external\_id** [string](/docs/api/liquid/basics#string)

:   The external ID of the location.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the location.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-metafields) 

metafields**metafields** array of [metafield](/docs/api/liquid/objects/metafield)

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the company location.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the location.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-shipping_address) 

shipping\_address**shipping\_address** [company\_address](/docs/api/liquid/objects/company_address)

:   The address of the location.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-store_credit_account) 

store\_credit\_account**store\_credit\_account** [store\_credit\_account](/docs/api/liquid/objects/store_credit_account)

:   The store credit account associated with the company location.

    The account shown will be in the currency associated with the company location’s current context.
    For example, when browsing a storefront for a company location in the US market, the company location's USD store credit
    account will be returned. If the company location does not have a USD store credit account `nil` will be returned.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-tax_registration_id) 

tax\_registration\_id**tax\_registration\_id** [number](/docs/api/liquid/basics#number)

:   The tax ID of the location.

[Anchor to](/docs/api/liquid/objects/company_location#company_location-url_to_set_as_current) 

url\_to\_set\_as\_current**url\_to\_set\_as\_current** [string](/docs/api/liquid/basics#string)

:   The URL to set the location as the current location for the customer.

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

{

"company": {},

"current?": false,

"external\_id": null,

"id": 98369,

"metafields": {},

"name": "99 Cauldron Lane",

"shipping\_address": {},

"store\_credit\_account": null,

"tax\_registration\_id": null,

"url\_to\_set\_as\_current": "https://polinas-potent-potions.myshopify.com/company\_location/update?location\_id=98369&return\_to=/resource"

}

##### Example

```liquid
{
  "company": {},
  "current?": false,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "99 Cauldron Lane",
  "shipping_address": {},
  "store_credit_account": null,
  "tax_registration_id": null,
  "url_to_set_as_current": "https://polinas-potent-potions.myshopify.com/company_location/update?location_id=98369&return_to=/resource"
}
```

Was this section helpful?

YesNo