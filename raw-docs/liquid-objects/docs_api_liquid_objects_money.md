---
source: https://shopify.dev/docs/api/liquid/objects/money
---

A money value, in the the customer's local (presentment) currency.

---

Tip

Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

**Tip:**

Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

**Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

---

## Properties

[Anchor to](/docs/api/liquid/objects/money#money-currency) 

currency**currency** [currency](/docs/api/liquid/objects/currency)

:   The customer's local (presentment) currency.

9

1

2

3

{

"currency": {}

}

##### Example

```liquid
{
  "currency": {}
}
```

[Anchor to Referencing money objects directly](/docs/api/liquid/objects/money#money-referencing-money-objects-directly)

### Referencing money objects directly

When a money object is referenced directly, the money value in cents is returned.

9

1

{{ product.metafields.details.price\_per\_100g.value }}

##### Code

```liquid
{{ product.metafields.details.price_per_100g.value }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

1796

##### Output

```liquid
1796
```

Was this section helpful?

YesNo