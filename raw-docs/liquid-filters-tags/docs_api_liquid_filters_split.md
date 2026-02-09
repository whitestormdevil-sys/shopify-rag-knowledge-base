---
source: https://shopify.dev/docs/api/liquid/filters/split
---

9

1

string | split: string

returns array of [string](/docs/api/liquid/basics#string)

Splits a string into an array of substrings based on a given separator.

9

1

2

3

4

5

{%- assign title\_words = product.handle | split: '-' -%}

{% for word in title\_words -%}

{{ word }}

{%- endfor %}

##### Code

```liquid
{%- assign title_words = product.handle | split: '-' -%}

{% for word in title_words -%}
  {{ word }}
{%- endfor %}
```

##### Data

```liquid
{
  "product": {
    "handle": "health-potion"
  }
}
```

## Output

9

1

2

health

potion

##### Output

```liquid
health
potion
```

Was this page helpful?

YesNo