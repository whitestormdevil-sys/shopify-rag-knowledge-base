---
source: https://shopify.dev/docs/api/liquid/filters/color_modify
---

9

1

string | color\_modify: string, number

returns [string](/docs/api/liquid/basics#string)

Modifies a specific color component of a given color by a specific amount.

The following table outlines valid color components, and the value range for their modifications:

| Component | Value range |
| --- | --- |
| * `red` * `green` * `blue` | An integer between 0 and 255 |
| `alpha` | A decimal between 0 and 1 |
| `hue` | An integer between 0 and 360 |
| * `saturation` * `lightness` | An integer between 0 and 100 |

9

1

{{ '#EA5AB9' | color\_modify: 'red', 255 }}

##### Code

```liquid
{{ '#EA5AB9' | color_modify: 'red', 255 }}
```

## Output

9

1

#ff5ab9

##### Output

```liquid
#ff5ab9
```

The format of the modified color depends on the component being modified. For example, if you modify the `alpha` component of a color in hexadecimal format, then the modified color will be in `rgba()` format.

9

1

{{ '#EA5AB9' | color\_modify: 'alpha', 0.85 }}

##### Code

```liquid
{{ '#EA5AB9' | color_modify: 'alpha', 0.85 }}
```

## Output

9

1

rgba(234, 90, 185, 0.85)

##### Output

```liquid
rgba(234, 90, 185, 0.85)
```

Was this page helpful?

YesNo