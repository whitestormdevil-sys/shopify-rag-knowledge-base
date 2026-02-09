---
source: https://shopify.dev/docs/api/ajax/reference/cart
---

The Cart API is used to interact with a cart during a customer's session. This guide shows how to use the Cart API to update cart line items, add cart attributes and notes, and generate shipping rates.

All Ajax API requests should use [locale-aware URLs](/docs/api/ajax#locale-aware-urls) to give visitors a consistent experience.

Note

For simplicity, the code examples in this guide don't always use a callback.

**Note:**

For simplicity, the code examples in this guide don't always use a callback.

---

## [Anchor to POST /{locale}/cart/add.js](/docs/api/ajax/reference/cart#post--locale-cart-addjs)POST /{locale}/cart/add.js

Use the `POST /{locale}/cart/add.js` endpoint to add one or multiple variants to the cart.

In the following example, `quantity` is the amount of the variant that you want to add and `id` is the variant ID of that variant. You can add multiple variants to the cart by appending more objects in the `items` array.

Below is a simplified `POST` request using the `fetch` API. The `formData` object is built in JavaScript, so the `Content-Type` should be set to `application/json` in the `headers` object. The response is the JSON of the line items associated with the added variants. If an item is already in the cart, then `quantity` is equal to the new quantity for that item.

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

let formData = {

'items': [{

'id': 36110175633573,

'quantity': 2

}]

};

fetch(window.Shopify.routes.root + 'cart/add.js', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify(formData)

})

.then(response => {

return response.json();

})

.catch((error) => {

console.error('Error:', error);

});

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

{

"items": [

{

"id": 36110175633573,

"title": "Red Rain Coat - Small",

"key": "794864229:03af7a8cb59a4c3c45595c76fa8cb53c",

"price": 12900,

"line\_price": 12900,

"quantity": 2,

"sku": null,

"grams": 0,

"vendor": "Shopify",

"properties": {},

"variant\_id": 794864229,

"gift\_card": false,

"url": "/products/red-rain-coat?variant=794864229",

"featured\_image": {

"url": "http://cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",

"aspect\_ratio": 1.0,

"alt": "Red rain coat with a hood"

},

"image": "http://cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",

"handle": "red-rain-coat",

"requires\_shipping": true,

"product\_title": "Red Rain Coat",

"product\_description": "A bright red rain coat for rainy days!",

"product\_type": "Coat",

"properties" : null,

"variant\_title": "Red",

"variant\_options": ["Red"],

"options\_with\_values": [

{

"name": "Color",

"value": "Red"

}

]

}

]

}

Alternatively, you can use the [`FormData` constructor](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData) and target the desired add-to-cart form:

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

let addToCartForm = document.querySelector('form[action$="/cart/add"]');

let formData = new FormData(addToCartForm);

fetch(window.Shopify.routes.root + 'cart/add.js', {

method: 'POST',

body: formData

})

.then(response => {

return response.json();

})

.catch((error) => {

console.error('Error:', error);

});

### [Anchor to Response](/docs/api/ajax/reference/cart#response)Response

The response for a successful `POST` request is a JSON object of the line items associated with the added items.

If an added item was already in the cart, then the `quantity` is equal to the new quantity for that cart line item. However, if the same items have differing prices, properties, or selling plans, then they'll be split into their own line items.

Tip

Changes in price are typically the result of [automatic discounts](https://help.shopify.com/en/manual/discounts/automatic-discounts) or [Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor).

**Tip:**

Changes in price are typically the result of [automatic discounts](https://help.shopify.com/en/manual/discounts/automatic-discounts) or [Shopify Scripts](https://help.shopify.com/manual/checkout-settings/script-editor).

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

items: [

{

id: 36323170943141,

quantity: 1

},

{

id: 36323170943141,

selling\_plan: 6717605,

quantity: 1

},

{

id: 36323170943141,

parent\_id: 4534355122,

quantity: 1

}

]

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

"items":[

{

"id":36323170943141,

"properties":null,

"quantity":1,

"variant\_id":36323170943141,

"key":"36323170943141:b15f59bb6d406f2f45dc383a5493bdb8",

"title":"Great Granola Bar",

"price":2000,

"original\_price":2000,

"discounted\_price":2000,

"line\_price":2000,

"original\_line\_price":2000,

"total\_discount":0,

"discounts":[],

"sku":"",

"grams":0,

"vendor":"shopify",

"taxable":true,

"product\_id":5680114172069,

"product\_has\_only\_default\_variant":true,

"gift\_card":false,

"final\_price":2000,

"final\_line\_price":2000,

"url":"/products/great-granola-bar?variant=36323170943141",

"featured\_image":{

"aspect\_ratio":1.504,

"alt":"Great Granola Bar",

"height":1277,

"url":"https://cdn.shopify.com/s/files/1/0401/3218/2181/products/fallon-michael-h2UH2674Bg4-unsplash.jpg?v=1600796940",

"width":1920

},

"image":"https://cdn.shopify.com/s/files/1/0401/3218/2181/products/fallon-michael-h2UH2674Bg4-unsplash.jpg?v=1600796940",

"handle":"great-granola-bar",

"requires\_shipping":true,

### [Anchor to Error responses](/docs/api/ajax/reference/cart#error-responses)Error responses

If the specified quantity for an item exceeds the available stock (e.g., attempting to add 20 items when only 10 are available), the cart will instead add the maximum available quantity. The error returned in JSON format is as follows:

9

1

2

3

4

5

{

"status": 422,

"message": "Cart Error",

"description": "You can't add more #{item.name} to the cart."

}

If the product is entirely sold out, then the following error is returned:

9

1

2

3

4

5

{

"status": 422,

"message": "Cart Error",

"description": "The product '#{item.name}' is already sold out."

}

If the product is not sold out, but all of its stock is in the cart, then the following error is returned:

9

1

2

3

4

5

{

"status": 422,

"message": "Cart Error",

"description": "You can't add more #{item.name} to the cart."

}

### [Anchor to Add line item properties](/docs/api/ajax/reference/cart#add-line-item-properties)Add line item properties

You can add a variant to the cart with [line item properties](/docs/api/liquid/objects/line_item#line_item-properties) using the `properties` property. Its value must be an object of key-value pairs.

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

items: [

{

quantity: 1,

id: 794864229,

properties: {

'First name': 'Caroline'

}

}

]

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

{

"items": [

{

"id": 794864229,

"quantity": 1,

// ...

"properties" : {

"First name": "Caroline"

}

}

]

}

### [Anchor to Add a selling plan](/docs/api/ajax/reference/cart#add-a-selling-plan)Add a selling plan

You can add a variant with a [selling plan](/docs/api/liquid/objects/selling_plan) to the cart using the `selling_plan` parameter. Its value must be the [selling plan ID](/docs/api/liquid/objects/selling_plan#selling_plan-id).

9

1

2

3

4

5

6

7

items: [

{

quantity: 1,

id: 794864229,

selling\_plan: 183638

}

]

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

{

"items": [

{

"id": 794864229,

// ...

"selling\_plan\_allocation": {

"price": 3120,

"compare\_at\_price": 3900,

"per\_delivery\_price": 3120,

"selling\_plan": {

"id": 183638,

"name": "Pay every month, delivery every month | save 20%",

"description": "No commitment · Auto-renews · Skip or cancel anytime",

"options": [{

"name": "Delivery Frequency",

"position": 1,

"value": "Month"

}, {

"name": "Billing Frequency",

"position": 2,

"value": "Month"

}],

"recurring\_deliveries": true

}

}

}

]

}

---

## [Anchor to GET /{locale}/cart.js](/docs/api/ajax/reference/cart#get--locale-cartjs)GET /{locale}/cart.js

Use the `GET /{locale}/cart.js` endpoint to get the cart as JSON.

All monetary properties are returned in the customer's presentment currency. To check the customer's presentment currency, you can use the `currency` field in the response. To learn more about selling in multiple currencies, refer to [Migrate your app to support multi-currency](/docs/api/admin-rest/latest/resources/transaction).

### [Anchor to Responses](/docs/api/ajax/reference/cart#responses)Responses

#### [Anchor to JSON of a cart](/docs/api/ajax/reference/cart#json-of-a-cart)JSON of a cart

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

"token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",

"note": "Hello!",

"attributes": {

"Gift wrap": "Yes"

},

"original\_total\_price": 3399,

"total\_price": 2925,

"total\_discount": 474,

"total\_weight": 500,

"item\_count": 2,

"items": [

{

"id": 39897499729985,

"properties": {},

"quantity": 1,

"variant\_id": 39897499729985,

"key": "39897499729985:b1fca88d0e8bf5290f306f808785f744",

"title": "Health potion - S / Low",

"price": 900,

"original\_price": 900,

"discounted\_price": 900,

"line\_price": 900,

"original\_line\_price": 900,

"total\_discount": 0,

"discounts": [],

"sku": "",

"grams": 500,

"vendor": "Polina's Potent Potions",

"taxable": true,

"product\_id": 6786188247105,

"product\_has\_only\_default\_variant": false,

"gift\_card": false,

"final\_price": 900,

"final\_line\_price": 900,

"url": "/products/health-potion?selling\_plan=610435137&variant=39897499729985",

#### [Anchor to JSON of an empty cart](/docs/api/ajax/reference/cart#json-of-an-empty-cart)JSON of an empty cart

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

{

"token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",

"note": null,

"attributes": {},

"original\_total\_price": 0,

"total\_price": 0,

"total\_discount": 0,

"total\_weight": 0,

"item\_count": 0,

"items": [],

"requires\_shipping": false,

"currency": "CAD",

"items\_subtotal\_price": 0,

"cart\_level\_discount\_applications": []

}

Tip

If you want to empty an existing cart, then use the `/{locale}/cart/clear` endpoint.

**Tip:**

If you want to empty an existing cart, then use the `/{locale}/cart/clear` endpoint.

#### [Anchor to JSON of a cart with remote products](/docs/api/ajax/reference/cart#json-of-a-cart-with-remote-products)JSON of a cart with remote products

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

"token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",

"note": null,

"attributes": {},

"original\_total\_price": 4925,

"total\_price": 4925,

"total\_discount": 0,

"total\_weight": 500,

"item\_count": 3,

"items": [

{

"id": 36323170943141,

"quantity": 1,

"title": "Blue Mug - Sold by Sam's Shop",

"remote": true,

...

},

{

"id": 36323170943142,

"quantity": 1,

"title": "Salad bowl - Sold by Home Experts",

"remote": true,

...

},

{

"id": 36323170943143,

"quantity": 1,

"title": "Silverware set",

...

}

],

"requires\_shipping": false,

"currency": "CAD",

"items\_subtotal\_price": 3149,

"cart\_level\_discount\_applications": []

}

---

## [Anchor to POST /{locale}/cart/update.js](/docs/api/ajax/reference/cart#post--locale-cart-updatejs)POST /{locale}/cart/update.js

Use the `POST /{locale}/cart/update.js` endpoint to update the cart's line item quantities, note, or attributes. You can submit a serialized cart form, or submit separate updates to a cart's line items, note, or attributes.

### [Anchor to Update line item quantities](/docs/api/ajax/reference/cart#update-line-item-quantities)Update line item quantities

To update line item quantities, you can make a `POST` request with an `updates` object. The `updates` object must contain key-value pairs where the value is the desired quantity, and the key is one of the following:

* The line item's [`variant_id`](/docs/api/liquid/objects/line_item#line_item-variant_id)
* The line item's [`key`](/docs/api/liquid/objects/line_item#line_item-key)

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

let updates = {

794864053: 2,

794864233: 3

};

fetch(window.Shopify.routes.root + 'cart/update.js', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify({ updates })

})

.then(response => {

return response.json();

})

.catch((error) => {

console.error('Error:', error);

});

A cart can have multiple line items that share the same `variant_id`. For example, when variants have different [line item properties](/docs/api/liquid/objects/line_item#line_item-properties), or [automatic discounts](https://help.shopify.com/en/manual/discounts/automatic-discounts) create variants at different prices. Because of this, it's recommended to use the line item key to ensure that you're only changing the intended line item.

The line item key is not persistent for the lifetime of a line item, it changes as characteristics of the line item change. This includes, but is not limited to, properties and discount applications.

Note

If you use the variant ID, then the key can be either an integer or a string. However, if you use the line item key, then the key needs to be a string.

**Note:**

If you use the variant ID, then the key can be either an integer or a string. However, if you use the line item key, then the key needs to be a string.

The following `POST` request yields the same result:

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

var formData = new FormData();

formData.append("updates[794864053]", 2);

formData.append("updates[794864233]", 3);

fetch(window.Shopify.routes.root + 'cart/update.js', {

method: 'POST',

body: formData

})

.then(response => response.json())

.then(data => console.log(data));

The `/{locale}/cart/update.js` endpoint adds new line items to the cart if the `variant_id` provided doesn't match any line item already in the cart. However, if the `variant_id` matches multiple line items, then the first matching line item is updated.

Tip

Use the `change.js` endpoint when changing line items that are already in the cart, and the `add.js` endpoint when adding new line items.

**Tip:**

Use the `change.js` endpoint when changing line items that are already in the cart, and the `add.js` endpoint when adding new line items.

You can remove items from the cart by setting the quantity to 0:

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

let updates = {

794864053: 0,

794864233: 0

};

fetch(window.Shopify.routes.root + 'cart/update.js', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify({ updates })

})

.then(response => {

return response.json();

})

.catch((error) => {

console.error('Error:', error);

});

You can also submit an array of numbers to `/{locale}/cart/update.js`, provided the size of the array matches the number of line items in the cart. Each number in the array sets the quantity for the corresponding line item in the cart. For example, if you have 3 line items in the cart with quantities 1, 2, and 3, and you want to change those quantities to 3, 2, and 1, then you can use the following:

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

fetch(window.Shopify.routes.root + 'cart/update.js', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify({ updates: [3, 2, 1] })

})

.then(response => response.json())

.then(data => console.log(data));

### [Anchor to Update the cart note](/docs/api/ajax/reference/cart#update-the-cart-note)Update the cart note

To update the cart note, you can make a `POST` request with a `note` character string:

9

1

2

3

{

note: 'This is a note about my order'

}

### [Anchor to Update cart attributes](/docs/api/ajax/reference/cart#update-cart-attributes)Update cart attributes

To update cart attributes, you can make a `POST` request with an `attributes` object. The `attributes` object must contain key-value pairs where the `key` is the name of the attribute you want to update, and the value is the attribute value:

9

1

2

3

4

5

{

attributes: {

'Gift wrap': 'Yes'

}

}

The following `POST` request yields the same result:

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

var formData = new FormData();

formData.append("attributes[Gift wrap]", "Yes");

fetch(window.Shopify.routes.root + 'cart/update.js', {

method: 'POST',

body: formData

})

.then(response => response.json())

.then(data => console.log(data));

### [Anchor to Update discounts in the cart](/docs/api/ajax/reference/cart#update-discounts-in-the-cart)Update discounts in the cart

You can apply a discount to the cart, as shown in the following example:

9

1

2

3

{

discount: 'discount\_code'

}

You can also apply multiple discounts to the cart using a comma `,` separator:

9

1

2

3

{

discount: 'discount\_code,discount\_code2'

}

To remove all discounts from the cart, use an empty string:

9

1

2

3

{

discount: ''

}

### [Anchor to Response](/docs/api/ajax/reference/cart#response)Response

The JSON of the cart.

### [Anchor to Error responses](/docs/api/ajax/reference/cart#error-responses)Error responses

If a variant ID is provided that either doesn't exist or isn't available in the online store channel, then the endpoint returns the following error:

9

1

2

3

4

5

{

"status": 404,

"message": "Cart Error"

"description": "Cannot find variant"

}

Caution

The `update.js` endpoint doesn't validate the quantity on variants that are already in the cart. This means that it's possible to add more inventory than is available.

**Caution:**

The `update.js` endpoint doesn't validate the quantity on variants that are already in the cart. This means that it's possible to add more inventory than is available.

---

## [Anchor to POST /{locale}/cart/change.js](/docs/api/ajax/reference/cart#post--locale-cart-changejs)POST /{locale}/cart/change.js

Use the `/{locale}/cart/change.js` endpoint to change the `quantity`, `properties`, and `selling_plan` properties of a cart line item. Only items already in your cart can be changed, and you can change only one line item at a time.

### [Anchor to Identify the line item to change](/docs/api/ajax/reference/cart#identify-the-line-item-to-change)Identify the line item to change

The `POST` data requires either an `id` or `line` property to identify the line item to be changed.

#### [Anchor to The ,[object Object], property](/docs/api/ajax/reference/cart#the-id-property)The `id` property

The value of the `id` property can be one of the following:

* The line item's [`variant_id`](/docs/api/liquid/objects/line_item#line_item-variant_id)
* The line item's [`key`](/docs/api/liquid/objects/line_item#line_item-key)

9

1

2

3

4

{

'id': 794864053,

'quantity': 3

}

9

1

2

3

4

{

'id': '794864053:83503fd282b94a4737d2c95bd95db0b8',

'quantity': 3

}

##### Variant ID

```liquid
{
  'id': 794864053,
  'quantity': 3
}
```

##### Line item key

```liquid
{
  'id': '794864053:83503fd282b94a4737d2c95bd95db0b8',
  'quantity': 3
}
```

A cart can have multiple line items that share the same `variant_id`. For example, when variants have different [line item properties](/docs/api/liquid/objects/line_item#line_item-properties), or [automatic discounts](https://help.shopify.com/en/manual/discounts/automatic-discounts) create variants at different prices. Because of this, it's recommended to use the line item key to ensure that you're only changing the intended line item.

Note

If you use the variant ID, then the `id` value can be either an integer or a string. However, if you use the line item key, then the `id` value needs to be a string.

**Note:**

If you use the variant ID, then the `id` value can be either an integer or a string. However, if you use the line item key, then the `id` value needs to be a string.

#### [Anchor to The ,[object Object], property](/docs/api/ajax/reference/cart#the-line-property)The `line` property

A cart can have multiple line items that share the same `variant_id`. For example, when variants have different [line item properties](/docs/api/liquid/objects/line_item#line_item-properties), or [automatic discounts](https://help.shopify.com/en/manual/discounts/automatic-discounts) create variants at different prices. To account for this, you can use the `line` property when updating the cart.

The value of `line` is the 1-based index position of the item in the cart.

9

1

2

3

4

{

'line': 1,

'quantity': 3

}

### [Anchor to Update quantities](/docs/api/ajax/reference/cart#update-quantities)Update quantities

The value of the`quantity` property represents the new quantity you want for the line item. It must be an integer.

9

1

2

3

4

{

'line': 2,

'quantity': 1

}

You can remove a line item by setting the `quantity` to `0`:

9

1

2

3

4

{

'line': 2,

'quantity': 0

}

### [Anchor to Update properties](/docs/api/ajax/reference/cart#update-properties)Update properties

The `properties` property sets the [line item properties](/docs/api/liquid/objects/line_item#line_item-properties). Its value must be an object of key-value pairs.

9

1

2

3

4

{

'line': 2,

'properties': { 'gift\_wrap': true }

}

Whenever a `POST` request includes `properties`, it overwrites the entire `properties` object. Any key-value pairs that were already in the `properties` object are erased.

It's not possible to set a line item's `properties` property to an empty object once a value is set. If you need to remove all line item properties, then you need to remove the entire line item.

Tip

You can visually hide line item properties at checkout by creating [private properties](#private-properties-and-attributes). This technique might be an alternative to removing a line item when managing `properties`.

**Tip:**

You can visually hide line item properties at checkout by creating [private properties](#private-properties-and-attributes). This technique might be an alternative to removing a line item when managing `properties`.

### [Anchor to Update selling plans](/docs/api/ajax/reference/cart#update-selling-plans)Update selling plans

The `selling_plan` property sets the [line item selling plan](/docs/api/liquid/objects/line_item#line_item-selling_plan_allocation). Its value must be one of the following:

* The [selling plan ID](/docs/api/liquid/objects/selling_plan#selling_plan-id): To set a specific selling plan for the line item.
* `null` or an empty string: To remove any selling plan from the line item.

9

1

2

3

4

5

{

'line': 2,

'quantity': 2,

'selling\_plan': 183638

}

9

1

2

3

4

5

{

'line': 2,

'quantity': 2,

'selling\_plan': null

}

##### Add selling plan

```liquid
{
  'line': 2,
  'quantity': 2,
  'selling_plan': 183638
}
```

##### Remove selling plan

```liquid
{
  'line': 2,
  'quantity': 2,
  'selling_plan': null
}
```

Note

When specifying the `selling_plan` property, consider the following:

* You can use only the [`line` property](#the-line-property) for identifying the line item.
* You should always specify the `quantity` property. If the `quantity` isn't specified, then it's assumed to be 1.

**Note:**

When specifying the `selling_plan` property, consider the following:

* You can use only the [`line` property](#the-line-property) for identifying the line item.
* You should always specify the `quantity` property. If the `quantity` isn't specified, then it's assumed to be 1.

### [Anchor to Response](/docs/api/ajax/reference/cart#response)Response

The JSON of the cart.

### [Anchor to Error responses](/docs/api/ajax/reference/cart#error-responses)Error responses

If the item that you're attempting to change isn't already in the cart, then `/{locale}/cart/change.js` doesn't add it. Instead, it returns a `400` error:

9

1

2

3

4

5

{

"status": "bad\_request",

"message": "no valid id or line parameter",

"description": "no valid id or line parameter"

}

---

## [Anchor to POST /{locale}/cart/clear.js](/docs/api/ajax/reference/cart#post--locale-cart-clearjs)POST /{locale}/cart/clear.js

Use the `POST /{locale}/cart/clear.js` endpoint to set all quantities of all line items in the cart to zero.

### [Anchor to Response](/docs/api/ajax/reference/cart#response)Response

The JSON of an empty cart. This does not remove cart attributes or the cart note.

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

{

"token": "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",

"note": null,

"attributes": {},

"total\_price": 0,

"total\_weight": 0,

"item\_count": 0,

"items": [],

"requires\_shipping": false

}

---

## [Anchor to Generate shipping rates](/docs/api/ajax/reference/cart#generate-shipping-rates)Generate shipping rates

Use the `POST /{locale}/cart/prepare_shipping_rates.json` and `GET /{locale}/cart/async_shipping_rates.json` endpoints to generate shipping rates:

* The `POST /{locale}/cart/prepare_shipping_rates.json` endpoint initiates the process of calculating shipping rates for the cart given a destination.
* The `GET /{locale}/cart/async_shipping_rates.json` endpoint returns the shipping rates results if the calculations have finished.

### [Anchor to Example ,[object Object], call](/docs/api/ajax/reference/cart#example-prepare_shipping_rates-call)Example `prepare_shipping_rates` call

9

1

/{locale}/cart/prepare\_shipping\_rates.json?shipping\_address%5Bzip%5D=K1N+5T2&shipping\_address%5Bcountry%5D=Canada&shipping\_address%5Bprovince%5D=Ontario

#### [Anchor to Response](/docs/api/ajax/reference/cart#response)Response

`null`

### [Anchor to Example ,[object Object], call](/docs/api/ajax/reference/cart#example-async_shipping_rates-call)Example `async_shipping_rates` call

9

1

/{locale}/cart/async\_shipping\_rates.json?shipping\_address%5Bzip%5D=K1N+5T2&shipping\_address%5Bcountry%5D=Canada&shipping\_address%5Bprovince%5D=Ontario

If you call `async_shipping_rates` with the same parameters as `prepare_shipping_rates`, then it checks whether Shopify has finished calculating the rates. If the shipping rates aren't ready, then the response is `null`.

If the shipping rates are ready, the rates are returned:

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

{

"shipping\_rates": [

{

"name": "Generic Rate",

"presentment\_name": "Generic Rate",

"code": "Generic Rate",

"price": "6.00",

"markup": null,

"source": "shopify",

"delivery\_date": null,

"delivery\_range": null,

"delivery\_days": [],

"compare\_price": null,

"phone\_required": false,

"currency": null,

"carrier\_identifier": null,

"delivery\_category": null,

"using\_merchant\_account": null,

"carrier\_service\_id": null,

"description": null,

"api\_client\_id": null,

"requested\_fulfillment\_service\_id": null,

"shipment\_options": null,

"charge\_items": null,

"has\_restrictions": null,

"rating\_classification": null,

"accepts\_instructions": false

},

{

"name": "Carrier Service Mail",

"presentment\_name": "Carrier Service Mail",

"code": "CarrierServiceMail",

"price": "12.46",

"markup": "0.00",

"source": "usps",

"delivery\_date": "2020-10-09",

"delivery\_range": [

"2020-10-06",

"2020-10-09"

],

"delivery\_days": [

0,

3

],

"compare\_price": null,

"phone\_required": true,

"currency": null,

"carrier\_identifier": null,

"delivery\_category": null,

"using\_merchant\_account": null,

"carrier\_service\_id": 2,

"description": null,

"api\_client\_id": null,

"requested\_fulfillment\_service\_id": null,

"shipment\_options": null,

"charge\_items": null,

"has\_restrictions": null,

"rating\_classification": null,

"accepts\_instructions": false

}

]

}

### [Anchor to GET /{locale}/cart/shipping\_rates.json](/docs/api/ajax/reference/cart#get--locale-cart-shipping_ratesjson)GET /{locale}/cart/shipping\_rates.json

Use the `GET /{locale}/cart/shipping_rates.json` to get estimated shipping rates.

Note

The recommended method to generate shipping rates is to use the `POST /{locale}/cart/prepare_shipping_rates.json` and `GET /{locale}/cart/async_shipping_rates.json` endpoints because it might take a while for shipping rates to be returned. The `GET /{locale}/cart/shipping_rates.json` endpoint is subject to throttling.

**Note:**

The recommended method to generate shipping rates is to use the `POST /{locale}/cart/prepare_shipping_rates.json` and `GET /{locale}/cart/async_shipping_rates.json` endpoints because it might take a while for shipping rates to be returned. The `GET /{locale}/cart/shipping_rates.json` endpoint is subject to throttling.

9

1

/{locale}/cart/shipping\_rates.json?shipping\_address%5Bzip%5D=K1N+5T2&shipping\_address%5Bcountry%5D=Canada&shipping\_address%5Bprovince%5D=Ontario

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

{

"shipping\_rates": [

{

"name": "Ground Shipping",

"price": "8.00",

"delivery\_date": null,

"source": "shopify"

},

{

"name": "Expedited Shipping",

"price": "15.00",

"delivery\_date": null,

"source": "shopify"

},

{

"name": "Express Shipping",

"price": "30.00",

"delivery\_date": null,

"source": "shopify"

}

]

}

---

## [Anchor to Private properties and attributes](/docs/api/ajax/reference/cart#private-properties-and-attributes)Private properties and attributes

Private line item properties and private cart attributes are used when you need to attach information to either cart line items or the entire cart, and you don't want the properties and attributes to be visible to the online store's visitors.

Both private properties and private cart attributes are visually hidden at checkout, but are visible on the **Order details** page in the Shopify admin.

Caution

If you hide private line item properties on the storefront, then you must [modify your theme's codebase](#hide-properties-in-a-theme).

**Caution:**

If you hide private line item properties on the storefront, then you must [modify your theme's codebase](#hide-properties-in-a-theme).

### [Anchor to Private line item properties](/docs/api/ajax/reference/cart#private-line-item-properties)Private line item properties

To make a line item property private, prepend an underscore (`_`) to the key. For example, to add a variant to cart with a private `_foo` property using the `/{locale}/cart/add.js` endpoint:

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

items: [

{

'quantity': 2,

'id': 794864229,

'properties': {

'\_foo': 'bar'

}

}

]

The `properties` property can have a mix of private and public line item properties:

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

items: [

{

quantity: 2,

id: 794864229,

properties: {

'\_foo': 'bar',

'gift\_wrap': true

}

}

]

#### [Anchor to Hide properties in a theme](/docs/api/ajax/reference/cart#hide-properties-in-a-theme)Hide properties in a theme

Private line item properties are available in the Liquid [`line_item.properties`](/docs/api/liquid/objects/line_item#line_item-properties) object and Ajax API. To hide private properties on the storefront, you must modify the theme's codebase.

In the following example, all `properties` items that begin with `_` in Liquid are filtered out:

9

1

2

3

4

5

6

{% for property in line\_item.properties %}

{% assign first\_character\_in\_key = property.first | slice: 0 %}

{% unless first\_character\_in\_key == '\_' %}

{{ property.first }}: {{ property.last }}

{% endunless %}

{% endfor %}

### [Anchor to Private cart attributes](/docs/api/ajax/reference/cart#private-cart-attributes)Private cart attributes

To make a cart attribute private, append a double underscore (`__`) to an attribute name.

Private cart attributes are not available in the Liquid [`cart.attributes`](/docs/api/liquid/objects/cart#cart-attributes) object or the Ajax API. This means there is no code modification required to hide them in theme files. Private cart attributes also do not affect the page rendering, which allows for more effective page caching.

---

## [Anchor to Bundled section rendering](/docs/api/ajax/reference/cart#bundled-section-rendering)Bundled section rendering

Bundled section rendering allows you to request the HTML markup for up to five sections you might want to update based on an initial call to the Cart API, within that same call.

Bundled section rendering is available for the following Cart API endpoints:

* `/{locale}/cart/add`
* `/{locale}/cart/change`
* `/{locale}/cart/clear`
* `/{locale}/cart/update`

### [Anchor to Request sections](/docs/api/ajax/reference/cart#request-sections)Request sections

To request sections, you can include a `sections` parameter in your API call data:

9

1

2

3

4

5

6

7

items: [

{

id: 36110175633573,

quantity: 2

}

],

sections: "cart-items,cart-icon-bubble,cart-live-region-text,cart-footer"

Note

The `sections` parameter can be a comma-separated list or an array, similar to when using the [Section Rendering API](/docs/api/ajax/section-rendering) directly.

**Note:**

The `sections` parameter can be a comma-separated list or an array, similar to when using the [Section Rendering API](/docs/api/ajax/section-rendering) directly.

By default, sections are rendered in the context of the current page, based on the [HTTP Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header. However, you can specify any other page using the `sections_url` parameter. The `sections_url` must begin with a `/` and can include query parameters like `q` and `page`.

9

1

2

sections: "cart-items,cart-icon-bubble,cart-live-region-text,cart-footer",

sections\_url: "/cart?some\_param=foo"

The HTML for the requested sections is included under the `sections` key of the returned JSON. Each section can be identified by the same ID that was passed in the request.

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

{

attributes: {},

cart\_level\_discount\_applications: [],

currency: "CAD",

item\_count: 1,

items: [{…}],

items\_subtotal\_price: 100100,

note: null,

original\_total\_price: 100100,

requires\_shipping: true,

sections: {

cart-items: "<div id=\"shopify-section-template--14199693705272\_…9930913703934\" defer=\"defer\"></script>\n\n\n\n\n</div>",

cart-icon-bubble: "<div id=\"shopify-section-cart-icon-bubble\" className=\"…ss=\"visually-hidden\">1 item</span>\n </div></div>",

cart-live-region-text: "<div id=\"shopify-section-cart-live-region-text\" cl…opify-section\">New subtotal: $1,001.00 CAD\n</div>",

cart-footer: "<div id=\"shopify-section-template--14199693705272\_… </div>\n </div>\n </div>\n</div>\n\n\n\n\n\n\n</div>"

},

token: "Z2NwLXVzLXdlc3QxOjAxSjBQTVk1Sjc5NVFKTjNOVlhLWENXQUI1?key=0d9909213054e22d092152de385763f0",

total\_discount: 0,

total\_price: 100100,

total\_weight: 1000,

}

### [Anchor to Error response](/docs/api/ajax/reference/cart#error-response)Error response

Sections are rendered after the data modifications from the request are completed. Because of this, rendering errors don't affect the response status of the API call. Sections that fail to render are returned as `null`, so you should account for this possibility.

Passing invalid values for the `sections` or `sections_url` parameters, such as a `sections_url` that doesn't begin with `/`, causes the entire request to return an **HTTP 400 Bad Request** status. However, this doesn't mean that the rest of the request didn't succeed.

---

Was this page helpful?

YesNo