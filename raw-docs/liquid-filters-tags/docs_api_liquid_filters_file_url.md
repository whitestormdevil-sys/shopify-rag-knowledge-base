---
source: https://shopify.dev/docs/api/liquid/filters/file_url
---

9

1

string | file\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for a file from the
[Files](https://www.shopify.com/admin/settings/files) page of the Shopify admin.

9

1

{{ 'disclaimer.pdf' | file\_url }}

##### Code

```liquid
{{ 'disclaimer.pdf' | file_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859
```

Was this page helpful?

YesNo