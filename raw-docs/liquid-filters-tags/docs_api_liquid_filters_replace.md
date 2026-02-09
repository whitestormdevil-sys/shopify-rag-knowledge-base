---
source: https://shopify.dev/docs/api/liquid/filters/replace
---

9

1

string | replace: string, string

returns [string](/docs/api/liquid/basics#string)

Replaces any instance of a substring inside a string with a given string.

9

1

{{ product.handle | replace: '-', ' ' }}

##### Code

```liquid
{{ product.handle | replace: '-', ' ' }}
```

##### Data

```liquid
{
  "product": {
    "handle": "komodo-dragon-scale"
  }
}
```

## Output

9

1

komodo dragon scale

##### Output

```liquid
komodo dragon scale
```

Was this page helpful?

YesNo