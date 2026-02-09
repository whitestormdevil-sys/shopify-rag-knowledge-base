---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/metaobjects
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_metaobjects` access scope.

Returns a paginated list of [`Metaobject`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Metaobject) entries for a specific type. Metaobjects are custom data structures that extend Shopify's data model with merchant or app-specific data types.

Filter results using the query parameter with a search syntax for metaobject fields. Use `fields.{key}:{value}` to filter by field values, supporting any field previously marked as filterable. The `sortKey` parameter accepts `id`, `type`, `updated_at`, or `display_name` to control result ordering.

Learn more about [querying metaobjects by field value](https://shopify.dev/docs/apps/build/custom-data/metafields/query-by-metafield-value).

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* sortKey (String)
* type (String!)

[Anchor to after](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/metaobjects#argument-query-filter-display_name) display\_name •string

    [Anchor to](/docs/api/admin-graphql/latest/queries/metaobjects#argument-query-filter-fields.{key}) fields.{key} •mixed
    :   Filters metaobject entries by field value. Format: `fields.{key}:{value}`. Only fields marked as filterable in the metaobject definition can be used. Learn more about [querying metaobjects by field value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

    Example:

    * `fields.color:blue`
    * `fields.on_sale:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/metaobjects#argument-query-filter-handle) handle •string

    [Anchor to](/docs/api/admin-graphql/latest/queries/metaobjects#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/metaobjects#argument-query-filter-updated_at) updated\_at •time

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-sortKey)sortKey •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The key of a field to sort with. Supports "id", "type", "updated\_at", and "display\_name".

[Anchor to type](/docs/api/admin-graphql/latest/queries/metaobjects#arguments-type)type •[String!](/docs/api/admin-graphql/latest/scalars/String) required
:   The type of the metaobjects to query.

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/metaobjects#possible-returns)Possible returns

* edges ([MetaobjectEdge!]!)
* nodes ([Metaobject!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/metaobjects#returns-edges)edges •[[MetaobjectEdge!]!](/docs/api/admin-graphql/latest/objects/MetaobjectEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/metaobjects#returns-nodes)nodes •[[Metaobject!]!](/docs/api/admin-graphql/latest/objects/Metaobject) non-null
:   A list of nodes that are contained in MetaobjectEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/metaobjects#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo