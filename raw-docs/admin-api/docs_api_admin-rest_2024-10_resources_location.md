---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/location
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# Location

Ask assistant

A location represents a geographical location where your stores, pop-up stores, headquarters,
and warehouses exist. You can use the Location resource to track sales, manage inventory,
and configure the tax rates to apply at checkout. For a better understanding of the relationship
between locations, inventory levels and inventory items, refer to the
[InventoryLevel](/api/admin-rest/latest/resources/inventorylevel) resource reference documentation

Was this section helpful?

YesNo

#

## Endpoints

* [get

  /admin/api/latest/locations.json](/docs/api/admin-rest/latest/resources/location#get-locations)

  Retrieve a list of locations

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  locations](/docs/api/admin-graphql/latest/queries/locations?example=retrieve-a-list-of-locations)
* [get

  /admin/api/latest/locations/{location\_id}.json](/docs/api/admin-rest/latest/resources/location#get-locations-location-id)

  Retrieve a single location by its ID

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  location](/docs/api/admin-graphql/latest/queries/location?example=retrieve-a-single-location-by-its-id)
* [get

  /admin/api/latest/locations/{location\_id}/inventory\_levels.json](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-inventory-levels)

  Retrieve a list of inventory levels for a location

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  location](/docs/api/admin-graphql/latest/queries/location?example=retrieve-a-list-of-inventory-levels-for-a-location)
* [get

  /admin/api/latest/locations/count.json](/docs/api/admin-rest/latest/resources/location#get-locations-count)

  Retrieve a count of locations

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  locationsCount](/docs/api/admin-graphql/latest/queries/locationsCount?example=retrieve-a-count-of-locations)

---

[Anchor to](/docs/api/admin-rest/latest/resources/location#resource-object) 

## The Location resource

[Anchor to](/docs/api/admin-rest/latest/resources/location#resource-object-properties) 

### Properties

---

active

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

isActive](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.isActive)

Whether the location is active. If `true`, then the location can be used to sell products,
stock inventory, and fulfill orders. Merchants can deactivate locations from the Shopify admin.
Deactivated locations don't contribute to the shop's
[location limit](https://help.shopify.com/manual/locations/setting-up-your-locations).

---

address1

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

address1](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.address1)

The location's street address.

---

address2

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

address2](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.address2)

The optional second line of the location's street address.

---

city

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

city](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.city)

The city the location is in.

---

country

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

country](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.country)

The country the location is in.

---

country\_code

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

countryCode](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.countryCode)

The two-letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) corresponding to country the location is in.

---

created\_at

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

createdAt](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the location was created.

---

id

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

id](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id)

The ID of the location.

---

legacy

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

isFulfillmentService](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.isFulfillmentService)

Whether this is a fulfillment service location. If `true`, then the location is a
fulfillment service location. If `false`, then the location was created by the
merchant and isn't tied to a fulfillment service.

---

name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

name](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.name)

The name of the location.

---

phone

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

phone](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.phone)

The phone number of the location. This value can contain special characters, such as `-` or `+`.

---

province

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

province](/docs/api/admin-graphql/latest/objects/LocationAddress#field-LocationAddress.fields.province)

The province, state, or district of the location.

---

Show 5 hidden fields

Was this section helpful?

YesNo

{}

## The Location resource

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

{

"active": true,

"address1": "126 York Street",

"address2": "Unit 42",

"city": "Ottawa",

"country": "Canada",

"country\_code": "CA",

"created\_at": "2008-12-31T19:00:00-05:00",

"id": 121,

"legacy": true,

"name": "Ottawa Store",

"phone": "18883290139",

"province": "Ontario",

"province\_code": "ON",

"updated\_at": "2009-01-31T19:00:00-05:00",

"zip": "k1n5t5",

"localized\_country\_name": "Canada",

"localized\_province\_name": "Ontario"

}

---

## [Anchor to GET request, Retrieve a list of locations](/docs/api/admin-rest/latest/resources/location#get-locations) get Retrieve a list of locations

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

locations](/docs/api/admin-graphql/latest/queries/locations?example=retrieve-a-list-of-locations)

Retrieve a list of locations. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieve a list of locations](/docs/api/admin-rest/latest/resources/location#get-locations-parameters)Parameters

---

api\_version

string**string**

required**required**

---

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

---

Was this section helpful?

YesNo

### [Anchor to get-locations-examples](/docs/api/admin-rest/latest/resources/location#get-locations-examples)Examples

Retrieve a list of all locations

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations.json" \

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

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

HTTP/1.1 200 OK

{

"locations": [

{

"id": 655441491,

"name": "50 Rideau Street",

"address1": "50 Rideau Street",

"address2": null,

"city": "Ottawa",

"zip": "K1N 9J7",

"province": "Ontario",

"country": "CA",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "CA",

"country\_name": "Canada",

"province\_code": "ON",

"legacy": false,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/655441491",

"localized\_country\_name": "Canada",

"localized\_province\_name": "Ontario"

},

{

"id": 24826418,

"name": "Apple Api Shipwire",

"address1": null,

"address2": null,

"city": null,

"zip": null,

"province": null,

"country": "DE",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "DE",

"country\_name": "Germany",

"province\_code": null,

"legacy": true,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/24826418",

"localized\_country\_name": "Germany",

"localized\_province\_name": null

},

{

"id": 844681632,

"name": "Apple Cupertino",

"address1": "One Apple Park Way",

"address2": null,

"city": "Cupertino",

"zip": "95014",

"province": "California",

"country": "US",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "US",

"country\_name": "United States",

"province\_code": "CA",

"legacy": false,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/844681632",

"localized\_country\_name": "United States",

"localized\_province\_name": "California"

},

{

"id": 611870435,

"name": "Apple Shipwire",

"address1": null,

"address2": null,

"city": null,

"zip": null,

"province": null,

"country": "DE",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "DE",

"country\_name": "Germany",

"province\_code": null,

"legacy": true,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/611870435",

"localized\_country\_name": "Germany",

"localized\_province\_name": null

},

{

"id": 487838322,

"name": "Fifth Avenue AppleStore",

"address1": null,

"address2": null,

"city": null,

"zip": null,

"province": null,

"country": "US",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "US",

"country\_name": "United States",

"province\_code": null,

"legacy": false,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/487838322",

"localized\_country\_name": "United States",

"localized\_province\_name": null

}

]

}

### examples

* #### Retrieve a list of all locations

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Location.all({
    session: session,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Location.all(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Location.all({
    session: session,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"locations":[{"id":655441491,"name":"50 Rideau Street","address1":"50 Rideau Street","address2":null,"city":"Ottawa","zip":"K1N 9J7","province":"Ontario","country":"CA","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"CA","country_name":"Canada","province_code":"ON","legacy":false,"active":true,"admin_graphql_api_id":"gid://shopify/Location/655441491","localized_country_name":"Canada","localized_province_name":"Ontario"},{"id":24826418,"name":"Apple Api Shipwire","address1":null,"address2":null,"city":null,"zip":null,"province":null,"country":"DE","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"DE","country_name":"Germany","province_code":null,"legacy":true,"active":true,"admin_graphql_api_id":"gid://shopify/Location/24826418","localized_country_name":"Germany","localized_province_name":null},{"id":844681632,"name":"Apple Cupertino","address1":"One Apple Park Way","address2":null,"city":"Cupertino","zip":"95014","province":"California","country":"US","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"US","country_name":"United States","province_code":"CA","legacy":false,"active":true,"admin_graphql_api_id":"gid://shopify/Location/844681632","localized_country_name":"United States","localized_province_name":"California"},{"id":611870435,"name":"Apple Shipwire","address1":null,"address2":null,"city":null,"zip":null,"province":null,"country":"DE","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"DE","country_name":"Germany","province_code":null,"legacy":true,"active":true,"admin_graphql_api_id":"gid://shopify/Location/611870435","localized_country_name":"Germany","localized_province_name":null},{"id":487838322,"name":"Fifth Avenue AppleStore","address1":null,"address2":null,"city":null,"zip":null,"province":null,"country":"US","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"US","country_name":"United States","province_code":null,"legacy":false,"active":true,"admin_graphql_api_id":"gid://shopify/Location/487838322","localized_country_name":"United States","localized_province_name":null}]}
  ```

---

## [Anchor to GET request, Retrieve a single location by its ID](/docs/api/admin-rest/latest/resources/location#get-locations-location-id) get Retrieve a single location by its ID

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

location](/docs/api/admin-graphql/latest/queries/location?example=retrieve-a-single-location-by-its-id)

Retrieve a single location by its ID.

### [Anchor to Parameters of Retrieve a single location by its ID](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

location\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-locations-location-id-examples](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-examples)Examples

Retrieve a single location

Path parameters

location\_id=487838322

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/487838322.json" \

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

"location": {

"id": 487838322,

"name": "Fifth Avenue AppleStore",

"address1": null,

"address2": null,

"city": null,

"zip": null,

"province": null,

"country": "US",

"phone": null,

"created\_at": "2026-01-09T17:04:11-05:00",

"updated\_at": "2026-01-09T17:04:11-05:00",

"country\_code": "US",

"country\_name": "United States",

"province\_code": null,

"legacy": false,

"active": true,

"admin\_graphql\_api\_id": "gid://shopify/Location/487838322"

}

}

### examples

* #### Retrieve a single location

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/487838322.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Location.find({
    session: session,
    id: 487838322,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Location.find(
    session: test_session,
    id: 487838322,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Location.find({
    session: session,
    id: 487838322,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"location":{"id":487838322,"name":"Fifth Avenue AppleStore","address1":null,"address2":null,"city":null,"zip":null,"province":null,"country":"US","phone":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","country_code":"US","country_name":"United States","province_code":null,"legacy":false,"active":true,"admin_graphql_api_id":"gid://shopify/Location/487838322"}}
  ```

---

## [Anchor to GET request, Retrieve a list of inventory levels for a location](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-inventory-levels) get Retrieve a list of inventory levels for a location

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

location](/docs/api/admin-graphql/latest/queries/location?example=retrieve-a-list-of-inventory-levels-for-a-location)

Retrieve a list of inventory levels for a location. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieve a list of inventory levels for a location](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-inventory-levels-parameters)Parameters

---

api\_version

string**string**

required**required**

---

location\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-locations-location-id-inventory-levels-examples](/docs/api/admin-rest/latest/resources/location#get-locations-location-id-inventory-levels-examples)Examples

Retrieve a list of all inventory for a location by its ID

Path parameters

location\_id=487838322

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/487838322/inventory\_levels.json" \

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

HTTP/1.1 200 OK

{

"inventory\_levels": [

{

"inventory\_item\_id": 49148385,

"location\_id": 487838322,

"available": 18,

"updated\_at": "2026-01-09T17:04:11-05:00",

"admin\_graphql\_api\_id": "gid://shopify/InventoryLevel/548380009?inventory\_item\_id=49148385"

},

{

"inventory\_item\_id": 808950810,

"location\_id": 487838322,

"available": 9,

"updated\_at": "2026-01-09T17:04:11-05:00",

"admin\_graphql\_api\_id": "gid://shopify/InventoryLevel/548380009?inventory\_item\_id=808950810"

},

{

"inventory\_item\_id": 457924702,

"location\_id": 487838322,

"available": 36,

"updated\_at": "2026-01-09T17:04:11-05:00",

"admin\_graphql\_api\_id": "gid://shopify/InventoryLevel/548380009?inventory\_item\_id=457924702"

},

{

"inventory\_item\_id": 39072856,

"location\_id": 487838322,

"available": 27,

"updated\_at": "2026-01-09T17:04:11-05:00",

"admin\_graphql\_api\_id": "gid://shopify/InventoryLevel/548380009?inventory\_item\_id=39072856"

}

]

}

### examples

* #### Retrieve a list of all inventory for a location by its ID

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/487838322/inventory_levels.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Location.inventory_levels({
    session: session,
    id: 487838322,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Location.inventory_levels(
    session: test_session,
    id: 487838322,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Location.inventory_levels({
    session: session,
    id: 487838322,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"inventory_levels":[{"inventory_item_id":49148385,"location_id":487838322,"available":18,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=49148385"},{"inventory_item_id":808950810,"location_id":487838322,"available":9,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=808950810"},{"inventory_item_id":457924702,"location_id":487838322,"available":36,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=457924702"},{"inventory_item_id":39072856,"location_id":487838322,"available":27,"updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/InventoryLevel/548380009?inventory_item_id=39072856"}]}
  ```

---

## [Anchor to GET request, Retrieve a count of locations](/docs/api/admin-rest/latest/resources/location#get-locations-count) get Retrieve a count of locations

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

locationsCount](/docs/api/admin-graphql/latest/queries/locationsCount?example=retrieve-a-count-of-locations)

Retrieve a count of locations.

### [Anchor to Parameters of Retrieve a count of locations](/docs/api/admin-rest/latest/resources/location#get-locations-count-parameters)Parameters

---

api\_version

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-locations-count-examples](/docs/api/admin-rest/latest/resources/location#get-locations-count-examples)Examples

Count all store locations

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/count.json" \

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

"count": 5

}

### examples

* #### Count all store locations

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/locations/count.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Location.count({
    session: session,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Location.count(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Location.count({
    session: session,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"count":5}
  ```