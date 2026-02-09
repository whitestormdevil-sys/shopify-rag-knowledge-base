---
source: https://shopify.dev/docs/api/liquid/tags/tablerow
---

Generates HTML table rows for every item in an array.

The `tablerow` tag must be wrapped in HTML `<table>` and `</table>` tags.

---

Tip

Every `tablerow` loop has an associated [`tablerowloop` object](/docs/api/liquid/objects/tablerowloop) with information about the loop.

**Tip:**

Every `tablerow` loop has an associated [`tablerowloop` object](/docs/api/liquid/objects/tablerowloop) with information about the loop.

**Tip:** Every <code>tablerow</code> loop has an associated <a href="/docs/api/liquid/objects/tablerowloop"><code>tablerowloop</code> object</a> with information about the loop.

---

## Syntax

9

1

2

3

{% tablerow variable in array %}

expression

{% endtablerow %}

variable

The current item in the array.

array

The array to iterate over.

expression

The expression to render.

9

1

2

3

4

5

<table>

{% tablerow product in collection.products %}

{{ product.title }}

{% endtablerow %}

</table>

##### Code

```liquid
<table>
  {% tablerow product in collection.products %}
    {{ product.title }}
  {% endtablerow %}
</table>
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

<table>

<tr class="row1">

<td class="col1">

Draught of Immortality

</td><td class="col2">

Glacier ice

</td><td class="col3">

Health potion

</td><td class="col4">

Invisibility potion

</td></tr>

</table>

##### Output

```liquid
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td><td class="col3">
    Health potion
  </td><td class="col4">
    Invisibility potion
  </td></tr>

</table>
```

[Anchor to tablerow](/docs/api/liquid/tags/tablerow#tablerow-parameters)

## tablerow tag parameters

[Anchor to cols](/docs/api/liquid/tags/tablerow#tablerow-cols)

### cols

## Syntax

9

1

2

3

4

{% tablerow variable in array cols: number %}

expression

{% endtablerow %}

You can define how many columns the table should have using the `cols` parameter.

9

1

2

3

4

5

<table>

{% tablerow product in collection.products cols: 2 %}

{{ product.title }}

{% endtablerow %}

</table>

##### Code

```liquid
<table>
  {% tablerow product in collection.products cols: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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

<table>

<tr class="row1">

<td class="col1">

Draught of Immortality

</td><td class="col2">

Glacier ice

</td></tr>

<tr class="row2"><td class="col1">

Health potion

</td><td class="col2">

Invisibility potion

</td></tr>

</table>

##### Output

```liquid
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>
<tr class="row2"><td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

[Anchor to limit](/docs/api/liquid/tags/tablerow#tablerow-limit)

### limit

## Syntax

9

1

2

3

4

{% tablerow variable in array limit: number %}

expression

{% endtablerow %}

You can limit the number of iterations using the `limit` parameter.

9

1

2

3

4

5

<table>

{% tablerow product in collection.products limit: 2 %}

{{ product.title }}

{% endtablerow %}

</table>

##### Code

```liquid
<table>
  {% tablerow product in collection.products limit: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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

6

7

8

9

<table>

<tr class="row1">

<td class="col1">

Draught of Immortality

</td><td class="col2">

Glacier ice

</td></tr>

</table>

##### Output

```liquid
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>

</table>
```

[Anchor to offset](/docs/api/liquid/tags/tablerow#tablerow-offset)

### offset

## Syntax

9

1

2

3

4

{% tablerow variable in array offset: number %}

expression

{% endtablerow %}

You can specify a 1-based index to start iterating at using the `offset` parameter.

9

1

2

3

4

5

<table>

{% tablerow product in collection.products offset: 2 %}

{{ product.title }}

{% endtablerow %}

</table>

##### Code

```liquid
<table>
  {% tablerow product in collection.products offset: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
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

6

7

8

9

<table>

<tr class="row1">

<td class="col1">

Health potion

</td><td class="col2">

Invisibility potion

</td></tr>

</table>

##### Output

```liquid
<table>
  <tr class="row1">
<td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

[Anchor to range](/docs/api/liquid/tags/tablerow#tablerow-range)

### range

## Syntax

9

1

2

3

4

{% tablerow variable in (number..number) %}

expression

{% endtablerow %}

Instead of iterating over specific items in an array, you can specify a numeric range to iterate over.

---

Note

You can define the range using both literal and variable values.

**Note:**

You can define the range using both literal and variable values.

**Note:** You can define the range using both literal and variable values.

---

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

<table>

{% tablerow i in (1..3) %}

{{ i }}

{% endtablerow %}

</table>

{%- assign lower\_limit = 2 -%}

{%- assign upper\_limit = 4 -%}

<table>

{% tablerow i in (lower\_limit..upper\_limit) %}

{{ i }}

{% endtablerow %}

</table>

##### Code

```liquid
<table>
  {% tablerow i in (1..3) %}
    {{ i }}
  {% endtablerow %}
</table>

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

<table>
  {% tablerow i in (lower_limit..upper_limit) %}
    {{ i }}
  {% endtablerow %}
</table>
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

<table>

<tr class="row1">

<td class="col1">

1

</td><td class="col2">

2

</td><td class="col3">

3

</td></tr>

</table><table>

<tr class="row1">

<td class="col1">

2

</td><td class="col2">

3

</td><td class="col3">

4

</td></tr>

</table>

##### Output

```liquid
<table>
  <tr class="row1">
<td class="col1">
    1
  </td><td class="col2">
    2
  </td><td class="col3">
    3
  </td></tr>

</table><table>
  <tr class="row1">
<td class="col1">
    2
  </td><td class="col2">
    3
  </td><td class="col3">
    4
  </td></tr>

</table>
```

Information about a parent [`tablerow` loop](/docs/api/liquid/tags/tablerow).

## Properties

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-col) 

col**col** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current column.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-col_first) 

col\_first**col\_first** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current column is the first in the row. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-col_last) 

col\_last**col\_last** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current column is the last in the row. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-col0) 

col0**col0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current column.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-first) 

first**first** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the first. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-index) 

index**index** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-index0) 

index0**index0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current iteration.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-last) 

last**last** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the last. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-length) 

length**length** [number](/docs/api/liquid/basics#number)

:   The total number of iterations in the loop.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-rindex) 

rindex**rindex** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration, in reverse order.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-rindex0) 

rindex0**rindex0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current iteration, in reverse order.

[Anchor to](/docs/api/liquid/tags/tablerow#tablerowloop-row) 

row**row** [number](/docs/api/liquid/basics#number)

:   The 1-based index of current row.

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

{

"col": 1,

"col0": 0,

"col\_first": true,

"col\_last": false,

"first": true,

"index": 1,

"index0": 0,

"last": false,

"length": 5,

"rindex": 5,

"rindex0": 4,

"row": 1

}

##### Example

```liquid
{
  "col": 1,
  "col0": 0,
  "col_first": true,
  "col_last": false,
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 5,
  "rindex": 5,
  "rindex0": 4,
  "row": 1
}
```

Was this page helpful?

YesNo