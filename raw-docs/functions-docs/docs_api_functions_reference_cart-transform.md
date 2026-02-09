---
source: https://shopify.dev/docs/api/functions/reference/cart-transform
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

A cart represents the merchandise that a customer intends to purchase, and the estimated cost associated with the cart. Transforming a cart refers to
changing the pricing and presentation of items in a cart. To modify the appearance of cart items, such as updating titles and images, changing prices,
and bundling items, you can only use the Cart Transform API.

[Shopify Functions](/docs/api/functions/current) enable you to customize Shopify's backend logic. The Cart Transform API integrates this logic into the checkout flow.

Use the API to add [product bundles](/docs/apps/build/product-merchandising/bundles) to a store or break down bundled products into individual components, with associated
data such as buyer identity, quantity, cost, and subscription information.

Note

You can install a maximum of one cart transform function on each store.

**Note:**

You can install a maximum of one cart transform function on each store.

### [Anchor to Use cases](/docs/api/functions/latest/cart-transform#use-cases)Use cases

* Expand a cart line item to display the bundled items it contains.
* Merge multiple cart lines into a single line that represents a bundle.
* Update the presentation of line items in a cart to override their price, title, or image.

Note

Only [development stores](/docs/api/development-stores) or stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use apps with `lineUpdate` operations.

**Note:**

Only [development stores](/docs/api/development-stores) or stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use apps with `lineUpdate` operations.

Note

Only [development stores](/docs/api/development-stores) or stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use apps with `update` operations.

**Note:**

Only [development stores](/docs/api/development-stores) or stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use apps with `update` operations.

Compatibility with Shopify surfaces

Supported (7)

Partially supported (2)

Unsupported (5)

* [B2B](https://shopify.dev/docs/apps/build/b2b): Supported
* [Cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart): Supported
* [Checkout](https://shopify.dev/docs/apps/build/checkout): Partially supported

  Shopify rejects `lineExpand`, `linesMerge`, and `lineUpdate` operations if a [selling plan](/docs/apps/build/purchase-options/subscriptions/selling-plans) is present.
* [Create Order API](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCreate): Not supported
* [Draft Order (Admin)](https://shopify.dev/docs/apps/build/b2b/draft-orders): Supported
* [Draft Order (Checkout)](https://shopify.dev/docs/apps/build/b2b/draft-orders): Supported
* [Order Edit (Admin)](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders): Not supported
* [Order Edit (Checkout)](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders): Not supported
* [POS](https://shopify.dev/docs/apps/build/pos): Partially supported

  `ProductVariant.requiresComponents` boolean has to be `true` for complete cartTransform support on POS.
* [Pre-order and Try Before You Buy](https://shopify.dev/docs/apps/build/purchase-options/deferred): Not supported
* [Shopify Admin](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries#creating-your-merchant-interface): Supported
* [Storefront](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/): Supported
* [Storefront Accelerated Checkout](https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout): Supported
* [Subscription (Recurring Orders)](https://shopify.dev/docs/apps/build/purchase-options/subscriptions): Not supported

Was this section helpful?

YesNo

---

## [Anchor to Getting started](/docs/api/functions/latest/cart-transform#getting-started)Getting started

Scaffolding the function using [Shopify CLI](/docs/api/shopify-cli) will automatically configure your TOML file.
You can alter the default [configuration](/docs/api/functions/2026-01#configuration) to customize the
way your function operates.

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

TutorialBuild a cart transform function

Tutorial

Build a cart transform function](/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

[Tutorial - Build a cart transform function](/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

Was this section helpful?

YesNo

---

## [Anchor to Targets](/docs/api/functions/latest/cart-transform#targets)Targets

A [target](/docs/apps/build/app-extensions/configure-app-extensions#targets) is an identifier in `shopify.extension.toml` that specifies where you're injecting code into Shopify Functions
APIs, or other parts of the Shopify platform. Each target is composed of three to four namespaces. The name begins with
a broad Shopify context and ends with the behavior of the extensible element.

---

### [Anchor to Run target](/docs/api/functions/latest/cart-transform#run-target)Run target

`cart.transform.run`

The run target modifies the pricing and presentation of items in a cart either using Shopify data or hardcoded values.
The target returns a list of operations to be applied to cart line items.

For example, you might use this to automatically add a warranty when a specific product is added to a cart.

* Input

[Anchor to Input](/docs/api/functions/latest/cart-transform#Input)Input OBJECT
:   The `Input` object is the complete GraphQL schema that your function can query as input to customize the presentation of
    items in a cart. Your function receives only the fields that you request in the input query. To optimize performance,
    we highly recommend that you request only the fields that your function requires.

    Hide fields

    [Anchor to cart](/docs/api/functions/latest/cart-transform#Input.fields.cart)cart • Cart! non-null
    :   The cart where the Function is running. A cart contains the merchandise that a customer intends to purchase
        and information about the customer, such as the customer's email address and phone number.

        Show fields

        [Anchor to attribute](/docs/api/functions/latest/cart-transform#Input.fields.cart.attribute)attribute • Attribute
        :   The custom attributes associated with a cart to store additional information. Cart attributes
            allow you to collect specific information from customers on the **Cart** page, such as order notes,
            gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

            Show arguments and fields

            ### Arguments

            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.attribute.arguments.key)key • String
            :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

            ---

            ### Fields

            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.attribute.key)key • String! non-null
            :   The key or name of the attribute. For example, `"customer_first_order"`.

            [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.attribute.value)value • String
            :   The value of the attribute. For example, `"true"`.

        [Anchor to buyerIdentity](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity)buyerIdentity • BuyerIdentity
        :   Information about the customer that's interacting with the cart. It includes details such as the
            customer's email and phone number, and the total amount of money the customer has spent in the store.
            This information helps personalize the checkout experience and ensures that accurate pricing and delivery options
            are displayed to customers.

            Show fields

            [Anchor to customer](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer)customer • Customer
            :   The [customer](https://help.shopify.com/manual/customers/manage-customers) that's interacting with the cart.

                Show fields

                [Anchor to amountSpent](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.amountSpent)amountSpent • MoneyV2! non-null
                :   The total amount that the customer has spent on orders.
                    The amount is converted from the shop's currency to the currency of the cart using a market rate.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.amountSpent.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.amountSpent.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to displayName](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.displayName)displayName • String! non-null
                :   The full name of the customer, based on the values for `firstName` and `lastName`.
                    If `firstName` and `lastName` aren't specified, then the value is the customer's email address.
                    If the email address isn't specified, then the value is the customer's phone number.

                [Anchor to email](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.email)email • String
                :   The customer's email address.

                [Anchor to firstName](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.firstName)firstName • String
                :   The customer's first name.

                [Anchor to hasAnyTag](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasAnyTag)hasAnyTag • Boolean! non-null
                :   Whether the customer is associated with any of the specified tags. The customer must have at least one tag
                    from the list to return `true`.

                    Show arguments

                    ### Arguments

                    [Anchor to tags](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                    :   A comma-separated list of searchable keywords that are associated with the customer. For example,
                        `"VIP, Gold"` returns customers with either the `VIP` or `Gold` tag.

                    ---

                [Anchor to hasTags](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasTags)hasTags • [HasTagResponse!]! non-null
                :   Whether the customer is associated with the specified tags.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to tags](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                    :   A comma-separated list of searchable keywords that are associated with the customer. For example,
                        `"VIP, Gold"` returns customers with both the `VIP` and `Gold` tags.

                    ---

                    ### Fields

                    [Anchor to hasTag](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasTags.hasTag)hasTag • Boolean! non-null
                    :   Whether the Shopify resource has the tag.

                    [Anchor to tag](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.hasTags.tag)tag • String! non-null
                    :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                        a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                        summer.

                [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.id)id • ID! non-null
                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                    for the customer.

                [Anchor to lastName](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.lastName)lastName • String
                :   The customer's last name.

                [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield)metafield • Metafield
                :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                    about a Shopify resource, such as products, orders, and
                    [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                    Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                    enables you to customize the checkout experience.

                    Show arguments and fields

                    ### Arguments

                    [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield.arguments.namespace)namespace • String
                    :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                        between different apps or different parts of the same app. If omitted, then the
                        [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                        is used.

                    [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield.arguments.key)key • String! required
                    :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                        namespace and a key, in the format `namespace.key`.

                    ---

                    ### Fields

                    [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield.jsonValue)jsonValue • JSON! non-null
                    :   The data that's stored in the metafield, using JSON format.

                    [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield.type)type • String! non-null
                    :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                        the `value` field.

                    [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.metafield.value)value • String! non-null
                    :   The data that's stored in the metafield. The data is always stored as a string,
                        regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                [Anchor to numberOfOrders](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.customer.numberOfOrders)numberOfOrders • Int! non-null
                :   The total number of orders that the customer has made at the store.

            [Anchor to email](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.email)email • String
            :   The email address of the customer that's interacting with the cart.

            [Anchor to isAuthenticated](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.isAuthenticated)isAuthenticated • Boolean! non-null
            :   Whether the customer is authenticated through their
                [customer account](https://help.shopify.com/manual/customers/customer-accounts).

            [Anchor to phone](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.phone)phone • String
            :   The phone number of the customer that's interacting with the cart.

            [Anchor to purchasingCompany](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany)purchasingCompany • PurchasingCompany
            :   The company of a B2B customer that's interacting with the cart.
                Used to manage and track purchases made by businesses rather than individual customers.

                Show fields

                [Anchor to company](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company)company • Company! non-null
                :   The company associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company was created in Shopify.

                    [Anchor to externalId](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.externalId)externalId • String
                    :   A unique externally-supplied ID for the company.

                    [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.name)name • String! non-null
                    :   The name of the company.

                    [Anchor to updatedAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.company.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company was last modified.

                [Anchor to contact](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact)contact • CompanyContact
                :   The company contact associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company contact was created in Shopify.

                    [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to locale](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact.locale)locale • String
                    :   The company contact's locale (language).

                    [Anchor to title](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact.title)title • String
                    :   The company contact's job title.

                    [Anchor to updatedAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.contact.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company contact was last modified.

                [Anchor to location](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location)location • CompanyLocation! non-null
                :   The company location associated to the order or draft order.

                    Show fields

                    [Anchor to createdAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.createdAt)createdAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company location was created in Shopify.

                    [Anchor to externalId](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.externalId)externalId • String
                    :   A unique externally-supplied ID for the company.

                    [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.id)id • ID! non-null
                    :   The ID of the company.

                    [Anchor to locale](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.locale)locale • String
                    :   The preferred locale of the company location.

                    [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.name)name • String! non-null
                    :   The name of the company location.

                    [Anchor to ordersCount](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.ordersCount)ordersCount • Int! non-null
                    :   The number of orders placed at this company location.

                    [Anchor to totalSpent](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent)totalSpent • MoneyV2! non-null
                    :   The total amount spent at this company location.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.totalSpent.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to updatedAt](/docs/api/functions/latest/cart-transform#Input.fields.cart.buyerIdentity.purchasingCompany.location.updatedAt)updatedAt • DateTime! non-null
                    :   The date and time ([ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601)) at which the company location was last modified.

        [Anchor to lines](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines)lines • [CartLine!]! non-null
        :   The items in a cart that the customer intends to purchase. A cart line is an entry in the
            customer's cart that represents a single unit of a product variant. For example, if a customer adds two
            different sizes of the same t-shirt to their cart, then each size is represented as a separate cart line.

            Show fields

            [Anchor to attribute](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.attribute)attribute • Attribute
            :   The custom attributes associated with a cart to store additional information. Cart attributes
                allow you to collect specific information from customers on the **Cart** page, such as order notes,
                gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                Cart line attributes are equivalent to the
                [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
                object in Liquid.

                Show arguments and fields

                ### Arguments

                [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.attribute.arguments.key)key • String
                :   The key of the cart attribute to retrieve. For example, `"gift_wrapping"`.

                ---

                ### Fields

                [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.attribute.key)key • String! non-null
                :   The key or name of the attribute. For example, `"customer_first_order"`.

                [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.attribute.value)value • String
                :   The value of the attribute. For example, `"true"`.

            [Anchor to cost](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost)cost • CartLineCost! non-null
            :   The cost of an item in a cart that the customer intends to purchase. Cart lines are entries in the customer's
                cart that represent a single unit of a product variant. For example, if a customer adds two different sizes of
                the same t-shirt to their cart, then each size is represented as a separate cart line.

                Show fields

                [Anchor to amountPerQuantity](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.amountPerQuantity)amountPerQuantity • MoneyV2! non-null
                :   The cost of a single unit. For example, if a customer purchases three units of a product
                    that are priced at $10 each, then the `amountPerQuantity` is $10.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.amountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.amountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to compareAtAmountPerQuantity](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.compareAtAmountPerQuantity)compareAtAmountPerQuantity • MoneyV2
                :   The `compareAt` price of a single unit before any discounts are applied. This field is used to calculate and display
                    savings for customers. For example, if a product's `compareAtAmountPerQuantity` is $25 and its current price
                    is $20, then the customer sees a $5 discount. This value can change based on the buyer's identity and is
                    `null` when the value is hidden from buyers.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.compareAtAmountPerQuantity.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.compareAtAmountPerQuantity.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to subtotalAmount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.subtotalAmount)subtotalAmount • MoneyV2! non-null
                :   The cost of items in the cart before applying any discounts to certain items.
                    This amount serves as the starting point for calculating any potential savings customers
                    might receive through promotions or discounts.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.subtotalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.subtotalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to totalAmount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.totalAmount)totalAmount • MoneyV2! non-null
                :   The total cost of items in a cart.

                    Show fields

                    [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.totalAmount.amount)amount • Decimal! non-null
                    :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                        currency. For example, 12.99.

                    [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.cost.totalAmount.currencyCode)currencyCode • CurrencyCode! non-null
                    :   The three-letter currency code that represents a world currency used in a store. Currency codes
                        include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                        and non-standard codes. For example, USD.

                        Show enum values

                        AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

            [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.id)id • ID! non-null
            :   The ID of the cart line.

            [Anchor to merchandise](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise)merchandise • Merchandise! non-null
            :   The item that the customer intends to purchase.

                Show union types

                [Anchor to CustomProduct](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct) CustomProduct •OBJECT
                :   A custom product represents a product that doesn't map to Shopify's
                    [standard product categories](https://help.shopify.com/manual/products/details/product-type).
                    For example, you can use a custom product to manage gift cards, shipping requirements, localized product
                    information, or weight measurements and conversions.

                    Show fields

                    [Anchor to isGiftCard](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct.isGiftCard)isGiftCard • Boolean! non-null
                    :   Whether the merchandise is a gift card.

                    [Anchor to requiresShipping](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to title](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct.title)title • String! non-null
                    :   The localized name for the product that displays to customers. The title is used to construct the product's
                        handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                        "Black Sunglasses", then the handle is `black-sunglasses`.

                    [Anchor to weight](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.CustomProduct.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

                [Anchor to ProductVariant](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant) ProductVariant •OBJECT
                :   A specific version of a product that comes in more than one option, such as size or color. For example,
                    if a merchant sells t-shirts with options for size and color, then a small, blue t-shirt would be one
                    product variant and a large, blue t-shirt would be another.

                    Show fields

                    [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.id)id • ID! non-null
                    :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                        for the product variant.

                    [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to product](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product)product • Product! non-null
                    :   The product associated with the product variant. For example, if a
                        merchant sells t-shirts with options for size and color, then a small,
                        blue t-shirt would be one product variant and a large, blue t-shirt would be another.
                        The product associated with the product variant would be the t-shirt itself.

                        Show fields

                        [Anchor to handle](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.handle)handle • Handle! non-null
                        :   A unique, human-readable string of the product's title. A handle can contain letters, hyphens (`-`), and
                            numbers, but not spaces. The handle is used in the online store URL for the product. For example, if a product
                            is titled "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to hasAnyTag](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasAnyTag)hasAnyTag • Boolean! non-null
                        :   Whether the product is associated with any of the specified tags. The product must have at least one tag
                            from the list to return `true`.

                            Show arguments

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasAnyTag.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with either the `sports` or `summer` tag.

                            ---

                        [Anchor to hasTags](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags)hasTags • [HasTagResponse!]! non-null
                        :   Whether the product is associated with the specified tags.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to tags](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.arguments.tags)tags • [String!]! requiredDefault:[]
                            :   A comma-separated list of searchable keywords that are associated with the product. For example,
                                `"sports, summer"` returns products with both the `sports` and `summer` tags.

                            ---

                            ### Fields

                            [Anchor to hasTag](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.hasTag)hasTag • Boolean! non-null
                            :   Whether the Shopify resource has the tag.

                            [Anchor to tag](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.hasTags.tag)tag • String! non-null
                            :   A searchable keyword that's associated with a Shopify resource, such as a product or customer. For example,
                                a merchant might apply the `sports` and `summer` tags to products that are associated with sportswear for
                                summer.

                        [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.id)id • ID! non-null
                        :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                            for the product.

                        [Anchor to inAnyCollection](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inAnyCollection)inAnyCollection • Boolean! non-null
                        :   Whether the product is in any of the specified collections. The product must be in at least one collection
                            from the list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inAnyCollection.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                        [Anchor to inCollections](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections)inCollections • [CollectionMembership!]! non-null
                        :   Whether the product is in the specified collections. The product must be in all of the collections in the
                            list to return `true`.

                            A collection is a group of products that can be displayed in online stores and other sales channels in
                            categories, which makes it easy for customers to find them. For example, an athletics store might create
                            different collections for running attire and accessories.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to ids](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.arguments.ids)ids • [ID!]! requiredDefault:[]
                            :   A comma-separated list of [globally-unique collection IDs](https://shopify.dev/docs/api/usage/gids)
                                that are associated with the product. For example, `gid://shopify/Collection/123`, `gid://shopify/Collection/456`.

                            ---

                            ### Fields

                            [Anchor to collectionId](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.collectionId)collectionId • ID! non-null
                            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                                for the collection.

                            [Anchor to isMember](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.inCollections.isMember)isMember • Boolean! non-null
                            :   Whether the product is in the specified collection.

                        [Anchor to isGiftCard](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.isGiftCard)isGiftCard • Boolean! non-null
                        :   Whether the product is a gift card.

                        [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield)metafield • Metafield
                        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                            about a Shopify resource, such as products, orders, and
                            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                            enables you to customize the checkout experience.

                            Show arguments and fields

                            ### Arguments

                            [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.arguments.namespace)namespace • String
                            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                                between different apps or different parts of the same app. If omitted, then the
                                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                                is used.

                            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.arguments.key)key • String! required
                            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                                namespace and a key, in the format `namespace.key`.

                            ---

                            ### Fields

                            [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.jsonValue)jsonValue • JSON! non-null
                            :   The data that's stored in the metafield, using JSON format.

                            [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.type)type • String! non-null
                            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                                the `value` field.

                            [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.metafield.value)value • String! non-null
                            :   The data that's stored in the metafield. The data is always stored as a string,
                                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                        [Anchor to productType](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.productType)productType • String
                        :   A custom category for a product. Product types allow merchants to define categories other than the
                            ones available in Shopify's
                            [standard product categories](https://help.shopify.com/manual/products/details/product-type).

                        [Anchor to title](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.title)title • String! non-null
                        :   The localized name for the product that displays to customers. The title is used to construct the product's
                            handle, which is a unique, human-readable string of the product's title. For example, if a product is titled
                            "Black Sunglasses", then the handle is `black-sunglasses`.

                        [Anchor to vendor](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.product.vendor)vendor • String
                        :   The name of the product's vendor.

                    [Anchor to requiresShipping](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.requiresShipping)requiresShipping • Boolean! non-null
                    :   Whether the item needs to be shipped to the customer. For example, a
                        digital gift card doesn't need to be shipped, but a t-shirt does
                        need to be shipped.

                    [Anchor to sku](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.sku)sku • String
                    :   A case-sensitive identifier for the product variant in the merchant's store. For example, `"BBC-1"`.
                        A product variant must have a SKU to be connected to a
                        [fulfillment service](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services).

                    [Anchor to title](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.title)title • String
                    :   The localized name for the product variant that displays to customers.

                    [Anchor to weight](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.weight)weight • Float
                    :   The product variant's weight, in the system of measurement set in the `weightUnit` field.

                    [Anchor to weightUnit](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.merchandise.ProductVariant.weightUnit)weightUnit • WeightUnit! non-null
                    :   The unit of measurement for weight.

                        Show enum values

                        GRAMS, KILOGRAMS, OUNCES, POUNDS

            [Anchor to parentRelationship](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.parentRelationship)parentRelationship • CartLineParentRelationship
            :   The [nested relationship](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines)
                between this line and its parent line, if any.

                Show fields

                [Anchor to parent](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.parentRelationship.parent)parent • CartLine! non-null
                :   The parent line in the relationship.

            [Anchor to quantity](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.quantity)quantity • Int! non-null
            :   The quantity of the item that the customer intends to purchase.

            [Anchor to sellingPlanAllocation](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation)sellingPlanAllocation • SellingPlanAllocation
            :   The [selling plan](https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans)
                associated with the cart line, including information about how a product variant can be sold and purchased.

                Show fields

                [Anchor to priceAdjustments](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments)priceAdjustments • [SellingPlanAllocationPriceAdjustment!]! non-null
                :   A list of price adjustments, with a maximum of two. When there are two, the first price adjustment goes into effect at the time of purchase, while the second one starts after a certain number of orders. A price adjustment represents how a selling plan affects pricing when a variant is purchased with a selling plan. Prices display in the customer's currency if the shop is configured for it.

                    Show fields

                    [Anchor to perDeliveryPrice](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice)perDeliveryPrice • MoneyV2! non-null
                    :   The effective price for a single delivery. For example, for a prepaid subscription plan that includes 6 deliveries at the price of $48.00, the per delivery price is $8.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.perDeliveryPrice.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                    [Anchor to price](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price)price • MoneyV2! non-null
                    :   The price of the variant when it's purchased with a selling plan For example, for a prepaid subscription plan that includes 6 deliveries of $10.00 granola, where the customer gets 20% off, the price is 6 x $10.00 x 0.80 = $48.00.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price.amount)amount • Decimal! non-null
                        :   A monetary value in decimal format, allowing for precise representation of cents or fractional
                            currency. For example, 12.99.

                        [Anchor to currencyCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.priceAdjustments.price.currencyCode)currencyCode • CurrencyCode! non-null
                        :   The three-letter currency code that represents a world currency used in a store. Currency codes
                            include standard [standard ISO 4217 codes](https://en.wikipedia.org/wiki/ISO_4217), legacy codes,
                            and non-standard codes. For example, USD.

                            Show enum values

                            AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USDC, UYU, UZS, VED, VES, VND, VUV, WST, XAF, XCD, XOF, XPF, XXX, YER, ZAR, ZMW, BYR, STD, VEF

                [Anchor to sellingPlan](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan)sellingPlan • SellingPlan! non-null
                :   A representation of how products and variants can be sold and purchased. For example, an individual selling plan could be '6 weeks of prepaid granola, delivered weekly'.

                    Show fields

                    [Anchor to description](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.description)description • String
                    :   The description of the selling plan.

                    [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.id)id • ID! non-null
                    :   A globally-unique identifier.

                    [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield)metafield • Metafield
                    :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                        about a Shopify resource, such as products, orders, and
                        [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                        Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                        enables you to customize the checkout experience.

                        Show arguments and fields

                        ### Arguments

                        [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.namespace)namespace • String
                        :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                            between different apps or different parts of the same app. If omitted, then the
                            [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                            is used.

                        [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.arguments.key)key • String! required
                        :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                            namespace and a key, in the format `namespace.key`.

                        ---

                        ### Fields

                        [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.jsonValue)jsonValue • JSON! non-null
                        :   The data that's stored in the metafield, using JSON format.

                        [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.type)type • String! non-null
                        :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                            the `value` field.

                        [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.metafield.value)value • String! non-null
                        :   The data that's stored in the metafield. The data is always stored as a string,
                            regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

                    [Anchor to name](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.name)name • String! non-null
                    :   The name of the selling plan. For example, '6 weeks of prepaid granola, delivered weekly'.

                    [Anchor to recurringDeliveries](/docs/api/functions/latest/cart-transform#Input.fields.cart.lines.sellingPlanAllocation.sellingPlan.recurringDeliveries)recurringDeliveries • Boolean! non-null
                    :   Whether purchasing the selling plan will result in multiple deliveries.

        [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

        [Anchor to retailLocation](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation)retailLocation • Location
        :   The physical location where a retail order is created or completed.

            Show fields

            [Anchor to address](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address)address • LocationAddress! non-null
            :   The address of this location.

                Show fields

                [Anchor to address1](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.address1)address1 • String
                :   The first line of the address for the location.

                [Anchor to address2](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.address2)address2 • String
                :   The second line of the address for the location.

                [Anchor to city](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.city)city • String
                :   The city of the location.

                [Anchor to country](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.country)country • String
                :   The country of the location.

                [Anchor to countryCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.countryCode)countryCode • String
                :   The country code of the location.

                [Anchor to formatted](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.formatted)formatted • [String!]! non-null
                :   A formatted version of the address for the location.

                [Anchor to latitude](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.latitude)latitude • Float
                :   The approximate latitude coordinates of the location.

                [Anchor to longitude](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.longitude)longitude • Float
                :   The approximate longitude coordinates of the location.

                [Anchor to phone](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.phone)phone • String
                :   The phone number of the location.

                [Anchor to province](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.province)province • String
                :   The province of the location.

                [Anchor to provinceCode](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.provinceCode)provinceCode • String
                :   The code for the province, state, or district of the address of the location.

                [Anchor to zip](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.address.zip)zip • String
                :   The ZIP code of the location.

            [Anchor to handle](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.handle)handle • Handle! non-null
            :   The location handle.

            [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.id)id • ID! non-null
            :   The location id.

            [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield)metafield • Metafield
            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                about a Shopify resource, such as products, orders, and
                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                enables you to customize the checkout experience.

                Show arguments and fields

                ### Arguments

                [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield.arguments.namespace)namespace • String
                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                    between different apps or different parts of the same app. If omitted, then the
                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                    is used.

                [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield.arguments.key)key • String! required
                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                    namespace and a key, in the format `namespace.key`.

                ---

                ### Fields

                [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield.jsonValue)jsonValue • JSON! non-null
                :   The data that's stored in the metafield, using JSON format.

                [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield.type)type • String! non-null
                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                    the `value` field.

                [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.metafield.value)value • String! non-null
                :   The data that's stored in the metafield. The data is always stored as a string,
                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

            [Anchor to name](/docs/api/functions/latest/cart-transform#Input.fields.cart.retailLocation.name)name • String! non-null
            :   The name of the location.

    [Anchor to cartTransform](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform)cartTransform • CartTransform! non-null
    :   A customization that changes the pricing and
        presentation of items in a cart. For example,
        you can modify the appearance of cart items,
        such as updating titles and images,
        or [bundling items](https://shopify.dev/docs/apps/build/product-merchandising/bundles).

        Show fields

        [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.cartTransform.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

    [Anchor to localization](/docs/api/functions/latest/cart-transform#Input.fields.localization)localization • Localization! non-null
    :   The regional and language settings that determine how the Function
        handles currency, numbers, dates, and other locale-specific values
        during discount calculations. These settings are based on the store's configured
        [localization practices](https://shopify.dev/docs/apps/build/functions/localization-practices-shopify-functions).

        Show fields

        [Anchor to country](/docs/api/functions/latest/cart-transform#Input.fields.localization.country)country • Country! non-null
        :   The country for which the store is customized, reflecting local preferences and regulations.
            Localization might influence the language, currency, and product offerings available in a store to enhance
            the shopping experience for customers in that region.

            Show fields

            [Anchor to isoCode](/docs/api/functions/latest/cart-transform#Input.fields.localization.country.isoCode)isoCode • CountryCode! non-null
            :   The ISO code of the country.

                Show enum values

                AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AR, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MK, ML, MM, MN, MO, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PS, PT, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TA, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW, ZZ

        [Anchor to language](/docs/api/functions/latest/cart-transform#Input.fields.localization.language)language • Language! non-null
        :   The language for which the store is customized, ensuring content is tailored to local customers.
            This includes product descriptions and customer communications that resonate with the target audience.

            Show fields

            [Anchor to isoCode](/docs/api/functions/latest/cart-transform#Input.fields.localization.language.isoCode)isoCode • LanguageCode! non-null
            :   The ISO code.

                Show enum values

                AF, AK, AM, AR, AS, AZ, BE, BG, BM, BN, BO, BR, BS, CA, CE, CKB, CS, CU, CY, DA, DE, DZ, EE, EL, EN, EO, ES, ET, EU, FA, FF, FI, FIL, FO, FR, FY, GA, GD, GL, GU, GV, HA, HE, HI, HR, HU, HY, IA, ID, IG, II, IS, IT, JA, JV, KA, KI, KK, KL, KM, KN, KO, KS, KU, KW, KY, LB, LG, LN, LO, LT, LU, LV, MG, MI, MK, ML, MN, MR, MS, MT, MY, NB, ND, NE, NL, NN, NO, OM, OR, OS, PA, PL, PS, PT, PT\_BR, PT\_PT, QU, RM, RN, RO, RU, RW, SA, SC, SD, SE, SG, SI, SK, SL, SN, SO, SQ, SR, SU, SV, SW, TA, TE, TG, TH, TI, TK, TO, TR, TT, UG, UK, UR, UZ, VI, VO, WO, XH, YI, YO, ZH, ZH\_CN, ZH\_TW, ZU

        [Anchor to market](/docs/api/functions/latest/cart-transform#Input.fields.localization.market)market • Market! non-nullDeprecated
        :   Show fields

            [Anchor to handle](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.handle)handle • Handle! non-null
            :   A human-readable unique string for the market automatically generated from its title.

            [Anchor to id](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.id)id • ID! non-null
            :   A globally-unique identifier.

            [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield)metafield • Metafield
            :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
                about a Shopify resource, such as products, orders, and
                [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
                Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
                enables you to customize the checkout experience.

                Show arguments and fields

                ### Arguments

                [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield.arguments.namespace)namespace • String
                :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                    between different apps or different parts of the same app. If omitted, then the
                    [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                    is used.

                [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield.arguments.key)key • String! required
                :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                    namespace and a key, in the format `namespace.key`.

                ---

                ### Fields

                [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield.jsonValue)jsonValue • JSON! non-null
                :   The data that's stored in the metafield, using JSON format.

                [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield.type)type • String! non-null
                :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                    the `value` field.

                [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.metafield.value)value • String! non-null
                :   The data that's stored in the metafield. The data is always stored as a string,
                    regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

            [Anchor to regions](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.regions)regions • [MarketRegion!]! non-null
            :   A geographic region which comprises a market.

                Show fields

                [Anchor to name](/docs/api/functions/latest/cart-transform#Input.fields.localization.market.regions.name)name • String
                :   The name of the region in the language of the current localization.

    [Anchor to presentmentCurrencyRate](/docs/api/functions/latest/cart-transform#Input.fields.presentmentCurrencyRate)presentmentCurrencyRate • Decimal! non-null
    :   The exchange rate used to convert discounts between the shop's default
        currency and the currency that displays to the customer during checkout.
        For example, if a store operates in USD but a customer is viewing discounts in EUR,
        then the presentment currency rate handles this conversion for accurate pricing.

    [Anchor to shop](/docs/api/functions/latest/cart-transform#Input.fields.shop)shop • Shop! non-null
    :   Information about the shop where the Function is running, including the shop's timezone
        setting and associated [metafields](https://shopify.dev/docs/apps/build/custom-data).

        Show fields

        [Anchor to localTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime)localTime • LocalTime! non-null
        :   The current time based on the
            [store's timezone setting](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-business-settings).

            Show fields

            [Anchor to date](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.date)date • Date! non-null
            :   The current date relative to the parent object.

            [Anchor to dateTimeAfter](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeAfter)dateTimeAfter • Boolean! non-null
            :   Returns true if the current date and time is at or past the given date and time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to dateTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeAfter.arguments.dateTime)dateTime • DateTimeWithoutTimezone! required
                :   The date and time to compare against, assumed to be in the timezone of the parent object.

                ---

            [Anchor to dateTimeBefore](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeBefore)dateTimeBefore • Boolean! non-null
            :   Returns true if the current date and time is before the given date and time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to dateTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeBefore.arguments.dateTime)dateTime • DateTimeWithoutTimezone! required
                :   The date and time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to dateTimeBetween](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeBetween)dateTimeBetween • Boolean! non-null
            :   Returns true if the current date and time is between the two given date and times, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to startDateTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeBetween.arguments.startDateTime)startDateTime • DateTimeWithoutTimezone! required
                :   The lower bound time to compare against, assumed to be in the timezone of the parent timezone.

                [Anchor to endDateTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.dateTimeBetween.arguments.endDateTime)endDateTime • DateTimeWithoutTimezone! required
                :   The upper bound time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeAfter](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeAfter)timeAfter • Boolean! non-null
            :   Returns true if the current time is at or past the given time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to time](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeAfter.arguments.time)time • TimeWithoutTimezone! required
                :   The time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeBefore](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeBefore)timeBefore • Boolean! non-null
            :   Returns true if the current time is at or past the given time, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to time](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeBefore.arguments.time)time • TimeWithoutTimezone! required
                :   The time to compare against, assumed to be in the timezone of the parent timezone.

                ---

            [Anchor to timeBetween](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeBetween)timeBetween • Boolean! non-null
            :   Returns true if the current time is between the two given times, and false otherwise.

                Show arguments

                ### Arguments

                [Anchor to startTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeBetween.arguments.startTime)startTime • TimeWithoutTimezone! required
                :   The lower bound time to compare against, assumed to be in the timezone of the parent timezone.

                [Anchor to endTime](/docs/api/functions/latest/cart-transform#Input.fields.shop.localTime.timeBetween.arguments.endTime)endTime • TimeWithoutTimezone! required
                :   The upper bound time to compare against, assumed to be in the timezone of the parent timezone.

                ---

        [Anchor to metafield](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield)metafield • Metafield
        :   A [custom field](https://shopify.dev/docs/apps/build/custom-data) that stores additional information
            about a Shopify resource, such as products, orders, and
            [many more](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).
            Using [metafields with Shopify Functions](https://shopify.dev/docs/apps/build/functions/input-output/metafields-for-input-queries)
            enables you to customize the checkout experience.

            Show arguments and fields

            ### Arguments

            [Anchor to namespace](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield.arguments.namespace)namespace • String
            :   A category that organizes a group of metafields. Namespaces are used to prevent naming conflicts
                between different apps or different parts of the same app. If omitted, then the
                [app-reserved namespace](https://shopify.dev/docs/apps/build/custom-data/ownership)
                is used.

            [Anchor to key](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield.arguments.key)key • String! required
            :   The unique identifier for the metafield within its namespace. A metafield is composed of a
                namespace and a key, in the format `namespace.key`.

            ---

            ### Fields

            [Anchor to jsonValue](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield.jsonValue)jsonValue • JSON! non-null
            :   The data that's stored in the metafield, using JSON format.

            [Anchor to type](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield.type)type • String! non-null
            :   The [type of data](https://shopify.dev/apps/metafields/types) that the metafield stores in
                the `value` field.

            [Anchor to value](/docs/api/functions/latest/cart-transform#Input.fields.shop.metafield.value)value • String! non-null
            :   The data that's stored in the metafield. The data is always stored as a string,
                regardless of the [metafield's type](https://shopify.dev/apps/metafields/types).

#### [Anchor to Run Function](/docs/api/functions/latest/cart-transform#run-function)Run Function

The logic that processes the input data to generate a standardized list of operations that change the pricing and
presentation of items in a cart.

Each operation specifies how to display the items in a cart. Shopify processes your response to present
the cart items to customers during checkout, including data such as price and quantity.

This return must follow the schema defined in the `CartTransformRunResult` object.

* CartTransformRunResult

[Anchor to CartTransformRunResult](/docs/api/functions/latest/cart-transform#CartTransformRunResult)CartTransformRunResult OBJECT
:   The `CartTransformRunResult` object is the output of the function run target. The object contains the operations to change
    the pricing and presentation of items in a cart.

    Hide fields

    [Anchor to operations](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations)operations • [Operation!]! non-null
    :   The ordered list of operations to apply to the cart. For example, you can expand a cart line item to display
        its [bundled items](https://shopify.dev/docs/apps/build/product-merchandising/bundles), merge
        multiple cart lines into a single line representing a bundle, and update the presentation of line items
        in the cart to override their price, title, or image.

        Hide fields

        [Anchor to lineExpand](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand)lineExpand • LineExpandOperation
        :   An operation that expands a single cart line item to form a
            [bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles)
            of components.

            Show fields

            [Anchor to cartLineId](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.cartLineId)cartLineId • ID! non-null
            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                for a line item in a cart. A cart line represents a single unit of a
                product variant that a customer intends to purchase.

            [Anchor to expandedCartItems](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems)expandedCartItems • [ExpandedItem!]! non-null
            :   The cart items to expand. Each item in the list is a component of the
                [bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles). A
                bundle is a group of products that are sold together as a single unit.

                Show fields

                [Anchor to attributes](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.attributes)attributes • [AttributeOutput!]
                :   The custom attributes associated with a cart line to store additional information. Cart attributes
                    allow you to collect specific information from customers on the **Cart** page, such as order notes,
                    gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                    Show fields

                    [Anchor to key](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.attributes.key)key • String! non-null
                    :   The key of the cart line attribute to retrieve. For example, `"gift_wrapping"`.

                    [Anchor to value](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.attributes.value)value • String! non-null
                    :   The value of the cart line attribute to retrieve. For example, `"true"`.

                [Anchor to merchandiseId](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.merchandiseId)merchandiseId • ID! non-null
                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                    for the product variant that represents the expanded item.

                [Anchor to price](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.price)price • ExpandedItemPriceAdjustment
                :   A change to the original price of the expanded item. Price adjustments include discounts or additional charges that
                    affect the final price the customer pays. Price adjustments are often used for promotions, special offers,
                    or any price changes that the customer qualifies for.

                    Show fields

                    [Anchor to adjustment](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.price.adjustment)adjustment • ExpandedItemPriceAdjustmentValue! non-null
                    :   The value of the price adjustment to apply to the expanded item.

                        Show fields

                        [Anchor to fixedPricePerUnit](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.price.adjustment.fixedPricePerUnit)fixedPricePerUnit • ExpandedItemFixedPricePerUnitAdjustment
                        :   A fixed price per unit adjustment to apply to the expanded item.

                            Show fields

                            [Anchor to amount](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.price.adjustment.fixedPricePerUnit.amount)amount • Decimal! non-null
                            :   The fixed price amount per quantity of the expanded item in presentment currency.

                [Anchor to quantity](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.expandedCartItems.quantity)quantity • Int! non-null
                :   The quantity of the expanded item. The maximum quantity is
                    2000.

            [Anchor to image](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.image)image • ImageInput
            :   The image that replaces the existing image for the group of cart line items.
                The image must have a publicly accessible URL.

                Show fields

                [Anchor to url](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.image.url)url • URL! non-null
                :   The URL of the image.

            [Anchor to price](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.price)price • PriceAdjustment
            :   A change to the original price of a group of items. Price adjustments include discounts or additional charges that
                affect the final price the customer pays. Price adjustments are often used for promotions, special offers,
                or any price changes that the customer qualifies for.

                Show fields

                [Anchor to percentageDecrease](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.price.percentageDecrease)percentageDecrease • PriceAdjustmentValue
                :   The percentage price decrease of the price adjustment.

                    Show fields

                    [Anchor to value](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.price.percentageDecrease.value)value • Decimal! non-null
                    :   The value of the price adjustment.

            [Anchor to title](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineExpand.title)title • String
            :   The title that replaces the existing title for the cart line item.
                If you don't provide a title, then the title of the product variant is used.

        [Anchor to linesMerge](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge)linesMerge • LinesMergeOperation
        :   An operation that merges multiple cart line items into a
            single line, representing a
            [bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles)
            of components.

            Show fields

            [Anchor to attributes](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.attributes)attributes • [AttributeOutput!]
            :   The custom attributes associated with a cart line to store additional information. Cart attributes
                allow you to collect specific information from customers on the **Cart** page, such as order notes,
                gift wrapping requests, or custom product details. Attributes are stored as key-value pairs.

                Show fields

                [Anchor to key](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.attributes.key)key • String! non-null
                :   The key of the cart line attribute to retrieve. For example, `"gift_wrapping"`.

                [Anchor to value](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.attributes.value)value • String! non-null
                :   The value of the cart line attribute to retrieve. For example, `"true"`.

            [Anchor to cartLines](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.cartLines)cartLines • [CartLineInput!]! non-null
            :   The cart items to merge. Each item in the list is a component of the
                [bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles).

                Show fields

                [Anchor to cartLineId](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.cartLines.cartLineId)cartLineId • ID! non-null
                :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                    for a line item in a cart. A cart line represents a single unit of a
                    product variant that a customer intends to purchase.

                [Anchor to quantity](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.cartLines.quantity)quantity • Int! non-null
                :   The quantity of the cart line to be merged.The max quantity is 2000.

            [Anchor to image](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.image)image • ImageInput
            :   The image that replaces the existing image for the group of cart line items.
                The image must have a publicly accessible URL.

                Show fields

                [Anchor to url](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.image.url)url • URL! non-null
                :   The URL of the image.

            [Anchor to parentVariantId](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.parentVariantId)parentVariantId • ID! non-null
            :   The [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                of the product variant that represents the collection of cart line items.

            [Anchor to price](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.price)price • PriceAdjustment
            :   A change to the original price of a group of items. Price adjustments include discounts or additional charges that
                affect the final price the customer pays. Price adjustments are often used for promotions, special offers,
                or any price changes that the customer qualifies for.

                Show fields

                [Anchor to percentageDecrease](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.price.percentageDecrease)percentageDecrease • PriceAdjustmentValue
                :   The percentage price decrease of the price adjustment.

                    Show fields

                    [Anchor to value](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.price.percentageDecrease.value)value • Decimal! non-null
                    :   The value of the price adjustment.

            [Anchor to title](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.linesMerge.title)title • String
            :   The title that replaces the existing title for a group of cart line items.
                If you don't provide a title, then the title of the parent variant is used.

        [Anchor to lineUpdate](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate)lineUpdate • LineUpdateOperation
        :   An operation that allows you to override the price, title,
            and image of a cart line item. Only stores on a
            [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan)
            can use apps with `update` operations.

            Show fields

            [Anchor to cartLineId](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.cartLineId)cartLineId • ID! non-null
            :   A [globally-unique ID](https://shopify.dev/docs/api/usage/gids)
                for a line item in a cart. A cart line represents a single unit of a
                product variant that a customer intends to purchase.

            [Anchor to image](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.image)image • ImageInput
            :   The image that replaces the existing image for the cart line item.
                The image must have a publicly accessible URL.
                This image is visible in checkout only and is not persisted to orders.

                Show fields

                [Anchor to url](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.image.url)url • URL! non-null
                :   The URL of the image.

            [Anchor to price](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.price)price • LineUpdateOperationPriceAdjustment
            :   A change to an item's original price. Price adjustments include discounts or additional charges that affect the final
                price the customer pays. Price adjustments are often used for promotions, special offers, or any price changes
                for which the customer qualifies.

                Show fields

                [Anchor to adjustment](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.price.adjustment)adjustment • LineUpdateOperationPriceAdjustmentValue! non-null
                :   The price adjustment per unit to apply to the cart line item.

                    Show fields

                    [Anchor to fixedPricePerUnit](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.price.adjustment.fixedPricePerUnit)fixedPricePerUnit • LineUpdateOperationFixedPricePerUnitAdjustment
                    :   A fixed price per unit adjustment to apply to a cart line.

                        Show fields

                        [Anchor to amount](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.price.adjustment.fixedPricePerUnit.amount)amount • Decimal! non-null
                        :   The fixed price amount per quantity of the cart line item in presentment currency.

            [Anchor to title](/docs/api/functions/latest/cart-transform#CartTransformRunResult.fields.operations.lineUpdate.title)title • String
            :   The title that replaces the existing title for the cart line item.
                If you don't provide a title, then the title of the product variant is used.

Was this section helpful?

YesNo

---

## [Anchor to Multiple operations](/docs/api/functions/latest/cart-transform#multiple-operations)Multiple operations

Sometimes, a function might return multiple expand, merge, and update operations for the same cart line, which can lead
to collisions. For example, a collision might happen when you execute different operations in quick succession, or when
multiple changes are applied to the same cart line. To avoid potential issues, try to minimize these collisions in your
implementation.

If a collision does occur, then Shopify handles it by executing a subset of operations based on the following criteria:

* If multiple `lineExpand` operations target the same cart line, then the first `lineExpand` operation in the list is executed,
  and all other `lineExpand` operations for the same cart line are discarded.
* If multiple `linesMerge` operations target the same cart line, then the first `linesMerge` operation in the list is executed,
  and all other `linesMerge` operations for the same cart line are discarded.
* If both `lineExpand` and `linesMerge` operations target the same cart line, then the `lineExpand` operation is executed, and the
  merge operation is discarded.
* If multiple `lineUpdate` operations target the same cart line, then the first `lineUpdate` operation in the list is executed,
  and all other `lineUpdate` operations for the same cart line are discarded.
* If `lineExpand`, `linesMerge`, and `lineUpdate` operations target the same cart line, then the `lineExpand` operation is executed
  while the merge and `lineUpdate` operations are discarded.
* If both fixed `lineExpand` and customized `lineExpand` operations target the same cart line, then the fixed `lineExpand`
  operation is executed and the customized `lineExpand` operation is discarded.

Was this section helpful?

YesNo

---

## [Anchor to Pricing adjustments](/docs/api/functions/latest/cart-transform#pricing-adjustments)Pricing adjustments

You can use `linesMerge` and `lineExpand` operations to adjust pricing. The bundle base price varies depending on the operation:

* **`linesMerge`**: The adjustment is based on the components' price sum.
* **`lineExpand`**: The adjustment is based on the bundle product price.

This distinction ensures that the correct price appears for expand operations on the
[Product details page](https://help.shopify.com/manual/products/details) and in
[Liquid](/docs/api/liquid/objects/line_item).

For example, to arrive at the final bundle price, you can use the following post-processing operations:

* **`linesMerge`**: The final price is the sum of the individual component prices, plus the adjustment, if present.
* **`lineExpand`**: The final price is the sum of the individual component `fixedPricePerUnit` values, or the
  bundle product price, plus the adjustment, if present.

### [Anchor to Component pricing](/docs/api/functions/latest/cart-transform#component-pricing)Component pricing

Expand operations allow you to adjust the price of each individual component in the bundle by providing a price on the
`expandedCartItems` field in the `LineExpandOperation` object.

The costs returned by the input query reflect prices in the
[presentment currency](https://help.shopify.com/manual/international/pricing/exchange-rates#currency-definitions-and-conversions),
and all operation outputs are also processed in this currency. Presentment currency is the currency that customers see
when they view prices in a store.

If you need to set a new price based on the cost in the
[store's currency](https://help.shopify.com/manual/international/pricing/exchange-rates#currency-definitions-and-conversions),
then you should do the following:

1. To get the conversion rate from shop currency to presentment currency, include the
   `presentmentCurrencyRate` field in your input query.
2. Convert the amount from the shop currency to presentment currency using the rate.
3. Return the converted price in your operation output.

### [Anchor to Weight price algorithm](/docs/api/functions/latest/cart-transform#weight-price-algorithm)Weight price algorithm

When you don't provide a fixed price per unit on `lineExpand` operations, Shopify allocates the bundle price to its
component lines based on the weight of each component line. The weight of a component is calculated as the unit price
multiplied by quantity, as `unit price * quantity`.

The algorithm considers the item's price as if the item was bought individually and the quantity inside the bundle.
For example, if a bundle has 10 t-shirts and 1 pair of shorts, and the shorts and t-shirt cost $5 if they were bought
individually, then Shopify allocates more weight to the t-shirt. The total weight of all component lines is then used
to calculate the weight of each component line.

#### [Anchor to Example](/docs/api/functions/latest/cart-transform#example)Example

**Amount to be allocated**: $100

**Component lines**:

* `unit_price`: $10, `quantity`: 1, `id`: 1 # weight 10
* `unit_price`: $20, `quantity`: 2, `id`: 2 # weight 40
* `unit_price`: $30, `quantity`: 3, `id`: 3 # weight 90

**Total weight**: 140

**Result**:

* **Component 1**: $7.14 -> (10 / 140) \* $100 = 7.14
* **Component 2**: $28.57 -> (40 / 140) \* $100 = 28.57
* **Component 3**: $64.29 -> (90 / 140) \* $100 = 64.29

Was this section helpful?

YesNo

---

## [Anchor to Overriding images and titles](/docs/api/functions/latest/cart-transform#overriding-images-and-titles)Overriding images and titles

* **Uploading images**: For optimal performance and security, you can only use upload images for cart lines from
  [Shopify CDN](https://cdn.shopify.com/). You can upload images through the
  [Shopify admin](https://help.shopify.com/manual/shopify-admin/productivity-tools/file-uploads) or using the
  [GraphQL Admin API](/docs/api/admin-graphql/latest/mutations/fileCreate). Using images from outside
  of the CDN will result in an `invalid_image_url` error.
* **Image sizes**: Image URLs shouldn't include a size suffix. The cart will automatically request the appropriately
  sized image from the CDN by adding a size suffix to the image name, such as `custom-image_64x64.png`.
* **Showing overrides**: Title and image overrides appear across various surfaces, including the cart, checkout, and
  order notification emails. To see title overrides applied by cart transform functions in these areas, you'll need to
  modify your themes. Use [`item.title`](/docs/api/liquid/objects/line_item#line_item-title) for the
  cart and [`line.title`](https://help.shopify.com/manual/fulfillment/setup/notifications/email-variables#line-item) for
  order notification emails to display the updated titles.

Was this section helpful?

YesNo

---

## [Anchor to Errors](/docs/api/functions/latest/cart-transform#errors)Errors

The following errors can occur when using the Cart Transform API:

Errors that can occur when using the Cart Transform API

| Operation type | Error code | Message |
| --- | --- | --- |
| `lineExpand` | `cannot_combine_price_adjustment_and_price_per_component` | Cannot combine both an overall price adjustment and individual prices for components. |
| `component_merchandise_not_found` | One or more of the expanded cart items have a merchandise ID that does not exist. |
| `exceeded_maximum_number_of_supported_expanded_cart_items` | Exceeded the maximum number of supported expanded cart items (150). |
| `expanded_items_missing_prices` | One or more expanded cart items are missing prices. Either all must have a price, or none. |
| `image_feature_not_available` | The feature to update the image is not accessible for the given shop. |
| `image_not_found` | Image not found for the shop. |
| `invalid_cart_line_id` | The cart line ID is invalid. |
| `invalid_component_merchandise_id` | One or more of the expanded cart items have an invalid merchandise ID. |
| `invalid_component_quantity` | One or more of the expanded cart items have an invalid quantity. |
| `invalid_component_price` | One or more of the expanded cart items have an invalid price. |
| `invalid_image_url` | The base image URL must be any of the following: <https://cdn.shopify.com/>, <https://cdn.shopifycdn.net/>, or the shop's domain with a path of /cdn/\*. |
| `invalid_price_adjustment_percentage_decrease` | The percentage decrease value must be less than or equal to 100. |
| `price_per_component_feature_not_available` | The feature to price an expanded cart item is not accessible for the given shop. |
| `title_feature_not_available` | The feature to update the title is not accessible for the given shop. |
| `linesMerge` | `exceeded_maximum_number_of_supported_merged_cart_items` | Exceeded the maximum number of supported merged cart items. |
| `image_not_found` | Image not found for the shop. |
| `insufficient_component_quantity_to_merge` | There are not enough items in the cart to satisfy one or more of the component quantities. |
| `invalid_component_cart_line_id` | One or more of the cart lines have an invalid cart line ID. |
| `invalid_component_quantity` | One or more of the cart lines have an invalid quantity. |
| `invalid_image_url` | The base image URL must be any of the following: <https://cdn.shopify.com/>, <https://cdn.shopifycdn.net/>, or the shop's domain with a path of /cdn/\*. |
| `invalid_parent_variant_id` | The parent variant ID isn't valid. |
| `invalid_price_adjustment_percentage_decrease` | The percentage decrease value must be less than or equal to 100. |
| `parent_variant_not_found` | The parent variant doesn't exist. |
| `lineUpdate` | `fixed_price_adjustment_cannot_be_negative` | Fixed price adjustments cannot be negative. |
| `image_not_found` | Image not found for the shop. |
| `invalid_cart_line_id` | The cart line ID is invalid. |
| `invalid_image_url` | The base image URL must be any of the following: <https://cdn.shopify.com/>, <https://cdn.shopifycdn.net/>, or the shop's domain with a path of /cdn/\*. |
| `update_feature_not_available` | The update operation feature is not accessible for the given shop. |

Was this section helpful?

YesNo

---

## [Anchor to Invalid scenarios](/docs/api/functions/latest/cart-transform#invalid-scenarios)Invalid scenarios

Shopify rejects `lineExpand`, `linesMerge`, and `lineUpdate` operations if a
[selling plan](/docs/apps/build/purchase-options/subscriptions/selling-plans) is present. Rejections are different from
error scenarios, which might involve implementation issues not directly related to the operations being performed.

The following table describes invalid scenarios by operation type:

Invalid scenarios by operation type

| Operation type | Scenarios |
| --- | --- |
| `lineExpand` | * One of the component quantities is less than 0. * The line to be expanded doesn't exist. * One of the component variant IDs doesn't exist. * Both `ExpandedItem.Price` and `PriceAdjustment` are returned in the operation. * One of the components is given a price less than 0. * Some of the components have a customized price and others don't. |
| `linesMerge` | * The merge operation contains an invalid quantity for the children (less than 0 or the quantity to merge is bigger than the line's quantity). * The parent variant ID doesn't exist. * One of the lines to be merged doesn't exist. |
| `lineUpdate` | * The operation includes a price < 0. * The line to be updated doesn't exist. * The operation targets a line that is going to be expanded or merged. * The shop is not on a Plus plan or a Development store plan. |

Was this section helpful?

YesNo

---

## [Anchor to Nested cart lines](/docs/api/functions/latest/cart-transform#nested-cart-lines)Nested cart lines

CartTransform operations have specific behaviors when applied to nested cart lines. For details, see [CartTransform operations on nested cart lines](/docs/apps/build/product-merchandising/nested-cart-lines#carttransform-operations-on-nested-cart-lines).

Was this section helpful?

YesNo

---

## [Anchor to Additional resources](/docs/api/functions/latest/cart-transform#additional-resources)Additional resources

Explore comprehensive guides and references to help you build, deploy, and optimize your Shopify Functions.

### [Anchor to Working with Functions](/docs/api/functions/latest/cart-transform#working-with-functions)Working with Functions

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

### [Anchor to Performance and troubleshooting](/docs/api/functions/latest/cart-transform#performance-and-troubleshooting)Performance and troubleshooting

Optimize function performance and ensure reliable operation from development through production deployment.

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Resource limits and performance

Understand function performance requirements and resource limitations for optimal execution.

Resource limits and performance

Understand function performance requirements and resource limitations for optimal execution.](/docs/api/functions/current#resource-limits-and-performance)

[Resource limits and performance](/docs/api/functions/current#resource-limits-and-performance)

[![](/images/icons/48/industries.png)![](/images/icons/48/industries-dark.png)

Test and debug Shopify Functions

Explore comprehensive testing workflows from local development to production deployment.

Test and debug Shopify Functions

Explore comprehensive testing workflows from local development to production deployment.](/docs/apps/build/functions/test-debug-functions)

[Test and debug Shopify Functions  
  

Explore comprehensive testing workflows from local development to production deployment.](/docs/apps/build/functions/test-debug-functions)

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