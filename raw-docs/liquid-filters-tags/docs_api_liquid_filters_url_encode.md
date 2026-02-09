---
source: https://shopify.dev/docs/api/liquid/filters/url_encode
---

9

1

string | url\_encode

returns [string](/docs/api/liquid/basics#string)

Converts any URL-unsafe characters in a string to the
[percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) equivalent.

---

Note

Spaces are converted to a `+` character, instead of a percent-encoded character.

**Note:**

Spaces are converted to a `+` character, instead of a percent-encoded character.

**Note:** Spaces are converted to a <code>+</code> character, instead of a percent-encoded character.

---

9

1

{{ 'test@test.com' | url\_encode }}

##### Code

```liquid
{{ 'test@test.com' | url_encode }}
```

## Output

9

1

test%40test.com

##### Output

```liquid
test%40test.com
```

Was this page helpful?

YesNo