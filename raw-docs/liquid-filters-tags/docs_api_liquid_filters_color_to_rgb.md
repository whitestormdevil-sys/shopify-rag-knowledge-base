---
source: https://shopify.dev/docs/api/liquid/filters/color_to_rgb
---

9

1

string | color\_to\_rgb

returns [string](/docs/api/liquid/basics#string)

Converts a CSS color string to `RGB` format.

If a color with an alpha component is provided, then the color is converted to `RGBA` format.

9

1

{{ '#EA5AB9' | color\_to\_rgb }}

##### Code

```liquid
{{ '#EA5AB9' | color_to_rgb }}
```

## Output

9

1

rgb(234, 90, 185)

##### Output

```liquid
rgb(234, 90, 185)
```

Was this page helpful?

YesNo