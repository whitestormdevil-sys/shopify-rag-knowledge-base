---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/PaymentTerms
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_payment_terms` access scope.

Payment conditions for an [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) or [`DraftOrder`](https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder), including when payment is due and how it's scheduled. Payment terms are created from templates that specify net terms (payment due after a certain number of days) or fixed schedules with specific due dates. You can optionally provide custom payment schedules using [`PaymentScheduleInput`](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/PaymentScheduleInput).

Each payment term contains one or more [`PaymentSchedule`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentSchedule), which you can access through the [`paymentSchedules`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules) field. Payment schedules contain detailed information for each payment installment.

Learn more about [payment terms](https://shopify.dev/docs/apps/build/checkout/payments/payment-terms).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/PaymentTerms#fields)Fields

* draftOrder (DraftOrder)
* due (Boolean!)
* dueInDays (Int)
* id (ID!)
* order (Order)
* overdue (Boolean!)
* paymentSchedules (PaymentScheduleConnection!)
* paymentTermsName (String!)
* paymentTermsType (PaymentTermsType!)
* translatedName (String!)

[Anchor to draftOrder](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.draftOrder)draftOrder •[DraftOrder](/docs/api/admin-graphql/latest/objects/DraftOrder)
:   The draft order associated with the payment terms.

    Show fields

[Anchor to due](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.due)due •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether payment terms have a payment schedule that's due.

[Anchor to dueInDays](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.dueInDays)dueInDays •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   Duration of payment terms in days based on the payment terms template used to create the payment terms.

[Anchor to id](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to order](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.order)order •[Order](/docs/api/admin-graphql/latest/objects/Order)
:   The order associated with the payment terms.

    Show fields

[Anchor to overdue](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.overdue)overdue •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the payment terms have overdue payment schedules.

[Anchor to paymentSchedules](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules)paymentSchedules •[PaymentScheduleConnection!](/docs/api/admin-graphql/latest/connections/PaymentScheduleConnection) non-null
:   List of schedules for the payment terms.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentSchedules.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to paymentTermsName](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentTermsName)paymentTermsName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The name of the payment terms template used to create the payment terms.

[Anchor to paymentTermsType](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.paymentTermsType)paymentTermsType •[PaymentTermsType!](/docs/api/admin-graphql/latest/enums/PaymentTermsType) non-null
:   The payment terms template type used to create the payment terms.

    Show enum values

[Anchor to translatedName](/docs/api/admin-graphql/latest/objects/PaymentTerms#field-PaymentTerms.fields.translatedName)translatedName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The payment terms name, translated into the shop admin's preferred language.

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutations)Mutations

* paymentTermsCreate (PaymentTermsCreatePayload)
* paymentTermsUpdate (PaymentTermsUpdatePayload)

[Anchor to paymentTermsCreate](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutation-paymentTermsCreate)[paymentTermsCreate](/docs/api/admin-graphql/latest/mutations/paymentTermsCreate) •mutation
:   Create payment terms on an order. To create payment terms on a draft order, use a draft order mutation and include the request with the `DraftOrderInput`.

    Show payload

    ### Arguments

    [Anchor to referenceId](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutation-paymentTermsCreate.arguments.referenceId)referenceId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   Specifies the reference orderId to add the payment terms for.

    [Anchor to paymentTermsAttributes](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutation-paymentTermsCreate.arguments.paymentTermsAttributes)paymentTermsAttributes •[PaymentTermsCreateInput!](/docs/api/admin-graphql/latest/input-objects/PaymentTermsCreateInput) required
    :   The attributes used to create the payment terms.

        Show input fields

    ---

[Anchor to paymentTermsUpdate](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutation-paymentTermsUpdate)[paymentTermsUpdate](/docs/api/admin-graphql/latest/mutations/paymentTermsUpdate) •mutation
:   Update payment terms on an order. To update payment terms on a draft order, use a draft order mutation and include the request with the `DraftOrderInput`.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/PaymentTerms#mutation-paymentTermsUpdate.arguments.input)input •[PaymentTermsUpdateInput!](/docs/api/admin-graphql/latest/input-objects/PaymentTermsUpdateInput) required
    :   The input fields used to update the payment terms.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/PaymentTerms#interfaces)Interfaces

* Node

[Anchor to Node](/docs/api/admin-graphql/latest/objects/PaymentTerms#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo