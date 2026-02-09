---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/refund
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# Refund

Ask assistant

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace\_orders`.:**

The Refund resource has two major components:

* Transaction records of money returned to the customer
* The line items included in the refund, along with restocking instructions

Before you create a refund, use the `calculate` endpoint to generate accurate refund transactions. Specify the line items that are being refunded, their quantity and restock instructions, and whether you're refunding shipping costs. You can then use the response of the `calculate` endpoint to create the actual refund.

When you create a refund using the response from the `calculate` endpoint, you can set additional options, such as whether to notify the customer of the refund. You can refund less than the calculated amount for either shipping or the line items by setting a custom value for the `amount` property.

If a refund includes shipping costs, or if you choose to refund line items for less than their calculated amount, then an order adjustment is created automatically to account for the discrepancy in the store's financial reports.

Was this section helpful?

YesNo

#

## Endpoints

* [post

  /admin/api/latest/orders/{order\_id}/refunds.json](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds)

  Creates a refund

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  refundCreate](/docs/api/admin-graphql/latest/mutations/refundCreate)
* [post

  /admin/api/latest/orders/{order\_id}/refunds/calculate.json](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-calculate)

  Calculates a refund

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  order](/docs/api/admin-graphql/latest/queries/order)
* [get

  /admin/api/latest/orders/{order\_id}/refunds.json](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds)

  Retrieves a list of refunds for an order

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  order](/docs/api/admin-graphql/latest/queries/order)
* [get

  /admin/api/latest/orders/{order\_id}/refunds/{refund\_id}.json](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-refund-id)

  Retrieves a specific refund

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  refund](/docs/api/admin-graphql/latest/queries/refund?example=retrieves-a-specific-refund)

---

[Anchor to](/docs/api/admin-rest/latest/resources/refund#resource-object) 

## The Refund resource

[Anchor to](/docs/api/admin-rest/latest/resources/refund#resource-object-properties) 

### Properties

---

created\_at

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

createdAt](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.createdAt)

The date and time (<a href='[https://en.wikipedia.org/wiki/ISO\_8601'target="\_blank">ISO](https://en.wikipedia.org/wiki/ISO_8601'target=%22_blank%22%3EISO) 8601 format) when the refund was created.

---

duties

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

duties](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.duties)

A list of duties that have been reimbursed as part of the refund.

---

id

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

id](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.id)

The unique identifier for the refund.

---

note

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

note](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.note)

An optional note attached to a refund.

---

order\_adjustments

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

orderAdjustments](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.orderAdjustments)

A list of order adjustments attached to the refund. Order adjustments are generated to account for refunded shipping costs and differences between calculated and actual refund amounts. As of the 2024-10 Admin API version, refunded shipping costs are no longer considered order adjustments and should be accessed through `refund_shipping_lines`. Each entry has the following properties:

Show order\_adjustments properties

* **id**: The unique identifier for the order adjustment.
* **order\_id**: The unique identifier for the order that the order adjustment is associated with.
* **refund\_id**: The unique identifier for the refund that the order adjustment is associated with.
* **amount**: This field is deprecated, please use `amount_set`. The value of the discrepancy between the calculated refund and the actual refund. If the `kind` property's value is `shipping_refund`, then `amount` returns the value of shipping charges refunded to the customer.
* **tax\_amount**: This field is deprecated, please use `tax_amount_set`. The taxes that are added to `amount`, such as applicable shipping taxes added to a shipping refund.
* **kind**: This field is deprecated as of the 2024-10 Admin API and will not be supported in the future. The order adjustment type. Valid values: `shipping_refund` and `refund_discrepancy`.
* **reason**: The reason for the order adjustment. To set this value, include `discrepancy_reason` when you create a refund.
* **amount\_set**: The amount of the order adjustment in shop and presentment currencies.
* **tax\_amount\_set**: The tax amount of the order adjustment in shop and presentment currencies.

---

processed\_at

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

processedAt](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.processedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the refund was imported. This value can be set to a date in the past when importing from other systems. If no value is provided, then it will be auto-generated as the current time in Shopify. Public apps need to be granted permission by Shopify to import orders with the `processed_at` timestamp set to a value earlier the `created_at` timestamp. Private apps can't be granted permission by Shopify.

---

refund\_duties

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

duties](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.duties)

A list of refunded duties. Each entry has the following properties:

Show refund\_duties properties

* **duty\_id**: The unique identifier of the duty.
* **refund\_type**: Specifies how you want the duty refunded. Valid values:

+ `FULL`: Refunds all the duties associated with a duty ID. You do not need to include refund line items if you are using the full refund type.
+ `PROPORTIONAL`: Refunds duties in proportion to the line item quantity that you want to refund. If you choose the proportional refund type, then you must also pass the refund line items to calculate the portion of duties to refund.

---

refund\_line\_items

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundLineItems](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.refundLineItems)

A list of refunded line items. Each entry has the following properties:

Show refund\_line\_items properties

* **id**: The unique identifier of the line item in the refund.
* **line\_item**: A line item being refunded.
* **line\_item\_id**: The ID of the related line item in the order.
* **quantity**: The refunded quantity of the associated line item.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:
  + **no\_restock**: Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example, a refund payment can be issued but no items will be refunded or made available for sale again.
  + **cancel**: The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered, and will be returned to the merchant. The refunded quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.
  + **legacy\_restock**: The deprecated `restock` property was used for this refund. These items were made available for sale again. This value is not accepted when creating new refunds.
* **location\_id**: The unique identifier of the [location](/api/admin-rest/current/resources/location) where the items will be restocked. Required when `restock_type` has the value `return` or `cancel`.
* **subtotal**: The subtotal of the refund line item.
* **total\_tax**: The total tax on the refund line item.
* **subtotal\_set**: The subtotal of the refund line item in shop and presentment currencies.
* **total\_tax\_set**: The total tax of the line item in shop and presentment currencies.

---

refund\_shipping\_lines

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundShippingLines](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.refundShippingLines)

A list of refunded shipping lines. Each entry has the following properties:

Show refund\_shipping\_lines properties

* **id**: The unique identifier of the shipping line in the refund.
* **shipping\_line**: The shipping line being refunded.
* **shipping\_line\_id**: The ID of the related shipping line in the order.
* **subtotal\_amount\_set**: The subtotal of the refund shipping line in shop and presentment currencies.

---

restock

deprecated**deprecated**

Whether to add any of the line items back to the store's inventory. Use `restock_type` for refund line items instead.

---

transactions

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

transactions](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.transactions)

A list of transactions involved in the refund. A single order can have multiple transactions associated with it. For more information, see the  [Transaction](/api/admin-rest/current/resources/transaction) resource.

---

user\_id

read-only**read-only**

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

staffMember](/docs/api/admin-graphql/latest/objects/Refund#field-Refund.fields.staffMember)

The unique identifier of the user who performed the refund.

---

Was this section helpful?

YesNo

{}

## The Refund resource

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

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

{

"created\_at": "2008-01-10T11:00:00-05:00",

"duties": {

"duties": [

{

"duty\_id": 1,

"amount\_set": {

"shop\_money": {

"amount": "9.83",

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": "9.83",

"currency\_code": "CAD"

}

}

}

]

},

"id": 92738740,

"note": "Item was damaged during shipping",

"order\_adjustments": [

{

"id": 4221763620,

"order\_id": 171016912932,

"refund\_id": 8244756516,

"amount": "10.00",

"tax\_amount": "0.00",

"kind": "refund\_discrepancy",

"reason": "Refund discrepancy",

"amount\_set": {

"shop\_money": {

"amount": 10,

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": 7.3,

"currency\_code": "USD"

}

},

"tax\_amount\_set": {

"shop\_money": {

"amount": 0,

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": 0,

"currency\_code": "USD"

}

}

}

],

"processed\_at": "2007-01-10T11:00:00-05:00",

"refund\_duties": [

{

"duty\_id": 1,

"refund\_type": "FULL"

}

],

"refund\_line\_items": [

{

"id": 209341123,

"line\_item": {},

"line\_item\_id": 128323456,

"quantity": 2,

"location\_id": 40642626,

"restock\_type": "return",

"subtotal": 10.99,

"total\_tax": 2.67,

"subtotal\_set": {

"shop\_money": {

"amount": 10.99,

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": 8.95,

"currency\_code": "USD"

}

},

"total\_tax\_set": {

"shop\_money": {

"amount": 1.67,

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": 1.32,

"currency\_code": "USD"

}

}

}

],

"refund\_shipping\_lines": [

{

"id": 712736824,

"shipping\_line": {},

"shipping\_line\_id": 8845532987448,

"subtotal\_amount\_set": {

"shop\_money": {

"amount": 5,

"currency\_code": "CAD"

},

"presentment\_money": {

"amount": 3.65,

"currency\_code": "USD"

}

}

}

],

"restock": true,

"transactions": [

{

"id": 179259969,

"order\_id": 450789469,

"amount": "209.00",

"kind": "refund",

"gateway": "shopify\_payments",

"status": "success",

"message": null,

"created\_at": "2005-08-05T12:59:12-04:00",

"test": false,

"authorization": "authorization-key",

"currency": "USD",

"location\_id": null,

"user\_id": null,

"parent\_id": 801038806,

"device\_id": null,

"receipt": {},

"error\_code": null,

"source\_name": "web"

}

],

"user\_id": 238478920

}

---

## [Anchor to POST request, Creates a refund](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds) post Creates a refund

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundCreate](/docs/api/admin-graphql/latest/mutations/refundCreate)

Caution

For multi-currency orders, the `currency` property is required whenever the `amount` property is provided.

**Caution:** 


For multi-currency orders, the `currency` property is required whenever the `amount` property is provided.

Creates a refund. Use the `calculate` endpoint to produce the transactions to submit.

  

Note

When you use this endpoint with a Partner development store or a trial store, you can create only five refunds per minute.

**Note:** 


When you use this endpoint with a Partner development store or a trial store, you can create only five refunds per minute.

### [Anchor to Parameters of Creates a refund](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-parameters)Parameters

---

api\_version

string**string**

required**required**

---

order\_id

string**string**

required**required**

---

currency

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the refund.

---

discrepancy\_reason

An optional comment that explains a discrepancy between calculated and actual refund amounts. Used to populate the `reason` property of the resulting `order_adjustment` object attached to the refund. Valid values: `restock`, `damage`, `customer`, and `other`.

---

note

An optional note attached to a refund.

---

notify

Whether to send a refund notification to the customer.

---

refund\_line\_items

A list of line item IDs, quantities to refund, and restock instructions. Each entry has the following properties:

Show refund\_line\_items properties

* **line\_item\_id**: The ID of a line item to refund.
* **quantity**: The quantity to refund.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:

  + **no\_restock**: Refunding these items won't affect inventory.
  + **cancel**: The items have not yet been fulfilled.
    The canceled quantity will be added back to the available count.
    The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered but will be returned to the merchant.
    The returned quantity will be added back to the available count. The number of fulfillable units for this
    line item will remain unchanged.
* **location\_id**: The ID of the [location](/api/admin-rest/current/resources/location) where the items should be
  restocked. This is required when the value of `restock_type` is `return` or `cancel`.
  If the item is not already stocked at the location, then
  the item is connected to the location. An error is returned when the item is connected to
  a [fulfillment service location](/api/admin-rest/current/resources/inventorylevel) and a different location is provided.

---

restock

deprecated**deprecated**

Whether to add the line items back to the store inventory. Use `restock_type` for refund line items instead.

---

shipping

Specify how much shipping to refund. It has the following properties:

Show shipping properties

* **full\_refund**: Whether to refund all remaining shipping.
* **amount**: Set a specific amount to refund for shipping. Takes precedence over `full_refund`.

---

transactions

A list of [transactions](/api/admin-rest/current/resources/transaction)
to process as refunds. Use the `calculate` endpoint to obtain these transactions.

---

Was this section helpful?

YesNo

### [Anchor to post-orders-order-id-refunds-examples](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-examples)Examples

Create a refund for an order

Path parameters

order\_id=450789469

string**string**

required**required**

Request body

refund

Refund resource**Refund resource**

Show refund properties

refund.note:"wrong size"

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

note](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-note)

An optional note attached to a refund.

refund.refund\_line\_items:[{"line\_item\_id":518995019,"quantity":1,"restock\_type":"return","location\_id":487838322}]

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundLineItems](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-refundLineItems)

A list of refunded line items. Each entry has the following properties:

Show refund\_line\_items properties

* **id**: The unique identifier of the line item in the refund.
* **line\_item**: A line item being refunded.
* **line\_item\_id**: The ID of the related line item in the order.
* **quantity**: The refunded quantity of the associated line item.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:
  + **no\_restock**: Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example, a refund payment can be issued but no items will be refunded or made available for sale again.
  + **cancel**: The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered, and will be returned to the merchant. The refunded quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.
  + **legacy\_restock**: The deprecated `restock` property was used for this refund. These items were made available for sale again. This value is not accepted when creating new refunds.
* **location\_id**: The unique identifier of the [location](/api/admin-rest/current/resources/location) where the items will be restocked. Required when `restock_type` has the value `return` or `cancel`.
* **subtotal**: The subtotal of the refund line item.
* **total\_tax**: The total tax on the refund line item.
* **subtotal\_set**: The subtotal of the refund line item in shop and presentment currencies.
* **total\_tax\_set**: The total tax of the line item in shop and presentment currencies.

refund.transactions:[{"parent\_id":801038806,"amount":41.94,"kind":"refund","gateway":"bogus"}]

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

transactions](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-transactions)

A list of transactions involved in the refund. A single order can have multiple transactions associated with it. For more information, see the  [Transaction](/api/admin-rest/current/resources/transaction) resource.

Refund a specific amount of shipping

Path parameters

order\_id=450789469

string**string**

required**required**

Request body

refund

Refund resource**Refund resource**

Show refund properties

refund.transactions:[{"parent\_id":801038806,"amount":5,"kind":"refund","gateway":"web"}]

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

transactions](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-transactions)

A list of transactions involved in the refund. A single order can have multiple transactions associated with it. For more information, see the  [Transaction](/api/admin-rest/current/resources/transaction) resource.

Was this section helpful?

YesNo

9

1

2

3

4

5

curl -d '{"refund":{"currency":"USD","notify":true,"note":"wrong size","shipping":{"full\_refund":true},"refund\_line\_items":[{"line\_item\_id":518995019,"quantity":1,"restock\_type":"return","location\_id":487838322}],"transactions":[{"parent\_id":801038806,"amount":41.94,"kind":"refund","gateway":"bogus"}]}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds.json" \

-H "X-Shopify-Access-Token: {access\_token}" \

-H "Content-Type: application/json"

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

HTTP/1.1 201 Created

{

"refund": {

"id": 929361483,

"order\_id": 450789469,

"created\_at": "2026-01-09T19:00:17-05:00",

"note": "wrong size",

"user\_id": null,

"processed\_at": "2026-01-09T19:00:17-05:00",

"duties": [],

"total\_duties\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"return": null,

"restock": false,

"additional\_fees": [],

"total\_additional\_fees\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"refund\_shipping\_lines": [],

"admin\_graphql\_api\_id": "gid://shopify/Refund/929361483",

"order\_adjustments": [],

### examples

* #### Create a refund for an order

  ##### 

  ```liquid
  curl -d '{"refund":{"currency":"USD","notify":true,"note":"wrong size","shipping":{"full_refund":true},"refund_line_items":[{"line_item_id":518995019,"quantity":1,"restock_type":"return","location_id":487838322}],"transactions":[{"parent_id":801038806,"amount":41.94,"kind":"refund","gateway":"bogus"}]}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const refund = new admin.rest.resources.Refund({session: session});

  refund.order_id = 450789469;
  refund.currency = "USD";
  refund.notify = true;
  refund.note = "wrong size";
  refund.shipping = {
    "full_refund": true
  };
  refund.refund_line_items = [
    {
      "line_item_id": 518995019,
      "quantity": 1,
      "restock_type": "return",
      "location_id": 487838322
    }
  ];
  refund.transactions = [
    {
      "parent_id": 801038806,
      "amount": 41.94,
      "kind": "refund",
      "gateway": "bogus"
    }
  ];
  await refund.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  refund = ShopifyAPI::Refund.new(session: test_session)
  refund.order_id = 450789469
  refund.currency = "USD"
  refund.notify = true
  refund.note = "wrong size"
  refund.shipping = {
    "full_refund" => true
  }
  refund.refund_line_items = [
    {
      "line_item_id" => 518995019,
      "quantity" => 1,
      "restock_type" => "return",
      "location_id" => 487838322
    }
  ]
  refund.transactions = [
    {
      "parent_id" => 801038806,
      "amount" => 41.94,
      "kind" => "refund",
      "gateway" => "bogus"
    }
  ]
  refund.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const refund = new shopify.rest.Refund({session: session});
  refund.order_id = 450789469;
  refund.currency = "USD";
  refund.notify = true;
  refund.note = "wrong size";
  refund.shipping = {
    "full_refund": true
  };
  refund.refund_line_items = [
    {
      "line_item_id": 518995019,
      "quantity": 1,
      "restock_type": "return",
      "location_id": 487838322
    }
  ];
  refund.transactions = [
    {
      "parent_id": 801038806,
      "amount": 41.94,
      "kind": "refund",
      "gateway": "bogus"
    }
  ];
  await refund.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"refund":{"id":929361483,"order_id":450789469,"created_at":"2026-01-09T19:00:17-05:00","note":"wrong size","user_id":null,"processed_at":"2026-01-09T19:00:17-05:00","duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"restock":false,"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[],"admin_graphql_api_id":"gid://shopify/Refund/929361483","order_adjustments":[],"refund_line_items":[{"location_id":null,"restock_type":"no_restock","quantity":1,"id":1058498334,"line_item_id":518995019,"subtotal":0.0,"total_tax":0.0,"subtotal_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"line_item":{"id":518995019,"variant_id":49148385,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008RED","variant_title":"red","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - red","variant_inventory_management":"shopify","properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.33","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/518995019","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}}],"transactions":[{"id":1068278588,"order_id":450789469,"kind":"refund","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T19:00:17-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":801038806,"processed_at":"2026-01-09T19:00:17-05:00","device_id":null,"error_code":null,"source_name":"755357713","receipt":{},"currency_exchange_adjustment":null,"amount":"41.94","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278588"}]}}
  ```
* #### Refund a specific amount of shipping

  ##### 

  ```liquid
  curl -d '{"refund":{"currency":"USD","shipping":{"amount":5.0},"transactions":[{"parent_id":801038806,"amount":5.0,"kind":"refund","gateway":"web"}]}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const refund = new admin.rest.resources.Refund({session: session});

  refund.order_id = 450789469;
  refund.currency = "USD";
  refund.shipping = {
    "amount": 5.0
  };
  refund.transactions = [
    {
      "parent_id": 801038806,
      "amount": 5.0,
      "kind": "refund",
      "gateway": "web"
    }
  ];
  await refund.save({
    update: true,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  refund = ShopifyAPI::Refund.new(session: test_session)
  refund.order_id = 450789469
  refund.currency = "USD"
  refund.shipping = {
    "amount" => 5.0
  }
  refund.transactions = [
    {
      "parent_id" => 801038806,
      "amount" => 5.0,
      "kind" => "refund",
      "gateway" => "web"
    }
  ]
  refund.save!
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const refund = new shopify.rest.Refund({session: session});
  refund.order_id = 450789469;
  refund.currency = "USD";
  refund.shipping = {
    "amount": 5.0
  };
  refund.transactions = [
    {
      "parent_id": 801038806,
      "amount": 5.0,
      "kind": "refund",
      "gateway": "web"
    }
  ];
  await refund.save({
    update: true,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 201 Created{"refund":{"id":929361482,"order_id":450789469,"created_at":"2026-01-09T19:00:14-05:00","note":null,"user_id":null,"processed_at":"2026-01-09T19:00:14-05:00","duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"restock":false,"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[{"id":623176827,"shipping_line_id":369256396,"subtotal_amount_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"shipping_line":{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"5.00","discounted_price_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"phone":null,"price":"5.00","price_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}}],"admin_graphql_api_id":"gid://shopify/Refund/929361482","order_adjustments":[{"id":1030976847,"order_id":450789469,"refund_id":929361482,"amount":"-5.00","tax_amount":"0.00","kind":"shipping_refund","reason":"Shipping refund","amount_set":{"shop_money":{"amount":"-5.00","currency_code":"USD"},"presentment_money":{"amount":"-5.00","currency_code":"USD"}},"tax_amount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}}}],"refund_line_items":[],"transactions":[{"id":1068278587,"order_id":450789469,"kind":"refund","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T19:00:14-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":801038806,"processed_at":"2026-01-09T19:00:14-05:00","device_id":null,"error_code":null,"source_name":"755357713","receipt":{},"currency_exchange_adjustment":null,"amount":"5.00","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278587"}]}}
  ```

---

## [Anchor to POST request, Calculates a refund](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-calculate) post Calculates a refund

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

order](/docs/api/admin-graphql/latest/queries/order)

Caution

For multi-currency orders, the `currency` property is required whenever the `amount` property is provided.

**Caution:** 


For multi-currency orders, the `currency` property is required whenever the `amount` property is provided.

Calculates refund transactions based on line items and shipping. When you want to create a refund,
you should first use the `calculate` endpoint to generate accurate refund transactions. Specify the line items
that are being refunded, their quantity and restock instructions, and whether you intend to refund
shipping costs. If the restock instructions can't be met—for example, because you try to return more items than have been
fulfilled—then the endpoint returns modified restock instructions. You can then use the response in the body of the request to create the actual refund.

The response includes a `transactions` object with `"kind": "suggested_refund"`,
which must to be changed to `"kind" : "refund"` for the refund to be accepted.

### [Anchor to Parameters of Calculates a refund](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-calculate-parameters)Parameters

---

api\_version

string**string**

required**required**

---

order\_id

string**string**

required**required**

---

currency

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the
currency used for the refund. **Note:** Required whenever the shipping `amount` property is provided.

---

refund\_line\_items

A list of line item IDs, quantities to refund, and restock instructions. Each entry has the following properties:

Show refund\_line\_items properties

* **line\_item\_id**: The ID of a line item to refund.
* **quantity**: The quantity to refund.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:

  + **no\_restock**: Refunding these items won't affect inventory.
  + **cancel**: The items have not yet been fulfilled. The canceled quantity will be added
    back to the available count. The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered but will be returned to the merchant.
    The returned quantity will be added back to the available count.
    The number of fulfillable units for this line item will remain unchanged.
* **location\_id**: The ID of the [location](https://shopify.dev/api/admin-rest/current/resources/location)
  where the items should be restocked. If `location_id` is not provided and the value of
  `restock_type` is `return` or `cancel`, then the endpoint returns a suitable
  location ID.
* **already\_stocked**: Whether the item is already stocked at
  the location. If this is `false`, then creating the refund will connect the item to the location and start
  stocking it there.

---

shipping

Specify how much shipping to refund. It has the following properties:

Show shipping properties

* **full\_refund**: Whether to refund all remaining shipping.
* **amount**: Set a specific amount to refund for shipping. Takes precedence over `full_refund`.

---

Was this section helpful?

YesNo

### [Anchor to post-orders-order-id-refunds-calculate-examples](/docs/api/admin-rest/latest/resources/refund#post-orders-order-id-refunds-calculate-examples)Examples

Calculate a refund for a partial amount of shipping

Path parameters

order\_id=450789469

string**string**

required**required**

Calculate the refund for a line item and shipping

Path parameters

order\_id=450789469

string**string**

required**required**

Request body

refund

Refund resource**Refund resource**

Show refund properties

refund.refund\_line\_items:[{"line\_item\_id":518995019,"quantity":1,"restock\_type":"no\_restock"}]

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundLineItems](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-refundLineItems)

A list of refunded line items. Each entry has the following properties:

Show refund\_line\_items properties

* **id**: The unique identifier of the line item in the refund.
* **line\_item**: A line item being refunded.
* **line\_item\_id**: The ID of the related line item in the order.
* **quantity**: The refunded quantity of the associated line item.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:
  + **no\_restock**: Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example, a refund payment can be issued but no items will be refunded or made available for sale again.
  + **cancel**: The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered, and will be returned to the merchant. The refunded quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.
  + **legacy\_restock**: The deprecated `restock` property was used for this refund. These items were made available for sale again. This value is not accepted when creating new refunds.
* **location\_id**: The unique identifier of the [location](/api/admin-rest/current/resources/location) where the items will be restocked. Required when `restock_type` has the value `return` or `cancel`.
* **subtotal**: The subtotal of the refund line item.
* **total\_tax**: The total tax on the refund line item.
* **subtotal\_set**: The subtotal of the refund line item in shop and presentment currencies.
* **total\_tax\_set**: The total tax of the line item in shop and presentment currencies.

Calculate the refund without specifying currency

Path parameters

order\_id=450789469

string**string**

required**required**

Request body

refund

Refund resource**Refund resource**

Show refund properties

refund.refund\_line\_items:[{"line\_item\_id":518995019,"quantity":1,"restock\_type":"no\_restock"}]

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refundLineItems](/docs/api/admin-graphql/latest/input-objects/RefundInput#fields-refundLineItems)

A list of refunded line items. Each entry has the following properties:

Show refund\_line\_items properties

* **id**: The unique identifier of the line item in the refund.
* **line\_item**: A line item being refunded.
* **line\_item\_id**: The ID of the related line item in the order.
* **quantity**: The refunded quantity of the associated line item.
* **restock\_type**: How this refund line item affects inventory levels. Valid values:
  + **no\_restock**: Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example, a refund payment can be issued but no items will be refunded or made available for sale again.
  + **cancel**: The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.
  + **return**: The items were already delivered, and will be returned to the merchant. The refunded quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.
  + **legacy\_restock**: The deprecated `restock` property was used for this refund. These items were made available for sale again. This value is not accepted when creating new refunds.
* **location\_id**: The unique identifier of the [location](/api/admin-rest/current/resources/location) where the items will be restocked. Required when `restock_type` has the value `return` or `cancel`.
* **subtotal**: The subtotal of the refund line item.
* **total\_tax**: The total tax on the refund line item.
* **subtotal\_set**: The subtotal of the refund line item in shop and presentment currencies.
* **total\_tax\_set**: The total tax of the line item in shop and presentment currencies.

Was this section helpful?

YesNo

9

1

2

3

4

5

curl -d '{"refund":{"currency":"USD","shipping":{"amount":2.0}}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/calculate.json" \

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

HTTP/1.1 200 OK

{

"refund": {

"duties": [],

"total\_duties\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"return": null,

"shipping": {

"amount": "2.00",

"tax": "0.00",

"maximum\_refundable": "5.00"

},

"additional\_fees": [],

"total\_additional\_fees\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"refund\_shipping\_lines": [

{

"id": null,

"shipping\_line\_id": 369256396,

"subtotal\_amount\_set": {

"shop\_money": {

"amount": "2.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "2.00",

"currency\_code": "USD"

}

},

"shipping\_line": {

"id": 369256396,

"carrier\_identifier": null,

"code": "Free Shipping",

"discounted\_price": "5.00",

"discounted\_price\_set": {

"shop\_money": {

"amount": "5.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "5.00",

"currency\_code": "USD"

}

},

"phone": null,

"price": "5.00",

"price\_set": {

"shop\_money": {

"amount": "5.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "5.00",

"currency\_code": "USD"

}

},

"requested\_fulfillment\_service\_id": null,

"source": "shopify",

"title": "Free Shipping",

"tax\_lines": [],

"discount\_allocations": []

}

}

],

"refund\_line\_items": [],

"transactions": [

{

"order\_id": 450789469,

"kind": "suggested\_refund",

"gateway": "bogus",

"parent\_id": 801038806,

"amount": "2.00",

"currency": "USD",

"maximum\_refundable": "41.94"

}

],

"currency": "USD"

}

}

### examples

* #### Calculate a refund for a partial amount of shipping

  ##### 

  ```liquid
  curl -d '{"refund":{"currency":"USD","shipping":{"amount":2.0}}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/calculate.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const refund = new admin.rest.resources.Refund({session: session});

  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"currency": "USD", "shipping": {"amount": 2.0}}},
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  refund = ShopifyAPI::Refund.new(session: test_session)
  refund.order_id = 450789469
  refund.calculate(
    session: test_session,
    body: {"refund" => {"currency" => "USD", "shipping" => {"amount" => 2.0}}},
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const refund = new shopify.rest.Refund({session: session});
  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"currency": "USD", "shipping": {"amount": 2.0}}},
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"refund":{"duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"shipping":{"amount":"2.00","tax":"0.00","maximum_refundable":"5.00"},"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[{"id":null,"shipping_line_id":369256396,"subtotal_amount_set":{"shop_money":{"amount":"2.00","currency_code":"USD"},"presentment_money":{"amount":"2.00","currency_code":"USD"}},"shipping_line":{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"5.00","discounted_price_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"phone":null,"price":"5.00","price_set":{"shop_money":{"amount":"5.00","currency_code":"USD"},"presentment_money":{"amount":"5.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}}],"refund_line_items":[],"transactions":[{"order_id":450789469,"kind":"suggested_refund","gateway":"bogus","parent_id":801038806,"amount":"2.00","currency":"USD","maximum_refundable":"41.94"}],"currency":"USD"}}
  ```
* #### Calculate the refund for a line item and shipping

  ##### 

  ```liquid
  curl -d '{"refund":{"currency":"USD","shipping":{"full_refund":true},"refund_line_items":[{"line_item_id":518995019,"quantity":1,"restock_type":"no_restock"}]}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/calculate.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const refund = new admin.rest.resources.Refund({session: session});

  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"currency": "USD", "shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 518995019, "quantity": 1, "restock_type": "no_restock"}]}},
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  refund = ShopifyAPI::Refund.new(session: test_session)
  refund.order_id = 450789469
  refund.calculate(
    session: test_session,
    body: {"refund" => {"currency" => "USD", "shipping" => {"full_refund" => true}, "refund_line_items" => [{"line_item_id" => 518995019, "quantity" => 1, "restock_type" => "no_restock"}]}},
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const refund = new shopify.rest.Refund({session: session});
  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"currency": "USD", "shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 518995019, "quantity": 1, "restock_type": "no_restock"}]}},
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"refund":{"duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"shipping":{"amount":"0.00","tax":"0.00","maximum_refundable":"0.00"},"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[],"refund_line_items":[{"quantity":1,"line_item_id":518995019,"location_id":null,"restock_type":"no_restock","price":"199.00","subtotal":"195.67","total_tax":"3.98","discounted_price":"199.00","discounted_total_price":"199.00","total_cart_discount_amount":"3.33"}],"transactions":[{"order_id":450789469,"kind":"suggested_refund","gateway":"bogus","parent_id":801038806,"amount":"41.94","currency":"USD","maximum_refundable":"41.94"}],"currency":"USD"}}
  ```
* #### Calculate the refund without specifying currency

  ##### 

  ```liquid
  curl -d '{"refund":{"shipping":{"full_refund":true},"refund_line_items":[{"line_item_id":518995019,"quantity":1,"restock_type":"no_restock"}]}}' \
  -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/calculate.json" \
  -H "X-Shopify-Access-Token: {access_token}" \
  -H "Content-Type: application/json"
  ```

  ##### 

  ```liquid
  const { admin, session } = await authenticate.admin(request);

  const refund = new admin.rest.resources.Refund({session: session});

  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 518995019, "quantity": 1, "restock_type": "no_restock"}]}},
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  refund = ShopifyAPI::Refund.new(session: test_session)
  refund.order_id = 450789469
  refund.calculate(
    session: test_session,
    body: {"refund" => {"shipping" => {"full_refund" => true}, "refund_line_items" => [{"line_item_id" => 518995019, "quantity" => 1, "restock_type" => "no_restock"}]}},
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  const refund = new shopify.rest.Refund({session: session});
  refund.order_id = 450789469;
  await refund.calculate({
    body: {"refund": {"shipping": {"full_refund": true}, "refund_line_items": [{"line_item_id": 518995019, "quantity": 1, "restock_type": "no_restock"}]}},
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"refund":{"duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"shipping":{"amount":"0.00","tax":"0.00","maximum_refundable":"0.00"},"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[],"refund_line_items":[{"quantity":1,"line_item_id":518995019,"location_id":null,"restock_type":"no_restock","price":"199.00","subtotal":"195.67","total_tax":"3.98","discounted_price":"199.00","discounted_total_price":"199.00","total_cart_discount_amount":"3.33"}],"transactions":[{"order_id":450789469,"kind":"suggested_refund","gateway":"bogus","parent_id":801038806,"amount":"41.94","currency":"USD","maximum_refundable":"41.94"}],"currency":"USD"}}
  ```

---

## [Anchor to GET request, Retrieves a list of refunds for an order](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds) get Retrieves a list of refunds for an order

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

order](/docs/api/admin-graphql/latest/queries/order)

Retrieves a list of refunds for an order. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieves a list of refunds for an order](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-parameters)Parameters

---

api\_version

string**string**

required**required**

---

order\_id

string**string**

required**required**

---

fields

Show only certain fields, specified by a comma-separated list of field names.

---

in\_shop\_currency

default false**default false**

Show amounts in the shop currency for the underlying transaction.

---

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to retrieve.

---

Was this section helpful?

YesNo

### [Anchor to get-orders-order-id-refunds-examples](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-examples)Examples

Retrieve all refunds from a specific order

Path parameters

order\_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds.json" \

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

"refunds": [

{

"id": 509562969,

"order\_id": 450789469,

"created\_at": "2026-01-09T17:04:11-05:00",

"note": "it broke during shipping",

"user\_id": 548380009,

"processed\_at": "2026-01-09T17:04:11-05:00",

"duties": [],

"total\_duties\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"return": null,

"restock": true,

"additional\_fees": [],

"total\_additional\_fees\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"refund\_shipping\_lines": [],

"admin\_graphql\_api\_id": "gid://shopify/Refund/509562969",

### examples

* #### Retrieve all refunds from a specific order

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Refund.all({
    session: session,
    order_id: 450789469,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Refund.all(
    session: test_session,
    order_id: 450789469,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Refund.all({
    session: session,
    order_id: 450789469,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"refunds":[{"id":509562969,"order_id":450789469,"created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","user_id":548380009,"processed_at":"2026-01-09T17:04:11-05:00","duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"restock":true,"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[],"admin_graphql_api_id":"gid://shopify/Refund/509562969","order_adjustments":[],"refund_line_items":[{"id":104689539,"quantity":1,"line_item_id":703073504,"location_id":487838322,"restock_type":"legacy_restock","subtotal":195.66,"total_tax":3.98,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"variant_id":457924702,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008BLACK","variant_title":"black","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - black","variant_inventory_management":"shopify","properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.33","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/703073504","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}},{"id":709875399,"quantity":1,"line_item_id":466157049,"location_id":487838322,"restock_type":"legacy_restock","subtotal":195.67,"total_tax":3.98,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"variant_id":39072856,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008GREEN","variant_title":"green","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - green","variant_inventory_management":"shopify","properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.34","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/466157049","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}}],"transactions":[{"id":179259969,"order_id":450789469,"kind":"refund","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-05T12:59:12-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":801038806,"processed_at":"2005-08-05T12:59:12-04:00","device_id":null,"error_code":null,"source_name":"web","receipt":{},"currency_exchange_adjustment":null,"amount":"209.00","currency":"USD","payment_id":"#1001.3","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969"}]}]}
  ```

---

## [Anchor to GET request, Retrieves a specific refund](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-refund-id) get Retrieves a specific refund

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

refund](/docs/api/admin-graphql/latest/queries/refund?example=retrieves-a-specific-refund)

Retrieves a specific refund.

### [Anchor to Parameters of Retrieves a specific refund](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-refund-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

order\_id

string**string**

required**required**

---

refund\_id

string**string**

required**required**

---

fields

Show only certain fields, specified by a comma-separated list of field names.

---

in\_shop\_currency

default false**default false**

Show amounts in the shop currency for the underlying transaction.

---

Was this section helpful?

YesNo

### [Anchor to get-orders-order-id-refunds-refund-id-examples](/docs/api/admin-rest/latest/resources/refund#get-orders-order-id-refunds-refund-id-examples)Examples

Retrieve a specific refund

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/509562969.json" \

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

"refund": {

"id": 509562969,

"order\_id": 450789469,

"created\_at": "2026-01-09T17:04:11-05:00",

"note": "it broke during shipping",

"user\_id": 548380009,

"processed\_at": "2026-01-09T17:04:11-05:00",

"duties": [],

"total\_duties\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"return": null,

"restock": true,

"additional\_fees": [],

"total\_additional\_fees\_set": {

"shop\_money": {

"amount": "0.00",

"currency\_code": "USD"

},

"presentment\_money": {

"amount": "0.00",

"currency\_code": "USD"

}

},

"refund\_shipping\_lines": [],

"admin\_graphql\_api\_id": "gid://shopify/Refund/509562969",

"order\_adjustments": [],

### examples

* #### Retrieve a specific refund

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/refunds/509562969.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.Refund.find({
    session: session,
    order_id: 450789469,
    id: 509562969,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::Refund.find(
    session: test_session,
    order_id: 450789469,
    id: 509562969,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.Refund.find({
    session: session,
    order_id: 450789469,
    id: 509562969,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"refund":{"id":509562969,"order_id":450789469,"created_at":"2026-01-09T17:04:11-05:00","note":"it broke during shipping","user_id":548380009,"processed_at":"2026-01-09T17:04:11-05:00","duties":[],"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"return":null,"restock":true,"additional_fees":[],"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"refund_shipping_lines":[],"admin_graphql_api_id":"gid://shopify/Refund/509562969","order_adjustments":[],"refund_line_items":[{"id":104689539,"quantity":1,"line_item_id":703073504,"location_id":487838322,"restock_type":"legacy_restock","subtotal":195.66,"total_tax":3.98,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"variant_id":457924702,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008BLACK","variant_title":"black","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - black","variant_inventory_management":"shopify","properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.33","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/703073504","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}},{"id":709875399,"quantity":1,"line_item_id":466157049,"location_id":487838322,"restock_type":"legacy_restock","subtotal":195.67,"total_tax":3.98,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"variant_id":39072856,"title":"IPod Nano - 8gb","quantity":1,"sku":"IPOD2008GREEN","variant_title":"green","vendor":null,"fulfillment_service":"manual","product_id":632910392,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"IPod Nano - 8gb - green","variant_inventory_management":"shopify","properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"product_exists":true,"fulfillable_quantity":1,"grams":200,"price":"199.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[{"amount":"3.34","discount_application_index":0,"amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}}}],"duties":[],"admin_graphql_api_id":"gid://shopify/LineItem/466157049","tax_lines":[{"title":"State Tax","price":"3.98","rate":0.06,"channel_liable":null,"price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}}}]}}],"transactions":[{"id":179259969,"order_id":450789469,"kind":"refund","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-05T12:59:12-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":801038806,"processed_at":"2005-08-05T12:59:12-04:00","device_id":null,"error_code":null,"source_name":"web","receipt":{},"currency_exchange_adjustment":null,"amount":"209.00","currency":"USD","payment_id":"#1001.3","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969"}]}}
  ```