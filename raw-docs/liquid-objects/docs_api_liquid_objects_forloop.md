---
source: https://shopify.dev/docs/api/liquid/objects/forloop
---

Information about a parent [`for` loop](/docs/api/liquid/tags/for).

## Properties

[Anchor to](/docs/api/liquid/objects/forloop#forloop-first) 

first**first** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the first. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-index) 

index**index** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-index0) 

index0**index0** [number](/docs/api/liquid/basics#number)

:   The 0-based index of the current iteration.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-last) 

last**last** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current iteration is the last. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-length) 

length**length** [number](/docs/api/liquid/basics#number)

:   The total number of iterations in the loop.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-parentloop) 

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

[Anchor to](/docs/api/liquid/objects/forloop#forloop-rindex) 

rindex**rindex** [number](/docs/api/liquid/basics#number)

:   The 1-based index of the current iteration, in reverse order.

[Anchor to](/docs/api/liquid/objects/forloop#forloop-rindex0) 

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

[Anchor to Use the `forloop` object](/docs/api/liquid/objects/forloop#forloop-use-the-forloop-object)

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

Was this section helpful?

YesNo