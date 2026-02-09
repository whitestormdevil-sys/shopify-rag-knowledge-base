---
source: https://shopify.dev/docs/api/liquid/filters/rstrip
---

9

1

string | rstrip

returns [string](/docs/api/liquid/basics#string)

Strips all whitespace from the right of a string.

9

1

2

3

4

{%- assign text = ' Some potions create whitespace. ' -%}

"{{ text }}"

"{{ text | rstrip }}"

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | rstrip }}"
```

## Output

9

1

2

" Some potions create whitespace. "

" Some potions create whitespace."

##### Output

```liquid
"  Some potions create whitespace.      "
"  Some potions create whitespace."
```

Was this page helpful?

YesNo