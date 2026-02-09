---
source: https://shopify.dev/docs/api/liquid/filters/escape_once
---

9

1

string | escape\_once

returns [string](/docs/api/liquid/basics#string)

Escapes a string without changing characters that have already been escaped.

99

1

2

3

4

5

6

7

8

9

10

11

# applying the escape filter to already escaped text escapes characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape }}

# applying the escape\_once filter to already escaped text skips characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape\_once }}

# use escape\_once to escape strings where a combination of HTML entities and non-escaped characters might be present:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt; & some additional text" | escape\_once }}

##### Code

```liquid
# applying the escape filter to already escaped text escapes characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape }}

# applying the escape_once filter to already escaped text skips characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape_once }}

# use escape_once to escape strings where a combination of HTML entities and non-escaped characters might be present:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt; & some additional text" | escape_once }}
```

##### Data

## Output

9

1

##### Output

Was this page helpful?

YesNo