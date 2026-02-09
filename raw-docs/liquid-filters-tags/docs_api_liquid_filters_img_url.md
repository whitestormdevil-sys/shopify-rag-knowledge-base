---
source: https://shopify.dev/docs/api/liquid/filters/img_url
---

9

1

variable | img\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `img_url` filter on the following objects:

* [`article`](/docs/api/liquid/objects/article)
* [`collection`](/docs/api/liquid/objects/collection)
* [`image`](/docs/api/liquid/objects/image)
* [`line_item`](/docs/api/liquid/objects/line_item)
* [`product`](/docs/api/liquid/objects/product)
* [`variant`](/docs/api/liquid/objects/variant)

Deprecated

The `img_url` filter has been replaced by [`image_url`](/docs/api/liquid/filters/image_url).

**Deprecated:**

The `img_url` filter has been replaced by [`image_url`](/docs/api/liquid/filters/image_url).

9

1

{{ product | img\_url }}

##### Code

```liquid
{{ product | img_url }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_small.jpg?v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

[Anchor to size](/docs/api/liquid/filters/img_url#img_url-size)

### size

9

1

variable | img\_url: string

The size parameter allows you to specify the dimensions of the image up to a maximum of 5760 x 5760 px. You can specify only the width, only the height, or both, and you can also use the following named sizes:

| Name | Dimensions |
| --- | --- |
| `pico` | `16x16 px` |
| `icon` | `32x32 px` |
| `thumb` | `50x50 px` |
| `small` | `100x100 px` |
| `compact` | `160x160 px` |
| `medium` | `240x240 px` |
| `large` | `480x480 px` |
| `grande` | `600x600 px` |
| `original` `master` | `1024x1024 px` |

9

1

2

3

4

5

6

7

{{ product | img\_url: '480x' }}

{{ product | img\_url: 'x480' }}

{{ product | img\_url: '480x480' }}

{{ product | img\_url: 'large' }}

##### Code

```liquid
{{ product | img_url: '480x' }}

{{ product | img_url: 'x480' }}

{{ product | img_url: '480x480' }}

{{ product | img_url: 'large' }}
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

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_480x.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_480x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_large.jpg?v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_large.jpg?v=1683744744
```

[Anchor to crop](/docs/api/liquid/filters/img_url#img_url-crop)

### crop

9

1

variable | img\_url: crop: string

The `crop` parameter allows you to specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

* `top`
* `center`
* `bottom`
* `left`
* `right`

The default value is `center`.

9

1

{{ product | img\_url: crop: 'bottom' }}

##### Code

```liquid
{{ product | img_url: crop: 'bottom' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_small.jpg?v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

[Anchor to format](/docs/api/liquid/filters/img_url#img_url-format)

### format

9

1

variable | img\_url: format: string

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so this filter does
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

{{ product | img\_url: format: 'pjpg' }}

##### Code

```liquid
{{ product | img_url: format: 'pjpg' }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_small.jpg?v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

[Anchor to scale](/docs/api/liquid/filters/img_url#img_url-scale)

### scale

9

1

variable | img\_url: scale: number

Specify the pixel density of the image. The valid densities are 2 and 3.

9

1

{{ product | img\_url: scale: 2 }}

##### Code

```liquid
{{ product | img_url: scale: 2 }}
```

## Output

9

1

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new\_small.jpg?v=1683744744

##### Output

```liquid
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

Was this page helpful?

YesNo