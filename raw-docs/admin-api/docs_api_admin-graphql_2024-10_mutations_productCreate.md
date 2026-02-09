---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/productCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_products` access scope. Also: The user must have a permission to create products.

Creates a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
with attributes such as title, description, vendor, and media.

The `productCreate` mutation helps you create many products at once, avoiding the tedious or time-consuming
process of adding them one by one in the Shopify admin. Common examples include creating products for a
new collection, launching a new product line, or adding seasonal products.

You can define product
[options](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption) and
[values](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOptionValue),
allowing you to create products with different variations like sizes or colors. You can also associate media
files to your products, including images and videos.

The `productCreate` mutation only supports creating a product with its initial
[product variant](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant).
To create multiple product variants for a single product and manage prices, use the
[`productVariantsBulkCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkCreate)
mutation.

---

Note

The `productCreate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be created per day.

**Note:**

The `productCreate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be created per day.

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">product<wbr/>Create</span></code> mutation has a <a href="https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits">throttle</a>
that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
1,000 new product variants can be created per day.

---

After you create a product, you can make subsequent edits to the product using one of the following mutations:

* [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish):
  Used to publish the product and make it available to customers. The `productCreate` mutation creates products
  in an unpublished state by default, so you must perform a separate operation to publish the product.
* [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productUpdate):
  Used to update a single product, such as changing the product's title, description, vendor, or associated media.
* [`productSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet):
  Used to perform multiple operations on products, such as creating or modifying product options and variants.

Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model)
and [adding product data](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/add-data).

* media ([CreateMediaInput!])
* product (ProductCreateInput)
* input (ProductInput): deprecated

[Anchor to media](/docs/api/admin-graphql/latest/mutations/productCreate#arguments-media)media •[[CreateMediaInput!]](/docs/api/admin-graphql/latest/input-objects/CreateMediaInput)
:   The media to add to the product.

    Show input fields

[Anchor to product](/docs/api/admin-graphql/latest/mutations/productCreate#arguments-product)product •[ProductCreateInput](/docs/api/admin-graphql/latest/input-objects/ProductCreateInput)
:   The attributes of the new product.

    Show input fields

[Anchor to input](/docs/api/admin-graphql/latest/mutations/productCreate#arguments-input)input •[ProductInput](/docs/api/admin-graphql/latest/input-objects/ProductInput) Deprecated
:   Show input fields

---

Was this section helpful?

YesNo

## [Anchor to ProductCreatePayload returns](/docs/api/admin-graphql/latest/mutations/productCreate#returns)ProductCreatePayload returns

* product (Product)
* shop (Shop!)
* userErrors ([UserError!]!)

[Anchor to product](/docs/api/admin-graphql/latest/mutations/productCreate#returns-product)product •[Product](/docs/api/admin-graphql/latest/objects/Product)
:   The product object.

    Show fields

[Anchor to shop](/docs/api/admin-graphql/latest/mutations/productCreate#returns-shop)shop •[Shop!](/docs/api/admin-graphql/latest/objects/Shop) non-null
:   The shop associated with the product.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/productCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo