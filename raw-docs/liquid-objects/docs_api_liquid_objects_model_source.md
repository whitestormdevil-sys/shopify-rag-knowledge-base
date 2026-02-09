---
source: https://shopify.dev/docs/api/liquid/objects/model_source
---

A model source file.

## Properties

[Anchor to](/docs/api/liquid/objects/model_source#model_source-format) 

format**format** [string](/docs/api/liquid/basics#string)

:   The format of the model source file.

[Anchor to](/docs/api/liquid/objects/model_source#model_source-mime_type) 

mime\_type**mime\_type** [string](/docs/api/liquid/basics#string)

:   The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the model source file.

[Anchor to](/docs/api/liquid/objects/model_source#model_source-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) of the model source file.

9

1

2

3

4

5

{

"format": "glb",

"mime\_type": "model/gltf-binary",

"url": "//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0"

}

##### Example

```liquid
{
  "format": "glb",
  "mime_type": "model/gltf-binary",
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0"
}
```

Was this section helpful?

YesNo