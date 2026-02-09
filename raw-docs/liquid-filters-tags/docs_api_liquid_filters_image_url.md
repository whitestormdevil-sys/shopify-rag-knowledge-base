---
source: https://shopify.dev/docs/api/liquid/filters/image_url
---

9

1

variable | image\_url: width: number, height: number

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `image_url` filter on the following objects, as well as their `src` property:

* [`article`](/docs/api/liquid/objects/article)
* [`collection`](/docs/api/liquid/objects/collection)
* [`image`](/docs/api/liquid/objects/image)
* [`line_item`](/docs/api/liquid/objects/line_item)
* [`product`](/docs/api/liquid/objects/product)
* [`variant`](/docs/api/liquid/objects/variant)
* [`country`](/docs/api/liquid/objects/country)

---

Caution

You need to specify either a [`width`](/docs/api/liquid/filters/image_url#image_url-width) or
[`height`](/docs/api/liquid/filters/image_url#image_url-height) parameter. If neither are specified, then an error is returned.

**Caution:**

You need to specify either a [`width`](/docs/api/liquid/filters/image_url#image_url-width) or
[`height`](/docs/api/liquid/filters/image_url#image_url-height) parameter. If neither are specified, then an error is returned.

**Caution:** You need to specify either a <a href="/docs/api/liquid/filters/image\_url#image\_url-width"><code>width</code></a> or
<a href="/docs/api/liquid/filters/image\_url#image\_url-height"><code>height</code></a> parameter. If neither are specified, then an error is returned.

---

---

Note

Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions.

**Note:**

Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions.

**Note:** Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions.

---

9

1

{{ product | image\_url: width: 450 }}

##### Code

```liquid
{{ product | image_url: width: 450 }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

[Anchor to width](/docs/api/liquid/filters/image_url#image_url-width)

### width

9

1

variable | image\_url: width: number

Specify the width of the image up to a maximum of `5760px`. If only the width is specified, then the height is automatically calculated based on the image's dimensions.

9

1

{{ product | image\_url: width: 450 }}

##### Code

```liquid
{{ product | image_url: width: 450 }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

[Anchor to height](/docs/api/liquid/filters/image_url#image_url-height)

### height

9

1

variable | image\_url: height: number

Specify the height of the image up to a maximum of `5760px`. If only the height is specified, then the width is automatically calculated based on the image's dimensions.

9

1

{{ product | image\_url: height: 450 }}

##### Code

```liquid
{{ product | image_url: height: 450 }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=450&v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=450&v=1683744744
```

[Anchor to crop](/docs/api/liquid/filters/image_url#image_url-crop)

### crop

9

1

variable | image\_url: crop: string

Specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

* `top`
* `center`
* `bottom`
* `left`
* `right`
* `region`

The default value is `center`.

When using the `region` crop mode, the starting point for the crop is defined by `crop_left` and `crop_top` and extends to the `crop_width` and `crop_height`.
Optionally, to resize the region extracted by the crop, use the `width` and `height` parameters.

---

Note

Country flags are SVG images and can only be cropped if a value for `format`
is also provided.

**Note:**

Country flags are SVG images and can only be cropped if a value for `format`
is also provided.

**Note:** Country flags are SVG images and can only be cropped if a value for <code>format</code>
is also provided.

---

9

1

2

3

4

5

{{ product | image\_url: width: 400, height: 400, crop: 'bottom' }}

{{ product | image\_url: crop: 'region', crop\_left: 32, crop\_top: 32, crop\_width: 512, crop\_height: 512 }}

{{ product | image\_url: crop: 'region', width: 100, height: 100, crop\_left: 32, crop\_top: 32, crop\_width: 512, crop\_height: 512 }}

##### Code

```liquid
{{ product | image_url: width: 400, height: 400, crop: 'bottom' }}

{{ product | image_url: crop: 'region', crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}

{{ product | image_url: crop: 'region', width: 100, height: 100, crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}
```

## Output

9

1

2

3

4

5

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=bottom&height=400&v=1683744744&width=400

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop\_height=512&crop\_left=32&crop\_top=32&crop\_width=512&v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop\_height=512&crop\_left=32&crop\_top=32&crop\_width=512&height=100&v=1683744744&width=100

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=bottom&height=400&v=1683744744&width=400

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&height=100&v=1683744744&width=100
```

[Anchor to format](/docs/api/liquid/filters/image_url#image_url-format)

### format

9

1

variable | image\_url: format: string

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so Shopify can do
only the following conversions:

* `png` to `jpg`
* `png` to `pjpg`
* `jpg` to `pjpg`

---

Note

Shopify automatically detects which image formats are supported by the client (e.g. `WebP`, `AVIF`, etc.) and
selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account
the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection.
To learn more, visit <https://cdn.shopify.com/>.

**Note:**

Shopify automatically detects which image formats are supported by the client (e.g. `WebP`, `AVIF`, etc.) and
selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account
the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection.
To learn more, visit <https://cdn.shopify.com/>.

**Note:** Shopify automatically detects which image formats are supported by the client (e.g. <code><span class="PreventFireFoxApplyingGapToWBR">Web<wbr/>P</span></code>, <code><span class="PreventFireFoxApplyingGapToWBR">A<wbr/>V<wbr/>I<wbr/>F</span></code>, etc.) and
selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account
the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection.
To learn more, visit <a href="https://cdn.shopify.com/">https://cdn.shopify.com/</a>.

---

9

1

{{ product | image\_url: width: 450, format: 'pjpg' }}

##### Code

```liquid
{{ product | image_url: width: 450, format: 'pjpg' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?format=pjpg&v=1683744744&width=450

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?format=pjpg&v=1683744744&width=450
```

[Anchor to pad\_color](/docs/api/liquid/filters/image_url#image_url-pad_color)

### pad\_color

9

1

variable | image\_url: pad\_color: string

Specify a color to pad the image if the specified dimensions result in an aspect ratio that differs from the original. The color must be in hexadecimal format (`hex3` or `hex6`).

9

1

{{ product | image\_url: width: 400, height: 400, pad\_color: '000' }}

##### Code

```liquid
{{ product | image_url: width: 400, height: 400, pad_color: '000' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=400&pad\_color=000&v=1683744744&width=400

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=400&pad_color=000&v=1683744744&width=400
```

Was this page helpful?

YesNo