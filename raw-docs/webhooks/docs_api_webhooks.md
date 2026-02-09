---
source: https://shopify.dev/docs/api/webhooks
---

# Webhooks

The list of all webhook topics you can subscribe to. You can use webhook subscriptions to receive notifications about particular events in a shop.

Caution

If your app is distributed through the Shopify App Store, it must be subscribed to Shopify's [mandatory compliance topics](/docs/apps/build/privacy-law-compliance). You can create mandatory compliance webhook subscriptions either using your Partner Dashboard or by updating your [app configuration file](/docs/apps/build/cli-for-apps/app-configuration#app-configuration-file-example).

**Caution:**

If your app is distributed through the Shopify App Store, it must be subscribed to Shopify's [mandatory compliance topics](/docs/apps/build/privacy-law-compliance). You can create mandatory compliance webhook subscriptions either using your Partner Dashboard or by updating your [app configuration file](/docs/apps/build/cli-for-apps/app-configuration#app-configuration-file-example).

Ask assistant

Choose a version:

unstable 2026-04 latest2026-01 2025-10 2025-07 2025-04 

2026-04latest

## [Anchor to Getting started](/docs/api/webhooks/latest#getting-started)Getting started

Creating subscriptions using the app configuration file

You can subscribe to most topics through your [app configuration file](/docs/apps/build/webhooks/subscribe/get-started?framework=remix&deliveryMethod=pubSub) using CLI version 3.63.0 or greater.

If you create and manage your subscriptions in your app configuration file, they will be used across all shops that your app is installed on.

Creating subscriptions using GraphQL Admin API

You can make app-specific subscriptions to all non-compliance topics through your app configuration file, or shop-specific subscriptions by Shopify's GraphQL Admin API.

For subscriptions managed with the [GraphQL Admin API](/docs/api/admin-graphql), use the `webhookSubscriptionCreate` mutation. Specify the `$topic` and `$webhookSubscription` parameters to create subscriptions.

---

## [Anchor to List of topics](/docs/api/webhooks/latest#list-of-topics)List of topics

Was this section helpful?

YesNo

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

"id": 1,

"shop\_id": "gid://shopify/Shop/548380009",

"previous": [

"read\_products"

],

"current": [

"read\_products",

"write\_products"

],

"updated\_at": "2024-06-25T00:00:00.000Z"

}

### Examples

* #### app/scopes\_update: Sample Payload

  ##### 

  ```liquid
  {
    "id": 1,
    "shop_id": "gid://shopify/Shop/548380009",
    "previous": [
      "read_products"
    ],
    "current": [
      "read_products",
      "write_products"
    ],
    "updated_at": "2024-06-25T00:00:00.000Z"
  }
  ```

---

## [Anchor to Customize](/docs/api/webhooks/latest#customize)Customize

Filter events

Manage the number of event messages your app receives by filtering events. Unlike payload modifications, filters are made up of rules, applied to a webhook subscription, which act as a gate for whether or not webhooks are delivered when an event occurs.

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

Navigate toWebhooks filters guide

Navigate to

Webhooks filters guide](/docs/apps/build/webhooks/customize/filters)

[Navigate to - Webhooks filters guide](/docs/apps/build/webhooks/customize/filters)

[![](/images/icons/32/liquidfilters.png)![](/images/icons/32/liquidfilters-dark.png)

Navigate toShopify API Search Syntax

Navigate to

Shopify API Search Syntax](/docs/api/usage/search-syntax)

[Navigate to - Shopify API Search Syntax](/docs/api/usage/search-syntax)

Modify payloads

Shopify provides you with a way to modify the payload you receive when you subscribe to webhook topics. Unlike filters, which always return the same payload, this feature enables you to specify what subset of information is most relevant to your use case from a webhook.

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

Navigate toWebhooks payload modification guide

Navigate to

Webhooks payload modification guide](/docs/apps/build/webhooks/customize/modify-payloads)

[Navigate to - Webhooks payload modification guide](/docs/apps/build/webhooks/customize/modify-payloads)

---

Was this page helpful?

YesNo