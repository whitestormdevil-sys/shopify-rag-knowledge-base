---
source: https://shopify.dev/docs/api/liquid/tags/break
---

Stops a [`for` loop](/docs/api/liquid/tags/for) from iterating.

## Syntax

9

1

{% break %}

9

1

2

3

4

5

6

7

{% for i in (1..5) -%}

{%- if i == 4 -%}

{% break %}

{%- else -%}

{{ i }}

{%- endif -%}

{%- endfor %}

##### Code

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% break %}
  {%- else -%}
    {{ i }}
  {%- endif -%}
{%- endfor %}
```

## Output

9

1

2

3

1

2

3

##### Output

```liquid
1
2
3
```

Was this page helpful?

YesNo