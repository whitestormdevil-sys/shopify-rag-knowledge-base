---
source: https://shopify.dev/docs/api/liquid/filters/round
---

9

1

number | round

returns [number](/docs/api/liquid/basics#number)

Rounds a number to the nearest integer.

9

1

2

{{ 2.7 | round }}

{{ 1.3 | round }}

##### Code

```liquid
{{ 2.7 | round }}
{{ 1.3 | round }}
```

## Output

9

1

2

3

1

##### Output

```liquid
3
1
```

[Anchor to Round to a specific number of decimal places](/docs/api/liquid/filters/round#round-round-to-a-specific-number-of-decimal-places)

### Round to a specific number of decimal places

You can specify a number of decimal places to round to. If you don't specify a number, then the `round` filter rounds to the nearest integer.

9

1

{{ 3.14159 | round: 2 }}

##### Code

```liquid
{{ 3.14159 | round: 2 }}
```

## Output

9

1

3.14

##### Output

```liquid
3.14
```

Was this page helpful?

YesNo