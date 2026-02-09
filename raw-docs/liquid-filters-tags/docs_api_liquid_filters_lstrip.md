---
source: https://shopify.dev/docs/api/liquid/filters/lstrip
---

9

1

string | lstrip

returns [string](/docs/api/liquid/basics#string)

Strips all whitespace from the left of a string.

9

1

2

3

4

{%- assign text = ' Some potions create whitespace. ' -%}

"{{ text }}"

"{{ text | lstrip }}"

##### Code

```liquid
{%- assign text = '  Some potions create whitespace.      ' -%}

"{{ text }}"
"{{ text | lstrip }}"
```

## Output

9

1

2

" Some potions create whitespace. "

"Some potions create whitespace. "

##### Output

```liquid
"  Some potions create whitespace.      "
"Some potions create whitespace.      "
```

Was this page helpful?

YesNo