---
source: https://shopify.dev/docs/api/liquid/tags/layout
---

Specify which [layout](/themes/architecture/layouts) to use.

## Syntax

9

1

{% layout name %}

name

The name of the layout file you want to use, wrapped in quotes, or `none` for no layout.

By default, the `theme.liquid` layout is used. The `layout` tag allows you to specify an alternate layout, or use no layout.

9

1

2

{% layout 'full-width' %}

{% layout none %}

```liquid
{% layout 'full-width' %}
{% layout none %}
```

Was this page helpful?

YesNo