---
source: https://shopify.dev/docs/api/liquid/filters/strip
---

9

1

string | strip

returns [string](/docs/api/liquid/basics#string)

Strips all whitespace from the left and right of a string.

9

1

2

3

4

{%- assign text = ' Some potions create whitespace. ' -%}

"{{ text }}"

"{{ text | strip }}"

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | strip }}"
```

## Output

9

1

2

" Some potions create whitespace. "

"Some potions create whitespace."

##### Output

```liquid
"  Some potions create whitespace.      "
"Some potions create whitespace."
```

Was this page helpful?

YesNo