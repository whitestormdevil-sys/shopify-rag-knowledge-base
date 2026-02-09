---
source: https://shopify.dev/docs/api/liquid/filters/font_url
---

9

1

font | font\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for the provided font in `woff2` format.

9

1

{{ settings.type\_header\_font | font\_url }}

##### Code

```liquid
{{ settings.type_header_font | font_url }}
```

##### Data

```liquid
{
  "settings": {
    "type_header_font": {}
  }
}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.9120912a469cad1cc292572851508ca49d12e768.woff2

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2
```

[Anchor to woff format](/docs/api/liquid/filters/font_url#font_url-woff-format)

### woff format

9

1

font | font\_url: string

By default, the `font_url` filter returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for the font in `woff2` format. However, you can also choose `woff` format.

9

1

{{ settings.type\_header\_font | font\_url: 'woff' }}

##### Code

```liquid
{{ settings.type_header_font | font_url: 'woff' }}
```

##### Data

```liquid
{
  "settings": {
    "type_header_font": {}
  }
}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff
```

Was this page helpful?

YesNo