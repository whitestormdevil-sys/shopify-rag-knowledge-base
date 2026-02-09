---
source: https://shopify.dev/docs/api/liquid/filters/uniq
---

9

1

array | uniq

Removes any duplicate items in an array.

9

1

2

3

{% assign potion\_array = 'invisibility, health, love, health, invisibility' | split: ', ' %}

{{ potion\_array | uniq | join: ', ' }}

##### Code

```liquid
{% assign potion_array = 'invisibility, health, love, health, invisibility' | split: ', ' %}

{{ potion_array | uniq | join: ', ' }}
```

## Output

9

1

invisibility, health, love

##### Output

```liquid
invisibility, health, love
```

Was this page helpful?

YesNo