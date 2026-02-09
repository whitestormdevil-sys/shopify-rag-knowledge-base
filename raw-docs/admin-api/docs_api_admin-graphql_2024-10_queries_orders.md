---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/queries/orders
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Returns a list of [orders](https://shopify.dev/api/admin-graphql/latest/objects/Order) placed in the store, including data such as order status, customer, and line item details.
Use the `orders` query to build reports, analyze sales performance, or automate fulfillment workflows. The `orders` query supports [pagination](https://shopify.dev/docs/api/usage/pagination-graphql),
[sorting](https://shopify.dev/docs/api/admin-graphql/latest/queries/orders#arguments-sortKey), and [filtering](https://shopify.dev/docs/api/admin-graphql/latest/queries/orders#arguments-query).

* after (String)
* before (String)
* first (Int)
* last (Int)
* query (String)
* reverse (Boolean)
* savedSearchId (ID)
* sortKey (OrderSortKeys)

[Anchor to after](/docs/api/admin-graphql/latest/queries/orders#arguments-after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to before](/docs/api/admin-graphql/latest/queries/orders#arguments-before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to first](/docs/api/admin-graphql/latest/queries/orders#arguments-first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to last](/docs/api/admin-graphql/latest/queries/orders#arguments-last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

[Anchor to query](/docs/api/admin-graphql/latest/queries/orders#arguments-query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A filter made up of terms, connectives, modifiers, and comparators.
    You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

    Show filters

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-default) default •string
    :   Filter by a case-insensitive search of multiple fields in a document.

    Example:

    * `query=Bob Norman`
    * `query=title:green hoodie`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-cart_token) cart\_token •string
    :   Filter by the cart token's unique value to track abandoned cart conversions or troubleshoot checkout issues. The token references the cart that's associated with an order.

    Example:

    * `cart_token:abc123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-channel) channel •string
    :   Filter by the channel information [`handle`](https://shopify.dev/api/admin-graphql/latest/objects/ChannelInformation#field-ChannelInformation.fields.channelDefinition.handle) (`ChannelInformation.channelDefinition.handle`) field.

    Example:

    * `channel:web`
    * `channel:web,pos`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-channel_id) channel\_id •id
    :   Filter by the channel [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.id) field.

    Example:

    * `channel_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-chargeback_status) chargeback\_status •string
    :   Filter by the order's chargeback status. A chargeback occurs when a customer questions the legitimacy of a charge with their financial institution.

    Valid values:

    * `accepted`
    * `charge_refunded`
    * `lost`
    * `needs_response`
    * `under_review`
    * `won`

    Example:

    * `chargeback_status:accepted`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-checkout_token) checkout\_token •string
    :   Filter by the checkout token's unique value to analyze conversion funnels or resolve payment issues. The checkout token's value references the checkout that's associated with an order.

    Example:

    * `checkout_token:abc123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-confirmation_number) confirmation\_number •string
    :   Filter by the randomly generated alpha-numeric identifier for an order that can be displayed to the customer instead of the sequential order name. This value isn't guaranteed to be unique.

    Example:

    * `confirmation_number:ABC123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-created_at) created\_at •time
    :   Filter by the date and time when the order was created in Shopify's system.

    Example:

    * `created_at:2020-10-21T23:39:20Z`
    * `created_at:<now`
    * `created_at:<=2024`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-credit_card_last4) credit\_card\_last4 •string
    :   Filter by the last four digits of the payment card that was used to pay for the order. This filter matches only the last four digits of the card for heightened security.

    Example:

    * `credit_card_last4:1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-current_total_price) current\_total\_price •float
    :   Filter by the current total price of the order in the shop currency, including any returns/refunds/removals. This filter supports both exact values and ranges.

    Example:

    * `current_total_price:10`
    * `current_total_price:>=5.00 current_total_price:<=20.99`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-customer_id) customer\_id •id
    :   Filter orders by the customer [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Customer#field-Customer.fields.id) field.

    Example:

    * `customer_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-delivery_method) delivery\_method •string
    :   Filter by the delivery [`methodType`](https://shopify.dev/api/admin-graphql/2024-07/objects/DeliveryMethod#field-DeliveryMethod.fields.methodType) field.

    Valid values:

    * `shipping`
    * `pick-up`
    * `retail`
    * `local`
    * `pickup-point`
    * `none`

    Example:

    * `delivery_method:shipping`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-discount_code) discount\_code •string
    :   Filter by the case-insensitive discount code that was applied to the order at checkout. Limited to the first discount code used on an order. Maximum characters: 255.

    Example:

    * `discount_code:ABC123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-email) email •string
    :   Filter by the email address that's associated with the order to provide customer support or analyze purchasing patterns.

    Example:

    * `email:example@shopify.com`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-financial_status) financial\_status •string
    :   Filter by the order [`displayFinancialStatus`](https://shopify.dev/api/admin-graphql/latest/objects/Order#field-Order.fields.displayFinancialStatus) field.

    Valid values:

    * `paid`
    * `pending`
    * `authorized`
    * `partially_paid`
    * `partially_refunded`
    * `refunded`
    * `voided`
    * `expired`

    Example:

    * `financial_status:authorized`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-fraud_protection_level) fraud\_protection\_level •string
    :   Filter by the level of fraud protection that's applied to the order. Use this filter to manage risk or handle disputes.

    Valid values:

    * `fully_protected`
    * `partially_protected`
    * `not_protected`
    * `pending`
    * `not_eligible`
    * `not_available`

    Example:

    * `fraud_protection_level:fully_protected`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-fulfillment_location_id) fulfillment\_location\_id •id
    :   Filter by the fulfillment location [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.location.id) (`Fulfillment.location.id`) field.

    Example:

    * `fulfillment_location_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-fulfillment_status) fulfillment\_status •string
    :   Filter by the [`displayFulfillmentStatus`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.displayFulfillmentStatus) field to prioritize shipments or monitor order processing.

    Valid values:

    * `unshipped`
    * `shipped`
    * `fulfilled`
    * `partial`
    * `scheduled`
    * `on_hold`
    * `unfulfilled`
    * `request_declined`

    Example:

    * `fulfillment_status:fulfilled`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-gateway) gateway •string
    :   Filter by the [`paymentGatewayNames`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.paymentGatewayNames) field. Use this filter to find orders that were processed through specific payment providers like Shopify Payments, PayPal, or other custom payment gateways.

    Example:

    * `gateway:shopify_payments`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-id) id •id
    :   Filter by `id` range.

    Example:

    * `id:1234`
    * `id:>=1234`
    * `id:<=1234`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-location_id) location\_id •id
    :   Filter by the location [`id`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id) that's associated with the order to view and manage orders for specific locations. For POS orders, locations must be defined in the Shopify admin under **Settings** > **Locations**. If no ID is provided, then the primary location of the shop is returned.

    Example:

    * `location_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
    :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

    Example:

    * `metafields.custom.on_sale:true`
    * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-name) name •string
    :   Filter by the order [`name`](https://shopify.dev/api/admin-graphql/latest/objects/Order#field-name) field.

    Example:

    * `name:1001-A`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-payment_id) payment\_id •string
    :   Filter by the payment ID that's associated with the order to reconcile financial records or troubleshoot payment issues.

    Example:

    * `payment_id:abc123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-payment_provider_id) payment\_provider\_id •id
    :   Filter by the ID of the payment provider that's associated with the order to manage payment methods or troubleshoot transactions.

    Example:

    * `payment_provider_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-po_number) po\_number •string
    :   Filter by the order [`poNumber`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.poNumber) field.

    Example:

    * `po_number:P01001`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-processed_at) processed\_at •time
    :   Filter by the order [`processedAt`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.processedAt) field.

    Example:

    * `processed_at:2021-01-01T00:00:00Z`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-reference_location_id) reference\_location\_id •id
    :   Filter by the ID of a location that's associated with the order, such as locations from fulfillments, refunds, or the shop's primary location.

    Example:

    * `reference_location_id:123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-return_status) return\_status •string
    :   Filter by the order's [`returnStatus`](https://shopify.dev/api/admin-graphql/latest/objects/Order#field-Order.fields.returnStatus) to monitor returns processing and track which orders have active returns.

    Valid values:

    * `return_requested`
    * `in_progress`
    * `inspection_complete`
    * `returned`
    * `return_failed`
    * `no_return`

    Example:

    * `return_status:in_progress`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-risk_level) risk\_level •string
    :   Filter by the order risk assessment [`riskLevel`](https://shopify.dev/api/admin-graphql/latest/objects/OrderRiskAssessment#field-OrderRiskAssessment.fields.riskLevel) field.

    Valid values:

    * `high`
    * `medium`
    * `low`
    * `none`
    * `pending`

    Example:

    * `risk_level:high`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-sales_channel) sales\_channel •string
    :   Filter by the [sales channel](https://shopify.dev/docs/apps/build/sales-channels) where the order was made to analyze performance or manage fulfillment processes.

    Example:

    * `sales_channel: some_sales_channel`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-sku) sku •string
    :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

    Example:

    * `sku:ABC123`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-source_identifier) source\_identifier •string
    :   Filter by the ID of the order placed on the originating platform, such as a unique POS or third-party identifier. This value doesn't correspond to the Shopify ID that's generated from a completed draft order.

    Example:

    * `source_identifier:1234-12-1000`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-source_name) source\_name •string
    :   Filter by the platform where the order was placed to distinguish between web orders, POS sales, draft orders, or third-party channels. Use this filter to analyze sales performance across different ordering methods.

    Example:

    * `source_name:web`
    * `source_name:shopify_draft_order`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-status) status •string
    :   Filter by the order's status to manage workflows or analyze the order lifecycle.

    Valid values:

    * `open`
    * `closed`
    * `cancelled`
    * `not_closed`

    Example:

    * `status:open`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-subtotal_line_items_quantity) subtotal\_line\_items\_quantity •string
    :   Filter by the total number of items across all line items in an order. This filter supports both exact values and ranges, and is useful for identifying bulk orders or analyzing purchase volume patterns.

    Example:

    * `subtotal_line_items_quantity:10`
    * `subtotal_line_items_quantity:5..20`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-tag) tag •string
    :   Filter objects by the `tag` field.

    Example:

    * `tag:my_tag`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-tag_not) tag\_not •string
    :   Filter by objects that don’t have the specified tag.

    Example:

    * `tag_not:my_tag`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-test) test •boolean
    :   Filter by test orders. Test orders are made using the [Shopify Bogus Gateway](https://help.shopify.com/manual/checkout-settings/test-orders/payments-test-mode#bogus-gateway) or a payment provider with test mode enabled.

    Example:

    * `test:true`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-total_weight) total\_weight •string
    :   Filter by the order weight. This filter supports both exact values and ranges, and is to be used to filter orders by the total weight of all items (excluding packaging). It takes a unit of measurement as a suffix. It accepts the following units: g, kg, lb, oz.

    Example:

    * `total_weight:10.5kg`
    * `total_weight:>=5g total_weight:<=20g`
    * `total_weight:.5 lb`

    [Anchor to](/docs/api/admin-graphql/latest/queries/orders#argument-query-filter-updated_at) updated\_at •time
    :   Filter by the date and time when the order was last updated in Shopify's system.

    Example:

    * `updated_at:2020-10-21T23:39:20Z`
    * `updated_at:<now`
    * `updated_at:<=2024`

[Anchor to reverse](/docs/api/admin-graphql/latest/queries/orders#arguments-reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
:   Reverse the order of the underlying list.

[Anchor to savedSearchId](/docs/api/admin-graphql/latest/queries/orders#arguments-savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
    The search’s query string is used as the query argument.

[Anchor to sortKey](/docs/api/admin-graphql/latest/queries/orders#arguments-sortKey)sortKey •[OrderSortKeys](/docs/api/admin-graphql/latest/enums/OrderSortKeys) Default:PROCESSED\_AT
:   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

    Show enum values

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/admin-graphql/latest/queries/orders#possible-returns)Possible returns

* edges ([OrderEdge!]!)
* nodes ([Order!]!)
* pageInfo (PageInfo!)

[Anchor to edges](/docs/api/admin-graphql/latest/queries/orders#returns-edges)edges •[[OrderEdge!]!](/docs/api/admin-graphql/latest/objects/OrderEdge) non-null
:   The connection between the node and its parent. Each edge contains a minimum of the edge's cursor and the node.

    Show fields

[Anchor to nodes](/docs/api/admin-graphql/latest/queries/orders#returns-nodes)nodes •[[Order!]!](/docs/api/admin-graphql/latest/objects/Order) non-null
:   A list of nodes that are contained in OrderEdge. You can fetch data about an individual node, or you can follow the edges to fetch data about a collection of related nodes. At each node, you specify the fields that you want to retrieve.

    Show fields

[Anchor to pageInfo](/docs/api/admin-graphql/latest/queries/orders#returns-pageInfo)pageInfo •[PageInfo!](/docs/api/admin-graphql/latest/objects/PageInfo) non-null
:   An object that’s used to retrieve [cursor information](https://shopify.dev/api/usage/pagination-graphql) about the current page.

    Show fields

---

Was this section helpful?

YesNo