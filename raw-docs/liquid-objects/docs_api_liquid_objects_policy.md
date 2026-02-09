---
source: https://shopify.dev/docs/api/liquid/objects/policy
---

A [store policy](https://help.shopify.com/manual/checkout-settings/refund-privacy-tos), such as a privacy or return policy.

## Properties

[Anchor to](/docs/api/liquid/objects/policy#policy-body) 

body**body** [string](/docs/api/liquid/basics#string)

:   The content of the policy.

[Anchor to](/docs/api/liquid/objects/policy#policy-id) 

id**id** [string](/docs/api/liquid/basics#string)

:   The ID of the policy.

[Anchor to](/docs/api/liquid/objects/policy#policy-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the policy.

[Anchor to](/docs/api/liquid/objects/policy#policy-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the policy.

9

1

2

3

4

5

6

{

"body": "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",

"id": 23805034561,

"title": "Refund policy",

"url": "/policies/refund-policy"

}

##### Example

```liquid
{
  "body": "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",
  "id": 23805034561,
  "title": "Refund policy",
  "url": "/policies/refund-policy"
}
```

Was this section helpful?

YesNo