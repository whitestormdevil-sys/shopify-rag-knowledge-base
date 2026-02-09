---
source: https://shopify.dev/docs/api/liquid/filters/within
---

9

1

string | within: collection

returns [string](/docs/api/liquid/basics#string)

Generates a product URL within the context of the provided collection.

When the collection context is included, you can access the associated [`collection` object](/docs/api/liquid/objects/collection)
in the [product template](/themes/architecture/templates/product).

---

Caution

Because a standard product page and a product page in the context of a collection have the same content on separate
URLs, you should consider the SEO implications of using the `within` filter.

**Caution:**

Because a standard product page and a product page in the context of a collection have the same content on separate
URLs, you should consider the SEO implications of using the `within` filter.

**Caution:** Because a standard product page and a product page in the context of a collection have the same content on separate
URLs, you should consider the SEO implications of using the <code>within</code> filter.

---

9

1

2

3

{%- assign collection\_product = collection.products.first -%}

{{ collection\_product.url | within: collection }}

##### Code

```liquid
{%- assign collection_product = collection.products.first -%}

{{ collection_product.url | within: collection }}
```

##### Data

```liquid
{
  "collection": {
    "products": [
      {
        "url": "/products/draught-of-immortality"
      },
      {
        "url": "/products/glacier-ice"
      },
      {
        "url": "/products/health-potion"
      },
      {
        "url": "/products/invisibility-potion"
      }
    ]
  }
}
```

## Output

9

1

/collections/sale-potions/products/draught-of-immortality

##### Output

```liquid
/collections/sale-potions/products/draught-of-immortality
```

Was this page helpful?

YesNo