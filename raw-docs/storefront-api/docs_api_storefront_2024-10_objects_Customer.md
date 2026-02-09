---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Customer
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_read_customers` access scope.

A customer represents a customer account with the shop. Customer accounts store contact information for the customer, saving logged-in customers the trouble of having to provide it at every checkout.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Customer#fields)Fields

* acceptsMarketing (Boolean!)
* addresses (MailingAddressConnection!)
* avatarUrl (String)
* createdAt (DateTime!)
* defaultAddress (MailingAddress)
* displayName (String!)
* email (String)
* firstName (String)
* id (ID!)
* lastName (String)
* metafield (Metafield)
* metafields ([Metafield]!)
* numberOfOrders (UnsignedInt64!)
* orders (OrderConnection!)
* phone (String)
* socialLoginProvider (SocialLoginProvider)
* tags ([String!]!)
* updatedAt (DateTime!)

[Anchor to acceptsMarketing](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.acceptsMarketing)acceptsMarketing •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null Token access required
:   Indicates whether the customer has consented to be sent marketing material via email.

[Anchor to addresses](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses)addresses •[MailingAddressConnection!](/docs/api/storefront/latest/connections/MailingAddressConnection) non-null Token access required
:   A list of addresses for the customer.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.addresses.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to avatarUrl](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.avatarUrl)avatarUrl •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The URL of the customer's avatar image.

[Anchor to createdAt](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.createdAt)createdAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
:   The date and time when the customer was created.

[Anchor to defaultAddress](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.defaultAddress)defaultAddress •[MailingAddress](/docs/api/storefront/latest/objects/MailingAddress) Token access required
:   The customer’s default address.

    Show fields

[Anchor to displayName](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.displayName)displayName •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   The customer’s name, email or phone number.

[Anchor to email](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.email)email •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The customer’s email address.

[Anchor to firstName](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.firstName)firstName •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The customer’s first name.

[Anchor to id](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null Token access required
:   A unique ID for the customer.

[Anchor to lastName](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.lastName)lastName •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The customer’s last name.

[Anchor to metafield](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to numberOfOrders](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.numberOfOrders)numberOfOrders •[UnsignedInt64!](/docs/api/storefront/latest/scalars/UnsignedInt64) non-null Token access required
:   The number of orders that the customer has made at the store in their lifetime.

[Anchor to orders](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders)orders •[OrderConnection!](/docs/api/storefront/latest/connections/OrderConnection) non-null Token access required
:   The orders associated with the customer.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.sortKey)sortKey •[OrderSortKeys](/docs/api/storefront/latest/enums/OrderSortKeys) Default:ID
    :   Sort the underlying list by the given key.

        Show enum values

    [Anchor to query](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.orders.arguments.query)query •[String](/docs/api/storefront/latest/scalars/String)
    :   Apply one or multiple filters to the query.
        Refer to the detailed [search syntax](https://shopify.dev/api/usage/search-syntax) for more information about using filters.

        Show filters

        [Anchor to](/docs/api/storefront/latest/objects/Customer#argument-query-filter-processed_at) processed\_at •

    ---

[Anchor to phone](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.phone)phone •[String](/docs/api/storefront/latest/scalars/String) Token access required
:   The customer’s phone number.

[Anchor to socialLoginProvider](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.socialLoginProvider)socialLoginProvider •[SocialLoginProvider](/docs/api/storefront/latest/objects/SocialLoginProvider) Token access required
:   The social login provider associated with the customer.

    Show fields

[Anchor to tags](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.tags)tags •[[String!]!](/docs/api/storefront/latest/scalars/String) non-null Token access required
:   A comma separated list of tags that have been added to the customer.
    Additional access scope required: unauthenticated\_read\_customer\_tags.

[Anchor to updatedAt](/docs/api/storefront/latest/objects/Customer#field-Customer.fields.updatedAt)updatedAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
:   The date and time when the customer information was updated.

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/storefront/latest/objects/Customer#queries)Queries

* customer (Customer)

[Anchor to customer](/docs/api/storefront/latest/objects/Customer#query-customer)[customer](/docs/api/storefront/latest/queries/customer) •query
:   The customer associated with the given access token. Tokens are obtained by using the
    [`customerAccessTokenCreate` mutation](https://shopify.dev/docs/api/storefront/latest/mutations/customerAccessTokenCreate).

    Show fields

    ### Arguments

    [Anchor to customerAccessToken](/docs/api/storefront/latest/objects/Customer#query-customer.arguments.customerAccessToken)customerAccessToken •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The customer access token.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/storefront/latest/objects/Customer#mutations)Mutations

* customerActivate (CustomerActivatePayload)
* customerActivateByUrl (CustomerActivateByUrlPayload)
* customerCreate (CustomerCreatePayload)
* customerDefaultAddressUpdate (CustomerDefaultAddressUpdatePayload)
* customerReset (CustomerResetPayload)
* customerResetByUrl (CustomerResetByUrlPayload)
* customerUpdate (CustomerUpdatePayload)

[Anchor to customerActivate](/docs/api/storefront/latest/objects/Customer#mutation-customerActivate)[customerActivate](/docs/api/storefront/latest/mutations/customerActivate) •mutation
:   Activates a customer.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/storefront/latest/objects/Customer#mutation-customerActivate.arguments.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   Specifies the customer to activate.

    [Anchor to input](/docs/api/storefront/latest/objects/Customer#mutation-customerActivate.arguments.input)input •[CustomerActivateInput!](/docs/api/storefront/latest/input-objects/CustomerActivateInput) required
    :   The fields used to activate a customer.

        Show input fields

    ---

[Anchor to customerActivateByUrl](/docs/api/storefront/latest/objects/Customer#mutation-customerActivateByUrl)[customerActivateByUrl](/docs/api/storefront/latest/mutations/customerActivateByUrl) •mutation
:   Activates a customer with the activation url received from `customerCreate`.

    Show payload

    ### Arguments

    [Anchor to activationUrl](/docs/api/storefront/latest/objects/Customer#mutation-customerActivateByUrl.arguments.activationUrl)activationUrl •[URL!](/docs/api/storefront/latest/scalars/URL) required
    :   The customer activation URL.

    [Anchor to password](/docs/api/storefront/latest/objects/Customer#mutation-customerActivateByUrl.arguments.password)password •[String!](/docs/api/storefront/latest/scalars/String) required
    :   A new password set during activation.

    ---

[Anchor to customerCreate](/docs/api/storefront/latest/objects/Customer#mutation-customerCreate)[customerCreate](/docs/api/storefront/latest/mutations/customerCreate) •mutation
:   Creates a new customer.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/storefront/latest/objects/Customer#mutation-customerCreate.arguments.input)input •[CustomerCreateInput!](/docs/api/storefront/latest/input-objects/CustomerCreateInput) required
    :   The fields used to create a new customer.

        Show input fields

    ---

[Anchor to customerDefaultAddressUpdate](/docs/api/storefront/latest/objects/Customer#mutation-customerDefaultAddressUpdate)[customerDefaultAddressUpdate](/docs/api/storefront/latest/mutations/customerDefaultAddressUpdate) •mutation
:   Updates the default address of an existing customer.

    Show payload

    ### Arguments

    [Anchor to customerAccessToken](/docs/api/storefront/latest/objects/Customer#mutation-customerDefaultAddressUpdate.arguments.customerAccessToken)customerAccessToken •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The access token used to identify the customer.

    [Anchor to addressId](/docs/api/storefront/latest/objects/Customer#mutation-customerDefaultAddressUpdate.arguments.addressId)addressId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   ID of the address to set as the new default for the customer.

    ---

[Anchor to customerReset](/docs/api/storefront/latest/objects/Customer#mutation-customerReset)[customerReset](/docs/api/storefront/latest/mutations/customerReset) •mutation
:   "Resets a customer’s password with the token received from a reset password email. You can send a reset password email with the [`customerRecover`](https://shopify.dev/api/storefront/latest/mutations/customerRecover) mutation."

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/storefront/latest/objects/Customer#mutation-customerReset.arguments.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   Specifies the customer to reset.

    [Anchor to input](/docs/api/storefront/latest/objects/Customer#mutation-customerReset.arguments.input)input •[CustomerResetInput!](/docs/api/storefront/latest/input-objects/CustomerResetInput) required
    :   The fields used to reset a customer’s password.

        Show input fields

    ---

[Anchor to customerResetByUrl](/docs/api/storefront/latest/objects/Customer#mutation-customerResetByUrl)[customerResetByUrl](/docs/api/storefront/latest/mutations/customerResetByUrl) •mutation
:   "Resets a customer’s password with the reset password URL received from a reset password email. You can send a reset password email with the [`customerRecover`](https://shopify.dev/api/storefront/latest/mutations/customerRecover) mutation."

    Show payload

    ### Arguments

    [Anchor to resetUrl](/docs/api/storefront/latest/objects/Customer#mutation-customerResetByUrl.arguments.resetUrl)resetUrl •[URL!](/docs/api/storefront/latest/scalars/URL) required
    :   The customer's reset password url.

    [Anchor to password](/docs/api/storefront/latest/objects/Customer#mutation-customerResetByUrl.arguments.password)password •[String!](/docs/api/storefront/latest/scalars/String) required
    :   New password that will be set as part of the reset password process.

    ---

[Anchor to customerUpdate](/docs/api/storefront/latest/objects/Customer#mutation-customerUpdate)[customerUpdate](/docs/api/storefront/latest/mutations/customerUpdate) •mutation
:   Updates an existing customer.

    Show payload

    ### Arguments

    [Anchor to customerAccessToken](/docs/api/storefront/latest/objects/Customer#mutation-customerUpdate.arguments.customerAccessToken)customerAccessToken •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The access token used to identify the customer.

    [Anchor to customer](/docs/api/storefront/latest/objects/Customer#mutation-customerUpdate.arguments.customer)customer •[CustomerUpdateInput!](/docs/api/storefront/latest/input-objects/CustomerUpdateInput) required
    :   The customer object input.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/Customer#interfaces)Interfaces

* HasMetafields

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/Customer#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

---

Was this section helpful?

YesNo