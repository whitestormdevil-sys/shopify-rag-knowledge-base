---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Customer
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_customers` access scope.

Information about a customer of the shop, such as the customer's contact details, purchase history, and marketing preferences.

Tracks the customer's total spending through the [`amountSpent`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-amountSpent) field and provides access to associated data such as payment methods and subscription contracts.

---

Caution

Only use this data if it's required for your app's functionality. Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-scopes) for apps that don't have a legitimate use for the associated data.

**Caution:**

Only use this data if it's required for your app's functionality. Shopify will restrict [access to scopes](https://shopify.dev/api/usage/access-scopes) for apps that don't have a legitimate use for the associated data.

**Caution:** Only use this data if it&#39;s required for your app&#39;s functionality. Shopify will restrict <a href="https://shopify.dev/api/usage/access-scopes">access to scopes</a> for apps that don&#39;t have a legitimate use for the associated data.

---

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Customer#fields)Fields

* addressesV2 (MailingAddressConnection!)
* amountSpent (MoneyV2!)
* canDelete (Boolean!)
* companyContactProfiles ([CompanyContact!]!)
* createdAt (DateTime!)
* dataSaleOptOut (Boolean!)
* defaultAddress (MailingAddress)
* defaultEmailAddress (CustomerEmailAddress)
* defaultPhoneNumber (CustomerPhoneNumber)
* displayName (String!)
* events (EventConnection!)
* firstName (String)
* id (ID!)
* image (Image!)
* lastName (String)
* lastOrder (Order)
* legacyResourceId (UnsignedInt64!)
* lifetimeDuration (String!)
* locale (String!)
* mergeable (CustomerMergeable!)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* multipassIdentifier (String)
* note (String)
* numberOfOrders (UnsignedInt64!)
* orders (OrderConnection!)
* paymentMethods (CustomerPaymentMethodConnection!)
* productSubscriberStatus (CustomerProductSubscriberStatus!)
* state (CustomerState!)
* statistics (CustomerStatistics!)
* storeCreditAccounts (StoreCreditAccountConnection!)
* subscriptionContracts (SubscriptionContractConnection!)
* tags ([String!]!)
* taxExempt (Boolean!)
* taxExemptions ([TaxExemption!]!)
* updatedAt (DateTime!)
* verifiedEmail (Boolean!)

[Anchor to addressesV2](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2)addressesV2 •[MailingAddressConnection!](/docs/api/admin-graphql/latest/connections/MailingAddressConnection) non-null
:   The addresses associated with the customer.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addressesV2.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to amountSpent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.amountSpent)amountSpent •[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2) non-null
:   The total amount that the customer has spent on orders in their lifetime.

    Show fields

[Anchor to canDelete](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.canDelete)canDelete •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the merchant can delete the customer from their store.

    A customer can be deleted from a store only if they haven't yet made an order. After a customer makes an
    order, they can't be deleted from a store.

[Anchor to companyContactProfiles](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.companyContactProfiles)companyContactProfiles •[[CompanyContact!]!](/docs/api/admin-graphql/latest/objects/CompanyContact) non-null
:   A list of the customer's company contact profiles.

    Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the customer was added to the store.

[Anchor to dataSaleOptOut](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.dataSaleOptOut)dataSaleOptOut •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the customer has opted out of having their data sold.

[Anchor to defaultAddress](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.defaultAddress)defaultAddress •[MailingAddress](/docs/api/admin-graphql/latest/objects/MailingAddress)
:   The default address associated with the customer.

    Show fields

[Anchor to defaultEmailAddress](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.defaultEmailAddress)defaultEmailAddress •[CustomerEmailAddress](/docs/api/admin-graphql/latest/objects/CustomerEmailAddress)
:   The customer's default email address.

    Show fields

[Anchor to defaultPhoneNumber](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.defaultPhoneNumber)defaultPhoneNumber •[CustomerPhoneNumber](/docs/api/admin-graphql/latest/objects/CustomerPhoneNumber)
:   The customer's default phone number.

    Show fields

[Anchor to displayName](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.displayName)displayName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The full name of the customer, based on the values for first\_name and last\_name. If the first\_name and
    last\_name are not available, then this falls back to the customer's email address, and if that is not available, the customer's phone number.

[Anchor to events](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events)events •[EventConnection!](/docs/api/admin-graphql/latest/connections/EventConnection) non-null
:   A list of events associated with the customer.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.sortKey)sortKey •[EventSortKeys](/docs/api/admin-graphql/latest/enums/EventSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.events.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-action) action •string
        :   The action that occured.

        Example:

        * `action:create`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-comments) comments •boolean
        :   Whether or not to include [comment-events](https://shopify.dev/api/admin-graphql/latest/objects/CommentEvent) in your search, passing `false` will exclude comment-events, any other value will include comment-events.

        Example:

        * `false`
        * `true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the event occurred. Event data is retained for 1 year.

        Example:

        * `created_at:>2025-10-21`
        * `created_at:<now`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-subject_type) subject\_type •string
        :   The resource type affected by this event. See [EventSubjectType](https://shopify.dev/api/admin-graphql/latest/enums/EventSubjectType) for possible values.

        Example:

        * `PRODUCT_VARIANT`
        * `PRODUCT`
        * `COLLECTION`

    ---

[Anchor to firstName](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.firstName)firstName •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The customer's first name.

[Anchor to id](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to image](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.image)image •[Image!](/docs/api/admin-graphql/latest/objects/Image) non-null
:   The image associated with the customer.

    Show fields

    ### Arguments

    [Anchor to size](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.image.arguments.size)size •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    ---

[Anchor to lastName](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lastName)lastName •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The customer's last name.

[Anchor to lastOrder](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lastOrder)lastOrder •[Order](/docs/api/admin-graphql/latest/objects/Order)
:   The customer's last order.

    Show fields

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to lifetimeDuration](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lifetimeDuration)lifetimeDuration •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The amount of time since the customer was first added to the store.

    Example: 'about 12 years'.

[Anchor to locale](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The customer's locale.

[Anchor to mergeable](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.mergeable)mergeable •[CustomerMergeable!](/docs/api/admin-graphql/latest/objects/CustomerMergeable) non-null
:   Whether the customer can be merged with another customer.

    Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to multipassIdentifier](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.multipassIdentifier)multipassIdentifier •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A unique identifier for the customer that's used with Multipass login.

[Anchor to note](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.note)note •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A note about the customer.

[Anchor to numberOfOrders](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.numberOfOrders)numberOfOrders •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The number of orders that the customer has made at the store in their lifetime.

[Anchor to orders](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders)orders •[OrderConnection!](/docs/api/admin-graphql/latest/connections/OrderConnection) non-null
:   A list of the customer's orders.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.sortKey)sortKey •[OrderSortKeys](/docs/api/admin-graphql/latest/enums/OrderSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.orders.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-cart_token) cart\_token •string
        :   Filter by the cart token's unique value to track abandoned cart conversions or troubleshoot checkout issues. The token references the cart that's associated with an order.

        Example:

        * `cart_token:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-channel) channel •string
        :   Filter by the channel information [`handle`](https://shopify.dev/api/admin-graphql/latest/objects/ChannelInformation#field-ChannelInformation.fields.channelDefinition.handle) (`ChannelInformation.channelDefinition.handle`) field.

        Example:

        * `channel:web`
        * `channel:web,pos`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-channel_id) channel\_id •id
        :   Filter by the channel [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.id) field.

        Example:

        * `channel_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-chargeback_status) chargeback\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-checkout_token) checkout\_token •string
        :   Filter by the checkout token's unique value to analyze conversion funnels or resolve payment issues. The checkout token's value references the checkout that's associated with an order.

        Example:

        * `checkout_token:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-confirmation_number) confirmation\_number •string
        :   Filter by the randomly generated alpha-numeric identifier for an order that can be displayed to the customer instead of the sequential order name. This value isn't guaranteed to be unique.

        Example:

        * `confirmation_number:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the order was created in Shopify's system.

        Example:

        * `created_at:2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-credit_card_last4) credit\_card\_last4 •string
        :   Filter by the last four digits of the payment card that was used to pay for the order. This filter matches only the last four digits of the card for heightened security.

        Example:

        * `credit_card_last4:1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-current_total_price) current\_total\_price •float
        :   Filter by the current total price of the order in the shop currency, including any returns/refunds/removals. This filter supports both exact values and ranges.

        Example:

        * `current_total_price:10`
        * `current_total_price:>=5.00 current_total_price:<=20.99`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-customer_id) customer\_id •id
        :   Filter orders by the customer [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Customer#field-Customer.fields.id) field.

        Example:

        * `customer_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-delivery_method) delivery\_method •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-discount_code) discount\_code •string
        :   Filter by the case-insensitive discount code that was applied to the order at checkout. Limited to the first discount code used on an order. Maximum characters: 255.

        Example:

        * `discount_code:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-email) email •string
        :   Filter by the email address that's associated with the order to provide customer support or analyze purchasing patterns.

        Example:

        * `email:example@shopify.com`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-financial_status) financial\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-fraud_protection_level) fraud\_protection\_level •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-fulfillment_location_id) fulfillment\_location\_id •id
        :   Filter by the fulfillment location [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.location.id) (`Fulfillment.location.id`) field.

        Example:

        * `fulfillment_location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-fulfillment_status) fulfillment\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-gateway) gateway •string
        :   Filter by the [`paymentGatewayNames`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.paymentGatewayNames) field. Use this filter to find orders that were processed through specific payment providers like Shopify Payments, PayPal, or other custom payment gateways.

        Example:

        * `gateway:shopify_payments`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-location_id) location\_id •id
        :   Filter by the location [`id`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id) that's associated with the order to view and manage orders for specific locations. For POS orders, locations must be defined in the Shopify admin under **Settings** > **Locations**. If no ID is provided, then the primary location of the shop is returned.

        Example:

        * `location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
        :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

        Example:

        * `metafields.custom.on_sale:true`
        * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-name) name •string
        :   Filter by the order [`name`](https://shopify.dev/api/admin-graphql/latest/objects/Order#field-name) field.

        Example:

        * `name:1001-A`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-payment_id) payment\_id •string
        :   Filter by the payment ID that's associated with the order to reconcile financial records or troubleshoot payment issues.

        Example:

        * `payment_id:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-payment_provider_id) payment\_provider\_id •id
        :   Filter by the ID of the payment provider that's associated with the order to manage payment methods or troubleshoot transactions.

        Example:

        * `payment_provider_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-po_number) po\_number •string
        :   Filter by the order [`poNumber`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.poNumber) field.

        Example:

        * `po_number:P01001`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-processed_at) processed\_at •time
        :   Filter by the order [`processedAt`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.processedAt) field.

        Example:

        * `processed_at:2021-01-01T00:00:00Z`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-reference_location_id) reference\_location\_id •id
        :   Filter by the ID of a location that's associated with the order, such as locations from fulfillments, refunds, or the shop's primary location.

        Example:

        * `reference_location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-return_status) return\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-risk_level) risk\_level •string
        :   Filter by the order risk assessment [`riskLevel`](https://shopify.dev/api/admin-graphql/latest/objects/OrderRiskAssessment#field-OrderRiskAssessment.fields.riskLevel) field.

        Valid values:

        * `high`
        * `medium`
        * `low`
        * `none`
        * `pending`

        Example:

        * `risk_level:high`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-sales_channel) sales\_channel •string
        :   Filter by the [sales channel](https://shopify.dev/docs/apps/build/sales-channels) where the order was made to analyze performance or manage fulfillment processes.

        Example:

        * `sales_channel: some_sales_channel`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-source_identifier) source\_identifier •string
        :   Filter by the ID of the order placed on the originating platform, such as a unique POS or third-party identifier. This value doesn't correspond to the Shopify ID that's generated from a completed draft order.

        Example:

        * `source_identifier:1234-12-1000`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-source_name) source\_name •string
        :   Filter by the platform where the order was placed to distinguish between web orders, POS sales, draft orders, or third-party channels. Use this filter to analyze sales performance across different ordering methods.

        Example:

        * `source_name:web`
        * `source_name:shopify_draft_order`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-status) status •string
        :   Filter by the order's status to manage workflows or analyze the order lifecycle.

        Valid values:

        * `open`
        * `closed`
        * `cancelled`
        * `not_closed`

        Example:

        * `status:open`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-subtotal_line_items_quantity) subtotal\_line\_items\_quantity •string
        :   Filter by the total number of items across all line items in an order. This filter supports both exact values and ranges, and is useful for identifying bulk orders or analyzing purchase volume patterns.

        Example:

        * `subtotal_line_items_quantity:10`
        * `subtotal_line_items_quantity:5..20`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-test) test •boolean
        :   Filter by test orders. Test orders are made using the [Shopify Bogus Gateway](https://help.shopify.com/manual/checkout-settings/test-orders/payments-test-mode#bogus-gateway) or a payment provider with test mode enabled.

        Example:

        * `test:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-total_weight) total\_weight •string
        :   Filter by the order weight. This filter supports both exact values and ranges, and is to be used to filter orders by the total weight of all items (excluding packaging). It takes a unit of measurement as a suffix. It accepts the following units: g, kg, lb, oz.

        Example:

        * `total_weight:10.5kg`
        * `total_weight:>=5g total_weight:<=20g`
        * `total_weight:.5 lb`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the order was last updated in Shopify's system.

        Example:

        * `updated_at:2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to paymentMethods](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods)paymentMethods •[CustomerPaymentMethodConnection!](/docs/api/admin-graphql/latest/connections/CustomerPaymentMethodConnection) non-null
:   A list of the customer's payment methods.

    Show fields

    ### Arguments

    [Anchor to showRevoked](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.showRevoked)showRevoked •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to show the customer's revoked payment method.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.paymentMethods.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to productSubscriberStatus](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.productSubscriberStatus)productSubscriberStatus •[CustomerProductSubscriberStatus!](/docs/api/admin-graphql/latest/enums/CustomerProductSubscriberStatus) non-null
:   Possible subscriber states of a customer defined by their subscription contracts.

    Show enum values

[Anchor to state](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.state)state •[CustomerState!](/docs/api/admin-graphql/latest/enums/CustomerState) non-null
:   The state of the customer's account with the shop.

    Please note that this only meaningful when Classic Customer Accounts is active.

    Show enum values

[Anchor to statistics](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.statistics)statistics •[CustomerStatistics!](/docs/api/admin-graphql/latest/objects/CustomerStatistics) non-null
:   The statistics for a given customer.

    Show fields

[Anchor to storeCreditAccounts](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts)storeCreditAccounts •[StoreCreditAccountConnection!](/docs/api/admin-graphql/latest/connections/StoreCreditAccountConnection) non-null
:   Returns a list of store credit accounts that belong to the owner resource.
    A store credit account owner can hold multiple accounts each with a different currency.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.storeCreditAccounts.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-currency_code) currency\_code •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

    ---

[Anchor to subscriptionContracts](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts)subscriptionContracts •[SubscriptionContractConnection!](/docs/api/admin-graphql/latest/connections/SubscriptionContractConnection) non-null
:   A list of the customer's subscription contracts.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to tags](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.tags)tags •[[String!]!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   A comma separated list of tags that have been added to the customer.

[Anchor to taxExempt](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.taxExempt)taxExempt •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the customer is exempt from being charged taxes on their orders.

[Anchor to taxExemptions](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.taxExemptions)taxExemptions •[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption) non-null
:   The list of tax exemptions applied to the customer.

    Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the customer was last updated.

[Anchor to verifiedEmail](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.verifiedEmail)verifiedEmail •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the customer has verified their email address. Defaults to `true` if the customer is created through the Shopify admin or API.

### Deprecated fields

* addresses ([MailingAddress!]!): deprecated
* email (String): deprecated
* emailMarketingConsent (CustomerEmailMarketingConsentState): deprecated
* hasTimelineComment (Boolean!): deprecated
* market (Market): deprecated
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated
* phone (String): deprecated
* smsMarketingConsent (CustomerSmsMarketingConsentState): deprecated
* unsubscribeUrl (URL!): deprecated
* validEmailAddress (Boolean!): deprecated

[Anchor to addresses](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addresses)addresses •[[MailingAddress!]!](/docs/api/admin-graphql/latest/objects/MailingAddress) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addresses.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   Truncate the array result to this size.

    ---

[Anchor to email](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.email)email •[String](/docs/api/admin-graphql/latest/scalars/String) Deprecated

[Anchor to emailMarketingConsent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.emailMarketingConsent)emailMarketingConsent •[CustomerEmailMarketingConsentState](/docs/api/admin-graphql/latest/objects/CustomerEmailMarketingConsentState) Deprecated
:   Show fields

[Anchor to hasTimelineComment](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.hasTimelineComment)hasTimelineComment •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-nullDeprecated

[Anchor to market](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.market)market •[Market](/docs/api/admin-graphql/latest/objects/Market) Deprecated
:   Show fields

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to phone](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.phone)phone •[String](/docs/api/admin-graphql/latest/scalars/String) Deprecated

[Anchor to smsMarketingConsent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.smsMarketingConsent)smsMarketingConsent •[CustomerSmsMarketingConsentState](/docs/api/admin-graphql/latest/objects/CustomerSmsMarketingConsentState) Deprecated
:   Show fields

[Anchor to unsubscribeUrl](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.unsubscribeUrl)unsubscribeUrl •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-nullDeprecated

[Anchor to validEmailAddress](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.validEmailAddress)validEmailAddress •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-nullDeprecated

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/Customer#queries)Queries

* customer (Customer)
* customerByIdentifier (Customer)
* customers (CustomerConnection!)

[Anchor to customer](/docs/api/admin-graphql/latest/objects/Customer#query-customer)[customer](/docs/api/admin-graphql/latest/queries/customer) •query
:   Returns a `Customer` resource by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Customer#query-customer.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `Customer` to return.

    ---

[Anchor to customerByIdentifier](/docs/api/admin-graphql/latest/objects/Customer#query-customerByIdentifier)[customerByIdentifier](/docs/api/admin-graphql/latest/queries/customerByIdentifier) •query
:   Return a customer by an identifier.

    Show fields

    ### Arguments

    [Anchor to identifier](/docs/api/admin-graphql/latest/objects/Customer#query-customerByIdentifier.arguments.identifier)identifier •[CustomerIdentifierInput!](/docs/api/admin-graphql/latest/input-objects/CustomerIdentifierInput) required
    :   The identifier of the customer.

        Show input fields

    ---

[Anchor to customers](/docs/api/admin-graphql/latest/objects/Customer#query-customers)[customers](/docs/api/admin-graphql/latest/queries/customers) •query
:   Returns a list of [customers](https://shopify.dev/api/admin-graphql/latest/objects/Customer) in your Shopify store, including key information such as name, email, location, and purchase history.
    Use this query to segment your audience, personalize marketing campaigns, or analyze customer behavior by applying filters based on location, order history, marketing preferences and tags.
    The `customers` query supports [pagination](https://shopify.dev/api/usage/pagination-graphql) and [sorting](https://shopify.dev/api/admin-graphql/latest/enums/CustomerSortKeys).

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.sortKey)sortKey •[CustomerSortKeys](/docs/api/admin-graphql/latest/enums/CustomerSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Customer#query-customers.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-accepts_marketing) accepts\_marketing •boolean
        :   Filter by whether a customer has consented to receive marketing material.

        Example:

        * `accepts_marketing:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-country) country •string
        :   Filter by the country associated with the customer's address. Use either the country name or the two-letter country code.

        Example:

        * `country:Canada`
        * `country:JP`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-customer_date) customer\_date •time
        :   Filter by the date and time when the customer record was created. This query parameter filters by the [`createdAt`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-createdAt) field.

        Example:

        * `customer_date:'2024-03-15T14:30:00Z'`
        * `customer_date: >='2024-01-01'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-email) email •string
        :   The customer's email address, used to communicate information about orders and for the purposes of email marketing campaigns. You can use a wildcard value to filter the query by customers who have an email address specified. Please note that *email* is a tokenized field: To retrieve exact matches, quote the email address (*phrase query*) as described in [Shopify API search syntax](https://shopify.dev/docs/api/usage/search-syntax).

        Example:

        * `email:gmail.com`
        * `email:"bo.wang@example.com"`
        * `email:*`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-first_name) first\_name •string
        :   Filter by the customer's first name.

        Example:

        * `first_name:Jane`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-last_abandoned_order_date) last\_abandoned\_order\_date •time
        :   Filter by the date and time of the customer's most recent abandoned checkout. An abandoned checkout occurs when a customer adds items to their cart, begins the checkout process, but leaves the site without completing their purchase.

        Example:

        * `last_abandoned_order_date:'2024-04-01T10:00:00Z'`
        * `last_abandoned_order_date: >='2024-01-01'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-last_name) last\_name •string
        :   Filter by the customer's last name.

        Example:

        * `last_name:Reeves`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-order_date) order\_date •time
        :   Filter by the date and time that the order was placed by the customer. Use this query filter to check if a customer has placed at least one order within a specified date range.

        Example:

        * `order_date:'2024-02-20T00:00:00Z'`
        * `order_date: >='2024-01-01'`
        * `order_date:'2024-01-01..2024-03-31'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-orders_count) orders\_count •integer
        :   Filter by the total number of orders a customer has placed.

        Example:

        * `orders_count:5`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-phone) phone •string
        :   The phone number of the customer, used to communicate information about orders and for the purposes of SMS marketing campaigns. You can use a wildcard value to filter the query by customers who have a phone number specified.

        Example:

        * `phone:+18005550100`
        * `phone:*`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-state) state •string
        :   Filter by the [state](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-state) of the customer's account with the shop. This filter is only valid when [Classic Customer Accounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerAccountsV2#field-customerAccountsVersion) is active.

        Example:

        * `state:ENABLED`
        * `state:INVITED`
        * `state:DISABLED`
        * `state:DECLINED`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-tag) tag •string
        :   Filter by the tags that are associated with the customer. This query parameter accepts multiple tags separated by commas.

        Example:

        * `tag:'VIP'`
        * `tag:'Wholesale,Repeat'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-tag_not) tag\_not •string
        :   Filter by the tags that aren't associated with the customer. This query parameter accepts multiple tags separated by commas.

        Example:

        * `tag_not:'Prospect'`
        * `tag_not:'Test,Internal'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-total_spent) total\_spent •float
        :   Filter by the total amount of money a customer has spent across all orders.

        Example:

        * `total_spent:100.50`
        * `total_spent:50.00`
        * `total_spent:>100.50`
        * `total_spent:>50.00`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Customer#argument-query-filter-updated_at) updated\_at •time
        :   The date and time, matching a whole day, when the customer's information was last updated.

        Example:

        * `updated_at:2024-01-01T00:00:00Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/Customer#mutations)Mutations

* customerAddTaxExemptions (CustomerAddTaxExemptionsPayload)
* customerCreate (CustomerCreatePayload)
* customerEmailMarketingConsentUpdate (CustomerEmailMarketingConsentUpdatePayload)
* customerPaymentMethodSendUpdateEmail (CustomerPaymentMethodSendUpdateEmailPayload)
* customerRemoveTaxExemptions (CustomerRemoveTaxExemptionsPayload)
* customerReplaceTaxExemptions (CustomerReplaceTaxExemptionsPayload)
* customerSendAccountInviteEmail (CustomerSendAccountInviteEmailPayload)
* customerSet (CustomerSetPayload)
* customerSmsMarketingConsentUpdate (CustomerSmsMarketingConsentUpdatePayload)
* customerUpdate (CustomerUpdatePayload)
* customerUpdateDefaultAddress (CustomerUpdateDefaultAddressPayload)

[Anchor to customerAddTaxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerAddTaxExemptions)[customerAddTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerAddTaxExemptions) •mutation
:   Add tax exemptions for the customer.

    Show payload

    ### Arguments

    [Anchor to customerId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerAddTaxExemptions.arguments.customerId)customerId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer to update.

    [Anchor to taxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerAddTaxExemptions.arguments.taxExemptions)taxExemptions •[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption) required
    :   The list of tax exemptions to add for the customer, in the format of an array or a comma-separated list. Example values: `["CA_BC_RESELLER_EXEMPTION", "CA_STATUS_CARD_EXEMPTION"]`, `"CA_BC_RESELLER_EXEMPTION, CA_STATUS_CARD_EXEMPTION"`.

        Show enum values

    ---

[Anchor to customerCreate](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerCreate)[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate) •mutation
:   Creates a new [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer) in the store.

    Accepts customer details including contact information, marketing consent preferences, and tax exemptions through the [`CustomerInput`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/CustomerInput) input object. You can also associate [`metafields`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/MetafieldInput) and tags to organize and extend customer data.

    Apps using protected customer data must meet Shopify's [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerCreate.arguments.input)input •[CustomerInput!](/docs/api/admin-graphql/latest/input-objects/CustomerInput) required
    :   The input fields to create a customer.

        Show input fields

    ---

[Anchor to customerEmailMarketingConsentUpdate](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerEmailMarketingConsentUpdate)[customerEmailMarketingConsentUpdate](/docs/api/admin-graphql/latest/mutations/customerEmailMarketingConsentUpdate) •mutation
:   Updates a [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer)'s email marketing consent information. The customer must have an email address to update their consent. Records the [marketing state](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerEmailAddress#field-marketingState) (such as subscribed, pending, unsubscribed), [opt-in level](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerEmailAddress#field-marketingOptInLevel), and when and where the customer gave or withdrew consent.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerEmailMarketingConsentUpdate.arguments.input)input •[CustomerEmailMarketingConsentUpdateInput!](/docs/api/admin-graphql/latest/input-objects/CustomerEmailMarketingConsentUpdateInput) required
    :   Specifies the input fields to update a customer's email marketing consent information.

        Show input fields

    ---

[Anchor to customerPaymentMethodSendUpdateEmail](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerPaymentMethodSendUpdateEmail)[customerPaymentMethodSendUpdateEmail](/docs/api/admin-graphql/latest/mutations/customerPaymentMethodSendUpdateEmail) •mutation
:   Sends a link to the customer so they can update a specific payment method.

    Show payload

    ### Arguments

    [Anchor to customerPaymentMethodId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerPaymentMethodSendUpdateEmail.arguments.customerPaymentMethodId)customerPaymentMethodId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The payment method to be updated.

    [Anchor to email](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerPaymentMethodSendUpdateEmail.arguments.email)email •[EmailInput](/docs/api/admin-graphql/latest/input-objects/EmailInput)
    :   Specifies the payment method update email fields. Only the 'from' and 'bcc' fields are accepted for input.

        Show input fields

    ---

[Anchor to customerRemoveTaxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerRemoveTaxExemptions)[customerRemoveTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerRemoveTaxExemptions) •mutation
:   Remove tax exemptions from a customer.

    Show payload

    ### Arguments

    [Anchor to customerId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerRemoveTaxExemptions.arguments.customerId)customerId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer to update.

    [Anchor to taxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerRemoveTaxExemptions.arguments.taxExemptions)taxExemptions •[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption) required
    :   The list of tax exemptions to remove for the customer, in the format of an array or a comma-separated list. Example values: `["CA_BC_RESELLER_EXEMPTION", "A_STATUS_CARD_EXEMPTION"]`, `"CA_BC_RESELLER_EXEMPTION, CA_STATUS_CARD_EXEMPTION"`.

        Show enum values

    ---

[Anchor to customerReplaceTaxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerReplaceTaxExemptions)[customerReplaceTaxExemptions](/docs/api/admin-graphql/latest/mutations/customerReplaceTaxExemptions) •mutation
:   Replace tax exemptions for a customer.

    Show payload

    ### Arguments

    [Anchor to customerId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerReplaceTaxExemptions.arguments.customerId)customerId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer to update.

    [Anchor to taxExemptions](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerReplaceTaxExemptions.arguments.taxExemptions)taxExemptions •[[TaxExemption!]!](/docs/api/admin-graphql/latest/enums/TaxExemption) required
    :   The list of tax exemptions that will replace the current exemptions for a customer. Can be an array or a comma-separated list.
        Example values: `["CA_BC_RESELLER_EXEMPTION", "A_STATUS_CARD_EXEMPTION"]`, `"CA_BC_RESELLER_EXEMPTION, CA_STATUS_CARD_EXEMPTION"`.

        Show enum values

    ---

[Anchor to customerSendAccountInviteEmail](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSendAccountInviteEmail)[customerSendAccountInviteEmail](/docs/api/admin-graphql/latest/mutations/customerSendAccountInviteEmail) •mutation
:   Sends an email invitation for a customer to create a legacy customer account. The invitation lets customers set up their password and activate their account in the online store.

    You can optionally customize the email content including the subject, sender, recipients, and message body. If you don't provide email customization, the store uses its default account invitation template.

    ---

    Note

    The invite only works when legacy customer accounts are enabled on the shop.

    **Note:**

    The invite only works when legacy customer accounts are enabled on the shop.

    **Note:** The invite only works when legacy customer accounts are enabled on the shop.

    ---

    Show payload

    ### Arguments

    [Anchor to customerId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSendAccountInviteEmail.arguments.customerId)customerId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer to whom an account invite email is to be sent.

    [Anchor to email](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSendAccountInviteEmail.arguments.email)email •[EmailInput](/docs/api/admin-graphql/latest/input-objects/EmailInput)
    :   Specifies the account invite email fields.

        Show input fields

    ---

[Anchor to customerSet](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSet)[customerSet](/docs/api/admin-graphql/latest/mutations/customerSet) •mutation
:   Creates or updates a customer in a single mutation.

    Use this mutation when syncing information from an external data source into Shopify.

    This mutation can be used to create a new customer, update an existing customer by id, or
    upsert a customer by a unique key (email or phone).

    To create a new customer omit the `identifier` argument.
    To update an existing customer, include the `identifier` with the id of the customer to update.

    To perform an 'upsert' by unique key (email or phone)
    use the `identifier` argument to upsert a customer by a unique key (email or phone). If a customer
    with the specified unique key exists, it will be updated. If not, a new customer will be created with
    that unique key.

    As of API version 2022-10, apps using protected customer data must meet the
    protected customer data [requirements](https://shopify.dev/apps/store/data-protection/protected-customer-data)

    Any list field (e.g.
    [addresses](https://shopify.dev/api/admin-graphql/unstable/input-objects/MailingAddressInput),
    will be updated so that all included entries are either created or updated, and all existing entries not
    included will be deleted.

    All other fields will be updated to the value passed. Omitted fields will not be updated.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSet.arguments.input)input •[CustomerSetInput!](/docs/api/admin-graphql/latest/input-objects/CustomerSetInput) required
    :   The properties of the customer.

        Show input fields

    [Anchor to identifier](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSet.arguments.identifier)identifier •[CustomerSetIdentifiers](/docs/api/admin-graphql/latest/input-objects/CustomerSetIdentifiers)
    :   Specifies the identifier that will be used to lookup the resource.

        Show input fields

    ---

[Anchor to customerSmsMarketingConsentUpdate](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSmsMarketingConsentUpdate)[customerSmsMarketingConsentUpdate](/docs/api/admin-graphql/latest/mutations/customerSmsMarketingConsentUpdate) •mutation
:   Updates a [customer](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer)'s SMS marketing consent information. The customer must have a phone number on their account to receive SMS marketing.

    You can set whether the customer subscribes or unsubscribes to SMS marketing and specify the [opt-in level](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSmsMarketingConsentUpdate#arguments-input.fields.smsMarketingConsent.marketingOptInLevel). Optionally include when the consent was collected and which [location](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSmsMarketingConsentUpdate#arguments-input.fields.smsMarketingConsent.sourceLocationId) collected it.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerSmsMarketingConsentUpdate.arguments.input)input •[CustomerSmsMarketingConsentUpdateInput!](/docs/api/admin-graphql/latest/input-objects/CustomerSmsMarketingConsentUpdateInput) required
    :   Specifies the input fields to update a customer's SMS marketing consent information.

        Show input fields

    ---

[Anchor to customerUpdate](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerUpdate)[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate) •mutation
:   Updates a [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer)'s attributes including personal information and [`tax exemptions`](https://shopify.dev/docs/api/admin-graphql/latest/enums/TaxExemption).

    Apps using protected customer data must meet Shopify's [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerUpdate.arguments.input)input •[CustomerInput!](/docs/api/admin-graphql/latest/input-objects/CustomerInput) required
    :   Provides updated fields for the customer. To set marketing consent, use the `customerEmailMarketingConsentUpdate` or `customerSmsMarketingConsentUpdate` mutations instead.

        Show input fields

    ---

[Anchor to customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerUpdateDefaultAddress)[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress) •mutation
:   Updates a customer's default address.

    Show payload

    ### Arguments

    [Anchor to customerId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerUpdateDefaultAddress.arguments.customerId)customerId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer whose default address is being updated.

    [Anchor to addressId](/docs/api/admin-graphql/latest/objects/Customer#mutation-customerUpdateDefaultAddress.arguments.addressId)addressId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the customer's new default address.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Customer#interfaces)Interfaces

* CommentEventSubject
* HasEvents
* HasMetafieldDefinitions
* HasMetafields
* HasStoreCreditAccounts
* LegacyInteroperability
* Node

[Anchor to CommentEventSubject](/docs/api/admin-graphql/latest/objects/Customer#interface-CommentEventSubject)[CommentEventSubject](/docs/api/admin-graphql/latest/interfaces/CommentEventSubject) •interface

[Anchor to HasEvents](/docs/api/admin-graphql/latest/objects/Customer#interface-HasEvents)[HasEvents](/docs/api/admin-graphql/latest/interfaces/HasEvents) •interface

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/Customer#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/Customer#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasStoreCreditAccounts](/docs/api/admin-graphql/latest/objects/Customer#interface-HasStoreCreditAccounts)[HasStoreCreditAccounts](/docs/api/admin-graphql/latest/interfaces/HasStoreCreditAccounts) •interface

[Anchor to LegacyInteroperability](/docs/api/admin-graphql/latest/objects/Customer#interface-LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Customer#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo