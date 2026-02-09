---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/draftOrderComplete
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_draft_orders` access scope. Also: The user must have access to mark as paid, or set payment terms.

Completes a [draft order](https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder) and
converts it into a [regular order](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order).
The order appears in the merchant's orders list, and the customer can be notified about their order.

Use the `draftOrderComplete` mutation when a merchant is ready to finalize a draft order and create a real
order in their store. The `draftOrderComplete` mutation also supports sales channel attribution for tracking
order sources using the [`sourceName`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderComplete#arguments-sourceName)
argument, [cart validation](https://shopify.dev/docs/apps/build/checkout/cart-checkout-validation)
controls for app integrations, and detailed error reporting for failed completions.

You can complete a draft order with different [payment scenarios](https://help.shopify.com/manual/fulfillment/managing-orders/payments):

* Mark the order as paid immediately.
* Set the order as payment pending using [payment terms](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentTerms).
* Specify a custom payment amount.
* Select a specific payment gateway.

---

Note

When completing a draft order, inventory is [reserved](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states)
for the items in the order. This means the items will no longer be available for other customers to purchase.
Make sure to verify inventory availability before completing the draft order.

**Note:**

When completing a draft order, inventory is [reserved](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states)
for the items in the order. This means the items will no longer be available for other customers to purchase.
Make sure to verify inventory availability before completing the draft order.

**Note:** When completing a draft order, inventory is <a href="https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states">reserved</a>
for the items in the order. This means the items will no longer be available for other customers to purchase.
Make sure to verify inventory availability before completing the draft order.

---

* id (ID!)
* paymentGatewayId (ID)
* sourceName (String)
* paymentPending (Boolean): deprecated

[Anchor to id](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#arguments-id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
:   The draft order to complete.

[Anchor to paymentGatewayId](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#arguments-paymentGatewayId)paymentGatewayId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   The gateway for the completed draft order.

[Anchor to sourceName](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#arguments-sourceName)sourceName •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A channel definition handle used for sales channel attribution.

[Anchor to paymentPending](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#arguments-paymentPending)paymentPending •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) DeprecatedDefault:false

---

Was this section helpful?

YesNo

## [Anchor to DraftOrderCompletePayload returns](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#returns)DraftOrderCompletePayload returns

* draftOrder (DraftOrder)
* userErrors ([UserError!]!)

[Anchor to draftOrder](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#returns-draftOrder)draftOrder •[DraftOrder](/docs/api/admin-graphql/latest/objects/DraftOrder)
:   The completed draft order.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/draftOrderComplete#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo