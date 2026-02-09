---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/customer-address
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# Customer Address

Ask assistant

Requires `customers` access scope.

**Requires `customers` access scope.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

The Customer Address resource represents addresses that a customer has added. Each customer can have multiple addresses associated with them.

For more information about the Customer resource, see [*Customer*](/docs/admin-api/rest/reference/customers/customer).

Was this section helpful?

YesNo

#

## Endpoints

* [post

  /admin/api/latest/customers/{customer\_id}/addresses.json](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses)

  Creates a new address for a customer

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=creates-a-new-address-for-a-customer)
* [get

  /admin/api/latest/customers/{customer\_id}/addresses.json?limit=1](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1)

  Retrieves a list of addresses for a customer

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customer](/docs/api/admin-graphql/latest/queries/customer?example=retrieves-a-list-of-addresses-for-a-customer)
* [get

  /admin/api/latest/customers/{customer\_id}/addresses/{address\_id}.json](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id)

  Retrieves details for a single customer address

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customer](/docs/api/admin-graphql/latest/queries/customer)
* [put

  /admin/api/latest/customers/{customer\_id}/addresses/{address\_id}.json](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id)

  Updates an existing customer address

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=updates-an-existing-customer-address)
* [put

  /admin/api/latest/customers/{customer\_id}/addresses/{address\_id}/default.json](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default)

  Sets the default address for a customer

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=sets-the-default-address-for-a-customer)
* [put

  /admin/api/latest/customers/{customer\_id}/addresses/set.json?address\_ids[]=1053317346&operation=destroy](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy)

  Performs bulk operations for multiple customer addresses

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=performs-bulk-operations-for-multiple-customer-addresses)
* [del

  /admin/api/latest/customers/{customer\_id}/addresses/{address\_id}.json](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id)

  Removes an address from a customer’s address list

---

[Anchor to](/docs/api/admin-rest/latest/resources/customer-address#resource-object) 

## The Customer Address resource

[Anchor to](/docs/api/admin-rest/latest/resources/customer-address#resource-object-properties) 

### Properties

---

address1

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

address1](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.address1)

The customer's mailing address

---

address2

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

address2](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.address2)

An additional field for the customer's mailing address.

---

city

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

city](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.city)

The customer's city, town, or village.

---

country

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

country](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.country)

The customer's country.

---

country\_code

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

countryCodeV2](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.countryCodeV2)

The two-letter country code corresponding to the customer's country.

---

country\_name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

country](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.country)

The customer’s normalized country name.

---

company

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

company](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.company)

The customer’s company.

---

customer\_id

deprecated**deprecated**

The unique identifier for the customer.

---

first\_name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

firstName](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.firstName)

The customer’s first name.

---

id

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

id](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.id)

The unique identifier for the address.

---

last\_name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

lastName](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.lastName)

The customer’s last name.

---

name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

name](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.name)

The customer’s first and last names.

---

Show 4 hidden fields

Was this section helpful?

YesNo

{}

## The Customer Address resource

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

{

"address1": "1 Rue des Carrieres",

"address2": "Suite 1234",

"city": "Montreal",

"country": "Canada",

"country\_code": "CA",

"country\_name": "Canada",

"company": "Fancy Co.",

"customer\_id": {

"id": 1073339470

},

"first\_name": "Samuel",

"id": 207119551,

"last\_name": "de Champlain",

"name": "Samuel de Champlain",

"phone": "819-555-5555",

"province": "Quebec",

"province\_code": "QC",

"zip": "G1R 4P5"

}

---

## [Anchor to POST request, Creates a new address for a customer](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses) post Creates a new address for a customer

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=creates-a-new-address-for-a-customer)

Creates a new address for a customer.

### [Anchor to Parameters of Creates a new address for a customer](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses-parameters)Parameters

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to post-customers-customer-id-addresses-examples](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses-examples)Examples

Create a new address for a customer

Path parameters

customer\_id=207119551

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

curl -d '{"address":{"address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","company":"Fancy Co.","first\_name":"Samuel","last\_name":"de Champlain","phone":"819-555-5555","province":"Quebec","country":"Canada","zip":"G1R 4P5","name":"Samuel de Champlain","province\_code":"QC","country\_code":"CA","country\_name":"Canada"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \

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

HTTP/1.1 201 Created

{

"customer\_address": {

"id": 1053317349,

"customer\_id": 207119551,

"first\_name": "Samuel",

"last\_name": "de Champlain",

"company": "Fancy Co.",

"address1": "1 Rue des Carrieres",

"address2": "Suite 1234",

"city": "Montreal",

"province": "Quebec",

"country": "Canada",

"zip": "G1R 4P5",

"phone": "819-555-5555",

"name": "Samuel de Champlain",

"province\_code": "QC",

"country\_code": "CA",

"country\_name": "Canada",

"default": false

}

}

### examples

* #### Create a new address for a customer

  ##### 

  ```liquid
  curl -d '{"address":{"address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","company":"Fancy Co.","first_name":"Samuel","last_name":"de Champlain","phone":"819-555-5555","province":"Quebec","country":"Canada","zip":"G1R 4P5","name":"Samuel de Champlain","province_code":"QC","country_code":"CA","country_name":"Canada"}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const customer_address = new admin.rest.resources.CustomerAddress({session: session});

  customer_address.customer_id = 207119551;
  customer_address.address1 = "1 Rue des Carrieres";
  customer_address.address2 = "Suite 1234";
  customer_address.city = "Montreal";
  customer_address.company = "Fancy Co.";
  customer_address.first_name = "Samuel";
  customer_address.last_name = "de Champlain";
  customer_address.phone = "819-555-5555";
  customer_address.province = "Quebec";
  customer_address.country = "Canada";
  customer_address.zip = "G1R 4P5";
  customer_address.name = "Samuel de Champlain";
  customer_address.province_code = "QC";
  customer_address.country_code = "CA";
  customer_address.country_name = "Canada";
  await customer_address.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
  customer_address.customer_id = 207119551
  customer_address.address1 = "1 Rue des Carrieres"
  customer_address.address2 = "Suite 1234"
  customer_address.city = "Montreal"
  customer_address.company = "Fancy Co."
  customer_address.first_name = "Samuel"
  customer_address.last_name = "de Champlain"
  customer_address.phone = "819-555-5555"
  customer_address.province = "Quebec"
  customer_address.country = "Canada"
  customer_address.zip = "G1R 4P5"
  customer_address.name = "Samuel de Champlain"
  customer_address.province_code = "QC"
  customer_address.country_code = "CA"
  customer_address.country_name = "Canada"
  customer_address.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const customer_address = new shopify.rest.CustomerAddress({session: session});
  customer_address.customer_id = 207119551;
  customer_address.address1 = "1 Rue des Carrieres";
  customer_address.address2 = "Suite 1234";
  customer_address.city = "Montreal";
  customer_address.company = "Fancy Co.";
  customer_address.first_name = "Samuel";
  customer_address.last_name = "de Champlain";
  customer_address.phone = "819-555-5555";
  customer_address.province = "Quebec";
  customer_address.country = "Canada";
  customer_address.zip = "G1R 4P5";
  customer_address.name = "Samuel de Champlain";
  customer_address.province_code = "QC";
  customer_address.country_code = "CA";
  customer_address.country_name = "Canada";
  await customer_address.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"customer_address":{"id":1053317349,"customer_id":207119551,"first_name":"Samuel","last_name":"de Champlain","company":"Fancy Co.","address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","province":"Quebec","country":"Canada","zip":"G1R 4P5","phone":"819-555-5555","name":"Samuel de Champlain","province_code":"QC","country_code":"CA","country_name":"Canada","default":false}}
  ```

---

## [Anchor to GET request, Retrieves a list of addresses for a customer](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1) get Retrieves a list of addresses for a customer

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customer](/docs/api/admin-graphql/latest/queries/customer?example=retrieves-a-list-of-addresses-for-a-customer)

Retrieves a list of addresses for a customer. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieves a list of addresses for a customer](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1-parameters)Parameters

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-customers-customer-id-addresses?limit=1-examples](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1-examples)Examples

Retrieve a limited number of addresses for a customer

Query parameters

Retrieve all of a customer’s addresses

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json?limit=1" \

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

HTTP/1.1 200 OK

{

"addresses": [

{

"id": 207119551,

"customer\_id": 207119551,

"first\_name": null,

"last\_name": null,

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"country": "United States",

"zip": "40202",

"phone": "555-625-1199",

"name": "",

"province\_code": "KY",

"country\_code": "US",

"country\_name": "United States",

"default": true

}

]

}

### examples

* #### Retrieve a limited number of addresses for a customer

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json?limit=1" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.CustomerAddress.all({
    session: session,
    customer_id: 207119551,
    limit: "1",
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::CustomerAddress.all(
    session: test_session,
    customer_id: 207119551,
    limit: "1",
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.CustomerAddress.all({
    session: session,
    customer_id: 207119551,
    limit: "1",
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}]}
  ```
* #### Retrieve all of a customer’s addresses

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.CustomerAddress.all({
    session: session,
    customer_id: 207119551,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::CustomerAddress.all(
    session: test_session,
    customer_id: 207119551,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.CustomerAddress.all({
    session: session,
    customer_id: 207119551,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}]}
  ```

---

## [Anchor to GET request, Retrieves details for a single customer address](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id) get Retrieves details for a single customer address

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customer](/docs/api/admin-graphql/latest/queries/customer)

Retrieves details for a single customer address.

### [Anchor to Parameters of Retrieves details for a single customer address](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id-parameters)Parameters

---

address\_id

string**string**

required**required**

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id-examples)Examples

Retrieve a single customer address

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \

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

HTTP/1.1 200 OK

{

"customer\_address": {

"id": 207119551,

"customer\_id": 207119551,

"first\_name": null,

"last\_name": null,

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"country": "United States",

"zip": "40202",

"phone": "555-625-1199",

"name": "",

"province\_code": "KY",

"country\_code": "US",

"country\_name": "United States",

"default": true

}

}

### examples

* #### Retrieve a single customer address

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.CustomerAddress.find({
    session: session,
    customer_id: 207119551,
    id: 207119551,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::CustomerAddress.find(
    session: test_session,
    customer_id: 207119551,
    id: 207119551,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.CustomerAddress.find({
    session: session,
    customer_id: 207119551,
    id: 207119551,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"customer_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}
  ```

---

## [Anchor to PUT request, Updates an existing customer address](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id) put Updates an existing customer address

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=updates-an-existing-customer-address)

Updates an existing customer address.

### [Anchor to Parameters of Updates an existing customer address](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-parameters)Parameters

---

address\_id

string**string**

required**required**

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to put-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-examples)Examples

Update the postal code of a customer address

Update the street address of a customer address

Was this section helpful?

YesNo

9

1

2

3

4

5

curl -d '{"address":{"id":207119551,"zip":"90210"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \

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

HTTP/1.1 200 OK

{

"customer\_address": {

"customer\_id": 207119551,

"zip": "90210",

"country": "United States",

"province": "Kentucky",

"city": "Louisville",

"address1": "Chestnut Street 92",

"address2": "",

"first\_name": null,

"last\_name": null,

"company": null,

"phone": "555-625-1199",

"id": 207119551,

"name": "",

"province\_code": "KY",

"country\_code": "US",

"country\_name": "United States",

"default": true

}

}

### examples

* #### Update the postal code of a customer address

  ##### 

  ```liquid
  curl -d '{"address":{"id":207119551,"zip":"90210"}}' \
  -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const customer_address = new admin.rest.resources.CustomerAddress({session: session});

  customer_address.customer_id = 207119551;
  customer_address.id = 207119551;
  customer_address.zip = "90210";
  await customer_address.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
  customer_address.customer_id = 207119551
  customer_address.id = 207119551
  customer_address.zip = "90210"
  customer_address.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const customer_address = new shopify.rest.CustomerAddress({session: session});
  customer_address.customer_id = 207119551;
  customer_address.id = 207119551;
  customer_address.zip = "90210";
  await customer_address.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"customer_address":{"customer_id":207119551,"zip":"90210","country":"United States","province":"Kentucky","city":"Louisville","address1":"Chestnut Street 92","address2":"","first_name":null,"last_name":null,"company":null,"phone":"555-625-1199","id":207119551,"name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}
  ```
* #### Update the street address of a customer address

  ##### 

  ```liquid
  curl -d '{"address":{"id":207119551,"address1":"Apartment 23","address2":"Chestnut Street 92"}}' \
  -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const customer_address = new admin.rest.resources.CustomerAddress({session: session});

  customer_address.customer_id = 207119551;
  customer_address.id = 207119551;
  customer_address.address1 = "Apartment 23";
  customer_address.address2 = "Chestnut Street 92";
  await customer_address.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
  customer_address.customer_id = 207119551
  customer_address.id = 207119551
  customer_address.address1 = "Apartment 23"
  customer_address.address2 = "Chestnut Street 92"
  customer_address.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const customer_address = new shopify.rest.CustomerAddress({session: session});
  customer_address.customer_id = 207119551;
  customer_address.id = 207119551;
  customer_address.address1 = "Apartment 23";
  customer_address.address2 = "Chestnut Street 92";
  await customer_address.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"customer_address":{"customer_id":207119551,"address1":"Apartment 23","address2":"Chestnut Street 92","country":"United States","province":"Kentucky","zip":"40202","city":"Louisville","first_name":null,"last_name":null,"company":null,"phone":"555-625-1199","id":207119551,"name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}
  ```

---

## [Anchor to PUT request, Sets the default address for a customer](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default) put Sets the default address for a customer

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=sets-the-default-address-for-a-customer)

Sets the default address for a customer.

### [Anchor to Parameters of Sets the default address for a customer](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default-parameters)Parameters

---

address\_id

string**string**

required**required**

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to put-customers-customer-id-addresses-address-id-default-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default-examples)Examples

Set a default address for a customer

Was this section helpful?

YesNo

9

1

2

3

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317347/default.json" \

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

HTTP/1.1 200 OK

{

"customer\_address": {

"id": 1053317347,

"customer\_id": 207119551,

"first\_name": null,

"last\_name": null,

"company": null,

"address1": "123 Test St",

"address2": null,

"city": "Ottawa",

"province": "Ontario",

"country": "Canada",

"zip": null,

"phone": null,

"name": "",

"province\_code": "ON",

"country\_code": "CA",

"country\_name": "Canada",

"default": true

}

}

### examples

* #### Set a default address for a customer

  ##### 

  ```liquid
  curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317347/default.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const customer_address = new admin.rest.resources.CustomerAddress({session: session});

  customer_address.customer_id = 207119551;
  customer_address.id = 1053317347;
  await customer_address.default({});
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
  customer_address.customer_id = 207119551
  customer_address.id = 1053317347
  customer_address.default(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const customer_address = new shopify.rest.CustomerAddress({session: session});
  customer_address.customer_id = 207119551;
  customer_address.id = 1053317347;
  await customer_address.default({});
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"customer_address":{"id":1053317347,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"123 Test St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":null,"phone":null,"name":"","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}
  ```

---

## [Anchor to PUT request, Performs bulk operations for multiple customer addresses](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy) put Performs bulk operations for multiple customer addresses

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=performs-bulk-operations-for-multiple-customer-addresses)

Performs bulk operations for multiple customer addresses.

### [Anchor to Parameters of Performs bulk operations for multiple customer addresses](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy-parameters)Parameters

---

address\_ids[]

required**required**

Performs bulk operations on a list of customer address IDs. Format: `address_ids[]=1&address_ids[]=2&address_ids[]=3`.

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

operation

required**required**

Operation to perform by keyword (for example, destroy)

---

Was this section helpful?

YesNo

### [Anchor to put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy-examples)Examples

Destroy multiple customer addresses

Query parameters

address\_ids[]=1053317346

required**required**

Performs bulk operations on a list of customer address IDs. Format: `address_ids[]=1&address_ids[]=2&address_ids[]=3`.

operation=destroy

required**required**

Operation to perform by keyword (for example, destroy)

Was this section helpful?

YesNo

9

1

2

3

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/set.json?address\_ids%5B%5D=1053317346&operation=destroy" \

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

* #### Destroy multiple customer addresses

  ##### 

  ```liquid
  curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/set.json?address_ids%5B%5D=1053317346&operation=destroy" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const customer_address = new admin.rest.resources.CustomerAddress({session: session});

  customer_address.customer_id = 207119551;
  await customer_address.set({
    address_ids: ["1053317346"],
    operation: "destroy",
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
  customer_address.customer_id = 207119551
  customer_address.set(
    session: test_session,
    address_ids: ["1053317346"],
    operation: "destroy",
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const customer_address = new shopify.rest.CustomerAddress({session: session});
  customer_address.customer_id = 207119551;
  await customer_address.set({
    address_ids: ["1053317346"],
    operation: "destroy",
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{}
  ```

---

## [Anchor to DELETE request, Removes an address from a customer’s address list](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id) del Removes an address from a customer’s address list

Removes an address from a customer’s address list.

### [Anchor to Parameters of Removes an address from a customer’s address list](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id-parameters)Parameters

---

address\_id

string**string**

required**required**

---

api\_version

string**string**

required**required**

---

customer\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to delete-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id-examples)Examples

Remove a customer address

Removing a customer’s default address fails and returns an error

Was this section helpful?

YesNo

9

1

2

3

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317348.json" \

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

* #### Remove a customer address

  ##### 

  ```liquid
  curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317348.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.CustomerAddress.delete({
    session: session,
    customer_id: 207119551,
    id: 1053317348,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::CustomerAddress.delete(
    session: test_session,
    customer_id: 207119551,
    id: 1053317348,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.CustomerAddress.delete({
    session: session,
    customer_id: 207119551,
    id: 1053317348,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{}
  ```
* #### Removing a customer’s default address fails and returns an error

  ##### 

  ```liquid
  curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.CustomerAddress.delete({
    session: session,
    customer_id: 207119551,
    id: 207119551,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::CustomerAddress.delete(
    session: test_session,
    customer_id: 207119551,
    id: 207119551,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.CustomerAddress.delete({
    session: session,
    customer_id: 207119551,
    id: 207119551,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 422 Unprocessable Entity{"errors":{"base":["Cannot delete the customer’s default address"]}}
  ```