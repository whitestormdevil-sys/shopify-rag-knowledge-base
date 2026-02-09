---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Image
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Represents an image resource.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Image#fields)Fields

* altText (String)
* height (Int)
* id (ID)
* thumbhash (String)
* url (URL!)
* width (Int)

[Anchor to altText](/docs/api/storefront/latest/objects/Image#field-Image.fields.altText)altText •[String](/docs/api/storefront/latest/scalars/String)
:   A word or phrase to share the nature or contents of an image.

[Anchor to height](/docs/api/storefront/latest/objects/Image#field-Image.fields.height)height •[Int](/docs/api/storefront/latest/scalars/Int)
:   The original height of the image in pixels. Returns `null` if the image isn't hosted by Shopify.

[Anchor to id](/docs/api/storefront/latest/objects/Image#field-Image.fields.id)id •[ID](/docs/api/storefront/latest/scalars/ID)
:   A unique ID for the image.

[Anchor to thumbhash](/docs/api/storefront/latest/objects/Image#field-Image.fields.thumbhash)thumbhash •[String](/docs/api/storefront/latest/scalars/String)
:   The ThumbHash of the image.

    Useful to display placeholder images while the original image is loading.

    See <https://evanw.github.io/thumbhash/> for details on how to use it.

[Anchor to url](/docs/api/storefront/latest/objects/Image#field-Image.fields.url)url •[URL!](/docs/api/storefront/latest/scalars/URL) non-null
:   The location of the image as a URL.

    If no transform options are specified, then the original image will be preserved including any pre-applied transforms.

    All transformation options are considered "best-effort". Any transformation that the original image type doesn't support will be ignored.

    If you need multiple variations of the same image, then you can use [GraphQL aliases](https://graphql.org/learn/queries/#aliases).

    Show arguments

    ### Arguments

    [Anchor to transform](/docs/api/storefront/latest/objects/Image#field-Image.fields.url.arguments.transform)transform •[ImageTransformInput](/docs/api/storefront/latest/input-objects/ImageTransformInput)
    :   A set of options to transform the original image.

        Show input fields

    ---

[Anchor to width](/docs/api/storefront/latest/objects/Image#field-Image.fields.width)width •[Int](/docs/api/storefront/latest/scalars/Int)
:   The original width of the image in pixels. Returns `null` if the image isn't hosted by Shopify.

### Deprecated fields

* originalSrc (URL!): deprecated
* src (URL!): deprecated
* transformedSrc (URL!): deprecated

[Anchor to originalSrc](/docs/api/storefront/latest/objects/Image#field-Image.fields.originalSrc)originalSrc •[URL!](/docs/api/storefront/latest/scalars/URL) non-nullDeprecated

[Anchor to src](/docs/api/storefront/latest/objects/Image#field-Image.fields.src)src •[URL!](/docs/api/storefront/latest/scalars/URL) non-nullDeprecated

[Anchor to transformedSrc](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc)transformedSrc •[URL!](/docs/api/storefront/latest/scalars/URL) non-nullDeprecated
:   Show arguments

    ### Arguments

    [Anchor to maxWidth](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc.arguments.maxWidth)maxWidth •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Image width in pixels between 1 and 5760.

    [Anchor to maxHeight](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc.arguments.maxHeight)maxHeight •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Image height in pixels between 1 and 5760.

    [Anchor to crop](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc.arguments.crop)crop •[CropRegion](/docs/api/storefront/latest/enums/CropRegion)
    :   Crops the image according to the specified region.

        Show enum values

    [Anchor to scale](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc.arguments.scale)scale •[Int](/docs/api/storefront/latest/scalars/Int) Default:1
    :   Image size multiplier for high-resolution retina displays. Must be between 1 and 3.

    [Anchor to preferredContentType](/docs/api/storefront/latest/objects/Image#field-Image.fields.transformedSrc.arguments.preferredContentType)preferredContentType •[ImageContentType](/docs/api/storefront/latest/enums/ImageContentType)
    :   Best effort conversion of image into content type (SVG -> PNG, Anything -> JPG, Anything -> WEBP are supported).

        Show enum values

    ---

---

Was this section helpful?

YesNo