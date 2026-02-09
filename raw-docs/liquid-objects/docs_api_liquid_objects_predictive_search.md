---
source: https://shopify.dev/docs/api/liquid/objects/predictive_search
---

Information about the results from a predictive search query through the
[Predictive Search API](/api/ajax/reference/predictive-search#get-locale-search-suggest).

---

Note

The `predictive_search` object returns results only when rendered in a section using the Predictive Search API and the
[Section Rendering API](/api/section-rendering). To learn about how to include predictive search in your theme,
refer to [Add predictive search to your theme](/themes/navigation-search/search/predictive-search).

**Note:**

The `predictive_search` object returns results only when rendered in a section using the Predictive Search API and the
[Section Rendering API](/api/section-rendering). To learn about how to include predictive search in your theme,
refer to [Add predictive search to your theme](/themes/navigation-search/search/predictive-search).

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">predictive<wbr/>\_search</span></code> object returns results only when rendered in a section using the Predictive Search API and the
<a href="/api/section-rendering">Section Rendering API</a>. To learn about how to include predictive search in your theme,
refer to <a href="/themes/navigation-search/search/predictive-search">Add predictive search to your theme</a>.

---

## Properties

[Anchor to](/docs/api/liquid/objects/predictive_search#predictive_search-performed) 

performed**performed** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` when being referenced inside a section that's been rendered using the Predictive Search API and
    the Section Rendering API. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/predictive_search#predictive_search-resources) 

resources**resources** [predictive\_search\_resources](/docs/api/liquid/objects/predictive_search_resources)

:   The resources associated with the query.

    You can check whether any resources of a specific type were returned using the [`size` filter](/docs/api/liquid/filters/size).

    9

    1

    2

    3

    4

    5

    {% if predictive\_search.resources.articles.size > 0 %}

    {% for article in predictive\_search.resources.articles %}

    {{ article.title }}

    {% endfor %}

    {% endif %}

    ```liquid
    {% if predictive_search.resources.articles.size > 0 %}
      {% for article in predictive_search.resources.articles %}
        {{ article.title }}
      {% endfor %}
    {% endif %}
    ```

[Anchor to](/docs/api/liquid/objects/predictive_search#predictive_search-terms) 

terms**terms** [string](/docs/api/liquid/basics#string)

:   The entered search terms.

    Tip

    Use the [`highlight` filter](/docs/api/liquid/filters/highlight) to highlight the search terms in search results content.

    **Tip:**

    Use the [`highlight` filter](/docs/api/liquid/filters/highlight) to highlight the search terms in search results content.

    **Tip:** Use the <a href="/docs/api/liquid/filters/highlight"><code>highlight</code> filter</a> to highlight the search terms in search results content.

[Anchor to](/docs/api/liquid/objects/predictive_search#predictive_search-types) 

types**types** array of [string](/docs/api/liquid/basics#string)

:   The object types that the search was performed on.

    Searches can be performed on the following object types:

    * [`article`](/docs/api/liquid/objects/article)
    * [`collection`](/docs/api/liquid/objects/collection)
    * [`page`](/docs/api/liquid/objects/page)
    * [`product`](/docs/api/liquid/objects/product)

    Note

    The types are determined by the [`type` query parameter](/api/ajax/reference/predictive-search#query-parameters).

    **Note:**

    The types are determined by the [`type` query parameter](/api/ajax/reference/predictive-search#query-parameters).

    **Note:** The types are determined by the <a href="/api/ajax/reference/predictive-search#query-parameters"><code>type</code> query parameter</a>.

9

1

2

3

4

5

6

{

"performed": true,

"resources": {},

"terms": "potion",

"types": []

}

##### Example

```liquid
{
  "performed": true,
  "resources": {},
  "terms": "potion",
  "types": []
}
```

Was this section helpful?

YesNo