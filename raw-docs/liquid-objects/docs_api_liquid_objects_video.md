---
source: https://shopify.dev/docs/api/liquid/objects/video
---

Information about a video uploaded as [product media](/docs/api/liquid/objects/product-media) or a [`file_reference` metafield](/apps/metafields/types).

---

Tip

Use the [`video_tag` filter](/docs/api/liquid/filters/video_tag) to output the video in an HTML `<video>` tag.

**Tip:**

Use the [`video_tag` filter](/docs/api/liquid/filters/video_tag) to output the video in an HTML `<video>` tag.

**Tip:** Use the <a href="/docs/api/liquid/filters/video\_tag"><code><span class="PreventFireFoxApplyingGapToWBR">video<wbr/>\_tag</span></code> filter</a> to output the video in an HTML <code>&lt;video&gt;</code> tag.

---

## Properties

[Anchor to](/docs/api/liquid/objects/video#video-alt) 

alt**alt** [string](/docs/api/liquid/basics#string)

:   The alt text of the video.

[Anchor to](/docs/api/liquid/objects/video#video-aspect_ratio) 

aspect\_ratio**aspect\_ratio** [number](/docs/api/liquid/basics#number)

:   The aspect ratio of the video as a decimal.

[Anchor to](/docs/api/liquid/objects/video#video-duration) 

duration**duration** [number](/docs/api/liquid/basics#number)

:   The duration of the video in milliseconds.

[Anchor to](/docs/api/liquid/objects/video#video-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the video.

[Anchor to](/docs/api/liquid/objects/video#video-media_type) 

media\_type**media\_type** [string](/docs/api/liquid/basics#string)

:   The media type of the model. Always returns `video`.

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

    {% assign videos = product.media | where: 'media\_type', 'video' %}

    {% for video in videos %}

    {{- video | video\_tag }}

    {% endfor %}

    ##### Code

    ```liquid
    {% assign videos = product.media | where: 'media_type', 'video' %}

    {% for video in videos %}
      {{- video | video_tag }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "media": [
          {
            "media_type": "external_video"
          },
          {
            "media_type": "video"
          }
        ]
      }
    }
    ```

    ## Output

    9

    1

    <video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000\_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000\_small.jpg?v=1655255324"></video>

    ##### Output

    ```liquid
    <video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
    ```

[Anchor to](/docs/api/liquid/objects/video#video-position) 

position**position** [number](/docs/api/liquid/basics#number)

:   The position of the video in the [`product.media`](/docs/api/liquid/objects/product#product-media) array.

[Anchor to](/docs/api/liquid/objects/video#video-preview_image) 

preview\_image**preview\_image** [image](/docs/api/liquid/objects/image)

:   A preview image for the video.

[Anchor to](/docs/api/liquid/objects/video#video-sources) 

sources**sources** array of [video\_source](/docs/api/liquid/objects/video_source)

:   The source files for the video.

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

{

"alt": "Potion beats",

"aspect\_ratio": 1.779,

"duration": 34801,

"id": 22070396551233,

"media\_type": "video",

"position": 2,

"preview\_image": {},

"sources": []

}

##### Example

```liquid
{
  "alt": "Potion beats",
  "aspect_ratio": 1.779,
  "duration": 34801,
  "id": 22070396551233,
  "media_type": "video",
  "position": 2,
  "preview_image": {},
  "sources": []
}
```

Was this section helpful?

YesNo