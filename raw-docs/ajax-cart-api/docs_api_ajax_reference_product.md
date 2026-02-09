---
source: https://shopify.dev/docs/api/ajax/reference/product
---

You can make a `GET` request for the information of any product using the Ajax Product API.

All Ajax API requests should use [locale-aware URLs](/docs/api/ajax#locale-aware-urls) to give visitors a consistent experience.

---

## [Anchor to GET /{locale}/products/{product-handle}.js](/docs/api/ajax/reference/product#get--locale-products-product-handlejs)GET /{locale}/products/{product-handle}.js

Get the JSON of a product using the product [handle](/docs/api/liquid/basics/handle).

All monetary properties are returned in the customer's presentment currency. To check the customer's presentment currency, you can use the `currency` field of the `/{locale}/cart.js` endpoint. To learn more about selling in multiple currencies, see [Support multiple currencies and languages](/docs/storefronts/themes/markets/multiple-currencies-languages).

### [Anchor to Example](/docs/api/ajax/reference/product#example)Example

9

1

2

3

fetch(window.Shopify.routes.root + 'products/red-rain-coat.js')

.then(response => response.json())

.then(product => alert('The title of this product is ' + product.title));

---

## [Anchor to Response](/docs/api/ajax/reference/product#response)Response

The JSON of the product.

Example:

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

{

"id": 329678821,

"title": "Red Rain Coat",

"handle": "red-rain-coat",

"description": "<p>Lorem Ipsum.</p>",

"published\_at": "2014-06-12T16:28:11-04:00",

"created\_at": "2014-06-12T16:28:13-04:00",

"vendor": "Shopify",

"type": "Coat",

"tags": [

"Spring"

],

"price": 12900,

"price\_min": 12900,

"price\_max": 12900,

"available": true,

"price\_varies": false,

"compare\_at\_price": null,

"compare\_at\_price\_min": 0,

"compare\_at\_price\_max": 0,

"compare\_at\_price\_varies": false,

"variants": [

{

"id": 794864229,

"title": "Small",

"options": [

"Small"

],

"option1": "Small",

"option2": null,

"option3": null,

"price": 12900,

"weight": 0,

"compare\_at\_price": null,

"inventory\_management": "shopify",

"available": true,

"sku": null,

"requires\_shipping": true,

"taxable": true,

"barcode": "49738645"

},

{

"id": 794864233,

"title": "Medium",

"options": [

"Medium"

],

"option1": "Medium",

"option2": null,

"option3": null,

"price": 12900,

"weight": 0,

"compare\_at\_price": null,

"inventory\_management": "shopify",

"available": true,

"sku": null,

"requires\_shipping": true,

"taxable": true,

"barcode": "49738657"

},

{

"id": 794864237,

"title": "Large",

"options": [

"Large"

],

"option1": "Large",

"option2": null,

"option3": null,

"price": 12900,

"weight": 0,

"compare\_at\_price": null,

"inventory\_management": "shopify",

"available": true,

"sku": null,

"requires\_shipping": true,

"taxable": true,

"barcode": "49738673"

}

],

"images": [

"//cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893"

],

"featured\_image": "//cdn.shopify.com/s/files/1/0040/7092/products/red-rain-coat.jpeg?v=1402604893",

"options": [

{

"name": "Size",

"position": 1

}

],

"url": "/products/red-rain-coat"

}

Note

The JSON of the product can contain a maximum of 250 variants in the variants array.

**Note:**

The JSON of the product can contain a maximum of 250 variants in the variants array.

### [Anchor to Selling plan example](/docs/api/ajax/reference/product#selling-plan-example)Selling plan example

Products with selling plans will have the following additional properties available at `/{locale}/products/<handle>.js`.

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

{

"id":5290511958181,

// ...

"variants":[

{

"id":34620489400485,

// ...

"requires\_selling\_plan":false,

"selling\_plan\_allocations":[

{

"price":3120,

"compare\_at\_price":3900,

"per\_delivery\_price":3120,

"selling\_plan\_id":360613,

"selling\_plan\_group\_id":14699254537353206000

},

{

"price":3510,

"compare\_at\_price":3900,

"per\_delivery\_price":3510,

"selling\_plan\_id":393381,

"selling\_plan\_group\_id":14699254537353206000

}

]

}

],

"requires\_selling\_plan":false,

"selling\_plan\_groups":[

{

"id":14699254537353206000,

"name":"Subscribe and Save",

"options":[

{

"name":"Delivery Frequency",

"position":1,

"values":[

"Month",

"Week"

]

},

{

"name":"Billing Frequency",

"position":2,

"values":[

"Month",

"Week"

]

}

],

"selling\_plans":[

{

"id":360613,

"name":"Pay every month, delivery every month | save 20%",

"description":"No commitment · Auto-renews · Skip or cancel anytime",

"options":[

{

"name":"Delivery Frequency",

"position":1,

"value":"Month"

},

{

"name":"Billing Frequency",

"position":2,

"value":"Month"

}

],

"recurring\_deliveries":true

},

{

---

Was this page helpful?

YesNo