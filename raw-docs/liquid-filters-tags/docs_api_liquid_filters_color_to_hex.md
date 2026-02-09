---
source: https://shopify.dev/docs/api/liquid/filters/color_to_hex
---

9

1

string | color\_to\_hex

returns [string](/docs/api/liquid/basics#string)

Converts a CSS color string to hexadecimal format (`hex6`).

Because colors are converted to `hex6` format, if a color with an alpha component is provided, then the alpha component
is excluded from the output.

9

1

{{ 'rgb(234, 90, 185)' | color\_to\_hex }}

##### Code

```liquid
{{ 'rgb(234, 90, 185)' | color_to_hex }}
```

## Output

9

1

#ea5ab9

##### Output

```liquid
#ea5ab9
```

Was this page helpful?

YesNo