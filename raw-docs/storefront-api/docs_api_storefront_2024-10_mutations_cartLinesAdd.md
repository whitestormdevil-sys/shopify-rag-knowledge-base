---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/cartLinesAdd
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Adds a merchandise line to the cart.

* cartId (ID!)
* lines ([CartLineInput!]!)

[Anchor to cartId](/docs/api/storefront/latest/mutations/cartLinesAdd#arguments-cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
:   The ID of the cart.

[Anchor to lines](/docs/api/storefront/latest/mutations/cartLinesAdd#arguments-lines)lines •[[CartLineInput!]!](/docs/api/storefront/latest/input-objects/CartLineInput) required
:   A list of merchandise lines to add to the cart.

    The input must not contain more than `250` values.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CartLinesAddPayload returns](/docs/api/storefront/latest/mutations/cartLinesAdd#returns)CartLinesAddPayload returns

* cart (Cart)
* userErrors ([CartUserError!]!)
* warnings ([CartWarning!]!)

[Anchor to cart](/docs/api/storefront/latest/mutations/cartLinesAdd#returns-cart)cart •[Cart](/docs/api/storefront/latest/objects/Cart)
:   The updated cart.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/cartLinesAdd#returns-userErrors)userErrors •[[CartUserError!]!](/docs/api/storefront/latest/objects/CartUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to warnings](/docs/api/storefront/latest/mutations/cartLinesAdd#returns-warnings)warnings •[[CartWarning!]!](/docs/api/storefront/latest/objects/CartWarning) non-null
:   A list of warnings that occurred during the mutation.

    Show fields

---

Was this section helpful?

YesNo