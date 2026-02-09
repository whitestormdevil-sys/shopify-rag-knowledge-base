---
source: https://shopify.dev/docs/apps/build/purchase-options
---

Purchase option apps provide merchants and customers with various ways to sell and buy products, beyond the "buy now, pay now, and ship now" experience. For example, customers can place an order for an album before it's released or place a subscription order to receive a bag of coffee beans every month.

This guide describes what purchase options are, how they work, and some tools and resources to consider before you get started.

---

## [Anchor to What's a purchase option?](/docs/apps/build/purchase-options#whats-a-purchase-option)What's a purchase option?

A purchase option determines how customers can buy products from a store. Purchase options can help merchants manage cash flow and inventory, have flexibility on product launches, and diversify marketing strategies.

---

## [Anchor to Purchase option types](/docs/apps/build/purchase-options#purchase-option-types)Purchase option types

Purchase options include subscriptions and deferred purchase options.

### [Anchor to Subscriptions](/docs/apps/build/purchase-options#subscriptions)Subscriptions

Subscriptions enable customers to purchase products on a recurring basis. For example, customers can do the following:

* **Pay-per-delivery subscription**: Pay for products for each delivery. New orders are created at regular intervals. This option is also known as "Subscribe and save".
* **Pre-paid subscription**: Make a single payment upfront and receive products on a regular cadence until the order is fulfilled.

Subscriptions can be sold through online channels and Shopify POS (requires POS app version 10.13+).

For more information, refer to [Subscriptions](/docs/apps/build/purchase-options/subscriptions).

### [Anchor to Pre-order and Try Before You Buy](/docs/apps/build/purchase-options#pre-order-and-try-before-you-buy)Pre-order and Try Before You Buy

Pre-order and TBYB enable customers to purchase products with deferred payments or deliveries. For example, customers can do the following:

* **Pre-order**: Place an order for products or variants that haven't been released yet.
* **Try before you buy**: Try products before completing payment, and send back the products that aren't wanted.

You can enable deposits for pre-order and TBYB. Shopify stores a customer's payment method so that merchants can collect the remaining balance amount without contacting the customer.

For more information, refer to [Pre-order and Try Before You Buy (TBYB) apps](/docs/apps/build/purchase-options/deferred).

---

## [Anchor to How do purchase options work?](/docs/apps/build/purchase-options#how-do-purchase-options-work)How do purchase options work?

### [Anchor to Purchase options and selling plans](/docs/apps/build/purchase-options#purchase-options-and-selling-plans)Purchase options and selling plans

A purchase option defines how a product can be sold and specifies selling plan policies around pricing, delivery, and more.

For example, a subscription can include "Delivery every week, 15% off" and "Delivered every two weeks, 10% off" selling plans.

### [Anchor to Selling plans and policies](/docs/apps/build/purchase-options#selling-plans-and-policies)Selling plans and policies

Selling plans include configurations of the following policies:

* Pricing: Defines pricing changes on a given product variant.
* Billing: Defines the intervals of time between the placement of an order and payment collection.
* Delivery: Defines when the order should be fulfilled, from the time that the order is created to the time that it leaves the merchant's possession.
* Inventory: Defines whether the inventory is committed when the order is created or when the order is fulfilled.

![Purchase option policies](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/purchase-options/purchase-options-policies-CD0VhhEE.png)

* You can create subscriptions by configuring pricing, delivery, and billing policies.
* You can create deferred purchase options by configuring pricing, inventory, delivery, and billing policies.

  For more information, refer to [Subscriptions](/docs/apps/build/purchase-options/subscriptions) and [Deferred purchase options](/docs/apps/build/purchase-options/deferred).

### [Anchor to GraphQL Admin API objects for purchase options](/docs/apps/build/purchase-options#graphql-admin-api-objects-for-purchase-options)GraphQL Admin API objects for purchase options

The following diagram illustrates the GraphQL Admin API objects for purchase options:

![Graph Admin API object for purchase options](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/purchase-options/purchase-options-selling-plan-Dnbic69z.png)

* The [`SellingPlanGroup`](/docs/api/admin-graphql/latest/objects/sellingplangroup) object includes one or more [`SellingPlan`](/docs/api/admin-graphql/latest/objects/sellingplan) objects.
* The `SellingPlan` object specifies how a product can be sold, such as "Weekly delivery" or "Monthly delivery". Policies are organized into `SellingPlan`.
* Each `SellingPlanGroup` includes products ([`Product`](/docs/api/admin-graphql/latest/objects/product)), product variants ([`ProductVariant`](/docs/api/admin-graphql/latest/objects/productvariant)), and policy configurations (`SellingPlan`).

### [Anchor to Selling plans category](/docs/apps/build/purchase-options#selling-plans-category)Selling plans category

The `category` field represents the selling plan category that's used to filter orders by selling plan category on the order page. The `category` field supports the following approved categories:

* `SUBSCRIPTION`
* `PRE_ORDER`
* `TRY_BEFORE_YOU_BUY`

  If you want to offer a category that isn't listed above, then set the `category` field to `OTHER`, and fill out our [request form](https://docs.google.com/forms/d/e/1FAIpQLSeU18Xmw0Q61V8wdH-dfGafFqIBfRchQKUO8WAF3yJTvgyyZQ/viewform), where we'll review your request for a new selling plan category.

---

## [Anchor to Shopify's principles](/docs/apps/build/purchase-options#shopifys-principles)Shopify's principles

The following are our principles for extending the Shopify platform to support purchase options.

### [Anchor to Selling and buying products in various ways](/docs/apps/build/purchase-options#selling-and-buying-products-in-various-ways)Selling and buying products in various ways

Purchase option apps provide merchants and customers with various ways to sell and buy products, beyond the "buy now, pay now, and ship now" experience.

### [Anchor to Using checkout to ensure performance, integration, and sustainability](/docs/apps/build/purchase-options#using-checkout-to-ensure-performance-integration-and-sustainability)Using checkout to ensure performance, integration, and sustainability

[Checkout](/docs/apps/build/checkout) determines charge amounts, payment terms, and payment and shipping methods. Checkout needs to be accurate and have the highest standards of performance and reliability at global scale.

Ensuring that merchants are using Shopify's checkout guarantees performance and integration with Shopify's core feature set and ecosystem of apps. As Shopify and its ecosystem evolve, checkout is crucial to ensure a sustainable long-term journey for merchants.

### [Anchor to Modeling and storing purchase option business data in Shopify](/docs/apps/build/purchase-options#modeling-and-storing-purchase-option-business-data-in-shopify)Modeling and storing purchase option business data in Shopify

To maximize merchant success, Shopify models and stores business operational data related to purchase options. A centralized location for key purchase option business data can help merchants mitigate integrity risks and reduce synchronization costs.

Both Shopify and apps should be able to access the purchase option business data to help merchants understand and grow their business. The following are examples of purchase option business data:

* What purchase options are offered
* Who the purchase options customers are
* What products customers buy using purchase options
* How customers are paying for their purchase option orders
* How purchase option data changes over time

### [Anchor to Providing creative solutions for merchants](/docs/apps/build/purchase-options#providing-creative-solutions-for-merchants)Providing creative solutions for merchants

Merchants can use purchase options in various ways depending on the industry, product type (physical or digital), and business size. Shopify's role is to create a platform where developers can provide creative solutions for merchants to effectively manage their purchase options.

---

## [Anchor to Requirements](/docs/apps/build/purchase-options#requirements)Requirements

Note

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

**Note:**

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

### [Anchor to Access scopes](/docs/apps/build/purchase-options#access-scopes)Access scopes

To use the GraphQL Admin API for purchase options, your app needs to request the following [access scopes](/docs/api/usage/access-scopes):

Note

You must request permission for the access scopes that are marked with **permissions required**. To learn how to request permission, refer to [orders permissions](/docs/api/usage/access-scopes#orders-permissions) and [subscriptions permissions](/docs/api/usage/access-scopes#subscription-apis-permissions).

**Note:**

You must request permission for the access scopes that are marked with **permissions required**. To learn how to request permission, refer to [orders permissions](/docs/api/usage/access-scopes#orders-permissions) and [subscriptions permissions](/docs/api/usage/access-scopes#subscription-apis-permissions).

Access scopes

| Access scope | Description | Subscriptions | Deferred purchase options |
| --- | --- | --- | --- |
| `write_products` | Allows your app to write products | ✔ | ✔ |
| `read_all_orders` permissions required | Allows your app to read all orders rather than the default window of 60 days worth of orders | ✔ | ✔ |
| `read_customer_payment_methods`permissions required | Allows your app to read customer payment methods | ✔ | ✔ |
| `read_own_subscription_contracts`permissions required | Allows your app to read subscription contract mutations for contracts they own | ✔ |  |
| `write_own_subscription_contracts`permissions required | Allows your app to write subscription contract mutations for contracts they own | ✔ |  |
| `read_purchase_options` | Allows your app to read purchase options |  | ✔ |
| `write_purchase_options` | Allows your app to write purchase options |  | ✔ |
| `read_payment_mandate`permissions required | Allows your app to read payment mandates |  | ✔ |
| `write_payment_mandate`permissions required | Allows your app to write payment mandates |  | ✔ |

---

## [Anchor to Developer tools and resources](/docs/apps/build/purchase-options#developer-tools-and-resources)Developer tools and resources

To help you build and manage purchase options, Shopify offers the following developer tools and resources.

Developer tools and resources

| Tools/Resources | Description |
| --- | --- |
| [App extensions](/docs/apps/build/purchase-options/purchase-options-extensions) | Surfaces your app's purchase options in the Shopify admin |
| [App proxy](/docs/apps/build/purchase-options/customer-portal) | Fetches data from an app proxy server to display on a page of the online store. By using an app proxy, customers can have a seamless experience managing their existing agreements under the shop's domain. |
| Storefront Liquid drops and properties | Allows you to integrate purchase options into a store's theme |

---

## [Anchor to UX guidelines](/docs/apps/build/purchase-options#ux-guidelines)UX guidelines

For information on UX guidelines, refer to the following resources:

* [Subscription UX guidelines](/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines)
* [Pre-orders and try before you buy UX guidelines](/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines)

---

## [Anchor to Next steps](/docs/apps/build/purchase-options#next-steps)Next steps

* Learn about [subscriptions](/docs/apps/build/purchase-options/subscriptions)
* Learn about [deferred purchase options](/docs/apps/build/purchase-options/deferred)

---

Was this page helpful?

YesNo