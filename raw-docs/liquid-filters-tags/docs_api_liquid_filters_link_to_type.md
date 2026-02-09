---
source: https://shopify.dev/docs/api/liquid/filters/link_to_type
---

9

1

string | link\_to\_type

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag with an `href` attribute linking to a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of the given
product type.

9

1

{{ 'Health' | link\_to\_type }}

##### Code

```liquid
{{ 'Health' | link_to_type }}
```

## Output

9

1

<a href="/collections/types?q=Health" title="Health">Health</a>

##### Output

```liquid
<a href="/collections/types?q=Health" title="Health">Health</a>
```

[Anchor to HTML attributes](/docs/api/liquid/filters/link_to_type#link_to_type-html-attributes)

### HTML attributes

9

1

string | link\_to\_type: attribute: string

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

9

1

{{ 'Health' | link\_to\_type: class: 'link-class' }}

##### Code

```liquid
{{ 'Health' | link_to_type: class: 'link-class' }}
```

## Output

9

1

<a class="link-class" href="/collections/types?q=Health" title="Health">Health</a>

##### Output

```liquid
<a class="link-class" href="/collections/types?q=Health" title="Health">Health</a>
```

Was this page helpful?

YesNo