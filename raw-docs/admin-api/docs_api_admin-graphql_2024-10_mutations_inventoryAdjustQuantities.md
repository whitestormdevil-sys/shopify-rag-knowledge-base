---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/inventoryAdjustQuantities
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_inventory` access scope. Also: The user must have a permission to apply changes to inventory quantities.

Adjusts quantities for inventory items by applying incremental changes at specific locations. Each adjustment modifies the quantity by a delta value rather than setting an absolute amount.

The mutation tracks adjustments with a reason code and optional reference URI for audit trails. Returns an [`InventoryAdjustmentGroup`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryAdjustmentGroup) that records all changes made in the operation.

Learn more about [managing inventory quantities and states](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#adjust-inventory-quantities).

---

Caution

As of version `2026-01`, this mutation supports an optional idempotency key using the `@idempotent` directive.
As of version `2026-04`, the idempotency key is required and must be provided using the `@idempotent` directive.
For more information, see the [idempotency documentation](https://shopify.dev/docs/api/usage/idempotent-requests).

**Caution:**

As of version `2026-01`, this mutation supports an optional idempotency key using the `@idempotent` directive.
As of version `2026-04`, the idempotency key is required and must be provided using the `@idempotent` directive.
For more information, see the [idempotency documentation](https://shopify.dev/docs/api/usage/idempotent-requests).

**Caution:** As of version <code>2026-01</code>, this mutation supports an optional idempotency key using the <code>@idempotent</code> directive.
As of version <code>2026-04</code>, the idempotency key is required and must be provided using the <code>@idempotent</code> directive.
For more information, see the <a href="https://shopify.dev/docs/api/usage/idempotent-requests">idempotency documentation</a>.

---

* input (InventoryAdjustQuantitiesInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities#arguments-input)input •[InventoryAdjustQuantitiesInput!](/docs/api/admin-graphql/latest/input-objects/InventoryAdjustQuantitiesInput) required
:   The information required to adjust inventory quantities.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to InventoryAdjustQuantitiesPayload returns](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities#returns)InventoryAdjustQuantitiesPayload returns

* inventoryAdjustmentGroup (InventoryAdjustmentGroup)
* userErrors ([InventoryAdjustQuantitiesUserError!]!)

[Anchor to inventoryAdjustmentGroup](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities#returns-inventoryAdjustmentGroup)inventoryAdjustmentGroup •[InventoryAdjustmentGroup](/docs/api/admin-graphql/latest/objects/InventoryAdjustmentGroup)
:   The group of changes made by the operation.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/inventoryAdjustQuantities#returns-userErrors)userErrors •[[InventoryAdjustQuantitiesUserError!]!](/docs/api/admin-graphql/latest/objects/InventoryAdjustQuantitiesUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo