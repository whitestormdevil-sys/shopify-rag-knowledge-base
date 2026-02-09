---
source: https://shopify.dev/docs/apps/selling-strategies/subscriptions/modeling
---

This guide provides an overview of how subscriptions work in Shopify and explains our approach to building support for subscriptions.

---

## [Anchor to Lifecycle of a subscription app](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#lifecycle-of-a-subscription-app)Lifecycle of a subscription app

The following diagram illustrates the lifecycle of a subscription based on the actions of the merchant, customer, Shopify, and your app:

![Subscriptions lifecycle diagram](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/subscriptions-lifecycle-Cmr9p0Fv.png)

* Merchants create and manage how they want to sell their products.
* Customers purchase subscriptions and update their subscriptions (such as changing their payment method).
* When a customer purchases a subscription, Shopify first creates a transaction and then an order. After the transaction and order are created, Shopify generates a subscription contract and creates a billing attempt on the initial purchase.
* Subsequent customer orders are automated by the app. The app creates a billing attempt based on the existing subscription contract using the API. When the app creates a billing attempt, a transaction and an order are created.
* Your app receives webhooks when subscription-related events occur, handles billing failures and scheduling, and provides a subscription management user interface for both customers and merchants.

---

## [Anchor to Building subscriptions in your app](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#building-subscriptions-in-your-app)Building subscriptions in your app

Subscription apps need to have end-to-end workflows implemented for the following areas:

* [Plan setup](#plan-setup)
* [Plan purchase and checkout](#plan-purchase-and-checkout)

* [Plan post-purchase and subscription management](#plan-post-purchase-and-subscription-management)

| Area | Task |
| --- | --- |
| Plan setup | **Save selling plans**You can use the `SellingPlanGroup` and `SellingPlan` objects to store selling plans and associate them with products or variants. Regardless of whether your app has an internal representation of selling plans, you need to save the selling plans in Shopify using the `SellingPlanGroup` and `SellingPlan` objects.Learn more about [GraphQL Admin API objects for selling plans](/docs/apps/selling-strategies/purchase-options#graphql-admin-api-objects-for-purchase-options). |
| **Set up app extensions**Your app should provide the experience for users to manage their selling plans. The app should implement an embedded UX that enables the user to set up selling plans directly from the product page, using an [app extension](/docs/apps/build/purchase-options/purchase-options-extensions).If there aren't any app extensions to modify selling plans that are associated with a given product or variant, then the selling plans are listed in a read-only state on the product page in the Shopify admin. |
| Plan purchase and checkout | **Display selling plans in the purchase flow**Shopify provides Liquid objects and the [Ajax API](/docs/api/ajax/reference/product) to enable theme developers to display the selling plans for a given product in the purchase flow. To purchase a product with a purchase option, a variant ID and a selling plan ID need to be submitted through the [Cart API](/docs/api/ajax/reference/cart).Learn more about how to [implement subscriptions in a theme](/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme). |
| **Display selling plans in the checkout**The Shopify checkout handles carts containing line items that have plans associated with them. It also handles pricing, messaging, payment method vaulting, and customer consent, which the user should customize to their needs. |
| **Create subscription contracts**The [subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts) describes the agreement between merchant and customer. The agreement includes key information, like the variant, plan, payment method to be used for subsequent billing, and the billing and shipping addresses.Shopify automatically creates subscription contracts when products with selling plans are purchased through checkout. The contract is detached from the original plan. Updating the original plan doesn't modify pre-existing subscription contracts. |
| Plan post-purchase and subscription management | **Keep contracts updated**The app should [update contracts](/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract) as necessary to make sure that it reflects the true current state of the agreement between the merchant and customer. |
| **Provide a subscription management interface**The app should provide the [customer-facing](/docs/storefronts/themes/pricing-payments/subscriptions) and [merchant-facing](/docs/apps/build/purchase-options/product-subscription-app-extensions/start-building) UX for managing subscriptions, such as upgrades and downgrades, pauses, cancellations, and product changes. |
| **Automate billing**The app should provide the automation for [billing and renewing subscriptions](/docs/apps/selling-strategies/subscriptions/contracts/create#step-4-create-a-billing-attempt). |

---

## [Anchor to Prohibited actions](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#prohibited-actions)Prohibited actions

Note

Any failure to avoid these prohibited actions constitutes a breach of the [Shopify API License and Terms of Use](https://www.shopify.com/legal/api-terms).

The prohibited actions list isn't exhaustive and might be updated at any time.

**Note:**

Any failure to avoid these prohibited actions constitutes a breach of the [Shopify API License and Terms of Use](https://www.shopify.com/legal/api-terms).

The prohibited actions list isn't exhaustive and might be updated at any time.

The following are prohibited actions for all selling plans:

* **Vaulting payment methods**: Don't vault payment methods for any purpose other than processing recurring or deferred payments.
* **Overbilling**: A selling plan specifies how to bill a customer. Don't overbill a customer.
* **Unsupported usage**: APIs are built to support only authorized selling plans, such as pre-orders, try before you buys, and subscriptions. Don't use the APIs to solve for other business use cases, such as installments, layaways, and crowdfunding campaigns.

The following are prohibited actions for subscriptions:

* **Inappropriate contract updates**: Subscription contracts only need to be updated to reflect what the customer has agreed to.
* **Unclear contracts**: The customer needs to understand what they're agreeing to. The storefront needs to clearly state the conditions of the contract.
* **Stale contracts**: Don't let contracts become stale in Shopify. As soon as a customer agrees to a contract change, the updates need to be reflected in Shopify. This helps to ensure that merchants are never locked into a particular subscription provider.

---

## [Anchor to Division of responsibilities between Shopify and apps](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#division-of-responsibilities-between-shopify-and-apps)Division of responsibilities between Shopify and apps

The division of responsibilities enables Shopify to provide a fully integrated purchase option experience and enables apps to provide innovative user-facing workflows and purchase option management automation.

The following table describes the division of responsibilities between Shopify and subscription apps:

Division of responsibilities between Shopify and apps

| Responsibility | Shopify | App |
| --- | --- | --- |
| Modeling and storing purchase option business data | ✔ |  |
| Billing and processing purchase payments (both initial purchase and renewals) | ✔ |  |
| Labeling the purchase option as a subscription |  | ✔ |
| Scheduling and automating payments, authorizing capture through the Shopify APIs and handles billing failures |  | ✔ |
| Providing customer & merchant UX for managing purchase options, both pre-purchase and post-purchase |  | ✔ |

---

## [Anchor to Subscriptions on multiple channels](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#subscriptions-on-multiple-channels)Subscriptions on multiple channels

Subscriptions can be sold across different sales channels:

* Online Store: Customers can purchase subscriptions through the merchant's online storefront.
* Shopify POS: Merchants can sell subscriptions in-store.

For more information about selling subscriptions on POS, including limitations and implementation details, refer to [Subscriptions on Shopify POS](/docs/apps/build/purchase-options/subscriptions#pos-support).

---

## [Anchor to Developer tools and resources](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to learn more about building subscriptions.

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

SellingPlanGroup object

Consult the GraphQL Admin API reference to learn more about the SellingPlanGroup object.

SellingPlanGroup object

Consult the GraphQL Admin API reference to learn more about the SellingPlanGroup object.](/docs/api/admin-graphql/latest/objects/sellingplangroup)

[SellingPlanGroup object  
  

Consult the GraphQL Admin API reference to learn more about the SellingPlanGroup object.](/docs/api/admin-graphql/latest/objects/sellingplangroup)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

SellingPlan object

Consult the GraphQL Admin API reference to learn more about the SellingPlan object.

SellingPlan object

Consult the GraphQL Admin API reference to learn more about the SellingPlan object.](/docs/api/admin-graphql/latest/objects/sellingplan)

[SellingPlan object  
  

Consult the GraphQL Admin API reference to learn more about the SellingPlan object.](/docs/api/admin-graphql/latest/objects/sellingplan)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

SubscriptionContract object

Consult the GraphQL Admin API reference to learn more about the SubscriptionContract object.

SubscriptionContract object

Consult the GraphQL Admin API reference to learn more about the SubscriptionContract object.](/docs/api/admin-graphql/latest/objects/subscriptioncontract)

[SubscriptionContract object  
  

Consult the GraphQL Admin API reference to learn more about the SubscriptionContract object.](/docs/api/admin-graphql/latest/objects/subscriptioncontract)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

SubscriptionBillingCycle object

Consult the GraphQL Admin API reference to learn more about the SubscriptionBillingCycle object.

SubscriptionBillingCycle object

Consult the GraphQL Admin API reference to learn more about the SubscriptionBillingCycle object.](/docs/api/admin-graphql/latest/objects/subscriptionbillingcycle)

[SubscriptionBillingCycle object  
  

Consult the GraphQL Admin API reference to learn more about the SubscriptionBillingCycle object.](/docs/api/admin-graphql/latest/objects/subscriptionbillingcycle)

---

## [Anchor to Next steps](/docs/apps/build/purchase-options/subscriptions/model-subscriptions-solution#next-steps)Next steps

* Learn how to use [selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans) to control the methods through which products or variants can be sold and purchased.
* Learn how to use [contracts](/docs/apps/build/purchase-options/subscriptions/contracts) to create and manage the agreements between a merchant and a customer.

---

Was this page helpful?

YesNo