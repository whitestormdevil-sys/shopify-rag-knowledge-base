---
source: https://shopify.dev/docs/api/liquid/objects/fulfillment
---

An order [fulfillment](https://help.shopify.com/manual/orders/fulfillment), which includes information like the line items
being fulfilled and shipment tracking.

## Properties

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-created_at) 

created\_at**created\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the fulfillment was created.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-fulfillment_line_items) 

fulfillment\_line\_items**fulfillment\_line\_items** array of [line\_item](/docs/api/liquid/objects/line_item)

:   The line items in the fulfillment.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-item_count) 

item\_count**item\_count** [number](/docs/api/liquid/basics#number)

:   The number of items in the fulfillment.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-tracking_company) 

tracking\_company**tracking\_company** [string](/docs/api/liquid/basics#string)

:   The name of the fulfillment service.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-tracking_number) 

tracking\_number**tracking\_number** [string](/docs/api/liquid/basics#string)

:   The fulfillment's tracking number.

    If there's no tracking number, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-tracking_numbers) 

tracking\_numbers**tracking\_numbers** array of [string](/docs/api/liquid/basics#string)

:   An array of the fulfillment's tracking numbers.

[Anchor to](/docs/api/liquid/objects/fulfillment#fulfillment-tracking_url) 

tracking\_url**tracking\_url** [string](/docs/api/liquid/basics#string)

:   The URL for the fulfillment's tracking number.

    If there's no tracking number, then `nil` is returned.

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

"created\_at": "2022-06-15 17:08:30 -0400",

"fulfillment\_line\_items": [

{

"quantity": 2,

"line\_item": "LineItemDrop"

},

{

"quantity": 1,

"line\_item": "LineItemDrop"

}

],

"item\_count": 3,

"tracking\_company": "Canada Post",

"tracking\_number": "01189998819991197253",

"tracking\_numbers": [

"01189998819991197253"

],

"tracking\_url": "https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=01189998819991197253"

}

##### Example

```liquid
{
  "created_at": "2022-06-15 17:08:30 -0400",
  "fulfillment_line_items": [
    {
      "quantity": 2,
      "line_item": "LineItemDrop"
    },
    {
      "quantity": 1,
      "line_item": "LineItemDrop"
    }
  ],
  "item_count": 3,
  "tracking_company": "Canada Post",
  "tracking_number": "01189998819991197253",
  "tracking_numbers": [
    "01189998819991197253"
  ],
  "tracking_url": "https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=01189998819991197253"
}
```

Was this section helpful?

YesNo