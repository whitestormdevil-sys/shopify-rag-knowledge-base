---
source: https://shopify.dev/docs/api/liquid/filters/brightness_difference
---

9

1

string | brightness\_difference: string

returns [number](/docs/api/liquid/basics#number)

Calculates the [perceived brightness difference](https://www.w3.org/WAI/ER/WD-AERT/#color-contrast) between two colors.

---

Tip

For accessibility best practices, it's recommended to have a minimum brightness difference of 125.

**Tip:**

For accessibility best practices, it's recommended to have a minimum brightness difference of 125.

**Tip:** For accessibility best practices, it&#39;s recommended to have a minimum brightness difference of 125.

---

9

1

{{ '#E800B0' | brightness\_difference: '#FECEE9' }}

##### Code

```liquid
{{ '#E800B0' | brightness_difference: '#FECEE9' }}
```

## Output

9

1

134

##### Output

```liquid
134
```

Was this page helpful?

YesNo