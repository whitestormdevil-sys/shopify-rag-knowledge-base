---
source: https://shopify.dev/docs/api/liquid/tags/capture
---

Creates a new variable with a string value.

You can create complex strings with Liquid logic and variables.

---

Caution

Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.

**Caution:**

Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.

**Caution:** Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn&#39;t match a predefined object&#39;s name.

---

## Syntax

9

1

2

3

{% capture variable %}

value

{% endcapture %}

variable

The name of the variable being created.

value

The value you want to assign to the variable.

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

{%- assign up\_title = product.title | upcase -%}

{%- assign down\_title = product.title | downcase -%}

{%- assign show\_up\_title = true -%}

{%- capture title -%}

{% if show\_up\_title -%}

Upcase title: {{ up\_title }}

{%- else -%}

Downcase title: {{ down\_title }}

{%- endif %}

{%- endcapture %}

{{ title }}

##### Code

```liquid
{%- assign up_title = product.title | upcase -%}
{%- assign down_title = product.title | downcase -%}
{%- assign show_up_title = true -%}

{%- capture title -%}
  {% if show_up_title -%}
    Upcase title: {{ up_title }}
  {%- else -%}
    Downcase title: {{ down_title }}
  {%- endif %}
{%- endcapture %}

{{ title }}
```

##### Data

```liquid
{
  "product": {
    "title": "Health potion"
  }
}
```

## Output

9

1

Upcase title: HEALTH POTION

##### Output

```liquid
Upcase title: HEALTH POTION
```

Was this page helpful?

YesNo