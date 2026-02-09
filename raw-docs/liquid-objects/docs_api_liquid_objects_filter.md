---
source: https://shopify.dev/docs/api/liquid/objects/filter
---

A [storefront filter](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).

To learn about supporting filters in your theme, refer to [Support storefront filtering](/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

## Properties

[Anchor to](/docs/api/liquid/objects/filter#filter-active_values) 

active\_values**active\_values** array of [filter\_value](/docs/api/liquid/objects/filter_value)

:   The values of the filter that are currently active.

    The array can have values only for `boolean` and `list` type filters.

[Anchor to](/docs/api/liquid/objects/filter#filter-false_value) 

false\_value**false\_value** [filter\_value](/docs/api/liquid/objects/filter_value)

:   The `false` filter value.

    Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `false` filter value. Otherwise, it returns `nil`.

[Anchor to](/docs/api/liquid/objects/filter#filter-inactive_values) 

inactive\_values**inactive\_values** array of [filter\_value](/docs/api/liquid/objects/filter_value)

:   The values of the filter that are currently inactive.

    The array can have values only for `boolean` and `list` type filters.

[Anchor to](/docs/api/liquid/objects/filter#filter-label) 

label**label** [string](/docs/api/liquid/basics#string)

:   The customer-facing label for the filter.

[Anchor to](/docs/api/liquid/objects/filter#filter-max_value) 

max\_value**max\_value** [filter\_value](/docs/api/liquid/objects/filter_value)

:   The highest filter value.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

[Anchor to](/docs/api/liquid/objects/filter#filter-min_value) 

min\_value**min\_value** [filter\_value](/docs/api/liquid/objects/filter_value)

:   The lowest filter value.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

[Anchor to](/docs/api/liquid/objects/filter#filter-operator) 

operator**operator** [string](/docs/api/liquid/basics#string) from a set of values

:   The logical operator used by the filter.
    Returns a value only for `boolean` and `list` type filters. Returns `nil` for other types.

    Example:
    For a filter named `color` with values `red` and `blue`:

    * If the operator is `AND`, it will filter items that are both red and blue.
    * If the operator is `OR`, it will filter items that are either red or blue or both.

    Filters that support the `AND` operator:

    * Product tags
    * Metafields of type `list.single_line_text_field` and `list.metaobject_reference`

    | Possible values | Description |
    | --- | --- |
    | AND | Includes products that match all buyer selections. |
    | OR | Includes products that match at least one buyer selection. |

[Anchor to](/docs/api/liquid/objects/filter#filter-param_name) 

param\_name**param\_name** [string](/docs/api/liquid/basics#string)

:   The URL parameter for the filter. For example, `filter.v.option.color`.

[Anchor to](/docs/api/liquid/objects/filter#filter-presentation) 

presentation**presentation** [string](/docs/api/liquid/basics#string) from a set of values

:   Describes how to present the filter values.

    Returns a value only for `list` type filters. Returns `nil` for other types.

    | Possible values |
    | --- |
    | image |
    | swatch |
    | text |

[Anchor to](/docs/api/liquid/objects/filter#filter-range_max) 

range\_max**range\_max** [number](/docs/api/liquid/basics#number)

:   The highest product price within the collection or search results.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

[Anchor to](/docs/api/liquid/objects/filter#filter-true_value) 

true\_value**true\_value** [filter\_value](/docs/api/liquid/objects/filter_value)

:   The `true` filter value.

    Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `true` filter value. Otherwise, it returns `nil`.

[Anchor to](/docs/api/liquid/objects/filter#filter-type) 

type**type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of the filter.

    | Possible values |
    | --- |
    | boolean |
    | list |
    | price\_range |

[Anchor to](/docs/api/liquid/objects/filter#filter-url_to_remove) 

url\_to\_remove**url\_to\_remove** [string](/docs/api/liquid/basics#string)

:   The current page URL with the URL parameter related to the filter removed.

[Anchor to](/docs/api/liquid/objects/filter#filter-values) 

values**values** array of [filter\_value](/docs/api/liquid/objects/filter_value)

:   The values of the filter.

    The array can have values only for `boolean` and `list` type filters.

### Returned by

* [collection.filters](/docs/api/liquid/objects/collection#collection-filters)
* [search.filters](/docs/api/liquid/objects/search#search-filters)

Was this section helpful?

YesNo