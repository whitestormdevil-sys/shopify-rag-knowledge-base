---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/cartLinesRemove
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Removes one or more merchandise lines from the cart.

* cartId (ID!)
* lineIds ([ID!]!)

[Anchor to cartId](/docs/api/storefront/latest/mutations/cartLinesRemove#arguments-cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
:   The ID of the cart.

[Anchor to lineIds](/docs/api/storefront/latest/mutations/cartLinesRemove#arguments-lineIds)lineIds •[[ID!]!](/docs/api/storefront/latest/scalars/ID) required
:   The merchandise line IDs to remove.

    The input must not contain more than `250` values.

---

Was this section helpful?

YesNo

## [Anchor to CartLinesRemovePayload returns](/docs/api/storefront/latest/mutations/cartLinesRemove#returns)CartLinesRemovePayload returns

* cart (Cart)
* userErrors ([CartUserError!]!)
* warnings ([CartWarning!]!)

[Anchor to cart](/docs/api/storefront/latest/mutations/cartLinesRemove#returns-cart)cart •[Cart](/docs/api/storefront/latest/objects/Cart)
:   The updated cart.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/cartLinesRemove#returns-userErrors)userErrors •[[CartUserError!]!](/docs/api/storefront/latest/objects/CartUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to warnings](/docs/api/storefront/latest/mutations/cartLinesRemove#returns-warnings)warnings •[[CartWarning!]!](/docs/api/storefront/latest/objects/CartWarning) non-null
:   A list of warnings that occurred during the mutation.

    Show fields

---

Was this section helpful?

YesNo