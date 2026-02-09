---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/customerAccessTokenCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_write_customers` access scope.

Creates a customer access token.
The customer access token is required to modify the customer object in any way.

* input (CustomerAccessTokenCreateInput!)

[Anchor to input](/docs/api/storefront/latest/mutations/customerAccessTokenCreate#arguments-input)input •[CustomerAccessTokenCreateInput!](/docs/api/storefront/latest/input-objects/CustomerAccessTokenCreateInput) required
:   The fields used to create a customer access token.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CustomerAccessTokenCreatePayload returns](/docs/api/storefront/latest/mutations/customerAccessTokenCreate#returns)CustomerAccessTokenCreatePayload returns

* customerAccessToken (CustomerAccessToken)
* customerUserErrors ([CustomerUserError!]!)
* userErrors ([UserError!]!): deprecated

[Anchor to customerAccessToken](/docs/api/storefront/latest/mutations/customerAccessTokenCreate#returns-customerAccessToken)customerAccessToken •[CustomerAccessToken](/docs/api/storefront/latest/objects/CustomerAccessToken)
:   The newly created customer access token object.

    Show fields

[Anchor to customerUserErrors](/docs/api/storefront/latest/mutations/customerAccessTokenCreate#returns-customerUserErrors)customerUserErrors •[[CustomerUserError!]!](/docs/api/storefront/latest/objects/CustomerUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/customerAccessTokenCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/storefront/latest/objects/UserError) non-nullDeprecated
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo