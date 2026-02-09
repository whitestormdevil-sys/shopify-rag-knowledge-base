---
source: https://shopify.dev/docs/api/liquid/filters/downcase
---

9

1

string | downcase

returns [string](/docs/api/liquid/basics#string)

Converts a string to all lowercase characters.

9

1

{{ product.title | downcase }}

##### Code

```liquid
{{ product.title | downcase }}
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

health potion

##### Output

```liquid
health potion
```

Was this page helpful?

YesNo