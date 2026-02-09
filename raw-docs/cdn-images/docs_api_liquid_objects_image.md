---
source: https://shopify.dev/docs/api/liquid/objects/image
---

An image, such as a product or collection image.

To learn about the image formats that Shopify supports, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/images/theme-images#image-formats).

---

Tip

Use the [`image_url`](/docs/api/liquid/filters/image_url) and [`image_tag`](/docs/api/liquid/filters/image_tag) filters to display
images on the storefront.

**Tip:**

Use the [`image_url`](/docs/api/liquid/filters/image_url) and [`image_tag`](/docs/api/liquid/filters/image_tag) filters to display
images on the storefront.

**Tip:** Use the <a href="/docs/api/liquid/filters/image\_url"><code><span class="PreventFireFoxApplyingGapToWBR">image<wbr/>\_url</span></code></a> and <a href="/docs/api/liquid/filters/image\_tag"><code><span class="PreventFireFoxApplyingGapToWBR">image<wbr/>\_tag</span></code></a> filters to display
images on the storefront.

---

## Properties

[Anchor to](/docs/api/liquid/objects/image#image-alt) 

alt**alt** [string](/docs/api/liquid/basics#string)

:   The alt text of the image.

[Anchor to](/docs/api/liquid/objects/image#image-aspect_ratio) 

aspect\_ratio**aspect\_ratio** [number](/docs/api/liquid/basics#number)

:   The aspect ratio of the image as a decimal.

[Anchor to](/docs/api/liquid/objects/image#image-attached_to_variant?) 

attached\_to\_variant?**attached\_to\_variant?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the image is associated with a variant. Returns `false` if not.

    The `attached_to_variant?` property is only available for images accessed through the following sources:

    * [`product.featured_image`](/docs/api/liquid/objects/product#product-featured_image)
    * [`product.images`](/docs/api/liquid/objects/product#product-images)

    If you reference this property on an image from another source, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-height) 

height**height** [number](/docs/api/liquid/basics#number)

:   The height of the image in pixels.

[Anchor to](/docs/api/liquid/objects/image#image-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the image.

    If you reference the `id` property for preview images of [`generic_file`](/docs/api/liquid/objects/generic_file) or
    [`media`](/docs/api/liquid/objects/media) objects, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-media_type) 

media\_type**media\_type** [string](/docs/api/liquid/basics#string)

:   The media type of the image. Always returns `image`.

    The `media_type` property is only available for images accessed through the following sources:

    * [`product.media`](/docs/api/liquid/objects/product#product-media)
    * [`file_reference` type metafields](/apps/metafields/types#supported-types)

    If you reference this property on an image from another source, then `nil` is returned.

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

[Anchor to](/docs/api/liquid/objects/image#image-position) 

position**position** [number](/docs/api/liquid/basics#number)

:   The position of the image in the [`product.images`](/docs/api/liquid/objects/product#product-images) or [`product.media`](/docs/api/liquid/objects/product#product-media)
    array.

    The `position` property is only available for images that are associated with a product. If you reference this property
    on an image from another source, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-presentation) 

presentation**presentation** [image\_presentation](/docs/api/liquid/objects/image_presentation)

:   The presentation settings for the image.

[Anchor to](/docs/api/liquid/objects/image#image-preview_image) 

preview\_image**preview\_image** [image](/docs/api/liquid/objects/image)

:   A preview image for the image.

    The `preview_image` property is only available for images accessed through the following sources:

    * [`product.featured_media`](/docs/api/liquid/objects/product#product-featured_media)
    * [`product.media`](/docs/api/liquid/objects/product#product-media)
    * [`file_reference` type metafields](/apps/metafields/types#supported-types)

    If you reference this property on an image from another source, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-product_id) 

product\_id**product\_id** [number](/docs/api/liquid/basics#number)

:   The ID of the product that the image is associated with.

    The `product_id` property is only available for images associated with a product. If you reference this property on
    an image from another source, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-src) 

src**src** [string](/docs/api/liquid/basics#string)

:   The relative URL of the image.

[Anchor to](/docs/api/liquid/objects/image#image-variants) 

variants**variants** array of [variant](/docs/api/liquid/objects/variant)

:   The product variants that the image is associated with.

    The `variants` property is only available for images accessed through the following sources:

    * [`product.featured_image`](/docs/api/liquid/objects#product-featured_image)
    * [`product.images`](/docs/api/liquid/objects/product#product-images)

    If you reference this property on an image from another source, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/image#image-width) 

width**width** [number](/docs/api/liquid/basics#number)

:   The width of the image in pixels.

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

{

"alt": "Charcoal",

"aspect\_ratio": 1.50016818028927,

"attached\_to\_variant?": false,

"height": 2973,

"id": 29355706875969,

"position": 1,

"product\_id": 6790277595201,

"src": {},

"variants": [],

"width": 4460

}

##### Example

```liquid
{
  "alt": "Charcoal",
  "aspect_ratio": 1.50016818028927,
  "attached_to_variant?": false,
  "height": 2973,
  "id": 29355706875969,
  "position": 1,
  "product_id": 6790277595201,
  "src": {},
  "variants": [],
  "width": 4460
}
```

[Anchor to Referencing the `image` object directly](/docs/api/liquid/objects/image#image-referencing-the-image-object-directly)

### Referencing the `image` object directly

When an `image` object is referenced directly, the image's relative URL path is returned.

9

1

{{ product.featured\_image }}

##### Code

```liquid
{{ product.featured_image }}
```

##### Data

```liquid
{
  "product": {
    "featured_image": "products/mushrooms-on-a-table.jpg"
  }
}
```

## Output

9

1

products/mushrooms-on-a-table.jpg

##### Output

```liquid
products/mushrooms-on-a-table.jpg
```

Was this section helpful?

YesNo