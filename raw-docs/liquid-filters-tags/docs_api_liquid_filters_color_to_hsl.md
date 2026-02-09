---
source: https://shopify.dev/docs/api/liquid/filters/color_to_hsl
---

9

1

string | color\_to\_hsl

returns [string](/docs/api/liquid/basics#string)

Converts a CSS color string to `HSL` format.

If a color with an alpha component is provided, the color is converted to `HSLA` format.

9

1

{{ '#EA5AB9' | color\_to\_hsl }}

##### Code

```liquid
{{ '#EA5AB9' | color_to_hsl }}
```

## Output

9

1

hsl(320, 77%, 64%)

##### Output

```liquid
hsl(320, 77%, 64%)
```

Was this page helpful?

YesNo