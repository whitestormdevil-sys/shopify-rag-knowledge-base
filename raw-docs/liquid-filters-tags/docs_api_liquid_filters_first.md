---
source: https://shopify.dev/docs/api/liquid/filters/first
---

9

1

array | first

Returns the first item in an array.

9

1

2

3

{%- assign first\_product = collection.products | first -%}

{{ first\_product.title }}

##### Code

```liquid
{%- assign first_product = collection.products | first -%}

{{ first_product.title }}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

## Output

9

1

Blue Mountain Flower

##### Output

```liquid
Blue Mountain Flower
```

[Anchor to Dot notation](/docs/api/liquid/filters/first#first-dot-notation)

### Dot notation

You can use the `first` filter with dot notation when you need to use it inside a tag or object output.

9

1

{{ collection.products.first.title }}

##### Code

```liquid
{{ collection.products.first.title }}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower"
      },
      {
        "title": "Charcoal"
      },
      {
        "title": "Crocodile tears"
      },
      {
        "title": "Dandelion milk"
      },
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Dried chamomile"
      },
      {
        "title": "Forest mushroom"
      },
      {
        "title": "Gift Card"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Ground mandrake root"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      },
      {
        "title": "Komodo dragon scale"
      },
      {
        "title": "Love Potion"
      },
      {
        "title": "Mana potion"
      },
      {
        "title": "Potion beats"
      },
      {
        "title": "Potion bottle"
      },
      {
        "title": "Viper venom"
      },
      {
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

## Output

9

1

Blue Mountain Flower

##### Output

```liquid
Blue Mountain Flower
```

Was this page helpful?

YesNo