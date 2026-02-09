---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/customers
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Returns a list of [customers](https://shopify.dev/api/admin-graphql/latest/objects/Customer) in your Shopify store, including key information such as name, email, location, and purchase history.
Use this query to segment your audience, personalize marketing campaigns, or analyze customer behavior by applying filters based on location, order history, marketing preferences and tags.
The `customers` query supports [pagination](https://shopify.dev/api/usage/pagination-graphql) and [sorting](https://shopify.dev/api/admin-graphql/latest/enums/CustomerSortKeys).

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* sortKey (CustomerSortKeys)

[Anchor to after](/docs/api/admin-graphql/latest/queries/customers#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/customers#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/customers#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/customers#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/customers#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-default) default •string
    :   Filter by a case-insensitive search of multiple fields in a document.

    Example:

    * `query=Bob Norman`
    * `query=title:green hoodie`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-accepts_marketing) accepts\_marketing •boolean
    :   Filter by whether a customer has consented to receive marketing material.

    Example:

    * `accepts_marketing:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-country) country •string
    :   Filter by the country associated with the customer's address. Use either the country name or the two-letter country code.

    Example:

    * `country:Canada`
    * `country:JP`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-customer_date) customer\_date •time
    :   Filter by the date and time when the customer record was created. This query parameter filters by the [`createdAt`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-createdAt) field.

    Example:

    * `customer_date:'2024-03-15T14:30:00Z'`
    * `customer_date: >='2024-01-01'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-email) email •string
    :   The customer's email address, used to communicate information about orders and for the purposes of email marketing campaigns. You can use a wildcard value to filter the query by customers who have an email address specified. Please note that *email* is a tokenized field: To retrieve exact matches, quote the email address (*phrase query*) as described in [Shopify API search syntax](https://shopify.dev/docs/api/usage/search-syntax).

    Example:

    * `email:gmail.com`
    * `email:"bo.wang@example.com"`
    * `email:*`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-first_name) first\_name •string
    :   Filter by the customer's first name.

    Example:

    * `first_name:Jane`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-last_abandoned_order_date) last\_abandoned\_order\_date •time
    :   Filter by the date and time of the customer's most recent abandoned checkout. An abandoned checkout occurs when a customer adds items to their cart, begins the checkout process, but leaves the site without completing their purchase.

    Example:

    * `last_abandoned_order_date:'2024-04-01T10:00:00Z'`
    * `last_abandoned_order_date: >='2024-01-01'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-last_name) last\_name •string
    :   Filter by the customer's last name.

    Example:

    * `last_name:Reeves`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-order_date) order\_date •time
    :   Filter by the date and time that the order was placed by the customer. Use this query filter to check if a customer has placed at least one order within a specified date range.

    Example:

    * `order_date:'2024-02-20T00:00:00Z'`
    * `order_date: >='2024-01-01'`
    * `order_date:'2024-01-01..2024-03-31'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-orders_count) orders\_count •integer
    :   Filter by the total number of orders a customer has placed.

    Example:

    * `orders_count:5`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-phone) phone •string
    :   The phone number of the customer, used to communicate information about orders and for the purposes of SMS marketing campaigns. You can use a wildcard value to filter the query by customers who have a phone number specified.

    Example:

    * `phone:+18005550100`
    * `phone:*`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-state) state •string
    :   Filter by the [state](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-state) of the customer's account with the shop. This filter is only valid when [Classic Customer Accounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerAccountsV2#field-customerAccountsVersion) is active.

    Example:

    * `state:ENABLED`
    * `state:INVITED`
    * `state:DISABLED`
    * `state:DECLINED`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-tag) tag •string
    :   Filter by the tags that are associated with the customer. This query parameter accepts multiple tags separated by commas.

    Example:

    * `tag:'VIP'`
    * `tag:'Wholesale,Repeat'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-tag_not) tag\_not •string
    :   Filter by the tags that aren't associated with the customer. This query parameter accepts multiple tags separated by commas.

    Example:

    * `tag_not:'Prospect'`
    * `tag_not:'Test,Internal'`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-total_spent) total\_spent •float
    :   Filter by the total amount of money a customer has spent across all orders.

    Example:

    * `total_spent:100.50`
    * `total_spent:50.00`
    * `total_spent:>100.50`
    * `total_spent:>50.00`

    [Anchor to](/docs/api/admin-graphql/latest/queries/customers#argument-query-filter-updated_at) updated\_at •time
    :   The date and time, matching a whole day, when the customer's information was last updated.

    Example:

    * `updated_at:2024-01-01T00:00:00Z`
    * `updated_at:<now`
    * `updated_at:<=2024`

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/customers#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to sortKey](/docs/api/admin-graphql/latest/queries/customers#arguments-sortKey)sortKey •[CustomerSortKeys](/docs/api/admin-graphql/latest/enums/CustomerSortKeys) Default:ID
:   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/customers#possible-returns)Possible returns

* edges ([CustomerEdge!]!)
* nodes ([Customer!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/customers#returns-edges)edges •[[CustomerEdge!]!](/docs/api/admin-graphql/latest/objects/CustomerEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/customers#returns-nodes)nodes •[[Customer!]!](/docs/api/admin-graphql/latest/objects/Customer) non-null
:   A list of nodes that are contained in CustomerEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/customers#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo