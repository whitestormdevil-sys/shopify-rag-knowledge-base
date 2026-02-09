---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/discountCodeBasicCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires Apps must have `write_discounts` access scope.

Creates an [amount off discount](https://help.shopify.com/manual/discounts/discount-types/percentage-fixed-amount) that's applied on a cart and at checkout when a customer enters a code. Amount off discounts can be a percentage off or a fixed amount off.

---

Note

To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) mutation.

**Note:**

To create discounts that are automatically applied on a cart and at checkout, use the [`discountAutomaticBasicCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) mutation.

**Note:** To create discounts that are automatically applied on a cart and at checkout, use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate"><code><span class="PreventFireFoxApplyingGapToWBR">discount<wbr/>Automatic<wbr/>Basic<wbr/>Create</span></code></a> mutation.

---

* basicCodeDiscount (DiscountCodeBasicInput!)

[Anchor to basicCodeDiscount](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate#arguments-basicCodeDiscount)basicCodeDiscount •[DiscountCodeBasicInput!](/docs/api/admin-graphql/latest/input-objects/DiscountCodeBasicInput) required
:   The input data used to create the discount code.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to DiscountCodeBasicCreatePayload returns](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate#returns)DiscountCodeBasicCreatePayload returns

* codeDiscountNode (DiscountCodeNode)
* userErrors ([DiscountUserError!]!)

[Anchor to codeDiscountNode](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate#returns-codeDiscountNode)codeDiscountNode •[DiscountCodeNode](/docs/api/admin-graphql/latest/objects/DiscountCodeNode)
:   The discount code that was created.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate#returns-userErrors)userErrors •[[DiscountUserError!]!](/docs/api/admin-graphql/latest/objects/DiscountUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo