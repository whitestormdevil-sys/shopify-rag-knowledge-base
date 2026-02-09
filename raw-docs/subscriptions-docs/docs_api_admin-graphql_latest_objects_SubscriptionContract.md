---
source: https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionContract
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires the `read_own_subscription_contracts` or `write_own_subscription_contracts` scope.

A subscription contract that defines recurring purchases for a customer. Each contract specifies what products to deliver, when to bill and ship them, and at what price.

The contract includes [`SubscriptionBillingPolicy`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionBillingPolicy) and [`SubscriptionDeliveryPolicy`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionDeliveryPolicy) that control the frequency of charges and fulfillments. [`SubscriptionLine`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionLine) items define the products, quantities, and pricing for each recurring [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order). The contract tracks [`SubscriptionBillingAttempt`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionBillingAttempt) records, payment status, and generated orders throughout its lifecycle. [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) instances manage contracts through various status transitions including active, paused, failed, cancelled, or expired states.

Learn more about [building subscription contracts](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract) and [updating subscription contracts](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/SubscriptionContract#fields)Fields

* app (App)
* appAdminUrl (URL)
* billingAttempts (SubscriptionBillingAttemptConnection!)
* billingPolicy (SubscriptionBillingPolicy!)
* createdAt (DateTime!)
* currencyCode (CurrencyCode!)
* customAttributes ([Attribute!]!)
* customer (Customer)
* customerPaymentMethod (CustomerPaymentMethod)
* deliveryMethod (SubscriptionDeliveryMethod)
* deliveryPolicy (SubscriptionDeliveryPolicy!)
* deliveryPrice (MoneyV2!)
* discounts (SubscriptionManualDiscountConnection!)
* id (ID!)
* lastBillingAttemptErrorType (SubscriptionContractLastBillingErrorType)
* lastPaymentStatus (SubscriptionContractLastPaymentStatus)
* lines (SubscriptionLineConnection!)
* linesCount (Count)
* nextBillingDate (DateTime)
* note (String)
* orders (OrderConnection!)
* originOrder (Order)
* revisionId (UnsignedInt64!)
* status (SubscriptionContractSubscriptionStatus!)
* updatedAt (DateTime!)
* lineCount (Int!): deprecated

[Anchor to app](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.app)app •[App](/docs/api/admin-graphql/latest/objects/App)
:   The subscription app that the subscription contract is registered to.

    Show fields

[Anchor to appAdminUrl](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.appAdminUrl)appAdminUrl •[URL](/docs/api/admin-graphql/latest/scalars/URL)
:   The URL of the subscription contract page on the subscription app.

[Anchor to billingAttempts](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts)billingAttempts •[SubscriptionBillingAttemptConnection!](/docs/api/admin-graphql/latest/connections/SubscriptionBillingAttemptConnection) non-null
:   The list of billing attempts associated with the subscription contract.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingAttempts.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to billingPolicy](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.billingPolicy)billingPolicy •[SubscriptionBillingPolicy!](/docs/api/admin-graphql/latest/objects/SubscriptionBillingPolicy) non-null
:   The billing policy associated with the subscription contract.

    Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the subscription contract was created.

[Anchor to currencyCode](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.currencyCode)currencyCode •[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode) non-null
:   The currency that's used for the subscription contract.

    Show enum values

[Anchor to customAttributes](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.customAttributes)customAttributes •[[Attribute!]!](/docs/api/admin-graphql/latest/objects/Attribute) non-null
:   A list of the custom attributes to be added to the generated orders.

    Show fields

[Anchor to customer](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.customer)customer •[Customer](/docs/api/admin-graphql/latest/objects/Customer)
:   The customer to whom the subscription contract belongs.

    Show fields

[Anchor to customerPaymentMethod](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.customerPaymentMethod)customerPaymentMethod •[CustomerPaymentMethod](/docs/api/admin-graphql/latest/objects/CustomerPaymentMethod)
:   The customer payment method that's used for the subscription contract.

    Show fields

    ### Arguments

    [Anchor to showRevoked](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.customerPaymentMethod.arguments.showRevoked)showRevoked •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to show the customer's revoked payment method.

    ---

[Anchor to deliveryMethod](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.deliveryMethod)deliveryMethod •[SubscriptionDeliveryMethod](/docs/api/admin-graphql/latest/unions/SubscriptionDeliveryMethod)
:   The delivery method for each billing of the subscription contract.

    Show union types

[Anchor to deliveryPolicy](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.deliveryPolicy)deliveryPolicy •[SubscriptionDeliveryPolicy!](/docs/api/admin-graphql/latest/objects/SubscriptionDeliveryPolicy) non-null
:   The delivery policy associated with the subscription contract.

    Show fields

[Anchor to deliveryPrice](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.deliveryPrice)deliveryPrice •[MoneyV2!](/docs/api/admin-graphql/latest/objects/MoneyV2) non-null
:   The delivery price for each billing of the subscription contract.

    Show fields

[Anchor to discounts](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts)discounts •[SubscriptionManualDiscountConnection!](/docs/api/admin-graphql/latest/connections/SubscriptionManualDiscountConnection) non-null
:   The list of subscription discounts associated with the subscription contract.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.discounts.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to id](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to lastBillingAttemptErrorType](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lastBillingAttemptErrorType)lastBillingAttemptErrorType •[SubscriptionContractLastBillingErrorType](/docs/api/admin-graphql/latest/enums/SubscriptionContractLastBillingErrorType)
:   The last billing error type of the contract.

    Show enum values

[Anchor to lastPaymentStatus](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lastPaymentStatus)lastPaymentStatus •[SubscriptionContractLastPaymentStatus](/docs/api/admin-graphql/latest/enums/SubscriptionContractLastPaymentStatus)
:   The current status of the last payment.

    Show enum values

[Anchor to lines](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines)lines •[SubscriptionLineConnection!](/docs/api/admin-graphql/latest/connections/SubscriptionLineConnection) non-null
:   The list of subscription lines associated with the subscription contract.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lines.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to linesCount](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.linesCount)linesCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   The number of lines associated with the subscription contract.

    Show fields

[Anchor to nextBillingDate](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.nextBillingDate)nextBillingDate •[DateTime](/docs/api/admin-graphql/latest/scalars/DateTime)
:   The next billing date for the subscription contract. This field is managed by the apps.
    Alternatively you can utilize our
    [Billing Cycles APIs](https://shopify.dev/docs/apps/selling-strategies/subscriptions/billing-cycles),
    which provide auto-computed billing dates and additional functionalities.

[Anchor to note](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.note)note •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The note field that will be applied to the generated orders.

[Anchor to orders](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders)orders •[OrderConnection!](/docs/api/admin-graphql/latest/connections/OrderConnection) non-null
:   A list of the subscription contract's orders.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.orders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to originOrder](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.originOrder)originOrder •[Order](/docs/api/admin-graphql/latest/objects/Order)
:   The order from which this contract originated.

    Show fields

[Anchor to revisionId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.revisionId)revisionId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The revision id of the contract.

[Anchor to status](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.status)status •[SubscriptionContractSubscriptionStatus!](/docs/api/admin-graphql/latest/enums/SubscriptionContractSubscriptionStatus) non-null
:   The current status of the subscription contract.

    Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the subscription contract was updated.

[Anchor to lineCount](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-SubscriptionContract.fields.lineCount)lineCount •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-nullDeprecated

---

Was this section helpful?

YesNo

### Fields and connections with this object

* {}[Customer.subscriptionContracts](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.subscriptionContracts)
* {}[CustomerPaymentMethod.subscriptionContracts](/docs/api/admin-graphql/latest/objects/CustomerPaymentMethod#field-CustomerPaymentMethod.fields.subscriptionContracts)
* {}[LineItem.contract](/docs/api/admin-graphql/latest/objects/LineItem#field-LineItem.fields.contract)
* {}[SubscriptionBillingAttempt.subscriptionContract](/docs/api/admin-graphql/latest/objects/SubscriptionBillingAttempt#field-SubscriptionBillingAttempt.fields.subscriptionContract)
* {}[SubscriptionBillingCycle.sourceContract](/docs/api/admin-graphql/latest/objects/SubscriptionBillingCycle#field-SubscriptionBillingCycle.fields.sourceContract)
* <->[SubscriptionContractConnection.nodes](/docs/api/admin-graphql/latest/connections/SubscriptionContractConnection#returns-nodes)
* {}[SubscriptionContractEdge.node](/docs/api/admin-graphql/latest/objects/SubscriptionContractEdge#field-SubscriptionContractEdge.fields.node)
* {}[SubscriptionDraft.originalContract](/docs/api/admin-graphql/latest/objects/SubscriptionDraft#field-SubscriptionDraft.fields.originalContract)
* {}[SubscriptionLine.concatenatedOriginContract](/docs/api/admin-graphql/latest/objects/SubscriptionLine#field-SubscriptionLine.fields.concatenatedOriginContract)

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/SubscriptionContract#queries)Queries

* subscriptionContract (SubscriptionContract)
* subscriptionContracts (SubscriptionContractConnection!)

[Anchor to subscriptionContract](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContract)[subscriptionContract](/docs/api/admin-graphql/latest/queries/subscriptionContract) •query
:   Retrieves a [`SubscriptionContract`](https://shopify.dev/docs/api/customer/latest/objects/SubscriptionContract) by ID.

    The contract tracks the subscription's lifecycle through various [statuses](https://shopify.dev/docs/api/admin-graphql/latest/queries/subscriptionContract#returns-SubscriptionContract.fields.status), and links to related billing attempts, generated [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) objects, and the customer's [`CustomerPaymentMethod`](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerPaymentMethod).

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContract.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract to return.

    ---

[Anchor to subscriptionContracts](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts)[subscriptionContracts](/docs/api/admin-graphql/latest/queries/subscriptionContracts) •query
:   Returns a [`SubscriptionContractConnection`](https://shopify.dev/docs/api/admin-graphql/latest/objects/SubscriptionContractConnection) containing [subscription contracts](https://shopify.dev/docs/api/customer/latest/objects/SubscriptionContract). Subscription contracts are agreements between [customers](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer) and merchants for recurring purchases with defined billing and delivery schedules.

    Filter results with the [`query`](https://shopify.dev/docs/api/admin-graphql/latest/queries/subscriptionContracts#arguments-query) argument. You can paginate results using standard [cursor-based pagination](https://shopify.dev/docs/api/usage/pagination-graphql).

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.sortKey)sortKey •[SubscriptionContractsSortKeys](/docs/api/admin-graphql/latest/enums/SubscriptionContractsSortKeys) Default:CREATED\_AT
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/SubscriptionContract#query-subscriptionContracts.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/SubscriptionContract#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/SubscriptionContract#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/SubscriptionContract#argument-query-filter-last_billing_attempt_error_type) last\_billing\_attempt\_error\_type •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/SubscriptionContract#argument-query-filter-status) status •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/SubscriptionContract#argument-query-filter-updated_at) updated\_at •time

    ---

---

Was this section helpful?

YesNo

### Queried by

* <?>[subscriptionContract](/docs/api/admin-graphql/latest/queries/subscriptionContract)
* <?>[subscriptionContracts](/docs/api/admin-graphql/latest/queries/subscriptionContracts)

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutations)Mutations

* subscriptionContractActivate (SubscriptionContractActivatePayload)
* subscriptionContractAtomicCreate (SubscriptionContractAtomicCreatePayload)
* subscriptionContractCancel (SubscriptionContractCancelPayload)
* subscriptionContractExpire (SubscriptionContractExpirePayload)
* subscriptionContractFail (SubscriptionContractFailPayload)
* subscriptionContractPause (SubscriptionContractPausePayload)
* subscriptionContractProductChange (SubscriptionContractProductChangePayload)
* subscriptionContractSetNextBillingDate (SubscriptionContractSetNextBillingDatePayload)
* subscriptionDraftCommit (SubscriptionDraftCommitPayload)

[Anchor to subscriptionContractActivate](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractActivate)[subscriptionContractActivate](/docs/api/admin-graphql/latest/mutations/subscriptionContractActivate) •mutation
:   Activates a Subscription Contract. Contract status must be either active, paused, or failed.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractActivate.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract.

    ---

[Anchor to subscriptionContractAtomicCreate](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractAtomicCreate)[subscriptionContractAtomicCreate](/docs/api/admin-graphql/latest/mutations/subscriptionContractAtomicCreate) •mutation
:   Creates a Subscription Contract.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractAtomicCreate.arguments.input)input •[SubscriptionContractAtomicCreateInput!](/docs/api/admin-graphql/latest/input-objects/SubscriptionContractAtomicCreateInput) required
    :   The properties of the new Subscription Contract.

        Show input fields

    ---

[Anchor to subscriptionContractCancel](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractCancel)[subscriptionContractCancel](/docs/api/admin-graphql/latest/mutations/subscriptionContractCancel) •mutation
:   Cancels a Subscription Contract.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractCancel.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract.

    ---

[Anchor to subscriptionContractExpire](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractExpire)[subscriptionContractExpire](/docs/api/admin-graphql/latest/mutations/subscriptionContractExpire) •mutation
:   Expires a Subscription Contract.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractExpire.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract.

    ---

[Anchor to subscriptionContractFail](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractFail)[subscriptionContractFail](/docs/api/admin-graphql/latest/mutations/subscriptionContractFail) •mutation
:   Fails a Subscription Contract.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractFail.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract.

    ---

[Anchor to subscriptionContractPause](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractPause)[subscriptionContractPause](/docs/api/admin-graphql/latest/mutations/subscriptionContractPause) •mutation
:   Pauses a Subscription Contract.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractPause.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the Subscription Contract.

    ---

[Anchor to subscriptionContractProductChange](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractProductChange)[subscriptionContractProductChange](/docs/api/admin-graphql/latest/mutations/subscriptionContractProductChange) •mutation
:   Allows for the easy change of a Product in a Contract or a Product price change.

    Show payload

    ### Arguments

    [Anchor to subscriptionContractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractProductChange.arguments.subscriptionContractId)subscriptionContractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the subscription contract.

    [Anchor to lineId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractProductChange.arguments.lineId)lineId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The gid of the Subscription Line to update.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractProductChange.arguments.input)input •[SubscriptionContractProductChangeInput!](/docs/api/admin-graphql/latest/input-objects/SubscriptionContractProductChangeInput) required
    :   The properties of the Product changes.

        Show input fields

    ---

[Anchor to subscriptionContractSetNextBillingDate](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractSetNextBillingDate)[subscriptionContractSetNextBillingDate](/docs/api/admin-graphql/latest/mutations/subscriptionContractSetNextBillingDate) •mutation
:   Sets the next billing date of a Subscription Contract. This field is managed by the apps.
    Alternatively you can utilize our
    [Billing Cycles APIs](https://shopify.dev/docs/apps/selling-strategies/subscriptions/billing-cycles),
    which provide auto-computed billing dates and additional functionalities.

    Show payload

    ### Arguments

    [Anchor to contractId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractSetNextBillingDate.arguments.contractId)contractId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The gid of the Subscription Contract to set the next billing date for.

    [Anchor to date](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionContractSetNextBillingDate.arguments.date)date •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) required
    :   The next billing date.

    ---

[Anchor to subscriptionDraftCommit](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionDraftCommit)[subscriptionDraftCommit](/docs/api/admin-graphql/latest/mutations/subscriptionDraftCommit) •mutation
:   Commits the updates of a Subscription Contract draft.

    Show payload

    ### Arguments

    [Anchor to draftId](/docs/api/admin-graphql/latest/objects/SubscriptionContract#mutation-subscriptionDraftCommit.arguments.draftId)draftId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The gid of the Subscription Contract draft to commit.

    ---

---

Was this section helpful?

YesNo

### Mutated by

* <~>[subscriptionContractActivate](/docs/api/admin-graphql/latest/mutations/subscriptionContractActivate)
* <~>[subscriptionContractAtomicCreate](/docs/api/admin-graphql/latest/mutations/subscriptionContractAtomicCreate)
* <~>[subscriptionContractCancel](/docs/api/admin-graphql/latest/mutations/subscriptionContractCancel)
* <~>[subscriptionContractExpire](/docs/api/admin-graphql/latest/mutations/subscriptionContractExpire)
* <~>[subscriptionContractFail](/docs/api/admin-graphql/latest/mutations/subscriptionContractFail)
* <~>[subscriptionContractPause](/docs/api/admin-graphql/latest/mutations/subscriptionContractPause)
* <~>[subscriptionContractProductChange](/docs/api/admin-graphql/latest/mutations/subscriptionContractProductChange)
* <~>[subscriptionContractSetNextBillingDate](/docs/api/admin-graphql/latest/mutations/subscriptionContractSetNextBillingDate)
* <~>[subscriptionDraftCommit](/docs/api/admin-graphql/latest/mutations/subscriptionDraftCommit)

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/SubscriptionContract#interfaces)Interfaces

* Node
* SubscriptionContractBase

[Anchor to Node](/docs/api/admin-graphql/latest/objects/SubscriptionContract#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

[Anchor to SubscriptionContractBase](/docs/api/admin-graphql/latest/objects/SubscriptionContract#interface-SubscriptionContractBase)[SubscriptionContractBase](/docs/api/admin-graphql/latest/interfaces/SubscriptionContractBase) •interface

---

Was this section helpful?

YesNo

### Implements

* ||-[Node](/docs/api/admin-graphql/latest/interfaces/Node)
* ||-[SubscriptionContractBase](/docs/api/admin-graphql/latest/interfaces/SubscriptionContractBase)