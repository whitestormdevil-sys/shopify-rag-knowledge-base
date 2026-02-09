---
source: https://shopify.dev/docs/api/liquid/tags/for
---

Renders an expression for every item in an array.

You can do a maximum of 50 iterations with a `for` loop. If you need to iterate over more than 50 items, then use the
[`paginate` tag](/docs/api/liquid/tags/paginate) to split the items over multiple pages.

---

Tip

Every `for` loop has an associated [`forloop` object](/docs/api/liquid/objects/forloop) with information about the loop.

**Tip:**

Every `for` loop has an associated [`forloop` object](/docs/api/liquid/objects/forloop) with information about the loop.

**Tip:** Every <code>for</code> loop has an associated <a href="/docs/api/liquid/objects/forloop"><code>forloop</code> object</a> with information about the loop.

---

## Syntax

9

1

2

3

{% for variable in array %}

expression

{% endfor %}

variable

The current item in the array.

array

The array to iterate over.

expression

The expression to render for each iteration.

9

1

2

3

{% for product in collection.products -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% for product in collection.products -%}
  {{ product.title }}
{%- endfor %}
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

Draught of Immortality

Glacier ice

Health potion

Invisibility potion

##### Output

```liquid
Draught of Immortality
Glacier ice
Health potion
Invisibility potion
```

[Anchor to for](/docs/api/liquid/tags/for#for-parameters)

## for tag parameters

[Anchor to limit](/docs/api/liquid/tags/for#for-limit)

### limit

## Syntax

9

1

2

3

4

{% for variable in array limit: number %}

expression

{% endfor %}

You can limit the number of iterations using the `limit`
parameter.

---

Tip

Limit the amount of data fetched for arrays that can be paginated with the `paginate` tag instead of using the `limit` parameter. Learn more about [limiting data fetching](/docs/api/liquid/tags/paginate#paginate-limit-data-fetching) for improved server-side performance.

**Tip:**

Limit the amount of data fetched for arrays that can be paginated with the `paginate` tag instead of using the `limit` parameter. Learn more about [limiting data fetching](/docs/api/liquid/tags/paginate#paginate-limit-data-fetching) for improved server-side performance.

**Tip:** Limit the amount of data fetched for arrays that can be paginated with the <code>paginate</code> tag instead of using the <code>limit</code> parameter. Learn more about <a href="/docs/api/liquid/tags/paginate#paginate-limit-data-fetching">limiting data fetching</a> for improved server-side performance.

---

9

1

2

3

{% for product in collection.products limit: 2 -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% for product in collection.products limit: 2 -%}
  {{ product.title }}
{%- endfor %}
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

Draught of Immortality

Glacier ice

##### Output

```liquid
Draught of Immortality
Glacier ice
```

[Anchor to offset](/docs/api/liquid/tags/for#for-offset)

### offset

## Syntax

9

1

2

3

4

{% for variable in array offset: number %}

expression

{% endfor %}

You can specify a 1-based index to start iterating at using the `offset` parameter.

9

1

2

3

{% for product in collection.products offset: 2 -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% for product in collection.products offset: 2 -%}
  {{ product.title }}
{%- endfor %}
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

Health potion

Invisibility potion

##### Output

```liquid
Health potion
Invisibility potion
```

[Anchor to range](/docs/api/liquid/tags/for#for-range)

### range

## Syntax

9

1

2

3

4

{% for variable in (number..number) %}

expression

{% endfor %}

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

{% for i in (1..3) -%}

{{ i }}

{%- endfor %}

{%- assign lower\_limit = 2 -%}

{%- assign upper\_limit = 4 -%}

{% for i in (lower\_limit..upper\_limit) -%}

{{ i }}

{%- endfor %}

##### Code

```liquid
{% for i in (1..3) -%}
  {{ i }}
{%- endfor %}

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

{% for i in (lower_limit..upper_limit) -%}
  {{ i }}
{%- endfor %}
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

1

2

3

2

3

4

##### Output

```liquid
1
2
3

2
3
4
```

[Anchor to reversed](/docs/api/liquid/tags/for#for-reversed)

### reversed

## Syntax

9

1

2

3

4

{% for variable in array reversed %}

expression

{% endfor %}

You can iterate in reverse order using the `reversed` parameter.

9

1

2

3

{% for product in collection.products reversed -%}

{{ product.title }}

{%- endfor %}

##### Code

```liquid
{% for product in collection.products reversed -%}
  {{ product.title }}
{%- endfor %}
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

Invisibility potion

Health potion

Glacier ice

Draught of Immortality

##### Output

```liquid
Invisibility potion
Health potion
Glacier ice
Draught of Immortality
```

Information about a parent [`for` loop](/docs/api/liquid/tags/for).

## Properties

[Anchor to](/docs/api/liquid/tags/for#forloop-first) 

first**first** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the first. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/for#forloop-index) 

index**index** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration.

[Anchor to](/docs/api/liquid/tags/for#forloop-index0) 

index0**index0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current iteration.

[Anchor to](/docs/api/liquid/tags/for#forloop-last) 

last**last** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the last. Returns `false` if not.

[Anchor to](/docs/api/liquid/tags/for#forloop-length) 

length**length** [number](/docs/api/liquid/basics#number)

:   The total number of iterations in the loop.

[Anchor to](/docs/api/liquid/tags/for#forloop-parentloop) 

parentloop**parentloop** [forloop](/docs/api/liquid/objects/forloop)

:   The parent `forloop` object.

    If the current `for` loop isn't nested inside another `for` loop, then `nil` is returned.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Use the `parentloop` property

    9

    1

    2

    3

    4

    5

    {% for i in (1..3) -%}

    {% for j in (1..3) -%}

    {{ forloop.parentloop.index }} - {{ forloop.index }}

    {%- endfor %}

    {%- endfor %}

    ##### Code

    ```liquid
    {% for i in (1..3) -%}
      {% for j in (1..3) -%}
        {{ forloop.parentloop.index }} - {{ forloop.index }}
      {%- endfor %}
    {%- endfor %}
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

    1 - 1

    1 - 2

    1 - 3

    2 - 1

    2 - 2

    2 - 3

    3 - 1

    3 - 2

    3 - 3

    ##### Output

    ```liquid
    1 - 1
    1 - 2
    1 - 3

    2 - 1
    2 - 2
    2 - 3

    3 - 1
    3 - 2
    3 - 3
    ```

[Anchor to](/docs/api/liquid/tags/for#forloop-rindex) 

rindex**rindex** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration, in reverse order.

[Anchor to](/docs/api/liquid/tags/for#forloop-rindex0) 

rindex0**rindex0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current iteration, in reverse order.

9

1

2

3

4

5

6

7

8

{

"first": true,

"index": 1,

"index0": 0,

"last": false,

"length": 4,

"rindex": 3

}

##### Example

```liquid
{
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 4,
  "rindex": 3
}
```

[Anchor to Use the `forloop` object](/docs/api/liquid/tags/for#forloop-use-the-forloop-object)

### Use the `forloop` object

9

1

2

3

4

5

{% for page in pages -%}

{%- if forloop.length > 0 -%}

{{ page.title }}{% unless forloop.last %}, {% endunless -%}

{%- endif -%}

{% endfor %}

##### Code

```liquid
{% for page in pages -%}
  {%- if forloop.length > 0 -%}
    {{ page.title }}{% unless forloop.last %}, {% endunless -%}
  {%- endif -%}
{% endfor %}
```

## Output

9

1

About us, Contact, Potion dosages

##### Output

```liquid
About us, Contact, Potion dosages
```

Was this page helpful?

YesNo