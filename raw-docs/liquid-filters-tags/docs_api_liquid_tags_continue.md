---
source: https://shopify.dev/docs/api/liquid/tags/continue
---

Causes a [`for` loop](/docs/api/liquid/tags/for) to skip to the next iteration.

## Syntax

9

1

{% continue %}

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

{% continue %}

{%- else -%}

{{ i }}

{%- endif -%}

{%- endfor %}

##### Code

```liquid
{% for i in (1..5) -%}
  {%- if i == 4 -%}
    {% continue %}
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

4

1

2

3

5

##### Output

```liquid
1
2
3
5
```

Was this page helpful?

YesNo