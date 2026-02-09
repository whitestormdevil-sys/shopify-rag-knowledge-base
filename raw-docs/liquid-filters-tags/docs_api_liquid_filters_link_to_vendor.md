---
source: https://shopify.dev/docs/api/liquid/filters/link_to_vendor
---

9

1

string | link\_to\_vendor

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag with an `href` attribute linking to a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of a given
product vendor.

9

1

{{ "Polina's Potent Potions" | link\_to\_vendor }}

##### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor }}
```

## Output

9

1

<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

##### Output

```liquid
<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```

[Anchor to HTML attributes](/docs/api/liquid/filters/link_to_vendor#link_to_vendor-html-attributes)

### HTML attributes

9

1

string | link\_to\_vendor: attribute: string

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

9

1

{{ "Polina's Potent Potions" | link\_to\_vendor: class: 'link-class' }}

##### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor: class: 'link-class' }}
```

## Output

9

1

<a class="link-class" href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

##### Output

```liquid
<a class="link-class" href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```

Was this page helpful?

YesNo