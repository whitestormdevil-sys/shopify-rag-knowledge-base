---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Metafield
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Metafields enable you to attach additional information to a Shopify resource, such as a [Product](https://shopify.dev/api/admin-graphql/latest/objects/product) or a [Collection](https://shopify.dev/api/admin-graphql/latest/objects/collection).
For more information about where you can attach metafields refer to [HasMetafields](https://shopify.dev/api/admin-graphql/latest/interfaces/HasMetafields).
Some examples of the data that metafields enable you to store are specifications, size charts, downloadable documents, release dates, images, or part numbers.
Metafields are identified by an owner resource, namespace, and key. and store a value along with type information for that value.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Metafield#fields)Fields

* compareDigest (String!)
* createdAt (DateTime!)
* definition (MetafieldDefinition)
* id (ID!)
* jsonValue (JSON!)
* key (String!)
* legacyResourceId (UnsignedInt64!)
* namespace (String!)
* owner (HasMetafields!)
* ownerType (MetafieldOwnerType!)
* reference (MetafieldReference)
* references (MetafieldReferenceConnection)
* type (String!)
* updatedAt (DateTime!)
* value (String!)
* description (String): deprecated

[Anchor to compareDigest](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.compareDigest)compareDigest •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The data stored in the resource, represented as a digest.

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the metafield was created.

[Anchor to definition](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.definition)definition •[MetafieldDefinition](/docs/api/admin-graphql/latest/objects/MetafieldDefinition)
:   The metafield definition that the metafield belongs to, if any.

    Show fields

[Anchor to id](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to jsonValue](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.jsonValue)jsonValue •[JSON!](/docs/api/admin-graphql/latest/scalars/JSON) non-null
:   The data stored in the metafield in JSON format.

[Anchor to key](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The unique identifier for the metafield within its namespace.

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to namespace](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.namespace)namespace •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The container for a group of metafields that the metafield is associated with.

[Anchor to owner](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.owner)owner •[HasMetafields!](/docs/api/admin-graphql/latest/interfaces/HasMetafields) non-null
:   The resource that the metafield is attached to.

    Show fields

[Anchor to ownerType](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.ownerType)ownerType •[MetafieldOwnerType!](/docs/api/admin-graphql/latest/enums/MetafieldOwnerType) non-null
:   The type of resource that the metafield is attached to.

    Show enum values

[Anchor to reference](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.reference)reference •[MetafieldReference](/docs/api/admin-graphql/latest/unions/MetafieldReference)
:   Returns a reference object if the metafield definition's type is a resource reference.

    Show union types

[Anchor to references](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.references)references •[MetafieldReferenceConnection](/docs/api/admin-graphql/latest/connections/MetafieldReferenceConnection)
:   A list of reference objects if the metafield's type is a resource reference list.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.references.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.references.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.references.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.references.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to type](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.type)type •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The type of data that's stored in the metafield.
    Refer to the list of [supported types](https://shopify.dev/apps/metafields/types).

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the metafield was updated.

[Anchor to value](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.value)value •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

[Anchor to description](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.description)description •[String](/docs/api/admin-graphql/latest/scalars/String) Deprecated

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/Metafield#mutations)Mutations

* metafieldsSet (MetafieldsSetPayload)

[Anchor to metafieldsSet](/docs/api/admin-graphql/latest/objects/Metafield#mutation-metafieldsSet)[metafieldsSet](/docs/api/admin-graphql/latest/mutations/metafieldsSet) •mutation
:   Sets metafield values. Metafield values will be set regardless if they were previously created or not.

    Allows a maximum of 25 metafields to be set at a time, with a maximum total request payload size of 10MB.

    This operation is atomic, meaning no changes are persisted if an error is encountered.

    As of `2024-07`, this operation supports compare-and-set functionality to better handle concurrent requests.
    If `compareDigest` is set for any metafield, the mutation will only set that metafield if the persisted metafield value matches the digest used on `compareDigest`.
    If the metafield doesn't exist yet, but you want to guarantee that the operation will run in a safe manner, set `compareDigest` to `null`.
    The `compareDigest` value can be acquired by querying the metafield object and selecting `compareDigest` as a field.
    If the `compareDigest` value does not match the digest for the persisted value, the mutation will return an error.
    You can opt out of write guarantees by not sending `compareDigest` in the request.

    Show payload

    ### Arguments

    [Anchor to metafields](/docs/api/admin-graphql/latest/objects/Metafield#mutation-metafieldsSet.arguments.metafields)metafields •[[MetafieldsSetInput!]!](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput) required
    :   The list of metafield values to set. Maximum of 25.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Metafield#interfaces)Interfaces

* HasCompareDigest
* LegacyInteroperability
* Node

[Anchor to HasCompareDigest](/docs/api/admin-graphql/latest/objects/Metafield#interface-HasCompareDigest)[HasCompareDigest](/docs/api/admin-graphql/latest/interfaces/HasCompareDigest) •interface

[Anchor to LegacyInteroperability](/docs/api/admin-graphql/latest/objects/Metafield#interface-LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Metafield#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo