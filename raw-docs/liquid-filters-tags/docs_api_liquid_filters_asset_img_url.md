---
source: https://shopify.dev/docs/api/liquid/filters/asset_img_url
---

9

1

string | asset\_img\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for an image in the
[`assets` directory](/themes/architecture#assets) of a theme.

9

1

{{ 'red-and-black-bramble-berries.jpg' | asset\_img\_url }}

##### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries\_small.jpg?v=336

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_small.jpg?v=336
```

[Anchor to size](/docs/api/liquid/filters/asset_img_url#asset_img_url-size)

### size

9

1

image | asset\_img\_url: string

By default, the `asset_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](/docs/api/liquid/filters/img_url#img_url-size).

9

1

{{ 'red-and-black-bramble-berries.jpg' | asset\_img\_url: 'large' }}

##### Code

```liquid
{{ 'red-and-black-bramble-berries.jpg' | asset_img_url: 'large' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries\_large.jpg?v=336

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/red-and-black-bramble-berries_large.jpg?v=336
```

Was this page helpful?

YesNo