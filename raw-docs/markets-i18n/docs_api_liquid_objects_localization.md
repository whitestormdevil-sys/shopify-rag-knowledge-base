---
source: https://shopify.dev/docs/api/liquid/objects/localization
---

Information about the countries and languages that are available on a store.

The `localization` object can be used in a [localization form](/docs/api/liquid/tags/form#form-localization).

To learn about how to offer localization options in your theme, refer to [Support multiple currencies and languages](/themes/internationalization/multiple-currencies-languages).

## Properties

[Anchor to](/docs/api/liquid/objects/localization#localization-available_countries) 

available\_countries**available\_countries** array of [country](/docs/api/liquid/objects/country)

:   The countries that are available on the store.

[Anchor to](/docs/api/liquid/objects/localization#localization-available_languages) 

available\_languages**available\_languages** array of [shop\_locale](/docs/api/liquid/objects/shop_locale)

:   The languages that are available on the store.

[Anchor to](/docs/api/liquid/objects/localization#localization-country) 

country**country** [country](/docs/api/liquid/objects/country)

:   The currently selected country on the storefront.

[Anchor to](/docs/api/liquid/objects/localization#localization-language) 

language**language** [shop\_locale](/docs/api/liquid/objects/shop_locale)

:   The currently selected language on the storefront.

[Anchor to](/docs/api/liquid/objects/localization#localization-market) 

market**market** [market](/docs/api/liquid/objects/market)

:   The currently selected market on the storefront.

9

1

2

3

4

5

6

7

{

"available\_countries": [],

"available\_languages": [],

"country": {},

"language": {},

"market": {}

}

##### Example

```liquid
{
  "available_countries": [],
  "available_languages": [],
  "country": {},
  "language": {},
  "market": {}
}
```

Was this section helpful?

YesNo