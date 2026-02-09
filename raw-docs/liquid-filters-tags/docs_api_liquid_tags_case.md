---
source: https://shopify.dev/docs/api/liquid/tags/case
---

Renders a specific expression depending on the value of a specific variable.

## Syntax

9

1

2

3

4

5

6

7

8

{% case variable %}

{% when first\_value %}

first\_expression

{% when second\_value %}

second\_expression

{% else %}

third\_expression

{% endcase %}

variable

The name of the variable you want to base your case statement on.

first\_value

A specific value to check for.

second\_value

A specific value to check for.

first\_expression

An expression to be rendered when the variable's value matches `first_value`.

second\_expression

An expression to be rendered when the variable's value matches `second_value`.

third\_expression

An expression to be rendered when the variable's value has no match.

9

1

2

3

4

5

6

7

8

{% case product.type %}

{% when 'Health' %}

This is a health potion.

{% when 'Love' %}

This is a love potion.

{% else %}

This is a potion.

{% endcase %}

##### Code

```liquid
{% case product.type %}
  {% when 'Health' %}
    This is a health potion.
  {% when 'Love' %}
    This is a love potion.
  {% else %}
    This is a potion.
{% endcase %}
```

##### Data

```liquid
{
  "product": {
    "type": null
  }
}
```

## Output

9

1

This is a health potion.

##### Output

```liquid
This is a health potion.
```

[Anchor to Multiple values](/docs/api/liquid/tags/case#case-multiple-values)

### Multiple values

## Syntax

9

1

2

3

4

5

6

7

8

9

{% case variable %}

{% when first\_value or second\_value or third\_value %}

first\_expression

{% when fourth\_value, fifth\_value, sixth\_value %}

second\_expression

{% else %}

third\_expression

{% endcase %}

A `when` tag can accept multiple values. When multiple values are provided, the expression is returned when the variable matches any of the values inside of the tag.
Provide the values as a comma-separated list, or separate them using an `or` operator.

9

1

2

3

4

5

6

7

8

{% case product.type %}

{% when 'Love' or 'Luck' %}

This is a love or luck potion.

{% when 'Strength','Health' %}

This is a strength or health potion.

{% else %}

This is a potion.

{% endcase %}

##### Code

```liquid
{% case product.type %}
  {% when 'Love' or 'Luck' %}
    This is a love or luck potion.
  {% when 'Strength','Health' %}
    This is a strength or health potion.
  {% else %}
    This is a potion.
{% endcase %}
```

##### Data

```liquid
{
  "product": {
    "type": null
  }
}
```

## Output

9

1

This is a strength or health potion.

##### Output

```liquid
This is a strength or health potion.
```

Was this page helpful?

YesNo