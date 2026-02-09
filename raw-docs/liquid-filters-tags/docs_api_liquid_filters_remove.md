---
source: https://shopify.dev/docs/api/liquid/filters/remove
---

9

1

string | remove: string

returns [string](/docs/api/liquid/basics#string)

Removes any instance of a substring inside a string.

9

1

{{ "I can't do it!" | remove: "'t" }}

##### Code

```liquid
{{ "I can't do it!" | remove: "'t" }}
```

## Output

9

1

I can do it!

##### Output

```liquid
I can do it!
```

Was this page helpful?

YesNo