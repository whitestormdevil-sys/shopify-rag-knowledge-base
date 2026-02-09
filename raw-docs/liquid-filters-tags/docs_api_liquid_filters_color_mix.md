---
source: https://shopify.dev/docs/api/liquid/filters/color_mix
---

9

1

string | color\_mix: string, number

returns [string](/docs/api/liquid/basics#string)

Blends two colors together by a specific percentage factor. The percentage must be between 0 and 100.

---

Tip

A percentage factor of 100 returns the color being filtered. A percentage factor of 0 returns the color
supplied to the filter.

**Tip:**

A percentage factor of 100 returns the color being filtered. A percentage factor of 0 returns the color
supplied to the filter.

**Tip:** A percentage factor of 100 returns the color being filtered. A percentage factor of 0 returns the color
supplied to the filter.

---

9

1

{{ '#E800B0' | color\_mix: '#00936F', 50 }}

##### Code

```liquid
{{ '#E800B0' | color_mix: '#00936F', 50 }}
```

## Output

9

1

#744a90

##### Output

```liquid
#744a90
```

If one input has an alpha component, but the other does not, an alpha component of 1.0 will be assumed for the input without an alpha component.

9

1

{{ 'rgba(232, 0, 176, 0.75)' | color\_mix: '#00936F', 50 }}

##### Code

```liquid
{{ 'rgba(232, 0, 176, 0.75)' | color_mix: '#00936F', 50 }}
```

## Output

9

1

rgba(116, 74, 144, 0.88)

##### Output

```liquid
rgba(116, 74, 144, 0.88)
```

Was this page helpful?

YesNo