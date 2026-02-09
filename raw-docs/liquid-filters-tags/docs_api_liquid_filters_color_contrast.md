---
source: https://shopify.dev/docs/api/liquid/filters/color_contrast
---

9

1

string | color\_contrast: string

returns [number](/docs/api/liquid/basics#number)

Calculates the contrast ratio between two colors and returns the ratio's numerator. The ratio's denominator, which isn't
returned, is always 1. For example, with a contrast ratio of 3.5:1, this filter returns 3.5.

The order in which you specify the colors doesn't matter.

---

Tip

For accessibility best practices, the
[WCAG 2.0 level AA](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast-contrast) requires a
minimum contrast ratio of 4.5:1 for normal text, and 3:1 for large text. [Level AAA](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast7)
requires a minimum contrast ratio of 7:1 for normal text, and 4.5:1 for large text.

**Tip:**

For accessibility best practices, the
[WCAG 2.0 level AA](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast-contrast) requires a
minimum contrast ratio of 4.5:1 for normal text, and 3:1 for large text. [Level AAA](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast7)
requires a minimum contrast ratio of 7:1 for normal text, and 4.5:1 for large text.

**Tip:** For accessibility best practices, the
<a href="https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast-contrast">WCAG 2.0 level AA</a> requires a
minimum contrast ratio of 4.5:1 for normal text, and 3:1 for large text. <a href="https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast7">Level AAA</a>
requires a minimum contrast ratio of 7:1 for normal text, and 4.5:1 for large text.

---

9

1

{{ '#E800B0' | color\_contrast: '#D9D8FF' }}

##### Code

```liquid
{{ '#E800B0' | color_contrast: '#D9D8FF' }}
```

## Output

9

1

3.0

##### Output

```liquid
3.0
```

Was this page helpful?

YesNo