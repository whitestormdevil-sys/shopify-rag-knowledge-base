---
source: https://shopify.dev/docs/api/liquid/filters/color_difference
---

9

1

string | color\_difference: string

returns [number](/docs/api/liquid/basics#number)

Calculates the [color difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two colors.

---

Tip

For accessibility best practices, it's recommended to have a minimum color difference of 500.

**Tip:**

For accessibility best practices, it's recommended to have a minimum color difference of 500.

**Tip:** For accessibility best practices, it&#39;s recommended to have a minimum color difference of 500.

---

9

1

{{ '#720955' | color\_difference: '#FFF3F9' }}

##### Code

```liquid
{{ '#720955' | color_difference: '#FFF3F9' }}
```

## Output

9

1

539

##### Output

```liquid
539
```

Was this page helpful?

YesNo