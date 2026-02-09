---
source: https://shopify.dev/docs/api/liquid/filters/where
---

9

1

array | where: string, string

Filters an array to include only items with a specific property value.

This requires you to provide both the property name and the associated value.

9

1

2

3

4

5

6

7

{% assign polina\_products = collection.products | where: 'vendor', "Polina's Potent Potions" %}

Products from Polina's Potent Potions:

{% for product in polina\_products -%}

- {{ product.title }}

{%- endfor %}

##### Code

```liquid
{% assign polina_products = collection.products | where: 'vendor', "Polina's Potent Potions" %}

Products from Polina's Potent Potions:

{% for product in polina_products -%}
  - {{ product.title }}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "title": "Blue Mountain Flower",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Charcoal",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Crocodile tears",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dandelion milk",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Draught of Immortality",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Dried chamomile",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Forest mushroom",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Gift Card",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Glacier ice",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Ground mandrake root",
        "vendor": "Clover's Apothecary"
      },
      {
        "title": "Health potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Invisibility potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Komodo dragon scale",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Love Potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Mana potion",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion beats",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Potion bottle",
        "vendor": "Polina's Potent Potions"
      },
      {
        "title": "Viper venom",
        "vendor": "Ted's Apothecary Supply"
      },
      {
        "title": "Whole bloodroot",
        "vendor": "Clover's Apothecary"
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

Products from Polina's Potent Potions:

- Blue Mountain Flower

- Crocodile tears

- Draught of Immortality

- Gift Card

- Health potion

- Invisibility potion

- Love Potion

- Mana potion

- Potion beats

- Potion bottle

##### Output

```liquid
Products from Polina's Potent Potions:

- Blue Mountain Flower
- Crocodile tears
- Draught of Immortality
- Gift Card
- Health potion
- Invisibility potion
- Love Potion
- Mana potion
- Potion beats
- Potion bottle
```

[Anchor to Filter for boolean properties with a `true` value](/docs/api/liquid/filters/where#where-filter-for-boolean-properties-with-a-true-value)

### Filter for boolean properties with a `true` value

You can filter for items that have a `true` value for a boolean property. This requires you to provide only the property name.

9

1

2

3

4

5

6

7

{% assign available\_products = collection.products | where: 'available' %}

Available products:

{% for product in available\_products -%}

- {{ product.title }}

{%- endfor %}

##### Code

```liquid
{% assign available_products = collection.products | where: 'available' %}

Available products:

{% for product in available_products -%}
  - {{ product.title }}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "available": false,
        "title": "Blue Mountain Flower"
      },
      {
        "available": true,
        "title": "Charcoal"
      },
      {
        "available": false,
        "title": "Crocodile tears"
      },
      {
        "available": false,
        "title": "Dandelion milk"
      },
      {
        "available": true,
        "title": "Draught of Immortality"
      },
      {
        "available": true,
        "title": "Dried chamomile"
      },
      {
        "available": false,
        "title": "Forest mushroom"
      },
      {
        "available": true,
        "title": "Gift Card"
      },
      {
        "available": false,
        "title": "Glacier ice"
      },
      {
        "available": true,
        "title": "Ground mandrake root"
      },
      {
        "available": true,
        "title": "Health potion"
      },
      {
        "available": true,
        "title": "Invisibility potion"
      },
      {
        "available": false,
        "title": "Komodo dragon scale"
      },
      {
        "available": false,
        "title": "Love Potion"
      },
      {
        "available": true,
        "title": "Mana potion"
      },
      {
        "available": true,
        "title": "Potion beats"
      },
      {
        "available": false,
        "title": "Potion bottle"
      },
      {
        "available": true,
        "title": "Viper venom"
      },
      {
        "available": true,
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

Available products:

- Charcoal

- Draught of Immortality

- Dried chamomile

- Gift Card

- Ground mandrake root

- Health potion

- Invisibility potion

- Mana potion

- Potion beats

- Viper venom

- Whole bloodroot

##### Output

```liquid
Available products:

- Charcoal
- Draught of Immortality
- Dried chamomile
- Gift Card
- Ground mandrake root
- Health potion
- Invisibility potion
- Mana potion
- Potion beats
- Viper venom
- Whole bloodroot
```

Was this page helpful?

YesNo