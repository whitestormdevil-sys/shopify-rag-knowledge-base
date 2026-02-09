---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/draftOrderCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_draft_orders` access scope or `write_quick_sale` access scope. Also: The user must have access to manage draft orders.

Creates a [draft order](https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder)
with attributes such as customer information, line items, shipping and billing addresses, and payment terms.
Draft orders are useful for merchants that need to:

* Create new orders for sales made by phone, in person, by chat, or elsewhere. When a merchant accepts payment for a draft order, an order is created.
* Send invoices to customers with a secure checkout link.
* Use custom items to represent additional costs or products not in inventory.
* Re-create orders manually from active sales channels.
* Sell products at discount or wholesale rates.
* Take pre-orders.

After creating a draft order, you can:

* Send an invoice to the customer using the [`draftOrderInvoiceSend`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderInvoiceSend) mutation.
* Complete the draft order using the [`draftOrderComplete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderComplete) mutation.
* Update the draft order using the [`draftOrderUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderUpdate) mutation.
* Duplicate a draft order using the [`draftOrderDuplicate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderDuplicate) mutation.
* Delete the draft order using the [`draftOrderDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderDelete) mutation.

---

Note

When you create a draft order, you can't [reserve or hold inventory](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states) for the items in the order by default.
However, you can reserve inventory using the [`reserveInventoryUntil`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderCreate#arguments-input.fields.reserveInventoryUntil) input.

**Note:**

When you create a draft order, you can't [reserve or hold inventory](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states) for the items in the order by default.
However, you can reserve inventory using the [`reserveInventoryUntil`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderCreate#arguments-input.fields.reserveInventoryUntil) input.

**Note:** When you create a draft order, you can&#39;t <a href="https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states">reserve or hold inventory</a> for the items in the order by default.
However, you can reserve inventory using the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/draftOrderCreate#arguments-input.fields.reserveInventoryUntil"><code><span class="PreventFireFoxApplyingGapToWBR">reserve<wbr/>Inventory<wbr/>Until</span></code></a> input.

---

* input (DraftOrderInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/draftOrderCreate#arguments-input)input •[DraftOrderInput!](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput) required
:   The fields used to create the draft order.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to DraftOrderCreatePayload returns](/docs/api/admin-graphql/latest/mutations/draftOrderCreate#returns)DraftOrderCreatePayload returns

* draftOrder (DraftOrder)
* userErrors ([UserError!]!)

[Anchor to draftOrder](/docs/api/admin-graphql/latest/mutations/draftOrderCreate#returns-draftOrder)draftOrder •[DraftOrder](/docs/api/admin-graphql/latest/objects/DraftOrder)
:   The created draft order.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/draftOrderCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo