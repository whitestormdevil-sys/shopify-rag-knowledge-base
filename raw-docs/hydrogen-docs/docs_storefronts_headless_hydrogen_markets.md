---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/markets
---

---

## [Anchor to Introduction](/docs/storefronts/headless/hydrogen/markets#introduction)Introduction

Shopify Markets helps merchants expand their business to a global audience by creating shopping experiences in local languages and currencies.

Hydrogen provides patterns on top of React Router to set up internationalization (i18n) that leverages a merchant’s market configuration. It also makes locales available throughout the app and in Storefront API queries.

---

## [Anchor to Requirements](/docs/storefronts/headless/hydrogen/markets#requirements)Requirements

* You've completed the [Hydrogen Getting Started](/docs/storefronts/headless/hydrogen/getting-started) with a `Hello World` example project.
* You've setup you store's regions and languages using [Shopify Markets](https://help.shopify.com/en/manual/markets).
* You're familiar with [using the Storefront API with Shopify Markets](/docs/storefronts/headless/building-with-the-storefront-api/markets).

---

## [Anchor to Setup the default locale](/docs/storefronts/headless/hydrogen/markets#setup-the-default-locale)Setup the default locale

Before setting up your Hydrogen Storefront, make sure to set a default `language` and `country code`. This ensures that the correct language and currency are used throughout the app.

This guide shows you how to add or update your custom storefront's default language.

[![](/images/icons/48/flag.png)![](/images/icons/48/flag-dark.png)

Setup the default locale

Learn how to set the default locale for the language and country using Hydrogen.

Setup the default locale

Learn how to set the default locale for the language and country using Hydrogen.](/docs/storefronts/headless/hydrogen/markets/default-locale)

[Setup the default locale  
  

Learn how to set the default locale for the language and country using Hydrogen.](/docs/storefronts/headless/hydrogen/markets/default-locale)

---

## [Anchor to Setup a multi-region and multilingual storefront](/docs/storefronts/headless/hydrogen/markets#setup-a-multi-region-and-multilingual-storefront)Setup a multi-region and multilingual storefront

Shopify recommends that storefronts with multiple regions and languages have separate URLs for each locale. This improves accessibility for search engines and screen readers.

Use one of the following methods to create different URLs for each region and language.

| Option | URL examples |
| --- | --- |
| Localization scheme using URL paths | `hydrogen.shop/fr`, `hydrogen.shop/es` |
| Localization scheme using domains and subdomains | `hydrogen.fr`, `hydrogen.es` |

The advantage of using the URL paths method is that you only need to set this up from the app and you don't need to setup any domain infrastructure.

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)

Setup i18n with URL paths

Learn how to support multiple countries and languages by using URL paths

Setup i18n with URL paths

Learn how to support multiple countries and languages by using URL paths](/docs/storefronts/headless/hydrogen/markets/multiple-languages-url-paths)

[Setup i18n with URL paths  
  

Learn how to support multiple countries and languages by using URL paths](/docs/storefronts/headless/hydrogen/markets/multiple-languages-url-paths)

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)

Setup i18n with domains and subdomains

Learn how to support multiple countries and languages by using domains and subdomains

Setup i18n with domains and subdomains

Learn how to support multiple countries and languages by using domains and subdomains](/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains)

[Setup i18n with domains and subdomains  
  

Learn how to support multiple countries and languages by using domains and subdomains](/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains)

---

## [Anchor to Create a country selector](/docs/storefronts/headless/hydrogen/markets#create-a-country-selector)Create a country selector

Users will want to switch your Storefront to their preferred country. It is good user experience to provide a way for them to achieve this within your store.

* [How to setup a country selector](/docs/storefronts/headless/hydrogen/markets/country-selector)

---

## [Anchor to Localization detection using headers, cookies, or URL search params](/docs/storefronts/headless/hydrogen/markets#localization-detection-using-headers-cookies-or-url-search-params)Localization detection using headers, cookies, or URL search params

While it's possible to detect an approximation of the user's locale by reading the header, cookies or URL search params. Shopify only recommends this to improve the experience of the user.

A good example of detecting localization is to show a banner to asking the user if they want to switch country.

A bad example of localization detection is when the user gets automatically redirected.

Other drawbacks of this approach are that page caching ignores locale cookies, headers and URL search params. SEO bots tend to origin from the US, don't have cookies and will not change their `accept-language` headers.

* [Learn how to setup localization detection using headers, cookies or URL search params](/docs/storefronts/headless/hydrogen/markets/locale-detection)

---

## [Anchor to Developer tools and resources](/docs/storefronts/headless/hydrogen/markets#developer-tools-and-resources)Developer tools and resources

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

Shopify Markets

Learn about Shopify Markets for launching to multiple international markets

Shopify Markets

Learn about Shopify Markets for launching to multiple international markets](https://help.shopify.com/en/manual/markets)

[Shopify Markets  
  

Learn about Shopify Markets for launching to multiple international markets](https://help.shopify.com/en/manual/markets)

---

## [Anchor to Next steps](/docs/storefronts/headless/hydrogen/markets#next-steps)Next steps

* Learn how to [set up default locale](/docs/storefronts/headless/hydrogen/markets/default-locale) for your storefront.
* Learn how to [set up multiregion and multilingual storefront with URL paths](/docs/storefronts/headless/hydrogen/markets/multiple-languages-url-paths) to get the right language and currency.
* Learn how to [set up multiregion and multilingual storefront with domains and subdomains](/docs/storefronts/headless/hydrogen/markets/multiple-languages-domains) to get the right language and currency.
* Learn how to [create a country selector](/docs/storefronts/headless/hydrogen/markets/country-selector) to allow users to choose their own country.
* Learn how to [set up locale detection using response header, cookies, or URL search params](/docs/storefronts/headless/hydrogen/markets/locale-detection).
* Learn how to [set up localization detection using headers, cookies or URL search params](/docs/storefronts/headless/hydrogen/markets/locale-detection)

---

Was this page helpful?

YesNo