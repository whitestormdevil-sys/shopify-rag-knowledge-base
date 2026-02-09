---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_assigned_fulfillment_orders` access scope, `read_merchant_managed_fulfillment_orders` access scope, `read_third_party_fulfillment_orders` access scope or `read_marketplace_fulfillment_orders` access scope.

The FulfillmentOrder object represents either an item or a group of items in an
[Order](https://shopify.dev/api/admin-graphql/latest/objects/Order)
that are expected to be fulfilled from the same location.
There can be more than one fulfillment order for an
[order](https://shopify.dev/api/admin-graphql/latest/objects/Order)
at a given location.

![](/assets/api/reference/fulfillment_order_relationships.png)

Fulfillment orders represent the work which is intended to be done in relation to an order.
When fulfillment has started for one or more line items, a
[Fulfillment](https://shopify.dev/api/admin-graphql/latest/objects/Fulfillment)
is created by a merchant or third party to represent the ongoing or completed work of fulfillment.

[See below for more details on creating fulfillments](#the-lifecycle-of-a-fulfillment-order-at-a-location-which-is-managed-by-a-fulfillment-service).

---

Note

Shopify creates fulfillment orders automatically when an order is created.
It is not possible to manually create fulfillment orders.

[See below for more details on the lifecycle of a fulfillment order](#the-lifecycle-of-a-fulfillment-order).

**Note:**

Shopify creates fulfillment orders automatically when an order is created.
It is not possible to manually create fulfillment orders.

[See below for more details on the lifecycle of a fulfillment order](#the-lifecycle-of-a-fulfillment-order).

**Note:** Shopify creates fulfillment orders automatically when an order is created.
It is not possible to manually create fulfillment orders.</p>
<p><a href="#the-lifecycle-of-a-fulfillment-order">See below for more details on the lifecycle of a fulfillment order</a>.

---

## Retrieving fulfillment orders

### Fulfillment orders from an order

All fulfillment orders related to a given order can be retrieved with the
[Order.fulfillmentOrders](https://shopify.dev/api/admin-graphql/latest/objects/Order#connection-order-fulfillmentorders)
connection.

[API access scopes](#api-access-scopes)
govern which fulfillments orders are returned to clients.
An API client will only receive a subset of the fulfillment orders which belong to an order
if they don't have the necessary access scopes to view all of the fulfillment orders.

### Fulfillment orders assigned to the app for fulfillment

Fulfillment service apps can retrieve the fulfillment orders which have been assigned to their locations with the
[assignedFulfillmentOrders](https://shopify.dev/api/admin-graphql/2024-07/objects/queryroot#connection-assignedfulfillmentorders)
connection.
Use the `assignmentStatus` argument to control whether all assigned fulfillment orders
should be returned or only those where a merchant has sent a
[fulfillment request](https://shopify.dev/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest)
and it has yet to be responded to.

The API client must be granted the `read_assigned_fulfillment_orders` access scope to access
the assigned fulfillment orders.

### All fulfillment orders

Apps can retrieve all fulfillment orders with the
[fulfillmentOrders](https://shopify.dev/api/admin-graphql/latest/queries/fulfillmentOrders)
query. This query returns all assigned, merchant-managed, and third-party fulfillment orders on the shop,
which are accessible to the app according to the
[fulfillment order access scopes](#api-access-scopes) it was granted with.

## The lifecycle of a fulfillment order

### Fulfillment Order Creation

After an order is created, a background worker performs the order routing process which determines
which locations will be responsible for fulfilling the purchased items.
Once the order routing process is complete, one or more fulfillment orders will be created
and assigned to these locations. It is not possible to manually create fulfillment orders.

Once a fulfillment order has been created, it will have one of two different lifecycles depending on
the type of location which the fulfillment order is assigned to.

### The lifecycle of a fulfillment order at a merchant managed location

Fulfillment orders are completed by creating
[fulfillments](https://shopify.dev/api/admin-graphql/latest/objects/Fulfillment).
Fulfillments represents the work done.

For digital products a merchant or an order management app would create a fulfilment once the digital asset
has been provisioned.
For example, in the case of a digital gift card, a merchant would to do this once
the gift card has been activated - before the email has been shipped.

On the other hand, for a traditional shipped order,
a merchant or an order management app would create a fulfillment after picking and packing the items relating
to a fulfillment order, but before the courier has collected the goods.

[Learn about managing fulfillment orders as an order management app](https://shopify.dev/apps/fulfillment/order-management-apps/manage-fulfillments).

### The lifecycle of a fulfillment order at a location which is managed by a fulfillment service

For fulfillment orders which are assigned to a location that is managed by a fulfillment service,
a merchant or an Order Management App can
[send a fulfillment request](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest)
to the fulfillment service which operates the location to request that they fulfill the associated items.
A fulfillment service has the option to
[accept](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest)
or [reject](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderRejectFulfillmentRequest)
this fulfillment request.

Once the fulfillment service has accepted the request, the request can no longer be cancelled by the merchant
or order management app and instead a
[cancellation request must be submitted](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitCancellationRequest)
to the fulfillment service.

Once a fulfillment service accepts a fulfillment request,
then after they are ready to pack items and send them for delivery, they create fulfillments with the
[fulfillmentCreate](https://shopify.dev/api/admin-graphql/unstable/mutations/fulfillmentCreate)
mutation.
They can provide tracking information right away or create fulfillments without it and then
update the tracking information for fulfillments with the
[fulfillmentTrackingInfoUpdate](https://shopify.dev/api/admin-graphql/unstable/mutations/fulfillmentTrackingInfoUpdate)
mutation.

[Learn about managing fulfillment orders as a fulfillment service](https://shopify.dev/apps/fulfillment/fulfillment-service-apps/manage-fulfillments).

## API access scopes

Fulfillment orders are governed by the following API access scopes:

* The `read_merchant_managed_fulfillment_orders` and
  `write_merchant_managed_fulfillment_orders` access scopes
  grant access to fulfillment orders assigned to merchant-managed locations.
* The `read_assigned_fulfillment_orders` and `write_assigned_fulfillment_orders`
  access scopes are intended for fulfillment services.
  These scopes grant access to fulfillment orders assigned to locations that are being managed
  by fulfillment services.
* The `read_third_party_fulfillment_orders` and `write_third_party_fulfillment_orders`
  access scopes grant access to fulfillment orders
  assigned to locations managed by other fulfillment services.

### Fulfillment service app access scopes

Usually, **fulfillment services** have the `write_assigned_fulfillment_orders` access scope
and don't have the `*_third_party_fulfillment_orders`
or `*_merchant_managed_fulfillment_orders` access scopes.
The app will only have access to the fulfillment orders assigned to their location
(or multiple locations if the app registers multiple fulfillment services on the shop).
The app will not have access to fulfillment orders assigned to merchant-managed locations
or locations owned by other fulfillment service apps.

### Order management app access scopes

**Order management apps** will usually request `write_merchant_managed_fulfillment_orders` and
`write_third_party_fulfillment_orders` access scopes. This will allow them to manage all fulfillment orders
on behalf of a merchant.

If an app combines the functions of an order management app and a fulfillment service,
then the app should request all
access scopes to manage all assigned and all unassigned fulfillment orders.

## Notifications about fulfillment orders

Fulfillment services are required to
[register](https://shopify.dev/api/admin-graphql/latest/objects/FulfillmentService)
a self-hosted callback URL which has a number of uses. One of these uses is that this callback URL will be notified
whenever a merchant submits a fulfillment or cancellation request.

Both merchants and apps can
[subscribe](https://shopify.dev/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#webhooks)
to the
[fulfillment order webhooks](https://shopify.dev/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-fulfillmentorderscancellationrequestaccepted)
to be notified whenever fulfillment order related domain events occur.

[Learn about fulfillment workflows](https://shopify.dev/apps/fulfillment).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#fields)Fields

* assignedLocation (FulfillmentOrderAssignedLocation!)
* channelId (ID)
* createdAt (DateTime!)
* deliveryMethod (DeliveryMethod)
* destination (FulfillmentOrderDestination)
* fulfillAt (DateTime)
* fulfillBy (DateTime)
* fulfillmentHolds ([FulfillmentHold!]!)
* fulfillmentOrdersForMerge (FulfillmentOrderConnection!)
* fulfillments (FulfillmentConnection!)
* id (ID!)
* internationalDuties (FulfillmentOrderInternationalDuties)
* lineItems (FulfillmentOrderLineItemConnection!)
* locationsForMove (FulfillmentOrderLocationForMoveConnection!)
* merchantRequests (FulfillmentOrderMerchantRequestConnection!)
* order (Order!)
* orderId (ID!)
* orderName (String!)
* orderProcessedAt (DateTime!)
* requestStatus (FulfillmentOrderRequestStatus!)
* status (FulfillmentOrderStatus!)
* supportedActions ([FulfillmentOrderSupportedAction!]!)
* updatedAt (DateTime!)

[Anchor to assignedLocation](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.assignedLocation)assignedLocation •[FulfillmentOrderAssignedLocation!](/docs/api/admin-graphql/latest/objects/FulfillmentOrderAssignedLocation) non-null
:   The fulfillment order's assigned location. This is the location where the fulfillment is expected to happen.

    The fulfillment order's assigned location might change in the following cases:

    * The fulfillment order has been entirely moved to a new location. For example, the [fulfillmentOrderMove](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderMove) mutation has been called, and you see the original fulfillment order in the [movedFulfillmentOrder](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderMove#field-fulfillmentordermovepayload-movedfulfillmentorder) field within the mutation's response.
    * Work on the fulfillment order hasn't yet begun, which means that the fulfillment order has the
      [OPEN](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-open),
      [SCHEDULED](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-scheduled), or
      [ON\_HOLD](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderStatus#value-onhold)
      status, and the shop's location properties might be undergoing edits (for example, in the Shopify admin).

    Show fields

[Anchor to channelId](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.channelId)channelId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   ID of the channel that created the order.

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   Date and time when the fulfillment order was created.

[Anchor to deliveryMethod](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.deliveryMethod)deliveryMethod •[DeliveryMethod](/docs/api/admin-graphql/latest/objects/DeliveryMethod)
:   Delivery method of this fulfillment order.

    Show fields

[Anchor to destination](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.destination)destination •[FulfillmentOrderDestination](/docs/api/admin-graphql/latest/objects/FulfillmentOrderDestination)
:   The destination where the items should be sent.

    Show fields

[Anchor to fulfillAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillAt)fulfillAt •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The date and time at which the fulfillment order will be fulfillable. When this date and time is reached, the scheduled fulfillment order is automatically transitioned to open. For example, the `fulfill_at` date for a subscription order might be the 1st of each month, a pre-order `fulfill_at` date would be `nil`, and a standard order `fulfill_at` date would be the order creation date.

[Anchor to fulfillBy](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillBy)fulfillBy •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The latest date and time by which all items in the fulfillment order need to be fulfilled.

[Anchor to fulfillmentHolds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentHolds)fulfillmentHolds •[[FulfillmentHold!]!](/docs/api/admin-graphql/latest/objects/FulfillmentHold) non-null
:   The fulfillment holds applied on the fulfillment order.

    Show fields

[Anchor to fulfillmentOrdersForMerge](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge)fulfillmentOrdersForMerge •[FulfillmentOrderConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderConnection) non-null
:   Fulfillment orders eligible for merging with the given fulfillment order.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentOrdersForMerge.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to fulfillments](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments)fulfillments •[FulfillmentConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentConnection) non-null
:   A list of fulfillments for the fulfillment order.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillments.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to internationalDuties](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.internationalDuties)internationalDuties •[FulfillmentOrderInternationalDuties](/docs/api/admin-graphql/latest/objects/FulfillmentOrderInternationalDuties)
:   The duties delivery method of this fulfillment order.

    Show fields

[Anchor to lineItems](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems)lineItems •[FulfillmentOrderLineItemConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderLineItemConnection) non-null
:   A list of the fulfillment order's line items.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to locationsForMove](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove)locationsForMove •[FulfillmentOrderLocationForMoveConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderLocationForMoveConnection) non-null
:   A list of locations that the fulfillment order can potentially move to.

    Show fields

    ### Arguments

    [Anchor to lineItemIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.lineItemIds)lineItemIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID) Default:[]
    :   Filter to a list of Fulfillment Order Line Items.

    [Anchor to query](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-active) active •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-address1) address1 •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-address2) address2 •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-city) city •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-country) country •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-geolocated) geolocated •boolean

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-legacy) legacy •boolean

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-location_id) location\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-name) name •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-pickup_in_store) pickup\_in\_store •string


        Valid values:

        * `enabled`
        * `disabled`

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-province) province •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-zip) zip •string

    [Anchor to locationIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.locationIds)locationIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   Specific Location ids to check for the movability for a fulfillment order.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.locationsForMove.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to merchantRequests](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests)merchantRequests •[FulfillmentOrderMerchantRequestConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderMerchantRequestConnection) non-null
:   A list of requests sent by the merchant or an order management app to the fulfillment service for the fulfillment order.

    Show fields

    ### Arguments

    [Anchor to kind](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.kind)kind •[FulfillmentOrderMerchantRequestKind](/docs/api/admin-graphql/latest/enums/FulfillmentOrderMerchantRequestKind)
    :   The kind of request the merchant sent.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.merchantRequests.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to order](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.order)order •[Order!](/docs/api/admin-graphql/latest/objects/Order) non-null
:   The order that's associated with the fulfillment order.

    Show fields

[Anchor to orderId](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.orderId)orderId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   ID of the order that's associated with the fulfillment order.

[Anchor to orderName](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.orderName)orderName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The unique identifier for the order that appears on the order page in the Shopify admin and the **Order status** page.
    For example, "#1001", "EN1001", or "1001-A".
    This value isn't unique across multiple stores.

[Anchor to orderProcessedAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.orderProcessedAt)orderProcessedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the order was processed.
    This date and time might not match the date and time when the order was created.

[Anchor to requestStatus](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.requestStatus)requestStatus •[FulfillmentOrderRequestStatus!](/docs/api/admin-graphql/latest/enums/FulfillmentOrderRequestStatus) non-null
:   The request status of the fulfillment order.

    Show enum values

[Anchor to status](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.status)status •[FulfillmentOrderStatus!](/docs/api/admin-graphql/latest/enums/FulfillmentOrderStatus) non-null
:   The status of the fulfillment order.

    Show enum values

[Anchor to supportedActions](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.supportedActions)supportedActions •[[FulfillmentOrderSupportedAction!]!](/docs/api/admin-graphql/latest/objects/FulfillmentOrderSupportedAction) non-null
:   The actions that can be performed on this fulfillment order.

    Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the fulfillment order was last updated.

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#queries)Queries

* assignedFulfillmentOrders (FulfillmentOrderConnection!)
* fulfillmentOrder (FulfillmentOrder)
* fulfillmentOrders (FulfillmentOrderConnection!)
* manualHoldsFulfillmentOrders (FulfillmentOrderConnection!)

[Anchor to assignedFulfillmentOrders](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders)[assignedFulfillmentOrders](/docs/api/admin-graphql/latest/queries/assignedFulfillmentOrders) •query
:   The paginated list of fulfillment orders assigned to the shop locations owned by the app.

    Assigned fulfillment orders are fulfillment orders that are set to be fulfilled from locations
    managed by
    [fulfillment services](https://shopify.dev/api/admin-graphql/latest/objects/FulfillmentService)
    that are registered by the app.
    One app (api\_client) can host multiple fulfillment services on a shop.
    Each fulfillment service manages a dedicated location on a shop.
    Assigned fulfillment orders can have associated
    [fulfillment requests](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderRequestStatus),
    or might currently not be requested to be fulfilled.

    The app must have the `read_assigned_fulfillment_orders`
    [access scope](https://shopify.dev/docs/api/usage/access-scopes)
    to be able to retrieve the fulfillment orders assigned to its locations.

    All assigned fulfillment orders (except those with the `CLOSED` status) will be returned by default.
    Perform filtering with the `assignmentStatus` argument
    to receive only fulfillment orders that have been requested to be fulfilled.

    Show fields

    ### Arguments

    [Anchor to assignmentStatus](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.assignmentStatus)assignmentStatus •[FulfillmentOrderAssignmentStatus](/docs/api/admin-graphql/latest/enums/FulfillmentOrderAssignmentStatus)
    :   The assigment status of the fulfillment orders that should be returned.
        If `assignmentStatus` argument is not provided, then
        the query will return all assigned fulfillment orders,
        except those that have the `CLOSED` status.

        Show enum values

    [Anchor to locationIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.locationIds)locationIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   Returns fulfillment orders only for certain locations, specified by a list of location IDs.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-assignedFulfillmentOrders.arguments.sortKey)sortKey •[FulfillmentOrderSortKeys](/docs/api/admin-graphql/latest/enums/FulfillmentOrderSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    ---

[Anchor to fulfillmentOrder](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrder)[fulfillmentOrder](/docs/api/admin-graphql/latest/queries/fulfillmentOrder) •query
:   Returns a `FulfillmentOrder` resource by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrder.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `FulfillmentOrder` to return.

    ---

[Anchor to fulfillmentOrders](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders)[fulfillmentOrders](/docs/api/admin-graphql/latest/queries/fulfillmentOrders) •query
:   The paginated list of all fulfillment orders.
    The returned fulfillment orders are filtered according to the
    [fulfillment order access scopes](https://shopify.dev/api/admin-graphql/latest/objects/fulfillmentorder#api-access-scopes)
    granted to the app.

    Use this query to retrieve fulfillment orders assigned to merchant-managed locations,
    third-party fulfillment service locations, or all kinds of locations together.

    For fetching only the fulfillment orders assigned to the app's locations, use the
    [assignedFulfillmentOrders](https://shopify.dev/api/admin-graphql/2024-07/objects/queryroot#connection-assignedfulfillmentorders)
    connection.

    Show fields

    ### Arguments

    [Anchor to includeClosed](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.includeClosed)includeClosed •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to include closed fulfillment orders.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.sortKey)sortKey •[FulfillmentOrderSortKeys](/docs/api/admin-graphql/latest/enums/FulfillmentOrderSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-fulfillmentOrders.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-assigned_location_id) assigned\_location\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-status) status •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#argument-query-filter-updated_at) updated\_at •time

    ---

[Anchor to manualHoldsFulfillmentOrders](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders)[manualHoldsFulfillmentOrders](/docs/api/admin-graphql/latest/queries/manualHoldsFulfillmentOrders) •query
:   Returns a list of fulfillment orders that are on hold.

    Show fields

    ### Arguments

    [Anchor to query](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The query conditions used to filter fulfillment orders. Only fulfillment orders corresponding to orders matching the query will be counted.
        Supported filter parameters:

        * `order_financial_status`
        * `order_risk_level`
        * `shipping_address_coordinates_validated`

        See the detailed [search syntax](https://shopify.dev/api/usage/search-syntax)
        for more information about using filters.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#query-manualHoldsFulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutations)Mutations

* fulfillmentOrderAcceptCancellationRequest (FulfillmentOrderAcceptCancellationRequestPayload)
* fulfillmentOrderAcceptFulfillmentRequest (FulfillmentOrderAcceptFulfillmentRequestPayload)
* fulfillmentOrderCancel (FulfillmentOrderCancelPayload)
* fulfillmentOrderClose (FulfillmentOrderClosePayload)
* fulfillmentOrderHold (FulfillmentOrderHoldPayload)
* fulfillmentOrderMove (FulfillmentOrderMovePayload)
* fulfillmentOrderOpen (FulfillmentOrderOpenPayload)
* fulfillmentOrderRejectCancellationRequest (FulfillmentOrderRejectCancellationRequestPayload)
* fulfillmentOrderRejectFulfillmentRequest (FulfillmentOrderRejectFulfillmentRequestPayload)
* fulfillmentOrderReleaseHold (FulfillmentOrderReleaseHoldPayload)
* fulfillmentOrderReschedule (FulfillmentOrderReschedulePayload)
* fulfillmentOrdersReroute (FulfillmentOrdersReroutePayload)
* fulfillmentOrderSubmitCancellationRequest (FulfillmentOrderSubmitCancellationRequestPayload)
* fulfillmentOrderSubmitFulfillmentRequest (FulfillmentOrderSubmitFulfillmentRequestPayload)

[Anchor to fulfillmentOrderAcceptCancellationRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptCancellationRequest)[fulfillmentOrderAcceptCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptCancellationRequest) •mutation
:   Accept a cancellation request sent to a fulfillment service for a fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptCancellationRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with the cancellation request.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptCancellationRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for accepting the cancellation request.

    ---

[Anchor to fulfillmentOrderAcceptFulfillmentRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptFulfillmentRequest)[fulfillmentOrderAcceptFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest) •mutation
:   Accepts a fulfillment request that the fulfillment service has received for a [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) which signals that the fulfillment service will process and fulfill the order. The fulfillment service can optionally provide a message to the merchant and an estimated shipped date when accepting the request.

    Learn more about [accepting fulfillment requests](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#accept-a-fulfillment-request).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptFulfillmentRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with the fulfillment request.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptFulfillmentRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for accepting the fulfillment request.

    [Anchor to estimatedShippedAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderAcceptFulfillmentRequest.arguments.estimatedShippedAt)estimatedShippedAt •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
    :   The estimated date and time when the fulfillment order will be shipped.

    ---

[Anchor to fulfillmentOrderCancel](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderCancel)[fulfillmentOrderCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderCancel) •mutation
:   Cancels a [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) and creates a replacement fulfillment order to represent the work left to be done. The original fulfillment order will be marked as closed.

    This mutation works when the fulfillment order has a `SUBMITTED` or `CANCELLATION_REQUESTED` status. For `SUBMITTED` orders, cancellation happens immediately because the fulfillment service hasn't accepted the request.

    ---

    Note

    Orders that have had cancellation requested but the cancellation has yet to be accepted by the fulfillment service might still have work completed despite cancellation.

    **Note:**

    Orders that have had cancellation requested but the cancellation has yet to be accepted by the fulfillment service might still have work completed despite cancellation.

    **Note:** Orders that have had cancellation requested but the cancellation has yet to be accepted by the fulfillment service might still have work completed despite cancellation.

    ---

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderCancel.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order to mark as canceled.

    ---

[Anchor to fulfillmentOrderClose](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderClose)[fulfillmentOrderClose](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderClose) •mutation
:   Marks an in-progress fulfillment order as incomplete,
    indicating the fulfillment service is unable to ship any remaining items,
    and closes the fulfillment request.

    This mutation can only be called for fulfillment orders that meet the following criteria:

    * Assigned to a fulfillment service location,
    * The fulfillment request has been accepted,
    * The fulfillment order status is `IN_PROGRESS`.

    This mutation can only be called by the fulfillment service app that accepted the fulfillment request.
    Calling this mutation returns the control of the fulfillment order to the merchant, allowing them to
    move the fulfillment order line items to another location and fulfill from there,
    remove and refund the line items, or to request fulfillment from the same fulfillment service again.

    Closing a fulfillment order is explained in
    [the fulfillment service guide](https://shopify.dev/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-7-optional-close-a-fulfillment-order).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderClose.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order to mark as incomplete.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderClose.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for marking the fulfillment order as incomplete.

    ---

[Anchor to fulfillmentOrderHold](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderHold)[fulfillmentOrderHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderHold) •mutation
:   Applies a fulfillment hold on a fulfillment order.

    As of the
    [2025-01 API version](https://shopify.dev/changelog/apply-multiple-holds-to-a-single-fulfillment-order),
    the mutation can be successfully executed on fulfillment orders that are already on hold.
    To place multiple holds on a fulfillment order, apps need to supply the
    [handle](https://shopify.dev/api/admin-graphql/latest/objects/FulfillmentHold#field-handle)
    field. Each app can place up to
    10 active holds
    per fulfillment order. If an app attempts to place more than this, the mutation will return
    [a user error indicating that the limit has been reached](https://shopify.dev/api/admin-graphql/latest/enums/FulfillmentOrderHoldUserErrorCode#value-fulfillmentorderholdlimitreached).
    The app would need to release one of its existing holds before being able to apply a new one.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderHold.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order on which a fulfillment hold is applied.

    [Anchor to fulfillmentHold](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderHold.arguments.fulfillmentHold)fulfillmentHold •[FulfillmentOrderHoldInput!](/docs/api/admin-graphql/latest/input-objects/FulfillmentOrderHoldInput) required
    :   The details of the fulfillment hold applied on the fulfillment order.

        Show input fields

    ---

[Anchor to fulfillmentOrderMove](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderMove)[fulfillmentOrderMove](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderMove) •mutation
:   Changes the location which is assigned to fulfill a number of unfulfilled fulfillment order line items.

    Moving a fulfillment order will fail in the following circumstances:

    * The fulfillment order is closed.
    * The fulfillment order has had progress manually reported. To move a fulfillment order that has had progress manually reported, the fulfillment order must first be marked as open resolving the ongoing progress state.
    * The destination location doesn't stock the requested inventory item.
    * The API client doesn't have the correct permissions.

    Line items which have already been fulfilled can't be re-assigned
    and will always remain assigned to the original location.

    You can't change the assigned location while a fulfillment order has a
    [request status](https://shopify.dev/docs/api/admin-graphql/latest/enums/FulfillmentOrderRequestStatus)
    of `SUBMITTED`, `ACCEPTED`, `CANCELLATION_REQUESTED`, or `CANCELLATION_REJECTED`.
    These request statuses mean that a fulfillment order is awaiting action by a fulfillment service
    and can't be re-assigned without first having the fulfillment service accept a cancellation request.
    This behavior is intended to prevent items from being fulfilled by multiple locations or fulfillment services.

    ### How re-assigning line items affects fulfillment orders

    **First scenario:** Re-assign all line items belonging to a fulfillment order to a new location.

    In this case, the
    [assignedLocation](https://shopify.dev/docs/api/admin-graphql/latest/objects/fulfillmentorder#field-fulfillmentorder-assignedlocation)
    of the original fulfillment order will be updated to the new location.

    **Second scenario:** Re-assign a subset of the line items belonging to a fulfillment order to a new location.
    You can specify a subset of line items using the `fulfillmentOrderLineItems` parameter
    (available as of the `2023-04` API version),
    or specify that the original fulfillment order contains line items which have already been fulfilled.

    If the new location is already assigned to another active fulfillment order, on the same order, then
    a new fulfillment order is created. The existing fulfillment order is closed and line items are recreated
    in a new fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderMove.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order to be moved.

    [Anchor to newLocationId](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderMove.arguments.newLocationId)newLocationId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the location where the fulfillment order will be moved.

    [Anchor to fulfillmentOrderLineItems](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderMove.arguments.fulfillmentOrderLineItems)fulfillmentOrderLineItems •[[FulfillmentOrderLineItemInput!]](/docs/api/admin-graphql/latest/input-objects/FulfillmentOrderLineItemInput)
    :   The fulfillment order line items to be moved.
        If left blank, all unfulfilled line items belonging to the fulfillment order are moved.

        Show input fields

    ---

[Anchor to fulfillmentOrderOpen](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderOpen)[fulfillmentOrderOpen](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderOpen) •mutation
:   Marks a scheduled fulfillment order as open.

    From API version 2026-01, this will also mark a fulfillment order as open when it is assigned to a merchant managed location and has had progress reported.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderOpen.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order to mark as open.

    ---

[Anchor to fulfillmentOrderRejectCancellationRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectCancellationRequest)[fulfillmentOrderRejectCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectCancellationRequest) •mutation
:   Rejects a cancellation request sent to a fulfillment service for a fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectCancellationRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with the cancellation request.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectCancellationRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for rejecting the cancellation request.

    ---

[Anchor to fulfillmentOrderRejectFulfillmentRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectFulfillmentRequest)[fulfillmentOrderRejectFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectFulfillmentRequest) •mutation
:   Rejects a fulfillment request sent to a fulfillment service for a fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectFulfillmentRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with the fulfillment request.

    [Anchor to reason](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectFulfillmentRequest.arguments.reason)reason •[FulfillmentOrderRejectionReason](/docs/api/admin-graphql/latest/enums/FulfillmentOrderRejectionReason)
    :   The reason for the fulfillment order rejection.

        Show enum values

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectFulfillmentRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for rejecting the fulfillment request.

    [Anchor to lineItems](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderRejectFulfillmentRequest.arguments.lineItems)lineItems •[[IncomingRequestLineItemInput!]](/docs/api/admin-graphql/latest/input-objects/IncomingRequestLineItemInput)
    :   An optional array of line item rejection details. If none are provided, all line items will be assumed to be unfulfillable.

        **Note**: After the fulfillment request has been rejected, none of the line items will be able to be fulfilled. This field documents which line items specifically were unable to be fulfilled and why.

        Show input fields

    ---

[Anchor to fulfillmentOrderReleaseHold](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReleaseHold)[fulfillmentOrderReleaseHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold) •mutation
:   Releases the fulfillment hold on a fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReleaseHold.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order for which to release the fulfillment hold.

    [Anchor to holdIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReleaseHold.arguments.holdIds)holdIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   The IDs of the fulfillment holds to release.  
          
        Holds will only be released if they belong to the fulfillment order specified by the `id` argument.  
          
        **NOTE:** If not supplied, all holds for the fulfillment order will be released.
        It is highly recommended that apps supply the ids of the holds that they intend to release.
        Releasing all holds on a fulfillment order will result in the fulfillment order being released prematurely
        and items being incorrectly fulfilled.

    [Anchor to externalId](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReleaseHold.arguments.externalId)externalId •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A configurable ID used to track the automation system releasing this hold.

    ---

[Anchor to fulfillmentOrderReschedule](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReschedule)[fulfillmentOrderReschedule](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReschedule) •mutation
:   Reschedules a scheduled fulfillment order.

    Updates the value of the `fulfillAt` field on a scheduled fulfillment order.

    The fulfillment order will be marked as ready for fulfillment at this date and time.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReschedule.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order to reschedule.

    [Anchor to fulfillAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderReschedule.arguments.fulfillAt)fulfillAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) required
    :   A future date and time when the fulfillment order will be marked as ready for fulfillment.

    ---

[Anchor to fulfillmentOrdersReroute](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrdersReroute)[fulfillmentOrdersReroute](/docs/api/admin-graphql/latest/mutations/fulfillmentOrdersReroute) •mutation
:   Route the fulfillment orders to an alternative location, according to the shop's order routing settings. This involves:

    * Finding an alternate location that can fulfill the fulfillment orders.
    * Assigning the fulfillment orders to the new location.

    Show payload

    ### Arguments

    [Anchor to fulfillmentOrderIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrdersReroute.arguments.fulfillmentOrderIds)fulfillmentOrderIds •[[ID!]!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The list of IDs of the fulfillment orders.

    [Anchor to includedLocationIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrdersReroute.arguments.includedLocationIds)includedLocationIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   The list of IDs of the locations to include for rerouting. By default, all locations are included.

    [Anchor to excludedLocationIds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrdersReroute.arguments.excludedLocationIds)excludedLocationIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   The list of IDs of the locations to exclude for rerouting. Excluded locations specified here take precedence over included locations provided through included\_location\_ids.

    ---

[Anchor to fulfillmentOrderSubmitCancellationRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitCancellationRequest)[fulfillmentOrderSubmitCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitCancellationRequest) •mutation
:   Sends a cancellation request to the fulfillment service of a fulfillment order.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitCancellationRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with the cancellation request.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitCancellationRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional reason for the cancellation request.

    ---

[Anchor to fulfillmentOrderSubmitFulfillmentRequest](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitFulfillmentRequest)[fulfillmentOrderSubmitFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest) •mutation
:   Sends a fulfillment request to the fulfillment service assigned to a [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder). The fulfillment service must then accept or reject the request before processing can begin.

    You can either request fulfillment for all line items or specify individual items with quantities for partial fulfillment. When requesting partial fulfillment, Shopify splits the original fulfillment order into two: one with the submitted items and another with the remaining unsubmitted items. Include an optional message to communicate special instructions to the fulfillment service, such as gift wrapping or handling requirements.

    Learn more about [managing fulfillment requests as a fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-4-act-on-fulfillment-requests).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitFulfillmentRequest.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment order associated with fulfillment request.

    [Anchor to message](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitFulfillmentRequest.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional message for the fulfillment request.

    [Anchor to notifyCustomer](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitFulfillmentRequest.arguments.notifyCustomer)notifyCustomer •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)
    :   Whether the customer should be notified when fulfillments are created for this fulfillment order.

    [Anchor to fulfillmentOrderLineItems](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#mutation-fulfillmentOrderSubmitFulfillmentRequest.arguments.fulfillmentOrderLineItems)fulfillmentOrderLineItems •[[FulfillmentOrderLineItemInput!]](/docs/api/admin-graphql/latest/input-objects/FulfillmentOrderLineItemInput)
    :   The fulfillment order line items to be requested for fulfillment.
        If left blank, all line items of the fulfillment order are requested for fulfillment.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#interfaces)Interfaces

* Node

[Anchor to Node](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo