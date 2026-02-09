---
source: https://shopify.dev/docs/api/liquid/filters/remove_first
---

9

1

string | remove\_first: string

returns [string](/docs/api/liquid/basics#string)

Removes the first instance of a substring inside a string.

9

1

{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove\_first: ' accidentally' }}

##### Code

```liquid
{{ "I hate it when I accidentally spill my duplication potion accidentally!" | remove_first: ' accidentally' }}
```

## Output

9

1

I hate it when I spill my duplication potion accidentally!

##### Output

```liquid
I hate it when I spill my duplication potion accidentally!
```

Was this page helpful?

YesNo