---
source: https://shopify.dev/docs/api/liquid/tags/echo
---

Outputs an expression.

Using the `echo` tag is the same as wrapping an expression in curly brackets (`{{` and `}}`). However, unlike the curly
bracket method, you can use the `echo` tag inside [`liquid` tags](/docs/api/liquid/tags/liquid).

---

Tip

You can use [filters](/docs/api/liquid/filters) on expressions inside `echo` tags.

**Tip:**

You can use [filters](/docs/api/liquid/filters) on expressions inside `echo` tags.

**Tip:** You can use <a href="/docs/api/liquid/filters">filters</a> on expressions inside <code>echo</code> tags.

---

## Syntax

9

1

2

3

{% liquid

echo expression

%}

expression

The expression to be output.

9

1

2

3

4

5

{% echo product.title %}

{% liquid

echo product.price | money

%}

##### Code

```liquid
{% echo product.title %}

{% liquid
  echo product.price | money
%}
```

##### Data

```liquid
{
  "product": {
    "price": "10.00",
    "title": "Health potion"
  }
}
```

## Output

9

1

2

3

Health potion

$10.00

##### Output

```liquid
Health potion

$10.00
```

Was this page helpful?

YesNo