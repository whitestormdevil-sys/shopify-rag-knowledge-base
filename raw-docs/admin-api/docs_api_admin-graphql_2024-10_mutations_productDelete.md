---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/productDelete
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_products` access scope. Also: The user must have a permission to delete products.

Permanently deletes a product and all its associated data, including variants, media, publications, and inventory items.

Use the `productDelete` mutation to programmatically remove products from your store when they need to be
permanently deleted from your catalog, such as when removing discontinued items, cleaning up test data, or
synchronizing with external inventory management systems.

The `productDelete` mutation removes the product from all associated collections,
and removes all associated data for the product, including:

* All product variants and their inventory items
* Product media (images, videos) that are not referenced by other products
* [Product options](https://shopify.dev/api/admin-graphql/latest/objects/ProductOption) and [option values](https://shopify.dev/api/admin-graphql/latest/objects/ProductOptionValue)
* Product publications across all sales channels
* Product tags and metadata associations

The `productDelete` mutation also has the following effects on existing orders and transactions:

* **Draft orders**: Existing draft orders that reference this product will retain the product information as stored data, but the product reference will be removed. Draft orders can still be completed with the stored product details.
* **Completed orders and refunds**: Previously completed orders that included this product aren't affected. The product information in completed orders is preserved for record-keeping, and existing refunds for this product remain valid and processable.

---

Caution

Product deletion is irreversible. After a product is deleted, it can't be recovered. Consider archiving
or unpublishing products instead if you might need to restore them later.

**Caution:**

Product deletion is irreversible. After a product is deleted, it can't be recovered. Consider archiving
or unpublishing products instead if you might need to restore them later.

**Caution:** Product deletion is irreversible. After a product is deleted, it can&#39;t be recovered. Consider archiving
or unpublishing products instead if you might need to restore them later.

---

If you need to delete a large product, such as one that has many
[variants](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant)
that are active at several
[locations](https://shopify.dev/api/admin-graphql/latest/objects/Location),
you might encounter timeout errors. To avoid these timeout errors, you can set the
[`synchronous`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productDelete#arguments-synchronous)
parameter to `false` to run the deletion asynchronously, which returns a
[`ProductDeleteOperation`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductDeleteOperation)
that you can monitor for completion status.

If you need more granular control over product cleanup, consider using these alternative mutations:

* [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productUpdate):
  Update the product status to archived or unpublished instead of deleting.
* [`productVariantsBulkDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkDelete):
  Delete specific variants while keeping the product.
* [`productOptionsDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsDelete):
  Delete the choices available for a product, such as size, color, or material.

Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model).

* input (ProductDeleteInput!)
* synchronous (Boolean)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/productDelete#arguments-input)input •[ProductDeleteInput!](/docs/api/admin-graphql/latest/input-objects/ProductDeleteInput) required
:   Specifies the product to delete by its ID.

    Show input fields

[Anchor to synchronous](/docs/api/admin-graphql/latest/mutations/productDelete#arguments-synchronous)synchronous •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
:   Specifies whether or not to run the mutation synchronously.

---

Was this section helpful?

YesNo

## [Anchor to ProductDeletePayload returns](/docs/api/admin-graphql/latest/mutations/productDelete#returns)ProductDeletePayload returns

* deletedProductId (ID)
* productDeleteOperation (ProductDeleteOperation)
* shop (Shop!)
* userErrors ([UserError!]!)

[Anchor to deletedProductId](/docs/api/admin-graphql/latest/mutations/productDelete#returns-deletedProductId)deletedProductId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   The ID of the deleted product.

[Anchor to productDeleteOperation](/docs/api/admin-graphql/latest/mutations/productDelete#returns-productDeleteOperation)productDeleteOperation •[ProductDeleteOperation](/docs/api/admin-graphql/latest/objects/ProductDeleteOperation)
:   The product delete operation, returned when run in asynchronous mode.

    Show fields

[Anchor to shop](/docs/api/admin-graphql/latest/mutations/productDelete#returns-shop)shop •[Shop!](/docs/api/admin-graphql/latest/objects/Shop) non-null
:   The shop associated with the product.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/productDelete#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo