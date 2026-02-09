---
source: https://shopify.dev/docs/api/liquid/filters/sort
---

9

1

array | sort

Sorts the items in an array in case-sensitive alphabetical, or numerical, order.

9

1

2

3

4

5

{% assign tags = collection.all\_tags | sort %}

{% for tag in tags -%}

{{ tag }}

{%- endfor %}

##### Code

```liquid
{% assign tags = collection.all_tags | sort %}

{% for tag in tags -%}
  {{ tag }}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ]
  }
}
```

## Output

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

Burning

Salty

dried

extra-potent

extracts

fresh

healing

ingredients

music

plant

supplies

##### Output

```liquid
Burning
Salty
dried
extra-potent
extracts
fresh
healing
ingredients
music
plant
supplies
```

[Anchor to Sort by an array item property](/docs/api/liquid/filters/sort#sort-sort-by-an-array-item-property)

### Sort by an array item property

9

1

array | sort: string

You can specify an array item property to sort the array items by. You can sort by any property of the object that you're sorting.

9

1

2

3

4

5

{% assign products = collection.products | sort: 'price' %}

{% for product in products -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% assign products = collection.products | sort: 'price' %}

{% for product in products -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "price": "10.00",
        "title": "Blue Mountain Flower"
      },
      {
        "price": "0.00",
        "title": "Charcoal"
      },
      {
        "price": "56.00",
        "title": "Crocodile tears"
      },
      {
        "price": "0.00",
        "title": "Dandelion milk"
      },
      {
        "price": "1000000.00",
        "title": "Draught of Immortality"
      },
      {
        "price": "8.98",
        "title": "Dried chamomile"
      },
      {
        "price": "0.00",
        "title": "Forest mushroom"
      },
      {
        "price": "10.00",
        "title": "Gift Card"
      },
      {
        "price": "0.00",
        "title": "Glacier ice"
      },
      {
        "price": "0.00",
        "title": "Ground mandrake root"
      },
      {
        "price": "10.00",
        "title": "Health potion"
      },
      {
        "price": "250.00",
        "title": "Invisibility potion"
      },
      {
        "price": "0.00",
        "title": "Komodo dragon scale"
      },
      {
        "price": "0.00",
        "title": "Love Potion"
      },
      {
        "price": "10.00",
        "title": "Mana potion"
      },
      {
        "price": "0.00",
        "title": "Potion beats"
      },
      {
        "price": "0.00",
        "title": "Potion bottle"
      },
      {
        "price": "400.00",
        "title": "Viper venom"
      },
      {
        "price": "24.99",
        "title": "Whole bloodroot"
      }
    ]
  }
}
```

## Output

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

14

15

16

17

18

19

Charcoal

Dandelion milk

Forest mushroom

Glacier ice

Ground mandrake root

Komodo dragon scale

Love Potion

Potion beats

Potion bottle

Dried chamomile

Blue Mountain Flower

Gift Card

Health potion

Mana potion

Whole bloodroot

Crocodile tears

Invisibility potion

Viper venom

Draught of Immortality

##### Output

```liquid
Charcoal
Dandelion milk
Forest mushroom
Glacier ice
Ground mandrake root
Komodo dragon scale
Love Potion
Potion beats
Potion bottle
Dried chamomile
Blue Mountain Flower
Gift Card
Health potion
Mana potion
Whole bloodroot
Crocodile tears
Invisibility potion
Viper venom
Draught of Immortality
```

Was this page helpful?

YesNo