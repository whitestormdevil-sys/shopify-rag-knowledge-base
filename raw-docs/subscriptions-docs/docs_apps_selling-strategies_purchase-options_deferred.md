---
source: https://shopify.dev/docs/apps/selling-strategies/purchase-options/deferred
---

Pre-order and TBYB apps enable flexible payments and fulfillments on product variants. This guide describes how these apps work, their requirements, and their limitations.

---

## [Anchor to How it works](/docs/apps/build/purchase-options/deferred#how-it-works)How it works

You can create pre-order and TBYB options with [`sellingPlanGroupCreate`](/docs/api/admin-graphql/latest/mutations/sellingPlanGroupCreate) mutation.

There's no single API to create a specific pre-order or TBYB option. Instead, a pre-order or TBYB option has configurations for [pricing, delivery, inventory, and billing policies](/docs/apps/build/purchase-options#how-do-purchase-options-work). This enables you to build more flexible and extensible apps that support various ways to sell and buy products.

### [Anchor to Pricing policy](/docs/apps/build/purchase-options/deferred#pricing-policy)Pricing policy

The `pricingPolicies` field defines pricing changes on a given product variant. Pricing policies enable merchants to adjust prices on pre-order and TBYB orders by setting `adjustmentType` and `adjustmentValue`. Pricing policies work in conjunction with [price lists](/docs/apps/build/markets/catalogs-different-markets).

Note

* Configuring pricing policies is optional.
* Pre-order and TBYB options can have only one `fixed` pricing policy. `recurring` pricing policies aren't available for pre-order and TBYB options.

**Note:**

* Configuring pricing policies is optional.
* Pre-order and TBYB options can have only one `fixed` pricing policy. `recurring` pricing policies aren't available for pre-order and TBYB options.

### [Anchor to Delivery policy](/docs/apps/build/purchase-options/deferred#delivery-policy)Delivery policy

The `deliveryPolicy` field defines when the order should be fulfilled, from the time that the order is created to the time that it leaves the merchant's possession. The order can be fulfilled as soon as possible (`ASAP`) or on a specific date (`EXACT_TIME`). If the fulfillment timeline depends on other conditions, then the fulfillment timeline can be set to unknown (`UNKNOWN`).

### [Anchor to Inventory policy](/docs/apps/build/purchase-options/deferred#inventory-policy)Inventory policy

The `inventoryPolicy` field defines whether the inventory is committed when the order is created (`ON_SALE`) or when the order is fulfilled (`ON_FULFILLMENT`). This helps merchants manage inventory when there are orders with delayed fulfillments.

### [Anchor to Billing policy](/docs/apps/build/purchase-options/deferred#billing-policy)Billing policy

The `billingPolicy` field defines the intervals of time between the placement of an order and payment collection.

When configuring the billing policy, you can set checkout charges for pre-order or TBYB options to secure customers' commitments to orders before the orders are fulfilled. When you set a checkout charge, a partial amount is charged at checkout, and the remaining balance amount is charged on a specific date (`EXACT_TIME`) or X days after checkout (`TIME_AFTER_CHECKOUT`). You can set the checkout charge value to `0` to charge the full amount at checkout.

Note

Delivery and billing policies must be either all `recurring` or all `fixed`.

* Use `recurring` policies for subscriptions.
* Use `fixed` policies for pre-orders and TBYB

**Note:**

Delivery and billing policies must be either all `recurring` or all `fixed`.

* Use `recurring` policies for subscriptions.
* Use `fixed` policies for pre-orders and TBYB

Shopify will store a customer's payment method so that merchants can collect the remaining balance amount without contacting the customer.

To learn more about policy configuration, refer to [Create and manage pre-orders and TBYB](/docs/apps/build/purchase-options/deferred/build-deferment-solution).

### [Anchor to Selling plan categories](/docs/apps/build/purchase-options/deferred#selling-plan-categories)Selling plan categories

The `category` field represents the selling plan category that's used to filter orders by selling plan category on the order page. The `category` field supports the following approved categories:

* `SUBSCRIPTION`
* `PRE_ORDER`
* `TRY_BEFORE_YOU_BUY`

  If you want to offer a category that isn't listed above, then set the `category` field to `OTHER`, and fill out our [request form](https://docs.google.com/forms/d/e/1FAIpQLSeU18Xmw0Q61V8wdH-dfGafFqIBfRchQKUO8WAF3yJTvgyyZQ/viewform), where we'll review your request for a new selling plan category.

---

## [Anchor to Charging the remaining balance](/docs/apps/build/purchase-options/deferred#charging-the-remaining-balance)Charging the remaining balance

A [`PaymentMandate`](/docs/api/admin-graphql/latest/objects/PaymentMandate) is the payment method and permission that a customer gives to the merchant to debit money. You can use the [`orderCreateMandatePayment`](/docs/api/admin-graphql/unstable/mutations/orderCreateMandatePayment) mutation to use a customer's payment mandate to trigger a payment for the remaining balance on an order or create a payment schedule. You can query `vaultedPaymentMethods` on the [`Order`](/docs/api/admin-graphql/latest/objects/Order#field-order-paymentcollectiondetails) object to retrieve the list of available payment mandates.

Note

The `orderCreateMandatePayment` mutation is idempotent and requires a unique `idempotencyKey`. The payment attempts with the same `idempotencyKey` will return the same result of a previous payment rather than create a new payment. Learn more about [idempotent requests](/docs/api/usage/idempotent-requests).

**Note:**

The `orderCreateMandatePayment` mutation is idempotent and requires a unique `idempotencyKey`. The payment attempts with the same `idempotencyKey` will return the same result of a previous payment rather than create a new payment. Learn more about [idempotent requests](/docs/api/usage/idempotent-requests).

Orders with a deferred payment will have an attached payment term that indicates when the payment should be made and how. You can query the [`PaymentTerms`](/docs/api/admin-graphql/latest/objects/paymentterms) object to check the payment terms and when the remaining balance amount is due on a given order. To poll the payment status, you can use the [`orderPaymentStatus`](/docs/api/admin-graphql/latest/queries/orderPaymentStatus) query.

It's your app's responsibility to schedule the charge at the right time and automate any process around payment failures. To learn more about your app's responsibilities, refer to [the division of responsibilities between Shopify and apps](/docs/apps/build/purchase-options/deferred/model-deferred-purchase-solutions#division-of-responsibilities-between-shopify-and-apps).

---

## [Anchor to Use cases](/docs/apps/build/purchase-options/deferred#use-cases)Use cases

Note

Shopify supports pre-orders and TBYB as use cases. However, you can also create custom use cases by configuring policies.

**Note:**

Shopify supports pre-orders and TBYB as use cases. However, you can also create custom use cases by configuring policies.

The following diagram illustrates how you can create pre-order and TBYB options:

![Pre-order and try before you buy policies](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/purchase-options/purchase-options-deferred-CrMH8xoV.png)

### [Anchor to Pre-order](/docs/apps/build/purchase-options/deferred#pre-order)Pre-order

* A 20% price reduction will be applied on the variant.
* The product will be fulfilled on 2022-07-01.
* The inventory will be updated when the order is created.
* The 10% of the total amount will be charged as a deposit at checkout. The remaining amount will be charged on 2022-07-01, when the product is fulfilled.

### [Anchor to Try before you buy](/docs/apps/build/purchase-options/deferred#try-before-you-buy)Try before you buy

* The product will be fulfilled as soon as possible.
* The inventory will be updated when the order is created.
* There's no deposit. The full amount will be charged 14 days after checkout.

---

## [Anchor to Orders with multiple due dates and deposits](/docs/apps/build/purchase-options/deferred#orders-with-multiple-due-dates-and-deposits)Orders with multiple due dates and deposits

Orders can include multiple products with different deferred payment due dates, and can also use [Payment Customization Functions](/docs/api/functions/latest/payment-customization) that set payment terms. However, each order can have only one deferred payment due date. Shopify determines the due dates and deposit amounts according to the following rules:

### [Anchor to How due dates are determined](/docs/apps/build/purchase-options/deferred#how-due-dates-are-determined)How due dates are determined

* **Multiple selling plan due dates:** When a cart contains multiple lines with a selling plan and different due dates, only the earliest due date is applied.
* **Due on fulfillment priority:** When a cart contains multiple lines with a selling plan and at least one is due on fulfillment, the due on fulfillment payment term takes precedence over any specific date.

Note

For pre-order selling plans, due on fulfillment is currently available in the `unstable` API version. We plan to release it to stable in the `2026-01` stable release.

**Note:**

For pre-order selling plans, due on fulfillment is currently available in the `unstable` API version. We plan to release it to stable in the `2026-01` stable release.

### [Anchor to How deposits are calculated](/docs/apps/build/purchase-options/deferred#how-deposits-are-calculated)How deposits are calculated

* **Selling plan deposits:** Lines with selling plans use the deposit specified by the selling plan configuration. Payment Customization Function deposits don't apply to these products.
* **Total deposit:** All deposits are summed and charged at checkout.

### [Anchor to Payment Customization Functions](/docs/apps/build/purchase-options/deferred#payment-customization-functions)Payment Customization Functions

* **Due dates:** The returned payment terms from the Payment Customization Function are only considered when the cart contains at least one line not associated to a selling plan. Due dates follow the same rules as selling plans: earliest date applies, due on fulfillment takes precedence.
* **Deposits:** Apply to all lines without a selling plan.

---

## [Anchor to Limitations](/docs/apps/build/purchase-options/deferred#limitations)Limitations

The following are known limitations for Subscriptions, pre-orders and TBYB:

* Customers can't use [local payment methods](https://help.shopify.com/manual/payments/shopify-payments/local-payment-methods) for subscriptions, pre-orders and TBYB.
* Pre-orders and TBYB can't be used through Shopify POS. Subscriptions are supported on Shopify POS. For limitations specific to subscriptions on POS, see [Shopify POS limitations for subscriptions](/docs/apps/build/purchase-options/subscriptions#pos-limitations).
* Subscriptions, pre-orders and TBYB can't be used on draft orders.
* Subscriptions, pre-orders and TBYB can't be used with [B2B](/docs/apps/build/b2b).
* Subscriptions, pre-orders and TBYB don't support "Buy X get Y" discounts.

* To use pre-order and TBYB options, merchants need to use one of the following payment gateways:
  + [Shopify Payments](https://help.shopify.com/manual/payments/shopify-payments)
  + [PayPal Express](https://help.shopify.com/manual/payments/paypal)
  + [Adyen on Shopify](https://help.shopify.com/en/manual/payments/third-party-providers/adyen-gateway)
  + Stripe, which is only available to some merchants
* The [Order Edits API](/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders) only supports removing a product with a pre-orders or TBYB.
* Pre-order and TBYB options aren't supported on stores with checkouts customized using [`checkout.liquid`](/docs/storefronts/themes/architecture/layouts/checkout-liquid).

  Instead, you need to [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations).
* Pre-order and TBYB options don't support [cart permalinks](/docs/apps/build/checkout/create-cart-permalinks).

---

## [Anchor to Next steps](/docs/apps/build/purchase-options/deferred#next-steps)Next steps

* Learn about [modeling pre-order and TBYB apps](/docs/apps/build/purchase-options/deferred/model-deferred-purchase-solutions).

---

Was this page helpful?

YesNo