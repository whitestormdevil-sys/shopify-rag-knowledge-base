---
source: https://shopify.dev/docs/api/liquid/filters/at_least
---

9

1

number | at\_least

returns [number](/docs/api/liquid/basics#number)

Limits a number to a minimum value.

9

1

2

{{ 4 | at\_least: 5 }}

{{ 4 | at\_least: 3 }}

##### Code

```liquid
{{ 4 | at_least: 5 }}
{{ 4 | at_least: 3 }}
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