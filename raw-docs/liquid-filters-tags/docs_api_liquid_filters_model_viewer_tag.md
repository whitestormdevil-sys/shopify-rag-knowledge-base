---
source: https://shopify.dev/docs/api/liquid/filters/model_viewer_tag
---

9

1

media | model\_viewer\_tag

returns [string](/docs/api/liquid/basics#string)

Generates a [Google model viewer component](https://modelviewer.dev/) for a given 3D model.

9

1

2

3

4

5

{% for media in product.media %}

{% if media.media\_type == 'model' %}

{{ media | model\_viewer\_tag }}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag }}
  {% endif %}
{% endfor %}
```

##### Data

```liquid
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

## Output

9

1

<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle\_small.jpg?v=1655189057"></model-viewer>

##### Output

```liquid
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

[Anchor to Model viewer attributes](/docs/api/liquid/filters/model_viewer_tag#model_viewer_tag-model-viewer-attributes)

### Model viewer attributes

9

1

media | model\_viewer\_tag: attribute: string

By default, the model viewer component has the following attributes:

| Attribute | Value |
| --- | --- |
| `alt` | `[alt-text]` - The media's alt text. |
| `poster` | `[preview-image-url]` - The media's preview image URL. |
| `camera-controls` | N/A - Allows for controls via mouse/touch. |

You can override these attributes, or any [supported model viewer component attributes](https://modelviewer.dev/docs/index.html#stagingandcameras-attributes) by adding a parameter that matches the attribute name, and the desired value.

9

1

2

3

4

5

{% for media in product.media %}

{% if media.media\_type == 'model' %}

{{ media | model\_viewer\_tag: interaction-policy: 'allow-when-focused' }}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: interaction-policy: 'allow-when-focused' }}
  {% endif %}
{% endfor %}
```

##### Data

```liquid
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

## Output

9

1

<model-viewer interaction-policy="allow-when-focused" src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle\_small.jpg?v=1655189057"></model-viewer>

##### Output

```liquid
<model-viewer interaction-policy="allow-when-focused" src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

[Anchor to image\_size](/docs/api/liquid/filters/model_viewer_tag#model_viewer_tag-image_size)

### image\_size

9

1

media | model\_viewer\_tag: image\_size: string

Specify the dimensions of the model's poster image in pixels.

9

1

2

3

4

5

{% for media in product.media %}

{% if media.media\_type == 'model' %}

{{ media | model\_viewer\_tag: image\_size: '400x' }}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: image_size: '400x' }}
  {% endif %}
{% endfor %}
```

##### Data

```liquid
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

## Output

9

1

<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle\_400x.jpg?v=1655189057"></model-viewer>

##### Output

```liquid
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_400x.jpg?v=1655189057"></model-viewer>
```

Was this page helpful?

YesNo