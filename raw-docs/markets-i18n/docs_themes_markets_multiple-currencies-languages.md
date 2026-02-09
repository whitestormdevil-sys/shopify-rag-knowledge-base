---
source: https://shopify.dev/docs/themes/markets/multiple-currencies-languages
---

Merchants can enable selling in [multiple currencies](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/setup) with Shopify Payments, and [multiple languages](https://help.shopify.com/en/manual/cross-border/multilingual-online-store). This means that customers can browse the shop, and checkout, in their preferred currency and/or language.

In this tutorial, you'll learn how to support multiple currencies and languages in your theme through country and language selectors.

You should also consider the following when dealing with multiple currencies and languages:

* [Locale-aware URLs](#locale-aware-urls)
* [Search engine optimization](#search-engine-optimization)

---

## [Anchor to Resources](/docs/storefronts/themes/markets/multiple-currencies-languages#resources)Resources

To support multiple currencies and languages in your theme, you'll use the following:

* The [`form` object](/docs/api/liquid/objects/form)
* The [`localization` object](/docs/api/liquid/objects/localization)

---

## [Anchor to Implementing country and language selectors](/docs/storefronts/themes/markets/multiple-currencies-languages#implementing-country-and-language-selectors)Implementing country and language selectors

If a merchant has enabled multiple currencies and/or languages, then you should give customers the ability to select their preference. You can build the following components to give customers this ability:

* A [country selector](#the-country-selector)
* A [language selector](#the-country-selector)

Plus

For merchants on the [Shopify Plus](https://www.shopify.com/plus?utm_source=shopify&utm_medium=docs&utm_campaign=multiple-currencies-and-languages) plan, Shopify will use geolocation to detect where customers are located and automatically select the most relevant country from the options that the merchant has enabled.

**Plus:**

For merchants on the [Shopify Plus](https://www.shopify.com/plus?utm_source=shopify&utm_medium=docs&utm_campaign=multiple-currencies-and-languages) plan, Shopify will use geolocation to detect where customers are located and automatically select the most relevant country from the options that the merchant has enabled.

You might include a country and/or language selector in your header or footer, or inside of a navigation drawer. For more detailed placement recommendations, and to learn about best practices for styling country and language selectors, refer to the [UX guidelines](/docs/storefronts/themes/markets/country-language-ux).

---

## [Anchor to The country selector](/docs/storefronts/themes/markets/multiple-currencies-languages#the-country-selector)The country selector

You can build a country selector to allow customers to manually choose their preferred currency. If the currently selected language is not supported by the selected country, it will be updated to the default language for that country.

The selector needs to be placed inside a localization form. This form can be created using the Liquid [`form` tag](/docs/api/liquid/tags/form#form-localization) and the `'localization'` parameter.

The selector also needs to contain an input with the attribute `name="country_code"`, whose value will be the selected country.

The shop's enabled countries are accessible through the `available_countries` attribute of the [`localization` object](/docs/api/liquid/objects/localization), and the currently selected country is accessible through the `country` attribute.

Note

You should only output a country selector if there's more than one available country.

**Note:**

You should only output a country selector if there's more than one available country.

The following example includes a button and a popover containing each country option:

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

{% if localization.available\_countries.size > 1 %}

<localization-form>

{% form 'localization' %}

<div className="disclosure">

<button type="button" className="disclosure\_\_button" aria-expanded="false" aria-controls="CountryList">

{{ localization.country.name }} ({{ localization.country.currency.iso\_code }} {{ localization.country.currency.symbol }})

<svg aria-hidden="true" focusable="false" role="presentation" className="icon icon-caret" viewBox="0 0 10 6">

<path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">

</svg>

</button>

<ul id="CountryList" role="list" className="disclosure\_\_list" hidden>

{% for country in localization.available\_countries %}

<li className="disclosure\_\_item" tabindex="-1">

<a href="#"{% if country.iso\_code == localization.country.iso\_code %} aria-current="true"{% endif %} data-value="{{ country.iso\_code }}">

{{ country.name }} ({{ country.currency.iso\_code }} {{ country.currency.symbol }})

</a>

</li>

{% endfor %}

</ul>

<input type="hidden" name="country\_code" value="{{ localization.country.iso\_code }}" />

</div>

{% endform %}

</localization-form>

{% endif %}

For an example of JavaScript that manages the visibility of the option list and submits the form on selection, refer to [JavaScript submission of the localization form](#javascript-submission-of-the-localization-form).

Note

For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

**Note:**

For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

---

## [Anchor to The language selector](/docs/storefronts/themes/markets/multiple-currencies-languages#the-language-selector)The language selector

You can build a language selector to allow customers to manually choose their preferred language.

The selector needs to be placed inside a localization form. This form can be created using the Liquid [`form` tag](/docs/api/liquid/tags/form#form-localization) and the `'localization'` parameter.

The selector also needs to contain an input with the attribute `name="language_code"`, whose value will be the selected language.

The available languages are accessible through the `available_languages` attribute of the [`localization` object](/docs/api/liquid/objects/localization), and the currently selected language is accessible through the `language` attribute.

Note

You should only output a country selector if there's more than one available language.

**Note:**

You should only output a country selector if there's more than one available language.

The following example includes a button and a popover containing each language option:

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

{% if localization.available\_languages.size > 1 %}

<localization-form>

{% form 'localization' %}

<div className="disclosure">

<button type="button" className="disclosure\_\_button" aria-expanded="false" aria-controls="LanguageList">

{{ localization.language.endonym\_name | capitalize }}

<svg aria-hidden="true" focusable="false" role="presentation" className="icon icon-caret" viewBox="0 0 10 6">

<path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">

</svg>

</button>

<ul id="LanguageList" role="list" className="disclosure\_\_list" hidden>

{% for language in localization.available\_languages %}

<li className="disclosure\_\_item" tabindex="-1">

<a href="#"{% if language.iso\_code == localization.language.iso\_code %} aria-current="true"{% endif %} hreflang="{{ language.iso\_code }}" lang="{{ language.iso\_code }}" data-value="{{ language.iso\_code }}">

{{ language.endonym\_name | capitalize }}

</a>

</li>

{% endfor %}

</ul>

<input type="hidden" name="language\_code" value="{{ localization.language.iso\_code }}" />

</div>

{% endform %}

</localization-form>

{% endif %}

For an example of JavaScript that manages the visibility of the option list and submits the form on selection, refer to [JavaScript submission of the localization form](#javascript-submission-of-the-localization-form).

Note

For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

**Note:**

For a more in-depth example, you can refer to Dawn's implementation in the [`footer.liquid` section](https://github.com/Shopify/dawn/blob/main/sections/footer.liquid).

---

## [Anchor to JavaScript submission of the localization form](/docs/storefronts/themes/markets/multiple-currencies-languages#javascript-submission-of-the-localization-form)JavaScript submission of the localization form

Because your country or language selector is a custom element and there's no submit button included in the form, you need to submit the form through JavaScript.

The following example is based on the previous [country](#the-country-selector) and [language](#the-language-selector) selector examples:

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

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

class LocalizationForm extends HTMLElement {

constructor() {

super();

this.elements = {

input: this.querySelector('input[name="language\_code"], input[name="country\_code"]'),

button: this.querySelector('button'),

panel: this.querySelector('ul'),

};

this.elements.button.addEventListener('click', this.openSelector.bind(this));

this.elements.button.addEventListener('focusout', this.closeSelector.bind(this));

this.addEventListener('keyup', this.onContainerKeyUp.bind(this));

this.querySelectorAll('a').forEach(item => item.addEventListener('click', this.onItemClick.bind(this)));

}

hidePanel() {

this.elements.button.setAttribute('aria-expanded', 'false');

this.elements.panel.setAttribute('hidden', true);

}

onContainerKeyUp(event) {

if (event.code.toUpperCase() !== 'ESCAPE') return;

this.hidePanel();

this.elements.button.focus();

}

onItemClick(event) {

event.preventDefault();

const form = this.querySelector('form');

this.elements.input.value = event.currentTarget.dataset.value;

if (form) form.submit();

}

openSelector() {

this.elements.button.focus();

this.elements.panel.toggleAttribute('hidden');

this.elements.button.setAttribute('aria-expanded', (this.elements.button.getAttribute('aria-expanded') === 'false').toString());

}

closeSelector(event) {

const shouldClose = event.relatedTarget && event.relatedTarget.nodeName === 'BUTTON';

if (event.relatedTarget === null || shouldClose) {

this.hidePanel();

}

}

}

customElements.define('localization-form', LocalizationForm);

Note

Your default solution should be a custom element that uses JavaScript to help with accessibility, however, you should also include a fallback in case JavaScript is disabled.

**Note:**

Your default solution should be a custom element that uses JavaScript to help with accessibility, however, you should also include a fallback in case JavaScript is disabled.

---

## [Anchor to Locale-aware URLs](/docs/storefronts/themes/markets/multiple-currencies-languages#locale-aware-urls)Locale-aware URLs

Stores can have dynamic URLs generated for them when they sell internationally or in multiple languages.

* When an additional locale (language) is published on a domain, Shopify automatically creates a URL path for it. For example, if a shop's primary URL is `shop.com`, and a french (`fr`) locale is published on that domain, then the URL `shop.com/fr` is automatically created.
* When a merchant creates a new market, Shopify creates a URL path for that market. For example, if a shop's primary market is the United States and primary locale is English on `shop.com`, when a Canada market is created, then the URL `shop.com/en-ca` is created.

Given these possible dynamic changes in URL structure, you should avoid hardcoding URLs. If you've hardcoded a URL like `/cart` in a link or Ajax request, then visitors browsing in another language or market context will be forced back to the domain defaults. This means they may see the wrong language or currency. Instead, use the following instructions to build dynamic URLs in Liquid or in JavaScript.

### [Anchor to In Liquid](/docs/storefronts/themes/markets/multiple-currencies-languages#in-liquid)In Liquid

Use one of the following approaches to build dynamic URLs with Liquid:

* The `url` attribute of any applicable Liquid objects
* The [routes object](/docs/api/liquid/objects/routes)

If a merchant has English and French locales, then the cart URL could be `/cart` or `/fr/cart`, respectively. The following example shows how to link to the cart page in the currently selected locale.

9

1

<a href="{{ routes.cart\_url }}">{{ 'templates.cart.go\_to\_cart' | t }}</a>

### [Anchor to In JavaScript](/docs/storefronts/themes/markets/multiple-currencies-languages#in-javascript)In JavaScript

You can build dynamic URLs in JavaScript by basing them off of the dynamic root route accessible on the window object, `window.Shopify.routes.root`. This value will always end in a `/`. For instance, if a merchant has a Canadian market in addition to their primary, `window.Shopify.routes.root` could return `"/en-ca/"` when a visitor is accessing that market's subfolder.

The following example shows how to make an Ajax request to the cart while preserving the current market's pricing:

9

1

2

3

fetch(window.Shopify.routes.root + 'cart.js')

.then(response => response.json())

.then(data => showCartContents(data));

---

## [Anchor to Search engine optimization](/docs/storefronts/themes/markets/multiple-currencies-languages#search-engine-optimization)Search engine optimization

In addition to providing options for customers to select a country and/or language, you also need to ensure that search engines return localized content and prices for customers.

Shopify automatically includes [hreflang tags](https://moz.com/learn/seo/hreflang-tag) through the [content\_for\_header object](/docs/api/liquid/objects/content_for_header). You can also return localized prices by including, or extending, [structured data](#considerations-for-structured-data) in your theme.

Note

Any information on this page around search engines and SEO is for general information only. If you have issues related to search results and currency, then contact an SEO expert. You can find Partners with SEO expertise in Shopify's [Partner Directory](https://www.shopify.com/partners/directory).

**Note:**

Any information on this page around search engines and SEO is for general information only. If you have issues related to search results and currency, then contact an SEO expert. You can find Partners with SEO expertise in Shopify's [Partner Directory](https://www.shopify.com/partners/directory).

### [Anchor to Considerations for structured data](/docs/storefronts/themes/markets/multiple-currencies-languages#considerations-for-structured-data)Considerations for structured data

When outputting [structured data](https://developers.google.com/search/docs/guides/intro-structured-data) for products, you need to ensure that the `priceCurrency` property is set to reflect the [cart currency](/docs/api/liquid/objects/cart#cart-currency), rather than the shop's currency.

For example:

9

1

priceCurrency: {{ cart.currency.iso\_code }},

---

Was this page helpful?

YesNo