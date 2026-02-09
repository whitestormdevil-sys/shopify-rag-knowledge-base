---
source: https://shopify.dev/docs/api/liquid/filters/reverse
---

9

1

array | reverse

Reverses the order of the items in an array.

9

1

2

3

4

5

Original order:

{{ collection.products | map: 'title' | join: ', ' }}

Reverse order:

{{ collection.products | reverse | map: 'title' | join: ', ' }}

##### Code

```liquid
Original order:
{{ collection.products | map: 'title' | join: ', ' }}

Reverse order:
{{ collection.products | reverse | map: 'title' | join: ', ' }}
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

2

3

4

5

Original order:

Draught of Immortality, Glacier ice, Health potion, Invisibility potion

Reverse order:

Invisibility potion, Health potion, Glacier ice, Draught of Immortality

##### Output

```liquid
Original order:
Draught of Immortality, Glacier ice, Health potion, Invisibility potion

Reverse order:
Invisibility potion, Health potion, Glacier ice, Draught of Immortality
```

[Anchor to Reversing strings](/docs/api/liquid/filters/reverse#reverse-reversing-strings)

### Reversing strings

You can't use the `reverse` filter on strings directly. However, you can use the [`split` filter](/docs/api/liquid/filters/split) to create an array of characters in the string, reverse that array, and then use the [`join` filter](/docs/api/liquid/filters/join) to combine them again.

9

1

{{ collection.title | split: '' | reverse | join: '' }}

##### Code

```liquid
{{ collection.title | split: '' | reverse | join: '' }}
```

##### Data

```liquid
{
  "collection": {
    "title": "Sale potions"
  }
}
```

## Output

9

1

snoitop elaS

##### Output

```liquid
snoitop elaS
```

Was this page helpful?

YesNo