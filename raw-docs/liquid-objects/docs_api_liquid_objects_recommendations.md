---
source: https://shopify.dev/docs/api/liquid/objects/recommendations
---

Product recommendations for a specific product based on sales data, product descriptions, and collection relationships.

Product recommendations become more accurate over time as new orders and product data become available. To learn more about
how product recommendations are generated, refer to [Product recommendations](/themes/product-merchandising/recommendations).

---

Note

The `recommendations` object returns products only when rendered in a section using the [Product Recommendations API](/api/ajax/reference/product-recommendations)
and the [Section Rendering API](/api/section-rendering). To learn about how to include product recommendations in your theme,
refer to [Show product recommendations](/themes/product-merchandising/recommendations/show-product-recommendations).

**Note:**

The `recommendations` object returns products only when rendered in a section using the [Product Recommendations API](/api/ajax/reference/product-recommendations)
and the [Section Rendering API](/api/section-rendering). To learn about how to include product recommendations in your theme,
refer to [Show product recommendations](/themes/product-merchandising/recommendations/show-product-recommendations).

**Note:** The <code>recommendations</code> object returns products only when rendered in a section using the <a href="/api/ajax/reference/product-recommendations">Product Recommendations API</a>
and the <a href="/api/section-rendering">Section Rendering API</a>. To learn about how to include product recommendations in your theme,
refer to <a href="/themes/product-merchandising/recommendations/show-product-recommendations">Show product recommendations</a>.

---

## Properties

[Anchor to](/docs/api/liquid/objects/recommendations#recommendations-intent) 

intent**intent** [string](/docs/api/liquid/basics#string)

:   The recommendation intent.

    If `performed?` is `false`, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/recommendations#recommendations-performed?) 

performed?**performed?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` when being referenced inside a section that's been rendered using the Product Recommendations API and
    the Section Rendering API. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/recommendations#recommendations-products) 

products**products** array of [product](/docs/api/liquid/objects/product)

:   The recommended products.

    If `performed?` is `false`, then an [EmptyDrop](/docs/api/liquid/basics#emptydrop) is returned.

[Anchor to](/docs/api/liquid/objects/recommendations#recommendations-products_count) 

products\_count**products\_count** [number](/docs/api/liquid/basics#number)

:   The number of recommended products.

    If `performed?` is `false`, then 0 is returned.

9

1

2

3

4

5

{

"products": [],

"products\_count": 4,

"performed?": true

}

##### Example

```liquid
{
  "products": [],
  "products_count": 4,
  "performed?": true
}
```

Was this section helpful?

YesNo