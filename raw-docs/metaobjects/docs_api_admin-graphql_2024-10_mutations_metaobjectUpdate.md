---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/metaobjectUpdate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_metaobjects` access scope.

Updates a [`Metaobject`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Metaobject) with new field values, handle, or capabilities. [Metaobjects](https://shopify.dev/docs/apps/build/custom-data#what-are-metaobjects) are custom data structures that extend Shopify's data model.

You can modify field values mapped to the metaobject's [`MetaobjectDefinition`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetaobjectDefinition), update the handle for a unique identifier, and adjust capabilities like publishing status. When updating the handle, you can optionally create a redirect from the old handle to maintain existing references.

* id (ID!)
* metaobject (MetaobjectUpdateInput!)

[Anchor to id](/docs/api/admin-graphql/latest/mutations/metaobjectUpdate#arguments-id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
:   The ID of the metaobject to update.

[Anchor to metaobject](/docs/api/admin-graphql/latest/mutations/metaobjectUpdate#arguments-metaobject)metaobject •[MetaobjectUpdateInput!](/docs/api/admin-graphql/latest/input-objects/MetaobjectUpdateInput) required
:   Specifies parameters to update on the metaobject.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to MetaobjectUpdatePayload returns](/docs/api/admin-graphql/latest/mutations/metaobjectUpdate#returns)MetaobjectUpdatePayload returns

* metaobject (Metaobject)
* userErrors ([MetaobjectUserError!]!)

[Anchor to metaobject](/docs/api/admin-graphql/latest/mutations/metaobjectUpdate#returns-metaobject)metaobject •[Metaobject](/docs/api/admin-graphql/latest/objects/Metaobject)
:   The updated metaobject.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/metaobjectUpdate#returns-userErrors)userErrors •[[MetaobjectUserError!]!](/docs/api/admin-graphql/latest/objects/MetaobjectUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo