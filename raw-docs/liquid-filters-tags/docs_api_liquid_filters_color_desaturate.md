---
source: https://shopify.dev/docs/api/liquid/filters/color_desaturate
---

9

1

string | color\_desaturate: number

returns [string](/docs/api/liquid/basics#string)

Desaturates a given color by a specific percentage. The percentage must be between 0 and 100.

9

1

{{ '#EA5AB9' | color\_desaturate: 30 }}

##### Code

```liquid
{{ '#EA5AB9' | color_desaturate: 30 }}
```

## Output

9

1

#ce76b0

##### Output

```liquid
#ce76b0
```

Was this page helpful?

YesNo