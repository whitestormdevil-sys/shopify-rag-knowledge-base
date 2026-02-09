---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/customerCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_write_customers` access scope.

Creates a new customer.

* input (CustomerCreateInput!)

[Anchor to input](/docs/api/storefront/latest/mutations/customerCreate#arguments-input)input •[CustomerCreateInput!](/docs/api/storefront/latest/input-objects/CustomerCreateInput) required
:   The fields used to create a new customer.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CustomerCreatePayload returns](/docs/api/storefront/latest/mutations/customerCreate#returns)CustomerCreatePayload returns

* customer (Customer)
* customerUserErrors ([CustomerUserError!]!)
* userErrors ([UserError!]!): deprecated

[Anchor to customer](/docs/api/storefront/latest/mutations/customerCreate#returns-customer)customer •[Customer](/docs/api/storefront/latest/objects/Customer)
:   The created customer object.

    Show fields

[Anchor to customerUserErrors](/docs/api/storefront/latest/mutations/customerCreate#returns-customerUserErrors)customerUserErrors •[[CustomerUserError!]!](/docs/api/storefront/latest/objects/CustomerUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/customerCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/storefront/latest/objects/UserError) non-nullDeprecated
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo