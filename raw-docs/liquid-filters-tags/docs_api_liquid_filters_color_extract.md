---
source: https://shopify.dev/docs/api/liquid/filters/color_extract
---

9

1

string | color\_extract: string

returns [number](/docs/api/liquid/basics#number)

Extracts a specific color component from a given color.

Accepts the following color components:

* `alpha`
* `red`
* `green`
* `blue`
* `hue`
* `saturation`
* `lightness`

9

1

{{ '#EA5AB9' | color\_extract: 'red' }}

##### Code

```liquid
{{ '#EA5AB9' | color_extract: 'red' }}
```

## Output

9

1

234

##### Output

```liquid
234
```

Was this page helpful?

YesNo