---
source: https://shopify.dev/docs/api/liquid/filters/stylesheet_tag
---

9

1

string | stylesheet\_tag

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<link>` tag for a given resource URL. The tag has the following parameters:

| Attribute | Value |
| --- | --- |
| `rel` | `stylesheet` |
| `type` | `text/css` |
| `media` | `all` |

9

1

{{ 'base.css' | asset\_url | stylesheet\_tag }}

##### Code

```liquid
{{ 'base.css' | asset_url | stylesheet_tag }}
```

## Output

9

1

<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/base.css?v=88290808517547527771663872409" rel="stylesheet" type="text/css" media="all" />

##### Output

```liquid
<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/base.css?v=88290808517547527771663872409" rel="stylesheet" type="text/css" media="all" />
```

[Anchor to preload](/docs/api/liquid/filters/stylesheet_tag#stylesheet_tag-preload)

### preload

9

1

stylesheet\_url | stylesheet\_tag: preload: boolean

Specify whether the stylesheet should be preloaded.

When `preload` is set to `true`, a resource hint is sent as a [Link header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) with a `rel` value of
[`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload).

9

1

Link: <STYLESHEET\_URL>; rel=preload; as=style

```liquid
Link: ; rel=preload; as=style
```

This option doesn't affect the HTML link tag directly.

You should use the `preload` parameter sparingly. For example, consider preloading only render-blocking stylesheets that
are needed for initial functionality of the page, such as above-the-fold content. To learn more about resource hints in
Shopify themes, refer to [Performance best practices for Shopify themes](/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others).

Was this page helpful?

YesNo