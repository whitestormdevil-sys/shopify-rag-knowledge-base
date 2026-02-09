---
source: https://shopify.dev/docs/api/liquid/filters/font_face
---

9

1

font | font\_face

returns [string](/docs/api/liquid/basics#string)

Generates a CSS [`@font_face` declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/%40font-face) to load the provided font.

9

1

{{ settings.type\_header\_font | font\_face }}

##### Code

```liquid
{{ settings.type_header_font | font_face }}
```

##### Data

```liquid
{
  "settings": {
    "type_header_font": {}
  }
}
```

## Output

9

1

2

3

4

5

6

7

@font-face {

font-family: Assistant;

font-weight: 400;

font-style: normal;

src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),

url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");

}

##### Output

```liquid
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```

[Anchor to font\_display](/docs/api/liquid/filters/font_face#font_face-font_display)

### font\_display

9

1

font | font\_face: font\_display: string

You can include an optional parameter to specify the [`font_display` property](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) of the `@font_face` declaration.

9

1

{{ settings.type\_header\_font | font\_face: font\_display: 'swap' }}

##### Code

```liquid
{{ settings.type_header_font | font_face: font_display: 'swap' }}
```

##### Data

```liquid
{
  "settings": {
    "type_header_font": {}
  }
}
```

## Output

9

1

2

3

4

5

6

7

8

@font-face {

font-family: Assistant;

font-weight: 400;

font-style: normal;

font-display: swap;

src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),

url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant\_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");

}

##### Output

```liquid
@font-face {
  font-family: Assistant;
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.9120912a469cad1cc292572851508ca49d12e768.woff2") format("woff2"),
       url("//polinas-potent-potions.myshopify.com/cdn/fonts/assistant/assistant_n4.6e9875ce64e0fefcd3f4446b7ec9036b3ddd2985.woff") format("woff");
}
```

Was this page helpful?

YesNo