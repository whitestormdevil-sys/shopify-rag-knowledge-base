---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/customerCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_customers` access scope.

Creates a new [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer) in the store.

Accepts customer details including contact information, marketing consent preferences, and tax exemptions through the [`CustomerInput`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/CustomerInput) input object. You can also associate [`metafields`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/MetafieldInput) and tags to organize and extend customer data.

Apps using protected customer data must meet Shopify's [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements).

* input (CustomerInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/customerCreate#arguments-input)input •[CustomerInput!](/docs/api/admin-graphql/latest/input-objects/CustomerInput) required
:   The input fields to create a customer.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CustomerCreatePayload returns](/docs/api/admin-graphql/latest/mutations/customerCreate#returns)CustomerCreatePayload returns

* customer (Customer)
* userErrors ([UserError!]!)

[Anchor to customer](/docs/api/admin-graphql/latest/mutations/customerCreate#returns-customer)customer •[Customer](/docs/api/admin-graphql/latest/objects/Customer)
:   The created customer.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/customerCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo