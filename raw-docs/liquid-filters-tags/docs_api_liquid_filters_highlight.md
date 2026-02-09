---
source: https://shopify.dev/docs/api/liquid/filters/highlight
---

9

1

string | highlight: string

returns [string](/docs/api/liquid/basics#string)

Wraps all instances of a specific string, within a given string, with an HTML `<strong>` tag with a `class` attribute
of `highlight`.

9

1

2

3

4

5

6

7

{% for item in search.results %}

{% if item.object\_type == 'product' %}

{{ item.description | highlight: search.terms }}

{% else %}

{{ item.content | highlight: search.terms }}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for item in search.results %}
  {% if item.object_type == 'product' %}
    {{ item.description | highlight: search.terms }}
  {% else %}
    {{ item.content | highlight: search.terms }}
  {% endif %}
{% endfor %}
```

##### Data

```liquid
{
  "search": {
    "results": [
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      },
      {
        "description": "This is a love potion.",
        "object_type": "product"
      },
      {
        "description": "",
        "object_type": "product"
      }
    ],
    "terms": "love"
  }
}
```

## Output

9

1

This is a <strong class="highlight">love</strong> potion.

##### Output

```liquid
This is a <strong class="highlight">love</strong> potion.
```

Was this page helpful?

YesNo