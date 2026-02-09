---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/metaobjectCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_metaobjects` access scope.

Creates a metaobject entry based on an existing [`MetaobjectDefinition`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetaobjectDefinition). The type must match a definition that already exists in the shop.

Specify field values using key-value pairs that correspond to the field definitions. The mutation generates a unique handle automatically if you don't provide one. You can also configure capabilities like publishable status to control the metaobject's visibility across channels.

Learn more about [managing metaobjects](https://shopify.dev/docs/apps/build/custom-data/metaobjects/manage-metaobjects).

* metaobject (MetaobjectCreateInput!)

[Anchor to metaobject](/docs/api/admin-graphql/latest/mutations/metaobjectCreate#arguments-metaobject)metaobject •[MetaobjectCreateInput!](/docs/api/admin-graphql/latest/input-objects/MetaobjectCreateInput) required
:   The parameters for the metaobject to create.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to MetaobjectCreatePayload returns](/docs/api/admin-graphql/latest/mutations/metaobjectCreate#returns)MetaobjectCreatePayload returns

* metaobject (Metaobject)
* userErrors ([MetaobjectUserError!]!)

[Anchor to metaobject](/docs/api/admin-graphql/latest/mutations/metaobjectCreate#returns-metaobject)metaobject •[Metaobject](/docs/api/admin-graphql/latest/objects/Metaobject)
:   The created metaobject.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/metaobjectCreate#returns-userErrors)userErrors •[[MetaobjectUserError!]!](/docs/api/admin-graphql/latest/objects/MetaobjectUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo