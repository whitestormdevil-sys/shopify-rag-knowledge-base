---
source: https://shopify.dev/docs/api/liquid/filters/url_decode
---

9

1

string | url\_decode

returns [string](/docs/api/liquid/basics#string)

Decodes any [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) characters
in a string.

9

1

{{ 'test%40test.com' | url\_decode }}

##### Code

```liquid
{{ 'test%40test.com' | url_decode }}
```

## Output

9

1

test@test.com

##### Output

```liquid
test@test.com
```

Was this page helpful?

YesNo