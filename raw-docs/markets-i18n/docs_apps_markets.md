---
source: https://shopify.dev/docs/apps/markets
---

Note

We're expanding Markets capabilities for merchants. Learn more about our [developer preview](/docs/apps/build/markets/new-markets/developer-preview).

**Note:**

We're expanding Markets capabilities for merchants. Learn more about our [developer preview](/docs/apps/build/markets/new-markets/developer-preview).

Shopify helps merchants expand their business to a global audience, sell to multiple countries, and scale internationally. With Shopify Markets, you can configure multiple languages, international pricing, market-specific domains and subfolders, and more. By creating localized shopping experiences, merchants can better expand their business internationally.

Note

Unless otherwise stated, the concepts and examples in this guide apply equally to stores using Shopify Markets, [Managed Markets](https://help.shopify.com/en/manual/markets/markets-pro), and [Global-E's native integration](https://www.global-e.com/) that works with Shopify's checkout.

**Note:**

Unless otherwise stated, the concepts and examples in this guide apply equally to stores using Shopify Markets, [Managed Markets](https://help.shopify.com/en/manual/markets/markets-pro), and [Global-E's native integration](https://www.global-e.com/) that works with Shopify's checkout.

---

## [Anchor to How it works](/docs/apps/build/markets#how-it-works)How it works

In Shopify, a market is a group of one or more regions of the world that a merchant is targeting for sales. Merchants have one primary market, and any number of other markets up to a total of 50.

A merchant can configure a different buyer experience for each market depending on their needs. If a store is selling somewhere, then that region is included in one and only one of the store's active markets—it's not possible for a visitor in checkout to select a shipping address that's not included in a market. If your app helps a merchant sell, then you may need to reference their market configuration to know where they sell and what buyer experiences they've configured.

When you're building experiences for customers, don't expose the merchant's specific market groupings. Merchants group regions into markets based on their needs, and visitors to a store shouldn't be asked to guess whether a particular merchant considers Germany to be "Western Europe" or "Central Europe." Visitors should be told and asked about only the actual geographic regions that a merchant sells.

### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Explore an example of [how to query for a merchant's markets configuration with the Admin API](/docs/api/admin-graphql/latest/queries/markets#examples-Get_the_first_three_markets).
* Check out an example of [how to load a store's supported countries and languages using the Storefront API](/docs/api/storefront/latest/queries/localization#examples-Load_the_countries_a_shop_sells_to_and_the_supported_languages_for_each).
* Learn about [the localization data available in Liquid](/docs/api/liquid/objects/localization).

### [Anchor to Determining which localized experience is best for a visitor](/docs/apps/build/markets#determining-which-localized-experience-is-best-for-a-visitor)Determining which localized experience is best for a visitor

If you have multiple localized versions of a single store, then you should make sure that each visitor interacts with the optimal version of the store. Depending on the merchant's store configuration, search engines might be able to pre-localize visitors, and Shopify might automatically redirect visitors. However, it's still possible for a visitor to be browsing in a context for a market that they aren't actually located in.

Learn how to [detect a visitor's optimal localized experience and help them access it](/docs/storefronts/themes/markets/localization-discovery).

---

## [Anchor to Local web presences](/docs/apps/build/markets#local-web-presences)Local web presences

For SEO purposes, and to localize marketing efforts, merchants often configure dynamic URLs for their international markets. Shopify Markets makes this automatic for merchants using Liquid storefronts. Developers of custom storefronts are encouraged to follow similar patterns.

Localized web presences for a specific market can take the form of different domains, subdomains, or subfolders. For example, if a store's primary market is the United States on `example.com`, then when a Canadian market is created, the merchant can enable a Canadian subfolder at `example.com/en-ca`. Alternatively, the merchant could choose to configure a Canadian subdomain at `ca.example.com` or purchase a ccTLD `example.ca`.

When a merchant translates their storefront, they need a language-specific subfolder for each alternative language. This configuration is automatic for Liquid storefronts. If the same example merchant enables French translations for their United States and Canadian markets, then they'll get a new URL for each market. The French version of their United States market will be at `example.com/fr`, and the French version for Canada will be at `example.com/fr-ca`, `ca.example.com/fr`, or `example.ca/fr` depending on the merchant's configuration for the Canadian market.

Caution

Given these possible dynamic changes in URL structure, avoid hardcoding URL when integrating or linking to the online store. If you've hardcoded a URL like `/cart` in a link or Ajax request, then visitors browsing in another language or market context will be forced back to the domain defaults. This means they might see the wrong language or currency.

**Caution:**

Given these possible dynamic changes in URL structure, avoid hardcoding URL when integrating or linking to the online store. If you've hardcoded a URL like `/cart` in a link or Ajax request, then visitors browsing in another language or market context will be forced back to the domain defaults. This means they might see the wrong language or currency.

### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Learn about [how to generate dynamic, locale-aware URLs in theme app extensions and script tags](/docs/storefronts/themes/markets/multiple-currencies-languages#locale-aware-urls).
* Refer to an example of [how to use the Admin API to access the root URLs for a shop's market web presences](/docs/api/admin-graphql/latest/queries/markets#examples-Get_market_web_presences_and_their_root_URLs).

---

## [Anchor to International pricing](/docs/apps/build/markets#international-pricing)International pricing

When selling internationally, localized pricing is essential. Automatic conversion with price rounding might be the perfect balance between effort and reward for many merchants, but some merchants need more control. To account for costs or competitive positioning, merchants can adjust product prices in specific international markets up or down by a percentage. Marketing needs or agreements with partners might require merchants to set a fixed, local-currency price for a given product.

Note

When reading product prices from Shopify, don't try to compute an international market's price from the base variant prices. Instead, you should load each international market's prices explicitly, treating Shopify as the source of truth.

**Note:**

When reading product prices from Shopify, don't try to compute an international market's price from the base variant prices. Instead, you should load each international market's prices explicitly, treating Shopify as the source of truth.

### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Explore an example of [how to query for local prices using the Storefront API](/docs/api/storefront/latest/queries/product#examples-Retrieve_local_prices_for_a_product).
* Refer to example of [how to use the Admin API to preview contextual prices for a product](/docs/api/admin-graphql/latest/queries/product#examples-Get_the_price_range_for_a_product_for_buyers_from_Canada) or [a specific variant](/docs/api/admin-graphql/latest/queries/productVariant#examples-Get_the_price_for_a_product_variant_for_buyers_from_Canada).
* Learn how to use locale-aware URLs and [automatically get correct prices in Liquid](/docs/storefronts/themes/markets/multiple-currencies-languages#locale-aware-urls) and the [Ajax API](/docs/api/ajax/reference/product#get-locale-products-product-handle-js).

### [Anchor to Configuring international prices](/docs/apps/build/markets#configuring-international-prices)Configuring international prices

There are a number of strategies that you can use to configure a market's international pricing. Automatic conversion can be configured by [updating a market's currency settings](/docs/api/admin-graphql/latest/mutations/marketCurrencySettingsUpdate). If automatic conversion is insufficient, then you can [use price lists](/docs/apps/build/markets/build-catalog) to uniformly adjust product prices up or down by a percentage, specify explicit per-variant fixed overrides.

### [Anchor to Currencies and foreign exchange](/docs/apps/build/markets#currencies-and-foreign-exchange)Currencies and foreign exchange

When a merchant's payment gateway supports selling in local currencies, it is often a merchant's first step in localizing their shop for international customers. When integrating with a store using Markets, expect to deal with money values in various presentment currencies.

The following concepts in Shopify's APIs are important to understand when working with multi-currency orders:

Currency concepts you'll encounter when working with multi-currency orders

| Concept | Description |
| --- | --- |
| Presentment currency | The presentment currency is what store visitors see in checkout, what they agree to pay, and how their payment method is charged. These values are the source of truth. Presentment currency values are also displayed to the merchant as their source of truth on the order details page. Refunds and order edits are always based on the presentment currency. [Shopify Functions](/docs/apps/build/functions) are also provided monetary input values in the presentment currency. |
| Shop currency | The shop currency is the merchant's common reference for their business on Shopify. If an order is placed in a different presentment currency, then shop currency values are back-converted from presentment values using the live exchange rate. These values power the merchant's [Analytics](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports) in the Shopify admin. Since the values are converted, intermediate shop currency values might not sum perfectly to totals, and shop currency values of corresponding transactions performed at different times (such as [captures](/docs/api/admin-graphql/latest/mutations/orderCapture) and [refunds](/docs/api/admin-graphql/latest/mutations/refundCreate)) might not match. |
| Settlement currency | The settlement currency is the currency of the merchant's payout. It might equal the shop currency or the presentment currency, but it's not guaranteed. These values are the most appropriate for accounting purposes. When a merchant is not using [Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments), settlement currency values must be fetched and reconciled directly from their payment gateways. |

---

## [Anchor to Market catalogs](/docs/apps/build/markets#market-catalogs)Market catalogs

Whether for strategic or logistical reasons, sometimes merchants don't want to sell all of their products in every market. With Shopify Markets, you can restrict specific products from sale in a specific market. Products that are excluded from a market's catalog are hidden from storefronts, omitted from search results, and blocked from being added to cart when a visitor is browsing in that market's context. If a customer is browsing in the wrong context, then the restricted product is removed from their cart when they change their shipping address in checkout.

In buyer-facing contexts, a product which is excluded from a market's catalog will behave just like it was archived or deleted when accessed from that market's perspective. It will be omitted from lists and not found when queried by handle or ID.

### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Refer to an example of [how to use the Storefront API to query for products published in a certain context](/docs/api/storefront/unstable/queries/product#examples-Load_products_which_are_published_in_a_given_context).
* Learn how to restrict products from sale in a market by [unpublishing it from that market's catalog](/docs/apps/build/markets/build-catalog).
* Explore an example of [how to use the Admin API to query whether a product is published in a given country](/docs/api/admin-graphql/unstable/queries/product#examples-Query_whether_a_product_is_published_in_a_given_country).

---

## [Anchor to Translations and localized content](/docs/apps/build/markets#translations-and-localized-content)Translations and localized content

Translation of store content is a major contributor to successfully selling in an international market, and in some parts of the world it's essential to reach the domestic market as well. You can assign an alternate language to one or more of a store's markets, and translations in that language are shared across all those markets. A merchant can also localize their store's content for a specific combination of market and language. For example, a merchant selling a product titled "Wool sweater" in English might translate it to French as "Pull en laine," and then localize it for their Canada market as "Chandail en laine."

### [Anchor to Building an experience for customers](/docs/apps/build/markets#building-an-experience-for-customers)Building an experience for customers

When building experiences for a merchant's customers, you should always query for and display the right content for the customer's language and country context. Shopify uses a defined fallback order when loading localized content. Consider a United States store with English as its primary language, which also sells in Belgium in French and Dutch. French is the default language for the shop's Belgian market. When loading content for a customer browsing in a Dutch Belgian context, Shopify follows the following fallback order:

1. Dutch (Belgium)
2. Base Dutch
3. French (Belgium)
4. Base French
5. Base English (shop primary)

Shopify's buyer-facing APIs, including Liquid and the Storefront API, handle this fallback automatically.

#### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Learn how to [load localized content with the Storefront API](/docs/api/storefront/latest/queries/product#examples-Load_translated_and_localized_content_for_a_product).
* Learn how to use locale-aware URLs and [automatically get localized content in Liquid](/docs/storefronts/themes/markets/multiple-currencies-languages#locale-aware-urls) and the [Ajax API](/docs/api/ajax/reference/product#get-locale-products-product-handle-js).

### [Anchor to Building an experience for merchants](/docs/apps/build/markets#building-an-experience-for-merchants)Building an experience for merchants

To better serve merchants around the world, you should [internationalize the user interface of a merchant-oriented app](/docs/apps/build/localize-your-app). However, merchant-oriented tools should typically identify a store's resources by their untranslated base attributes. For example, it might be confusing to a merchant if product titles in an inventory management app were shown in different languages based on their staff member's language preferences.

If your app helps a merchant build an experience for shoppers, then you should show localized and translated store data in previews, as applicable. If a merchant can use your app to create buyer-facing content, then consider making that content translatable. If you're storing the content in Shopify as metafields, for example, then your content will be translatable using the GraphQL Admin API. If not, you'll have to implement your own translation system.

#### [Anchor to Examples](/docs/apps/build/markets#examples)Examples

* Refer to an example of [how to load translations and localizations with the Admin API](/docs/api/admin-graphql/latest/queries/product#examples-Loading_translations_and_localizations_of_a_product_s_title_and_description) to power a merchant-facing preview of a shopper's experience.
* Learn about [how to save translations of merchant-provided content](/docs/apps/build/markets/manage-translated-content).

---

## [Anchor to Locally required order data](/docs/apps/build/markets#locally-required-order-data)Locally required order data

Some countries require additional information on international orders which must be collected from customers. If your app creates draft orders or orders with shipping addresses in these countries, then you might need to add the locally required data as "localized extensions" to the order. However, if your app helps merchants fulfill international orders, then you might need to [read the locally required data collected in checkout](/docs/apps/build/markets/add-locally-required-order-data).

---

## [Anchor to Developer tools and resources](/docs/apps/build/markets#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to learn more about Shopify Markets.

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

GraphQL Admin API

Consult the GraphQL Admin API reference to learn more about the `Market` object.

GraphQL Admin API

Consult the GraphQL Admin API reference to learn more about the `Market` object.](/docs/api/admin-graphql/latest/objects/Market)

[GraphQL Admin API  
  

Consult the GraphQL Admin API reference to learn more about the `Market` object.](/docs/api/admin-graphql/latest/objects/Market)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

Building for Markets with the Storefront API

Learn how to build localized customer experiences with the Storefront API and Shopify Markets.

Building for Markets with the Storefront API

Learn how to build localized customer experiences with the Storefront API and Shopify Markets.](/docs/storefronts/headless/building-with-the-storefront-api/markets)

[Building for Markets with the Storefront API  
  

Learn how to build localized customer experiences with the Storefront API and Shopify Markets.](/docs/storefronts/headless/building-with-the-storefront-api/markets)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

User manual for Shopify Markets

Learn more about how merchants use Shopify Markets to sell internationally.

User manual for Shopify Markets

Learn more about how merchants use Shopify Markets to sell internationally.](https://help.shopify.com/en/manual/markets)

[User manual for Shopify Markets  
  

Learn more about how merchants use Shopify Markets to sell internationally.](https://help.shopify.com/en/manual/markets)

---

Was this page helpful?

YesNo