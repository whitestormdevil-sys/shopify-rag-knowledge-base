---
source: https://shopify.dev/docs/api/liquid/objects/color
---

A color from a [`color` setting](/themes/architecture/settings/input-settings#color).

---

Tip

Use [color filters](/docs/api/liquid/filters/color-filters) to modify or extract properties of a `color` object.

**Tip:**

Use [color filters](/docs/api/liquid/filters/color-filters) to modify or extract properties of a `color` object.

**Tip:** Use <a href="/docs/api/liquid/filters/color-filters">color filters</a> to modify or extract properties of a <code>color</code> object.

---

## Properties

[Anchor to](/docs/api/liquid/objects/color#color-alpha) 

alpha**alpha** [number](/docs/api/liquid/basics#number)

:   The alpha component of the color, which is a decimal number between 0.0 and 1.0.

[Anchor to](/docs/api/liquid/objects/color#color-blue) 

blue**blue** [number](/docs/api/liquid/basics#number)

:   The blue component of the color, which is a number between 0 and 255.

[Anchor to](/docs/api/liquid/objects/color#color-chroma) 

chroma**chroma** [number](/docs/api/liquid/basics#number)

:   The chroma component of the color, which is a decimal number between 0.0 and 0.5.

[Anchor to](/docs/api/liquid/objects/color#color-color_space) 

color\_space**color\_space** [string](/docs/api/liquid/basics#string)

:   The color space of the color. Returns 'srgb' or 'oklch'

[Anchor to](/docs/api/liquid/objects/color#color-green) 

green**green** [number](/docs/api/liquid/basics#number)

:   The green component of the color, which is a number between 0 and 255.

[Anchor to](/docs/api/liquid/objects/color#color-hue) 

hue**hue** [number](/docs/api/liquid/basics#number)

:   The hue component of the color, which is a number between 0 and 360.

[Anchor to](/docs/api/liquid/objects/color#color-lightness) 

lightness**lightness** [number](/docs/api/liquid/basics#number)

:   The lightness component of the color, which is a number between 0 and 100.

[Anchor to](/docs/api/liquid/objects/color#color-oklch) 

oklch**oklch** [string](/docs/api/liquid/basics#string)

:   The lightness, chroma, and hue values of the color, represented as a
    space-separated string.

[Anchor to](/docs/api/liquid/objects/color#color-oklcha) 

oklcha**oklcha** [string](/docs/api/liquid/basics#string)

:   The lightness, chroma, hue and alpha values of the color, represented as a
    space-separated string, with a slash before the alpha channel.

[Anchor to](/docs/api/liquid/objects/color#color-red) 

red**red** [number](/docs/api/liquid/basics#number)

:   The red component of the color, which is a number between 0 and 255.

[Anchor to](/docs/api/liquid/objects/color#color-rgb) 

rgb**rgb** [string](/docs/api/liquid/basics#string)

:   The red, green, and blue values of the color, represented as a space-separated string.

[Anchor to](/docs/api/liquid/objects/color#color-rgba) 

rgba**rgba** [string](/docs/api/liquid/basics#string)

:   The red, green, blue, and alpha values of the color, represented as a
    space-separated string, with a slash before the alpha channel.

[Anchor to](/docs/api/liquid/objects/color#color-saturation) 

saturation**saturation** [number](/docs/api/liquid/basics#number)

:   The saturation component of the color, which is a number between 0 and 100.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

{

"alpha": 1,

"blue": 180,

"chroma": 0.16,

"color\_space": "srgb",

"green": 79,

"hue": 227,

"lightness": 45,

"oklch": "47% 0.16 268",

"oklcha": "47% 0.16 268 / 1.0",

"red": 51,

"rgb": "51 79 180",

"rgba": "51 79 180 / 1.0",

"saturation": 56

}

##### Example

```liquid
{
  "alpha": 1,
  "blue": 180,
  "chroma": 0.16,
  "color_space": "srgb",
  "green": 79,
  "hue": 227,
  "lightness": 45,
  "oklch": "47% 0.16 268",
  "oklcha": "47% 0.16 268 / 1.0",
  "red": 51,
  "rgb": "51 79 180",
  "rgba": "51 79 180 / 1.0",
  "saturation": 56
}
```

[Anchor to Referencing color settings directly](/docs/api/liquid/objects/color#color-referencing-color-settings-directly)

### Referencing color settings directly

When a color setting is referenced directly, the hexidecimal color code is returned.

9

1

{{ settings.colors\_accent\_2 }}

##### Code

```liquid
{{ settings.colors_accent_2 }}
```

##### Data

```liquid
{
  "settings": {
    "colors_accent_2": "#334fb4"
  }
}
```

## Output

9

1

#334fb4

##### Output

```liquid
#334fb4
```

Was this section helpful?

YesNo