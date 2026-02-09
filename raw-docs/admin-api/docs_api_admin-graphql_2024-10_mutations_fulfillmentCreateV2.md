---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreateV2
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_assigned_fulfillment_orders` access scope, `write_merchant_managed_fulfillment_orders` access scope or `write_third_party_fulfillment_orders` access scope. Also: The user must have fulfill\_and\_ship\_orders permission.

Deprecated. Use [fulfillmentCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentCreate) instead.

Creates a fulfillment for one or many fulfillment orders.
The fulfillment orders are associated with the same order and are assigned to the same location.

* fulfillment (FulfillmentV2Input!)
* message (String)

[Anchor to fulfillment](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2#arguments-fulfillment)fulfillment •[FulfillmentV2Input!](/docs/api/admin-graphql/latest/input-objects/FulfillmentV2Input) required
:   The input fields used to create a fulfillment from fulfillment orders.

    Show input fields

[Anchor to message](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2#arguments-message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
:   An optional message for the fulfillment request.

---

Was this section helpful?

YesNo

## [Anchor to FulfillmentCreateV2Payload returns](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2#returns)FulfillmentCreateV2Payload returns

* fulfillment (Fulfillment)
* userErrors ([UserError!]!)

[Anchor to fulfillment](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2#returns-fulfillment)fulfillment •[Fulfillment](/docs/api/admin-graphql/latest/objects/Fulfillment)
:   The created fulfillment.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo