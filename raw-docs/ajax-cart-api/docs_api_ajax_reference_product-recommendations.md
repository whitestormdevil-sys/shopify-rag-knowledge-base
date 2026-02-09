---
source: https://shopify.dev/docs/api/ajax/reference/product-recommendations
---

The Product Recommendations API can be used to recommend related products for a given product. To learn more about how recommendations are made and the associated limitations, refer to [Product recommendations](/docs/storefronts/themes/product-merchandising/recommendations).

To learn how to show product recommendations in your theme, refer to [Product recommendations](/docs/storefronts/themes/product-merchandising/recommendations).

All Ajax API requests should use [locale-aware URLs](/docs/api/ajax#locale-aware-urls) to give visitors a consistent experience.

Note

The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables users to customize product recommendation and search results, which can impact results from [storefront search](/docs/storefronts/themes/navigation-search/search) and the Ajax Product Recommendations API. To learn about how these results can be impacted, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations).

**Note:**

The [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) enables users to customize product recommendation and search results, which can impact results from [storefront search](/docs/storefronts/themes/navigation-search/search) and the Ajax Product Recommendations API. To learn about how these results can be impacted, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations).

---

## [Anchor to GET /{locale}/recommendations/products.json](/docs/api/ajax/reference/product-recommendations#get--locale-recommendations-productsjson)GET /{locale}/recommendations/products.json

The following example request retrieves the recommended products for a specific product:

9

1

GET /{locale}/recommendations/products.json?product\_id={product-id}&intent={intent}

### [Anchor to Query parameters](/docs/api/ajax/reference/product-recommendations#query-parameters)Query parameters

| Query parameter | Required | Description |
| --- | --- | --- |
| `product_id` | Yes | The unique [product ID](/docs/api/liquid/objects/product#product-id) of the product that you want to show recommended products for. |
| `limit` | No | Limits the number of results.  The value can range from `1` to `10`, and the default is `10`. |
| `intent` | No | The recommendation intent that is used to generate product recommendations. You can use `intent` to generate product recommendations on various pages across the online store, according to different strategies. [Learn more about recommendation intents](/docs/storefronts/themes/product-merchandising/recommendations).  The accepted values are `related` and `complementary`. The default value is `related`. |

9

1

2

3

4

5

{

"product\_id": "1234567890123",

"limit": 4,

"intent": "related"

}

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

12

fetch(window.Shopify.routes.root + "recommendations/products.json?product\_id=1234567890123&limit=4&intent=related")

.then(response => response.json())

.then(({ products }) => {

if (products.length > 0) {

const firstRecommendedProduct = products[0];

alert(

`The title of the first recommended product is: ${firstRecommendedProduct.title}`

);

}

}

);

### [Anchor to Products response](/docs/api/ajax/reference/product-recommendations#products-response)Products response

The following example is a response to a successful request to the `/{locale}/recommendations/products.json` endpoint:

999

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

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

{

"intent": "related",

"products": [

{

"id": 35,

"title": "Gorgeous Silk Coat",

"handle": "gorgeous-silk-coat",

"description": null,

"published\_at": "2019-02-26T11:34:58-05:00",

"created\_at": "2019-02-26T11:34:58-05:00",

"vendor": "Marge Group",

"type": "Outdoors",

"tags": [],

"price": 380000,

"price\_min": 380000,

"price\_max": 790000,

"available": true,

"price\_varies": true,

"compare\_at\_price": null,

"compare\_at\_price\_min": 0,

"compare\_at\_price\_max": 0,

"compare\_at\_price\_varies": false,

"variants": [

{

"id": 69,

"title": "Small Aluminum Knife",

"option1": "Small Aluminum Knife",

"option2": null,

"option3": null,

"sku": "",

"requires\_shipping": true,

"taxable": true,

"featured\_image": null,

"available": true,

"name": "Gorgeous Silk Coat - Small Aluminum Knife",

"public\_title": "Small Aluminum Knife",

### [Anchor to Error responses](/docs/api/ajax/reference/product-recommendations#error-responses)Error responses

When a request to the `/{locale}/recommendations/products.json` endpoint is unsuccessful, one of the following error responses is returned:

* [Invalid parameter](#invalid-parameter)
* [Product not found](#product-not-found)

#### [Anchor to Invalid parameter](/docs/api/ajax/reference/product-recommendations#invalid-parameter)Invalid parameter

In the absence of a `product_id` parameter, the endpoint returns the following error:

9

1

2

3

4

5

{

"status": 422,

"message": "Invalid parameter error",

"description": "A product\_id value is missing"

}

If `intent` isn't one of `related` or `complementary`, then the endpoint returns the following error:

9

1

2

3

4

5

{

"status": 422,

"message": "Invalid parameter error",

"description": "The intent parameter must be one of related, complementary"

}

#### [Anchor to Product not found](/docs/api/ajax/reference/product-recommendations#product-not-found)Product not found

If the `product_id` is for a product that doesn't exist, or that isn't published in the **Online store** channel, then the endpoint returns the following error:

9

1

2

3

4

5

{

"status": 404,

"message": "Product not found",

"description": "No product with id <product\_id> is published in the online store"

}

---

## [Anchor to GET /{locale}/recommendations/products](/docs/api/ajax/reference/product-recommendations#get--locale-recommendations-products)GET /{locale}/recommendations/products

The following example request retrieves the HTML from a section rendered with product recommendations for a specific product.

9

1

GET /{locale}/recommendations/products?product\_id={product-id}&section\_id=product-recommendations

### [Anchor to Query parameters](/docs/api/ajax/reference/product-recommendations#query-parameters)Query parameters

| Query parameter | Required | Description |
| --- | --- | --- |
| `product_id` | Yes | The unique [product ID](/docs/api/liquid/objects/product#product-id) of the product that you want to show recommended products for. |
| `limit` | No | Limits the number of results.  The value can range from `1` to `10`, and the default is `10`. |
| `section_id` | Yes | The unique [section ID](/docs/api/ajax/section-rendering#find-section-ids) of the section file that you want to render with product recommendations. |
| `intent` | No | The recommendation intent that is used to generate product recommendations. You can use `intent` to generate product recommendations on various pages across the online store, according to different strategies. [Learn more about recommendation intents](/docs/storefronts/themes/product-merchandising/recommendations#recommendation-intents).  The following values are accepted: `related`, `complementary`. The default value is `related`. |

9

1

2

3

4

5

6

{

"product\_id": "1234567890123",

"limit": 4,

"section\_id": "product-recommendations",

"intent": "related"

}

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

12

13

const productRecommendationsSection = document.querySelector('.product-recommendations');

fetch(window.Shopify.routes.root + "recommendations/products?product\_id=12345690123&limit=4&section\_id=product-recommendations&intent=related")

.then(response => response.text())

.then((text) => {

const html = document.createElement('div');

html.innerHTML = text;

const recommendations = html.querySelector('.product-recommendations');

if (recommendations && recommendations.innerHTML.trim().length) {

productRecommendationsSection.innerHTML = recommendations.innerHTML;

}

});

### [Anchor to Section response](/docs/api/ajax/reference/product-recommendations#section-response)Section response

The response to a successful request to the `/{locale}/recommendations/products` endpoint.

The section response contains the HTML of the provided section rendered with the [`recommendations` object](/docs/api/liquid/objects/recommendations) containing the recommended products for the specified product.

For example, the following section would generate the following section response:

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

12

13

14

15

16

17

18

19

20

21

22

{%- if recommendations.performed? -%}

<div id="product-recommendations">

{%- if recommendations.products\_count > 0 -%}

{% if recommendations.intent == 'related' %}

<h2>You may also like</h2>

{% elsif recommendations.intent == 'complementary' %}

<h2>Pair it with</h2>

{% endif %}

<ul>

{%- for product in recommendations.products -%}

<li className="grid\_\_item small--one-half medium-up--one-quarter">

<a href="{{ product.url }}">

<span>{{ product.title }}</span>

<span>{{ product.price | money }}</span>

</a>

</li>

{%- endfor -%}

</ul>

{%- endif -%}

</div>

{%- endif -%}

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

12

13

<div id="product-recommendations">

<h2>You may also like</h2>

<ul>

<li className="grid\_\_item small--one-half medium-up--one-quarter">

<a href="/products/gorgeous-silk-coat?pr\_choice=default&pr\_prod\_strat=copurchase&pr\_rec\_pid=35&pr\_ref\_pid=17&pr\_seq=alternating">

<span>Gorgeous Silk Coat</span>

<span>$380.00</span>

</a>

</li>

...

</ul>

</div>

### [Anchor to Error responses](/docs/api/ajax/reference/product-recommendations#error-responses)Error responses

When a request to the `/{locale}/recommendations/products` endpoint is unsuccessful, one of the following error status codes is returned:

| Status code | Description |
| --- | --- |
| `404` | * **Product not found** - The provided product ID doesn't exist, or doesn't belong to a product published on the **Online store** channel. * **Section not found** - The provided section ID wasn't found in the theme. |
| `422` | * **Invalid parameter error** - The `product_id` query parameter was missing. * **Invalid parameter error** - The `intent` parameter must be one of `related`, `complementary`. |

---

## [Anchor to Tracking conversions for product recommendations](/docs/api/ajax/reference/product-recommendations#tracking-conversions-for-product-recommendations)Tracking conversions for product recommendations

The `url` property for each `product` in the [products response](#products-response) contains URL parameters that lets you build a conversion funnel that can be tracked by using reports in Shopify. Similarly, the Liquid `url` property returned for [`recommendations.products`](/docs/api/liquid/objects/recommendations#recommendations-products) contains this tracking information as well. The URL uses the following format:

9

1

/products/gorgeous-wooden-computer?pr\_choice=default&pr\_prod\_strat=description&pr\_rec\_pid=13&pr\_ref\_pid=17&pr\_seq=alternating

To learn more about product recommendation reports, see [Product recommendation conversion over time](https://help.shopify.com/manual/reports-and-analytics/shopify-reports/report-types/behaviour-reports#product-recommendation-conversions-over-time).

---

Was this page helpful?

YesNo