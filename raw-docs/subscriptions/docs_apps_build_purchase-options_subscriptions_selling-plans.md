---
source: https://shopify.dev/docs/apps/build/purchase-options/subscriptions/selling-plans
---

Selling plans represent how products can be sold and purchased. For example, a product can be configured to enable it to be billed and delivered on a monthly basis at a 15% discount.

Two common selling plan types include the "Subscribe and save" and "Prepaid" options. "Subscribe and save", also known as "pay per delivery", is a selling method where a customer pays for goods or services per delivery. "Prepaid" is a selling method where a customer makes a single payment upfront.

Learn more about [purchase option types](/docs/apps/build/purchase-options) and [associated policies](/docs/apps/build/purchase-options/subscriptions).

---

## [Anchor to Requirements](/docs/apps/build/purchase-options/subscriptions/selling-plans#requirements)Requirements

Note

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

**Note:**

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

* Your app can make [authenticated requests](/docs/api/admin-graphql#authentication) to the GraphQL Admin API.
* Your app has the `write_products`, `read_customer_payment_methods`, `read_own_subscription_contracts`, and `write_own_subscription_contracts` [access scopes](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).
* You've created [products](/docs/api/admin-graphql/latest/mutations/productcreate) and [product variants](/docs/api/admin-graphql/latest/mutations/productvariantcreate) in your development store.
* To be eligible to use Shopify subscriptions, users need to meet the [qualifying criteria](https://help.shopify.com/en/manual/products/subscriptions/setup#eligibility-requirements).

---

## [Anchor to Selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans#selling-plans)Selling plans

Selling plans are organized into selling plan groups, which represent a selling method or purchase option. The following diagram shows the object relationships between selling plan groups, products, variants, selling plans, and policies.

![GraphQL Admin API objects for selling plan groups.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/purchase-options/purchase-options-selling-plan-Dnbic69z.png)

| API object | Description |
| --- | --- |
| Selling plan group | Represents a selling method. For example, "Subscribe and save" or "Prepaid" subscriptions. |
| Products | Represents the products that are associated to the selling plan group. |
| Variants | Represents the product variants that are associated to the selling plan group. |
| Selling plans | Represents an alternative way to buy a product or variant. Selling plans are organized into a selling plan group. For example, individual selling plans might be named "Deliver weekly" or "Deliver monthly". |
| Policies | Each selling plan is associated with the following policies:  * **Billing policy**: The billing frequency associated with the subscription. For example, bill every week, or bill every three months. * **Delivery policy**: The delivery frequency associated with the subscription. For example, deliver every month, or deliver every other week. * **Inventory policy**: The inventory behavior associated with the subscription. Inventory can be committed when the order is created, or when the order is fulfilled. * **Pricing policy**: The type of pricing associated with the subscription. For example, a $10 or 20% discount that recurs for a limited period or that is fixed for the duration of the subscription. The two types of pricing policies are:    + **Fixed pricing policy**: A single pricing policy. For example, all billing cycles might have a flat 15% discount. An initial pricing policy is applied until a defined recurring policy kicks in.   + **Recurring pricing policy**: A follow up pricing policy that applies if the initial pricing policy expires. For example, the first billing cycle might have a 20% discount and the recurring cycles after might be discounted by 15%. |

---

## [Anchor to Selling plans-related webhooks](/docs/apps/build/purchase-options/subscriptions/selling-plans#selling-plans-related-webhooks)Selling plans-related webhooks

Your app can subscribe to webhooks that are related to selling plans. The following examples show the JSON responses from each of the available webhooks.

To learn how to set up and consume webhooks, refer to the [Webhook configuration overview](/docs/apps/build/webhooks/subscribe).

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

// Occurs when a selling plan group is created. Requires the read\_own\_subscription\_contracts scope.

{

"admin\_graphql\_api\_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",

"id": 1039518903,

"name": "Subscribe & Save",

"merchant\_code": "sub-n-save",

"admin\_graphql\_api\_app": "gid:\/\/shopify\/App\/2525000003",

"app\_id": null,

"description": null,

"options": [

"Delivery every"

],

"position": null,

"summary": "1 delivery frequency, discount",

"selling\_plans": [

{

"name": "Pay every month deliver every month",

"options": [

"month"

],

"position": null,

"description": null,

"billing\_policy": {

"interval": "month",

"interval\_count": 1,

"min\_cycles": null,

"max\_cycles": null

},

"delivery\_policy": {

"interval": "month",

"interval\_count": 1,

"anchors": [

],

"cutoff": null,

"pre\_anchor\_behavior": "asap"

},

"pricing\_policies": [

]

}

],

"product\_variants": [

],

"products": [

]

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

// Occurs when a selling plan group is updated. Requires the read\_own\_subscription\_contracts scope.

{

"admin\_graphql\_api\_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",

"id": 1039518903,

"name": "Subscribe & Save",

"merchant\_code": "sub-n-save",

"admin\_graphql\_api\_app": "gid:\/\/shopify\/App\/2525000003",

"app\_id": null,

"description": null,

"options": [

"Delivery every"

],

"position": null,

"summary": "1 delivery frequency, discount",

"selling\_plans": [

{

"name": "Pay every month deliver every month",

"options": [

"month"

],

"position": null,

"description": null,

"billing\_policy": {

"interval": "month",

"interval\_count": 1,

"min\_cycles": null,

"max\_cycles": null

},

"delivery\_policy": {

"interval": "month",

"interval\_count": 1,

"anchors": [

],

"cutoff": null,

"pre\_anchor\_behavior": "asap"

},

"pricing\_policies": [

]

}

],

"product\_variants": [

],

"products": [

]

}

9

1

2

3

4

5

// Occurs when a selling plan group is deleted. Requires the read\_own\_subscription\_contracts scope.

{

"admin\_graphql\_api\_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",

"id": 1039518903,

}

##### selling\_plan\_groups/create

```liquid
// Occurs when a selling plan group is created.	Requires the read_own_subscription_contracts scope.
{
  "admin_graphql_api_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",
  "id": 1039518903,
  "name": "Subscribe & Save",
  "merchant_code": "sub-n-save",
  "admin_graphql_api_app": "gid:\/\/shopify\/App\/2525000003",
  "app_id": null,
  "description": null,
  "options": [
    "Delivery every"
  ],
  "position": null,
  "summary": "1 delivery frequency,  discount",
  "selling_plans": [
    {
      "name": "Pay every month deliver every month",
      "options": [
        "month"
      ],
      "position": null,
      "description": null,
      "billing_policy": {
        "interval": "month",
        "interval_count": 1,
        "min_cycles": null,
        "max_cycles": null
      },
      "delivery_policy": {
        "interval": "month",
        "interval_count": 1,
        "anchors": [

        ],
        "cutoff": null,
        "pre_anchor_behavior": "asap"
      },
      "pricing_policies": [

      ]
    }
  ],
  "product_variants": [

  ],
  "products": [

  ]
}
```

##### selling\_plan\_groups/update

```liquid
// Occurs when a selling plan group is updated.	Requires the read_own_subscription_contracts scope.
{
  "admin_graphql_api_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",
  "id": 1039518903,
  "name": "Subscribe & Save",
  "merchant_code": "sub-n-save",
  "admin_graphql_api_app": "gid:\/\/shopify\/App\/2525000003",
  "app_id": null,
  "description": null,
  "options": [
    "Delivery every"
  ],
  "position": null,
  "summary": "1 delivery frequency,  discount",
  "selling_plans": [
    {
      "name": "Pay every month deliver every month",
      "options": [
        "month"
      ],
      "position": null,
      "description": null,
      "billing_policy": {
        "interval": "month",
        "interval_count": 1,
        "min_cycles": null,
        "max_cycles": null
      },
      "delivery_policy": {
        "interval": "month",
        "interval_count": 1,
        "anchors": [

        ],
        "cutoff": null,
        "pre_anchor_behavior": "asap"
      },
      "pricing_policies": [

      ]
    }
  ],
  "product_variants": [

  ],
  "products": [

  ]
}
```

##### selling\_plan\_groups/delete

```liquid
// Occurs when a selling plan group is deleted.	Requires the read_own_subscription_contracts scope.
{
  "admin_graphql_api_id": "gid:\/\/shopify\/SellingPlanGroup\/1039518903",
  "id": 1039518903,
}
```

---

## [Anchor to Subscription shipping and delivery](/docs/apps/build/purchase-options/subscriptions/selling-plans#subscription-shipping-and-delivery)Subscription shipping and delivery

Note

To manage delivery profiles on your selling plans, your app needs the `read_shipping` and `write_shipping` [access scopes](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).

**Note:**

To manage delivery profiles on your selling plans, your app needs the `read_shipping` and `write_shipping` [access scopes](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).

Customers can buy one-time purchases and subscriptions when both are offered by a merchant. Some merchants might want to offer custom shipping rules for subscription purchases. You can use the [`DeliveryProfile`](/docs/api/admin-graphql/latest/objects/deliveryprofile) object to create shipping profiles and associate them with selling plan groups. Here are some example scenarios where delivery profiles can be useful to implement custom shipping rules for subscription purchases:

* A merchant wants to offer free or discounted shipping on subscriptions.
* A merchant wants to limit subscription purchases to certain shipping destinations.
* A merchant wants to offer local pickup for one-time purchases of a product, but requires shipping for subscription purchases.

### [Anchor to Delivery profiles](/docs/apps/build/purchase-options/subscriptions/selling-plans#delivery-profiles)Delivery profiles

By default, a product has the same shipping rate whether it's bought as a one-time purchase or as part of a subscription. To calculate subscription shipping separately from one-time purchases, you can associate a [`DeliveryProfile`](/docs/api/admin-graphql/latest/objects/deliveryprofile) object with the selling plan group using the [`deliveryProfileCreate`](/docs/api/admin-graphql/latest/mutations/deliveryprofilecreate) or [`deliveryProfileUpdate`](/docs/api/admin-graphql/latest/mutations/deliveryprofileupdate) mutation.

When one-time purchases and subscriptions are in the same delivery profile, coming from the same location, shipping for one-time purchases is calculated and combined with the subscription purchases. Subsequent subscription shipping rates are calculated separately.

Shipping rates that are specific to a selling plan group don't display in the **Shipping and delivery** settings in the Shopify admin. You need to configure shipping rates for selling plan groups in your app.

### [Anchor to Delivery method display at checkout](/docs/apps/build/purchase-options/subscriptions/selling-plans#delivery-method-display-at-checkout)Delivery method display at checkout

When multiple subscriptions are in the cart, shipping rates are consolidated if they share the same [selling plan billing and delivery policies](/docs/api/admin-graphql/latest/input-objects/sellingplaninput).

Customers can select a shipping rate for one-time purchase products in the cart if more than one rate is available. They can also view the total cost of shipping for their subscriptions and the total cost of shipping for one-time purchases:

![One-time and subscriptions shipping screenshot](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/shipping-on-subscriptions-LSS_8rzn.png)

### [Anchor to Local delivery and local pickup](/docs/apps/build/purchase-options/subscriptions/selling-plans#local-delivery-and-local-pickup)Local delivery and local pickup

Note

[Local delivery](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-delivery) and [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup) options might not be supported on subscriptions for some merchants on the [Shopify Plus](https://www.shopify.com/plus) plan with custom checkouts.

**Note:**

[Local delivery](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-delivery) and [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup) options might not be supported on subscriptions for some merchants on the [Shopify Plus](https://www.shopify.com/plus) plan with custom checkouts.

When choosing [local delivery or pickup methods](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/local-methods), the chosen method applies to the entire order. Mixed delivery methods aren't supported.

For example, if the customer has a one-time purchase and subscription on the same cart, and they select local pickup at checkout, then they can't choose shipping or local delivery for the subscription. All items would be fulfilled as local pickup.

### [Anchor to Updating shipping and delivery for contracts](/docs/apps/build/purchase-options/subscriptions/selling-plans#updating-shipping-and-delivery-for-contracts)Updating shipping and delivery for contracts

Shopify automatically creates [subscription contracts](/docs/apps/build/purchase-options/subscriptions/contracts) when products with selling plans are purchased through checkout. Subscription contracts are detached from the original selling plan. Updates to the original selling plan don't modify pre-existing subscription contracts.

To make changes to those contracts, you can [update their delivery prices and delivery methods](/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract#step-3-update-the-subscription-draft) with the [`subscriptionDraftUpdate`](/docs/api/admin-graphql/latest/mutations/subscriptiondraftupdate) mutation.

When [querying a shipping rate for a subscription draft](/docs/api/admin-graphql/latest/queries/subscriptiondraft), the returned shipping rate depends on whether the subscription contract has a selling plan ID and variant ID:

* If the subscription contract doesn't have a selling plan ID, then the shipping rates from the delivery profile associated with the variant ID are displayed.
* If the subscription contract doesn't have a selling plan or variant ID, then the shipping rates from the shop's general delivery profile are displayed.

  For more information on contracts, refer to [Subscription contracts](/docs/apps/build/purchase-options/subscriptions/contracts).

---

## [Anchor to Anchors](/docs/apps/build/purchase-options/subscriptions/selling-plans#anchors)Anchors

Anchors define the date when fulfillment is completed by a merchant or when delivery occurs for the customer for a given time cycle. You can also define a cutoff for which customers are eligible to enter this cycle and the desired behavior for customers who start their subscription inside the cutoff period.

If you need to define more advanced delivery behaviors for subscriptions, then you should use anchors. Here are some example scenarios where anchors can be useful to implement advanced delivery behavior:

* A merchant starts fulfillment on a specific date every month.
* A merchant wants to bill the 1st of every quarter.
* A customer expects their delivery every Tuesday.

### [Anchor to Billing anchor behaviors](/docs/apps/build/purchase-options/subscriptions/selling-plans#billing-anchor-behaviors)Billing anchor behaviors

If something occurs that delays a [billing attempt](/docs/api/admin-graphql/latest/objects/SubscriptionBillingAttempt) past an anchor date, then fulfillment is also delayed to the next anchor date. You can prevent this by providing an appropriate `originTime` value when you [create a new billing attempt](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

An example is a subscription with anchor billing and fulfillment dates for the 15th of every month. If a customer's payment fails and doesn't go through until the 16th, then their order won't be fulfilled until the 15th of the next month. Providing an `originTime` value on or before the 15th allows the fulfillment to take place on schedule, regardless of whether the billing attempt was successful past the anchor date.

### [Anchor to Delivery cutoff behaviors](/docs/apps/build/purchase-options/subscriptions/selling-plans#delivery-cutoff-behaviors)Delivery cutoff behaviors

You can use the `anchors`, `cutoff`, and `preAnchorBehavior` properties of the [recurring delivery policy](/docs/api/admin-graphql/latest/objects/sellingplanrecurringdeliverypolicy) on a selling plan to define the behavior for when customers are eligible to enter a delivery or fulfillment cycle:

| Property | Description |
| --- | --- |
| `anchors` | Specifies the date when delivery or fulfillment is completed by a merchant. |
| `cutoff` | Specifies a buffer period before the anchor date for orders to be included in a delivery or fulfillment cycle. |
| `preAnchorBehavior` | Defines whether an order that is placed can be delivered or fulfilled immediately, or at the next anchor date. Valid values are `ASAP` or `NEXT`. When the `preAnchorBehavior` is `ASAP`, an order that is placed can be delivered or fulfilled immediately. Orders that are placed within a cutoff period can be delivered or fulfilled at the next anchor date. When the `preAnchorBehavior` is `NEXT`, an order that is placed can be delivered or fulfilled at the next anchor date. Orders that are placed within a cutoff period skip the next anchor date and can be delivered or fulfilled at the following anchor date. |

The following table shows some example scenarios of what the expected next billing and delivery dates are for a subscription with billing and delivery anchor dates at the 15th of each month, given different first billing dates (when a subscription starts), `cutoff`, and `preAnchorBehavior` values:

| First billing date | `cutoff` | `preAnchorBehavior` | First delivery date | Next billing and delivery date |
| --- | --- | --- | --- | --- |
| On the anchor date: `2023-01-15` | `0` | `ASAP` | `2023-01-15` | `2023-02-15` |
| `NEXT` | `2023-01-15` | `2023-02-15` |
| Before the anchor date, and before the cutoff period: `2023-01-12` | `0` | `ASAP` | `2023-01-12` | `2023-01-15` |
| `NEXT` | `2023-01-15` | `2023-02-15` |
| Before the anchor date, and within the cutoff period: `2023-01-12` | `5` | `ASAP` | `2023-01-15` | `2023-02-15` |
| `NEXT` | `2023-02-15` | `2023-03-15` |

For an example implementation of anchors, refer to the "Subscribe and save" example in the [Create and manage selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan#step-1-create-a-selling-plan-group) guide.

---

## [Anchor to Selling plans on Shopify POS](/docs/apps/build/purchase-options/subscriptions/selling-plans#selling-plans-on-shopify-pos)Selling plans on Shopify POS

Selling plans can be sold through Shopify Point of Sale (POS). When a merchant creates selling plans using the Admin API, those plans become available for sale on both online channels and POS.

### [Anchor to Requirements for POS](/docs/apps/build/purchase-options/subscriptions/selling-plans#requirements-for-pos)Requirements for POS

To sell products with selling plans on POS, merchants need:

* To publish the product so it is available on the POS channel.
* Shopify POS app version 10.13 or later.
* Shopify Payments enabled.
* A subscription app that supports POS through a POS UI extension.

### [Anchor to Implementation for app developers](/docs/apps/build/purchase-options/subscriptions/selling-plans#implementation-for-app-developers)Implementation for app developers

Subscription apps need to build a [POS UI extension](/docs/api/pos-ui-extensions) to enable merchants to sell selling plans on POS. The extension uses the Cart API to add and remove selling plans from line items.

For detailed information about implementing POS support, refer to [Subscriptions on Shopify POS](/docs/apps/build/purchase-options/subscriptions#pos-support).

### [Anchor to Limitations](/docs/apps/build/purchase-options/subscriptions/selling-plans#limitations)Limitations

For a complete list of POS-specific limitations, refer to [POS limitations for subscriptions](/docs/apps/build/purchase-options/subscriptions#pos-limitations).

---

## [Anchor to Next steps](/docs/apps/build/purchase-options/subscriptions/selling-plans#next-steps)Next steps

* Learn how to [create and manage selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan) to determine the policies under which products can be sold.

---

Was this page helpful?

YesNo