---
source: https://shopify.dev/docs/api/liquid/filters/size
---

9

1

variable | size

returns [number](/docs/api/liquid/basics#number)

Returns the size of a string or array.

The size of a string is the number of characters that the string includes. The size of an array is the number of items
in the array.

9

1

2

{{ collection.title | size }}

{{ collection.products | size }}

##### Code

```liquid
{{ collection.title | size }}
{{ collection.products | size }}
```

##### Data

```liquid
{
  "collection": {
    "products": [],
    "title": "Sale potions"
  }
}
```

## Output

9

1

2

12

4

##### Output

```liquid
12
4
```

[Anchor to Dot notation](/docs/api/liquid/filters/size#size-dot-notation)

### Dot notation

You can use the `size` filter with dot notation when you need to use it inside a tag or object output.

9

1

2

3

4

5

{% if collection.products.size >= 10 %}

There are 10 or more products in this collection.

{% else %}

There are less than 10 products in this collection.

{% endif %}

##### Code

```liquid
{% if collection.products.size >= 10 %}
  There are 10 or more products in this collection.
{% else %}
  There are less than 10 products in this collection.
{% endif %}
```

##### Data

```liquid
{
  "collection": {
    "products": []
  }
}
```

## Output

9

1

There are less than 10 products in this collection.

##### Output

```liquid
There are less than 10 products in this collection.
```

Was this page helpful?

YesNo