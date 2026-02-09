---
source: https://shopify.dev/docs/api/liquid/objects/company
---

A company that a [customer](/docs/api/liquid/objects/customer) is purchasing for.

To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

## Properties

[Anchor to](/docs/api/liquid/objects/company#company-available_locations) 

available\_locations**available\_locations** array of [company\_location](/docs/api/liquid/objects/company_location)

:   The company locations that the current customer has access to, or can interact with.

[Anchor to](/docs/api/liquid/objects/company#company-available_locations_count) 

available\_locations\_count**available\_locations\_count** [number](/docs/api/liquid/basics#number)

:   The number of company locations associated with the customer's company.

[Anchor to](/docs/api/liquid/objects/company#company-external_id) 

external\_id**external\_id** [string](/docs/api/liquid/basics#string)

:   The external ID of the company.

[Anchor to](/docs/api/liquid/objects/company#company-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the company.

[Anchor to](/docs/api/liquid/objects/company#company-metafields) 

metafields**metafields** array of [metafield](/docs/api/liquid/objects/metafield)

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the company.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/company#company-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the company.

9

1

2

3

4

5

6

7

8

{

"available\_locations": [],

"available\_locations\_count": 1,

"external\_id": null,

"id": 98369,

"metafields": {},

"name": "Cornelius&#39; Custom Concoctions"

}

##### Example

```liquid
{
  "available_locations": [],
  "available_locations_count": 1,
  "external_id": null,
  "id": 98369,
  "metafields": {},
  "name": "Cornelius&#39; Custom Concoctions"
}
```

Was this section helpful?

YesNo