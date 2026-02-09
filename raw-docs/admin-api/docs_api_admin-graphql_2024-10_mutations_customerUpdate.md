---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/customerUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_customers` access scope.

Updates a [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer)'s attributes including personal information and [`tax exemptions`](https://shopify.dev/docs/api/admin-graphql/latest/enums/TaxExemption).

Apps using protected customer data must meet Shopify's [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements).

* input (CustomerInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/customerUpdate#arguments-input)input •[CustomerInput!](/docs/api/admin-graphql/latest/input-objects/CustomerInput) required
:   Provides updated fields for the customer. To set marketing consent, use the `customerEmailMarketingConsentUpdate` or `customerSmsMarketingConsentUpdate` mutations instead.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CustomerUpdatePayload returns](/docs/api/admin-graphql/latest/mutations/customerUpdate#returns)CustomerUpdatePayload returns

* customer (Customer)
* userErrors ([UserError!]!)

[Anchor to customer](/docs/api/admin-graphql/latest/mutations/customerUpdate#returns-customer)customer •[Customer](/docs/api/admin-graphql/latest/objects/Customer)
:   The updated customer.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/customerUpdate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo