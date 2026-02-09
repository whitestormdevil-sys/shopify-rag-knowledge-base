---
source: https://shopify.dev/docs/api/liquid/objects/font
---

A font from a [`font_picker` setting](/themes/architecture/settings/input-settings#font_picker).

You can use the `font` object in Liquid [assets](/themes/architecture#assets) or inside a [`style` tag](/docs/api/liquid/tags/style)
to apply font setting values to theme CSS.

---

Tip

Use [font filters](/docs/api/liquid/filters/font-filters) to modify properties of the `font` object, load the font,
or obtain font variants.

**Tip:**

Use [font filters](/docs/api/liquid/filters/font-filters) to modify properties of the `font` object, load the font,
or obtain font variants.

**Tip:** Use <a href="/docs/api/liquid/filters/font-filters">font filters</a> to modify properties of the <code>font</code> object, load the font,
or obtain font variants.

---

## Properties

[Anchor to](/docs/api/liquid/objects/font#font-baseline_ratio) 

baseline\_ratio**baseline\_ratio** [number](/docs/api/liquid/basics#number)

:   The baseline ratio of the font as a decimal.

[Anchor to](/docs/api/liquid/objects/font#font-fallback_families) 

fallback\_families**fallback\_families** [string](/docs/api/liquid/basics#string)

:   The fallback families of the font.

[Anchor to](/docs/api/liquid/objects/font#font-family) 

family**family** [string](/docs/api/liquid/basics#string)

:   The family name of the font.

    Tip

    If the family name contains non-alphanumeric characters (A-Z, a-z, 0-9, or '-'), then it will be wrapped in double quotes.

    **Tip:**

    If the family name contains non-alphanumeric characters (A-Z, a-z, 0-9, or '-'), then it will be wrapped in double quotes.

    **Tip:** If the family name contains non-alphanumeric characters (A-Z, a-z, 0-9, or &#39;-&#39;), then it will be wrapped in double quotes.

[Anchor to](/docs/api/liquid/objects/font#font-style) 

style**style** [string](/docs/api/liquid/basics#string)

:   The style of the font.

[Anchor to](/docs/api/liquid/objects/font#font-system?) 

system?**system?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the font is a system font. Returns `false` if not.

    Tip

    You can use this property to determine whether you need to include a corresponding [font-face](/docs/api/liquid/filters/font_face)
    declaration for the font.

    **Tip:**

    You can use this property to determine whether you need to include a corresponding [font-face](/docs/api/liquid/filters/font_face)
    declaration for the font.

    **Tip:** You can use this property to determine whether you need to include a corresponding <a href="/docs/api/liquid/filters/font\_face">font-face</a>
    declaration for the font.

[Anchor to](/docs/api/liquid/objects/font#font-variants) 

variants**variants** array of [font](/docs/api/liquid/objects/font)

:   The variants in the family of the font.

[Anchor to](/docs/api/liquid/objects/font#font-weight) 

weight**weight** [number](/docs/api/liquid/basics#number)

:   The weight of the font.

9

1

2

3

4

5

6

7

8

9

{

"baseline\_ratio": 0.133,

"fallback\_families": "sans-serif",

"family": "Assistant",

"style": "normal",

"system?": false,

"variants": {},

"weight": "400"

}

##### Example

```liquid
{
  "baseline_ratio": 0.133,
  "fallback_families": "sans-serif",
  "family": "Assistant",
  "style": "normal",
  "system?": false,
  "variants": {},
  "weight": "400"
}
```

Was this section helpful?

YesNo