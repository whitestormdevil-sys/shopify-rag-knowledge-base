---
source: https://shopify.dev/docs/api/liquid/tags/raw
---

Outputs any Liquid code as text instead of rendering it.

## Syntax

9

1

2

3

{% raw %}

expression

{% endraw %}

expression

The expression to be output without being rendered.

9

1

2

3

{% raw %}

{{ 2 | plus: 2 }} equals 4.

{% endraw %}

##### Code

```liquid
{% raw %}
{{ 2 | plus: 2 }} equals 4.
{% endraw %}
```

## Output

9

1

{{ 2 | plus: 2 }} equals 4.

##### Output

```liquid
{{ 2 | plus: 2 }} equals 4.
```

Was this page helpful?

YesNo