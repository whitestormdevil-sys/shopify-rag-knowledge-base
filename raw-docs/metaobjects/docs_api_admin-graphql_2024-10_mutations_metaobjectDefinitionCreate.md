---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/metaobjectDefinitionCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `write_metaobject_definitions` access scope.

Creates a metaobject definition that establishes the structure for custom data objects in your store. The definition specifies the fields, data types, and access permissions that all [`Metaobject`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Metaobject) entries of this type share.

Use the `type` field to create a unique namespace for your metaobjects. Prefix the type with `$app:` to reserve the definition for your app's exclusive use. The definition can include capabilities like publishable status or translation eligibility, to extend how metaobjects integrate with Shopify's features.

Learn more about [managing metaobjects](https://shopify.dev/docs/apps/build/custom-data/metaobjects/manage-metaobjects).

* definition (MetaobjectDefinitionCreateInput!)

[Anchor to definition](/docs/api/admin-graphql/latest/mutations/metaobjectDefinitionCreate#arguments-definition)definition •[MetaobjectDefinitionCreateInput!](/docs/api/admin-graphql/latest/input-objects/MetaobjectDefinitionCreateInput) required
:   The input fields for creating a metaobject definition.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to MetaobjectDefinitionCreatePayload returns](/docs/api/admin-graphql/latest/mutations/metaobjectDefinitionCreate#returns)MetaobjectDefinitionCreatePayload returns

* metaobjectDefinition (MetaobjectDefinition)
* userErrors ([MetaobjectUserError!]!)

[Anchor to metaobjectDefinition](/docs/api/admin-graphql/latest/mutations/metaobjectDefinitionCreate#returns-metaobjectDefinition)metaobjectDefinition •[MetaobjectDefinition](/docs/api/admin-graphql/latest/objects/MetaobjectDefinition)
:   The created metaobject definition.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/metaobjectDefinitionCreate#returns-userErrors)userErrors •[[MetaobjectUserError!]!](/docs/api/admin-graphql/latest/objects/MetaobjectUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo