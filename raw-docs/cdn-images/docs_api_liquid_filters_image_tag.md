---
source: https://shopify.dev/docs/api/liquid/filters/image_tag
---

9

1

string | image\_tag

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<img>` tag for a given [`image_url`](/docs/api/liquid/filters/image_url).

By default, `width` and `height` attributes are added to the `<img>` tag based on the dimensions and aspect ratio from
the image URL. However, you can override these attributes with the [width](/docs/api/liquid/filters/image_tag#image_tag-width) and [height](/docs/api/liquid/filters/image_tag#image_tag-height)
parameters. If only one parameter is provided, then only that attribute is added.

9

1

{{ product | image\_url: width: 200 | image\_tag }}

##### Code

```liquid
{{ product | image_url: width: 200 | image_tag }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">
```

[Anchor to Lazy loading](/docs/api/liquid/filters/image_tag#image_tag-lazy-loading)

### Lazy loading

If you don't apply the `preload` attribute to `image_tag`, then `loading` is automatically set to `lazy` for images in sections further down the page.
You shouldn't lazy load images above the fold. If the default value doesn't work for your theme, then consider writing your own logic using the `section.index` and `section.location` properties. For more information, refer to the [`section` object](/docs/api/liquid/objects/section).

[Anchor to `image\_tag` and focal points](/docs/api/liquid/filters/image_tag#image_tag-image_tag-and-focal-points)

### `image_tag` and focal points

This filter automatically applies a focal point to the image using the `object-position` CSS style, if focal point coordinates are available. You can also access an image's focal point coordinates directly through the [`focal_point`](/docs/api/liquid/objects/focal_point) object. [Learn how to set a focal point](https://help.shopify.com/manual/online-store/images/theme-images#set-a-focal-point-on-a-theme-image).

9

1

{{ images['potions-header.png'] | image\_url: width: 300 | image\_tag }}

##### Code

```liquid
{{ images['potions-header.png'] | image_url: width: 300 | image_tag }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300" alt="" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300 300w" width="300" height="173" style="object-position:1.9231% 9.7917%;">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300" alt="" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300 300w" width="300" height="173" style="object-position:1.9231% 9.7917%;">
```

[Anchor to width](/docs/api/liquid/filters/image_tag#image_tag-width)

### width

9

1

image\_url | image\_tag: width: number

Specify the `width` attribute of the `<img>` tag. You can set the parameter to `nil` to prevent the attribute from being added.

9

1

2

3

4

5

<!-- With a width -->

{{ product | image\_url: width: 400 | image\_tag: width: 300 }}

<!-- With the width set to nil -->

{{ product | image\_url: width: 400 | image\_tag: width: nil }}

##### Code

```liquid
<!-- With a width -->
{{ product | image_url: width: 400 | image_tag: width: 300 }}

<!-- With the width set to nil -->
{{ product | image_url: width: 400 | image_tag: width: nil }}
```

## Output

9

1

2

3

4

5

<!-- With a width -->

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" width="300">

<!-- With the width set to nil -->

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">

##### Output

```liquid
<!-- With a width -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" width="300">

<!-- With the width set to nil -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">
```

[Anchor to height](/docs/api/liquid/filters/image_tag#image_tag-height)

### height

9

1

image\_url | image\_tag: height: number

Specify the `height` attribute of the `<img>` tag. You can set the parameter to `nil` to prevent the attribute from being added.

9

1

2

3

4

5

<!-- With a height -->

{{ product | image\_url: width: 400 | image\_tag: height: 300 }}

<!-- With the height set to nil -->

{{ product | image\_url: width: 400 | image\_tag: height: nil }}

##### Code

```liquid
<!-- With a height -->
{{ product | image_url: width: 400 | image_tag: height: 300 }}

<!-- With the height set to nil -->
{{ product | image_url: width: 400 | image_tag: height: nil }}
```

## Output

9

1

2

3

4

5

<!-- With a height -->

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" height="300">

<!-- With the height set to nil -->

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">

##### Output

```liquid
<!-- With a height -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w" height="300">

<!-- With the height set to nil -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=352 352w">
```

[Anchor to sizes](/docs/api/liquid/filters/image_tag#image_tag-sizes)

### sizes

9

1

image\_url | image\_tag: sizes: string

Specify source sizes with the [HTML `sizes` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).

9

1

{{ product | image\_url: width: 200 | image\_tag: sizes: '(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)' }}

##### Code

```liquid
{{ product | image_url: width: 200 | image_tag: sizes: '(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)' }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" sizes="(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" sizes="(min-width:1600px) 960px, (min-width: 750px) calc((100vw - 11.5rem) / 2), calc(100vw - 4rem)">
```

[Anchor to widths](/docs/api/liquid/filters/image_tag#image_tag-widths)

### widths

9

1

image\_url | image\_tag: widths: string

By default, Shopify generates a `srcset` with a smart set of default widths up to the maximum defined in the image URL. However, you can create your own set of widths.

9

1

{{ product | image\_url: width: 600 | image\_tag: widths: '200, 300, 400' }}

##### Code

```liquid
{{ product | image_url: width: 600 | image_tag: widths: '200, 300, 400' }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=600" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400 400w" width="600" height="400">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=600" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=300 300w, //polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=400 400w" width="600" height="400">
```

[Anchor to srcset](/docs/api/liquid/filters/image_tag#image_tag-srcset)

### srcset

9

1

image\_url | image\_tag: srcset: string

By default, Shopify generates a `srcset`. However, you can create your own `srcset`.
The `srcset` parameter takes precedence over the [`width` parameter](/docs/api/liquid/filters/image_tag#image_tag-width).
You shouldn't to use the `srcset` parameter unless you want to remove the attribute by setting the parameter to `nil`.

9

1

{{ product | image\_url: width: 200 | image\_tag: srcset: nil }}

##### Code

```liquid
{{ product | image_url: width: 200 | image_tag: srcset: nil }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" width="200" height="133">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" width="200" height="133">
```

[Anchor to preload](/docs/api/liquid/filters/image_tag#image_tag-preload)

### preload

9

1

image\_url | image\_tag: preload: boolean

Specify whether the image should be preloaded.

When `preload` is set to `true`, a resource hint is sent as a [Link HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link)
with a `rel` value of [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload).
The Link header also includes `imagesrcset` and `imagesizes` that match the `srcset` and `sizes` attribute of the tag,
where present:

9

1

2

Link: <IMAGE\_URL>; rel=preload; as=image

Link: <IMAGE\_URL>; rel=preload; as=image; imagesrcset=ADDITIONAL\_IMAGE\_URL 352w; imagesizes=40vw

```liquid
Link: ; rel=preload; as=image
Link: ; rel=preload; as=image; imagesrcset=ADDITIONAL_IMAGE_URL 352w; imagesizes=40vw
```

This option doesn't affect the HTML img tag directly.

You should use the preload parameter sparingly. For example, consider preloading only above-the-fold images.
To learn more about resource hints in Shopify themes, refer to [Performance best practices for Shopify themes](/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others).

[Anchor to alt](/docs/api/liquid/filters/image_tag#image_tag-alt)

### alt

9

1

image\_url | image\_tag: alt: string

By default, the `alt` attribute of the `<img>` tag is set to the [media alt text](https://help.shopify.com/manual/products/product-media/add-alt-text), or the resource title for article, collection, line item, product, and variant images. However, you can override this default, or set the value if there's no default.

9

1

{{ product | image\_url: width: 200 | image\_tag: alt: "My image's alt text" }}

##### Code

```liquid
{{ product | image_url: width: 200 | image_tag: alt: "My image's alt text" }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="My image&#39;s alt text" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="My image&#39;s alt text" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133">
```

[Anchor to HTML attributes](/docs/api/liquid/filters/image_tag#image_tag-html-attributes)

### HTML attributes

9

1

image\_url | image\_tag: attribute: string

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes) by adding a parameter that matches the attribute name, and the desired value.

9

1

{{ product | image\_url: width: 200 | image\_tag: class: 'custom-class', loading: 'lazy' }}

##### Code

```liquid
{{ product | image_url: width: 200 | image_tag: class: 'custom-class', loading: 'lazy' }}
```

## Output

9

1

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" loading="lazy" class="custom-class">

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200" alt="Health potion" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&amp;width=200 200w" width="200" height="133" loading="lazy" class="custom-class">
```

Was this page helpful?

YesNo