---
source: https://shopify.dev/docs/api/liquid/filters/sort_natural
---

9

1

array | sort\_natural

Sorts the items in an array in case-insensitive alphabetical order.

---

Caution

You shouldn't use the `sort_natural` filter to sort numerical values. When comparing items an array, each item is converted to a
string, so sorting on numerical values can lead to unexpected results.

**Caution:**

You shouldn't use the `sort_natural` filter to sort numerical values. When comparing items an array, each item is converted to a
string, so sorting on numerical values can lead to unexpected results.

**Caution:** You shouldn&#39;t use the <code><span class="PreventFireFoxApplyingGapToWBR">sort<wbr/>\_natural</span></code> filter to sort numerical values. When comparing items an array, each item is converted to a
string, so sorting on numerical values can lead to unexpected results.

---

9

1

2

3

4

5

{% assign tags = collection.all\_tags | sort\_natural %}

{% for tag in tags -%}

{{ tag }}

{%- endfor %}

##### Code

```liquid
{% assign tags = collection.all_tags | sort_natural %}

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

dried

extra-potent

extracts

fresh

healing

ingredients

music

plant

Salty

supplies

##### Output

```liquid
Burning
dried
extra-potent
extracts
fresh
healing
ingredients
music
plant
Salty
supplies
```

[Anchor to Sort by an array item property](/docs/api/liquid/filters/sort_natural#sort_natural-sort-by-an-array-item-property)

### Sort by an array item property

9

1

array | sort\_natural: string

You can specify an array item property to sort the array items by.

9

1

2

3

4

5

{% assign products = collection.products | sort\_natural: 'title' %}

{% for product in products -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% assign products = collection.products | sort_natural: 'title' %}

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

Blue Mountain Flower

Charcoal

Crocodile tears

Dandelion milk

Draught of Immortality

Dried chamomile

Forest mushroom

Gift Card

Glacier ice

Ground mandrake root

Health potion

Invisibility potion

Komodo dragon scale

Love Potion

Mana potion

Potion beats

Potion bottle

Viper venom

Whole bloodroot

##### Output

```liquid
Blue Mountain Flower
Charcoal
Crocodile tears
Dandelion milk
Draught of Immortality
Dried chamomile
Forest mushroom
Gift Card
Glacier ice
Ground mandrake root
Health potion
Invisibility potion
Komodo dragon scale
Love Potion
Mana potion
Potion beats
Potion bottle
Viper venom
Whole bloodroot
```

Was this page helpful?

YesNo