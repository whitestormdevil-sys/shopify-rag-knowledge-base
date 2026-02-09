---
source: https://shopify.dev/docs/api/liquid/objects/search
---

Information about a storefront search query.

To learn about storefront search and how to include it in your theme, refer to [Storefront search](/themes/navigation-search/search).

## Properties

[Anchor to](/docs/api/liquid/objects/search#search-default_sort_by) 

default\_sort\_by**default\_sort\_by** [string](/docs/api/liquid/basics#string)

:   The default sort order of the search results, which is `relevance`.

[Anchor to](/docs/api/liquid/objects/search#search-filters) 

filters**filters** array of [filter](/docs/api/liquid/objects/filter)

:   The filters that have been set up on the search page.

    Only filters that are relevant to the current search results are returned. If the search results contain more than 1000
    products, then the array will be empty.

    Tip

    To learn about how to set up filters in the admin, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).

    **Tip:**

    To learn about how to set up filters in the admin, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).

    **Tip:** To learn about how to set up filters in the admin, visit the <a href="https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/search#search-performed) 

performed**performed** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if a search was successfully performed. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/search#search-results) 

results**results**

:   The search result items.

    An item can be an [`article`](/docs/api/liquid/objects/article), a [`page`](/docs/api/liquid/objects/page), or a
    [`product`](/docs/api/liquid/objects/product).

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many results to show per page, up to a limit of 50.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many results to show per page, up to a limit of 50.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many results to show per page, up to a limit of 50.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Search result `object_type`

    Search results have an additional `object_type` property that returns the object type of the result.

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

    12

    13

    14

    15

    16

    17

    18

    19

    20

    21

    22

    23

    24

    25

    26

    27

    28

    29

    30

    31

    32

    33

    34

    35

    36

    37

    38

    39

    40

    41

    {% for item in search.results %}

    <!-- Result {{ forloop.index }}-->

    <h3>

    {{ item.title | link\_to: item.url }}

    </h3>

    {% if item.object\_type == 'article' -%}

    {%- comment -%}

    'item' is an article

    All article object properties can be accessed.

    {%- endcomment -%}

    {% if item.image -%}

    <div class="result-image">

    <a href="{{ item.url }}" title="{{ item.title | escape }}">

    {{ item | image\_url: width: 100 | image\_tag }}

    </a>

    </div>

    {% endif %}

    {%- elsif item.object\_type == 'page' -%}

    {%- comment -%}

    'item' is a page.

    All page object properties can be accessed.

    {%- endcomment -%}

    {%- else -%}

    {%- comment -%}

    'item' is a product.

    All product object properties can be accessed.

    {%- endcomment -%}

    {%- if item.featured\_image -%}

    <div class="result-image">

    <a href="{{ item.url }}" title="{{ item.title | escape }}">

    {{ item.featured\_image | image\_url: width: 100 | image\_tag }}

    </a>

    </div>

    {% endif %}

    {%- endif -%}

    <span>{{ item.content | strip\_html | truncatewords: 40 | highlight: search.terms }}</span>

    {% endfor %}

    ##### Code

    ```liquid
    {% for item in search.results %}
    <!-- Result {{ forloop.index }}-->
    <h3>
      {{ item.title | link_to: item.url }}
    </h3>

    {% if item.object_type == 'article' -%}
      {%- comment -%}
         'item' is an article
         All article object properties can be accessed.
      {%- endcomment -%}

      {% if item.image -%}
        <div class="result-image">
          <a href="{{ item.url }}" title="{{ item.title | escape }}">
            {{ item | image_url: width: 100 | image_tag }}
           </a>
        </div>
       {% endif %}
    {%- elsif item.object_type == 'page' -%}
      {%- comment -%}
        'item' is a page.
         All page object properties can be accessed.
      {%- endcomment -%}
    {%- else -%}
      {%- comment -%}
         'item' is a product.
         All product object properties can be accessed.
      {%- endcomment -%}

      {%- if item.featured_image -%}
        <div class="result-image">
           <a href="{{ item.url }}" title="{{ item.title | escape }}">
             {{ item.featured_image | image_url: width: 100 | image_tag }}
          </a>
        </div>
      {% endif %}
    {%- endif -%}

    <span>{{ item.content | strip_html | truncatewords: 40 | highlight: search.terms }}</span>
    {% endfor %}
    ```

    ##### Data

    ## Output

    9

    1

    ##### Output

[Anchor to](/docs/api/liquid/objects/search#search-results_count) 

results\_count**results\_count** [number](/docs/api/liquid/basics#number)

:   The number of results.

[Anchor to](/docs/api/liquid/objects/search#search-sort_by) 

sort\_by**sort\_by**

:   The sort order of the search results. This is determined by the `sort_by` URL parameter.

    If there's no `sort_by` URL parameter, then the value is `nil`.

[Anchor to](/docs/api/liquid/objects/search#search-sort_options) 

sort\_options**sort\_options** array of [sort\_option](/docs/api/liquid/objects/sort_option)

:   The available sorting options for the search results.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the sort options

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

    12

    13

    14

    {%- assign sort\_by = search.sort\_by | default: search.default\_sort\_by -%}

    <select>

    {%- for option in search.sort\_options %}

    <option

    value="{{ option.value }}"

    {%- if option.value == sort\_by %}

    selected="selected"

    {%- endif %}

    >

    {{ option.name }}

    </option>

    {% endfor -%}

    </select>

    ##### Code

    ```liquid
    {%- assign sort_by = search.sort_by | default: search.default_sort_by -%}

    <select>
    {%- for option in search.sort_options %}
      <option
        value="{{ option.value }}"
        {%- if option.value == sort_by %}
          selected="selected"
        {%- endif %}
      >
        {{ option.name }}
      </option>
    {% endfor -%}
    </select>
    ```

    ##### Data

    ## Output

    9

    1

    ##### Output

[Anchor to](/docs/api/liquid/objects/search#search-terms) 

terms**terms** [string](/docs/api/liquid/basics#string)

:   The entered search terms.

    Tip

    Use the [`highlight` filter](/docs/api/liquid/filters/highlight) to highlight the search terms in search result content.

    **Tip:**

    Use the [`highlight` filter](/docs/api/liquid/filters/highlight) to highlight the search terms in search result content.

    **Tip:** Use the <a href="/docs/api/liquid/filters/highlight"><code>highlight</code> filter</a> to highlight the search terms in search result content.

[Anchor to](/docs/api/liquid/objects/search#search-types) 

types**types** array of [string](/docs/api/liquid/basics#string)

:   The object types that the search was performed on.

    A search can be performed on the following object types:

    * [`article`](/docs/api/liquid/objects/article)
    * [`page`](/docs/api/liquid/objects/page)
    * [`product`](/docs/api/liquid/objects/product)

    Note

    The types are determined by the [`type` query parameter](/api/ajax/reference/predictive-search#query-parameters).

    **Note:**

    The types are determined by the [`type` query parameter](/api/ajax/reference/predictive-search#query-parameters).

    **Note:** The types are determined by the <a href="/api/ajax/reference/predictive-search#query-parameters"><code>type</code> query parameter</a>.

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

12

13

14

15

{

"default\_sort\_by": "relevance",

"filters": {},

"performed": true,

"results": [],

"results\_count": 16,

"sort\_by": "relevance",

"sort\_options": [],

"terms": "potion",

"types": [

"article",

"page",

"product"

]

}

##### Example

```liquid
{
  "default_sort_by": "relevance",
  "filters": {},
  "performed": true,
  "results": [],
  "results_count": 16,
  "sort_by": "relevance",
  "sort_options": [],
  "terms": "potion",
  "types": [
    "article",
    "page",
    "product"
  ]
}
```

[Anchor to](/docs/api/liquid/objects/search#template-using) 

## Templates using search

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturesearch template

Theme architecture

search template](/themes/architecture/templates/search)

Was this section helpful?

YesNo