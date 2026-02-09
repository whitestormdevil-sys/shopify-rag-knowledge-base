---
source: https://shopify.dev/docs/api/liquid/objects/country
---

A country supported by the store's localization options.

To learn how to use the `country` object to offer localization options in your theme,
refer to [Support multiple currencies and languages](/themes/internationalization/multiple-currencies-languages).

## Properties

[Anchor to](/docs/api/liquid/objects/country#country-available_languages) 

available\_languages**available\_languages** array of [shop\_locale](/docs/api/liquid/objects/shop_locale)

:   The languages that have been added to the market that this country belongs to.

[Anchor to](/docs/api/liquid/objects/country#country-continent) 

continent**continent** [string](/docs/api/liquid/basics#string)

:   The continent that the country is in.

    Possible values are `Africa`, `Asia`, `Central America`, `Europe`, `North America`, `Oceania`, and `South America`.

[Anchor to](/docs/api/liquid/objects/country#country-currency) 

currency**currency** [currency](/docs/api/liquid/objects/currency)

:   The currency used in the country.

[Anchor to](/docs/api/liquid/objects/country#country-iso_code) 

iso\_code**iso\_code** [string](/docs/api/liquid/basics#string)

:   The ISO code of the country in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

[Anchor to](/docs/api/liquid/objects/country#country-market) 

market**market** [market](/docs/api/liquid/objects/market)

:   The market that includes this country.

[Anchor to](/docs/api/liquid/objects/country#country-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the country.

[Anchor to](/docs/api/liquid/objects/country#country-popular?) 

popular?**popular?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the country is popular for this shop. Otherwise, returns `false`.
    This can be useful for sorting countries in a country selector.

[Anchor to](/docs/api/liquid/objects/country#country-unit_system) 

unit\_system**unit\_system** [string](/docs/api/liquid/basics#string) from a set of values

:   The unit system of the country.

    | Possible values |
    | --- |
    | imperial |
    | metric |

99

1

2

3

4

5

6

7

8

9

10

{

"available\_languages": [],

"continent": "North America",

"currency": {},

"iso\_code": "CA",

"market": {},

"name": "Canada",

"popular?": false,

"unit\_system": "metric"

}

##### Example

```liquid
{
  "available_languages": [],
  "continent": "North America",
  "currency": {},
  "iso_code": "CA",
  "market": {},
  "name": "Canada",
  "popular?": false,
  "unit_system": "metric"
}
```

[Anchor to Referencing the `country` object directly](/docs/api/liquid/objects/country#country-referencing-the-country-object-directly)

### Referencing the `country` object directly

When the country object is referenced directly, `country.name` is returned.

9

1

2

3

{% for country in localization.available\_countries -%}

{{ country }}

{%- endfor %}

##### Code

```liquid
{% for country in localization.available_countries -%}
  {{ country }}
{%- endfor %}
```

##### Data

```liquid
{
  "localization": {
    "available_countries": [
      "Afghanistan",
      "Australia",
      "Austria",
      "Belgium",
      "Canada",
      "Czechia",
      "Denmark",
      "Finland",
      "France",
      "Germany",
      "Hong Kong SAR",
      "Ireland",
      "Israel",
      "Italy",
      "Japan",
      "Malaysia",
      "Netherlands",
      "New Zealand",
      "Norway",
      "Poland",
      "Portugal",
      "Singapore",
      "South Korea",
      "Spain",
      "Sweden",
      "Switzerland",
      "United Arab Emirates",
      "United Kingdom",
      "United States"
    ]
  }
}
```

## Output

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

Afghanistan

Australia

Austria

Belgium

Canada

Czechia

Denmark

Finland

France

Germany

Hong Kong SAR

Ireland

Israel

Italy

Japan

Malaysia

Netherlands

New Zealand

Norway

Poland

Portugal

Singapore

South Korea

Spain

Sweden

Switzerland

United Arab Emirates

United Kingdom

United States

##### Output

```liquid
Afghanistan
Australia
Austria
Belgium
Canada
Czechia
Denmark
Finland
France
Germany
Hong Kong SAR
Ireland
Israel
Italy
Japan
Malaysia
Netherlands
New Zealand
Norway
Poland
Portugal
Singapore
South Korea
Spain
Sweden
Switzerland
United Arab Emirates
United Kingdom
United States
```

[Anchor to Rendering a flag image](/docs/api/liquid/objects/country#country-rendering-a-flag-image)

### Rendering a flag image

When the country object is passed to the [`image_url`](/docs/api/liquid/filters#image_url) filter, a [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for that country’s flag is returned. All country’s flags are SVGs, normalized to an aspect ratio of 4:3.

9

1

{{ localization.country | image\_url: width: 32 | image\_tag }}

##### Code

```liquid
{{ localization.country | image_url: width: 32 | image_tag }}
```

##### Data

```liquid
{
  "localization": {
    "country": "Canada"
  }
}
```

## Output

9

1

<img src="//cdn.shopify.com/static/images/flags/ca.svg?width=32" alt="Canada" srcset="//cdn.shopify.com/static/images/flags/ca.svg?width=32 32w" width="32" height="24">

##### Output

```liquid
<img src="//cdn.shopify.com/static/images/flags/ca.svg?width=32" alt="Canada" srcset="//cdn.shopify.com/static/images/flags/ca.svg?width=32 32w" width="32" height="24">
```

Was this section helpful?

YesNo