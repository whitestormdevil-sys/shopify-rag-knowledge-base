---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/collectionCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_products` access scope. Also: The app must have access to the input fields used to create the collection. Further, the store must not be on the Starter or Retail plans and user must have a permission to create collection.

Creates a [collection](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection)
to group [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) together
in the [online store](https://shopify.dev/docs/apps/build/online-store) and
other [sales channels](https://shopify.dev/docs/apps/build/sales-channels).
For example, an athletics store might create different collections for running attire, shoes, and accessories.

There are two types of collections:

* **[Custom (manual) collections](https://help.shopify.com/manual/products/collections/manual-shopify-collection)**: You specify the products to include in a collection.
* **[Smart (automated) collections](https://help.shopify.com/manual/products/collections/automated-collections)**: You define rules, and products matching those rules are automatically
  included in the collection.

Use the `collectionCreate` mutation when you need to:

* Create a new collection for a product launch or campaign
* Organize products by category, season, or promotion
* Automate product grouping using rules (for example, by tag, type, or price)

---

Note

The created collection is unpublished by default. To make it available to customers,
use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
mutation after creation.

**Note:**

The created collection is unpublished by default. To make it available to customers,
use the [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish)
mutation after creation.

**Note:** The created collection is unpublished by default. To make it available to customers,
use the <a href="https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish"><code><span class="PreventFireFoxApplyingGapToWBR">publishable<wbr/>Publish</span></code></a>
mutation after creation.

---

Learn more about [using metafields with smart collections](https://shopify.dev/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

* input (CollectionInput!)

[Anchor to input](/docs/api/admin-graphql/latest/mutations/collectionCreate#arguments-input)input •[CollectionInput!](/docs/api/admin-graphql/latest/input-objects/CollectionInput) required
:   The properties to use when creating the collection.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to CollectionCreatePayload returns](/docs/api/admin-graphql/latest/mutations/collectionCreate#returns)CollectionCreatePayload returns

* collection (Collection)
* userErrors ([UserError!]!)

[Anchor to collection](/docs/api/admin-graphql/latest/mutations/collectionCreate#returns-collection)collection •[Collection](/docs/api/admin-graphql/latest/objects/Collection)
:   The collection that has been created.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/collectionCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo