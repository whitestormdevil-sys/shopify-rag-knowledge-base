---
source: https://shopify.dev/docs/api/liquid/tags/style
---

Generates an HTML `<style>` tag with an attribute of `data-shopify`.

---

Note

If you reference [color settings](/themes/architecture/settings/input-settings#color) inside `style` tags, then
the associated CSS rules will update as the setting is changed in the theme editor, without a page refresh.

**Note:**

If you reference [color settings](/themes/architecture/settings/input-settings#color) inside `style` tags, then
the associated CSS rules will update as the setting is changed in the theme editor, without a page refresh.

**Note:** If you reference <a href="/themes/architecture/settings/input-settings#color">color settings</a> inside <code>style</code> tags, then
the associated CSS rules will update as the setting is changed in the theme editor, without a page refresh.

---

## Syntax

9

1

2

3

{% style %}

CSS\_rules

{% endstyle %}

CSS\_rules

The desired CSS rules for the `<style>` tag.

9

1

2

3

4

5

{% style %}

.h1 {

color: {{ settings.colors\_accent\_1 }};

}

{% endstyle %}

##### Code

```liquid
{% style %}
  .h1 {
    color: {{ settings.colors_accent_1 }};
  }
{% endstyle %}
```

##### Data

```liquid
{
  "settings": {
    "colors_accent_1": "#121212"
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

<style data-shopify>

.h1 {

color: #121212;

}

</style>

##### Output

```liquid
<style data-shopify>
  .h1 {
    color: #121212;
  }
</style>
```

Was this page helpful?

YesNo