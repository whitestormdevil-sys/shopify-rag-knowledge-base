---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/orderCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_orders` access scope. Also: This mutation is only accessible to apps authenticated using [offline tokens](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/offline-access-tokens).

Creates an order with attributes such as customer information, line items, and shipping and billing addresses.

Use the `orderCreate` mutation to programmatically generate orders in scenarios where
orders aren't created through the standard checkout process, such as when importing orders from an external
system or creating orders for wholesale customers.

The `orderCreate` mutation doesn't support applying multiple discounts, such as discounts on line items.
Automatic discounts won't be applied unless you replicate the logic of those discounts in your custom
implementation. You can [apply a discount code](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/OrderCreateDiscountCodeInput),
but only one discount code can be set for each order.

---

Note

If you're using the `orderCreate` mutation with a
[trial](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/free-trial) or
[development store](https://shopify.dev/docs/api/development-stores), then you can create a
maximum of five new orders per minute.

**Note:**

If you're using the `orderCreate` mutation with a
[trial](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/free-trial) or
[development store](https://shopify.dev/docs/api/development-stores), then you can create a
maximum of five new orders per minute.

**Note:** If you&#39;re using the <code><span class="PreventFireFoxApplyingGapToWBR">order<wbr/>Create</span></code> mutation with a
<a href="https://help.shopify.com/manual/intro-to-shopify/pricing-plans/free-trial">trial</a> or
<a href="https://shopify.dev/docs/api/development-stores">development store</a>, then you can create a
maximum of five new orders per minute.

---

After you create an order, you can make subsequent edits to the order using one of the following mutations:

* [`orderUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderUpdate):
  Used for simple updates to an order, such as changing the order's note, tags, or customer information.
* [`orderEditBegin`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderEditBegin):
  Used when you need to make significant updates to an order, such as adding or removing line items, changing
  quantities, or modifying discounts. The `orderEditBegin` mutation initiates an order editing session,
  allowing you to make multiple changes before finalizing them. Learn more about using the `orderEditBegin`
  mutation to [edit existing orders](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders).

Learn how to build apps that integrate with
[order management and fulfillment processes](https://shopify.dev/docs/apps/build/orders-fulfillment).

* options (OrderCreateOptionsInput)
* order (OrderCreateOrderInput!)

[Anchor to options](/docs/api/admin-graphql/latest/mutations/orderCreate#arguments-options)options •[OrderCreateOptionsInput](/docs/api/admin-graphql/latest/input-objects/OrderCreateOptionsInput)
:   The strategies for updating inventory and whether to send shipping and order confirmations to customers.

    Show input fields

[Anchor to order](/docs/api/admin-graphql/latest/mutations/orderCreate#arguments-order)order •[OrderCreateOrderInput!](/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput) required
:   The attributes of the new order.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to OrderCreatePayload returns](/docs/api/admin-graphql/latest/mutations/orderCreate#returns)OrderCreatePayload returns

* order (Order)
* userErrors ([OrderCreateUserError!]!)

[Anchor to order](/docs/api/admin-graphql/latest/mutations/orderCreate#returns-order)order •[Order](/docs/api/admin-graphql/latest/objects/Order)
:   The order that was created.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/orderCreate#returns-userErrors)userErrors •[[OrderCreateUserError!]!](/docs/api/admin-graphql/latest/objects/OrderCreateUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo