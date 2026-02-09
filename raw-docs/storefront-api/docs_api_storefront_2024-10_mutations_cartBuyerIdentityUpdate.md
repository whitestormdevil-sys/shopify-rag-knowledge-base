---
source: https://shopify.dev/docs/api/storefront/2024-10/mutations/cartBuyerIdentityUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Updates customer information associated with a cart.
Buyer identity is used to determine
[international pricing](https://shopify.dev/custom-storefronts/internationalization/international-pricing)
and should match the customer's shipping address.

* buyerIdentity (CartBuyerIdentityInput!)
* cartId (ID!)

[Anchor to buyerIdentity](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#arguments-buyerIdentity)buyerIdentity •[CartBuyerIdentityInput!](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput) required
:   The customer associated with the cart. Used to determine
    [international pricing](https://shopify.dev/custom-storefronts/internationalization/international-pricing).
    Buyer identity should match the customer's shipping address.

    Show input fields

[Anchor to cartId](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#arguments-cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
:   The ID of the cart.

---

Was this section helpful?

YesNo

## [Anchor to CartBuyerIdentityUpdatePayload returns](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#returns)CartBuyerIdentityUpdatePayload returns

* cart (Cart)
* userErrors ([CartUserError!]!)
* warnings ([CartWarning!]!)

[Anchor to cart](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#returns-cart)cart •[Cart](/docs/api/storefront/latest/objects/Cart)
:   The updated cart.

    Show fields

[Anchor to userErrors](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#returns-userErrors)userErrors •[[CartUserError!]!](/docs/api/storefront/latest/objects/CartUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to warnings](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate#returns-warnings)warnings •[[CartWarning!]!](/docs/api/storefront/latest/objects/CartWarning) non-null
:   A list of warnings that occurred during the mutation.

    Show fields

---

Was this section helpful?

YesNo