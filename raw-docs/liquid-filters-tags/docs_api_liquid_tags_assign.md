---
source: https://shopify.dev/docs/api/liquid/tags/assign
---

Creates a new variable.

You can create variables of any [basic type](/docs/api/liquid/basics#types), [object](/docs/api/liquid/objects), or object property.

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

{% assign variable\_name = value %}

variable\_name

The name of the variable being created.

value

The value you want to assign to the variable.

9

1

2

3

{%- assign product\_title = product.title | upcase -%}

{{ product\_title }}

##### Code

```liquid
{%- assign product_title = product.title | upcase -%}

{{ product_title }}
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

HEALTH POTION

##### Output

```liquid
HEALTH POTION
```

Was this page helpful?

YesNo