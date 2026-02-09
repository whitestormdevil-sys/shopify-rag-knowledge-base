---
source: https://shopify.dev/docs/api/liquid/filters/replace_first
---

9

1

string | replace\_first: string, string

returns [string](/docs/api/liquid/basics#string)

Replaces the first instance of a substring inside a string with a given string.

9

1

{{ product.handle | replace\_first: '-', ' ' }}

##### Code

```liquid
{{ product.handle | replace_first: '-', ' ' }}
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

komodo dragon-scale

##### Output

```liquid
komodo dragon-scale
```

Was this page helpful?

YesNo