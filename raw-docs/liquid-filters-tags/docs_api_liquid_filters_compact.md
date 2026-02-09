---
source: https://shopify.dev/docs/api/liquid/filters/compact
---

9

1

array | compact

Removes any `nil` items from an array.

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

{%- assign original\_prices = collection.products | map: 'compare\_at\_price' -%}

Original prices:

{% for price in original\_prices -%}

- {{ price }}

{%- endfor %}

{%- assign compacted\_original\_prices = original\_prices | compact -%}

Original prices - compacted:

{% for price in compacted\_original\_prices -%}

- {{ price }}

{%- endfor %}

##### Code

```liquid
{%- assign original_prices = collection.products | map: 'compare_at_price' -%}

Original prices:

{% for price in original_prices -%}
  - {{ price }}
{%- endfor %}

{%- assign compacted_original_prices = original_prices | compact -%}

Original prices - compacted:

{% for price in compacted_original_prices -%}
  - {{ price }}
{%- endfor %}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "1000000.59"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "10.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": "25.00"
      },
      {
        "compare_at_price": "400.00"
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
      },
      {
        "compare_at_price": null
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

20

21

22

23

24

25

26

27

28

Original prices:

-

-

-

-

- 100000059

-

-

-

- 1000

-

- 2500

- 40000

-

-

-

-

-

-

-

Original prices - compacted:

- 100000059

- 1000

- 2500

- 40000

##### Output

```liquid
Original prices:

- 
- 
- 
- 
- 100000059
- 
- 
- 
- 1000
- 
- 2500
- 40000
- 
- 
- 
- 
- 
- 
- 

Original prices - compacted:

- 100000059
- 1000
- 2500
- 40000
```

Was this page helpful?

YesNo