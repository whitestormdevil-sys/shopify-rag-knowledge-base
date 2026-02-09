---
source: https://shopify.dev/docs/api/liquid/filters/url_for_type
---

9

1

string | url\_for\_type

returns [string](/docs/api/liquid/basics#string)

Generates a URL for a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of the given product type.

9

1

{{ 'health' | url\_for\_type }}

##### Code

```liquid
{{ 'health' | url_for_type }}
```

## Output

9

1

/collections/types?q=health

##### Output

```liquid
/collections/types?q=health
```

Was this page helpful?

YesNo