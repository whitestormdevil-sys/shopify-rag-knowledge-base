---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/policy
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# Policy

Ask assistant

You can use the Policy resource to access the policies that a merchant has configured for their shop, such as their refund and privacy policies.

Only the shop owner can edit this information from the Shopify admin. The Policy resource lets you only retrieve information about a shop's policies.

Was this section helpful?

YesNo

#

## Endpoints

* [get

  /admin/api/latest/policies.json](/docs/api/admin-rest/latest/resources/policy#get-policies)

  Retrieves a list of the shop's policies

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-the-shops-policies)

---

[Anchor to](/docs/api/admin-rest/latest/resources/policy#resource-object) 

## The Policy resource

[Anchor to](/docs/api/admin-rest/latest/resources/policy#resource-object-properties) 

### Properties

---

title

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

title](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.title)

The name of the policy.

---

body

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

body](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.body)

A description of the policy.

---

url

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

url](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.url)

The public URL of the policy.

---

created\_at

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

createdAt](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the policy was created.

---

updated\_at

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

updatedAt](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the policy was last modified.

---

handle

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

type](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.type)

A unique identifer for the policy used to build the policy's URL.

---

Was this section helpful?

YesNo

{}

## The Policy resource

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

"title": {

"title": "Refund Policy"

},

"body": {

"body": "You have 30 days to get a refund"

},

"url": {

"url": "https://jsmith.myshopify.com/548380009/policies/878590288"

},

"created\_at": {

"created\_at": "2012-02-15T15:12:21-05:00"

},

"updated\_at": {

"updated\_at": "2012-08-24T14:01:47-04:00"

},

"handle": {

"handle": "terms-of-service"

}

}

---

## [Anchor to GET request, Retrieves a list of the shop's policies](/docs/api/admin-rest/latest/resources/policy#get-policies) get Retrieves a list of the shop's policies

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-the-shops-policies)

Retrieves a list of the shop's policies

### [Anchor to Parameters of Retrieves a list of the shop's policies](/docs/api/admin-rest/latest/resources/policy#get-policies-parameters)Parameters

---

api\_version

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-policies-examples](/docs/api/admin-rest/latest/resources/policy#get-policies-examples)Examples

Retrieve a list of the shop's policies

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/policies.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

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

HTTP/1.1 200 OK

{

"policies": [

{

"body": "You have 30 days to get a refund",

"created\_at": "2026-01-09T22:36:08-05:00",

"updated\_at": "2026-01-09T22:36:08-05:00",

"handle": "refund-policy",

"title": "Refund policy",

"url": "https://jsmith.myshopify.com/548380009/policies/997884057"

}

]

}

### examples

* #### Retrieve a list of the shop's policies

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/policies.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Policy.all({
    session: session,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Policy.all(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Policy.all({
    session: session,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"policies":[{"body":"You have 30 days to get a refund","created_at":"2026-01-09T22:36:08-05:00","updated_at":"2026-01-09T22:36:08-05:00","handle":"refund-policy","title":"Refund policy","url":"https://jsmith.myshopify.com/548380009/policies/997884057"}]}
  ```