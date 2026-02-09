---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/productUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_products` access scope. Also: The user must have a permission to update products.

Updates a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
with attributes such as title, description, vendor, and media.

The `productUpdate` mutation helps you modify many products at once, avoiding the tedious or time-consuming
process of updating them one by one in the Shopify admin. Common examples including updating
product details like status or tags.

The `productUpdate` mutation doesn't support updating
[product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant).
To update multiple product variants for a single product and manage prices, use the
[`productVariantsBulkUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate)
mutation.

---

Note

The `productUpdate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be updated per day.

**Note:**

The `productUpdate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be updated per day.

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">product<wbr/>Update</span></code> mutation has a <a href="https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits">throttle</a>
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be updated per day.

---

After updating a product, you can make additional changes using one of the following mutations:

* [`productSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet):
  Used to perform multiple operations on products, such as creating or modifying product options and variants.
* [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish):
  Used to publish the product and make it available to customers, if the product is currently unpublished.

Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model)
and [adding product data](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/add-data).

* media ([CreateMediaInput!])
* product (ProductUpdateInput)
* input (ProductInput): deprecated

[Anchor to media](/docs/api/admin-graphql/latest/mutations/productUpdate#arguments-media)media •[[CreateMediaInput!]](/docs/api/admin-graphql/latest/input-objects/CreateMediaInput)
:   List of new media to be added to the product.

    Show input fields

[Anchor to product](/docs/api/admin-graphql/latest/mutations/productUpdate#arguments-product)product •[ProductUpdateInput](/docs/api/admin-graphql/latest/input-objects/ProductUpdateInput)
:   The updated properties for a product.

    Show input fields

[Anchor to input](/docs/api/admin-graphql/latest/mutations/productUpdate#arguments-input)input •[ProductInput](/docs/api/admin-graphql/latest/input-objects/ProductInput) Deprecated
:   Show input fields

---

Was this section helpful?

YesNo

## [Anchor to ProductUpdatePayload returns](/docs/api/admin-graphql/latest/mutations/productUpdate#returns)ProductUpdatePayload returns

* product (Product)
* userErrors ([UserError!]!)

[Anchor to product](/docs/api/admin-graphql/latest/mutations/productUpdate#returns-product)product •[Product](/docs/api/admin-graphql/latest/objects/Product)
:   The updated product object.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/productUpdate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo