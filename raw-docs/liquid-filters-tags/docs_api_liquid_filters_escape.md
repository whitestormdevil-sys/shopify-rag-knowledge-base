---
source: https://shopify.dev/docs/api/liquid/filters/escape
---

9

1

string | escape

returns [string](/docs/api/liquid/basics#string)

Escapes special characters in HTML, such as `<>`, `'`, and `&`, and converts characters into escape sequences. The filter doesn't effect characters within the string that don’t have a corresponding escape sequence.".

9

1

{{ '<p>Text to be escaped.</p>' | escape }}

##### Code

```liquid
{{ '<p>Text to be escaped.</p>' | escape }}
```

## Output

9

1

&lt;p&gt;Text to be escaped.&lt;/p&gt;

##### Output

```liquid
&lt;p&gt;Text to be escaped.&lt;/p&gt;
```

Was this page helpful?

YesNo