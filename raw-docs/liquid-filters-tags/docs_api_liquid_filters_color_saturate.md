---
source: https://shopify.dev/docs/api/liquid/filters/color_saturate
---

9

1

string | color\_saturate: number

returns [string](/docs/api/liquid/basics#string)

Saturates a given color by a specific percentage. The percentage must be between 0 and 100.

9

1

{{ '#EA5AB9' | color\_saturate: 30 }}

##### Code

```liquid
{{ '#EA5AB9' | color_saturate: 30 }}
```

## Output

9

1

#ff45c0

##### Output

```liquid
#ff45c0
```

Was this page helpful?

YesNo