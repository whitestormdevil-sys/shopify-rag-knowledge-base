---
source: https://shopify.dev/docs/api/liquid/filters/shopify_asset_url
---

9

1

string | shopify\_asset\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for a globally accessible Shopify asset.

The following are the globally accessible Shopify assets:

* `option_selection.js`
* `api.jquery.js`
* `shopify_common.js`
* `customer_area.js`
* `currencies.js`
* `customer.css`

9

1

{{ 'option\_selection.js' | shopify\_asset\_url }}

##### Code

```liquid
{{ 'option_selection.js' | shopify_asset_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/themes\_support/option\_selection-b017cd28.js

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/themes_support/option_selection-b017cd28.js
```

Was this page helpful?

YesNo