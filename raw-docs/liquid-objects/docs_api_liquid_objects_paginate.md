---
source: https://shopify.dev/docs/api/liquid/objects/paginate
---

Information about the pagination inside a set of [`paginate` tags](/docs/api/liquid/tags/paginate).

---

Tip

Use the [`default_pagination` filter](/docs/api/liquid/filters/default_pagination) to output pagination links.

**Tip:**

Use the [`default_pagination` filter](/docs/api/liquid/filters/default_pagination) to output pagination links.

**Tip:** Use the <a href="/docs/api/liquid/filters/default\_pagination"><code><span class="PreventFireFoxApplyingGapToWBR">default<wbr/>\_pagination</span></code> filter</a> to output pagination links.

---

## Properties

[Anchor to](/docs/api/liquid/objects/paginate#paginate-current_offset) 

current\_offset**current\_offset** [number](/docs/api/liquid/basics#number)

:   The total number of items on pages previous to the current page.

    For example, if you show 5 items per page and are on page 3, then the value of `paginate.current_offset` is 10.

    Limited to 24,999 see [Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-current_page) 

current\_page**current\_page** [number](/docs/api/liquid/basics#number)

:   The page number of the current page.

    Limited to 25,000 see [Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-items) 

items**items** [number](/docs/api/liquid/basics#number)

:   The total number of items to be paginated.

    For example, if you paginate a collection of 120 products, then the value of `paginate.items` is 120.

    Limited to 25,000 see [Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-next) 

next**next** [part](/docs/api/liquid/objects/part)

:   The pagination part to go to the next page.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-page_param) 

page\_param**page\_param** [string](/docs/api/liquid/basics#string)

:   The URL parameter denoting the pagination.

    The default value is `page`.

    If you paginate over an array defined in a setting or a metafield list type, then a unique key is appended to page to allow the paginated list to
    operate independently from other lists on the page. For example, a paginated list defined in a setting might use the key
    `page_a9e329dc`.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-page_size) 

page\_size**page\_size** [number](/docs/api/liquid/basics#number)

:   The number of items displayed per page.

    Limited to 250.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-pages) 

pages**pages** [number](/docs/api/liquid/basics#number)

:   The total number of pages.

    Limited to 25,000 see [Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-parts) 

parts**parts** array of [part](/docs/api/liquid/objects/part)

:   The pagination parts.

    Pagination parts are used to build pagination navigation.

[Anchor to](/docs/api/liquid/objects/paginate#paginate-previous) 

previous**previous** [part](/docs/api/liquid/objects/part)

:   The pagination part to go to the previous page.

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

{

"current\_offset": 10,

"current\_page": 3,

"items": 17,

"next": {},

"page\_param": "page",

"page\_size": 5,

"pages": 4,

"parts": [],

"previous": {}

}

##### Example

```liquid
{
  "current_offset": 10,
  "current_page": 3,
  "items": 17,
  "next": {},
  "page_param": "page",
  "page_size": 5,
  "pages": 4,
  "parts": [],
  "previous": {}
}
```

Was this section helpful?

YesNo