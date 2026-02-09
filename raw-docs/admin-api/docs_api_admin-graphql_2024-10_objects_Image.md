---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/Image
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Represents an image resource.

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/Image#fields)Fields

* altText (String)
* height (Int)
* id (ID)
* metafield (Metafield)
* metafields (MetafieldConnection!)
* thumbhash (String)
* translations ([Translation!]!)
* url (URL!)
* width (Int)

[Anchor to altText](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.altText)altText •[String](/docs/api/admin-graphql/latest/scalars/String)
:   A word or phrase to share the nature or contents of an image.

[Anchor to height](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.height)height •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The original height of the image in pixels. Returns `null` if the image isn't hosted by Shopify.

[Anchor to id](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.id)id •[ID](/docs/api/admin-graphql/latest/scalars/ID)
:   A unique ID for the image.

[Anchor to metafield](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafield)metafield •[Metafield](/docs/api/admin-graphql/latest/objects/Metafield)
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data),
    including its `namespace` and `key`, that's associated with a Shopify resource
    for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafield.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafield.arguments.key)key •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   The key for the metafield.

    ---

[Anchor to metafields](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields)metafields •[MetafieldConnection!](/docs/api/admin-graphql/latest/connections/MetafieldConnection) non-null
:   A list of [custom fields](https://shopify.dev/docs/apps/build/custom-data)
    that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.namespace)namespace •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The metafield namespace to filter by. If omitted, all metafields are returned.

    [Anchor to keys](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.keys)keys •[[String!]](/docs/api/admin-graphql/latest/scalars/String)
    :   List of keys of metafields in the format `namespace.key`, will be returned in the same format.

    [Anchor to first](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.metafields.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to thumbhash](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.thumbhash)thumbhash •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The ThumbHash of the image.

    Useful to display placeholder images while the original image is loading.

[Anchor to translations](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.translations)translations •[[Translation!]!](/docs/api/admin-graphql/latest/objects/Translation) non-null
:   The published translations associated with the resource.

    Show fields

    ### Arguments

    [Anchor to locale](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.translations.arguments.locale)locale •[String!](/docs/api/admin-graphql/latest/scalars/String) required
    :   Filters translations locale.

    [Anchor to marketId](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.translations.arguments.marketId)marketId •[ID](/docs/api/admin-graphql/latest/scalars/ID)
    :   Filters translations by market ID. Use this argument to retrieve content specific to a market.

    ---

[Anchor to url](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.url)url •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-null
:   The location of the image as a URL.

    If no transform options are specified, then the original image will be preserved including any pre-applied transforms.

    All transformation options are considered "best-effort". Any transformation that the original image type doesn't support will be ignored.

    If you need multiple variations of the same image, then you can use [GraphQL aliases](https://graphql.org/learn/queries/#aliases).

    Show arguments

    ### Arguments

    [Anchor to transform](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.url.arguments.transform)transform •[ImageTransformInput](/docs/api/admin-graphql/latest/input-objects/ImageTransformInput)
    :   A set of options to transform the original image.

        Show input fields

    ---

[Anchor to width](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.width)width •[Int](/docs/api/admin-graphql/latest/scalars/Int)
:   The original width of the image in pixels. Returns `null` if the image isn't hosted by Shopify.

### Deprecated fields

* originalSrc (URL!): deprecated
* src (URL!): deprecated
* transformedSrc (URL!): deprecated

[Anchor to originalSrc](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.originalSrc)originalSrc •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-nullDeprecated

[Anchor to src](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.src)src •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-nullDeprecated

[Anchor to transformedSrc](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc)transformedSrc •[URL!](/docs/api/admin-graphql/latest/scalars/URL) non-nullDeprecated
:   Show arguments

    ### Arguments

    [Anchor to maxWidth](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc.arguments.maxWidth)maxWidth •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   Image width in pixels between 1 and 5760.

    [Anchor to maxHeight](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc.arguments.maxHeight)maxHeight •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   Image height in pixels between 1 and 5760.

    [Anchor to crop](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc.arguments.crop)crop •[CropRegion](/docs/api/admin-graphql/latest/enums/CropRegion)
    :   Crops the image according to the specified region.

        Show enum values

    [Anchor to scale](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc.arguments.scale)scale •[Int](/docs/api/admin-graphql/latest/scalars/Int) Default:1
    :   Image size multiplier for high-resolution retina displays. Must be between 1 and 3.

    [Anchor to preferredContentType](/docs/api/admin-graphql/latest/objects/Image#field-Image.fields.transformedSrc.arguments.preferredContentType)preferredContentType •[ImageContentType](/docs/api/admin-graphql/latest/enums/ImageContentType)
    :   Best effort conversion of image into content type (SVG -> PNG, Anything -> JPG, Anything -> WEBP are supported).

        Show enum values

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/Image#interfaces)Interfaces

* HasMetafields
* HasPublishedTranslations

[Anchor to HasMetafields](/docs/api/admin-graphql/latest/objects/Image#interface-HasMetafields)[HasMetafields](/docs/api/admin-graphql/latest/interfaces/HasMetafields) •interface

[Anchor to HasPublishedTranslations](/docs/api/admin-graphql/latest/objects/Image#interface-HasPublishedTranslations)[HasPublishedTranslations](/docs/api/admin-graphql/latest/interfaces/HasPublishedTranslations) •interface

---

Was this section helpful?

YesNo