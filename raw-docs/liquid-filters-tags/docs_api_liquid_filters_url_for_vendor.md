---
source: https://shopify.dev/docs/api/liquid/filters/url_for_vendor
---

9

1

string | url\_for\_vendor

returns [string](/docs/api/liquid/basics#string)

Generates a URL for a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products from the given product vendor.

9

1

{{ "Polina's Potent Potions" | url\_for\_vendor }}

##### Code

```liquid
{{ "Polina's Potent Potions" | url_for_vendor }}
```

## Output

9

1

/collections/vendors?q=Polina%27s%20Potent%20Potions

##### Output

```liquid
/collections/vendors?q=Polina%27s%20Potent%20Potions
```

Was this page helpful?

YesNo