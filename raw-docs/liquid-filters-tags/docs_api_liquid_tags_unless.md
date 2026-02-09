---
source: https://shopify.dev/docs/api/liquid/tags/unless
---

Renders an expression unless a specific condition is `true`.

---

Tip

Similar to the [`if` tag](/docs/api/liquid/tags/if), you can use `elsif` to add more conditions to an `unless` tag.

**Tip:**

Similar to the [`if` tag](/docs/api/liquid/tags/if), you can use `elsif` to add more conditions to an `unless` tag.

**Tip:** Similar to the <a href="/docs/api/liquid/tags/if"><code>if</code> tag</a>, you can use <code>elsif</code> to add more conditions to an <code>unless</code> tag.

---

## Syntax

9

1

2

3

{% unless condition %}

expression

{% endunless %}

condition

The condition to evaluate.

expression

The expression to render unless the condition is met.

9

1

2

3

{% unless product.has\_only\_default\_variant %}

// Variant selection functionality

{% endunless %}

##### Code

```liquid
{% unless product.has_only_default_variant %}
  // Variant selection functionality
{% endunless %}
```

##### Data

```liquid
{
  "product": {
    "has_only_default_variant": false
  }
}
```

## Output

9

1

// Variant selection functionality

##### Output

```liquid
// Variant selection functionality
```

Was this page helpful?

YesNo