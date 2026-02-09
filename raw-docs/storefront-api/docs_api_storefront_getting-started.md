---
source: https://shopify.dev/docs/api/storefront/getting-started
---

The [Storefront API](/docs/api/storefront) lets you build custom storefronts with any language and technology. It provides public access using GraphQL to products, collections, customers, carts, checkouts, and other store resources that you can use to build custom purchasing experiences. After you've [requested access tokens](/docs/storefronts/headless/building-with-the-storefront-api/getting-started) for your app and generated a Storefront API access token, you can make queries using the Storefront API.

---

## [Anchor to What you'll learn](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#what-youll-learn)What you'll learn

After you've finished this tutorial, you'll have accomplished the following:

* Requested public, unauthenticated Storefront API access scopes for your app
* Generated a Storefront API access token
* Queried products and collections

Tip

If you're a [Shopify Partner](https://help.shopify.com/en/partners/about), then you can create a [development store](/docs/api/development-stores) to test Storefront API queries.

**Tip:**

If you're a [Shopify Partner](https://help.shopify.com/en/partners/about), then you can create a [development store](/docs/api/development-stores) to test Storefront API queries.

---

## [Anchor to Requirements](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#requirements)Requirements

* You've completed the [Getting started with the Storefront API](/docs/storefronts/headless/building-with-the-storefront-api/getting-started) guide.

* If instead of completing the [Getting started](/docs/storefronts/headless/building-with-the-storefront-api/getting-started), you've created [a public or custom app](/docs/apps/launch/distribution) with Storefront API access enabled in the **Configuration** page. If you've created a public app, then you need to [turn your app into a sales channel](/docs/apps/build/sales-channels/start-building#step-2-turn-an-app-into-a-sales-channel-app).

* You've created [products](/docs/api/admin-graphql/latest/objects/product), [product variants](/docs/api/admin-graphql/latest/objects/productvariant), and [collections](/docs/api/admin-graphql/latest/objects/collection) in your store.

---

## [Anchor to Query products](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-products)Query products

You can use the [`products`](/docs/api/storefront/latest/queries/products) query to retrieve a list of products. The `products` query uses an argument (for example, `first`) to specify the number of results to query.

The following example shows how to query the IDs of the first 5 products in your store. For more information on selecting which set of results to query, refer to [Paginating results with GraphQL](/docs/api/usage/pagination-graphql).

9

1

2

3

4

5

6

7

8

9

{

products(first:5) {

edges {

node {

id

}

}

}

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

{

"data": {

"products": {

"edges": [

{

"node": {

"id": "gid:\/\/shopify\/Product\/1"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/2"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/3"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/4"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/5"

}

}

]

}

}

}

---

## [Anchor to Query a single product](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-a-single-product)Query a single product

Products are identified by a globally unique ID, which can be used to query for information. You can use the [`product`](/docs/api/storefront/latest/queries/product) query to retrieve a single product. The following example shows how to pass in the product ID to the `product` query.

9

1

2

3

4

5

6

{

# You can use `product(handle:)` to query a single product by its handle instead.

product(id: "gid:\/\/shopify\/Product\/1") {

title

}

}

9

1

2

3

4

5

6

7

{

"data": {

"product": {

"title": "Black Ban Glasses"

}

}

}

---

## [Anchor to Query product variants](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-product-variants)Query product variants

A product variant represents a different version of a product, such as differing sizes or differing colors. You can query the variants associated with a product by querying `variants` on the [`Product`](/docs/api/storefront/latest/objects/Product) object.

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

{

node(id: "gid:\/\/shopify\/Product\/1") {

id

... on Product {

variants(first: 5) {

edges {

node {

id

}

}

}

}

}

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

"data": {

"node": {

"id": "gid:\/\/shopify\/Product\/1",

"variants": {

"edges": [

{

"node": {

"id": "gid:\/\/shopify\/ProductVariant\/1"

}

},

{

"node": {

"id": "gid:\/\/shopify\/ProductVariant\/2"

}

},

{

"node": {

"id": "gid:\/\/shopify\/ProductVariant\/3"

}

},

{

"node": {

"id": "gid:\/\/shopify\/ProductVariant\/4"

}

},

{

"node": {

"id": "gid:\/\/shopify\/ProductVariant\/5"

}

}

]

}

}

}

}

---

## [Anchor to Query product recommendations](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-product-recommendations)Query product recommendations

Product recommendations can help merchants boost sales and conversions. You can use the [`productRecommendations`](/docs/api/storefront/latest/queries/productRecommendations) query to retrieve a list of up to ten recommended products that display to customers. In your query, provide the following arguments:

* `productId`: The [global ID](/docs/api/usage/gids) of the product that's published to the storefront. This is the product for which the recommended products are generated.
* `intent`: The [type of recommendation set](/docs/api/storefront/unstable/enums/productRecommendationIntent) that will be generated. This helps you tailor recommendations for a particular surface on a storefront or selling strategy. For more information, refer to [recommendation intents](/docs/storefronts/themes/product-merchandising/recommendations#recommendation-intents).

The following example shows how to retrieve related product recommendations for a given product. The query returns the product IDs for each recommended product.

Note

Shopify provides auto-generated product recommendations. Merchants can also [customize their product recommendations](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations) using the [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery).

**Note:**

Shopify provides auto-generated product recommendations. Merchants can also [customize their product recommendations](https://help.shopify.com/manual/online-store/search-and-discovery/product-recommendations) using the [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery).

9

1

2

3

4

5

6

{

# The `intent` argument is available only in the unstable API version.

productRecommendations(productId: "gid://shopify/Product/1", intent: RELATED) {

id

}

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

"data": {

"productRecommendations": [

{

"id": "gid:\/\/shopify\/Product\/2"

},

{

"id": "gid:\/\/shopify\/Product\/3"

},

{

"id": "gid:\/\/shopify\/Product\/4"

},

{

"id": "gid:\/\/shopify\/Product\/5"

},

{

"id": "gid:\/\/shopify\/Product\/6"

},

{

"id": "gid:\/\/shopify\/Product\/7"

},

{

"id": "gid:\/\/shopify\/Product\/8"

},

{

"id": "gid:\/\/shopify\/Product\/9"

},

{

"id": "gid:\/\/shopify\/Product\/10"

},

{

"id": "gid:\/\/shopify\/Product\/11"

}

]

}

}

---

## [Anchor to Query product media](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-product-media)Query product media

You can use the Storefront API to query a product's media and display it on a storefront.

Specify the `media` field on the [`Product`](/docs/api/storefront/latest/objects/Product) object to query for a product's media. Then use a fragment to specify the fields that you want to return for each possible media type.

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

37

38

39

40

41

42

{

product(id: "gid:\/\/shopify\/ProductVariant\/1") {

id

media(first: 10) {

edges {

node {

mediaContentType

alt

...mediaFieldsByType

}

}

}

}

}

fragment mediaFieldsByType on Media {

...on ExternalVideo {

id

embeddedUrl

}

...on MediaImage {

image {

url

}

}

...on Model3d {

sources {

url

mimeType

format

filesize

}

}

...on Video {

sources {

url

mimeType

format

height

width

}

}

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

{

"data": {

"product": {

"id": "gid:\/\/shopify\/ProductVariant\/1",

"media": {

"edges": [

{

"node": {

"mediaContentType": "VIDEO",

"alt": "Comparison video showing the different models of watches.",

"sources": [

{

"url": "https://videos.shopifycdn.com/c/vp/2a82811738ca41e7a508e6744028d169/SD-360p.mp4?Expires=1575744400&KeyName=core-signing-key-1&Signature=OPKELzhY-kYTx9QH9x6NJA9IqnI=",

"mimeType": "video/mp4",

"format": "mp4",

"height": 360,

"width": 640

}

]

}

},

{

"node": {

"mediaContentType": "IMAGE",

"alt": "Polaris watch",

"image": {

"url": "https://cdn.shopify.com/s/files/1/1768/1717/products/IGQ.png?v=1560528103"

}

}

}

]

}

}

}

}

---

## [Anchor to Query collections](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#query-collections)Query collections

A collection represents a grouping of products that a store owner can create to organize them or make their stores easier to browse. For example, a merchant might create a collection for a specific type of product that they sell, such as footwear.

Merchants can create collections by selecting products individually or by defining rules that automatically determine whether products are included.

The following example shows how to query for collections and the products that belong to those collections.

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

{

collections(first: 2) {

edges {

node {

id

products(first: 5) {

edges {

node {

id

}

}

}

}

}

}

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

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

{

"data": {

"collections": {

"edges": [

{

"node": {

"id": "gid:\/\/shopify\/Collection\/1",

"products": {

"edges": [

{

"node": {

"id": "gid:\/\/shopify\/Product\/1"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/2"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/3"

}

}

]

}

}

},

{

"node": {

"id": "gid:\/\/shopify\/Collection\/2",

"products": {

"edges": [

{

"node": {

"id": "gid:\/\/shopify\/Product\/4"

}

},

{

"node": {

"id": "gid:\/\/shopify\/Product\/5"

}

}

]

}

}

}

]

}

}

}

---

## [Anchor to Next steps](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/getting-started#next-steps)Next steps

* [Filter products in a collection](/docs/storefronts/headless/building-with-the-storefront-api/products-collections/filter-products) with the Storefront API.
* [Create and update a cart](/docs/storefronts/headless/building-with-the-storefront-api/cart/manage) with the Storefront API.
* Learn about the [different tools](/docs/storefronts/headless/additional-sdks) that you can use to create unique buying experiences anywhere your customers are, including websites, apps, and video games.

---

Was this page helpful?

YesNo