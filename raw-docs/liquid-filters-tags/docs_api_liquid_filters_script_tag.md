---
source: https://shopify.dev/docs/api/liquid/filters/script_tag
---

9

1

string | script\_tag

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<script>` tag for a given resource URL. The tag has a `type` attribute of `text/javascript`.

9

1

{{ 'cart.js' | asset\_url | script\_tag }}

##### Code

```liquid
{{ 'cart.js' | asset_url | script_tag }}
```

## Output

9

1

<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" type="text/javascript"></script>

##### Output

```liquid
<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" type="text/javascript"></script>
```

Was this page helpful?

YesNo