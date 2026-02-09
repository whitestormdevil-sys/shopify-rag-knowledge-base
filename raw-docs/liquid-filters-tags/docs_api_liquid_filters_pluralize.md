---
source: https://shopify.dev/docs/api/liquid/filters/pluralize
---

9

1

number | pluralize: string, string

returns [string](/docs/api/liquid/basics#string)

Outputs the singular or plural version of a string based on a given number.

---

Caution

The `pluralize` filter applies English pluralization rules to determine which string to output. You shouldn't use this
filter on non-English strings because it could lead to incorrect pluralizations.

**Caution:**

The `pluralize` filter applies English pluralization rules to determine which string to output. You shouldn't use this
filter on non-English strings because it could lead to incorrect pluralizations.

**Caution:** The <code>pluralize</code> filter applies English pluralization rules to determine which string to output. You shouldn&#39;t use this
filter on non-English strings because it could lead to incorrect pluralizations.

---

9

1

Cart item count: {{ cart.item\_count }} {{ cart.item\_count | pluralize: 'item', 'items' }}

##### Code

```liquid
Cart item count: {{ cart.item_count }} {{ cart.item_count | pluralize: 'item', 'items' }}
```

##### Data

```liquid
{
  "cart": {
    "item_count": 2
  }
}
```

## Output

9

1

Cart item count: 2 items

##### Output

```liquid
Cart item count: 2 items
```

Was this page helpful?

YesNo