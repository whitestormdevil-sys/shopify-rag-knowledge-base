---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/metaobjectDefinitions
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_metaobject_definitions` access scope.

Returns a paginated list of all [`MetaobjectDefinition`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetaobjectDefinition) objects configured for the store. Metaobject definitions provide the schema for creating custom data structures composed of individual fields. Each definition specifies the field types, access permissions, and capabilities for [`Metaobject`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Metaobject) entries of that type. Use this query to discover available metaobject types before creating or querying metaobject entries.

Learn more about [managing metaobjects](https://shopify.dev/docs/apps/build/custom-data/metaobjects/manage-metaobjects).

* after (String)
* before (String)
* first (Int)
* last (Int)
* reverse (Boolean)

[Anchor to after](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#possible-returns)Possible returns

* edges ([MetaobjectDefinitionEdge!]!)
* nodes ([MetaobjectDefinition!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#returns-edges)edges •[[MetaobjectDefinitionEdge!]!](/docs/api/admin-graphql/latest/objects/MetaobjectDefinitionEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#returns-nodes)nodes •[[MetaobjectDefinition!]!](/docs/api/admin-graphql/latest/objects/MetaobjectDefinition) non-null
:   A list of nodes that are contained in MetaobjectDefinitionEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/metaobjectDefinitions#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo