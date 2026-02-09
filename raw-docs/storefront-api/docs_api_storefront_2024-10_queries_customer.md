---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/customer
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

The customer associated with the given access token. Tokens are obtained by using the
[`customerAccessTokenCreate` mutation](https://shopify.dev/docs/api/storefront/latest/mutations/customerAccessTokenCreate).

* customerAccessToken (String!)

[Anchor to customerAccessToken](/docs/api/storefront/latest/queries/customer#arguments-customerAccessToken)customerAccessToken •[String!](/docs/api/storefront/latest/scalars/String) required
:   The customer access token.

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/customer#possible-returns)Possible returns

* Customer (Customer)

[Anchor to Customer](/docs/api/storefront/latest/queries/customer#returns-Customer)Customer •[Customer](/docs/api/storefront/latest/objects/Customer)
:   A customer represents a customer account with the shop. Customer accounts store contact information for the customer, saving logged-in customers the trouble of having to provide it at every checkout.

    Show fields

    [Anchor to acceptsMarketing](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.acceptsMarketing)acceptsMarketing •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null Token access required
    :   Indicates whether the customer has consented to be sent marketing material via email.

    [Anchor to addresses](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses)addresses •[MailingAddressConnection!](/docs/api/storefront/latest/connections/MailingAddressConnection) non-null Token access required
    :   A list of addresses for the customer.

        Show fields

        ### Arguments

        [Anchor to first](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
        :   Returns up to the first `n` elements from the list.

        [Anchor to after](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
        :   Returns the elements that come after the specified cursor.

        [Anchor to last](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
        :   Returns up to the last `n` elements from the list.

        [Anchor to before](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
        :   Returns the elements that come before the specified cursor.

        [Anchor to reverse](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.addresses.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
        :   Reverse the order of the underlying list.

        ---

    [Anchor to avatarUrl](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.avatarUrl)avatarUrl •[String](/docs/api/storefront/latest/scalars/String) Token access required
    :   The URL of the customer's avatar image.

    [Anchor to createdAt](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.createdAt)createdAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
    :   The date and time when the customer was created.

    [Anchor to defaultAddress](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.defaultAddress)defaultAddress •[MailingAddress](/docs/api/storefront/latest/objects/MailingAddress) Token access required
    :   The customer’s default address.

        Show fields

    [Anchor to displayName](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.displayName)displayName •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
    :   The customer’s name, email or phone number.

    [Anchor to email](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.email)email •[String](/docs/api/storefront/latest/scalars/String) Token access required
    :   The customer’s email address.

    [Anchor to firstName](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.firstName)firstName •[String](/docs/api/storefront/latest/scalars/String) Token access required
    :   The customer’s first name.

    [Anchor to id](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null Token access required
    :   A unique ID for the customer.

    [Anchor to lastName](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.lastName)lastName •[String](/docs/api/storefront/latest/scalars/String) Token access required
    :   The customer’s last name.

    [Anchor to metafield](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

        Show fields

        ### Arguments

        [Anchor to namespace](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
        :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

        [Anchor to key](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
        :   The identifier for the metafield.

        ---

    [Anchor to metafields](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
    :   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

        Show fields

        ### Arguments

        [Anchor to identifiers](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
        :   The list of metafields to retrieve by namespace and key.

            The input must not contain more than `250` values.

            Show input fields

        ---

    [Anchor to numberOfOrders](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.numberOfOrders)numberOfOrders •[UnsignedInt64!](/docs/api/storefront/latest/scalars/UnsignedInt64) non-null Token access required
    :   The number of orders that the customer has made at the store in their lifetime.

    [Anchor to orders](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders)orders •[OrderConnection!](/docs/api/storefront/latest/connections/OrderConnection) non-null Token access required
    :   The orders associated with the customer.

        Show fields

        ### Arguments

        [Anchor to first](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
        :   Returns up to the first `n` elements from the list.

        [Anchor to after](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
        :   Returns the elements that come after the specified cursor.

        [Anchor to last](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
        :   Returns up to the last `n` elements from the list.

        [Anchor to before](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
        :   Returns the elements that come before the specified cursor.

        [Anchor to reverse](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
        :   Reverse the order of the underlying list.

        [Anchor to sortKey](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.sortKey)sortKey •[OrderSortKeys](/docs/api/storefront/latest/enums/OrderSortKeys) Default:ID
        :   Sort the underlying list by the given key.

            Show enum values

        [Anchor to query](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.orders.arguments.query)query •[String](/docs/api/storefront/latest/scalars/String)
        :   Apply one or multiple filters to the query.
            Refer to the detailed [search syntax](https://shopify.dev/api/usage/search-syntax) for more information about using filters.

            Show filters

            [Anchor to](/docs/api/storefront/latest/queries/customer#argument-query-filter-processed_at) processed\_at •

        ---

    [Anchor to phone](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.phone)phone •[String](/docs/api/storefront/latest/scalars/String) Token access required
    :   The customer’s phone number.

    [Anchor to socialLoginProvider](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.socialLoginProvider)socialLoginProvider •[SocialLoginProvider](/docs/api/storefront/latest/objects/SocialLoginProvider) Token access required
    :   The social login provider associated with the customer.

        Show fields

    [Anchor to tags](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.tags)tags •[[String!]!](/docs/api/storefront/latest/scalars/String) non-null Token access required
    :   A comma separated list of tags that have been added to the customer.
        Additional access scope required: unauthenticated\_read\_customer\_tags.

    [Anchor to updatedAt](/docs/api/storefront/latest/queries/customer#returns-Customer.fields.updatedAt)updatedAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null Token access required
    :   The date and time when the customer information was updated.

---

Was this section helpful?

YesNo