---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/localization
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Returns the localized experiences configured for the shop.

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/localization#possible-returns)Possible returns

* Localization (Localization!)

[Anchor to Localization](/docs/api/storefront/latest/queries/localization#returns-Localization)Localization •[Localization!](/docs/api/storefront/latest/objects/Localization)
:   Information about the localized experiences configured for the shop.

    Show fields

    [Anchor to availableCountries](/docs/api/storefront/latest/queries/localization#returns-Localization.fields.availableCountries)availableCountries •[[Country!]!](/docs/api/storefront/latest/objects/Country) non-null
    :   The list of countries with enabled localized experiences.

        Show fields

    [Anchor to availableLanguages](/docs/api/storefront/latest/queries/localization#returns-Localization.fields.availableLanguages)availableLanguages •[[Language!]!](/docs/api/storefront/latest/objects/Language) non-null
    :   The list of languages available for the active country.

        Show fields

    [Anchor to country](/docs/api/storefront/latest/queries/localization#returns-Localization.fields.country)country •[Country!](/docs/api/storefront/latest/objects/Country) non-null
    :   The country of the active localized experience. Use the `@inContext` directive to change this value.

        Show fields

    [Anchor to language](/docs/api/storefront/latest/queries/localization#returns-Localization.fields.language)language •[Language!](/docs/api/storefront/latest/objects/Language) non-null
    :   The language of the active localized experience. Use the `@inContext` directive to change this value.

        Show fields

    [Anchor to market](/docs/api/storefront/latest/queries/localization#returns-Localization.fields.market)market •[Market!](/docs/api/storefront/latest/objects/Market) non-nullDeprecated
    :   Show fields

---

Was this section helpful?

YesNo