---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Metafield
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Metafields represent custom metadata attached to a resource. Metafields can be sorted into namespaces and are
comprised of keys, values, and value types.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Metafield#fields)Fields

* createdAt (DateTime!)
* description (String)
* id (ID!)
* key (String!)
* namespace (String!)
* parentResource (MetafieldParentResource!)
* reference (MetafieldReference)
* references (MetafieldReferenceConnection)
* type (String!)
* updatedAt (DateTime!)
* value (String!)

[Anchor to createdAt](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.createdAt)createdAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
:   The date and time when the storefront metafield was created.

[Anchor to description](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.description)description •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The description of a metafield.

[Anchor to id](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null Token access required
:   A globally-unique ID.

[Anchor to key](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.key)key •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   The unique identifier for the metafield within its namespace.

[Anchor to namespace](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.namespace)namespace •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   The container for a group of metafields that the metafield is associated with.

[Anchor to parentResource](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.parentResource)parentResource •[MetafieldParentResource!](/docs/api/storefront/latest/unions/MetafieldParentResource) non-null Token access required
:   The type of resource that the metafield is attached to.

    Show union types

[Anchor to reference](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.reference)reference •[MetafieldReference](/docs/api/storefront/latest/unions/MetafieldReference) Token access required
:   Returns a reference object if the metafield's type is a resource reference.

    Show union types

[Anchor to references](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.references)references •[MetafieldReferenceConnection](/docs/api/storefront/latest/connections/MetafieldReferenceConnection) Token access required
:   A list of reference objects if the metafield's type is a resource reference list.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.references.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.references.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.references.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.references.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    ---

[Anchor to type](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.type)type •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   The type name of the metafield.
    Refer to the list of [supported types](https://shopify.dev/apps/metafields/definitions/types).

[Anchor to updatedAt](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.updatedAt)updatedAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
:   The date and time when the metafield was last updated.

[Anchor to value](/docs/api/storefront/latest/objects/Metafield#field-Metafield.fields.value)value •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/storefront/latest/objects/Metafield#mutations)Mutations

* cartMetafieldsSet (CartMetafieldsSetPayload)

[Anchor to cartMetafieldsSet](/docs/api/storefront/latest/objects/Metafield#mutation-cartMetafieldsSet)[cartMetafieldsSet](/docs/api/storefront/latest/mutations/cartMetafieldsSet) •mutation
:   Sets cart metafield values. Cart metafield values will be set regardless if they were previously created or not.

    Allows a maximum of 25 cart metafields to be set at a time.

    Cart metafields will be copied to order metafields at order creation time if there is a matching order metafield definition with the [`cart to order copyable`](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities#cart-to-order-copyable) capability enabled.

    ---

    Note

    This mutation won't trigger [Shopify Functions](https://shopify.dev/docs/api/functions). The changes won't be available to Shopify Functions until the buyer goes to checkout or performs another cart interaction that triggers the functions.

    **Note:**

    This mutation won't trigger [Shopify Functions](https://shopify.dev/docs/api/functions). The changes won't be available to Shopify Functions until the buyer goes to checkout or performs another cart interaction that triggers the functions.

    **Note:** This mutation won&#39;t trigger <a href="https://shopify.dev/docs/api/functions">Shopify Functions</a>. The changes won&#39;t be available to Shopify Functions until the buyer goes to checkout or performs another cart interaction that triggers the functions.

    ---

    Show payload

    ### Arguments

    [Anchor to metafields](/docs/api/storefront/latest/objects/Metafield#mutation-cartMetafieldsSet.arguments.metafields)metafields •[[CartMetafieldsSetInput!]!](/docs/api/storefront/latest/input-objects/CartMetafieldsSetInput) required
    :   The list of Cart metafield values to set. Maximum of 25.

        The input must not contain more than `250` values.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/Metafield#interfaces)Interfaces

* Node

[Anchor to Node](/docs/api/storefront/latest/objects/Metafield#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo