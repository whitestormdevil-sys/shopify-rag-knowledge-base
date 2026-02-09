---
source: https://shopify.dev/docs/api/liquid/tags/decrement
---

Creates a new variable, with a default value of -1, that's decreased by 1 with each subsequent call.

---

Caution

Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.

**Caution:**

Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.

**Caution:** Predefined Liquid objects can be overridden by variables with the same name.
To make sure that you can access all Liquid objects, make sure that your variable name doesn&#39;t match a predefined object&#39;s name.

---

Variables that are declared with `decrement` are unique to the [layout](/themes/architecture/layouts), [template](/themes/architecture/templates),
or [section](/themes/architecture/sections) file that they're created in. However, the variable is shared across
[snippets](/themes/architecture/snippets) included in the file.

Similarly, variables that are created with `decrement` are independent from those created with [`assign`](/docs/api/liquid/tags/assign)
and [`capture`](/docs/api/liquid/tags/capture). However, `decrement` and [`increment`](/docs/api/liquid/tags/increment) share
variables.

## Syntax

9

1

{% decrement variable\_name %}

variable\_name

The name of the variable being decremented.

9

1

2

3

{% decrement variable %}

{% decrement variable %}

{% decrement variable %}

##### Code

```liquid
{% decrement variable %}
{% decrement variable %}
{% decrement variable %}
```

## Output

9

1

2

3

-1

-2

-3

##### Output

```liquid
-1
-2
-3
```

Was this page helpful?

YesNo