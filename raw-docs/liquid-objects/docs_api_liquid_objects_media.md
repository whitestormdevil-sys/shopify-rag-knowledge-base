---
source: https://shopify.dev/docs/api/liquid/objects/media
---

An abstract media object that can represent the following object types:

* [`image`](/docs/api/liquid/objects/image)
* [`model`](/docs/api/liquid/objects/model)
* [`video`](/docs/api/liquid/objects/video)
* [`external_video`](/docs/api/liquid/objects/external_video)

The `media` object can be returned by the [`product.media` array](/docs/api/liquid/objects/product#product-media) or a
[`file_reference` metafield](/apps/metafields/types).

You can use [media filters](/docs/api/liquid/filters/media-filters) to generate URLs and media displays. To learn about how
to use media in your theme, refer to [Support product media](/themes/product-merchandising/media/support-media).

---

Note

Each media type has unique properties in addition to the general `media` properties. To learn about these
additional properties, refer to the reference for each type.

**Note:**

Each media type has unique properties in addition to the general `media` properties. To learn about these
additional properties, refer to the reference for each type.

**Note:** Each media type has unique properties in addition to the general <code>media</code> properties. To learn about these
additional properties, refer to the reference for each type.

---

## Properties

[Anchor to](/docs/api/liquid/objects/media#media-alt) 

alt**alt** [string](/docs/api/liquid/basics#string)

:   The alt text of the media.

[Anchor to](/docs/api/liquid/objects/media#media-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the media.

[Anchor to](/docs/api/liquid/objects/media#media-media_type) 

media\_type**media\_type** [string](/docs/api/liquid/basics#string) from a set of values

:   The media type.

    | Possible values |
    | --- |
    | image |
    | model |
    | video |
    | external\_video |

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

    {% assign images = product.media | where: 'media\_type', 'image' %}

    {% for image in images %}

    {{- image | image\_url: width: 300 | image\_tag }}

    {% endfor %}

    ##### Code

    ```liquid
    {% assign images = product.media | where: 'media_type', 'image' %}

    {% for image in images %}
      {{- image | image_url: width: 300 | image_tag }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "media": [
          "products/oil-dripping-into-jar.jpg"
        ]
      }
    }
    ```

    ## Output

    9

    1

    <img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300" alt="Viper venom" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300 300w" width="300" height="200">

    ##### Output

    ```liquid
    <img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300" alt="Viper venom" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300 300w" width="300" height="200">
    ```

[Anchor to](/docs/api/liquid/objects/media#media-position) 

position**position** [number](/docs/api/liquid/basics#number)

:   The position of the media in the [`product.media` array](/docs/api/liquid/objects/product#product-media).

    If the source is a [`file_reference` metafield](/apps/metafields/types), then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/media#media-preview_image) 

preview\_image**preview\_image** [image](/docs/api/liquid/objects/image)

:   A preview image of the media.

    Note

    Preview images don't have an ID attribute.

    **Note:**

    Preview images don't have an ID attribute.

    **Note:** Preview images don&#39;t have an ID attribute.

9

1

2

3

4

5

6

7

{

"alt": "Dandelion milk",

"id": 21772527435841,

"media\_type": "image",

"position": 1,

"preview\_image": {}

}

##### Example

```liquid
{
  "alt": "Dandelion milk",
  "id": 21772527435841,
  "media_type": "image",
  "position": 1,
  "preview_image": {}
}
```

Was this section helpful?

YesNo