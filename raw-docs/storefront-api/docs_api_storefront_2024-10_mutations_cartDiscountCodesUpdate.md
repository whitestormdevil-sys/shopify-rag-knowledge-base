---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/cartDiscountCodesUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Updates the discount codes applied to the cart.

* cartId (ID!)
* discountCodes ([String!]!)

[Anchor to cartId](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#arguments-cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
:   The ID of the cart.

[Anchor to discountCodes](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#arguments-discountCodes)discountCodes •[[String!]!](/docs/api/storefront/latest/scalars/String) required
:   The case-insensitive discount codes that the customer added at checkout.

    The input must not contain more than `250` values.

---

Was this section helpful?

YesNo

## [Anchor to CartDiscountCodesUpdatePayload returns](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#returns)CartDiscountCodesUpdatePayload returns

* cart (Cart)
* userErrors ([CartUserError!]!)
* warnings ([CartWarning!]!)

[Anchor to cart](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#returns-cart)cart •[Cart](/docs/api/storefront/latest/objects/Cart)
:   The updated cart.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#returns-userErrors)userErrors •[[CartUserError!]!](/docs/api/storefront/latest/objects/CartUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to warnings](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate#returns-warnings)warnings •[[CartWarning!]!](/docs/api/storefront/latest/objects/CartWarning) non-null
:   A list of warnings that occurred during the mutation.

    Show fields

---

Was this section helpful?

YesNo