---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Shop
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_read_product_listings` access scope.

Shop represents a collection of the general settings and information about the shop.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Shop#fields)Fields

* brand (Brand)
* customerAccountTranslations ([Translation!])
* customerAccountUrl (String)
* description (String)
* id (ID!)
* metafield (Metafield)
* metafields ([Metafield]!)
* moneyFormat (String!)
* name (String!)
* paymentSettings (PaymentSettings!)
* primaryDomain (Domain!)
* privacyPolicy (ShopPolicy)
* refundPolicy (ShopPolicy)
* shippingPolicy (ShopPolicy)
* shipsToCountries ([CountryCode!]!)
* shopPayInstallmentsPricing (ShopPayInstallmentsPricing)
* socialLoginProviders ([SocialLoginProvider!]!)
* subscriptionPolicy (ShopPolicyWithDefault)
* termsOfService (ShopPolicy)

[Anchor to brand](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.brand)brand •[Brand](/docs/api/storefront/latest/objects/Brand)
:   The shop's branding configuration.

    Show fields

[Anchor to customerAccountTranslations](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.customerAccountTranslations)customerAccountTranslations •[[Translation!]](/docs/api/storefront/latest/objects/Translation)
:   Translations for customer accounts.

    Show fields

[Anchor to customerAccountUrl](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.customerAccountUrl)customerAccountUrl •[String](/docs/api/storefront/latest/scalars/String)
:   The URL for the customer account (only present if shop has a customer account vanity domain).

[Anchor to description](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.description)description •[String](/docs/api/storefront/latest/scalars/String)
:   A description of the shop.

[Anchor to id](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to metafield](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to moneyFormat](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.moneyFormat)moneyFormat •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   A string representing the way currency is formatted when the currency isn’t specified.

[Anchor to name](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.name)name •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   The shop’s name.

[Anchor to paymentSettings](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.paymentSettings)paymentSettings •[PaymentSettings!](/docs/api/storefront/latest/objects/PaymentSettings) non-null
:   Settings related to payments.

    Show fields

[Anchor to primaryDomain](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.primaryDomain)primaryDomain •[Domain!](/docs/api/storefront/latest/objects/Domain) non-null
:   The primary domain of the shop’s Online Store.

    Show fields

[Anchor to privacyPolicy](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.privacyPolicy)privacyPolicy •[ShopPolicy](/docs/api/storefront/latest/objects/ShopPolicy)
:   The shop’s privacy policy.

    Show fields

[Anchor to refundPolicy](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.refundPolicy)refundPolicy •[ShopPolicy](/docs/api/storefront/latest/objects/ShopPolicy)
:   The shop’s refund policy.

    Show fields

[Anchor to shippingPolicy](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.shippingPolicy)shippingPolicy •[ShopPolicy](/docs/api/storefront/latest/objects/ShopPolicy)
:   The shop’s shipping policy.

    Show fields

[Anchor to shipsToCountries](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.shipsToCountries)shipsToCountries •[[CountryCode!]!](/docs/api/storefront/latest/enums/CountryCode) non-null
:   Countries that the shop ships to.

    Show enum values

[Anchor to shopPayInstallmentsPricing](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.shopPayInstallmentsPricing)shopPayInstallmentsPricing •[ShopPayInstallmentsPricing](/docs/api/storefront/latest/objects/ShopPayInstallmentsPricing) Token access required
:   The Shop Pay Installments pricing information for the shop.

    Show fields

[Anchor to socialLoginProviders](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.socialLoginProviders)socialLoginProviders •[[SocialLoginProvider!]!](/docs/api/storefront/latest/objects/SocialLoginProvider) non-null
:   The social login providers for customer accounts.

    Show fields

[Anchor to subscriptionPolicy](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.subscriptionPolicy)subscriptionPolicy •[ShopPolicyWithDefault](/docs/api/storefront/latest/objects/ShopPolicyWithDefault)
:   The shop’s subscription policy.

    Show fields

[Anchor to termsOfService](/docs/api/storefront/latest/objects/Shop#field-Shop.fields.termsOfService)termsOfService •[ShopPolicy](/docs/api/storefront/latest/objects/ShopPolicy)
:   The shop’s terms of service.

    Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/storefront/latest/objects/Shop#queries)Queries

* shop (Shop!)

[Anchor to shop](/docs/api/storefront/latest/objects/Shop#query-shop)[shop](/docs/api/storefront/latest/queries/shop) •query
:   The shop associated with the storefront access token.

    Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/Shop#interfaces)Interfaces

* HasMetafields
* Node

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/Shop#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/storefront/latest/objects/Shop#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo