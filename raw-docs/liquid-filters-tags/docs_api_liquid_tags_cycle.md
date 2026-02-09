---
source: https://shopify.dev/docs/api/liquid/tags/cycle
---

Loops through a group of strings and outputs them one at a time for each iteration of a [`for` loop](/docs/api/liquid/tags/for).

The `cycle` tag must be used inside a `for` loop.

---

Tip

Use the `cycle` tag to output text in a predictable pattern. For example, to apply odd/even classes to rows in a table.

**Tip:**

Use the `cycle` tag to output text in a predictable pattern. For example, to apply odd/even classes to rows in a table.

**Tip:** Use the <code>cycle</code> tag to output text in a predictable pattern. For example, to apply odd/even classes to rows in a table.

---

## Syntax

9

1

{% cycle string, string, ... %}

9

1

2

3

{% for i in (1..4) -%}

{% cycle 'one', 'two', 'three' %}

{%- endfor %}

##### Code

```liquid
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}
```

## Output

9

1

2

3

4

one

two

three

one

##### Output

```liquid
one
two
three
one
```

[Anchor to Create unique cycle groups](/docs/api/liquid/tags/cycle#cycle-create-unique-cycle-groups)

### Create unique cycle groups

## Syntax

9

1

{% cycle string: string, string, ... %}

If you include multiple `cycle` tags with the same parameters, in the same template, then each set of tags is treated as the same group. This means that it's possible for a `cycle` tag to output any of the provided strings, instead of always starting at the first string.
To account for this, you can specify a group name for each `cycle` tag.

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

<!-- Iteration 1 -->

{% for i in (1..4) -%}

{% cycle 'one', 'two', 'three' %}

{%- endfor %}

<!-- Iteration 2 -->

{% for i in (1..4) -%}

{% cycle 'one', 'two', 'three' %}

{%- endfor %}

<!-- Iteration 3 -->

{% for i in (1..4) -%}

{% cycle 'group\_1': 'one', 'two', 'three' %}

{%- endfor %}

<!-- Iteration 4 -->

{% for i in (1..4) -%}

{% cycle 'group\_2': 'one', 'two', 'three' %}

{%- endfor %}

##### Code

```liquid
<!-- Iteration 1 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 2 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 3 -->
{% for i in (1..4) -%}
  {% cycle 'group_1': 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 4 -->
{% for i in (1..4) -%}
  {% cycle 'group_2': 'one', 'two', 'three' %}
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

<!-- Iteration 1 -->

one

two

three

one

<!-- Iteration 2 -->

two

three

one

two

<!-- Iteration 3 -->

one

two

three

one

<!-- Iteration 4 -->

one

two

three

one

##### Output

```liquid
<!-- Iteration 1 -->
one
two
three
one


<!-- Iteration 2 -->
two
three
one
two


<!-- Iteration 3 -->
one
two
three
one


<!-- Iteration 4 -->
one
two
three
one
```

Was this page helpful?

YesNo