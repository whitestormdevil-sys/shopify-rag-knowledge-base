---
source: https://shopify.dev/docs/api/liquid/objects/filter_value
---

A specific value of a filter.

To learn about supporting filters in your theme, refer to [Support storefront filtering](/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

## Properties

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-active) 

active**active** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the value is currently active. Returns `false` if not.

    Can only return `true` for filters of type `boolean` or `list`.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-count) 

count**count** [number](/docs/api/liquid/basics#number)

:   The number of results related to the filter value.

    Returns a value only for `boolean` and `list` type filters. Returns `nil` for `price_range` type filters.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-image) 

image**image** [image](/docs/api/liquid/objects/image)

:   The visual representation of the filter value when an image is used.

    Returns an [image](/docs/api/liquid/objects/image) drop for the filter value.
    Requires the [filter presentation](/docs/api/liquid/objects/filter#filter-presentation) to be `image` and for an image to be available. Otherwise, returns `nil`.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-label) 

label**label** [string](/docs/api/liquid/basics#string)

:   The customer-facing label for the filter value. For example, `Red` or `Rouge`.

    Returns a value only for `boolean` and `list` type filters. Returns `nil` for `price_range` type filters.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-param_name) 

param\_name**param\_name** [string](/docs/api/liquid/basics#string)

:   The URL parameter for the parent filter of the filter value.

    For example, `filter.v.option.color`.

    Filters of type `price_range` include an extra component depending on whether the filter value is for the filter's
    `min_value` or `max_value`. The following table outlines the URL parameter for each:

    | Value type | URL parameter |
    | --- | --- |
    | `min_value` | `filter.v.price.gte` |
    | `max_value` | `filter.v.price.lte` |

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-swatch) 

swatch**swatch** [swatch](/docs/api/liquid/objects/swatch)

:   The visual representation of the filter value when a swatch is used.

    Returns a [swatch](/docs/api/liquid/objects/swatch) drop for the filter value.
    Requires the [filter presentation](/docs/api/liquid/objects/filter#filter-presentation) to be `swatch` and saved color or image content for the swatch. Otherwise, returns `nil`.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-url_to_add) 

url\_to\_add**url\_to\_add** [string](/docs/api/liquid/basics#string)

:   The current page URL with the filter value parameter added.

    Note

    Any [pagination](/docs/api/liquid/tags/paginate) URL parameters are removed.

    **Note:**

    Any [pagination](/docs/api/liquid/tags/paginate) URL parameters are removed.

    **Note:** Any <a href="/docs/api/liquid/tags/paginate">pagination</a> URL parameters are removed.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-url_to_remove) 

url\_to\_remove**url\_to\_remove** [string](/docs/api/liquid/basics#string)

:   The current page URL with the filter value parameter removed.

    Note

    Any [pagination](/docs/api/liquid/tags/paginate) URL parameters are also removed.

    **Note:**

    Any [pagination](/docs/api/liquid/tags/paginate) URL parameters are also removed.

    **Note:** Any <a href="/docs/api/liquid/tags/paginate">pagination</a> URL parameters are also removed.

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-value) 

value**value** [string](/docs/api/liquid/basics#string)

:   The value for the URL parameter. The `value` is paired with the [`param_name`](#filter_value-param_name) property.

    For example, `High` will be used in the URL as `filter.v.option.strength=High`.

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/filter_value#filter_value-display) 

display**display** [filter\_value\_display](/docs/api/liquid/objects/filter_value_display) Deprecated

:   The visual representation of the filter value.

    Returns a visual representation for the filter value.
    If no visual representation is available, then `nil` is returned.

    Deprecated

    Deprecated in favor of the [swatch](#swatch) attribute.

    **Deprecated:**

    Deprecated in favor of the [swatch](#swatch) attribute.

### Returned by

* [filter](/docs/api/liquid/objects/filter)
* [filter.false\_value](/docs/api/liquid/objects/filter#filter-false_value)
* [filter.true\_value](/docs/api/liquid/objects/filter#filter-true_value)
* [filter.max\_value](/docs/api/liquid/objects/filter#filter-max_value)
* [filter.min\_value](/docs/api/liquid/objects/filter#filter-min_value)

Was this section helpful?

YesNo