---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Fulfillment
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_orders` access scope, `read_marketplace_orders` access scope, `read_assigned_fulfillment_orders` access scope, `read_merchant_managed_fulfillment_orders` access scope, `read_third_party_fulfillment_orders` access scope or `read_marketplace_fulfillment_orders` access scope.

A shipment of one or more items from an [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order). Tracks which [`LineItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem) objects ship, their quantities, and the shipment's tracking information.

Includes tracking details such as the carrier, tracking numbers, and URLs. The fulfillment connects to both the original order and any associated [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) objects. [`FulfillmentEvent`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentEvent) objects record milestones throughout the shipment lifecycle, from creation through delivery.

Multiple fulfillments can exist for a single order when items either ship separately or from different locations.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Fulfillment#fields)Fields

* createdAt (DateTime!)
* deliveredAt (DateTime)
* displayStatus (FulfillmentDisplayStatus)
* estimatedDeliveryAt (DateTime)
* events (FulfillmentEventConnection!)
* fulfillmentLineItems (FulfillmentLineItemConnection!)
* fulfillmentOrders (FulfillmentOrderConnection!)
* id (ID!)
* inTransitAt (DateTime)
* legacyResourceId (UnsignedInt64!)
* location (Location)
* name (String!)
* order (Order!)
* originAddress (FulfillmentOriginAddress)
* requiresShipping (Boolean!)
* service (FulfillmentService)
* status (FulfillmentStatus!)
* totalQuantity (Int!)
* trackingInfo ([FulfillmentTrackingInfo!]!)
* updatedAt (DateTime!)

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the fulfillment was created.

[Anchor to deliveredAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.deliveredAt)deliveredAt •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The date that this fulfillment was delivered.

[Anchor to displayStatus](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.displayStatus)displayStatus •[FulfillmentDisplayStatus](/docs/api/admin-graphql/latest/enums/FulfillmentDisplayStatus)
:   Human readable display status for this fulfillment.

    Show enum values

[Anchor to estimatedDeliveryAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.estimatedDeliveryAt)estimatedDeliveryAt •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The estimated date that this fulfillment will arrive.

[Anchor to events](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events)events •[FulfillmentEventConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentEventConnection) non-null
:   The history of events associated with this fulfillment.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.events.arguments.sortKey)sortKey •[FulfillmentEventSortKeys](/docs/api/admin-graphql/latest/enums/FulfillmentEventSortKeys) Default:HAPPENED\_AT
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    ---

[Anchor to fulfillmentLineItems](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems)fulfillmentLineItems •[FulfillmentLineItemConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentLineItemConnection) non-null
:   List of the fulfillment's line items.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentLineItems.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to fulfillmentOrders](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders)fulfillmentOrders •[FulfillmentOrderConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderConnection) non-null
:   A paginated list of fulfillment orders for the fulfillment.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.fulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to inTransitAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.inTransitAt)inTransitAt •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The date and time when the fulfillment went into transit.

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to location](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.location)location •[Location](/docs/api/admin-graphql/latest/objects/Location)
:   The location that the fulfillment was processed at.

    Show fields

[Anchor to name](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.name)name •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   Human readable reference identifier for this fulfillment.

[Anchor to order](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.order)order •[Order!](/docs/api/admin-graphql/latest/objects/Order) non-null
:   The order for which the fulfillment was created.

    Show fields

[Anchor to originAddress](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.originAddress)originAddress •[FulfillmentOriginAddress](/docs/api/admin-graphql/latest/objects/FulfillmentOriginAddress)
:   The address at which the fulfillment occurred. This field is intended for tax purposes, as a full address is required for tax providers to accurately calculate taxes. Typically this is the address of the warehouse or fulfillment center. To retrieve a fulfillment location's address, use the `assignedLocation` field on the [`FulfillmentOrder`](/docs/api/admin-graphql/latest/objects/FulfillmentOrder) object instead.

    Show fields

[Anchor to requiresShipping](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.requiresShipping)requiresShipping •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether any of the line items in the fulfillment require shipping.

[Anchor to service](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.service)service •[FulfillmentService](/docs/api/admin-graphql/latest/objects/FulfillmentService)
:   Fulfillment service associated with the fulfillment.

    Show fields

[Anchor to status](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.status)status •[FulfillmentStatus!](/docs/api/admin-graphql/latest/enums/FulfillmentStatus) non-null
:   The status of the fulfillment.

    Show enum values

[Anchor to totalQuantity](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.totalQuantity)totalQuantity •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-null
:   Sum of all line item quantities for the fulfillment.

[Anchor to trackingInfo](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.trackingInfo)trackingInfo •[[FulfillmentTrackingInfo!]!](/docs/api/admin-graphql/latest/objects/FulfillmentTrackingInfo) non-null
:   Tracking information associated with the fulfillment,
    such as the tracking company, tracking number, and tracking URL.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.trackingInfo.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   Truncate the array result to this size.

    ---

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the fulfillment was last modified.

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/Fulfillment#queries)Queries

* fulfillment (Fulfillment)

[Anchor to fulfillment](/docs/api/admin-graphql/latest/objects/Fulfillment#query-fulfillment)[fulfillment](/docs/api/admin-graphql/latest/queries/fulfillment) •query
:   Retrieves a [`Fulfillment`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Fulfillment) by its ID. A fulfillment is a record that the merchant has completed their work required for one or more line items in an [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order). It includes tracking information, [`LineItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/LineItem) objects, and the status of the fulfillment.

    Use this query to track the progress of shipped items, view tracking details, or check [fulfillment events](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentEvent) for example when a package is out for delivery or delivered.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Fulfillment#query-fulfillment.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Fulfillment to return.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/Fulfillment#mutations)Mutations

* fulfillmentCancel (FulfillmentCancelPayload)
* fulfillmentCreate (FulfillmentCreatePayload)
* fulfillmentTrackingInfoUpdate (FulfillmentTrackingInfoUpdatePayload)

[Anchor to fulfillmentCancel](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCancel)[fulfillmentCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentCancel) •mutation
:   Cancels an existing [`Fulfillment`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Fulfillment) and reverses its effects on associated [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) objects. When you cancel a fulfillment, the system creates new fulfillment orders for the cancelled items so they can be fulfilled again.

    The cancellation affects fulfillment orders differently based on their fulfillment status. If a fulfillment order was entirely fulfilled, then it automatically closes. If a fulfillment order is partially fulfilled, then the remaining quantities adjust to include the cancelled items. The system creates new fulfillment orders at the original [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) when items are still stocked there, or at alternative locations based on the store's fulfillment priority settings.

    Learn more about [canceling fulfillments](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-7-cancel-a-fulfillment).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCancel.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment to be canceled.

    ---

[Anchor to fulfillmentCreate](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreate)[fulfillmentCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentCreate) •mutation
:   Creates a fulfillment for one or more [`FulfillmentOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) objects. The fulfillment orders are associated with the same [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) and are assigned to the same [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location).

    Use this mutation to mark items as fulfilled when they're ready to ship. You can specify tracking information, customer notification preferences, and which [`FulfillmentOrderLineItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/fulfillmentorderlineitem) objects to fulfill from each fulfillment order. If you don't specify line items, then the mutation fulfills all items in the fulfillment order.

    Learn more about [building fulfillment solutions](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/build-fulfillment-solutions#create-a-fulfillment).

    Show payload

    ### Arguments

    [Anchor to fulfillment](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreate.arguments.fulfillment)fulfillment •[FulfillmentInput!](/docs/api/admin-graphql/latest/input-objects/FulfillmentInput) required
    :   The input fields used to create a fulfillment from fulfillment orders.

        Show input fields

    [Anchor to message](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreate.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional message for the fulfillment request.

    ---

[Anchor to fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdate)[fulfillmentTrackingInfoUpdate](/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate) •mutation
:   Updates tracking information for a fulfillment, including the carrier name, tracking numbers, and tracking URLs. You can provide either single or multiple tracking numbers for shipments with multiple packages.

    The mutation accepts a [`FulfillmentTrackingInput`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/FulfillmentTrackingInput) that supports both single tracking (using [`number`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate#arguments-trackingInfoInput.fields.number) and [`url`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate#arguments-trackingInfoInput.fields.url) fields) and multi-package tracking (using [`numbers`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate#arguments-trackingInfoInput.fields.numbers) and [`urls`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate#arguments-trackingInfoInput.fields.urls) fields). When you specify a [supported carrier name](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentTrackingInfo#supported-tracking-companies), Shopify automatically generates tracking URLs for the provided tracking numbers.

    You can optionally notify customers about tracking updates with the [`notifyCustomer`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdate#arguments-notifyCustomer) argument. When enabled, customers receive shipping update emails with tracking details and receive notifications about future updates to the fulfillment.

    Learn more about [enabling tracking support](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-9-optional-enable-tracking-support) for fulfillment services.

    Show payload

    ### Arguments

    [Anchor to fulfillmentId](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdate.arguments.fulfillmentId)fulfillmentId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment.

    [Anchor to trackingInfoInput](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdate.arguments.trackingInfoInput)trackingInfoInput •[FulfillmentTrackingInput!](/docs/api/admin-graphql/latest/input-objects/FulfillmentTrackingInput) required
    :   The tracking input for the mutation, including tracking URL, number, and company.

        Show input fields

    [Anchor to notifyCustomer](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdate.arguments.notifyCustomer)notifyCustomer •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)
    :   Whether the customer will be notified of this update and future updates for the fulfillment.
        If this field is left blank, then notifications won't be sent to the customer when the fulfillment is updated.

    ---

### Deprecated mutations

* fulfillmentCreateV2 (FulfillmentCreateV2Payload): deprecated
* fulfillmentTrackingInfoUpdateV2 (FulfillmentTrackingInfoUpdateV2Payload): deprecated

[Anchor to fulfillmentCreateV2](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreateV2)[fulfillmentCreateV2](/docs/api/admin-graphql/latest/mutations/fulfillmentCreateV2) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to fulfillment](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreateV2.arguments.fulfillment)fulfillment •[FulfillmentV2Input!](/docs/api/admin-graphql/latest/input-objects/FulfillmentV2Input) required
    :   The input fields used to create a fulfillment from fulfillment orders.

        Show input fields

    [Anchor to message](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentCreateV2.arguments.message)message •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   An optional message for the fulfillment request.

    ---

[Anchor to fulfillmentTrackingInfoUpdateV2](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdateV2)[fulfillmentTrackingInfoUpdateV2](/docs/api/admin-graphql/latest/mutations/fulfillmentTrackingInfoUpdateV2) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to fulfillmentId](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdateV2.arguments.fulfillmentId)fulfillmentId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the fulfillment.

    [Anchor to trackingInfoInput](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdateV2.arguments.trackingInfoInput)trackingInfoInput •[FulfillmentTrackingInput!](/docs/api/admin-graphql/latest/input-objects/FulfillmentTrackingInput) required
    :   The tracking input for the mutation, including tracking URL, number, and company.

        Show input fields

    [Anchor to notifyCustomer](/docs/api/admin-graphql/latest/objects/Fulfillment#mutation-fulfillmentTrackingInfoUpdateV2.arguments.notifyCustomer)notifyCustomer •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean)
    :   Whether the customer will be notified of this update and future updates for the fulfillment.
        If this field is left blank, then notifications won't be sent to the customer when the fulfillment is updated.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Fulfillment#interfaces)Interfaces

* LegacyInteroperability
* Node

[Anchor to LegacyInteroperability](/docs/api/admin-graphql/latest/objects/Fulfillment#interface-LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Fulfillment#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo