---
source: https://shopify.dev/docs/apps/selling-strategies/subscriptions/contracts
---

A [subscription contract](/docs/api/admin-graphql/latest/queries/subscriptioncontract) is the agreement between a customer and a merchant over a specific term for recurring purchases over a set or undefined period of time.

A subscription contract is the result of purchasing a [selling plan](/docs/api/admin-graphql/latest/objects/SellingPlan) that has recurring policies. After a customer purchases a subscription [product](/docs/api/admin-graphql/latest/objects/Product) or [variant](/docs/api/admin-graphql/latest/objects/ProductVariant) at checkout, Shopify generates a [subscription contract](/docs/api/admin-graphql/latest/queries/subscriptionContract) and shares the subscription contract with your app using a webhook.

At the time of subscription renewal, apps charge customers for their subscriptions by initiating a [billing attempt](/docs/api/admin-graphql/latest/queries/subscriptionBillingAttempt) on the subscription contract. And a new order will be created.

Caution

48 hours after a user uninstalls a subscription app, any subscription contracts that are owned by that app and that haven't been terminated are cancelled. These subscriptions contracts might have a status of [active](/docs/api/admin-graphql/latest/mutations/subscriptionContractActivate), [paused](/docs/api/customer/latest/mutations/subscriptionContractPause), or [failed](/docs/api/admin-graphql/latest/mutations/subscriptionContractFail).

**Caution:**

48 hours after a user uninstalls a subscription app, any subscription contracts that are owned by that app and that haven't been terminated are cancelled. These subscriptions contracts might have a status of [active](/docs/api/admin-graphql/latest/mutations/subscriptionContractActivate), [paused](/docs/api/customer/latest/mutations/subscriptionContractPause), or [failed](/docs/api/admin-graphql/latest/mutations/subscriptionContractFail).

---

## [Anchor to Requirements](/docs/apps/build/purchase-options/subscriptions/contracts#requirements)Requirements

Note

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

**Note:**

* Most subscriptions, pre-order and try before you buy apps need to request API access through the [Partner Dashboard](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant#ask-for-permission). We give API access to apps that are designed according to our [principles for subscriptions, pre-order and TBYB apps] (/docs/apps/selling-strategies/purchase-options#shopifys-principles).
* Public apps that use subscriptions, pre-order or TBYB need to meet [specific requirements](/docs/apps/launch/app-requirements-checklist#purchase-option-apps) to be published on the Shopify App Store.
* Custom apps [created in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) can't use subscriptions, pre-order or TBYB because these apps can't use extensions or request access to protected scopes. If you're building a solution for a single store, then build your custom app in the Partner Dashboard.

* Your app can make [authenticated requests](/docs/api/admin-graphql#authentication) to the GraphQL Admin API.
* Your app has the `read_own_subscription_contracts` and `write_own_subscription_contracts` [access scopes](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).
* You've created [products](/docs/api/admin-graphql/latest/mutations/productcreate) and [product variants](/docs/api/admin-graphql/latest/mutations/productvariantcreate) in your development store.

* You've completed the [Create and manage selling plans](/docs/apps/build/purchase-options/subscriptions/selling-plans/build-a-selling-plan) guide.

---

## [Anchor to Subscription contract object relationships](/docs/apps/build/purchase-options/subscriptions/contracts#subscription-contract-object-relationships)Subscription contract object relationships

The following diagram shows the relationship between subscription contracts, orders, subscription contract drafts, and billing attempts:

![Subscription contract objects diagram](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/subscription-contracts-CcZohSI0.png)

| API object | Description |
| --- | --- |
| Subscription contract | Represents the agreement for a set of items delivered to a customer, on a specific billing and delivery schedule and at a specific price. A subscription contract is different from an order. An order is a customer's completed request to purchase one or more products from a shop. An order is created when a customer completes the checkout process, during which time they provide an email address or phone number, billing address, and payment information. Subscription contracts might not be immediately available when an order is created. It's best to rely on subscription contract webhooks to be notified when subscription contracts are created. |
| Subscription contract lines | Represents the price and quantity of items in a subscription contract. |
| Pricing policy | Represents the future intent to change the price after a given number of billing cycles. When the customer completes a checkout, Shopify creates a subscription contract, and the app developer is notified the policies that the customer chose. The pricing policy serves as a guide for apps to modify the contract's price in accordance with the billing cycle. It's important to understand that the price of the line item does not update automatically. |
| Subscription order line | Links a subscription contract to its related order line items, and optionally, to the billing attempt that created this order line.  A subscription order line is created when one of the following events occurs:   * A billing attempt creates an order. * A subscription is created from a selling plan purchase. |
| Subscription draft | Represents the intent to change a subscription. If a customer wants to change their subscription, then the app needs to create a subscription draft and commit the change to make the changes active. |
| Draft change | Represents a change made to a subscription draft, such as changing a subscription contract line. |
| Billing attempt | Represents an attempt at executing a billing cycle and charging the customer payment method for a subscription contract. |

---

## [Anchor to Subscription discounts](/docs/apps/build/purchase-options/subscriptions/contracts#subscription-discounts)Subscription discounts

Note

To manage discounts on your subscription contracts, your app needs the `write_discounts` [access scope](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).

**Note:**

To manage discounts on your subscription contracts, your app needs the `write_discounts` [access scope](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).

You can apply different discount types on subscriptions, including percentage, fixed amount, and free shipping discounts.

### [Anchor to Discount types](/docs/apps/build/purchase-options/subscriptions/contracts#discount-types)Discount types

Note

As of Admin API version 2023-10, you can create automatic discounts that apply to subscriptions. For more information on automatic discounts, refer to [discount types](/docs/apps/build/discounts#discount-methods).

**Note:**

As of Admin API version 2023-10, you can create automatic discounts that apply to subscriptions. For more information on automatic discounts, refer to [discount types](/docs/apps/build/discounts#discount-methods).

You can apply discounts on subscriptions in the following ways:

* **Manual custom discounts**: Defined on the subscription.
* **Shopify code discounts**: Defined on a shop and applied to a subscription.
* **Shopify automatic discounts**: Defined on a shop and applied to a subscription.

Using any of these methods, you can apply the following discount types:

* **Percentage discount**: A percentage amount deducted from the original product price. For example, 10% off.
* **Fixed amount discount**: A specific amount deducted from the original product price. For example, 10 CAD off.
* **Free shipping discount**: An offer that deducts shipping costs from the original product price. For example, free shipping on a subscription purchase.

You can define whether the discount applies to only one-time purchases, subscriptions, or both:

![Purchase type options screenshot](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/discount-purchase-type-DU1dxpYb.png)

You can also limit the number of times a discount can be used on recurring payments for subscriptions:

![Recurring payments for subscriptions screenshot](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/subscriptions/discount-usage-limit-C9X4zg8u.png)

Tip

Refer to the [Update a subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract) tutorial for an example of how to create and apply a discount code to a subscription contract.

**Tip:**

Refer to the [Update a subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract) tutorial for an example of how to create and apply a discount code to a subscription contract.

### [Anchor to Conditions for code discounts](/docs/apps/build/purchase-options/subscriptions/contracts#conditions-for-code-discounts)Conditions for code discounts

This section describes the conditions that Shopify provides for code discounts that apply to subscriptions.

#### [Anchor to Customer eligibility for discounts](/docs/apps/build/purchase-options/subscriptions/contracts#customer-eligibility-for-discounts)Customer eligibility for discounts

You can limit customer eligibility for discounts to certain groups of customers and use the subscription-aware customer filters. The filters are available on the **Customers** page in the Shopify admin.

#### [Anchor to How are code discounts verified](/docs/apps/build/purchase-options/subscriptions/contracts#how-are-code-discounts-verified)How are code discounts verified

A code discount is only verified when the code discount is first applied, either at checkout or when adding the discount to an existing subscription contract. After a code discount is successfully applied, it doesn't evaluate the conditions that were used in its first application again. Other conditions, such as recurring cycle limit, still apply.

#### [Anchor to Usage limits](/docs/apps/build/purchase-options/subscriptions/contracts#usage-limits)Usage limits

The usage limit of a code discount is validated when the code discount is applied to an existing subscription contract or if the code discount is used on a subscription at checkout.

If the usage limit has been reached, then the discount is rejected. The usage count of a code discount increases when it's saved on the subscription. The usage count doesn't decrease when removed from a subscription contract.

### [Anchor to How are automatic discounts verified](/docs/apps/build/purchase-options/subscriptions/contracts#how-are-automatic-discounts-verified)How are automatic discounts verified

An automatic discount is verified and automatically applied at cart or checkout. After an automatic discount is successfully applied, it doesn't evaluate the conditions that were used in its first application again. Other conditions, such as recurring cycle limit, still apply.

### [Anchor to Cancellation discounts](/docs/apps/build/purchase-options/subscriptions/contracts#cancellation-discounts)Cancellation discounts

Apps that provide a cancellation discount to potential churning subscribers can configure and save the discount as a manual discount on the subscription contract.

### [Anchor to Update line items of subscription contracts](/docs/apps/build/purchase-options/subscriptions/contracts#update-line-items-of-subscription-contracts)Update line items of subscription contracts

When line items are added, updated, or removed from a subscription contract draft, Shopify reapplies the discount on the remaining applicable items.

---

## [Anchor to Subscription-related webhooks](/docs/apps/build/purchase-options/subscriptions/contracts#subscription-related-webhooks)Subscription-related webhooks

Your app can subscribe to webhooks that are related to subscription events. The following examples show the JSON responses from each of the available webhooks.

To learn how to set up and consume webhooks, refer to [Webhooks configuration overview](/docs/apps/build/webhooks/subscribe).

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

// Occurs when a contract is first created. This is deferred until after the order is created. Requires the read\_own\_subscription\_contracts scope.

{

"admin\_graphql\_api\_id": "gid:\/\/shopify\/SubscriptionContract\/9998878778",

"id": 9998878778,

"billing\_policy": {

"interval": "month",

"interval\_count": 1,

"min\_cycles": 1,

"max\_cycles": 2

},

"currency\_code": "USD",

"customer\_id": 1,

"admin\_graphql\_api\_customer\_id": "gid:\/\/shopify\/Customer\/1",

"delivery\_policy": {

"interval": "week",

"interval\_count": 2

},

"status": "active",

"admin\_graphql\_api\_origin\_order\_id": "gid://shopify/Order/1",

"origin\_order\_id": 1,

"revision\_id": "9998878778"

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

// Occurs when a contract is updated. Requires the read\_own\_subscription\_contracts scope.

{

"admin\_graphql\_api\_id": "gid:\/\/shopify\/SubscriptionContract\/9998878778",

"id": 9998878778,

"billing\_policy": {

"interval": "month",

"interval\_count": 1,

"min\_cycles": 1,

"max\_cycles": 2

},

"currency\_code": "USD",

"customer\_id": 1,

"admin\_graphql\_api\_customer\_id": "gid:\/\/shopify\/Customer\/1",

"delivery\_policy": {

"interval": "week",

"interval\_count": 2

},

"status": "active",

"admin\_graphql\_api\_origin\_order\_id": "gid://shopify/Order/1",

"origin\_order\_id": 1,

"revision\_id": "9998878778"

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

// Occurs when a billing attempt succeeds. Requires the read\_own\_subscription\_contracts scope.

{

"id": null,

"admin\_graphql\_api\_id": null,

"idempotency\_key": "9a453d81-d41d-403e-806f-714dee215ff9",

"order\_id": 1,

"admin\_graphql\_api\_order\_id": "gid://shopify/Order/1",

"subscription\_contract\_id": 9998878778,

"admin\_graphql\_api\_subscription\_contract\_id": "gid://shopify/SubscriptionContract/9998878778",

"ready": true,

"error\_message": null,

"error\_code": null

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

// Occurs when a billing attempt fails. Requires the read\_own\_subscription\_contracts scope.

{

"id": null,

"admin\_graphql\_api\_id": null,

"idempotency\_key": "9a453d81-d41d-403e-806f-714dee215ff9",

// For a billing attempt failure, the order\_id might be null.

"order\_id": null,

"admin\_graphql\_api\_order\_id": null,

"subscription\_contract\_id": 9998878778,

"admin\_graphql\_api\_subscription\_contract\_id": "gid://shopify/SubscriptionContract/9998878778",

"ready": true,

// The error message is populated.

"error\_message": "Payment method was declined by processor.",

"error\_code": "PAYMENT\_METHOD\_DECLINED"

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

// Occurs when the financial institution challenges the subscription billing attempt charge as per 3D Secure. Requires the read\_own\_subscription\_contracts scope.

{

"id": null,

"admin\_graphql\_api\_id": null,

"idempotency\_key": "9a453d81-d41d-403e-806f-714dee215ff9",

"order\_id": 1,

"admin\_graphql\_api\_order\_id": "gid://shopify/Order/1",

"subscription\_contract\_id": 9998878778,

"admin\_graphql\_api\_subscription\_contract\_id": "gid://shopify/SubscriptionContract/9998878778",

"ready": false,

"error\_message": null,

"error\_code": null

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

// Occurs when a payment method is created. Requires the read\_customer\_payment\_methods scope.

{

"admin\_graphql\_api\_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",

"token": "0eccccc666aac73efcd31094ddc4ebf0",

"customer\_id": 82850125,

"admin\_graphql\_api\_customer\_id": "gid://shopify/Customer/82850125",

"instrument\_type": "CustomerCreditCard",

"payment\_instrument": {

"last\_digits": "4242",

"month": 8,

"year": 2060,

"name": "Jim Smith",

"brand": "Visa"

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

// Occurs when a payment method is updated. Requires the read\_customer\_payment\_methods scope.

{

"admin\_graphql\_api\_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",

"token": "0eccccc666aac73efcd31094ddc4ebf0",

"customer\_id": 82850125,

"admin\_graphql\_api\_customer\_id": "gid://shopify/Customer/82850125",

"instrument\_type": "CustomerCreditCard",

"payment\_instrument": {

"last\_digits": "4242",

"month": 8,

"year": 2060,

"name": "Jim Smith",

"brand": "Visa"

}

}

9

1

// Occurs when the payment method is revoked. A JSON response isn't applicable to this webhook. Requires the read\_customer\_payment\_methods scope.

##### subscription\_contracts/create

```liquid
// Occurs when a contract is first created. This is deferred until after the order is created. Requires the read_own_subscription_contracts scope.
{
  "admin_graphql_api_id": "gid:\/\/shopify\/SubscriptionContract\/9998878778",
  "id": 9998878778,
  "billing_policy": {
    "interval": "month",
    "interval_count": 1,
    "min_cycles": 1,
    "max_cycles": 2
  },
  "currency_code": "USD",
  "customer_id": 1,
  "admin_graphql_api_customer_id": "gid:\/\/shopify\/Customer\/1",
  "delivery_policy": {
    "interval": "week",
    "interval_count": 2
  },
  "status": "active",
  "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
  "origin_order_id": 1,
  "revision_id": "9998878778"
}
```

##### subscription\_contracts/update

```liquid
// Occurs when a contract is updated. Requires the read_own_subscription_contracts scope.
{
  "admin_graphql_api_id": "gid:\/\/shopify\/SubscriptionContract\/9998878778",
  "id": 9998878778,
  "billing_policy": {
    "interval": "month",
    "interval_count": 1,
    "min_cycles": 1,
    "max_cycles": 2
  },
  "currency_code": "USD",
  "customer_id": 1,
  "admin_graphql_api_customer_id": "gid:\/\/shopify\/Customer\/1",
  "delivery_policy": {
    "interval": "week",
    "interval_count": 2
  },
  "status": "active",
  "admin_graphql_api_origin_order_id": "gid://shopify/Order/1",
  "origin_order_id": 1,
  "revision_id": "9998878778"
}
```

##### subscription\_billing\_attempts/success

```liquid
// Occurs when a billing attempt succeeds. Requires the read_own_subscription_contracts scope.
{
  "id": null,
  "admin_graphql_api_id": null,
  "idempotency_key": "9a453d81-d41d-403e-806f-714dee215ff9",
  "order_id": 1,
  "admin_graphql_api_order_id": "gid://shopify/Order/1",
  "subscription_contract_id": 9998878778,
  "admin_graphql_api_subscription_contract_id": "gid://shopify/SubscriptionContract/9998878778",
  "ready": true,
  "error_message": null,
  "error_code": null
}
```

##### subscription\_billing\_attempts/failure

```liquid
// Occurs when a billing attempt fails. Requires the read_own_subscription_contracts scope.
{
  "id": null,
  "admin_graphql_api_id": null,
  "idempotency_key": "9a453d81-d41d-403e-806f-714dee215ff9",
  // For a billing attempt failure, the order_id might be null.
  "order_id": null,
  "admin_graphql_api_order_id": null,
  "subscription_contract_id": 9998878778,
  "admin_graphql_api_subscription_contract_id": "gid://shopify/SubscriptionContract/9998878778",
  "ready": true,
  // The error message is populated.
  "error_message": "Payment method was declined by processor.",
  "error_code": "PAYMENT_METHOD_DECLINED"
}
```

##### subscription\_billing\_attempts/challenged

```liquid
// Occurs when the financial institution challenges the subscription billing attempt charge as per 3D Secure. Requires the read_own_subscription_contracts scope.
{
  "id": null,
  "admin_graphql_api_id": null,
  "idempotency_key": "9a453d81-d41d-403e-806f-714dee215ff9",
  "order_id": 1,
  "admin_graphql_api_order_id": "gid://shopify/Order/1",
  "subscription_contract_id": 9998878778,
  "admin_graphql_api_subscription_contract_id": "gid://shopify/SubscriptionContract/9998878778",
  "ready": false,
  "error_message": null,
  "error_code": null
}
```

##### customer\_payment\_methods/create

```liquid
// Occurs when a payment method is created. Requires the read_customer_payment_methods scope.
{
  "admin_graphql_api_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",
  "token": "0eccccc666aac73efcd31094ddc4ebf0",
  "customer_id": 82850125,
  "admin_graphql_api_customer_id": "gid://shopify/Customer/82850125",
  "instrument_type": "CustomerCreditCard",
  "payment_instrument": {
    "last_digits": "4242",
    "month": 8,
    "year": 2060,
    "name": "Jim Smith",
    "brand": "Visa"
  }
}
```

##### customer\_payment\_methods/update

```liquid
// Occurs when a payment method is updated.	Requires the read_customer_payment_methods scope.
{
  "admin_graphql_api_id": "gid://shopify/CustomerPaymentMethod/0eccccc666aac73efcd31094ddc4ebf0",
  "token": "0eccccc666aac73efcd31094ddc4ebf0",
  "customer_id": 82850125,
  "admin_graphql_api_customer_id": "gid://shopify/Customer/82850125",
  "instrument_type": "CustomerCreditCard",
  "payment_instrument": {
    "last_digits": "4242",
    "month": 8,
    "year": 2060,
    "name": "Jim Smith",
    "brand": "Visa"
  }
}
```

##### customer\_payment\_methods/revoke

```liquid
// Occurs when the payment method is revoked. A JSON response isn't applicable to this webhook. Requires the read_customer_payment_methods scope.
```

### [Anchor to Revision ID](/docs/apps/build/purchase-options/subscriptions/contracts#revision-id)Revision ID

The `revision_id` field in the payload for the `subscription_contracts/create` and `subscription_contracts/update` webhooks is a version identifier that you can use to determine whether your subscription contract record is up-to-date. You can keep a copy of the last `revision_id` that you received with your subscription contract record, and compare it to the one that's included in the event payload. If the `revision_id` of the subscription contract in your record is greater than the `revision_id` that's received in the new webhook payload, then your subscription contract is up-to-date.

For example, if a webhook payload for the [`subscriptionContractCreate`](/docs/api/admin-graphql/latest/mutations/subscriptionContractCreate) mutation returned a `revision_id` of `1000`, and the subsequent webhook payload for the [`subscriptionContractUpdate`](/docs/api/admin-graphql/latest/mutations/subscriptionContractUpdate) mutation returns a `revision_id` of `1050`, then the update mutation occurred after the create mutation.

New `revision_id` values are incremental but not continuous. For example, a `revision_id` of `50` followed by a `revision_id` of `70` doesn't indicate that there are 20 versions of the subscription contract between the first and second IDs. `revision_id` determine if the subscription contract on your record is up-to-date.

---

## [Anchor to Next steps](/docs/apps/build/purchase-options/subscriptions/contracts#next-steps)Next steps

* Learn how to [create a subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract), and schedule and automate billing attempts for the subscription contract.
* Learn how to [update a subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts/update-a-subscription-contract) with new information.

---

Was this page helpful?

YesNo