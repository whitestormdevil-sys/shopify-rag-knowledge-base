---
source: https://shopify.dev/docs/api/liquid/filters/divided_by
---

9

1

number | divided\_by: number

returns [number](/docs/api/liquid/basics#number)

Divides a number by a given number. The `divided_by` filter produces a result of the same type as the divisor. This means if you divide by an integer, the result will be an integer, and if you divide by a float, the result will be a float.

9

1

2

3

4

5

6

7

{{ 4 | divided\_by: 2 }}

# divisor is an integer

{{ 20 | divided\_by: 7 }}

# divisor is a float

{{ 20 | divided\_by: 7.0 }}

##### Code

```liquid
{{ 4 | divided_by: 2 }}

# divisor is an integer
{{ 20 | divided_by: 7 }}

# divisor is a float 
{{ 20 | divided_by: 7.0 }}
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

2

# divisor is an integer

2

# divisor is a float

2.857142857142857

##### Output

```liquid
2

# divisor is an integer
2

# divisor is a float 
2.857142857142857
```

Was this page helpful?

YesNo