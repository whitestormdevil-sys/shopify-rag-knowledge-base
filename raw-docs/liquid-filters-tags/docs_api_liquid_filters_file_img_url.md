---
source: https://shopify.dev/docs/api/liquid/filters/file_img_url
---

9

1

string | file\_img\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for an image from the
[Files](https://www.shopify.com/admin/settings/files) page of the Shopify admin.

9

1

{{ 'potions-header.png' | file\_img\_url }}

##### Code

```liquid
{{ 'potions-header.png' | file_img_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header\_small.png?v=4246568442683817558

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_small.png?v=4246568442683817558
```

[Anchor to The size parameter](/docs/api/liquid/filters/file_img_url#file_img_url-the-size-parameter)

### The size parameter

9

1

image | file\_img\_url: string

By default, the `file_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](/docs/api/liquid/filters/img_url#img_url-size).

9

1

{{ 'potions-header.png' | file\_img\_url: 'large' }}

##### Code

```liquid
{{ 'potions-header.png' | file_img_url: 'large' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header\_large.png?v=4246568442683817558

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header_large.png?v=4246568442683817558
```

Was this page helpful?

YesNo