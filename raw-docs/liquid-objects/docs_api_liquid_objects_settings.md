---
source: https://shopify.dev/docs/api/liquid/objects/settings
---

Allows you to access all of the theme's settings from the [`settings_schema.json` file](/themes/architecture/config/settings-schema-json).

---

Tip

To learn about the available setting types, refer to [Input settings](/themes/architecture/settings/input-settings).

**Tip:**

To learn about the available setting types, refer to [Input settings](/themes/architecture/settings/input-settings).

**Tip:** To learn about the available setting types, refer to <a href="/themes/architecture/settings/input-settings">Input settings</a>.

---

### Directly accessible in

* Global

[Anchor to Reference a setting value](/docs/api/liquid/objects/settings#settings-reference-a-setting-value)

### Reference a setting value

9

1

2

3

{% if settings.favicon != blank %}

<link rel="icon" type="image/png" href="{{ settings.favicon | image\_url: width: 32, height: 32 }}">

{% endif %}

##### Code

```liquid
{% if settings.favicon != blank %}
  <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
{% endif %}
```

##### Data

```liquid
{
  "settings": {
    "favicon": null
  }
}
```

## Output

9

1

##### Output

Was this section helpful?

YesNo