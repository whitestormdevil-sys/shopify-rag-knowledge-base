---
source: https://shopify.dev/docs/api/liquid/tags/if
---

Renders an expression if a specific condition is `true`.

## Syntax

9

1

2

3

{% if condition %}

expression

{% endif %}

condition

The condition to evaluate.

expression

The expression to render if the condition is met.

9

1

2

3

{% if product.compare\_at\_price > product.price %}

This product is on sale!

{% endif %}

##### Code

```liquid
{% if product.compare_at_price > product.price %}
  This product is on sale!
{% endif %}
```

##### Data

```liquid
{
  "product": {
    "compare_at_price": "10.00",
    "price": "0.00"
  }
}
```

## Output

9

1

This product is on sale!

##### Output

```liquid
This product is on sale!
```

[Anchor to elsif](/docs/api/liquid/tags/if#if-elsif)

### elsif

You can use the `elsif` tag to check for multiple conditions.

9

1

2

3

4

5

{% if product.type == 'Love' %}

This is a love potion!

{% elsif product.type == 'Health' %}

This is a health potion!

{% endif %}

##### Code

```liquid
{% if product.type == 'Love' %}
  This is a love potion!
{% elsif product.type == 'Health' %}
  This is a health potion!
{% endif %}
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

This is a health potion!

##### Output

```liquid
This is a health potion!
```

Was this page helpful?

YesNo