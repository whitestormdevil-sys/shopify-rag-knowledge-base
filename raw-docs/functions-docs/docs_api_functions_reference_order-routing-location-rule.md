---
source: https://shopify.dev/docs/api/functions/reference/order-routing-location-rule
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

[Order routing](https://help.shopify.com/manual/fulfillment/setup/order-routing/understanding-order-routing) determines
the location to fulfill each item in a cart. A set of rules are used to evaluate an order and prioritize fulfillment
locations. Shopify selects the location with the highest priority ranking to fulfill the order.

Location rules let you send items to different fulfillment locations during order routing. For example, Product A can go
to Location X, and Product B can go to Location Y. If a product has multiple units, such as four units of Product A,
then three can go to Location X and one to Location Y. To define custom order routing rules, you can only use the Order
Routing Location Rule Function API.

[Shopify Functions](/docs/api/functions/current) enable you to customize Shopify's backend logic. The Order Routing
Location Rule API integrates this logic into the checkout flow, as well as for draft orders, order editing, and order
imports. You can also access this logic using the API after checkout, or re-trigger it in the Shopify admin.

Use the API to prioritize locations for order routing, with associated data such as buyer identity, fulfillment groups,
and location addresses.

Beta

The Order Routing Location Rule API is only available by request for merchants that have a
[Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan).

Merchants must be enrolled in the [Partners program](https://help.shopify.com/partners/about) to deploy their own
custom apps and location rules.

To request access to the Order Routing Location Rule API for your store, [sign up for early access](https://www.shopify.com/order-routing-early-access).

**Beta:**

The Order Routing Location Rule API is only available by request for merchants that have a
[Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan).

Merchants must be enrolled in the [Partners program](https://help.shopify.com/partners/about) to deploy their own
custom apps and location rules.

To request access to the Order Routing Location Rule API for your store, [sign up for early access](https://www.shopify.com/order-routing-early-access).

### [Anchor to Use cases](/docs/api/functions/latest/order-routing-location-rule#use-cases)Use cases

* Fulfill orders from the nearest location that serves the shop's market.
* Prioritize a group of locations for order routing, such as warehouses or retail stores.
* Rank locations relative to each other based on product metafields.
* Deprioritize a location if it's exceeded the maximum daily order capacity.
* Prioritize locations that can fulfill items faster or have a certain inventory rotation level.

Compatibility with Shopify surfaces

Supported (8)

Partially supported (3)

Unsupported (3)

* [B2B](https://shopify.dev/docs/apps/build/b2b): Supported
* [Cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart): Supported
* [Checkout](https://shopify.dev/docs/apps/build/checkout): Supported
* [Create Order API](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCreate): Supported
* [Draft Order (Admin)](https://shopify.dev/docs/apps/build/b2b/draft-orders): Supported
* [Draft Order (Checkout)](https://shopify.dev/docs/apps/build/b2b/draft-orders): Supported
* [Order Edit (Admin)](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders): Partially supported

  This option is available only for new items.
* [Order Edit (Checkout)](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders): Not supported
* [POS](https://shopify.dev/docs/apps/build/pos): Partially supported

  POS is available only when shipping to a customer.
* [Pre-order and Try Before You Buy](https://shopify.dev/docs/apps/build/purchase-options/deferred): Not supported
* [Shopify Admin](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries#creating-your-merchant-interface): Supported
* [Storefront](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/): Partially supported

  This option is available only with Buy with Prime.
* [Storefront Accelerated Checkout](https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout): Supported
* [Subscription (Recurring Orders)](https://shopify.dev/docs/apps/build/purchase-options/subscriptions): Not supported

Was this section helpful?

YesNo

---

## [Anchor to Getting started](/docs/api/functions/latest/order-routing-location-rule#getting-started)Getting started

Scaffolding the function using [Shopify CLI](/docs/api/shopify-cli) will automatically configure your TOML file. You can
alter the default [configuration](/docs/api/functions/2026-01#configuration) to customize the way your
function operates.

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

TutorialBuild an Order Routing Location Rule Function

Tutorial

Build an Order Routing Location Rule Function](/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

[Tutorial - Build an Order Routing Location Rule Function](/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

Was this section helpful?

YesNo

---

## [Anchor to Targets](/docs/api/functions/latest/order-routing-location-rule#targets)Targets

A [target](/docs/apps/build/app-extensions/configure-app-extensions#targets) is an identifier in `shopify.extension.toml` that specifies where you're injecting code into Shopify Function
APIs, or other parts of the Shopify platform. Each target is composed of three to four namespaces. The name begins with
a broad Shopify context and ends with the behavior of the extensible element.

---

### [Anchor to Run target](/docs/api/functions/latest/order-routing-location-rule#run-target)Run target

`cart.fulfillment-groups.location-rankings.generate.run`

The run target ranks locations using Shopify data or hardcoded values. Locations must be associated with a fulfillment
group to be ranked. The target returns a list of operations to be applied to locations associated with fulfillment
groups.

For example, you might use this to prioritize warehouses over storefront locations. Locations in the first group will
be [prioritized](#how-fulfillment-groups-are-ranked) over locations in the second group.

* Input

[Anchor to Input](/docs/api/functions/latest/order-routing-location-rule#Input)Input OBJECT
:   The `Input` object is the complete GraphQL schema that your function can query as input to customize order routing logic.
    Your function receives only the fields that you request in the input query. To optimize performance, we highly recommend
    that you request only the fields that your function requires.

    Hide fields

    [Anchor to cart](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart)cart • Cart! non-null
    :   The cart where the Function is running. A cart contains the merchandise that a customer intends to purchase
        and information about the customer, such as the customer's email address and phone number.

        Show fields

        [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.attribute)attribute • Attribute
        :   The custom attributes associated with a cart to store additional information. Cart attributes
            allow you to collect specific information from customers on the **Cart** page, such as order notes,
            gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

            Show arguments and fields

            ### Arguments

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.attribute.arguments.key)key • String
            :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

            ---

            ### Fields

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.attribute.key)key • String! non-null
            :   The key or name of the attribute. For example, `"customer_first_order"`.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.attribute.value)value • String
            :   The value of the attribute. For example, `"true"`.

        [Anchor to buyerIdentity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity)buyerIdentity • BuyerIdentity
        :   Information about the customer that's interacting with the cart. It includes details such as the
            customer's email and phone number, and the total amount of money the customer has spent in the store.
            This information helps personalize the checkout experience and ensures that accurate pricing and delivery options
            are displayed to customers.

            Show fields

            [Anchor to customer](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer)customer • Customer
            :   The [customer](https://help.shopify.com/manual/customers/manage-customers) that's interacting with the cart.

                Show fields

                [Anchor to amountSpent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.amountSpent)amountSpent • MoneyV2! non-null
                :   The total amount that the customer has spent on orders.
                    The amount is converted from the shop's currency to the currency of the cart using a market rate.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.amountSpent.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.amountSpent.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to displayName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.displayName)displayName • String! non-null
                :   The full name of the customer, based on the values for `firstName` and `lastName`.
                    If `firstName` and `lastName` aren't specified, then the value is the customer's email address.
                    If the email address isn't specified, then the value is the customer's phone number.

                [Anchor to email](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.email)email • String
                :   The customer's email address.

                [Anchor to firstName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.firstName)firstName • String
                :   The customer's first name.

                [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasAnyTag)hasAnyTag • Boolean! non-null
                :   Whether the customer is associated with any of the specified tags. The customer must have at least one tag
                    from the list to return `true`.

                    Show arguments

                    ### Arguments

                    [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                    :   A comma-separated list of searchable keywords that are associated with the customer. For example,
                        `"VIP, Gold"` returns customers with either the `VIP` or `Gold` tag.

                    ---

                [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasTags)hasTags • [HasTagResponse!]! non-null
                :   Whether the customer is associated with the specified tags.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                    :   A comma-separated list of searchable keywords that are associated with the customer. For example,
                        `"VIP, Gold"` returns customers with both the `VIP` and `Gold` tags.

                    ---

                    ### Fields

                    [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasTags.hasTag)hasTag • Boolean! non-null
                    :   Whether the Shopify resource has the tag.

                    [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.hasTags.tag)tag • String! non-null
                    :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                        a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                        summer.

                [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.id)id • ID! non-null
                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                    for the customer.

                [Anchor to lastName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.lastName)lastName • String
                :   The customer's last name.

                [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield)metafield • Metafield
                :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                    about a Shopify resource, such as products, orders, and
                    [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                    Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                    enables you to customize the checkout experience.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield.arguments.namespace)namespace • String
                    :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                        between different apps or different parts of the same app. If omitted, then the
                        [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                        is used.

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield.arguments.key)key • String! required
                    :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                        namespace and a key, in the format `namespace.key`.

                    ---

                    ### Fields

                    [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield.jsonValue)jsonValue • JSON! non-null
                    :   The data that's stored in the metafield, using JSON format.

                    [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield.type)type • String! non-null
                    :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                        the `value` field.

                    [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.metafield.value)value • String! non-null
                    :   The data that's stored in the metafield. The data is always stored as a string,
                        regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                [Anchor to numberOfOrders](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.customer.numberOfOrders)numberOfOrders • Int! non-null
                :   The total number of orders that the customer has made at the store.

            [Anchor to email](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.email)email • String
            :   The email address of the customer that's interacting with the cart.

            [Anchor to isAuthenticated](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.isAuthenticated)isAuthenticated • Boolean! non-null
            :   Whether the customer is authenticated through their
                [customer account](https://help.shopify.com/manual/customers/customer-accounts).

            [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.phone)phone • String
            :   The phone number of the customer that's interacting with the cart.

            [Anchor to purchasingCompany](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany)purchasingCompany • PurchasingCompany
            :   The company of a B2B customer that's interacting with the cart.
                Used to manage and track purchases made by businesses rather than individual customers.

                Show fields

                [Anchor to company](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company)company • Company! non-null
                :   The company associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company was created in Shopify.

                    [Anchor to externalId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.externalId)externalId • String
                    :   A unique externally-supplied ID for the company.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.name)name • String! non-null
                    :   The name of the company.

                    [Anchor to updatedAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.company.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company was last modified.

                [Anchor to contact](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact)contact • CompanyContact
                :   The company contact associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company contact was created in Shopify.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to locale](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact.locale)locale • String
                    :   The company contact's locale (language).

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact.title)title • String
                    :   The company contact's job title.

                    [Anchor to updatedAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.contact.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company contact was last modified.

                [Anchor to location](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location)location • CompanyLocation! non-null
                :   The company location associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company location was created in Shopify.

                    [Anchor to externalId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.externalId)externalId • String
                    :   A unique externally-supplied ID for the company.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to locale](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.locale)locale • String
                    :   The preferred locale of the company location.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.name)name • String! non-null
                    :   The name of the company location.

                    [Anchor to ordersCount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.ordersCount)ordersCount • Int! non-null
                    :   The number of orders placed at this company location.

                    [Anchor to totalSpent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent)totalSpent • MoneyV2! non-null
                    :   The total amount spent at this company location.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to updatedAt](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.buyerIdentity.purchasingCompany.location.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company location was last modified.

        [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost)cost • CartCost! non-null
        :   A breakdown of the costs that the customer will pay at checkout. It includes the total amount,
            the subtotal before taxes and duties, the tax amount, and duty charges.

            Show fields

            [Anchor to subtotalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
            :   The amount, before taxes and cart-level discounts, for the customer to pay.

                Show fields

                [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.subtotalAmount.amount)amount • Decimal! non-null
                :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                    currency. For example, 12.99.

                [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                :   The three-letter currency code that represents a world currency used in a store. Currency codes
                    include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                    and non-standard codes. For example, USD.

                    Show enum values

                    AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to totalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalAmount)totalAmount • MoneyV2! non-null
            :   The total amount for the customer to pay at checkout.

                Show fields

                [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalAmount.amount)amount • Decimal! non-null
                :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                    currency. For example, 12.99.

                [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                :   The three-letter currency code that represents a world currency used in a store. Currency codes
                    include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                    and non-standard codes. For example, USD.

                    Show enum values

                    AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to totalDutyAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalDutyAmount)totalDutyAmount • MoneyV2
            :   The duty charges for a customer to pay at checkout.

                Show fields

                [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalDutyAmount.amount)amount • Decimal! non-null
                :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                    currency. For example, 12.99.

                [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalDutyAmount.currencyCode)currencyCode • CurrencyCode! non-null
                :   The three-letter currency code that represents a world currency used in a store. Currency codes
                    include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                    and non-standard codes. For example, USD.

                    Show enum values

                    AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to totalTaxAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalTaxAmount)totalTaxAmount • MoneyV2
            :   The total tax amount for the customer to pay at checkout.

                Show fields

                [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalTaxAmount.amount)amount • Decimal! non-null
                :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                    currency. For example, 12.99.

                [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.cost.totalTaxAmount.currencyCode)currencyCode • CurrencyCode! non-null
                :   The three-letter currency code that represents a world currency used in a store. Currency codes
                    include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                    and non-standard codes. For example, USD.

                    Show enum values

                    AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

        [Anchor to deliverableLines](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines)deliverableLines • [DeliverableCartLine!]! non-null
        :   The items in a cart that are eligible for fulfillment and can be delivered to the customer.

            Show fields

            [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.attribute)attribute • Attribute
            :   The custom attributes associated with a cart to store additional information. Cart attributes
                allow you to collect specific information from customers on the **Cart** page, such as order notes,
                gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                Cart line attributes are equivalent to the
                [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                object in Liquid.

                Show arguments and fields

                ### Arguments

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.attribute.arguments.key)key • String
                :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                ---

                ### Fields

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.attribute.key)key • String! non-null
                :   The key or name of the attribute. For example, `"customer_first_order"`.

                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.attribute.value)value • String
                :   The value of the attribute. For example, `"true"`.

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.id)id • ID! non-null
            :   The ID of the cart line.

            [Anchor to merchandise](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise)merchandise • Merchandise! non-null
            :   The item that the customer intends to purchase.

                Show union types

                [Anchor to CustomProduct](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct) CustomProduct •OBJECT
                :   A custom product represents a product that doesn't map to Shopify's
                    [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                    For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                    information, or weight measurements and conversions.

                    Show fields

                    [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                    :   Whether the merchandise is a gift card.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct.title)title • String! non-null
                    :   The localized name for the product that displays to customers. The title is used to construct the product's
                        handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                        "Black Sunglasses", then the handle is `black-sunglasses`.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to ProductVariant](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant) ProductVariant •OBJECT
                :   A specific version of a product that comes in more than one option, such as size or color. For example,
                    if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                    product variant and a large, blue t-shirt would be another.

                    Show fields

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.id)id • ID! non-null
                    :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                        for the product variant.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to product](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product)product • Product! non-null
                    :   The product associated with the product variant. For example, if a
                        merchant sells t-shirts with options for size and color, then a small,
                        blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                        The product associated with the product variant would be the t-shirt itself.

                        Show fields

                        [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                        :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                            numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                            is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                        :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                            from the list to return `true`.

                            Show arguments

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with either the `sports` or `summer` tag.

                            ---

                        [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                        :   Whether the product is associated with the specified tags.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with both the `sports` and `summer` tags.

                            ---

                            ### Fields

                            [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                            :   Whether the Shopify resource has the tag.

                            [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                            :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                summer.

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product.

                        [Anchor to inAnyCollection](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                        :   Whether the product is in any of the specified collections. The product must be in at least one collection
                            from the list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                        [Anchor to inCollections](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                        :   Whether the product is in the specified collections. The product must be in all of the collections in the
                            list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                            ### Fields

                            [Anchor to collectionId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the collection.

                            [Anchor to isMember](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                            :   Whether the product is in the specified collection.

                        [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the product is a gift card.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to productType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.productType)productType • String
                        :   A custom category for a product. Product types allow merchants to define categories other than the
                            ones available in Shopify's
                            [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to vendor](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.product.vendor)vendor • String
                        :   The name of the product's vendor.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to sku](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.sku)sku • String
                    :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                        A product variant must have a SKU to be connected to a
                        [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.title)title • String
                    :   The localized name for the product variant that displays to customers.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

            [Anchor to quantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliverableLines.quantity)quantity • Int! non-null
            :   The quantity of the item that the customer intends to purchase.

        [Anchor to deliveryGroups](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups)deliveryGroups • [CartDeliveryGroup!]! non-null
        :   A collection of items that are grouped by shared delivery characteristics. Delivery groups streamline
            fulfillment by organizing items that can be shipped together, based on the customer's
            shipping address. For example, if a customer orders a t-shirt and a pair of shoes that can be shipped
            together, then the items are included in the same delivery group.

            In the [Order Discount](https://shopify.dev/docs/api/functions/reference/order-discounts) and
            [Product Discount](https://shopify.dev/docs/api/functions/reference/product-discounts) legacy APIs,
            the `cart.deliveryGroups` input is always an empty array. This means you can't access delivery groups when
            creating Order Discount or Product Discount Functions. If you need to apply discounts to shipping costs,
            then use the [Discount Function API](https://shopify.dev/docs/api/functions/reference/discount)
            instead.

            Show fields

            [Anchor to cartLines](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines)cartLines • [CartLine!]! non-null
            :   Information about items in a cart that a customer intends to purchase. A cart line is an entry in the
                customer's cart that represents a single unit of a product variant. For example, if a customer adds two
                different sizes of the same t-shirt to their cart, then each size is represented as a separate cart line.

                Show fields

                [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.attribute)attribute • Attribute
                :   The custom attributes associated with a cart to store additional information. Cart attributes
                    allow you to collect specific information from customers on the **Cart** page, such as order notes,
                    gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                    Cart line attributes are equivalent to the
                    [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                    object in Liquid.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.attribute.arguments.key)key • String
                    :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                    ---

                    ### Fields

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.attribute.key)key • String! non-null
                    :   The key or name of the attribute. For example, `"customer_first_order"`.

                    [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.attribute.value)value • String
                    :   The value of the attribute. For example, `"true"`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost)cost • CartLineCost! non-null
                :   The cost of an item in a cart that the customer intends to purchase. Cart lines are entries in the customer's
                    cart that represent a single unit of a product variant. For example, if a customer adds two different sizes of
                    the same t-shirt to their cart, then each size is represented as a separate cart line.

                    Show fields

                    [Anchor to amountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.amountPerQuantity)amountPerQuantity • MoneyV2! non-null
                    :   The cost of a single unit. For example, if a customer purchases three units of a product
                        that are priced at $10 each, then the `amountPerQuantity` is $10.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.amountPerQuantity.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.amountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to compareAtAmountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.compareAtAmountPerQuantity)compareAtAmountPerQuantity • MoneyV2
                    :   The `compareAt` price of a single unit before any discounts are applied. This field is used to calculate and display
                        savings for customers. For example, if a product's `compareAtAmountPerQuantity` is $25 and its current price
                        is $20, then the customer sees a $5 discount. This value can change based on the buyer's identity and is
                        `null` when the value is hidden from buyers.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.compareAtAmountPerQuantity.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.compareAtAmountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to subtotalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
                    :   The cost of items in the cart before applying any discounts to certain items.
                        This amount serves as the starting point for calculating any potential savings customers
                        might receive through promotions or discounts.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.subtotalAmount.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to totalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.totalAmount)totalAmount • MoneyV2! non-null
                    :   The total cost of items in a cart.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.totalAmount.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.id)id • ID! non-null
                :   The ID of the cart line.

                [Anchor to merchandise](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise)merchandise • Merchandise! non-null
                :   The item that the customer intends to purchase.

                    Show union types

                    [Anchor to CustomProduct](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct) CustomProduct •OBJECT
                    :   A custom product represents a product that doesn't map to Shopify's
                        [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                        For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                        information, or weight measurements and conversions.

                        Show fields

                        [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the merchandise is a gift card.

                        [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                        :   Whether the item needs to be shipped to the customer. For example, a
                            digital gift card doesn't need to be shipped, but a t-shirt does
                            need to be shipped.

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct.weight)weight • Float
                        :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                        [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                        :   The unit of measurement for weight.

                            Show enum values

                            GRAMS, KILOGRAMS, OUNCES, POUNDS

                    [Anchor to ProductVariant](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant) ProductVariant •OBJECT
                    :   A specific version of a product that comes in more than one option, such as size or color. For example,
                        if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                        product variant and a large, blue t-shirt would be another.

                        Show fields

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product variant.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to product](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product)product • Product! non-null
                        :   The product associated with the product variant. For example, if a
                            merchant sells t-shirts with options for size and color, then a small,
                            blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                            The product associated with the product variant would be the t-shirt itself.

                            Show fields

                            [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                            :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                                numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                                is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                            [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                            :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                                from the list to return `true`.

                                Show arguments

                                ### Arguments

                                [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                                :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                    `"sports, summer"` returns products with either the `sports` or `summer` tag.

                                ---

                            [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                            :   Whether the product is associated with the specified tags.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                                :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                    `"sports, summer"` returns products with both the `sports` and `summer` tags.

                                ---

                                ### Fields

                                [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                                :   Whether the Shopify resource has the tag.

                                [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                                :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                    a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                    summer.

                            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.id)id • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the product.

                            [Anchor to inAnyCollection](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                            :   Whether the product is in any of the specified collections. The product must be in at least one collection
                                from the list to return `true`.

                                A collection is a group of products that can be displayed in online stores and other sales channels in
                                categories, which makes it easy for customers to find them. For example, an athletics store might create
                                different collections for running attire and accessories.

                                Show arguments

                                ### Arguments

                                [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                                :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                    that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                                ---

                            [Anchor to inCollections](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                            :   Whether the product is in the specified collections. The product must be in all of the collections in the
                                list to return `true`.

                                A collection is a group of products that can be displayed in online stores and other sales channels in
                                categories, which makes it easy for customers to find them. For example, an athletics store might create
                                different collections for running attire and accessories.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                                :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                    that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                                ---

                                ### Fields

                                [Anchor to collectionId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                    for the collection.

                                [Anchor to isMember](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                                :   Whether the product is in the specified collection.

                            [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                            :   Whether the product is a gift card.

                            [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                                about a Shopify resource, such as products, orders, and
                                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                                enables you to customize the checkout experience.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                    between different apps or different parts of the same app. If omitted, then the
                                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                    is used.

                                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                    namespace and a key, in the format `namespace.key`.

                                ---

                                ### Fields

                                [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                                :   The data that's stored in the metafield, using JSON format.

                                [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                    the `value` field.

                                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                                :   The data that's stored in the metafield. The data is always stored as a string,
                                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                            [Anchor to productType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.productType)productType • String
                            :   A custom category for a product. Product types allow merchants to define categories other than the
                                ones available in Shopify's
                                [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                            [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.title)title • String! non-null
                            :   The localized name for the product that displays to customers. The title is used to construct the product's
                                handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                                "Black Sunglasses", then the handle is `black-sunglasses`.

                            [Anchor to vendor](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.product.vendor)vendor • String
                            :   The name of the product's vendor.

                        [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                        :   Whether the item needs to be shipped to the customer. For example, a
                            digital gift card doesn't need to be shipped, but a t-shirt does
                            need to be shipped.

                        [Anchor to sku](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.sku)sku • String
                        :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                            A product variant must have a SKU to be connected to a
                            [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.title)title • String
                        :   The localized name for the product variant that displays to customers.

                        [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.weight)weight • Float
                        :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                        [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                        :   The unit of measurement for weight.

                            Show enum values

                            GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to parentRelationship](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.parentRelationship)parentRelationship • CartLineParentRelationship
                :   The [nested relationship](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines)
                    between this line and its parent line, if any.

                    Show fields

                    [Anchor to parent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.parentRelationship.parent)parent • CartLine! non-null
                    :   The parent line in the relationship.

                [Anchor to quantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.quantity)quantity • Int! non-null
                :   The quantity of the item that the customer intends to purchase.

                [Anchor to sellingPlanAllocation](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation)sellingPlanAllocation • SellingPlanAllocation
                :   The [selling plan](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans)
                    associated with the cart line, including information about how a product variant can be sold and purchased.

                    Show fields

                    [Anchor to priceAdjustments](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments)priceAdjustments • [SellingPlanAllocationPriceAdjustment!]! non-null
                    :   A list of price adjustments, with a maximum of two. When there are two, the first price adjustment goes into effect at the time of purchase, while the second one starts after a certain number of orders. A price adjustment represents how a selling plan affects pricing when a variant is purchased with a selling plan. Prices display in the customer's currency if the shop is configured for it.

                        Show fields

                        [Anchor to perDeliveryPrice](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice)perDeliveryPrice • MoneyV2! non-null
                        :   The effective price for a single delivery. For example, for a prepaid subscription plan that includes 6 deliveries at the price of $48.00, the per delivery price is $8.00.

                            Show fields

                            [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.amount)amount • Decimal! non-null
                            :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                                currency. For example, 12.99.

                            [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.currencyCode)currencyCode • CurrencyCode! non-null
                            :   The three-letter currency code that represents a world currency used in a store. Currency codes
                                include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                                and non-standard codes. For example, USD.

                                Show enum values

                                AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                        [Anchor to price](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.price)price • MoneyV2! non-null
                        :   The price of the variant when it's purchased with a selling plan For example, for a prepaid subscription plan that includes 6 deliveries of $10.00 granola, where the customer gets 20% off, the price is 6 x $10.00 x 0.80 = $48.00.

                            Show fields

                            [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.price.amount)amount • Decimal! non-null
                            :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                                currency. For example, 12.99.

                            [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.priceAdjustments.price.currencyCode)currencyCode • CurrencyCode! non-null
                            :   The three-letter currency code that represents a world currency used in a store. Currency codes
                                include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                                and non-standard codes. For example, USD.

                                Show enum values

                                AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to sellingPlan](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan)sellingPlan • SellingPlan! non-null
                    :   A representation of how products and variants can be sold and purchased. For example, an individual selling plan could be '6 weeks of prepaid granola, delivered weekly'.

                        Show fields

                        [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.description)description • String
                        :   The description of the selling plan.

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.id)id • ID! non-null
                        :   A globally-unique identifier.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.name)name • String! non-null
                        :   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

                        [Anchor to recurringDeliveries](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.cartLines.sellingPlanAllocation.sellingPlan.recurringDeliveries)recurringDeliveries • Boolean! non-null
                        :   Whether purchasing the selling plan will result in multiple deliveries.

            [Anchor to deliveryAddress](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress)deliveryAddress • MailingAddress
            :   The shipping or destination address associated with the delivery group.

                Show fields

                [Anchor to address1](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.address1)address1 • String
                :   The first line of the address. Typically the street address or PO Box number.

                [Anchor to address2](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.address2)address2 • String
                :   The second line of the address. Typically the number of the apartment, suite, or unit.

                [Anchor to city](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.city)city • String
                :   The name of the city, district, village, or town.

                [Anchor to company](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.company)company • String
                :   The name of the customer's company or organization.

                [Anchor to countryCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.countryCode)countryCode • CountryCode
                :   The two-letter code for the country of the address. For example, US.

                    Show enum values

                    AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AR, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MK, ML, MM, MN, MO, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PS, PT, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TA, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW, ZZ

                [Anchor to firstName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.firstName)firstName • String
                :   The first name of the customer.

                [Anchor to lastName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.lastName)lastName • String
                :   The last name of the customer.

                [Anchor to latitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.latitude)latitude • Float
                :   The approximate latitude of the address.

                [Anchor to longitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.longitude)longitude • Float
                :   The approximate longitude of the address.

                [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.name)name • String
                :   The full name of the customer, based on firstName and lastName.

                [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.phone)phone • String
                :   A unique phone number for the customer. Formatted using E.164 standard. For example, +16135551111.

                [Anchor to provinceCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.provinceCode)provinceCode • String
                :   The alphanumeric code for the region. For example, ON.

                [Anchor to zip](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.zip)zip • String
                :   The zip or postal code of the address.

                [Anchor to market](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market)market • Market Deprecated
                :   Show fields

                    [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.handle)handle • Handle! non-null
                    :   A human-readable unique string for the market automatically generated from its title.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.id)id • ID! non-null
                    :   A globally-unique identifier.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to regions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.regions)regions • [MarketRegion!]! non-null
                    :   A geographic region which comprises a market.

                        Show fields

                        [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryAddress.market.regions.name)name • String
                        :   The name of the region in the language of the current localization.

            [Anchor to deliveryOptions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions)deliveryOptions • [CartDeliveryOption!]! non-null
            :   The delivery options available for the delivery group. Delivery options are the different ways that customers
                can choose to have their orders shipped. Examples include express shipping or standard shipping.

                Show fields

                [Anchor to code](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.code)code • String
                :   A unique identifier that represents the delivery option offered to customers.
                    For example, `Canada Post Expedited`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.cost)cost • MoneyV2! non-null
                :   The amount that the customer pays if they select the delivery option.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.cost.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.cost.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to deliveryMethodType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.deliveryMethodType)deliveryMethodType • DeliveryMethod! non-null
                :   The delivery method associated with the delivery option. A delivery method is a way that merchants can
                    fulfill orders from their online stores. Delivery methods include shipping to an address,
                    [local pickup](https://help.shopify.com/manual/fulfillment/setup/delivery-methods/pickup-in-store),
                    and shipping to a [pickup point](https://help.shopify.com/manual/fulfillment/shopify-shipping/pickup-points),
                    all of which are natively supported by Shopify checkout.

                    Show enum values

                    LOCAL, NONE, PICK\_UP, PICKUP\_POINT, RETAIL, SHIPPING

                [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.description)description • String
                :   A single-line description of the delivery option, with HTML tags removed.

                [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.handle)handle • Handle! non-null
                :   A unique, human-readable identifier of the delivery option's title.
                    A handle can contain letters, hyphens (`-`), and numbers, but not spaces.
                    For example, `standard-shipping`.

                [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.deliveryOptions.title)title • String
                :   The name of the delivery option that displays to customers. The title is used to construct the delivery
                    option's handle. For example, if a delivery option is titled "Standard Shipping", then the handle is
                    `standard-shipping`.

            [Anchor to groupType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.groupType)groupType • CartDeliveryGroupType! non-null
            :   The type of merchandise in the delivery group.

                Show enum values

                ONE\_TIME\_PURCHASE, SUBSCRIPTION

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.id)id • ID! non-null
            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                for the delivery group.

            [Anchor to selectedDeliveryOption](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption)selectedDeliveryOption • CartDeliveryOption
            :   Information about the delivery option that the customer has selected.

                Show fields

                [Anchor to code](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.code)code • String
                :   A unique identifier that represents the delivery option offered to customers.
                    For example, `Canada Post Expedited`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.cost)cost • MoneyV2! non-null
                :   The amount that the customer pays if they select the delivery option.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.cost.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.cost.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to deliveryMethodType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.deliveryMethodType)deliveryMethodType • DeliveryMethod! non-null
                :   The delivery method associated with the delivery option. A delivery method is a way that merchants can
                    fulfill orders from their online stores. Delivery methods include shipping to an address,
                    [local pickup](https://help.shopify.com/manual/fulfillment/setup/delivery-methods/pickup-in-store),
                    and shipping to a [pickup point](https://help.shopify.com/manual/fulfillment/shopify-shipping/pickup-points),
                    all of which are natively supported by Shopify checkout.

                    Show enum values

                    LOCAL, NONE, PICK\_UP, PICKUP\_POINT, RETAIL, SHIPPING

                [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.description)description • String
                :   A single-line description of the delivery option, with HTML tags removed.

                [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.handle)handle • Handle! non-null
                :   A unique, human-readable identifier of the delivery option's title.
                    A handle can contain letters, hyphens (`-`), and numbers, but not spaces.
                    For example, `standard-shipping`.

                [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.deliveryGroups.selectedDeliveryOption.title)title • String
                :   The name of the delivery option that displays to customers. The title is used to construct the delivery
                    option's handle. For example, if a delivery option is titled "Standard Shipping", then the handle is
                    `standard-shipping`.

        [Anchor to lines](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines)lines • [CartLine!]! non-null
        :   The items in a cart that the customer intends to purchase. A cart line is an entry in the
            customer's cart that represents a single unit of a product variant. For example, if a customer adds two
            different sizes of the same t-shirt to their cart, then each size is represented as a separate cart line.

            Show fields

            [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.attribute)attribute • Attribute
            :   The custom attributes associated with a cart to store additional information. Cart attributes
                allow you to collect specific information from customers on the **Cart** page, such as order notes,
                gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                Cart line attributes are equivalent to the
                [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                object in Liquid.

                Show arguments and fields

                ### Arguments

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.attribute.arguments.key)key • String
                :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                ---

                ### Fields

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.attribute.key)key • String! non-null
                :   The key or name of the attribute. For example, `"customer_first_order"`.

                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.attribute.value)value • String
                :   The value of the attribute. For example, `"true"`.

            [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost)cost • CartLineCost! non-null
            :   The cost of an item in a cart that the customer intends to purchase. Cart lines are entries in the customer's
                cart that represent a single unit of a product variant. For example, if a customer adds two different sizes of
                the same t-shirt to their cart, then each size is represented as a separate cart line.

                Show fields

                [Anchor to amountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.amountPerQuantity)amountPerQuantity • MoneyV2! non-null
                :   The cost of a single unit. For example, if a customer purchases three units of a product
                    that are priced at $10 each, then the `amountPerQuantity` is $10.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.amountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.amountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to compareAtAmountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.compareAtAmountPerQuantity)compareAtAmountPerQuantity • MoneyV2
                :   The `compareAt` price of a single unit before any discounts are applied. This field is used to calculate and display
                    savings for customers. For example, if a product's `compareAtAmountPerQuantity` is $25 and its current price
                    is $20, then the customer sees a $5 discount. This value can change based on the buyer's identity and is
                    `null` when the value is hidden from buyers.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.compareAtAmountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.compareAtAmountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to subtotalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
                :   The cost of items in the cart before applying any discounts to certain items.
                    This amount serves as the starting point for calculating any potential savings customers
                    might receive through promotions or discounts.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.subtotalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to totalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.totalAmount)totalAmount • MoneyV2! non-null
                :   The total cost of items in a cart.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.totalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.id)id • ID! non-null
            :   The ID of the cart line.

            [Anchor to merchandise](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise)merchandise • Merchandise! non-null
            :   The item that the customer intends to purchase.

                Show union types

                [Anchor to CustomProduct](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct) CustomProduct •OBJECT
                :   A custom product represents a product that doesn't map to Shopify's
                    [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                    For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                    information, or weight measurements and conversions.

                    Show fields

                    [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                    :   Whether the merchandise is a gift card.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct.title)title • String! non-null
                    :   The localized name for the product that displays to customers. The title is used to construct the product's
                        handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                        "Black Sunglasses", then the handle is `black-sunglasses`.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to ProductVariant](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant) ProductVariant •OBJECT
                :   A specific version of a product that comes in more than one option, such as size or color. For example,
                    if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                    product variant and a large, blue t-shirt would be another.

                    Show fields

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.id)id • ID! non-null
                    :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                        for the product variant.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to product](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product)product • Product! non-null
                    :   The product associated with the product variant. For example, if a
                        merchant sells t-shirts with options for size and color, then a small,
                        blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                        The product associated with the product variant would be the t-shirt itself.

                        Show fields

                        [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                        :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                            numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                            is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                        :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                            from the list to return `true`.

                            Show arguments

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with either the `sports` or `summer` tag.

                            ---

                        [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                        :   Whether the product is associated with the specified tags.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with both the `sports` and `summer` tags.

                            ---

                            ### Fields

                            [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                            :   Whether the Shopify resource has the tag.

                            [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                            :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                summer.

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product.

                        [Anchor to inAnyCollection](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                        :   Whether the product is in any of the specified collections. The product must be in at least one collection
                            from the list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                        [Anchor to inCollections](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                        :   Whether the product is in the specified collections. The product must be in all of the collections in the
                            list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                            ### Fields

                            [Anchor to collectionId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the collection.

                            [Anchor to isMember](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                            :   Whether the product is in the specified collection.

                        [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the product is a gift card.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to productType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.productType)productType • String
                        :   A custom category for a product. Product types allow merchants to define categories other than the
                            ones available in Shopify's
                            [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to vendor](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.product.vendor)vendor • String
                        :   The name of the product's vendor.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to sku](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.sku)sku • String
                    :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                        A product variant must have a SKU to be connected to a
                        [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.title)title • String
                    :   The localized name for the product variant that displays to customers.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

            [Anchor to parentRelationship](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.parentRelationship)parentRelationship • CartLineParentRelationship
            :   The [nested relationship](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines)
                between this line and its parent line, if any.

                Show fields

                [Anchor to parent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.parentRelationship.parent)parent • CartLine! non-null
                :   The parent line in the relationship.

            [Anchor to quantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.quantity)quantity • Int! non-null
            :   The quantity of the item that the customer intends to purchase.

            [Anchor to sellingPlanAllocation](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation)sellingPlanAllocation • SellingPlanAllocation
            :   The [selling plan](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans)
                associated with the cart line, including information about how a product variant can be sold and purchased.

                Show fields

                [Anchor to priceAdjustments](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments)priceAdjustments • [SellingPlanAllocationPriceAdjustment!]! non-null
                :   A list of price adjustments, with a maximum of two. When there are two, the first price adjustment goes into effect at the time of purchase, while the second one starts after a certain number of orders. A price adjustment represents how a selling plan affects pricing when a variant is purchased with a selling plan. Prices display in the customer's currency if the shop is configured for it.

                    Show fields

                    [Anchor to perDeliveryPrice](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice)perDeliveryPrice • MoneyV2! non-null
                    :   The effective price for a single delivery. For example, for a prepaid subscription plan that includes 6 deliveries at the price of $48.00, the per delivery price is $8.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to price](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price)price • MoneyV2! non-null
                    :   The price of the variant when it's purchased with a selling plan For example, for a prepaid subscription plan that includes 6 deliveries of $10.00 granola, where the customer gets 20% off, the price is 6 x $10.00 x 0.80 = $48.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to sellingPlan](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan)sellingPlan • SellingPlan! non-null
                :   A representation of how products and variants can be sold and purchased. For example, an individual selling plan could be '6 weeks of prepaid granola, delivered weekly'.

                    Show fields

                    [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.description)description • String
                    :   The description of the selling plan.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.id)id • ID! non-null
                    :   A globally-unique identifier.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.name)name • String! non-null
                    :   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

                    [Anchor to recurringDeliveries](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.recurringDeliveries)recurringDeliveries • Boolean! non-null
                    :   Whether purchasing the selling plan will result in multiple deliveries.

        [Anchor to localizedFields](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.localizedFields)localizedFields • [LocalizedField!]! non-null
        :   The additional fields on the **Cart** page that are required for international orders in specific countries,
            such as customs information or tax identification numbers.

            Show arguments and fields

            ### Arguments

            [Anchor to keys](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.localizedFields.arguments.keys)keys • [LocalizedFieldKey!]! requiredDefault:[]
            :   The keys of the localized fields to retrieve.

                Show enum values

                SHIPPING\_CREDENTIAL\_BR, SHIPPING\_CREDENTIAL\_CL, SHIPPING\_CREDENTIAL\_CN, SHIPPING\_CREDENTIAL\_CO, SHIPPING\_CREDENTIAL\_CR, SHIPPING\_CREDENTIAL\_EC, SHIPPING\_CREDENTIAL\_ES, SHIPPING\_CREDENTIAL\_GT, SHIPPING\_CREDENTIAL\_ID, SHIPPING\_CREDENTIAL\_KR, SHIPPING\_CREDENTIAL\_MX, SHIPPING\_CREDENTIAL\_MY, SHIPPING\_CREDENTIAL\_PE, SHIPPING\_CREDENTIAL\_PT, SHIPPING\_CREDENTIAL\_PY, SHIPPING\_CREDENTIAL\_TR, SHIPPING\_CREDENTIAL\_TW, SHIPPING\_CREDENTIAL\_TYPE\_CO, TAX\_CREDENTIAL\_BR, TAX\_CREDENTIAL\_CL, TAX\_CREDENTIAL\_CO, TAX\_CREDENTIAL\_CR, TAX\_CREDENTIAL\_EC, TAX\_CREDENTIAL\_ES, TAX\_CREDENTIAL\_GT, TAX\_CREDENTIAL\_ID, TAX\_CREDENTIAL\_IT, TAX\_CREDENTIAL\_MX, TAX\_CREDENTIAL\_MY, TAX\_CREDENTIAL\_PE, TAX\_CREDENTIAL\_PT, TAX\_CREDENTIAL\_PY, TAX\_CREDENTIAL\_TR, TAX\_CREDENTIAL\_TYPE\_CO, TAX\_CREDENTIAL\_TYPE\_MX, TAX\_CREDENTIAL\_USE\_MX, TAX\_EMAIL\_IT

            ---

            ### Fields

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.localizedFields.key)key • LocalizedFieldKey! non-null
            :   The key of the localized field.

                Show enum values

                SHIPPING\_CREDENTIAL\_BR, SHIPPING\_CREDENTIAL\_CL, SHIPPING\_CREDENTIAL\_CN, SHIPPING\_CREDENTIAL\_CO, SHIPPING\_CREDENTIAL\_CR, SHIPPING\_CREDENTIAL\_EC, SHIPPING\_CREDENTIAL\_ES, SHIPPING\_CREDENTIAL\_GT, SHIPPING\_CREDENTIAL\_ID, SHIPPING\_CREDENTIAL\_KR, SHIPPING\_CREDENTIAL\_MX, SHIPPING\_CREDENTIAL\_MY, SHIPPING\_CREDENTIAL\_PE, SHIPPING\_CREDENTIAL\_PT, SHIPPING\_CREDENTIAL\_PY, SHIPPING\_CREDENTIAL\_TR, SHIPPING\_CREDENTIAL\_TW, SHIPPING\_CREDENTIAL\_TYPE\_CO, TAX\_CREDENTIAL\_BR, TAX\_CREDENTIAL\_CL, TAX\_CREDENTIAL\_CO, TAX\_CREDENTIAL\_CR, TAX\_CREDENTIAL\_EC, TAX\_CREDENTIAL\_ES, TAX\_CREDENTIAL\_GT, TAX\_CREDENTIAL\_ID, TAX\_CREDENTIAL\_IT, TAX\_CREDENTIAL\_MX, TAX\_CREDENTIAL\_MY, TAX\_CREDENTIAL\_PE, TAX\_CREDENTIAL\_PT, TAX\_CREDENTIAL\_PY, TAX\_CREDENTIAL\_TR, TAX\_CREDENTIAL\_TYPE\_CO, TAX\_CREDENTIAL\_TYPE\_MX, TAX\_CREDENTIAL\_USE\_MX, TAX\_EMAIL\_IT

            [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.localizedFields.title)title • String! non-null
            :   The title of the localized field.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.localizedFields.value)value • String
            :   The value of the localized field.

        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

        [Anchor to retailLocation](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation)retailLocation • Location
        :   The physical location where a retail order is created or completed.

            Show fields

            [Anchor to address](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address)address • LocationAddress! non-null
            :   The address of this location.

                Show fields

                [Anchor to address1](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.address1)address1 • String
                :   The first line of the address for the location.

                [Anchor to address2](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.address2)address2 • String
                :   The second line of the address for the location.

                [Anchor to city](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.city)city • String
                :   The city of the location.

                [Anchor to country](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.country)country • String
                :   The country of the location.

                [Anchor to countryCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.countryCode)countryCode • String
                :   The country code of the location.

                [Anchor to formatted](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.formatted)formatted • [String!]! non-null
                :   A formatted version of the address for the location.

                [Anchor to latitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.latitude)latitude • Float
                :   The approximate latitude coordinates of the location.

                [Anchor to longitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.longitude)longitude • Float
                :   The approximate longitude coordinates of the location.

                [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.phone)phone • String
                :   The phone number of the location.

                [Anchor to province](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.province)province • String
                :   The province of the location.

                [Anchor to provinceCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.provinceCode)provinceCode • String
                :   The code for the province, state, or district of the address of the location.

                [Anchor to zip](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.address.zip)zip • String
                :   The ZIP code of the location.

            [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.handle)handle • Handle! non-null
            :   The location handle.

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.id)id • ID! non-null
            :   The location id.

            [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield)metafield • Metafield
            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                about a Shopify resource, such as products, orders, and
                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                enables you to customize the checkout experience.

                Show arguments and fields

                ### Arguments

                [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield.arguments.namespace)namespace • String
                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                    between different apps or different parts of the same app. If omitted, then the
                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                    is used.

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield.arguments.key)key • String! required
                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                    namespace and a key, in the format `namespace.key`.

                ---

                ### Fields

                [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield.jsonValue)jsonValue • JSON! non-null
                :   The data that's stored in the metafield, using JSON format.

                [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield.type)type • String! non-null
                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                    the `value` field.

                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.metafield.value)value • String! non-null
                :   The data that's stored in the metafield. The data is always stored as a string,
                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

            [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.cart.retailLocation.name)name • String! non-null
            :   The name of the location.

    [Anchor to fulfillmentGroups](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups)fulfillmentGroups • [FulfillmentGroup!]! non-null
    :   A list of
        [fulfillment locations](https://shopify.dev/manual/fulfillment/setup/shipping-profiles/managing-fulfillment-locations)
        that contain one or more items to be shipped together. Each item in the cart is assigned to one
        fulfillment group.

        Show fields

        [Anchor to deliveryAddress](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress)deliveryAddress • MailingAddress
        :   The delivery address for the fulfillment group.

            Show fields

            [Anchor to address1](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.address1)address1 • String
            :   The first line of the address. Typically the street address or PO Box number.

            [Anchor to address2](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.address2)address2 • String
            :   The second line of the address. Typically the number of the apartment, suite, or unit.

            [Anchor to city](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.city)city • String
            :   The name of the city, district, village, or town.

            [Anchor to company](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.company)company • String
            :   The name of the customer's company or organization.

            [Anchor to countryCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.countryCode)countryCode • CountryCode
            :   The two-letter code for the country of the address. For example, US.

                Show enum values

                AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AR, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MK, ML, MM, MN, MO, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PS, PT, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TA, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW, ZZ

            [Anchor to firstName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.firstName)firstName • String
            :   The first name of the customer.

            [Anchor to lastName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.lastName)lastName • String
            :   The last name of the customer.

            [Anchor to latitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.latitude)latitude • Float
            :   The approximate latitude of the address.

            [Anchor to longitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.longitude)longitude • Float
            :   The approximate longitude of the address.

            [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.name)name • String
            :   The full name of the customer, based on firstName and lastName.

            [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.phone)phone • String
            :   A unique phone number for the customer. Formatted using E.164 standard. For example, +16135551111.

            [Anchor to provinceCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.provinceCode)provinceCode • String
            :   The alphanumeric code for the region. For example, ON.

            [Anchor to zip](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.zip)zip • String
            :   The zip or postal code of the address.

            [Anchor to market](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market)market • Market Deprecated
            :   Show fields

                [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.handle)handle • Handle! non-null
                :   A human-readable unique string for the market automatically generated from its title.

                [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.id)id • ID! non-null
                :   A globally-unique identifier.

                [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield)metafield • Metafield
                :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                    about a Shopify resource, such as products, orders, and
                    [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                    Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                    enables you to customize the checkout experience.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield.arguments.namespace)namespace • String
                    :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                        between different apps or different parts of the same app. If omitted, then the
                        [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                        is used.

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield.arguments.key)key • String! required
                    :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                        namespace and a key, in the format `namespace.key`.

                    ---

                    ### Fields

                    [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield.jsonValue)jsonValue • JSON! non-null
                    :   The data that's stored in the metafield, using JSON format.

                    [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield.type)type • String! non-null
                    :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                        the `value` field.

                    [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.metafield.value)value • String! non-null
                    :   The data that's stored in the metafield. The data is always stored as a string,
                        regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                [Anchor to regions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.regions)regions • [MarketRegion!]! non-null
                :   A geographic region which comprises a market.

                    Show fields

                    [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryAddress.market.regions.name)name • String
                    :   The name of the region in the language of the current localization.

        [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.handle)handle • Handle! non-null
        :   The fulfillment group handle.

        [Anchor to inventoryLocationHandles](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.inventoryLocationHandles)inventoryLocationHandles • [Handle!]! non-null
        :   A list of inventory location handles for the fulfillment group.

        [Anchor to lines](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines)lines • [CartLine!]! non-null
        :   A list of lines containing information about the items that are part of the fulfillment group.

            Show fields

            [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.attribute)attribute • Attribute
            :   The custom attributes associated with a cart to store additional information. Cart attributes
                allow you to collect specific information from customers on the **Cart** page, such as order notes,
                gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                Cart line attributes are equivalent to the
                [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                object in Liquid.

                Show arguments and fields

                ### Arguments

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.attribute.arguments.key)key • String
                :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                ---

                ### Fields

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.attribute.key)key • String! non-null
                :   The key or name of the attribute. For example, `"customer_first_order"`.

                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.attribute.value)value • String
                :   The value of the attribute. For example, `"true"`.

            [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost)cost • CartLineCost! non-null
            :   The cost of an item in a cart that the customer intends to purchase. Cart lines are entries in the customer's
                cart that represent a single unit of a product variant. For example, if a customer adds two different sizes of
                the same t-shirt to their cart, then each size is represented as a separate cart line.

                Show fields

                [Anchor to amountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.amountPerQuantity)amountPerQuantity • MoneyV2! non-null
                :   The cost of a single unit. For example, if a customer purchases three units of a product
                    that are priced at $10 each, then the `amountPerQuantity` is $10.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.amountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.amountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to compareAtAmountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.compareAtAmountPerQuantity)compareAtAmountPerQuantity • MoneyV2
                :   The `compareAt` price of a single unit before any discounts are applied. This field is used to calculate and display
                    savings for customers. For example, if a product's `compareAtAmountPerQuantity` is $25 and its current price
                    is $20, then the customer sees a $5 discount. This value can change based on the buyer's identity and is
                    `null` when the value is hidden from buyers.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.compareAtAmountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.compareAtAmountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to subtotalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
                :   The cost of items in the cart before applying any discounts to certain items.
                    This amount serves as the starting point for calculating any potential savings customers
                    might receive through promotions or discounts.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.subtotalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to totalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.totalAmount)totalAmount • MoneyV2! non-null
                :   The total cost of items in a cart.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.totalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.id)id • ID! non-null
            :   The ID of the cart line.

            [Anchor to merchandise](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise)merchandise • Merchandise! non-null
            :   The item that the customer intends to purchase.

                Show union types

                [Anchor to CustomProduct](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct) CustomProduct •OBJECT
                :   A custom product represents a product that doesn't map to Shopify's
                    [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                    For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                    information, or weight measurements and conversions.

                    Show fields

                    [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                    :   Whether the merchandise is a gift card.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct.title)title • String! non-null
                    :   The localized name for the product that displays to customers. The title is used to construct the product's
                        handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                        "Black Sunglasses", then the handle is `black-sunglasses`.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to ProductVariant](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant) ProductVariant •OBJECT
                :   A specific version of a product that comes in more than one option, such as size or color. For example,
                    if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                    product variant and a large, blue t-shirt would be another.

                    Show fields

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.id)id • ID! non-null
                    :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                        for the product variant.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to product](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product)product • Product! non-null
                    :   The product associated with the product variant. For example, if a
                        merchant sells t-shirts with options for size and color, then a small,
                        blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                        The product associated with the product variant would be the t-shirt itself.

                        Show fields

                        [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                        :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                            numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                            is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                        :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                            from the list to return `true`.

                            Show arguments

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with either the `sports` or `summer` tag.

                            ---

                        [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                        :   Whether the product is associated with the specified tags.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with both the `sports` and `summer` tags.

                            ---

                            ### Fields

                            [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                            :   Whether the Shopify resource has the tag.

                            [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                            :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                summer.

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product.

                        [Anchor to inAnyCollection](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                        :   Whether the product is in any of the specified collections. The product must be in at least one collection
                            from the list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                        [Anchor to inCollections](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                        :   Whether the product is in the specified collections. The product must be in all of the collections in the
                            list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                            ### Fields

                            [Anchor to collectionId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the collection.

                            [Anchor to isMember](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                            :   Whether the product is in the specified collection.

                        [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the product is a gift card.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to productType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.productType)productType • String
                        :   A custom category for a product. Product types allow merchants to define categories other than the
                            ones available in Shopify's
                            [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to vendor](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.product.vendor)vendor • String
                        :   The name of the product's vendor.

                    [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to sku](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.sku)sku • String
                    :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                        A product variant must have a SKU to be connected to a
                        [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                    [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.title)title • String
                    :   The localized name for the product variant that displays to customers.

                    [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

            [Anchor to parentRelationship](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.parentRelationship)parentRelationship • CartLineParentRelationship
            :   The [nested relationship](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines)
                between this line and its parent line, if any.

                Show fields

                [Anchor to parent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.parentRelationship.parent)parent • CartLine! non-null
                :   The parent line in the relationship.

            [Anchor to quantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.quantity)quantity • Int! non-null
            :   The quantity of the item that the customer intends to purchase.

            [Anchor to sellingPlanAllocation](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation)sellingPlanAllocation • SellingPlanAllocation
            :   The [selling plan](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans)
                associated with the cart line, including information about how a product variant can be sold and purchased.

                Show fields

                [Anchor to priceAdjustments](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments)priceAdjustments • [SellingPlanAllocationPriceAdjustment!]! non-null
                :   A list of price adjustments, with a maximum of two. When there are two, the first price adjustment goes into effect at the time of purchase, while the second one starts after a certain number of orders. A price adjustment represents how a selling plan affects pricing when a variant is purchased with a selling plan. Prices display in the customer's currency if the shop is configured for it.

                    Show fields

                    [Anchor to perDeliveryPrice](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice)perDeliveryPrice • MoneyV2! non-null
                    :   The effective price for a single delivery. For example, for a prepaid subscription plan that includes 6 deliveries at the price of $48.00, the per delivery price is $8.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to price](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.price)price • MoneyV2! non-null
                    :   The price of the variant when it's purchased with a selling plan For example, for a prepaid subscription plan that includes 6 deliveries of $10.00 granola, where the customer gets 20% off, the price is 6 x $10.00 x 0.80 = $48.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.price.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.priceAdjustments.price.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to sellingPlan](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan)sellingPlan • SellingPlan! non-null
                :   A representation of how products and variants can be sold and purchased. For example, an individual selling plan could be '6 weeks of prepaid granola, delivered weekly'.

                    Show fields

                    [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.description)description • String
                    :   The description of the selling plan.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.id)id • ID! non-null
                    :   A globally-unique identifier.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.name)name • String! non-null
                    :   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

                    [Anchor to recurringDeliveries](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.lines.sellingPlanAllocation.sellingPlan.recurringDeliveries)recurringDeliveries • Boolean! non-null
                    :   Whether purchasing the selling plan will result in multiple deliveries.

        [Anchor to deliveryGroup](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup)deliveryGroup • CartDeliveryGroup! non-nullDeprecated
        :   Show fields

            [Anchor to cartLines](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines)cartLines • [CartLine!]! non-null
            :   Information about items in a cart that a customer intends to purchase. A cart line is an entry in the
                customer's cart that represents a single unit of a product variant. For example, if a customer adds two
                different sizes of the same t-shirt to their cart, then each size is represented as a separate cart line.

                Show fields

                [Anchor to attribute](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.attribute)attribute • Attribute
                :   The custom attributes associated with a cart to store additional information. Cart attributes
                    allow you to collect specific information from customers on the **Cart** page, such as order notes,
                    gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                    Cart line attributes are equivalent to the
                    [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                    object in Liquid.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.attribute.arguments.key)key • String
                    :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                    ---

                    ### Fields

                    [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.attribute.key)key • String! non-null
                    :   The key or name of the attribute. For example, `"customer_first_order"`.

                    [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.attribute.value)value • String
                    :   The value of the attribute. For example, `"true"`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost)cost • CartLineCost! non-null
                :   The cost of an item in a cart that the customer intends to purchase. Cart lines are entries in the customer's
                    cart that represent a single unit of a product variant. For example, if a customer adds two different sizes of
                    the same t-shirt to their cart, then each size is represented as a separate cart line.

                    Show fields

                    [Anchor to amountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.amountPerQuantity)amountPerQuantity • MoneyV2! non-null
                    :   The cost of a single unit. For example, if a customer purchases three units of a product
                        that are priced at $10 each, then the `amountPerQuantity` is $10.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.amountPerQuantity.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.amountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to compareAtAmountPerQuantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.compareAtAmountPerQuantity)compareAtAmountPerQuantity • MoneyV2
                    :   The `compareAt` price of a single unit before any discounts are applied. This field is used to calculate and display
                        savings for customers. For example, if a product's `compareAtAmountPerQuantity` is $25 and its current price
                        is $20, then the customer sees a $5 discount. This value can change based on the buyer's identity and is
                        `null` when the value is hidden from buyers.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.compareAtAmountPerQuantity.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.compareAtAmountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to subtotalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
                    :   The cost of items in the cart before applying any discounts to certain items.
                        This amount serves as the starting point for calculating any potential savings customers
                        might receive through promotions or discounts.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.subtotalAmount.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to totalAmount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.totalAmount)totalAmount • MoneyV2! non-null
                    :   The total cost of items in a cart.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.totalAmount.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.id)id • ID! non-null
                :   The ID of the cart line.

                [Anchor to merchandise](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise)merchandise • Merchandise! non-null
                :   The item that the customer intends to purchase.

                    Show union types

                    [Anchor to CustomProduct](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct) CustomProduct •OBJECT
                    :   A custom product represents a product that doesn't map to Shopify's
                        [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                        For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                        information, or weight measurements and conversions.

                        Show fields

                        [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the merchandise is a gift card.

                        [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                        :   Whether the item needs to be shipped to the customer. For example, a
                            digital gift card doesn't need to be shipped, but a t-shirt does
                            need to be shipped.

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct.weight)weight • Float
                        :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                        [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                        :   The unit of measurement for weight.

                            Show enum values

                            GRAMS, KILOGRAMS, OUNCES, POUNDS

                    [Anchor to ProductVariant](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant) ProductVariant •OBJECT
                    :   A specific version of a product that comes in more than one option, such as size or color. For example,
                        if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                        product variant and a large, blue t-shirt would be another.

                        Show fields

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product variant.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to product](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product)product • Product! non-null
                        :   The product associated with the product variant. For example, if a
                            merchant sells t-shirts with options for size and color, then a small,
                            blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                            The product associated with the product variant would be the t-shirt itself.

                            Show fields

                            [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                            :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                                numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                                is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                            [Anchor to hasAnyTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                            :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                                from the list to return `true`.

                                Show arguments

                                ### Arguments

                                [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                                :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                    `"sports, summer"` returns products with either the `sports` or `summer` tag.

                                ---

                            [Anchor to hasTags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                            :   Whether the product is associated with the specified tags.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to tags](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                                :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                    `"sports, summer"` returns products with both the `sports` and `summer` tags.

                                ---

                                ### Fields

                                [Anchor to hasTag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                                :   Whether the Shopify resource has the tag.

                                [Anchor to tag](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                                :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                    a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                    summer.

                            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.id)id • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the product.

                            [Anchor to inAnyCollection](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                            :   Whether the product is in any of the specified collections. The product must be in at least one collection
                                from the list to return `true`.

                                A collection is a group of products that can be displayed in online stores and other sales channels in
                                categories, which makes it easy for customers to find them. For example, an athletics store might create
                                different collections for running attire and accessories.

                                Show arguments

                                ### Arguments

                                [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                                :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                    that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                                ---

                            [Anchor to inCollections](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                            :   Whether the product is in the specified collections. The product must be in all of the collections in the
                                list to return `true`.

                                A collection is a group of products that can be displayed in online stores and other sales channels in
                                categories, which makes it easy for customers to find them. For example, an athletics store might create
                                different collections for running attire and accessories.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to ids](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                                :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                    that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                                ---

                                ### Fields

                                [Anchor to collectionId](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                    for the collection.

                                [Anchor to isMember](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                                :   Whether the product is in the specified collection.

                            [Anchor to isGiftCard](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                            :   Whether the product is a gift card.

                            [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                                about a Shopify resource, such as products, orders, and
                                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                                enables you to customize the checkout experience.

                                Show arguments and fields

                                ### Arguments

                                [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                    between different apps or different parts of the same app. If omitted, then the
                                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                    is used.

                                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                    namespace and a key, in the format `namespace.key`.

                                ---

                                ### Fields

                                [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                                :   The data that's stored in the metafield, using JSON format.

                                [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                    the `value` field.

                                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                                :   The data that's stored in the metafield. The data is always stored as a string,
                                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                            [Anchor to productType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.productType)productType • String
                            :   A custom category for a product. Product types allow merchants to define categories other than the
                                ones available in Shopify's
                                [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                            [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.title)title • String! non-null
                            :   The localized name for the product that displays to customers. The title is used to construct the product's
                                handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                                "Black Sunglasses", then the handle is `black-sunglasses`.

                            [Anchor to vendor](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.product.vendor)vendor • String
                            :   The name of the product's vendor.

                        [Anchor to requiresShipping](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                        :   Whether the item needs to be shipped to the customer. For example, a
                            digital gift card doesn't need to be shipped, but a t-shirt does
                            need to be shipped.

                        [Anchor to sku](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.sku)sku • String
                        :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                            A product variant must have a SKU to be connected to a
                            [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                        [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.title)title • String
                        :   The localized name for the product variant that displays to customers.

                        [Anchor to weight](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.weight)weight • Float
                        :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                        [Anchor to weightUnit](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                        :   The unit of measurement for weight.

                            Show enum values

                            GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to parentRelationship](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.parentRelationship)parentRelationship • CartLineParentRelationship
                :   The [nested relationship](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines)
                    between this line and its parent line, if any.

                    Show fields

                    [Anchor to parent](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.parentRelationship.parent)parent • CartLine! non-null
                    :   The parent line in the relationship.

                [Anchor to quantity](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.quantity)quantity • Int! non-null
                :   The quantity of the item that the customer intends to purchase.

                [Anchor to sellingPlanAllocation](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation)sellingPlanAllocation • SellingPlanAllocation
                :   The [selling plan](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans)
                    associated with the cart line, including information about how a product variant can be sold and purchased.

                    Show fields

                    [Anchor to priceAdjustments](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments)priceAdjustments • [SellingPlanAllocationPriceAdjustment!]! non-null
                    :   A list of price adjustments, with a maximum of two. When there are two, the first price adjustment goes into effect at the time of purchase, while the second one starts after a certain number of orders. A price adjustment represents how a selling plan affects pricing when a variant is purchased with a selling plan. Prices display in the customer's currency if the shop is configured for it.

                        Show fields

                        [Anchor to perDeliveryPrice](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice)perDeliveryPrice • MoneyV2! non-null
                        :   The effective price for a single delivery. For example, for a prepaid subscription plan that includes 6 deliveries at the price of $48.00, the per delivery price is $8.00.

                            Show fields

                            [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.amount)amount • Decimal! non-null
                            :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                                currency. For example, 12.99.

                            [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.currencyCode)currencyCode • CurrencyCode! non-null
                            :   The three-letter currency code that represents a world currency used in a store. Currency codes
                                include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                                and non-standard codes. For example, USD.

                                Show enum values

                                AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                        [Anchor to price](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.price)price • MoneyV2! non-null
                        :   The price of the variant when it's purchased with a selling plan For example, for a prepaid subscription plan that includes 6 deliveries of $10.00 granola, where the customer gets 20% off, the price is 6 x $10.00 x 0.80 = $48.00.

                            Show fields

                            [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.price.amount)amount • Decimal! non-null
                            :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                                currency. For example, 12.99.

                            [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.priceAdjustments.price.currencyCode)currencyCode • CurrencyCode! non-null
                            :   The three-letter currency code that represents a world currency used in a store. Currency codes
                                include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                                and non-standard codes. For example, USD.

                                Show enum values

                                AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to sellingPlan](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan)sellingPlan • SellingPlan! non-null
                    :   A representation of how products and variants can be sold and purchased. For example, an individual selling plan could be '6 weeks of prepaid granola, delivered weekly'.

                        Show fields

                        [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.description)description • String
                        :   The description of the selling plan.

                        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.id)id • ID! non-null
                        :   A globally-unique identifier.

                        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.name)name • String! non-null
                        :   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

                        [Anchor to recurringDeliveries](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.cartLines.sellingPlanAllocation.sellingPlan.recurringDeliveries)recurringDeliveries • Boolean! non-null
                        :   Whether purchasing the selling plan will result in multiple deliveries.

            [Anchor to deliveryAddress](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress)deliveryAddress • MailingAddress
            :   The shipping or destination address associated with the delivery group.

                Show fields

                [Anchor to address1](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.address1)address1 • String
                :   The first line of the address. Typically the street address or PO Box number.

                [Anchor to address2](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.address2)address2 • String
                :   The second line of the address. Typically the number of the apartment, suite, or unit.

                [Anchor to city](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.city)city • String
                :   The name of the city, district, village, or town.

                [Anchor to company](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.company)company • String
                :   The name of the customer's company or organization.

                [Anchor to countryCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.countryCode)countryCode • CountryCode
                :   The two-letter code for the country of the address. For example, US.

                    Show enum values

                    AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AR, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MK, ML, MM, MN, MO, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PS, PT, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TA, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW, ZZ

                [Anchor to firstName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.firstName)firstName • String
                :   The first name of the customer.

                [Anchor to lastName](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.lastName)lastName • String
                :   The last name of the customer.

                [Anchor to latitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.latitude)latitude • Float
                :   The approximate latitude of the address.

                [Anchor to longitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.longitude)longitude • Float
                :   The approximate longitude of the address.

                [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.name)name • String
                :   The full name of the customer, based on firstName and lastName.

                [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.phone)phone • String
                :   A unique phone number for the customer. Formatted using E.164 standard. For example, +16135551111.

                [Anchor to provinceCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.provinceCode)provinceCode • String
                :   The alphanumeric code for the region. For example, ON.

                [Anchor to zip](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.zip)zip • String
                :   The zip or postal code of the address.

                [Anchor to market](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market)market • Market Deprecated
                :   Show fields

                    [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.handle)handle • Handle! non-null
                    :   A human-readable unique string for the market automatically generated from its title.

                    [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.id)id • ID! non-null
                    :   A globally-unique identifier.

                    [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to regions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.regions)regions • [MarketRegion!]! non-null
                    :   A geographic region which comprises a market.

                        Show fields

                        [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryAddress.market.regions.name)name • String
                        :   The name of the region in the language of the current localization.

            [Anchor to deliveryOptions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions)deliveryOptions • [CartDeliveryOption!]! non-null
            :   The delivery options available for the delivery group. Delivery options are the different ways that customers
                can choose to have their orders shipped. Examples include express shipping or standard shipping.

                Show fields

                [Anchor to code](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.code)code • String
                :   A unique identifier that represents the delivery option offered to customers.
                    For example, `Canada Post Expedited`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.cost)cost • MoneyV2! non-null
                :   The amount that the customer pays if they select the delivery option.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.cost.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.cost.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to deliveryMethodType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.deliveryMethodType)deliveryMethodType • DeliveryMethod! non-null
                :   The delivery method associated with the delivery option. A delivery method is a way that merchants can
                    fulfill orders from their online stores. Delivery methods include shipping to an address,
                    [local pickup](https://help.shopify.com/manual/fulfillment/setup/delivery-methods/pickup-in-store),
                    and shipping to a [pickup point](https://help.shopify.com/manual/fulfillment/shopify-shipping/pickup-points),
                    all of which are natively supported by Shopify checkout.

                    Show enum values

                    LOCAL, NONE, PICK\_UP, PICKUP\_POINT, RETAIL, SHIPPING

                [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.description)description • String
                :   A single-line description of the delivery option, with HTML tags removed.

                [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.handle)handle • Handle! non-null
                :   A unique, human-readable identifier of the delivery option's title.
                    A handle can contain letters, hyphens (`-`), and numbers, but not spaces.
                    For example, `standard-shipping`.

                [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.deliveryOptions.title)title • String
                :   The name of the delivery option that displays to customers. The title is used to construct the delivery
                    option's handle. For example, if a delivery option is titled "Standard Shipping", then the handle is
                    `standard-shipping`.

            [Anchor to groupType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.groupType)groupType • CartDeliveryGroupType! non-null
            :   The type of merchandise in the delivery group.

                Show enum values

                ONE\_TIME\_PURCHASE, SUBSCRIPTION

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.id)id • ID! non-null
            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                for the delivery group.

            [Anchor to selectedDeliveryOption](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption)selectedDeliveryOption • CartDeliveryOption
            :   Information about the delivery option that the customer has selected.

                Show fields

                [Anchor to code](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.code)code • String
                :   A unique identifier that represents the delivery option offered to customers.
                    For example, `Canada Post Expedited`.

                [Anchor to cost](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.cost)cost • MoneyV2! non-null
                :   The amount that the customer pays if they select the delivery option.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.cost.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.cost.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to deliveryMethodType](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.deliveryMethodType)deliveryMethodType • DeliveryMethod! non-null
                :   The delivery method associated with the delivery option. A delivery method is a way that merchants can
                    fulfill orders from their online stores. Delivery methods include shipping to an address,
                    [local pickup](https://help.shopify.com/manual/fulfillment/setup/delivery-methods/pickup-in-store),
                    and shipping to a [pickup point](https://help.shopify.com/manual/fulfillment/shopify-shipping/pickup-points),
                    all of which are natively supported by Shopify checkout.

                    Show enum values

                    LOCAL, NONE, PICK\_UP, PICKUP\_POINT, RETAIL, SHIPPING

                [Anchor to description](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.description)description • String
                :   A single-line description of the delivery option, with HTML tags removed.

                [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.handle)handle • Handle! non-null
                :   A unique, human-readable identifier of the delivery option's title.
                    A handle can contain letters, hyphens (`-`), and numbers, but not spaces.
                    For example, `standard-shipping`.

                [Anchor to title](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.deliveryGroup.selectedDeliveryOption.title)title • String
                :   The name of the delivery option that displays to customers. The title is used to construct the delivery
                    option's handle. For example, if a delivery option is titled "Standard Shipping", then the handle is
                    `standard-shipping`.

        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.fulfillmentGroups.id)id • ID! non-nullDeprecated

    [Anchor to localization](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization)localization • Localization! non-null
    :   The regional and language settings that determine how the Function
        handles currency, numbers, dates, and other locale-specific values
        during discount calculations. These settings are based on the store's configured
        [localization practices](https://shopify.dev/docs/apps/build/functions/localization-practices-shopify-functions).

        Show fields

        [Anchor to country](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.country)country • Country! non-null
        :   The country for which the store is customized, reflecting local preferences and regulations.
            Localization might influence the language, currency, and product offerings available in a store to enhance
            the shopping experience for customers in that region.

            Show fields

            [Anchor to isoCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.country.isoCode)isoCode • CountryCode! non-null
            :   The ISO code of the country.

                Show enum values

                AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AR, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MK, ML, MM, MN, MO, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PS, PT, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TA, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW, ZZ

        [Anchor to language](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.language)language • Language! non-null
        :   The language for which the store is customized, ensuring content is tailored to local customers.
            This includes product descriptions and customer communications that resonate with the target audience.

            Show fields

            [Anchor to isoCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.language.isoCode)isoCode • LanguageCode! non-null
            :   The ISO code.

                Show enum values

                AF, AK, AM, AR, AS, AZ, BE, BG, BM, BN, BO, BR, BS, CA, CE, CKB, CS, CU, CY, DA, DE, DZ, EE, EL, EN, EO, ES, ET, EU, FA, FF, FI, FIL, FO, FR, FY, GA, GD, GL, GU, GV, HA, HE, HI, HR, HU, HY, IA, ID, IG, II, IS, IT, JA, JV, KA, KI, KK, KL, KM, KN, KO, KS, KU, KW, KY, LB, LG, LN, LO, LT, LU, LV, MG, MI, MK, ML, MN, MR, MS, MT, MY, NB, ND, NE, NL, NN, NO, OM, OR, OS, PA, PL, PS, PT, PT\_BR, PT\_PT, QU, RM, RN, RO, RU, RW, SA, SC, SD, SE, SG, SI, SK, SL, SN, SO, SQ, SR, SU, SV, SW, TA, TE, TG, TH, TI, TK, TO, TR, TT, UG, UK, UR, UZ, VI, VO, WO, XH, YI, YO, ZH, ZH\_CN, ZH\_TW, ZU

        [Anchor to market](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market)market • Market! non-nullDeprecated
        :   Show fields

            [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.handle)handle • Handle! non-null
            :   A human-readable unique string for the market automatically generated from its title.

            [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.id)id • ID! non-null
            :   A globally-unique identifier.

            [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield)metafield • Metafield
            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                about a Shopify resource, such as products, orders, and
                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                enables you to customize the checkout experience.

                Show arguments and fields

                ### Arguments

                [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield.arguments.namespace)namespace • String
                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                    between different apps or different parts of the same app. If omitted, then the
                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                    is used.

                [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield.arguments.key)key • String! required
                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                    namespace and a key, in the format `namespace.key`.

                ---

                ### Fields

                [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield.jsonValue)jsonValue • JSON! non-null
                :   The data that's stored in the metafield, using JSON format.

                [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield.type)type • String! non-null
                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                    the `value` field.

                [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.metafield.value)value • String! non-null
                :   The data that's stored in the metafield. The data is always stored as a string,
                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

            [Anchor to regions](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.regions)regions • [MarketRegion!]! non-null
            :   A geographic region which comprises a market.

                Show fields

                [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.localization.market.regions.name)name • String
                :   The name of the region in the language of the current localization.

    [Anchor to locationRule](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule)locationRule • OrderRoutingLocationRule! non-null
    :   The backend logic that the Function uses to
        [route orders](https://help.shopify.com/manual/fulfillment/setup/order-routing/understanding-order-routing).
        It includes the [metafields](https://shopify.dev/docs/apps/build/custom-data)
        that are associated with the customization.

        Show fields

        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locationRule.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

    [Anchor to locations](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations)locations • [Location!]! non-null
    :   A list of all geographical locations where the inventory is stored,
        including warehouses, retail locations, and distribution centers.
        The list captures the locations that can fulfill items in the cart.

        Show fields

        [Anchor to address](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address)address • LocationAddress! non-null
        :   The address of this location.

            Show fields

            [Anchor to address1](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.address1)address1 • String
            :   The first line of the address for the location.

            [Anchor to address2](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.address2)address2 • String
            :   The second line of the address for the location.

            [Anchor to city](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.city)city • String
            :   The city of the location.

            [Anchor to country](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.country)country • String
            :   The country of the location.

            [Anchor to countryCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.countryCode)countryCode • String
            :   The country code of the location.

            [Anchor to formatted](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.formatted)formatted • [String!]! non-null
            :   A formatted version of the address for the location.

            [Anchor to latitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.latitude)latitude • Float
            :   The approximate latitude coordinates of the location.

            [Anchor to longitude](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.longitude)longitude • Float
            :   The approximate longitude coordinates of the location.

            [Anchor to phone](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.phone)phone • String
            :   The phone number of the location.

            [Anchor to province](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.province)province • String
            :   The province of the location.

            [Anchor to provinceCode](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.provinceCode)provinceCode • String
            :   The code for the province, state, or district of the address of the location.

            [Anchor to zip](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.address.zip)zip • String
            :   The ZIP code of the location.

        [Anchor to handle](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.handle)handle • Handle! non-null
        :   The location handle.

        [Anchor to id](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.id)id • ID! non-null
        :   The location id.

        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

        [Anchor to name](/docs/api/functions/latest/order-routing-location-rule#Input.fields.locations.name)name • String! non-null
        :   The name of the location.

    [Anchor to presentmentCurrencyRate](/docs/api/functions/latest/order-routing-location-rule#Input.fields.presentmentCurrencyRate)presentmentCurrencyRate • Decimal! non-null
    :   The exchange rate used to convert discounts between the shop's default
        currency and the currency that displays to the customer during checkout.
        For example, if a store operates in USD but a customer is viewing discounts in EUR,
        then the presentment currency rate handles this conversion for accurate pricing.

    [Anchor to shop](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop)shop • Shop! non-null
    :   Information about the shop where the Function is running, including the shop's timezone
        setting and associated [metafields](https://shopify.dev/docs/apps/build/custom-data).

        Show fields

        [Anchor to localTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime)localTime • LocalTime! non-null
        :   The current time based on the
            [store's timezone setting](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-business-settings).

            Show fields

            [Anchor to date](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.date)date • Date! non-null
            :   The current date relative to the parent object.

            [Anchor to dateTimeAfter](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeAfter)dateTimeAfter • Boolean! non-null
            :   Returns true if the current date and time is at or past the given date and time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to dateTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeAfter.arguments.dateTime)dateTime • DateTimeWithoutTimezone! required
                :   The date and time to compare against, assumed to be in the timezone of the parent object.

                ---

            [Anchor to dateTimeBefore](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeBefore)dateTimeBefore • Boolean! non-null
            :   Returns true if the current date and time is before the given date and time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to dateTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeBefore.arguments.dateTime)dateTime • DateTimeWithoutTimezone! required
                :   The date and time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to dateTimeBetween](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeBetween)dateTimeBetween • Boolean! non-null
            :   Returns true if the current date and time is between the two given date and times, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to startDateTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeBetween.arguments.startDateTime)startDateTime • DateTimeWithoutTimezone! required
                :   The lower bound time to compare against, assumed to be in the timezone of the parent timezone.

                [Anchor to endDateTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.dateTimeBetween.arguments.endDateTime)endDateTime • DateTimeWithoutTimezone! required
                :   The upper bound time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeAfter](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeAfter)timeAfter • Boolean! non-null
            :   Returns true if the current time is at or past the given time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to time](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeAfter.arguments.time)time • TimeWithoutTimezone! required
                :   The time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeBefore](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeBefore)timeBefore • Boolean! non-null
            :   Returns true if the current time is at or past the given time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to time](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeBefore.arguments.time)time • TimeWithoutTimezone! required
                :   The time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeBetween](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeBetween)timeBetween • Boolean! non-null
            :   Returns true if the current time is between the two given times, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to startTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeBetween.arguments.startTime)startTime • TimeWithoutTimezone! required
                :   The lower bound time to compare against, assumed to be in the timezone of the parent timezone.

                [Anchor to endTime](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.localTime.timeBetween.arguments.endTime)endTime • TimeWithoutTimezone! required
                :   The upper bound time to compare against, assumed to be in the timezone of the parent timezone.

                ---

        [Anchor to metafield](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/order-routing-location-rule#Input.fields.shop.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

#### [Anchor to Run function](/docs/api/functions/latest/order-routing-location-rule#run-function)Run function

The logic that processes the input data. The function generates a list of operations that rank locations. Each location
is associated with a fulfillment group.

Each operation specifies how to rank locations. Shopify processes your response to determine how to best fulfill and
ship orders.

This return must follow the schema defined in the `CartFulfillmentGroupsLocationRankingsGenerateRunResult` object.

* CartFulfillmentGroupsLocationRankingsGenerateRunResult

[Anchor to CartFulfillmentGroupsLocationRankingsGenerateRunResult](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult)CartFulfillmentGroupsLocationRankingsGenerateRunResult OBJECT
:   The `CartFulfillmentGroupsLocationRankingsGenerateRunResult` object is the output of the function run target. The object contains the operations that rank
    locations for each fulfillment group.

    Hide fields

    [Anchor to operations](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations)operations • [Operation!]! non-null
    :   The ordered list of operations that rank locations for each fulfillment group,
        which includes one or more items to be shipped together.
        The locations with the highest ranking are selected to fulfill the order.

        Hide fields

        [Anchor to fulfillmentGroupLocationRankingAdd](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations.fulfillmentGroupLocationRankingAdd)fulfillmentGroupLocationRankingAdd • FulfillmentGroupLocationRankingAddOperation
        :   A request to rank the locations associated with a fulfillment group.
            The ranking determines the priority in which the locations are selected to fulfill the order.

            Hide fields

            [Anchor to fulfillmentGroupHandle](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations.fulfillmentGroupLocationRankingAdd.fulfillmentGroupHandle)fulfillmentGroupHandle • Handle! non-null
            :   The identifier for the fulfillment group.

            [Anchor to rankings](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations.fulfillmentGroupLocationRankingAdd.rankings)rankings • [RankedLocation!]! non-null
            :   The ranked locations for this fulfillment group.

                Show fields

                [Anchor to locationHandle](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations.fulfillmentGroupLocationRankingAdd.rankings.locationHandle)locationHandle • Handle! non-null
                :   The location handle.

                [Anchor to rank](/docs/api/functions/latest/order-routing-location-rule#CartFulfillmentGroupsLocationRankingsGenerateRunResult.fields.operations.fulfillmentGroupLocationRankingAdd.rankings.rank)rank • Int! non-null
                :   The location's rank.

Was this section helpful?

YesNo

---

## [Anchor to How fulfillment groups are ranked](/docs/api/functions/latest/order-routing-location-rule#how-fulfillment-groups-are-ranked)How fulfillment groups are ranked

For each fulfillment group, Shopify first sorts the output of each function based on the `locationRule` priority.
Shopify then takes the first output, and sorts the locations of the fulfillment group based on the rank.

If there are ties between the rankings, then Shopify breaks them using the ranks from the second output, and so on.
If there are no ties, then only the output of the first `locationRule` is considered.

Was this section helpful?

YesNo

---

## [Anchor to Additional resources](/docs/api/functions/latest/order-routing-location-rule#additional-resources)Additional resources

Explore comprehensive guides and references to help you build, deploy, and optimize your Shopify Functions.

### [Anchor to Working with Functions](/docs/api/functions/latest/order-routing-location-rule#working-with-functions)Working with Functions

These guides cover essential concepts for building Shopify Functions effectively. Learn how functions process data, execute during checkout, and handle versioning, localization, and external APIs.

[![](/images/icons/48/pickaxe-3.png)![](/images/icons/48/pickaxe-3-dark.png)

Function anatomy

Explore how functions process input data and generate operations.

Function anatomy

Explore how functions process input data and generate operations.](/docs/api/functions/current#function-anatomy)

[Function anatomy  
  

Explore how functions process input data and generate operations.](/docs/api/functions/current#function-anatomy)

[![](/images/icons/48/hearts.png)![](/images/icons/48/hearts-dark.png)

Execution order in checkout

Learn when Function APIs execute during the checkout process.

Execution order in checkout

Learn when Function APIs execute during the checkout process.](/docs/api/functions/current#function-execution-order-in-checkout)

[Execution order in checkout  
  

Learn when Function APIs execute during the checkout process.](/docs/api/functions/current#function-execution-order-in-checkout)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Schema and versioning

Understand schema versioning, release and upgrade requirements.

Schema and versioning

Understand schema versioning, release and upgrade requirements.](/docs/api/functions/current#graphql-schema-and-versioning)

[Schema and versioning  
  

Understand schema versioning, release and upgrade requirements.](/docs/api/functions/current#graphql-schema-and-versioning)

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)

API availability

Check which Shopify plans support functions in custom apps.

API availability

Check which Shopify plans support functions in custom apps.](/docs/api/functions/current#api-availability)

[API availability  
  

Check which Shopify plans support functions in custom apps.](/docs/api/functions/current#api-availability)

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)

Localization practices

Localize functions for international markets.

Localization practices

Localize functions for international markets.](/docs/apps/build/functions/localization-practices-shopify-functions)

[Localization practices  
  

Localize functions for international markets.](/docs/apps/build/functions/localization-practices-shopify-functions)

### [Anchor to Performance and troubleshooting](/docs/api/functions/latest/order-routing-location-rule#performance-and-troubleshooting)Performance and troubleshooting

Optimize function performance and ensure reliable operation from development through production deployment.

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Resource limits and performance

Understand function performance requirements and resource limitations for optimal execution.

Resource limits and performance

Understand function performance requirements and resource limitations for optimal execution.](/docs/api/functions/current#resource-limits-and-performance)

[Resource limits and performance  
  

Understand function performance requirements and resource limitations for optimal execution.](/docs/api/functions/current#resource-limits-and-performance)

[![](/images/icons/48/industries.png)![](/images/icons/48/industries-dark.png)

Test and debug Shopify Functions

Explore comprehensive testing workflows from local development to production deployment.

Test and debug Shopify Functions

Explore comprehensive testing workflows from local development to production deployment.](/docs/apps/build/functions/test-debug-functions)

[Test and debug Shopify Functions](/docs/apps/build/functions/test-debug-functions)

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-dark.png)

Considerations for programming languages

Choose languages that compile to WebAssembly for optimal function performance.

Considerations for programming languages

Choose languages that compile to WebAssembly for optimal function performance.](/docs/apps/build/functions/programming-languages)

[Considerations for programming languages  
  

Choose languages that compile to WebAssembly for optimal function performance.](/docs/apps/build/functions/programming-languages)

[![](/images/icons/48/flag.png)![](/images/icons/48/flag-dark.png)

Monitoring and handling errors in production

Master testing and debugging workflows for reliable function development.

Monitoring and handling errors in production

Master testing and debugging workflows for reliable function development.](/docs/apps/build/functions/monitoring-and-errors)

[Monitoring and handling errors in production  
  

Master testing and debugging workflows for reliable function development.](/docs/apps/build/functions/monitoring-and-errors)

Was this section helpful?

YesNo