---
source: https://shopify.dev/docs/api/liquid/filters/map
---

9

1

array | map: string

Creates an array of values from a specific property of the items in an array.

9

1

2

3

{%- assign product\_titles = collection.products | map: 'title' -%}

{{ product\_titles | join: ', ' }}

##### Code

```liquid
{%- assign product_titles = collection.products | map: 'title' -%}

{{ product_titles | join: ', ' }}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

## Output

9

1

Draught of Immortality, Glacier ice, Health potion, Invisibility potion

##### Output

```liquid
Draught of Immortality, Glacier ice, Health potion, Invisibility potion
```

Was this page helpful?

YesNo