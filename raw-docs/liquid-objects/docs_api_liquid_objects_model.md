---
source: https://shopify.dev/docs/api/liquid/objects/model
---

A 3D model uploaded as product media.

---

Tip

Use the [`model_viewer_tag` filter](/docs/api/liquid/filters/model_viewer_tag) to output a [Google model viewer component](https://modelviewer.dev)
for the model.

**Tip:**

Use the [`model_viewer_tag` filter](/docs/api/liquid/filters/model_viewer_tag) to output a [Google model viewer component](https://modelviewer.dev)
for the model.

**Tip:** Use the <a href="/docs/api/liquid/filters/model\_viewer\_tag"><code><span class="PreventFireFoxApplyingGapToWBR">model<wbr/>\_viewer<wbr/>\_tag</span></code> filter</a> to output a <a href="https://modelviewer.dev">Google model viewer component</a>
for the model.

---

## Properties

[Anchor to](/docs/api/liquid/objects/model#model-alt) 

alt**alt** [string](/docs/api/liquid/basics#string)

:   The alt text of the model.

[Anchor to](/docs/api/liquid/objects/model#model-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the model.

[Anchor to](/docs/api/liquid/objects/model#model-media_type) 

media\_type**media\_type** [string](/docs/api/liquid/basics#string)

:   The media type of the model. Always returns `model`.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Filter for media of a specific type

    You can use the `media_type` property with the [`where` filter](/docs/api/liquid/filters/where) to filter the [`product.media` array](/docs/api/liquid/objects/product#product-media) for all media of a desired type.

    9

    1

    2

    3

    4

    5

    {% assign models = product.media | where: 'media\_type', 'model' %}

    {% for model in models %}

    {{- model | model\_viewer\_tag }}

    {% endfor %}

    ##### Code

    ```liquid
    {% assign models = product.media | where: 'media_type', 'model' %}

    {% for model in models %}
      {{- model | model_viewer_tag }}
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

[Anchor to](/docs/api/liquid/objects/model#model-position) 

position**position** [number](/docs/api/liquid/basics#number)

:   The position of the model in the [`product.media`](/docs/api/liquid/objects/product#product-media) array.

[Anchor to](/docs/api/liquid/objects/model#model-preview_image) 

preview\_image**preview\_image** [image](/docs/api/liquid/objects/image)

:   A preview image for the model.

[Anchor to](/docs/api/liquid/objects/model#model-sources) 

sources**sources** array of [model\_source](/docs/api/liquid/objects/model_source)

:   The source files for the model.

9

1

2

3

4

5

6

7

8

{

"alt": "Potion bottle",

"id": 22064203137089,

"media\_type": "model",

"position": 1,

"preview\_image": {},

"sources": []

}

##### Example

```liquid
{
  "alt": "Potion bottle",
  "id": 22064203137089,
  "media_type": "model",
  "position": 1,
  "preview_image": {},
  "sources": []
}
```

Was this section helpful?

YesNo