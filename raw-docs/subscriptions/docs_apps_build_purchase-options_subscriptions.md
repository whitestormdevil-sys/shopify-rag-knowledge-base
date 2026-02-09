---
source: https://shopify.dev/docs/apps/build/purchase-options/subscriptions
---

Subscriptions enable customers to purchase products on a recurring basis. For example, customers can do the following:

* Pay-per-delivery subscription: Pay for products for each delivery. New orders are created at regular intervals. This option is also known as "Subscribe and save".
* Pre-paid subscription: Make a single payment upfront and receive products on a regular cadence until the order is fulfilled.

  Subscription apps enable developers and merchants to build subscription experiences directly into Shopify's ecosystem. This guide describes what a subscription is, subscription APIs, migration to subscription APIs, and limitations for subscription apps.

---

## [Anchor to Overview of merchant and buyer experiences](/docs/apps/build/purchase-options/subscriptions#overview-of-merchant-and-buyer-experiences)Overview of merchant and buyer experiences

Subscriptions are deeply integrated across merchant and customer experiences. Here's a high-level overview:

![Overview of merchant and buyer experiences](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/subscriptions-overview-CobJUghK.png)

Learn more about merchant and buyer subscription experiences on Shopify

---

## [Anchor to How do subscriptions work?](/docs/apps/build/purchase-options/subscriptions#how-do-subscriptions-work)How do subscriptions work?

Subscriptions include policy configurations and subscription contracts.

### [Anchor to Policy configurations](/docs/apps/build/purchase-options/subscriptions#policy-configurations)Policy configurations

A subscription includes [delivery, pricing, and billing policies](/docs/apps/build/purchase-options#how-do-purchase-options-work). This enables you to build more flexible and extensible apps that support various ways to sell and buy products.

[Learn more about policies and selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans#subscription-shipping-and-delivery).

![Policy configurations](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/subscriptions-configuration-lEs3Notn.png)

### [Anchor to Subscription contracts](/docs/apps/build/purchase-options/subscriptions#subscription-contracts)Subscription contracts

A subscription contract is the agreement between a customer and a merchant over a specific term for recurring purchases over a set or undefined period of time.

[Learn more about subscription contracts](/docs/apps/build/purchase-options/subscriptions/contracts).

---

## [Anchor to Subscription APIs](/docs/apps/build/purchase-options/subscriptions#subscription-apis)Subscription APIs

Shopify provides the following APIs to help you build and manage subscriptions in your app:

* [**Selling plan APIs**](/docs/api/admin-graphql/latest/objects/sellingplan): Create and manage various ways to sell and buy products.
* [**Subscription contract APIs**](/docs/api/admin-graphql/latest/objects/subscriptioncontract): Create and manage subscription agreements between a customer and merchant.
* [**Customer payment method APIs**](/docs/api/admin-graphql/latest/objects/customerpaymentmethod): Store payment methods that can be used to pay for future orders without requiring the customer to manually go through checkout.

---

## [Anchor to Migrating to use the Subscription APIs?](/docs/apps/build/purchase-options/subscriptions#migrating-to-use-the-subscription-apis)Migrating to use the Subscription APIs?

If you already have a subscription app and need to migrate to use Subscription APIs, then refer to the [Subscription API migration guide](/docs/apps/build/purchase-options/subscriptions/migrate-to-subscriptions-api).

If your existing subscription app uses Stripe to process subscription payments, refer to [Migrating existing subscription contracts to Shopify](/docs/apps/build/purchase-options/subscriptions/migrate-to-subscriptions-api).

---

## [Anchor to Developer tools and resources](/docs/apps/build/purchase-options/subscriptions#developer-tools-and-resources)Developer tools and resources

To help you build and manage purchase options, Shopify offers the following developer tools and resources.

Developer tools and resources

| Tools/Resources | Description |
| --- | --- |
| [App extensions](/docs/apps/build/purchase-options/purchase-options-extensions) | Surfaces your app's purchase options in the Shopify admin |
| [App proxy](/docs/apps/build/purchase-options/customer-portal) | Fetches data from an app proxy server to display on a page of the online store. By using an app proxy, customers can have a seamless experience managing their existing agreements under the shop's domain. |
| Storefront Liquid drops and properties | Allows you to integrate purchase options into a store's theme |

---

## [Anchor to Legacy subscription apps](/docs/apps/build/purchase-options/subscriptions#legacy-subscription-apps)Legacy subscription apps

If you have merchants that are dependent on features in your legacy subscription app that are currently unresolved limitations of the subscription APIs, then any existing installs can continue to use your app.

All new installs and apps should use the new Subscription APIs.

---

## [Anchor to Subscriptions on Shopify POS](/docs/apps/build/purchase-options/subscriptions#subscriptions-on-shopify-pos)Subscriptions on Shopify POS

### [Anchor to POS support](/docs/apps/build/purchase-options/subscriptions#pos-support)POS support

Requirements

* Shopify POS app version 10.13 or later
* POS UI extensions API version 2025-10 or later
* Shopify Payments enabled

**Requirements:**

* Shopify POS app version 10.13 or later
* POS UI extensions API version 2025-10 or later
* Shopify Payments enabled

Merchants can sell subscriptions through Shopify Point of Sale (POS). This enables customers to purchase subscription products in-store with the same subscription experience they have online.

### [Anchor to POS limitations](/docs/apps/build/purchase-options/subscriptions#pos-limitations)POS limitations

The following limitations apply to subscriptions on Shopify POS:

* Managing existing selling plan contracts must be done through the online store. You can't manage contracts directly on POS.
* [Ship and carry out orders](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/ship-and-carry-out) aren't supported with subscriptions on POS.
* [Split payment capabilities](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/payment-management/multiple-partial-payments) aren't supported with subscriptions on POS.
* Shipping selling plans outside of the [shipping zone](https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/shipping-zones) isn't supported because custom rates can't be applied when calculating recurring shipping rates.
* Subscriptions on POS require Shopify Payments. POS stores that don't use Shopify Payments can't sell subscriptions.
* Subscription-only products are not supported on POS.

### [Anchor to Building subscription apps for POS](/docs/apps/build/purchase-options/subscriptions#building-subscription-apps-for-pos)Building subscription apps for POS

To support subscriptions on POS, subscription apps need to build a [POS UI extension](/docs/api/pos-ui-extensions) that uses the Cart API to add selling plans to products.

The POS UI extensions API version 2025-10 introduces new methods for managing selling plans:

* [`addLineItemSellingPlan`](/docs/api/pos-ui-extensions/2025-10/apis/cart-api#cartapi-propertydetail-addlineitemsellingplan): Adds a selling plan to a line item in the cart
* [`removeLineItemSellingPlan`](/docs/api/pos-ui-extensions/2025-10/apis/cart-api#cartapi-propertydetail-removelineitemsellingplan): Removes a selling plan from a line item

The `LineItem` interface also includes new fields to support selling plans:

* `requiresSellingPlan`: Indicates if a product must have a selling plan
* `hasSellingPlanGroups`: Indicates if a product has available selling plans
* `sellingPlan`: The currently applied selling plan

Important

Attempting to use selling plan APIs in POS UI extensions versions earlier than 2025-10, or on POS app versions earlier than 10.13, results in blocked checkouts. Ensure your system meets the version requirements.

**Important:**

Attempting to use selling plan APIs in POS UI extensions versions earlier than 2025-10, or on POS app versions earlier than 10.13, results in blocked checkouts. Ensure your system meets the version requirements.

For more information, refer to the [POS UI extensions reference](/docs/api/pos-ui-extensions).

---

## [Anchor to UX guidelines](/docs/apps/build/purchase-options/subscriptions#ux-guidelines)UX guidelines

For information on UX guidelines, refer to the [Subscription UX guidelines](/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines).

---

## [Anchor to Next steps](/docs/apps/build/purchase-options/subscriptions#next-steps)Next steps

* Learn about the different methods of [authenticating and authorizing apps](/docs/apps/build/authentication-authorization) with Shopify's platform.
* Use [webhooks](/docs/apps/build/webhooks) to stay in sync with Shopify or execute code after a specific event occurs in a shop.
* Learn how to use [metafields](/docs/apps/build/custom-data/metafields) to share additional information about Shopify resources with your app.
* Learn about the [structure](/docs/apps/build/cli-for-apps/app-structure) of an app built with Shopify CLI.
* Refer to the [Shopify Partners Blog](https://www.shopify.com/ca/partners/blog/shopify-subscription-apis) for more information about why we built this feature and how to get started.

---

Was this page helpful?

YesNo