---
source: https://shopify.dev/docs/api/liquid/filters/link_to
---

9

1

string | link\_to: string

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag.

9

1

{{ 'Shopify' | link\_to: 'https://www.shopify.com' }}

##### Code

```liquid
{{ 'Shopify' | link_to: 'https://www.shopify.com' }}
```

## Output

9

1

<a href="https://www.shopify.com" title="" rel="nofollow">Shopify</a>

##### Output

```liquid
<a href="https://www.shopify.com" title="" rel="nofollow">Shopify</a>
```

[Anchor to HTML attributes](/docs/api/liquid/filters/link_to#link_to-html-attributes)

### HTML attributes

9

1

string | link\_to\_type: attribute: string

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

9

1

{{ 'Shopify' | link\_to: 'https://www.shopify.com', class: 'link-class' }}

##### Code

```liquid
{{ 'Shopify' | link_to: 'https://www.shopify.com', class: 'link-class' }}
```

## Output

9

1

<a class="link-class" href="https://www.shopify.com" rel="nofollow">Shopify</a>

##### Output

```liquid
<a class="link-class" href="https://www.shopify.com" rel="nofollow">Shopify</a>
```

Was this page helpful?

YesNo