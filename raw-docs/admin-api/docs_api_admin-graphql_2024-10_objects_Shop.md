---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Shop
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

The central configuration and settings hub for a Shopify store. Access business information, operational preferences, feature availability, and store-wide settings that control how the shop operates.

Includes core business details like the shop name, contact emails, billing address, and currency settings. The shop configuration determines customer account requirements, available sales channels, enabled features, payment settings, and policy documents. Also provides access to shop-level resources such as staff members, fulfillment services, navigation settings, and storefront access tokens.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Shop#fields)Fields

* accountOwner (StaffMember!)
* alerts ([ShopAlert!]!)
* allProductCategoriesList ([TaxonomyCategory!]!)
* availableChannelApps (AppConnection!)
* channelDefinitionsForInstalledChannels ([AvailableChannelDefinitionsByChannel!]!)
* checkoutApiSupported (Boolean!)
* contactEmail (String!)
* countriesInShippingZones (CountriesInShippingZones!)
* createdAt (DateTime!)
* currencyCode (CurrencyCode!)
* currencyFormats (CurrencyFormats!)
* currencySettings (CurrencySettingConnection!)
* customerAccounts (ShopCustomerAccountsSetting!)
* customerAccountsV2 (CustomerAccountsV2!)
* customerTags (StringConnection!)
* description (String)
* draftOrderTags (StringConnection!)
* email (String!)
* enabledPresentmentCurrencies ([CurrencyCode!]!)
* entitlements (EntitlementsType!)
* features (ShopFeatures!)
* fulfillmentServices ([FulfillmentService!]!)
* ianaTimezone (String!)
* id (ID!)
* marketingSmsConsentEnabledAtCheckout (Boolean!)
* merchantApprovalSignals (MerchantApprovalSignals)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* myshopifyDomain (String!)
* name (String!)
* navigationSettings ([NavigationItem!]!)
* orderNumberFormatPrefix (String!)
* orderNumberFormatSuffix (String!)
* orderTags (StringConnection!)
* paymentSettings (PaymentSettings!)
* plan (ShopPlan!)
* primaryDomain (Domain!)
* resourceLimits (ShopResourceLimits!)
* richTextEditorUrl (URL!)
* search (SearchResultConnection!)
* searchFilters (SearchFilterOptions!)
* setupRequired (Boolean!)
* shipsToCountries ([CountryCode!]!)
* shopAddress (ShopAddress!)
* shopOwnerName (String!)
* shopPolicies ([ShopPolicy!]!)
* storefrontAccessTokens (StorefrontAccessTokenConnection!)
* taxesIncluded (Boolean!)
* taxShipping (Boolean!)
* timezoneAbbreviation (String!)
* timezoneOffset (String!)
* timezoneOffsetMinutes (Int!)
* transactionalSmsDisabled (Boolean!)
* translations ([Translation!]!)
* unitSystem (UnitSystem!)
* updatedAt (DateTime!)
* url (URL!)
* weightUnit (WeightUnit!)

[Anchor to accountOwner](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.accountOwner)accountOwner •[StaffMember!](/docs/api/admin-graphql/latest/objects/StaffMember) non-null
:   Account owner information.

    Show fields

[Anchor to alerts](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.alerts)alerts •[[ShopAlert!]!](/docs/api/admin-graphql/latest/objects/ShopAlert) non-null
:   A list of the shop's active alert messages that appear in the Shopify admin.

    Show fields

[Anchor to allProductCategoriesList](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.allProductCategoriesList)allProductCategoriesList •[[TaxonomyCategory!]!](/docs/api/admin-graphql/latest/objects/TaxonomyCategory) non-null
:   A list of the shop's product categories. Limit: 1000 product categories.

    Show fields

[Anchor to availableChannelApps](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps)availableChannelApps •[AppConnection!](/docs/api/admin-graphql/latest/connections/AppConnection) non-null
:   The list of sales channels not currently installed on the shop.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.availableChannelApps.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to channelDefinitionsForInstalledChannels](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channelDefinitionsForInstalledChannels)channelDefinitionsForInstalledChannels •[[AvailableChannelDefinitionsByChannel!]!](/docs/api/admin-graphql/latest/objects/AvailableChannelDefinitionsByChannel) non-null
:   List of all channel definitions associated with a shop.

    Show fields

[Anchor to checkoutApiSupported](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.checkoutApiSupported)checkoutApiSupported •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Specifies whether the shop supports checkouts via Checkout API.

[Anchor to contactEmail](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.contactEmail)contactEmail •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The public-facing contact email address for the shop.
    Customers will use this email to communicate with the shop owner.

[Anchor to countriesInShippingZones](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.countriesInShippingZones)countriesInShippingZones •[CountriesInShippingZones!](/docs/api/admin-graphql/latest/objects/CountriesInShippingZones) non-null
:   Countries that have been defined in shipping zones for the shop.

    Show fields

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the shop was created.

[Anchor to currencyCode](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencyCode)currencyCode •[CurrencyCode!](/docs/api/admin-graphql/latest/enums/CurrencyCode) non-null
:   The three letter code for the currency that the shop sells in.

    Show enum values

[Anchor to currencyFormats](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencyFormats)currencyFormats •[CurrencyFormats!](/docs/api/admin-graphql/latest/objects/CurrencyFormats) non-null
:   How currencies are displayed on your store.

    Show fields

[Anchor to currencySettings](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings)currencySettings •[CurrencySettingConnection!](/docs/api/admin-graphql/latest/connections/CurrencySettingConnection) non-null
:   The presentment currency settings for the shop excluding the shop's own currency.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.currencySettings.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to customerAccounts](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customerAccounts)customerAccounts •[ShopCustomerAccountsSetting!](/docs/api/admin-graphql/latest/enums/ShopCustomerAccountsSetting) non-null
:   Whether customer accounts are required, optional, or disabled for the shop.

    Show enum values

[Anchor to customerAccountsV2](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customerAccountsV2)customerAccountsV2 •[CustomerAccountsV2!](/docs/api/admin-graphql/latest/objects/CustomerAccountsV2) non-null
:   Information about the shop's customer accounts.

    Show fields

[Anchor to customerTags](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customerTags)customerTags •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-null
:   A list of tags that have been added to customer accounts.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customerTags.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to description](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.description)description •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The shop's meta description used in search engine results.

[Anchor to draftOrderTags](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.draftOrderTags)draftOrderTags •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-null
:   A list of tags that have been added to draft orders.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.draftOrderTags.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to email](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.email)email •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop owner's email address.
    Shopify will use this email address to communicate with the shop owner.

[Anchor to enabledPresentmentCurrencies](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.enabledPresentmentCurrencies)enabledPresentmentCurrencies •[[CurrencyCode!]!](/docs/api/admin-graphql/latest/enums/CurrencyCode) non-null
:   The presentment currencies enabled for the shop.

    Show enum values

[Anchor to entitlements](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.entitlements)entitlements •[EntitlementsType!](/docs/api/admin-graphql/latest/objects/EntitlementsType) non-null
:   The entitlements for a shop.

    Show fields

[Anchor to features](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.features)features •[ShopFeatures!](/docs/api/admin-graphql/latest/objects/ShopFeatures) non-null
:   The set of features enabled for the shop.

    Show fields

[Anchor to fulfillmentServices](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentServices)fulfillmentServices •[[FulfillmentService!]!](/docs/api/admin-graphql/latest/objects/FulfillmentService) non-null
:   List of the shop's installed fulfillment services.

    Show fields

[Anchor to ianaTimezone](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.ianaTimezone)ianaTimezone •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop's time zone as defined by the IANA.

[Anchor to id](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to marketingSmsConsentEnabledAtCheckout](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.marketingSmsConsentEnabledAtCheckout)marketingSmsConsentEnabledAtCheckout •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether SMS marketing has been enabled on the shop's checkout configuration settings.

[Anchor to merchantApprovalSignals](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.merchantApprovalSignals)merchantApprovalSignals •[MerchantApprovalSignals](/docs/api/admin-graphql/latest/objects/MerchantApprovalSignals)
:   The approval signals for a shop to support onboarding to channel apps.

    Show fields

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to myshopifyDomain](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.myshopifyDomain)myshopifyDomain •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop's .myshopify.com domain name.

[Anchor to name](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.name)name •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop's name.

[Anchor to navigationSettings](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.navigationSettings)navigationSettings •[[NavigationItem!]!](/docs/api/admin-graphql/latest/objects/NavigationItem) non-null
:   The shop's settings related to navigation.

    Show fields

[Anchor to orderNumberFormatPrefix](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orderNumberFormatPrefix)orderNumberFormatPrefix •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The prefix that appears before order numbers.

[Anchor to orderNumberFormatSuffix](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orderNumberFormatSuffix)orderNumberFormatSuffix •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The suffix that appears after order numbers.

[Anchor to orderTags](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orderTags)orderTags •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-null
:   A list of tags that have been added to orders.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orderTags.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to sort](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orderTags.arguments.sort)sort •[ShopTagSort](/docs/api/admin-graphql/latest/enums/ShopTagSort) Default:ALPHABETICAL
    :   Sort type.

        Show enum values

    ---

[Anchor to paymentSettings](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.paymentSettings)paymentSettings •[PaymentSettings!](/docs/api/admin-graphql/latest/objects/PaymentSettings) non-null
:   The shop's settings related to payments.

    Show fields

[Anchor to plan](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.plan)plan •[ShopPlan!](/docs/api/admin-graphql/latest/objects/ShopPlan) non-null
:   The shop's billing plan.

    Show fields

[Anchor to primaryDomain](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.primaryDomain)primaryDomain •[Domain!](/docs/api/admin-graphql/latest/objects/Domain) non-null
:   The primary domain of the shop's online store.

    Show fields

[Anchor to resourceLimits](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.resourceLimits)resourceLimits •[ShopResourceLimits!](/docs/api/admin-graphql/latest/objects/ShopResourceLimits) non-null
:   The shop's limits for specific resources. For example, the maximum number ofvariants allowed per product, or the maximum number of locations allowed.

    Show fields

[Anchor to richTextEditorUrl](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.richTextEditorUrl)richTextEditorUrl •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-null
:   The URL of the rich text editor that can be used for mobile devices.

[Anchor to search](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.search)search •[SearchResultConnection!](/docs/api/admin-graphql/latest/connections/SearchResultConnection) non-null
:   Fetches a list of admin search results by a specified query.

    Show fields

    ### Arguments

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.search.arguments.query)query •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The search query to filter by.

    [Anchor to types](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.search.arguments.types)types •[[SearchResultType!]](/docs/api/admin-graphql/latest/enums/SearchResultType)
    :   The search result types to filter by.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.search.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.search.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to searchFilters](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.searchFilters)searchFilters •[SearchFilterOptions!](/docs/api/admin-graphql/latest/objects/SearchFilterOptions) non-null
:   The list of search filter options for the shop. These can be used to filter productvisibility for the shop.

    Show fields

[Anchor to setupRequired](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.setupRequired)setupRequired •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the shop has outstanding setup steps.

[Anchor to shipsToCountries](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.shipsToCountries)shipsToCountries •[[CountryCode!]!](/docs/api/admin-graphql/latest/enums/CountryCode) non-null
:   The list of countries that the shop ships to.

    Show enum values

[Anchor to shopAddress](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.shopAddress)shopAddress •[ShopAddress!](/docs/api/admin-graphql/latest/objects/ShopAddress) non-null
:   The shop's address information as it will appear to buyers.

    Show fields

[Anchor to shopOwnerName](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.shopOwnerName)shopOwnerName •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The name of the shop owner.

[Anchor to shopPolicies](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.shopPolicies)shopPolicies •[[ShopPolicy!]!](/docs/api/admin-graphql/latest/objects/ShopPolicy) non-null
:   The list of all legal policies associated with a shop.

    Show fields

[Anchor to storefrontAccessTokens](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens)storefrontAccessTokens •[StorefrontAccessTokenConnection!](/docs/api/admin-graphql/latest/connections/StorefrontAccessTokenConnection) non-null
:   The storefront access token of a private application. These are scoped per-application.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontAccessTokens.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to taxesIncluded](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.taxesIncluded)taxesIncluded •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether applicable taxes are included in the shop's product prices.

[Anchor to taxShipping](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.taxShipping)taxShipping •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the shop charges taxes for shipping.

[Anchor to timezoneAbbreviation](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.timezoneAbbreviation)timezoneAbbreviation •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop's time zone abbreviation.

[Anchor to timezoneOffset](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.timezoneOffset)timezoneOffset •[String!](/docs/api/admin-graphql/latest/scalars/String) non-null
:   The shop's time zone offset.

[Anchor to timezoneOffsetMinutes](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.timezoneOffsetMinutes)timezoneOffsetMinutes •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-null
:   The shop's time zone offset expressed as a number of minutes.

[Anchor to transactionalSmsDisabled](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.transactionalSmsDisabled)transactionalSmsDisabled •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether transactional SMS sent by Shopify have been disabled for a shop.

[Anchor to translations](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

[Anchor to unitSystem](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.unitSystem)unitSystem •[UnitSystem!](/docs/api/admin-graphql/latest/enums/UnitSystem) non-null
:   The shop's unit system for weights and measures.

    Show enum values

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the shop was last updated.

[Anchor to url](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.url)url •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-null
:   The URL of the shop's online store.

[Anchor to weightUnit](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.weightUnit)weightUnit •[WeightUnit!](/docs/api/admin-graphql/latest/enums/WeightUnit) non-null
:   The shop's primary unit of weight for products and shipping.

    Show enum values

### Deprecated fields

* allProductCategories ([ProductCategory!]!): deprecated
* analyticsToken (String!): deprecated
* assignedFulfillmentOrders (FulfillmentOrderConnection!): deprecated
* billingAddress (ShopAddress!): deprecated
* channels (ChannelConnection!): deprecated
* collections (CollectionConnection!): deprecated
* customers (CustomerConnection!): deprecated
* domains ([Domain!]!): deprecated
* fulfillmentOrders (FulfillmentOrderConnection!): deprecated
* inventoryItems (InventoryItemConnection!): deprecated
* limitedPendingOrderCount (LimitedPendingOrderCount!): deprecated
* locations (LocationConnection!): deprecated
* metafieldDefinitions (MetafieldDefinitionConnection!): deprecated
* orders (OrderConnection!): deprecated
* productImages (ImageConnection!): deprecated
* products (ProductConnection!): deprecated
* productTags (StringConnection!): deprecated
* productTypes (StringConnection!): deprecated
* productVariants (ProductVariantConnection!): deprecated
* productVendors (StringConnection!): deprecated
* publicationCount (Int!): deprecated
* staffMembers (StaffMemberConnection!): deprecated
* storefrontUrl (URL!): deprecated

[Anchor to allProductCategories](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.allProductCategories)allProductCategories •[[ProductCategory!]!](/docs/api/admin-graphql/latest/objects/ProductCategory) non-nullDeprecated
:   Show fields

[Anchor to analyticsToken](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.analyticsToken)analyticsToken •[String!](/docs/api/admin-graphql/latest/scalars/String) non-nullDeprecated

[Anchor to assignedFulfillmentOrders](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders)assignedFulfillmentOrders •[FulfillmentOrderConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to assignmentStatus](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.assignmentStatus)assignmentStatus •[FulfillmentOrderAssignmentStatus](/docs/api/admin-graphql/latest/enums/FulfillmentOrderAssignmentStatus)
    :   The assigment status of the fulfillment orders that should be returned.
        If `assignmentStatus` argument is not provided, then
        the query will return all assigned fulfillment orders,
        except those that have the `CLOSED` status.

        Show enum values

    [Anchor to locationIds](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.locationIds)locationIds •[[ID!]](/docs/api/admin-graphql/latest/scalars/ID)
    :   Returns fulfillment orders only for certain locations, specified by a list of location IDs.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.assignedFulfillmentOrders.arguments.sortKey)sortKey •[FulfillmentOrderSortKeys](/docs/api/admin-graphql/latest/enums/FulfillmentOrderSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    ---

[Anchor to billingAddress](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.billingAddress)billingAddress •[ShopAddress!](/docs/api/admin-graphql/latest/objects/ShopAddress) non-nullDeprecated
:   Show fields

[Anchor to channels](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels)channels •[ChannelConnection!](/docs/api/admin-graphql/latest/connections/ChannelConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.channels.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to collections](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections)collections •[CollectionConnection!](/docs/api/admin-graphql/latest/connections/CollectionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.sortKey)sortKey •[CollectionSortKeys](/docs/api/admin-graphql/latest/enums/CollectionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-collection_type) collection\_type •string


        Valid values:

        * `custom`
        * `smart`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-handle) handle •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_id) product\_id •id
        :   Filter by collections containing a product by its ID.

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_publication_status) product\_publication\_status •string
        :   Filter by channel approval process status of the resource on a channel, such as the online store. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.app) (`Channel.app.id`) and one of the valid values. For simple visibility checks, use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) instead.

        Valid values:

        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-rejected`
        * `* {channel_app_id}-needs_action`
        * `* {channel_app_id}-awaiting_review`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-demoted`
        * `* {channel_app_id}-scheduled`
        * `* {channel_app_id}-provisionally_published`

        Example:

        * `product_publication_status:189769876-approved`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-published_at) published\_at •time
        :   Filter by the date and time when the collection was published to the Online Store.

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-published_status) published\_status •string
        :   Filter resources by their visibility and publication state on a channel. Online store channel filtering: - `online_store_channel`: Returns all resources in the online store channel, regardless of publication status. - `published`/`visible`: Returns resources that are published to the online store. - `unpublished`: Returns resources that are not published to the online store. Channel-specific filtering using the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) with suffixes: - `{channel_app_id}-published`: Returns resources published to the specified channel. - `{channel_app_id}-visible`: Same as `{channel_app_id}-published` (kept for backwards compatibility). - `{channel_app_id}-intended`: Returns resources added to the channel but not yet published. - `{channel_app_id}-hidden`: Returns resources not added to the channel or not published. Other: - `unavailable`: Returns resources not published to any channel.

        Valid values:

        * `online_store_channel`
        * `published`
        * `visible`
        * `unpublished`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-visible`
        * `* {channel_app_id}-intended`
        * `* {channel_app_id}-hidden`
        * `unavailable`

        Example:

        * `published_status:online_store_channel`
        * `published_status:published`
        * `published_status:580111-published`
        * `published_status:580111-hidden`
        * `published_status:unavailable`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-title) title •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.collections.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

[Anchor to customers](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers)customers •[CustomerConnection!](/docs/api/admin-graphql/latest/connections/CustomerConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.sortKey)sortKey •[CustomerSortKeys](/docs/api/admin-graphql/latest/enums/CustomerSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.customers.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-accepts_marketing) accepts\_marketing •boolean
        :   Filter by whether a customer has consented to receive marketing material.

        Example:

        * `accepts_marketing:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-country) country •string
        :   Filter by the country associated with the customer's address. Use either the country name or the two-letter country code.

        Example:

        * `country:Canada`
        * `country:JP`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-customer_date) customer\_date •time
        :   Filter by the date and time when the customer record was created. This query parameter filters by the [`createdAt`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-createdAt) field.

        Example:

        * `customer_date:'2024-03-15T14:30:00Z'`
        * `customer_date: >='2024-01-01'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-email) email •string
        :   The customer's email address, used to communicate information about orders and for the purposes of email marketing campaigns. You can use a wildcard value to filter the query by customers who have an email address specified. Please note that *email* is a tokenized field: To retrieve exact matches, quote the email address (*phrase query*) as described in [Shopify API search syntax](https://shopify.dev/docs/api/usage/search-syntax).

        Example:

        * `email:gmail.com`
        * `email:"bo.wang@example.com"`
        * `email:*`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-first_name) first\_name •string
        :   Filter by the customer's first name.

        Example:

        * `first_name:Jane`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-last_abandoned_order_date) last\_abandoned\_order\_date •time
        :   Filter by the date and time of the customer's most recent abandoned checkout. An abandoned checkout occurs when a customer adds items to their cart, begins the checkout process, but leaves the site without completing their purchase.

        Example:

        * `last_abandoned_order_date:'2024-04-01T10:00:00Z'`
        * `last_abandoned_order_date: >='2024-01-01'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-last_name) last\_name •string
        :   Filter by the customer's last name.

        Example:

        * `last_name:Reeves`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-order_date) order\_date •time
        :   Filter by the date and time that the order was placed by the customer. Use this query filter to check if a customer has placed at least one order within a specified date range.

        Example:

        * `order_date:'2024-02-20T00:00:00Z'`
        * `order_date: >='2024-01-01'`
        * `order_date:'2024-01-01..2024-03-31'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-orders_count) orders\_count •integer
        :   Filter by the total number of orders a customer has placed.

        Example:

        * `orders_count:5`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-phone) phone •string
        :   The phone number of the customer, used to communicate information about orders and for the purposes of SMS marketing campaigns. You can use a wildcard value to filter the query by customers who have a phone number specified.

        Example:

        * `phone:+18005550100`
        * `phone:*`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-state) state •string
        :   Filter by the [state](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer#field-state) of the customer's account with the shop. This filter is only valid when [Classic Customer Accounts](https://shopify.dev/docs/api/admin-graphql/latest/objects/CustomerAccountsV2#field-customerAccountsVersion) is active.

        Example:

        * `state:ENABLED`
        * `state:INVITED`
        * `state:DISABLED`
        * `state:DECLINED`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag) tag •string
        :   Filter by the tags that are associated with the customer. This query parameter accepts multiple tags separated by commas.

        Example:

        * `tag:'VIP'`
        * `tag:'Wholesale,Repeat'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag_not) tag\_not •string
        :   Filter by the tags that aren't associated with the customer. This query parameter accepts multiple tags separated by commas.

        Example:

        * `tag_not:'Prospect'`
        * `tag_not:'Test,Internal'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-total_spent) total\_spent •float
        :   Filter by the total amount of money a customer has spent across all orders.

        Example:

        * `total_spent:100.50`
        * `total_spent:50.00`
        * `total_spent:>100.50`
        * `total_spent:>50.00`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time
        :   The date and time, matching a whole day, when the customer's information was last updated.

        Example:

        * `updated_at:2024-01-01T00:00:00Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to domains](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.domains)domains •[[Domain!]!](/docs/api/admin-graphql/latest/objects/Domain) non-nullDeprecated
:   Show fields

[Anchor to fulfillmentOrders](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders)fulfillmentOrders •[FulfillmentOrderConnection!](/docs/api/admin-graphql/latest/connections/FulfillmentOrderConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to includeClosed](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.includeClosed)includeClosed •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to include closed fulfillment orders.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.sortKey)sortKey •[FulfillmentOrderSortKeys](/docs/api/admin-graphql/latest/enums/FulfillmentOrderSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.fulfillmentOrders.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-assigned_location_id) assigned\_location\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-status) status •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time

    ---

[Anchor to inventoryItems](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems)inventoryItems •[InventoryItemConnection!](/docs/api/admin-graphql/latest/connections/InventoryItemConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.inventoryItems.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-sku) sku •string
        :   Filter by the inventory item [`sku`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time

    ---

[Anchor to limitedPendingOrderCount](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.limitedPendingOrderCount)limitedPendingOrderCount •[LimitedPendingOrderCount!](/docs/api/admin-graphql/latest/objects/LimitedPendingOrderCount) non-nullDeprecated
:   Show fields

[Anchor to locations](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations)locations •[LocationConnection!](/docs/api/admin-graphql/latest/connections/LocationConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.sortKey)sortKey •[LocationSortKeys](/docs/api/admin-graphql/latest/enums/LocationSortKeys) Default:NAME
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-active) active •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-address1) address1 •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-address2) address2 •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-city) city •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-country) country •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-geolocated) geolocated •boolean

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-legacy) legacy •boolean

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-location_id) location\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-name) name •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-pickup_in_store) pickup\_in\_store •string


        Valid values:

        * `enabled`
        * `disabled`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-province) province •string

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-zip) zip •string

    [Anchor to includeLegacy](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.includeLegacy)includeLegacy •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to include the legacy locations of fulfillment services.

    [Anchor to includeInactive](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.locations.arguments.includeInactive)includeInactive •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Whether to include the locations that are deactivated.

    ---

[Anchor to metafieldDefinitions](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions)metafieldDefinitions •[MetafieldDefinitionConnection!](/docs/api/admin-graphql/latest/connections/MetafieldDefinitionConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   Filter metafield definitions by namespace.

    [Anchor to pinnedStatus](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.pinnedStatus)pinnedStatus •[MetafieldDefinitionPinnedStatus](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionPinnedStatus) Default:ANY
    :   Filter by the definition's pinned status.

        Show enum values

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.sortKey)sortKey •[MetafieldDefinitionSortKeys](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.metafieldDefinitions.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the metafield definition was created.

        Example:

        * `created_at:>2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-key) key •string
        :   Filter by the metafield definition [`key`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-key) field.

        Example:

        * `key:some-key`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-namespace) namespace •string
        :   Filter by the metafield definition [`namespace`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-namespace) field.

        Example:

        * `namespace:some-namespace`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-owner_type) owner\_type •string
        :   Filter by the metafield definition [`ownerType`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-ownertype) field.

        Example:

        * `owner_type:PRODUCT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-type) type •string
        :   Filter by the metafield definition [`type`](https://shopify.dev/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-type) field.

        Example:

        * `type:single_line_text_field`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the metafield definition was last updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to orders](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders)orders •[OrderConnection!](/docs/api/admin-graphql/latest/connections/OrderConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.sortKey)sortKey •[OrderSortKeys](/docs/api/admin-graphql/latest/enums/OrderSortKeys) Default:PROCESSED\_AT
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.orders.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-cart_token) cart\_token •string
        :   Filter by the cart token's unique value to track abandoned cart conversions or troubleshoot checkout issues. The token references the cart that's associated with an order.

        Example:

        * `cart_token:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-channel) channel •string
        :   Filter by the channel information [`handle`](https://shopify.dev/api/admin-graphql/latest/objects/ChannelInformation#field-ChannelInformation.fields.channelDefinition.handle) (`ChannelInformation.channelDefinition.handle`) field.

        Example:

        * `channel:web`
        * `channel:web,pos`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-channel_id) channel\_id •id
        :   Filter by the channel [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.id) field.

        Example:

        * `channel_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-chargeback_status) chargeback\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-checkout_token) checkout\_token •string
        :   Filter by the checkout token's unique value to analyze conversion funnels or resolve payment issues. The checkout token's value references the checkout that's associated with an order.

        Example:

        * `checkout_token:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-confirmation_number) confirmation\_number •string
        :   Filter by the randomly generated alpha-numeric identifier for an order that can be displayed to the customer instead of the sequential order name. This value isn't guaranteed to be unique.

        Example:

        * `confirmation_number:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the order was created in Shopify's system.

        Example:

        * `created_at:2020-10-21T23:39:20Z`
        * `created_at:<now`
        * `created_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-credit_card_last4) credit\_card\_last4 •string
        :   Filter by the last four digits of the payment card that was used to pay for the order. This filter matches only the last four digits of the card for heightened security.

        Example:

        * `credit_card_last4:1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-current_total_price) current\_total\_price •float
        :   Filter by the current total price of the order in the shop currency, including any returns/refunds/removals. This filter supports both exact values and ranges.

        Example:

        * `current_total_price:10`
        * `current_total_price:>=5.00 current_total_price:<=20.99`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-customer_id) customer\_id •id
        :   Filter orders by the customer [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Customer#field-Customer.fields.id) field.

        Example:

        * `customer_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-delivery_method) delivery\_method •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-discount_code) discount\_code •string
        :   Filter by the case-insensitive discount code that was applied to the order at checkout. Limited to the first discount code used on an order. Maximum characters: 255.

        Example:

        * `discount_code:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-email) email •string
        :   Filter by the email address that's associated with the order to provide customer support or analyze purchasing patterns.

        Example:

        * `email:example@shopify.com`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-financial_status) financial\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-fraud_protection_level) fraud\_protection\_level •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-fulfillment_location_id) fulfillment\_location\_id •id
        :   Filter by the fulfillment location [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Fulfillment#field-Fulfillment.fields.location.id) (`Fulfillment.location.id`) field.

        Example:

        * `fulfillment_location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-fulfillment_status) fulfillment\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-gateway) gateway •string
        :   Filter by the [`paymentGatewayNames`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.paymentGatewayNames) field. Use this filter to find orders that were processed through specific payment providers like Shopify Payments, PayPal, or other custom payment gateways.

        Example:

        * `gateway:shopify_payments`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-location_id) location\_id •id
        :   Filter by the location [`id`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id) that's associated with the order to view and manage orders for specific locations. For POS orders, locations must be defined in the Shopify admin under **Settings** > **Locations**. If no ID is provided, then the primary location of the shop is returned.

        Example:

        * `location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
        :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

        Example:

        * `metafields.custom.on_sale:true`
        * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-name) name •string
        :   Filter by the order [`name`](https://shopify.dev/api/admin-graphql/latest/objects/Order#field-name) field.

        Example:

        * `name:1001-A`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-payment_id) payment\_id •string
        :   Filter by the payment ID that's associated with the order to reconcile financial records or troubleshoot payment issues.

        Example:

        * `payment_id:abc123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-payment_provider_id) payment\_provider\_id •id
        :   Filter by the ID of the payment provider that's associated with the order to manage payment methods or troubleshoot transactions.

        Example:

        * `payment_provider_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-po_number) po\_number •string
        :   Filter by the order [`poNumber`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.poNumber) field.

        Example:

        * `po_number:P01001`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-processed_at) processed\_at •time
        :   Filter by the order [`processedAt`](https://shopify.dev/api/admin-graphql/latest/objects/order#field-Order.fields.processedAt) field.

        Example:

        * `processed_at:2021-01-01T00:00:00Z`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-reference_location_id) reference\_location\_id •id
        :   Filter by the ID of a location that's associated with the order, such as locations from fulfillments, refunds, or the shop's primary location.

        Example:

        * `reference_location_id:123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-return_status) return\_status •string
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

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-risk_level) risk\_level •string
        :   Filter by the order risk assessment [`riskLevel`](https://shopify.dev/api/admin-graphql/latest/objects/OrderRiskAssessment#field-OrderRiskAssessment.fields.riskLevel) field.

        Valid values:

        * `high`
        * `medium`
        * `low`
        * `none`
        * `pending`

        Example:

        * `risk_level:high`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-sales_channel) sales\_channel •string
        :   Filter by the [sales channel](https://shopify.dev/docs/apps/build/sales-channels) where the order was made to analyze performance or manage fulfillment processes.

        Example:

        * `sales_channel: some_sales_channel`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:ABC123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-source_identifier) source\_identifier •string
        :   Filter by the ID of the order placed on the originating platform, such as a unique POS or third-party identifier. This value doesn't correspond to the Shopify ID that's generated from a completed draft order.

        Example:

        * `source_identifier:1234-12-1000`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-source_name) source\_name •string
        :   Filter by the platform where the order was placed to distinguish between web orders, POS sales, draft orders, or third-party channels. Use this filter to analyze sales performance across different ordering methods.

        Example:

        * `source_name:web`
        * `source_name:shopify_draft_order`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-status) status •string
        :   Filter by the order's status to manage workflows or analyze the order lifecycle.

        Valid values:

        * `open`
        * `closed`
        * `cancelled`
        * `not_closed`

        Example:

        * `status:open`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-subtotal_line_items_quantity) subtotal\_line\_items\_quantity •string
        :   Filter by the total number of items across all line items in an order. This filter supports both exact values and ranges, and is useful for identifying bulk orders or analyzing purchase volume patterns.

        Example:

        * `subtotal_line_items_quantity:10`
        * `subtotal_line_items_quantity:5..20`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-test) test •boolean
        :   Filter by test orders. Test orders are made using the [Shopify Bogus Gateway](https://help.shopify.com/manual/checkout-settings/test-orders/payments-test-mode#bogus-gateway) or a payment provider with test mode enabled.

        Example:

        * `test:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-total_weight) total\_weight •string
        :   Filter by the order weight. This filter supports both exact values and ranges, and is to be used to filter orders by the total weight of all items (excluding packaging). It takes a unit of measurement as a suffix. It accepts the following units: g, kg, lb, oz.

        Example:

        * `total_weight:10.5kg`
        * `total_weight:>=5g total_weight:<=20g`
        * `total_weight:.5 lb`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the order was last updated in Shopify's system.

        Example:

        * `updated_at:2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

    ---

[Anchor to productImages](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages)productImages •[ImageConnection!](/docs/api/admin-graphql/latest/connections/ImageConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to maxWidth](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.maxWidth)maxWidth •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to maxHeight](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.maxHeight)maxHeight •[Int](/docs/api/admin-graphql/latest/scalars/Int) Deprecated

    [Anchor to crop](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.crop)crop •[CropRegion](/docs/api/admin-graphql/latest/enums/CropRegion) Deprecated
    :   Show enum values

    [Anchor to scale](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.scale)scale •[Int](/docs/api/admin-graphql/latest/scalars/Int) DeprecatedDefault:1

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productImages.arguments.sortKey)sortKey •[ProductImageSortKeys](/docs/api/admin-graphql/latest/enums/ProductImageSortKeys) Default:CREATED\_AT
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    ---

[Anchor to products](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products)products •[ProductConnection!](/docs/api/admin-graphql/latest/connections/ProductConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.sortKey)sortKey •[ProductSortKeys](/docs/api/admin-graphql/latest/enums/ProductSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-barcode) barcode •string
        :   Filter by the product variant [`barcode`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-barcode) field.

        Example:

        * `barcode:ABC-abc-1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-bundles) bundles •boolean
        :   Filter by a [product bundle](https://shopify.dev/docs/apps/build/product-merchandising/bundles). A product bundle is a set of two or more related products, which are commonly offered at a discount.

        Example:

        * `bundles:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-category_id) category\_id •string
        :   Filter by the product [category ID](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-category) (`product.category.id`). A product category is the category of a product from [Shopify's Standard Product Taxonomy](https://shopify.github.io/product-taxonomy/releases/unstable/?categoryId=sg-4-17-2-17).

        Example:

        * `category_id:sg-4-17-2-17`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-collection_id) collection\_id •id
        :   Filter by the collection [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Collection#field-id) field.

        Example:

        * `collection_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-combined_listing_role) combined\_listing\_role •string
        :   Filter by the role of the product in a [combined listing](https://shopify.dev/apps/build/product-merchandising/combined-listings).

        Valid values:

        * `parent`
        * `child`
        * `no_role`

        Example:

        * `combined_listing_role:parent`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-created_at) created\_at •time
        :   Filter by the date and time when the product was created.

        Example:

        * `created_at:>'2020-10-21T23:39:20Z'`
        * `created_at:<now`
        * `created_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-delivery_profile_id) delivery\_profile\_id •id
        :   Filter by the delivery profile [`id`](https://shopify.dev/api/admin-graphql/latest/objects/DeliveryProfile#field-id) field.

        Example:

        * `delivery_profile_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-error_feedback) error\_feedback •string
        :   Filter by products with publishing errors.

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-gift_card) gift\_card •boolean
        :   Filter by the product [`isGiftCard`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-isgiftcard) field.

        Example:

        * `gift_card:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-handle) handle •string
        :   Filter by a comma-separated list of product [handles](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-handle).

        Example:

        * `handle:the-minimal-snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-has_only_composites) has\_only\_composites •boolean
        :   Filter by products that have only composite variants.

        Example:

        * `has_only_composites:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-has_only_default_variant) has\_only\_default\_variant •boolean
        :   Filter by products that have only a default variant. A default variant is the only variant if no other variants are specified.

        Example:

        * `has_only_default_variant:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-has_variant_with_components) has\_variant\_with\_components •boolean
        :   Filter by products that have variants with associated components.

        Example:

        * `has_variant_with_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-inventory_total) inventory\_total •integer
        :   Filter by inventory count.

        Example:

        * `inventory_total:0`
        * `inventory_total:>150`
        * `inventory_total:>=200`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-is_price_reduced) is\_price\_reduced •boolean
        :   Filter by products that have a reduced price. For more information, refer to the [`CollectionRule`](https://shopify.dev/api/admin-graphql/latest/objects/CollectionRule) object.

        Example:

        * `is_price_reduced:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-metafields.{namespace}.{key}) metafields.{namespace}.{key} •mixed
        :   Filters resources by metafield value. Format: `metafields.{namespace}.{key}:{value}`. Learn more about [querying by metafield value](https://shopify.dev/apps/build/custom-data/metafields/query-by-metafield-value).

        Example:

        * `metafields.custom.on_sale:true`
        * `metafields.product.material:"gid://shopify/Metaobject/43458085"`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-out_of_stock_somewhere) out\_of\_stock\_somewhere •boolean
        :   Filter by products that are out of stock in at least one location.

        Example:

        * `out_of_stock_somewhere:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-price) price •bigdecimal
        :   Filter by the product variant [`price`](https://shopify.dev/api/admin-graphql/latest/objects/Productvariant#field-price) field.

        Example:

        * `price:100.57`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_configuration_owner) product\_configuration\_owner •string
        :   Filter by the app [`id`](https://shopify.dev/api/admin-graphql/latest/objects/App#field-id) field.

        Example:

        * `product_configuration_owner:10001`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_publication_status) product\_publication\_status •string
        :   Filter by channel approval process status of the resource on a channel, such as the online store. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.app) (`Channel.app.id`) and one of the valid values. For simple visibility checks, use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) instead.

        Valid values:

        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-rejected`
        * `* {channel_app_id}-needs_action`
        * `* {channel_app_id}-awaiting_review`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-demoted`
        * `* {channel_app_id}-scheduled`
        * `* {channel_app_id}-provisionally_published`

        Example:

        * `product_publication_status:189769876-approved`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_type) product\_type •string
        :   Filter by a comma-separated list of [product types](https://help.shopify.com/manual/products/details/product-type).

        Example:

        * `product_type:snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-publication_ids) publication\_ids •string
        :   Filter by a comma-separated list of publication IDs that are associated with the product.

        Example:

        * `publication_ids:184111530305,184111694145`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-published_at) published\_at •time
        :   Filter by the date and time when the product was published to the online store and other sales channels.

        Example:

        * `published_at:>2020-10-21T23:39:20Z`
        * `published_at:<now`
        * `published_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-published_status) published\_status •string
        :   Filter resources by their visibility and publication state on a channel. Online store channel filtering: - `online_store_channel`: Returns all resources in the online store channel, regardless of publication status. - `published`/`visible`: Returns resources that are published to the online store. - `unpublished`: Returns resources that are not published to the online store. Channel-specific filtering using the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) with suffixes: - `{channel_app_id}-published`: Returns resources published to the specified channel. - `{channel_app_id}-visible`: Same as `{channel_app_id}-published` (kept for backwards compatibility). - `{channel_app_id}-intended`: Returns resources added to the channel but not yet published. - `{channel_app_id}-hidden`: Returns resources not added to the channel or not published. Other: - `unavailable`: Returns resources not published to any channel.

        Valid values:

        * `online_store_channel`
        * `published`
        * `visible`
        * `unpublished`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-visible`
        * `* {channel_app_id}-intended`
        * `* {channel_app_id}-hidden`
        * `unavailable`

        Example:

        * `published_status:online_store_channel`
        * `published_status:published`
        * `published_status:580111-published`
        * `published_status:580111-hidden`
        * `published_status:unavailable`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-status) status •string
        :   Filter by a comma-separated list of statuses. You can use statuses to manage inventory. Shopify only displays products with an `ACTIVE` status in online stores, sales channels, and apps.

        Valid values:

        * `active` Default
        * `archived`
        * `draft`

        Example:

        * `status:active,draft`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-title) title •string
        :   Filter by the product [`title`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-title) field.

        Example:

        * `title:The Minimal Snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time
        :   Filter by the date and time when the product was last updated.

        Example:

        * `updated_at:>'2020-10-21T23:39:20Z'`
        * `updated_at:<now`
        * `updated_at:<='2024'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-variant_id) variant\_id •id
        :   Filter by the product variant [`id`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-id) field.

        Example:

        * `variant_id:45779434701121`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-variant_title) variant\_title •string
        :   Filter by the product variant [`title`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-title) field.

        Example:

        * `variant_title:'Special ski wax'`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-vendor) vendor •string
        :   Filter by the origin or source of the product. Learn more about [vendors and managing vendor information](https://help.shopify.com/manual/products/managing-vendor-info).

        Example:

        * `vendor:Snowdevil`
        * `vendor:Snowdevil OR vendor:Icedevil`

    [Anchor to savedSearchId](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.products.arguments.savedSearchId)savedSearchId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   The ID of a [saved search](https://shopify.dev/api/admin-graphql/latest/objects/savedsearch#field-id).
        The search’s query string is used as the query argument.

    ---

[Anchor to productTags](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productTags)productTags •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productTags.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to productTypes](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productTypes)productTypes •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productTypes.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to productVariants](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants)productVariants •[ProductVariantConnection!](/docs/api/admin-graphql/latest/connections/ProductVariantConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to sortKey](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.sortKey)sortKey •[ProductVariantSortKeys](/docs/api/admin-graphql/latest/enums/ProductVariantSortKeys) Default:ID
    :   Sort the underlying list using a key. If your query is slow or returns an error, then [try specifying a sort key that matches the field used in the search](https://shopify.dev/api/usage/pagination-graphql#search-performance-considerations).

        Show enum values

    [Anchor to query](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVariants.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-default) default •string
        :   Filter by a case-insensitive search of multiple fields in a document.

        Example:

        * `query=Bob Norman`
        * `query=title:green hoodie`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-barcode) barcode •string
        :   Filter by the product variant [`barcode`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-barcode) field.

        Example:

        * `barcode:ABC-abc-123`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-collection) collection •string
        :   Filter by the [ID of the collection](https://shopify.dev/api/admin-graphql/latest/objects/Collection#field-id) that the product variant belongs to.

        Example:

        * `collection:465903092033`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-delivery_profile_id) delivery\_profile\_id •id
        :   Filter by the product variant [delivery profile ID](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-deliveryprofile) (`ProductVariant.deliveryProfile.id`).

        Example:

        * `delivery_profile_id:108179161409`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-exclude_composite) exclude\_composite •boolean
        :   Filter by product variants that aren't composites.

        Example:

        * `exclude_composite:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-exclude_variants_with_components) exclude\_variants\_with\_components •boolean
        :   Filter by whether there are [components](https://shopify.dev/docs/apps/build/product-merchandising/bundles/add-product-fixed-bundle) that are associated with the product variants in a bundle.

        Example:

        * `exclude_variants_with_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-gift_card) gift\_card •boolean
        :   Filter by the product [`isGiftCard`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-isgiftcard) field.

        Example:

        * `gift_card:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-inventory_quantity) inventory\_quantity •integer
        :   Filter by an aggregate of inventory across all locations where the product variant is stocked.

        Example:

        * `inventory_quantity:10`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-location_id) location\_id •id
        :   Filter by the [location ID](https://shopify.dev/api/admin-graphql/latest/objects/Location#field-id) for the product variant.

        Example:

        * `location_id:88511152449`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-managed) managed •boolean
        :   Filter by whether there is fulfillment service tracking associated with the product variants.

        Example:

        * `managed:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-managed_by) managed\_by •string
        :   Filter by the fulfillment service that tracks the number of items in stock for the product variant.

        Example:

        * `managed_by:shopify`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-option1) option1 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option1:small`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-option2) option2 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option2:medium`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-option3) option3 •string
        :   Filter by a custom property that a shop owner uses to define product variants.

        Example:

        * `option3:large`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_id) product\_id •id
        :   Filter by the product [`id`](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-id) field.

        Example:

        * `product_id:8474977763649`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_ids) product\_ids •string
        :   Filter by a comma-separated list of product [IDs](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-id).

        Example:

        * `product_ids:8474977763649,8474977796417`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_publication_status) product\_publication\_status •string
        :   Filter by channel approval process status of the resource on a channel, such as the online store. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#field-Channel.fields.app) (`Channel.app.id`) and one of the valid values. For simple visibility checks, use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) instead.

        Valid values:

        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-rejected`
        * `* {channel_app_id}-needs_action`
        * `* {channel_app_id}-awaiting_review`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-demoted`
        * `* {channel_app_id}-scheduled`
        * `* {channel_app_id}-provisionally_published`

        Example:

        * `product_publication_status:189769876-approved`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_status) product\_status •string
        :   Filter by a comma-separated list of product [statuses](https://shopify.dev/api/admin-graphql/latest/objects/Product#field-status).

        Example:

        * `product_status:ACTIVE,DRAFT`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-product_type) product\_type •string
        :   Filter by the product type that's associated with the product variants.

        Example:

        * `product_type:snowboard`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-publishable_status) publishable\_status •string
        :   **Deprecated:** This parameter is deprecated as of 2025-12 and will be removed in a future API version. Use [published\_status](https://shopify.dev/api/admin-graphql/latest/queries/products#argument-query-filter-publishable_status) for visibility checks. Filter by the publishable status of the resource on a channel. The value is a composite of the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) and one of the valid status values.

        Valid values:

        * `* {channel_app_id}-unset`
        * `* {channel_app_id}-pending`
        * `* {channel_app_id}-approved`
        * `* {channel_app_id}-not_approved`

        Example:

        * `publishable_status:580111-unset`
        * `publishable_status:580111-pending`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-published_status) published\_status •string
        :   Filter resources by their visibility and publication state on a channel. Online store channel filtering: - `online_store_channel`: Returns all resources in the online store channel, regardless of publication status. - `published`/`visible`: Returns resources that are published to the online store. - `unpublished`: Returns resources that are not published to the online store. Channel-specific filtering using the [channel `app` ID](https://shopify.dev/api/admin-graphql/latest/objects/Channel#app-price) (`Channel.app.id`) with suffixes: - `{channel_app_id}-published`: Returns resources published to the specified channel. - `{channel_app_id}-visible`: Same as `{channel_app_id}-published` (kept for backwards compatibility). - `{channel_app_id}-intended`: Returns resources added to the channel but not yet published. - `{channel_app_id}-hidden`: Returns resources not added to the channel or not published. Other: - `unavailable`: Returns resources not published to any channel.

        Valid values:

        * `online_store_channel`
        * `published`
        * `visible`
        * `unpublished`
        * `* {channel_app_id}-published`
        * `* {channel_app_id}-visible`
        * `* {channel_app_id}-intended`
        * `* {channel_app_id}-hidden`
        * `unavailable`

        Example:

        * `published_status:online_store_channel`
        * `published_status:published`
        * `published_status:580111-published`
        * `published_status:580111-hidden`
        * `published_status:unavailable`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-requires_components) requires\_components •boolean
        :   Filter by whether the product variant can only be purchased with components. [Learn more](https://shopify.dev/apps/build/product-merchandising/bundles#store-eligibility).

        Example:

        * `requires_components:true`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-sku) sku •string
        :   Filter by the product variant [`sku`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag) tag •string
        :   Filter objects by the `tag` field.

        Example:

        * `tag:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-tag_not) tag\_not •string
        :   Filter by objects that don’t have the specified tag.

        Example:

        * `tag_not:my_tag`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-taxable) taxable •boolean
        :   Filter by the product variant [`taxable`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-taxable) field.

        Example:

        * `taxable:false`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-title) title •string
        :   Filter by the product variant [`title`](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant#field-title) field.

        Example:

        * `title:ice`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-updated_at) updated\_at •time
        :   Filter by date and time when the product variant was updated.

        Example:

        * `updated_at:>2020-10-21T23:39:20Z`
        * `updated_at:<now`
        * `updated_at:<=2024`

        [Anchor to](/docs/api/admin-graphql/latest/objects/Shop#argument-query-filter-vendor) vendor •string
        :   Filter by the origin or source of the product variant. Learn more about [vendors and managing vendor information](https://help.shopify.com/manual/products/managing-vendor-info).

        Example:

        * `vendor:Snowdevil`
        * `vendor:Snowdevil OR vendor:Icedevil`

    ---

[Anchor to productVendors](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVendors)productVendors •[StringConnection!](/docs/api/admin-graphql/latest/connections/StringConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.productVendors.arguments.first)first •[Int!](/docs/api/admin-graphql/latest/scalars/Int) required
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to publicationCount](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.publicationCount)publicationCount •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-nullDeprecated

[Anchor to staffMembers](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers)staffMembers •[StaffMemberConnection!](/docs/api/admin-graphql/latest/connections/StaffMemberConnection) non-nullDeprecated
:   Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.staffMembers.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to storefrontUrl](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.storefrontUrl)storefrontUrl •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-nullDeprecated

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/Shop#queries)Queries

* shop (Shop!)

[Anchor to shop](/docs/api/admin-graphql/latest/objects/Shop#query-shop)[shop](/docs/api/admin-graphql/latest/queries/shop) •query
:   Returns the Shop resource corresponding to the access token used in the request. The Shop resource contains
    business and store management settings for the shop.

    Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/Shop#mutations)Mutations

* collectionDelete (CollectionDeletePayload)
* customerDelete (CustomerDeletePayload)
* delegateAccessTokenCreate (DelegateAccessTokenCreatePayload)
* delegateAccessTokenDestroy (DelegateAccessTokenDestroyPayload)
* productCreate (ProductCreatePayload)
* productDelete (ProductDeletePayload)
* productDuplicate (ProductDuplicatePayload)
* publishablePublish (PublishablePublishPayload)
* publishablePublishToCurrentChannel (PublishablePublishToCurrentChannelPayload)
* publishableUnpublish (PublishableUnpublishPayload)
* publishableUnpublishToCurrentChannel (PublishableUnpublishToCurrentChannelPayload)
* savedSearchDelete (SavedSearchDeletePayload)
* storefrontAccessTokenCreate (StorefrontAccessTokenCreatePayload)

[Anchor to collectionDelete](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionDelete)[collectionDelete](/docs/api/admin-graphql/latest/mutations/collectionDelete) •mutation
:   Deletes a collection and removes it permanently from the store. This operation cannot be undone and will remove the collection from all sales channels where it was published.

    For example, when merchants discontinue seasonal promotions or reorganize their catalog structure, they can delete outdated collections like "Back to School 2023" to keep their store organized.

    Use `CollectionDelete` to:

    * Remove outdated or unused collections from stores
    * Clean up collection structures during catalog reorganization
    * Implement collection management tools with deletion capabilities

    Products within the deleted collection remain in the store but are no longer grouped under that collection.

    Learn more about [collection management](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionDelete.arguments.input)input •[CollectionDeleteInput!](/docs/api/admin-graphql/latest/input-objects/CollectionDeleteInput) required
    :   The collection to delete.

        Show input fields

    ---

[Anchor to customerDelete](/docs/api/admin-graphql/latest/objects/Shop#mutation-customerDelete)[customerDelete](/docs/api/admin-graphql/latest/mutations/customerDelete) •mutation
:   Deletes a [`Customer`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Customer) from the store. You can only delete customers who haven't placed any [orders](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order).

    Apps using protected customer data must meet Shopify's [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-customerDelete.arguments.input)input •[CustomerDeleteInput!](/docs/api/admin-graphql/latest/input-objects/CustomerDeleteInput) required
    :   Specifies the customer to delete.

        Show input fields

    ---

[Anchor to delegateAccessTokenCreate](/docs/api/admin-graphql/latest/objects/Shop#mutation-delegateAccessTokenCreate)[delegateAccessTokenCreate](/docs/api/admin-graphql/latest/mutations/delegateAccessTokenCreate) •mutation
:   Creates a [`DelegateAccessToken`](https://shopify.dev/docs/api/admin-graphql/latest/objects/DelegateAccessToken) with a subset of the parent token's permissions.

    Delegate access tokens enable secure permission delegation to subsystems or services that need limited access to shop resources. Each token inherits only the scopes you specify, ensuring subsystems operate with minimal required permissions rather than full app access.

    Learn more about [delegating access tokens to subsystems](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/use-delegate-tokens).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-delegateAccessTokenCreate.arguments.input)input •[DelegateAccessTokenInput!](/docs/api/admin-graphql/latest/input-objects/DelegateAccessTokenInput) required
    :   The input fields for creating a delegate access token.

        Show input fields

    ---

[Anchor to delegateAccessTokenDestroy](/docs/api/admin-graphql/latest/objects/Shop#mutation-delegateAccessTokenDestroy)[delegateAccessTokenDestroy](/docs/api/admin-graphql/latest/mutations/delegateAccessTokenDestroy) •mutation
:   Destroys a delegate access token.

    Show payload

    ### Arguments

    [Anchor to accessToken](/docs/api/admin-graphql/latest/objects/Shop#mutation-delegateAccessTokenDestroy.arguments.accessToken)accessToken •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Provides the delegate access token to destroy.

    ---

[Anchor to productCreate](/docs/api/admin-graphql/latest/objects/Shop#mutation-productCreate)[productCreate](/docs/api/admin-graphql/latest/mutations/productCreate) •mutation
:   Creates a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
    with attributes such as title, description, vendor, and media.

    The `productCreate` mutation helps you create many products at once, avoiding the tedious or time-consuming
    process of adding them one by one in the Shopify admin. Common examples include creating products for a
    new collection, launching a new product line, or adding seasonal products.

    You can define product
    [options](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption) and
    [values](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOptionValue),
    allowing you to create products with different variations like sizes or colors. You can also associate media
    files to your products, including images and videos.

    The `productCreate` mutation only supports creating a product with its initial
    [product variant](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant).
    To create multiple product variants for a single product and manage prices, use the
    [`productVariantsBulkCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkCreate)
    mutation.

    ---

    Note

    The `productCreate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
    that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
    1,000 new product variants can be created per day.

    **Note:**

    The `productCreate` mutation has a [throttle](https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits)
    that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
    1,000 new product variants can be created per day.

    **Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">product<wbr/>Create</span></code> mutation has a <a href="https://shopify.dev/docs/api/usage/rate-limits#resource-based-rate-limits">throttle</a>
    that takes effect when a store has 50,000 product variants. After this threshold is reached, no more than
    1,000 new product variants can be created per day.

    ---

    After you create a product, you can make subsequent edits to the product using one of the following mutations:

    * [`publishablePublish`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/publishablePublish):
      Used to publish the product and make it available to customers. The `productCreate` mutation creates products
      in an unpublished state by default, so you must perform a separate operation to publish the product.
    * [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productUpdate):
      Used to update a single product, such as changing the product's title, description, vendor, or associated media.
    * [`productSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet):
      Used to perform multiple operations on products, such as creating or modifying product options and variants.

    Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model)
    and [adding product data](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model/add-data).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-productCreate.arguments.input)input •[ProductInput](/docs/api/admin-graphql/latest/input-objects/ProductInput) Deprecated
    :   Show input fields

    [Anchor to product](/docs/api/admin-graphql/latest/objects/Shop#mutation-productCreate.arguments.product)product •[ProductCreateInput](/docs/api/admin-graphql/latest/input-objects/ProductCreateInput)
    :   The attributes of the new product.

        Show input fields

    [Anchor to media](/docs/api/admin-graphql/latest/objects/Shop#mutation-productCreate.arguments.media)media •[[CreateMediaInput!]](/docs/api/admin-graphql/latest/input-objects/CreateMediaInput)
    :   The media to add to the product.

        Show input fields

    ---

[Anchor to productDelete](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDelete)[productDelete](/docs/api/admin-graphql/latest/mutations/productDelete) •mutation
:   Permanently deletes a product and all its associated data, including variants, media, publications, and inventory items.

    Use the `productDelete` mutation to programmatically remove products from your store when they need to be
    permanently deleted from your catalog, such as when removing discontinued items, cleaning up test data, or
    synchronizing with external inventory management systems.

    The `productDelete` mutation removes the product from all associated collections,
    and removes all associated data for the product, including:

    * All product variants and their inventory items
    * Product media (images, videos) that are not referenced by other products
    * [Product options](https://shopify.dev/api/admin-graphql/latest/objects/ProductOption) and [option values](https://shopify.dev/api/admin-graphql/latest/objects/ProductOptionValue)
    * Product publications across all sales channels
    * Product tags and metadata associations

    The `productDelete` mutation also has the following effects on existing orders and transactions:

    * **Draft orders**: Existing draft orders that reference this product will retain the product information as stored data, but the product reference will be removed. Draft orders can still be completed with the stored product details.
    * **Completed orders and refunds**: Previously completed orders that included this product aren't affected. The product information in completed orders is preserved for record-keeping, and existing refunds for this product remain valid and processable.

    ---

    Caution

    Product deletion is irreversible. After a product is deleted, it can't be recovered. Consider archiving
    or unpublishing products instead if you might need to restore them later.

    **Caution:**

    Product deletion is irreversible. After a product is deleted, it can't be recovered. Consider archiving
    or unpublishing products instead if you might need to restore them later.

    **Caution:** Product deletion is irreversible. After a product is deleted, it can&#39;t be recovered. Consider archiving
    or unpublishing products instead if you might need to restore them later.

    ---

    If you need to delete a large product, such as one that has many
    [variants](https://shopify.dev/api/admin-graphql/latest/objects/ProductVariant)
    that are active at several
    [locations](https://shopify.dev/api/admin-graphql/latest/objects/Location),
    you might encounter timeout errors. To avoid these timeout errors, you can set the
    [`synchronous`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productDelete#arguments-synchronous)
    parameter to `false` to run the deletion asynchronously, which returns a
    [`ProductDeleteOperation`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductDeleteOperation)
    that you can monitor for completion status.

    If you need more granular control over product cleanup, consider using these alternative mutations:

    * [`productUpdate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productUpdate):
      Update the product status to archived or unpublished instead of deleting.
    * [`productVariantsBulkDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productVariantsBulkDelete):
      Delete specific variants while keeping the product.
    * [`productOptionsDelete`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productOptionsDelete):
      Delete the choices available for a product, such as size, color, or material.

    Learn more about the [product model](https://shopify.dev/docs/apps/build/graphql/migrate/new-product-model).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDelete.arguments.input)input •[ProductDeleteInput!](/docs/api/admin-graphql/latest/input-objects/ProductDeleteInput) required
    :   Specifies the product to delete by its ID.

        Show input fields

    [Anchor to synchronous](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDelete.arguments.synchronous)synchronous •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Specifies whether or not to run the mutation synchronously.

    ---

[Anchor to productDuplicate](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate)[productDuplicate](/docs/api/admin-graphql/latest/mutations/productDuplicate) •mutation
:   Duplicates a product.

    If you need to duplicate a large product, such as one that has many
    [variants](https://shopify.dev/api/admin-graphql/latest/input-objects/ProductVariantInput)
    that are active at several
    [locations](https://shopify.dev/api/admin-graphql/latest/input-objects/InventoryLevelInput),
    you might encounter timeout errors.

    To avoid these timeout errors, you can instead duplicate the product asynchronously.

    In API version 2024-10 and higher, include `synchronous: false` argument in this mutation to perform the duplication asynchronously.

    In API version 2024-07 and lower, use the asynchronous [`ProductDuplicateAsyncV2`](https://shopify.dev/api/admin-graphql/2024-07/mutations/productDuplicateAsyncV2).

    Metafield values are not duplicated if the unique values capability is enabled.

    Show payload

    ### Arguments

    [Anchor to productId](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.productId)productId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the product to be duplicated.

    [Anchor to newTitle](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.newTitle)newTitle •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The new title of the product.

    [Anchor to newStatus](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.newStatus)newStatus •[ProductStatus](/docs/api/admin-graphql/latest/enums/ProductStatus)
    :   The new status of the product. If no value is provided the status will be inherited from the original product.

        Show enum values

    [Anchor to includeImages](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.includeImages)includeImages •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Specifies whether or not to duplicate images.

    [Anchor to includeTranslations](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.includeTranslations)includeTranslations •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Specifies whether or not to duplicate translations.

    [Anchor to synchronous](/docs/api/admin-graphql/latest/objects/Shop#mutation-productDuplicate.arguments.synchronous)synchronous •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:true
    :   Specifies whether or not to run the mutation synchronously.

    ---

[Anchor to publishablePublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishablePublish)[publishablePublish](/docs/api/admin-graphql/latest/mutations/publishablePublish) •mutation
:   Publishes a resource, such as a [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) or [`Collection`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection), to one or more [publications](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication).

    For products to be visible in a channel, they must have an active [`ProductStatus`](https://shopify.dev/docs/api/admin-graphql/latest/enums/ProductStatus). Products sold exclusively on subscription (`requiresSellingPlan: true`) can only be published to online stores.

    You can schedule future publication by providing a publish date. Only online store channels support [scheduled publishing](https://shopify.dev/docs/apps/build/sales-channels/scheduled-product-publishing).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishablePublish.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The resource to create or update publications for.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishablePublish.arguments.input)input •[[PublicationInput!]!](/docs/api/admin-graphql/latest/input-objects/PublicationInput) required
    :   Specifies the input fields required to publish a resource.

        Show input fields

    ---

[Anchor to publishablePublishToCurrentChannel](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishablePublishToCurrentChannel)[publishablePublishToCurrentChannel](/docs/api/admin-graphql/latest/mutations/publishablePublishToCurrentChannel) •mutation
:   Publishes a resource to the current [`Channel`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Channel) associated with the requesting app. The system determines the current channel by the app's API client ID. Resources include [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) and [`Collection`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection) objects that implement the [`Publishable`](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Publishable) interface.

    For products to be visible in the channel, they must have an active [`ProductStatus`](https://shopify.dev/docs/api/admin-graphql/latest/enums/ProductStatus). Products sold exclusively on subscription ([`requiresSellingPlan`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.requiresSellingPlan): `true`) can only be published to online stores.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishablePublishToCurrentChannel.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The resource to create or update publications for.

    ---

[Anchor to publishableUnpublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishableUnpublish)[publishableUnpublish](/docs/api/admin-graphql/latest/mutations/publishableUnpublish) •mutation
:   Unpublishes a resource, such as a [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) or [`Collection`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Collection), from one or more [publications](https://shopify.dev/docs/api/admin-graphql/latest/objects/Publication). The resource remains in your store but becomes unavailable to customers.

    For products to be visible in a channel, they must have an active [`ProductStatus`](https://shopify.dev/docs/api/admin-graphql/latest/enums/ProductStatus).

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishableUnpublish.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The resource to delete or update publications for.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishableUnpublish.arguments.input)input •[[PublicationInput!]!](/docs/api/admin-graphql/latest/input-objects/PublicationInput) required
    :   Specifies the input fields required to unpublish a resource.

        Show input fields

    ---

[Anchor to publishableUnpublishToCurrentChannel](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishableUnpublishToCurrentChannel)[publishableUnpublishToCurrentChannel](/docs/api/admin-graphql/latest/mutations/publishableUnpublishToCurrentChannel) •mutation
:   Unpublishes a resource from the current channel. If the resource is a product, then it's visible in the channel only if the product status is `active`.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/Shop#mutation-publishableUnpublishToCurrentChannel.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The resource to delete or update publications for.

    ---

[Anchor to savedSearchDelete](/docs/api/admin-graphql/latest/objects/Shop#mutation-savedSearchDelete)[savedSearchDelete](/docs/api/admin-graphql/latest/mutations/savedSearchDelete) •mutation
:   Delete a saved search.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-savedSearchDelete.arguments.input)input •[SavedSearchDeleteInput!](/docs/api/admin-graphql/latest/input-objects/SavedSearchDeleteInput) required
    :   The input fields to delete a saved search.

        Show input fields

    ---

[Anchor to storefrontAccessTokenCreate](/docs/api/admin-graphql/latest/objects/Shop#mutation-storefrontAccessTokenCreate)[storefrontAccessTokenCreate](/docs/api/admin-graphql/latest/mutations/storefrontAccessTokenCreate) •mutation
:   Creates a storefront access token that delegates unauthenticated access scopes to clients using the [Storefront API](https://shopify.dev/docs/api/storefront). The token provides public access to storefront resources without requiring customer authentication.

    Each shop can have up to 100 active [`StorefrontAccessToken`](https://shopify.dev/docs/api/admin-graphql/latest/objects/StorefrontAccessToken) objects. Headless storefronts, mobile apps, and other client applications typically use these tokens to access public storefront data.

    Learn more about [building with the Storefront API](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started).

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-storefrontAccessTokenCreate.arguments.input)input •[StorefrontAccessTokenInput!](/docs/api/admin-graphql/latest/input-objects/StorefrontAccessTokenInput) required
    :   Provides the input fields for creating a storefront access token.

        Show input fields

    ---

### Deprecated mutations

* collectionPublish (CollectionPublishPayload): deprecated
* collectionUnpublish (CollectionUnpublishPayload): deprecated
* productPublish (ProductPublishPayload): deprecated
* productUnpublish (ProductUnpublishPayload): deprecated

[Anchor to collectionPublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionPublish)[collectionPublish](/docs/api/admin-graphql/latest/mutations/collectionPublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionPublish.arguments.input)input •[CollectionPublishInput!](/docs/api/admin-graphql/latest/input-objects/CollectionPublishInput) required
    :   Specify a collection to publish and the sales channels to publish it to.

        Show input fields

    ---

[Anchor to collectionUnpublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionUnpublish)[collectionUnpublish](/docs/api/admin-graphql/latest/mutations/collectionUnpublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-collectionUnpublish.arguments.input)input •[CollectionUnpublishInput!](/docs/api/admin-graphql/latest/input-objects/CollectionUnpublishInput) required
    :   Specify a collection to unpublish and the sales channels to remove it from.

        Show input fields

    ---

[Anchor to productPublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-productPublish)[productPublish](/docs/api/admin-graphql/latest/mutations/productPublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-productPublish.arguments.input)input •[ProductPublishInput!](/docs/api/admin-graphql/latest/input-objects/ProductPublishInput) required
    :   Specifies the product to publish and the channels to publish it to.

        Show input fields

    ---

[Anchor to productUnpublish](/docs/api/admin-graphql/latest/objects/Shop#mutation-productUnpublish)[productUnpublish](/docs/api/admin-graphql/latest/mutations/productUnpublish) •mutation Deprecated
:   Show payload

    ### Arguments

    [Anchor to input](/docs/api/admin-graphql/latest/objects/Shop#mutation-productUnpublish.arguments.input)input •[ProductUnpublishInput!](/docs/api/admin-graphql/latest/input-objects/ProductUnpublishInput) required
    :   Specifies the product to unpublish and the channel to unpublish it from.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Shop#interfaces)Interfaces

* HasMetafieldDefinitions
* HasMetafields
* HasPublishedTranslations
* Node

[Anchor to HasMetafieldDefinitions](/docs/api/admin-graphql/latest/objects/Shop#interface-HasMetafieldDefinitions)[HasMetafieldDefinitions](/docs/api/admin-graphql/latest/interfaces/HasMetafieldDefinitions) •interface

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/Shop#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/Shop#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/Shop#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo