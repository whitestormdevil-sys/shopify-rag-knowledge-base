---
source: https://shopify.dev/docs/themes/navigation-search/search
---

Storefront search is based on [query parameters](#query-parameters) that determine what information is returned, and how it's returned, in the search results. In addition to the search query itself, there are parameters that allow you to customize the search in the following ways:

* Only search for certain resource types
* Choose whether unavailable products are returned, and where in the results
* Enable partial word matches

The query parameters can be used by including inputs in your [search form](#the-search-form), and they're reflected in the [search URL](#search-url-structure) when a search is performed.

Tip

To learn more about storefront search functionality and search query options, refer to the [Shopify Help Center](https://help.shopify.com/manual/online-store/storefront-search).

**Tip:**

To learn more about storefront search functionality and search query options, refer to the [Shopify Help Center](https://help.shopify.com/manual/online-store/storefront-search).

You can also add predictive search to your theme so that suggested results appear immediately as you type into the search field. To learn about predictive search, refer to [Add predictive search to your theme](/docs/storefronts/themes/navigation-search/search/predictive-search).

The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables users to customize product recommendation and search results, which can impact results from storefront search and the Ajax [Product Recommendations](/docs/api/ajax/reference/product-recommendations) API. To learn about how these results can be impacted, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations).

---

## [Anchor to Query parameters](/docs/storefronts/themes/navigation-search/search#query-parameters)Query parameters

Search queries accept the following parameters:

| Query parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `q` | String | Yes | The search query. |
| `type` | Comma-separated values | No | Specifies the type of results requested. The possible options are:   * `product` * `page` * `article`   Defaults to all types.  To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. |
| `page` | Integer | No | Specifies the current search results page. Defaults to `1`. |
| `options` | Hash | No | Specifies search options that you can customize with the `unavailable_products` and `prefix` settings. |
| `unavailable_products` | String | No | Specifies whether to display results for unavailable products or variants in filtered results. The following are the possible options:   * `show` - Show unavailable products or variants in the order that they're found. * `hide` - Exclude unavailable products or variants. * `last` - Show unavailable products or variants after all other matching results.   Defaults to `last`.  To change the default value, you can use [Search Settings](https://help.shopify.com/manual/online-store/search-and-discovery/settings) in the Search & Discovery app. |
| `prefix` | String | No | Specifies whether we want to perform a partial word match on the last search term.  For example, if "winter snow" is used as a search query, a search will find all applicable resources that contain both "winter" and any term that starts with "snow". This could be terms like "snow", "snowshoe", or "snowboard".  The possible options are:   * `last` - Perform a partial word match on the last search term. This is the default. * `none` - Don't perform a partial word match on the last search term. |
| `sort_by` | String | No | Specifies the sort order of the results. The possible options are:   * `relevance` - Sort results by relevance to the search query. * `price-ascending` - Sort results by price from high to low. All non-product results are pushed to the end of the results array. * `price-descending` - Sort results by price from low to high. All non-product results are pushed to the end of the results array.   Defaults to `relevance`. |

---

## [Anchor to The search form](/docs/storefronts/themes/navigation-search/search#the-search-form)The search form

The search form can be included with a `<form>` element that has an attribute of `action="/search"`.

Tip

You should use the [`routes` object](/docs/api/liquid/objects/routes#routes-search_url) to populate the `action` attribute so that the appropriate URL is used for multi-language stores.

**Tip:**

You should use the [`routes` object](/docs/api/liquid/objects/routes#routes-search_url) to populate the `action` attribute so that the appropriate URL is used for multi-language stores.

Inside the form, you can include inputs for each of the [query parameters](#query-parameters) above, where each input has the following attributes:

* `name="query-parameter"`
* `value="parameter-value"`

Aside from the `q` parameter, none of the query parameters require user input, so they should be hidden inputs.

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

<form action="{{ routes.search\_url }}">

<input type="text"

placeholder="Search"

name="q"

value="{{ search.terms | escape }}"

/>

<input type="hidden" name="type" value="product,page" />

<input type="hidden" name="options[unavailable\_products]" value="hide" />

<input type="hidden" name="options[prefix]" value="last" />

<input type="submit" value="Search" />

</form>

Tip

For another example of a search form, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/main-search.liquid).

**Tip:**

For another example of a search form, you can refer to [Dawn's implementation](https://github.com/Shopify/dawn/blob/main/sections/main-search.liquid).

---

## [Anchor to Search URL structure](/docs/storefronts/themes/navigation-search/search#search-url-structure)Search URL structure

When a search is performed, the search page's URL is updated to reflect that.

For example, a search with the following parameters returns the following URL:

| Attribute | Value |
| --- | --- |
| `q` | `snow` |
| `type` | `product,page` |
| `options[unavailable_products]` | `hide` |
| `options[prefix]` | `last` |

9

1

/search?q=snow&type=product,page&options[unavailable\_products]=hide&options[prefix]=last

---

Was this page helpful?

YesNo