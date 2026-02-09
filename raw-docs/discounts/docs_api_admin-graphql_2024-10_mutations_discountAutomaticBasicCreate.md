---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/discountAutomaticBasicCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires Apps must have `write_discounts` access scope.

Creates an
[amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount)
that's automatically applied on a cart and at checkout.

---

Note

To create code discounts, use the
[`discountCodeBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)
mutation.

**Note:**

To create code discounts, use the
[`discountCodeBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate)
mutation.

**Note:** To create code discounts, use the
<a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Code<wbr/>Basic<wbr/>Create</span></code></a>
mutation.

---

* automaticBasicDiscount (DiscountAutomaticBasicInput!)

[Anchor to automaticBasicDiscount](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate#arguments-automaticBasicDiscount)automaticBasicDiscount •[DiscountAutomaticBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountAutomaticBasicInput) required
:   The input data used to create the automatic amount off discount.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to DiscountAutomaticBasicCreatePayload returns](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate#returns)DiscountAutomaticBasicCreatePayload returns

* automaticDiscountNode (DiscountAutomaticNode)
* userErrors ([DiscountUserError!]!)

[Anchor to automaticDiscountNode](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate#returns-automaticDiscountNode)automaticDiscountNode •[DiscountAutomaticNode](/docs/api/admin-graphql/latest/objects/DiscountAutomaticNode)
:   The automatic discount that was created.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate#returns-userErrors)userErrors •[[DiscountUserError!]!](/docs/api/admin-graphql/latest/objects/DiscountUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo