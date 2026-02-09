---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/product-variant
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# Product Variant

Ask assistant

Requires `products` access scope.

**Requires `products` access scope.:**

Important

Listing, creating, updating, and deleting product variants is deprecated as of REST API 2024-04. For more information, refer to the [guide to the new product model](/docs/api/admin/migrate/new-product-model).

**Important:** 


Listing, creating, updating, and deleting product variants is deprecated as of REST API 2024-04. For more information, refer to the [guide to the new product model](/docs/api/admin/migrate/new-product-model).

Important

Apps can no longer set inventory using `inventory_quantity`. For more information, refer to the [`Inventory Level`](/api/admin-rest/latest/resources/inventorylevel) resource.

**Important:** 


Apps can no longer set inventory using `inventory_quantity`. For more information, refer to the [`Inventory Level`](/api/admin-rest/latest/resources/inventorylevel) resource.

A variant can be added to a Product resource to represent one version of a product with several options.
The Product resource will have a variant for every possible combination of its options.
Each product can have a maximum of three options and a maximum of 100 variants.

Was this section helpful?

YesNo

#

## Endpoints

* [post

  /admin/api/latest/products/{product\_id}/variants.json](/docs/api/admin-rest/latest/resources/product-variant#post-products-product-id-variants)

  Create a new Product Variant

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productCreate](/docs/api/admin-graphql/latest/mutations/productCreate)

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariantsBulkCreate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkCreate)
* [get

  /admin/api/latest/products/{product\_id}/variants.json](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants)

  Retrieves a list of product variants

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariants](/docs/api/admin-graphql/latest/queries/productVariants)
* [get

  /admin/api/latest/products/{product\_id}/variants/count.json](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-count)

  Receive a count of all Product Variants

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariantsCount](/docs/api/admin-graphql/latest/queries/productVariantsCount?example=receive-a-count-of-all-product-variants)
* [get

  /admin/api/latest/variants/{variant\_id}.json](/docs/api/admin-rest/latest/resources/product-variant#get-variants-variant-id)

  Receive a single Product Variant

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariant](/docs/api/admin-graphql/latest/queries/productVariant)
* [put

  /admin/api/latest/variants/{variant\_id}.json](/docs/api/admin-rest/latest/resources/product-variant#put-variants-variant-id)

  Modify an existing Product Variant

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariantsBulkUpdate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate)
* [del

  /admin/api/latest/products/{product\_id}/variants/{variant\_id}.json](/docs/api/admin-rest/latest/resources/product-variant#delete-products-product-id-variants-variant-id)

  Remove an existing Product Variant

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  productVariantsBulkDelete](/docs/api/admin-graphql/latest/mutations/productVariantsBulkDelete?example=remove-an-existing-product-variant)

---

[Anchor to](/docs/api/admin-rest/latest/resources/product-variant#resource-object) 

## The Product Variant resource

[Anchor to](/docs/api/admin-rest/latest/resources/product-variant#resource-object-properties) 

### Properties

---

barcode

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

barcode](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.barcode)

The barcode, UPC, or ISBN number for the product.

---

compare\_at\_price

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

compareAtPrice](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.compareAtPrice)

The original price of the item before an adjustment or a sale.

---

created\_at

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

createdAt](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the product variant was created.

---

fulfillment\_service

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

fulfillmentService](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.fulfillmentService)

The handle of a fulfillment service that stocks a product variant.

This is the handle of a third-party fulfillment service if the following conditions are met:

1. The product variant is stocked by a single fulfillment service.
2. The [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice) is a third-party fulfillment service. Third-party fulfillment services don't have a handle with the value `manual`.
3. The fulfillment service [hasn't opted into SKU sharing](/changelog/fulfillment-service-sku-sharing).

If the conditions aren't met, then this is `manual`.

The [relationship between a product variant and a fulfillment service was changed in the `2022-07` API version](/changelog/fulfillment-service-sku-sharing). A [ProductVariant](/api/admin-rest/latest/resources/product-variant) can be stocked by multiple fulfillment services. As a result, we recommend that you use the [InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource if you need to determine where a product variant is stocked.

If you previously set this field, then we recommend that you instead [connect an inventory item to a location](/api/admin-rest/latest/resources/inventorylevel#post-inventory-levels-connect). Each [Location](/api/admin-rest/latest/resources/location) is associated with a single [FulfillmentService](/api/admin-rest/latest/resources/fulfillmentservice). The value of this field after setting it will be as described above.

If you need to determine whether a product is a gift card, then you should continue to use this field until an alternative is available.

Learn more about [managing inventory quantities and states](/apps/fulfillment/inventory-management-apps/quantities-states).

---

grams

deprecated**deprecated**

The weight of the product variant in grams.

---

id

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

id](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.id)

The unique numeric identifier for the product variant.

---

image\_id

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

image](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.image)

The unique numeric identifier for a product's image.
The image must be associated to the same product as the variant.

---

inventory\_item\_id

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

inventoryItem](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryItem)

The unique identifier for the inventory item, which is used in the Inventory API to query for inventory information.

---

inventory\_management

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

inventoryLevel](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevel)

The fulfillment service that tracks the number of items in stock for the product variant.
Valid values:

Show inventory\_management properties

* `shopify`: You are tracking inventory yourself using the admin.
* `null`: You aren't tracking inventory on the variant.
* the handle of a [fulfillment service](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice) that has inventory management enabled: This must be the same fulfillment service referenced by the `fulfillment_service` property.

---

inventory\_policy

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

inventoryPolicy](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryPolicy)

Whether customers are allowed to place an order for the product variant when it's out of stock. Valid values:

Show inventory\_policy properties

* `deny`: Customers are not allowed to place orders for the product variant if it's out of stock.
* `continue`: Customers are allowed to place orders for the product variant if it's out of stock.

Default value: `deny`.

---

inventory\_quantity

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

inventoryQuantity](/docs/api/admin-graphql/latest/objects/ProductVariant#field-ProductVariant.fields.inventoryQuantity)

An aggregate of inventory across all locations. To adjust inventory at a specific location, use the
[InventoryLevel](/docs/admin-api/rest/reference/inventory/inventorylevel) resource.

---

old\_inventory\_quantity

deprecated**deprecated**

This property is deprecated. Use the
[InventoryLevel](/docs/admin-api/rest/reference/inventory/inventorylevel) resource instead.

---

Show 13 hidden fields

Was this section helpful?

YesNo

{}

## The Product Variant resource

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

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

{

"barcode": "1234\_pink",

"compare\_at\_price": "299.00",

"created\_at": "2012-08-24T14:01:47-04:00",

"fulfillment\_service": "manual",

"grams": 567,

"id": 808950810,

"image\_id": 434522,

"inventory\_item\_id": 342916,

"inventory\_management": "shopify",

"inventory\_policy": "continue",

"inventory\_quantity": 10,

"old\_inventory\_quantity": 5,

"option": {

"option1": "Pink"

},

"presentment\_prices": {

"presentment\_prices": [

{

"price": {

"currency\_code": "USD",

"amount": "199.99"

},

"compare\_at\_price": {

"currency\_code": "USD",

"amount": "249.99"

}

},

{

"price": {

"currency\_code": "EUR",

"amount": "158.95"

},

"compare\_at\_price": {

"currency\_code": "EUR",

"amount": "198.95"

}

},

{

"price": {

"currency\_code": "GBP",

"amount": "143.00"

},

"compare\_at\_price": {

"currency\_code": "GBP",

"amount": "179.00"

}

},

{

"price": {

"currency\_code": "JPY",

"amount": "22400"

},

"compare\_at\_price": {

"currency\_code": "JPY",

"amount": "28000"

}

}

]

},

"position": 1,

"price": "199.00",

"product\_id": 632910392,

"requires\_shipping": true,

"sku": "IPOD2008PINK",

"taxable": true,

"tax\_code": "DA040000",

"title": "Pink",

"updated\_at": "2012-08-24T14:01:47-04:00",

"weight": 100,

"weight\_unit": "oz"

}

---

## [Anchor to POST request, Create a new Product Variant](/docs/api/admin-rest/latest/resources/product-variant#post-products-product-id-variants) post Create a new Product Variant

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productCreate](/docs/api/admin-graphql/latest/mutations/productCreate)

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariantsBulkCreate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkCreate)

Creates a new product variant

### [Anchor to Parameters of Create a new Product Variant](/docs/api/admin-rest/latest/resources/product-variant#post-products-product-id-variants-parameters)Parameters

---

api\_version

string**string**

required**required**

---

product\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to post-products-product-id-variants-examples](/docs/api/admin-rest/latest/resources/product-variant#post-products-product-id-variants-examples)Examples

Create a new product variant

Path parameters

product\_id=632910392

string**string**

required**required**

Create a new product variant with a metafield

Path parameters

product\_id=632910392

string**string**

required**required**

Create a new product variant with an image

Path parameters

product\_id=632910392

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

4

5

curl -d '{"variant":{"option1":"Yellow","price":"1.00"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \

-H "X-Shopify-Access-Token: {access\_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

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

HTTP/1.1 201 Created

{

"variant": {

"id": 1070325042,

"product\_id": 632910392,

"title": "Yellow",

"price": "1.00",

"position": 5,

"inventory\_policy": "deny",

"compare\_at\_price": null,

"option1": "Yellow",

"option2": null,

"option3": null,

"created\_at": "2026-01-09T17:30:30-05:00",

"updated\_at": "2026-01-09T17:30:30-05:00",

"taxable": true,

"barcode": null,

"fulfillment\_service": "manual",

"grams": 0,

"inventory\_management": "shopify",

"requires\_shipping": true,

"sku": null,

"weight": 0,

"weight\_unit": "lb",

"inventory\_item\_id": 1070325042,

"inventory\_quantity": 0,

"old\_inventory\_quantity": 0,

"presentment\_prices": [

{

"price": {

"amount": "1.00",

"currency\_code": "USD"

},

"compare\_at\_price": null

}

],

"admin\_graphql\_api\_id": "gid://shopify/ProductVariant/1070325042",

"image\_id": null

}

}

### examples

* #### Create a new product variant

  ##### 

  ```liquid
  curl -d '{"variant":{"option1":"Yellow","price":"1.00"}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.product_id = 632910392;
  variant.option1 = "Yellow";
  variant.price = "1.00";
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.product_id = 632910392
  variant.option1 = "Yellow"
  variant.price = "1.00"
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.product_id = 632910392;
  variant.option1 = "Yellow";
  variant.price = "1.00";
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"variant":{"id":1070325042,"product_id":632910392,"title":"Yellow","price":"1.00","position":5,"inventory_policy":"deny","compare_at_price":null,"option1":"Yellow","option2":null,"option3":null,"created_at":"2026-01-09T17:30:30-05:00","updated_at":"2026-01-09T17:30:30-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":"shopify","requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325042,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"1.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325042","image_id":null}}
  ```
* #### Create a new product variant with a metafield

  ##### 

  ```liquid
  curl -d '{"variant":{"option1":"Blue","metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.product_id = 632910392;
  variant.option1 = "Blue";
  variant.metafields = [
    {
      "key": "new",
      "value": "newvalue",
      "type": "single_line_text_field",
      "namespace": "global"
    }
  ];
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.product_id = 632910392
  variant.option1 = "Blue"
  variant.metafields = [
    {
      "key" => "new",
      "value" => "newvalue",
      "type" => "single_line_text_field",
      "namespace" => "global"
    }
  ]
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.product_id = 632910392;
  variant.option1 = "Blue";
  variant.metafields = [
    {
      "key": "new",
      "value": "newvalue",
      "type": "single_line_text_field",
      "namespace": "global"
    }
  ];
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"variant":{"id":1070325044,"product_id":632910392,"title":"Blue","price":"0.00","position":5,"inventory_policy":"deny","compare_at_price":null,"option1":"Blue","option2":null,"option3":null,"created_at":"2026-01-09T17:30:47-05:00","updated_at":"2026-01-09T17:30:47-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":"shopify","requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325044,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325044","image_id":null}}
  ```
* #### Create a new product variant with an image

  ##### 

  ```liquid
  curl -d '{"variant":{"image_id":850703190,"option1":"Purple"}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.product_id = 632910392;
  variant.image_id = 850703190;
  variant.option1 = "Purple";
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.product_id = 632910392
  variant.image_id = 850703190
  variant.option1 = "Purple"
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.product_id = 632910392;
  variant.image_id = 850703190;
  variant.option1 = "Purple";
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"variant":{"id":1070325043,"product_id":632910392,"title":"Purple","price":"0.00","position":5,"inventory_policy":"deny","compare_at_price":null,"option1":"Purple","option2":null,"option3":null,"created_at":"2026-01-09T17:30:44-05:00","updated_at":"2026-01-09T17:30:44-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":"shopify","requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325043,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325043","image_id":850703190}}
  ```

---

## [Anchor to GET request, Retrieves a list of product variants](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants) get Retrieves a list of product variants

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariants](/docs/api/admin-graphql/latest/queries/productVariants)

Retrieves a list of product variants. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieves a list of product variants](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-parameters)Parameters

---

api\_version

string**string**

required**required**

---

product\_id

string**string**

required**required**

---

fields

A comma-separated list of fields to include in the response

---

limit

≤ 250**≤ 250**

default 50**default 50**

Return up to this many results per page

---

presentment\_currencies

Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency codes.

---

since\_id

Restrict results to after the specified ID

---

Was this section helpful?

YesNo

### [Anchor to get-products-product-id-variants-examples](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-examples)Examples

Retrieve all variants for a product

Path parameters

product\_id=632910392

string**string**

required**required**

Retrieve all variants for a product after a specified ID

Path parameters

product\_id=632910392

string**string**

required**required**

Query parameters

since\_id=49148385

Restrict results to after the specified ID

Retrieve all variants for a product with prices in specified presentment currencies

Path parameters

product\_id=632910392

string**string**

required**required**

Query parameters

presentment\_currencies=USD,CAD

Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency codes.

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

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

HTTP/1.1 200 OK

{

"variants": [

{

"id": 39072856,

"product\_id": 632910392,

"title": "Green",

"price": "199.00",

"position": 3,

"inventory\_policy": "continue",

"compare\_at\_price": null,

"option1": "Green",

"option2": null,

"option3": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"taxable": true,

"barcode": "1234\_green",

"fulfillment\_service": "manual",

"grams": 567,

"inventory\_management": "shopify",

"requires\_shipping": true,

"sku": "IPOD2008GREEN",

"weight": 1.25,

"weight\_unit": "lb",

"inventory\_item\_id": 39072856,

"inventory\_quantity": 30,

"old\_inventory\_quantity": 30,

"presentment\_prices": [

{

"price": {

"amount": "199.00",

"currency\_code": "USD"

},

"compare\_at\_price": null

}

### examples

* #### Retrieve all variants for a product

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.all({
    session: session,
    product_id: 632910392,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.all(
    session: test_session,
    product_id: 632910392,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.all({
    session: session,
    product_id: 632910392,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variants":[{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null},{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}]}
  ```
* #### Retrieve all variants for a product after a specified ID

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json?since_id=49148385" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.all({
    session: session,
    product_id: 632910392,
    since_id: "49148385",
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.all(
    session: test_session,
    product_id: 632910392,
    since_id: "49148385",
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.all({
    session: session,
    product_id: 632910392,
    since_id: "49148385",
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variants":[{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null},{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}]}
  ```
* #### Retrieve all variants for a product with prices in specified presentment currencies

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants.json?presentment_currencies=USD%2CCAD" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.all({
    session: session,
    product_id: 632910392,
    presentment_currencies: "USD,CAD",
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.all(
    session: test_session,
    product_id: 632910392,
    presentment_currencies: "USD,CAD",
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.all({
    session: session,
    product_id: 632910392,
    presentment_currencies: "USD,CAD",
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variants":[{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":"249.00","option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":{"amount":"249.00","currency_code":"USD"}},{"price":{"amount":"249.00","currency_code":"CAD"},"compare_at_price":{"amount":"312.00","currency_code":"CAD"}}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":"249.00","option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":{"amount":"249.00","currency_code":"USD"}},{"price":{"amount":"249.00","currency_code":"CAD"},"compare_at_price":{"amount":"312.00","currency_code":"CAD"}}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":"249.00","option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":{"amount":"249.00","currency_code":"USD"}},{"price":{"amount":"249.00","currency_code":"CAD"},"compare_at_price":{"amount":"312.00","currency_code":"CAD"}}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null},{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":"249.00","option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":{"amount":"249.00","currency_code":"USD"}},{"price":{"amount":"249.00","currency_code":"CAD"},"compare_at_price":{"amount":"312.00","currency_code":"CAD"}}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}]}
  ```

---

## [Anchor to GET request, Receive a count of all Product Variants](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-count) get Receive a count of all Product Variants

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariantsCount](/docs/api/admin-graphql/latest/queries/productVariantsCount?example=receive-a-count-of-all-product-variants)

Retrieves a count of product variants

### [Anchor to Parameters of Receive a count of all Product Variants](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-count-parameters)Parameters

---

api\_version

string**string**

required**required**

---

product\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-products-product-id-variants-count-examples](/docs/api/admin-rest/latest/resources/product-variant#get-products-product-id-variants-count-examples)Examples

Retrieve a count all variants for a product

Path parameters

product\_id=632910392

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants/count.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

9

1

2

3

4

HTTP/1.1 200 OK

{

"count": 4

}

### examples

* #### Retrieve a count all variants for a product

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants/count.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.count({
    session: session,
    product_id: 632910392,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.count(
    session: test_session,
    product_id: 632910392,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.count({
    session: session,
    product_id: 632910392,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"count":4}
  ```

---

## [Anchor to GET request, Receive a single Product Variant](/docs/api/admin-rest/latest/resources/product-variant#get-variants-variant-id) get Receive a single Product Variant

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariant](/docs/api/admin-graphql/latest/queries/productVariant)

Retrieves a single product variant by ID

### [Anchor to Parameters of Receive a single Product Variant](/docs/api/admin-rest/latest/resources/product-variant#get-variants-variant-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

variant\_id

string**string**

required**required**

---

fields

A comma-separated list of fields to include in the response

---

Was this section helpful?

YesNo

### [Anchor to get-variants-variant-id-examples](/docs/api/admin-rest/latest/resources/product-variant#get-variants-variant-id-examples)Examples

Retrieve a product variant by ID

Path parameters

variant\_id=808950810

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

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

HTTP/1.1 200 OK

{

"variant": {

"id": 808950810,

"product\_id": 632910392,

"title": "Pink",

"price": "199.00",

"position": 1,

"inventory\_policy": "continue",

"compare\_at\_price": null,

"option1": "Pink",

"option2": null,

"option3": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"taxable": true,

"barcode": "1234\_pink",

"fulfillment\_service": "manual",

"grams": 567,

"inventory\_management": "shopify",

"requires\_shipping": true,

"sku": "IPOD2008PINK",

"weight": 1.25,

"weight\_unit": "lb",

"inventory\_item\_id": 808950810,

"inventory\_quantity": 10,

"old\_inventory\_quantity": 10,

"presentment\_prices": [

{

"price": {

"amount": "199.00",

"currency\_code": "USD"

},

"compare\_at\_price": null

}

],

"tax\_code": "DA040000",

"admin\_graphql\_api\_id": "gid://shopify/ProductVariant/808950810",

"image\_id": 562641783

}

}

### examples

* #### Retrieve a product variant by ID

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.find({
    session: session,
    id: 808950810,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.find(
    session: test_session,
    id: 808950810,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.find({
    session: session,
    id: 808950810,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variant":{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"tax_code":"DA040000","admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}}
  ```

---

## [Anchor to PUT request, Modify an existing Product Variant](/docs/api/admin-rest/latest/resources/product-variant#put-variants-variant-id) put Modify an existing Product Variant

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariantsBulkUpdate](/docs/api/admin-graphql/latest/mutations/productVariantsBulkUpdate)

Updates an existing product variant

### [Anchor to Parameters of Modify an existing Product Variant](/docs/api/admin-rest/latest/resources/product-variant#put-variants-variant-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

variant\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to put-variants-variant-id-examples](/docs/api/admin-rest/latest/resources/product-variant#put-variants-variant-id-examples)Examples

Add a metafield to an existing variant

Path parameters

variant\_id=808950810

string**string**

required**required**

Add an existing image to an existing variant

Path parameters

variant\_id=808950810

string**string**

required**required**

Update the title and price of an existing variant

Path parameters

variant\_id=808950810

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

4

5

curl -d '{"variant":{"id":808950810,"metafields":[{"key":"new","value":"newvalue","type":"single\_line\_text\_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \

-H "X-Shopify-Access-Token: {access\_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

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

HTTP/1.1 200 OK

{

"variant": {

"id": 808950810,

"product\_id": 632910392,

"title": "Pink",

"price": "199.00",

"position": 1,

"inventory\_policy": "continue",

"compare\_at\_price": null,

"option1": "Pink",

"option2": null,

"option3": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"taxable": true,

"barcode": "1234\_pink",

"fulfillment\_service": "manual",

"grams": 567,

"inventory\_management": "shopify",

"requires\_shipping": true,

"sku": "IPOD2008PINK",

"weight": 1.25,

"weight\_unit": "lb",

"inventory\_item\_id": 808950810,

"inventory\_quantity": 10,

"old\_inventory\_quantity": 10,

"presentment\_prices": [

{

"price": {

"amount": "199.00",

"currency\_code": "USD"

},

"compare\_at\_price": null

}

],

"admin\_graphql\_api\_id": "gid://shopify/ProductVariant/808950810",

"image\_id": 562641783

}

}

### examples

* #### Add a metafield to an existing variant

  ##### 

  ```liquid
  curl -d '{"variant":{"id":808950810,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
  -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.id = 808950810;
  variant.metafields = [
    {
      "key": "new",
      "value": "newvalue",
      "type": "single_line_text_field",
      "namespace": "global"
    }
  ];
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.id = 808950810
  variant.metafields = [
    {
      "key" => "new",
      "value" => "newvalue",
      "type" => "single_line_text_field",
      "namespace" => "global"
    }
  ]
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.id = 808950810;
  variant.metafields = [
    {
      "key": "new",
      "value": "newvalue",
      "type": "single_line_text_field",
      "namespace": "global"
    }
  ];
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variant":{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}}
  ```
* #### Add an existing image to an existing variant

  ##### 

  ```liquid
  curl -d '{"variant":{"id":808950810,"image_id":562641783}}' \
  -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.id = 808950810;
  variant.image_id = 562641783;
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.id = 808950810
  variant.image_id = 562641783
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.id = 808950810;
  variant.image_id = 562641783;
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variant":{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:30:39-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}}
  ```
* #### Update the title and price of an existing variant

  ##### 

  ```liquid
  curl -d '{"variant":{"id":808950810,"option1":"Not Pink","price":"99.00"}}' \
  -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/variants/808950810.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const variant = new admin.rest.resources.Variant({session: session});

  variant.id = 808950810;
  variant.option1 = "Not Pink";
  variant.price = "99.00";
  await variant.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  variant = ShopifyAPI::Variant.new(session: test_session)
  variant.id = 808950810
  variant.option1 = "Not Pink"
  variant.price = "99.00"
  variant.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const variant = new shopify.rest.Variant({session: session});
  variant.id = 808950810;
  variant.option1 = "Not Pink";
  variant.price = "99.00";
  await variant.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"variant":{"id":808950810,"product_id":632910392,"title":"Not Pink","price":"99.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Not Pink","option2":null,"option3":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:30:46-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"99.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}}
  ```

---

## [Anchor to DELETE request, Remove an existing Product Variant](/docs/api/admin-rest/latest/resources/product-variant#delete-products-product-id-variants-variant-id) del Remove an existing Product Variant

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

productVariantsBulkDelete](/docs/api/admin-graphql/latest/mutations/productVariantsBulkDelete?example=remove-an-existing-product-variant)

### [Anchor to Parameters of Remove an existing Product Variant](/docs/api/admin-rest/latest/resources/product-variant#delete-products-product-id-variants-variant-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

product\_id

string**string**

required**required**

---

variant\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to delete-products-product-id-variants-variant-id-examples](/docs/api/admin-rest/latest/resources/product-variant#delete-products-product-id-variants-variant-id-examples)Examples

Delete a product variant

Was this section helpful?

YesNo

9

1

2

3

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants/808950810.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

* #### Delete a product variant

  ##### 

  ```liquid
  curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/variants/808950810.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Variant.delete({
    session: session,
    product_id: 632910392,
    id: 808950810,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Variant.delete(
    session: test_session,
    product_id: 632910392,
    id: 808950810,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Variant.delete({
    session: session,
    product_id: 632910392,
    id: 808950810,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{}
  ```