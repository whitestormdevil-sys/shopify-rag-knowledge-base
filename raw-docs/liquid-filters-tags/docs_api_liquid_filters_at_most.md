---
source: https://shopify.dev/docs/api/liquid/filters/at_most
---

9

1

number | at\_most

returns [number](/docs/api/liquid/basics#number)

Limits a number to a maximum value.

9

1

2

{{ 6 | at\_most: 5 }}

{{ 4 | at\_most: 5 }}

##### Code

```liquid
{{ 6 | at_most: 5 }}
{{ 4 | at_most: 5 }}
```

## Output

9

1

2

5

4

##### Output

```liquid
5
4
```

Was this page helpful?

YesNo