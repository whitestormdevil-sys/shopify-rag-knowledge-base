---
source: https://shopify.dev/docs/api/liquid/filters/concat
---

9

1

array | concat: array

Concatenates (combines) two arrays.

---

Note

The `concat` filter won't filter out duplicates. If you want to remove duplicates, then you need to use the
[`uniq` filter](/docs/api/liquid/filters/uniq).

**Note:**

The `concat` filter won't filter out duplicates. If you want to remove duplicates, then you need to use the
[`uniq` filter](/docs/api/liquid/filters/uniq).

**Note:** The <code>concat</code> filter won&#39;t filter out duplicates. If you want to remove duplicates, then you need to use the
<a href="/docs/api/liquid/filters/uniq"><code>uniq</code> filter</a>.

---

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

{%- assign types\_and\_vendors = collection.all\_types | concat: collection.all\_vendors -%}

Types and vendors:

{% for item in types\_and\_vendors -%}

{%- if item != blank -%}

- {{ item }}

{%- endif -%}

{%- endfor %}

##### Code

```liquid
{%- assign types_and_vendors = collection.all_types | concat: collection.all_vendors -%}

Types and vendors:

{% for item in types_and_vendors -%}
  {%- if item != blank -%}
    - {{ item }}
  {%- endif -%}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "all_types": [
      "",
      "Animals & Pet Supplies",
      "Baking Flavors & Extracts",
      "Container",
      "Cooking & Baking Ingredients",
      "Dried Flowers",
      "Fruits & Vegetables",
      "Gift Cards",
      "Health",
      "Health & Beauty",
      "Invisibility",
      "Love",
      "Music & Sound Recordings",
      "Seasonings & Spices",
      "Water"
    ],
    "all_vendors": [
      "Clover's Apothecary",
      "Polina's Potent Potions",
      "Ted's Apothecary Supply"
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

Types and vendors:

- Animals & Pet Supplies

- Baking Flavors & Extracts

- Container

- Cooking & Baking Ingredients

- Dried Flowers

- Fruits & Vegetables

- Gift Cards

- Health

- Health & Beauty

- Invisibility

- Love

- Music & Sound Recordings

- Seasonings & Spices

- Water

- Clover's Apothecary

- Polina's Potent Potions

- Ted's Apothecary Supply

##### Output

```liquid
Types and vendors:

- Animals & Pet Supplies
- Baking Flavors & Extracts
- Container
- Cooking & Baking Ingredients
- Dried Flowers
- Fruits & Vegetables
- Gift Cards
- Health
- Health & Beauty
- Invisibility
- Love
- Music & Sound Recordings
- Seasonings & Spices
- Water
- Clover's Apothecary
- Polina's Potent Potions
- Ted's Apothecary Supply
```

Was this page helpful?

YesNo