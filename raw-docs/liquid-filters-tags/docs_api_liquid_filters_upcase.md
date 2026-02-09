---
source: https://shopify.dev/docs/api/liquid/filters/upcase
---

9

1

string | upcase

returns [string](/docs/api/liquid/basics#string)

Converts a string to all uppercase characters.

9

1

{{ product.title | upcase }}

##### Code

```liquid
{{ product.title | upcase }}
```

##### Data

```liquid
{
  "product": {
    "title": "Health potion"
  }
}
```

## Output

9

1

HEALTH POTION

##### Output

```liquid
HEALTH POTION
```

Was this page helpful?

YesNo