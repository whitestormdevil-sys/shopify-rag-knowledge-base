---
source: https://shopify.dev/docs/api/liquid/filters/asset_url
---

9

1

string | asset\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for a file in the
[`assets` directory](/themes/architecture#assets) of a theme.

9

1

{{ 'cart.js' | asset\_url }}

##### Code

```liquid
{{ 'cart.js' | asset_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410
```

Was this page helpful?

YesNo