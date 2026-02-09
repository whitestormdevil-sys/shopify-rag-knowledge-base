---
source: https://shopify.dev/docs/api/liquid/tags/paginate
---

Splits an array's items across multiple pages.

Because [`for` loops](/docs/api/liquid/tags/for) are limited to 50 iterations per page, you need to use the `paginate` tag to
iterate over an array that has more than 50 items. The following arrays can be paginated:

* [`article.comments`](/docs/api/liquid/objects/article#article-comments)
* [`blog.articles`](/docs/api/liquid/objects/blog#blog-articles)
* [`collections`](/docs/api/liquid/objects/collections)
* [`collection.products`](/docs/api/liquid/objects/collection#collection-products)
* [`customer.addresses`](/docs/api/liquid/objects/customer#customer-addresses)
* [`customer.orders`](/docs/api/liquid/objects/customer#customer-orders)
* [`metaobject_definition.values`](/docs/api/liquid/objects/metaobject_definition#metaobject_definition-values)
* [`pages`](/docs/api/liquid/objects/pages)
* [`product.variants`](/docs/api/liquid/objects/product#variants)
* [`search.results`](/docs/api/liquid/objects/search#search-results)
* [`article_list` settings](/themes/architecture/settings/input-settings#article_list)
* [`collection_list` settings](/themes/architecture/settings/input-settings#collection_list)
* [`product_list` settings](/themes/architecture/settings/input-settings#product_list)

Within the `paginate` tag, you have access to the [`paginate` object](/docs/api/liquid/objects/paginate). You can use this
object, or the [`default_pagination` filter](/docs/api/liquid/filters/default_pagination), to build page navigation.

---

Note

The `paginate` tag allows the user to paginate to the 25,000th item in the array and no further. To reach items further in
the array the array should be filtered further before paginating. See
[Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

**Note:**

The `paginate` tag allows the user to paginate to the 25,000th item in the array and no further. To reach items further in
the array the array should be filtered further before paginating. See
[Pagination Limits](/themes/best-practices/performance/platform#pagination-limits) for more information.

**Note:** The <code>paginate</code> tag allows the user to paginate to the 25,000th item in the array and no further. To reach items further in
the array the array should be filtered further before paginating. See
<a href="/themes/best-practices/performance/platform#pagination-limits">Pagination Limits</a> for more information.

---

## Syntax

9

1

2

3

4

5

{% paginate array by page\_size %}

{% for item in array %}

forloop\_content

{% endfor %}

{% endpaginate %}

array

The array to be looped over.

page\_size

The number of array items to include per page, between 1 and 250.

item

An item in the array being looped.

forloop\_content

Content for each loop iteration.

9

1

2

3

4

5

6

7

{% paginate collection.products by 5 %}

{% for product in collection.products -%}

{{ product.title }}

{%- endfor %}

{{- paginate | default\_pagination }}

{% endpaginate %}

##### Code

```liquid
{% paginate collection.products by 5 %}
  {% for product in collection.products -%}
    {{ product.title }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{% endpaginate %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      }
    ],
    "products_count": 19
  }
}
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

Blue Mountain Flower

Charcoal

Crocodile tears

Dandelion milk

Draught of Immortality

<span class="page current">1</span> <span class="page"><a href="/services/liquid\_rendering/resource?page=2" title="">2</a></span> <span class="page"><a href="/services/liquid\_rendering/resource?page=3" title="">3</a></span> <span class="page"><a href="/services/liquid\_rendering/resource?page=4" title="">4</a></span> <span class="next"><a href="/services/liquid\_rendering/resource?page=2" title="">Next &raquo;</a></span>

##### Output

```liquid
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
Draught of Immortality

<span class="page current">1</span> <span class="page"><a href="/services/liquid_rendering/resource?page=2" title="">2</a></span> <span class="page"><a href="/services/liquid_rendering/resource?page=3" title="">3</a></span> <span class="page"><a href="/services/liquid_rendering/resource?page=4" title="">4</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

[Anchor to Paginating setting arrays](/docs/api/liquid/tags/paginate#paginate-paginating-setting-arrays)

### Paginating setting arrays

To allow the pagination of `article_list`, `collection_list` and `product_list` settings to operate independently from other paginated lists on a page, these lists use a pagination query parameter with a unique key. The key is automatically assigned by the `paginate` tag, and you don't need to reference the key in your code. However, you can access the key using [`paginate.page_param`](/docs/api/liquid/objects/paginate#paginate-page_param).

---

Tip

To paginate two arrays independently without refreshing the entire page, you can use the [Section Rendering API](/docs/api/ajax/section-rendering).

**Tip:**

To paginate two arrays independently without refreshing the entire page, you can use the [Section Rendering API](/docs/api/ajax/section-rendering).

**Tip:** To paginate two arrays independently without refreshing the entire page, you can use the <a href="/docs/api/ajax/section-rendering">Section Rendering API</a>.

---

[Anchor to Limit data fetching](/docs/api/liquid/tags/paginate#paginate-limit-data-fetching)

### Limit data fetching

The [`limit` parameter](/docs/api/liquid/tags/for#for-limit) of the `for` tag controls the number of iterations, but not the amount of information fetched. Using the `paginate` tag with a matching `page_size` can reduce the data queried, leading to faster server response times.

For example, referencing `collection.products` will fetch up to 50 products by default, regardless of the forloop's `limit` parameter. Use `paginate` and set a `page_size` to limit the amount of data fetched, and opt not to display any pagination controls.

More data than requested in a specific section may be returned. Because of this, make sure to include both `paginate` and `limit` when using this technique.

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

{% paginate collection.products by 4 %}

{% for product in collection.products limit: 4 -%}

{{ product.title }}

{%- endfor %}

{% endpaginate -%}

<!-- Less performant method -->

{% for product in collection.products limit: 4 -%}

{{ product.title }}

{%- endfor -%}

##### Code

```liquid
{% paginate collection.products by 4 %}
  {% for product in collection.products limit: 4 -%}
    {{ product.title }}
  {%- endfor %}
{% endpaginate -%}

<!-- Less performant method -->
{% for product in collection.products limit: 4 -%}
  {{ product.title }}
{%- endfor -%}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      }
    ],
    "products_count": 19
  }
}
```

## Output

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

Blue Mountain Flower

Charcoal

Crocodile tears

Dandelion milk

<!-- Less performant method -->

Blue Mountain Flower

Charcoal

Crocodile tears

Dandelion milk

##### Output

```liquid
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk

<!-- Less performant method -->
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
```

[Anchor to paginate](/docs/api/liquid/tags/paginate#paginate-parameters)

## paginate tag parameters

[Anchor to window\_size](/docs/api/liquid/tags/paginate#paginate-window_size)

### window\_size

## Syntax

9

1

{% paginate collection.products by 3, window\_size: 1 %}

Set the window size of the pagination. The window size is the number of pages that should be visible in the pagination navigation.

9

1

2

3

4

5

6

7

{% paginate collection.products by 3, window\_size: 1 %}

{% for product in collection.products -%}

{{ product.title }}

{%- endfor %}

{{- paginate | default\_pagination }}

{% endpaginate %}

##### Code

```liquid
{% paginate collection.products by 3, window_size: 1 %}
  {% for product in collection.products -%}
    {{ product.title }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{% endpaginate %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      }
    ],
    "products_count": 19
  }
}
```

## Output

9

1

2

3

4

5

Blue Mountain Flower

Charcoal

Crocodile tears

<span class="page current">1</span> <span class="deco">&hellip;</span> <span class="page"><a href="/services/liquid\_rendering/resource?page=7" title="">7</a></span> <span class="next"><a href="/services/liquid\_rendering/resource?page=2" title="">Next &raquo;</a></span>

##### Output

```liquid
Blue Mountain Flower
Charcoal
Crocodile tears

<span class="page current">1</span> <span class="deco">&hellip;</span> <span class="page"><a href="/services/liquid_rendering/resource?page=7" title="">7</a></span> <span class="next"><a href="/services/liquid_rendering/resource?page=2" title="">Next &raquo;</a></span>
```

Was this page helpful?

YesNo