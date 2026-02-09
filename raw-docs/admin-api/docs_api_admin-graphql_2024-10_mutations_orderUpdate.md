---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/orderUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_orders` access scope, `write_marketplace_orders` access scope or `write_quick_sale` access scope. Also: The app must have the `write_pos_staff_member_event_attribution_overrides` access scope to assign events to another staff member.

Updates the attributes of an order, such as the customer's email, the shipping address for the order,
tags, and [metafields](https://shopify.dev/docs/apps/build/custom-data) associated with the order.

If you need to make significant updates to an order, such as adding or removing line items, changing
quantities, or modifying discounts, then use
the [`orderEditBegin`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderEditBegin)
mutation instead. The `orderEditBegin` mutation initiates an order editing session,
allowing you to make multiple changes before finalizing them. Learn more about using the `orderEditBegin`
mutation to [edit existing orders](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders).

If you need to remove a customer from an order, then use the [`orderCustomerRemove`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCustomerRemove)
mutation instead.

Learn how to build apps that integrate with
[order management and fulfillment processes](https://shopify.dev/docs/apps/build/orders-fulfillment).

* input (OrderInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/orderUpdate#arguments-input)input •[OrderInput!](/docs/api/admin-graphql/latest/input-objects/OrderInput) required
:   The attributes of the updated order.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to OrderUpdatePayload returns](/docs/api/admin-graphql/latest/mutations/orderUpdate#returns)OrderUpdatePayload returns

* order (Order)
* userErrors ([UserError!]!)

[Anchor to order](/docs/api/admin-graphql/latest/mutations/orderUpdate#returns-order)order •[Order](/docs/api/admin-graphql/latest/objects/Order)
:   The updated order.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/orderUpdate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo