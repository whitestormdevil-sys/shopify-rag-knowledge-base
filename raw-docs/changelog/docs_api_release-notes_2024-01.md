---
source: https://shopify.dev/docs/api/release-notes/2024-01
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| January 1, 2024 | January 1, 2025 |

**What's new in 2024-01**

The 2024-01 version of Shopify's APIs include the following highlights:

* [Buy X Get Y discounts](/docs/apps/build/discounts#related-mutations-and-queries) now support setting a fixed amount discount.
* The new [`orderCancel`](/docs/api/admin-graphql/2024-01/mutations/orderCancel) mutation enables you to cancel orders.
* You can now [schedule changes to inventory quantities](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#schedule-changes-to-inventory-quantities).
* More granular capabilities are available for separating and combining line items inside a [fulfillment order](/docs/api/admin-graphql/2024-01/objects/FulfillmentOrder).
* You can now update and remove discounts when [editing orders](/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders#add-a-discount-to-the-variant).
* [Various improvements](#graphql-admin-api-changes) have been made to subscription contracts, subscription billing attempts, metaobjects, metafield definitions, and marketing activities.
* [Webhook sub-topics](/docs/apps/build/webhooks/customize/sub-topics) enable the delivery of a more specific and relevant stream of webhooks to your app.
* [New types](#payments-apps-api-changes) enable some credit card [payment apps](/docs/apps/build/payments) to support vaulting card data in Shopify.
* Several improvements have been made to [Shopify Function APIs](#shopify-function-apis-changes).
* The new [Customer Account API](/docs/api/customer) offers a secure and private way of accessing private customer-scoped data.

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2024-01#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Change to AppSubscriptionDiscountInput](/docs/api/release-notes/previous-versions/2024-01#change-to-appsubscriptiondiscountinput)Change to AppSubscriptionDiscountInput

The [`durationLimitInIntervals`](/docs/api/admin-graphql/2024-01/input-objects/AppSubscriptionDiscountInput#field-appsubscriptiondiscountinput-durationlimitinintervals) field on the `AppSubscriptionDiscountInput` input object no longer accepts `0` as a value.

To create a discount with an unlimited duration, don't specify the `durationLimitInIntervals` field.

### [Anchor to Field deprecation on ProductInput](/docs/api/release-notes/previous-versions/2024-01#field-deprecation-on-productinput)Field deprecation on ProductInput

We've deprecated the [`images` field on the `ProductInput` input object](/docs/api/admin-graphql/2024-01/input-objects/ProductInput#field-productinput-images).

Use the `media` argument on the [`productCreate`](/docs/api/admin-graphql/2023-10/mutations/productcreate#argument-media) and [`productUpdate`](/docs/api/admin-graphql/2023-10/mutations/productupdate#argument-media) mutations instead.

### [Anchor to Field removals on ProductVariantInput](/docs/api/release-notes/previous-versions/2024-01#field-removals-on-productvariantinput)Field removals on ProductVariantInput

We've removed the deprecated `imageId` and `imageSrc` fields from the [`ProductVariantInput`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput) input object.

Use the [`mediaId`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput#field-productvariantinput-mediaid) and [`mediaSrc`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput#field-productvariantinput-mediasrc) fields instead.

### [Anchor to Field removal on the Shipping Discount Function API](/docs/api/release-notes/previous-versions/2024-01#field-removal-on-the-shipping-discount-function-api)Field removal on the Shipping Discount Function API

We've removed the deprecated `discountApplicationStrategy` field on the [`FunctionRunResult`](/docs/api/functions/reference/shipping-discounts/graphql/functionrunresult?api%5Bversion%5D=latest) object, and its predecessor, the [`FunctionResult`](/docs/api/functions/reference/shipping-discounts/graphql/functionresult?api%5Bversion%5D=latest) object.

The discount application strategy for shipping discount functions is always considered to be `ALL`. This means that all applicable discounts are returned by a shipping discount function.

### [Anchor to Handle as a scalar type on Shopify Function APIs](/docs/api/release-notes/previous-versions/2024-01#handle-as-a-scalar-type-on-shopify-function-apis)Handle as a scalar type on Shopify Function APIs

The following fields and arguments that return a handle to identify a [Function](/docs/apps/build/functions) resource now use the appropriate `Handle` scalar as their type:

Fields and arguments that use `Handle` as a scalar type

| Name | Type | Change |
| --- | --- | --- |
| `handle` | Field | On the `CartDeliveryOption` object for all Function APIs |
| `handle` | Field | On the `Product` object for all Function APIs |
| `deliveryOptionHandle` | Field | On the `MoveOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/moveoperation?api%5Bversion%5D=latest)) |
| `deliveryOptionHandle` | Field | On the `RenameOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/renameoperation?api%5Bversion%5D=latest)) |
| `deliveryOptionHandle` | Field | On the `HideOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/hideoperation?api%5Bversion%5D=latest)) |
| `handle` | Field | On the `GateConfiguration` object for all Function APIs |
| `handle` | Argument | On the `HasGates` interface for all Function APIs |
| `handle` | Field | On the `Market` object for all Function APIs |

### [Anchor to Marketing activities](/docs/api/release-notes/previous-versions/2024-01#marketing-activities)Marketing activities

The following breaking changes have been made to marketing activity types on the GraphQL Admin API:

* The `channel` field on the [`marketingActivityCreateExternal`](/docs/api/admin-graphql/2024-01/mutations/marketingActivityCreateExternal) and [`marketingActivityUpdateExternal`](/docs/api/admin-graphql/2024-01/mutations/marketingActivityUpdateExternal) mutations has been renamed to `marketingChannelType`.
* `utcOffset` and `isCumulative` are now required fields on the [`marketingEngagementInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingEngagementInput) input object.
* The `fetchedAt` field has been removed from the [`marketingEngagementInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingEngagementInput) input object.
* The `utm` field has been deprecated from the [`MarketingActivityUpdateExternalInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingActivityUpdateExternalInput) input object.

### [Anchor to Marketing fields and properties removals](/docs/api/release-notes/previous-versions/2024-01#marketing-fields-and-properties-removals)Marketing fields and properties removals

* **GraphQL Admin API**: We've removed the following deprecated fields on the [`Customer`](/docs/api/admin-graphql/2024-01/objects/Customer) object and [`CustomerInput`](/docs/api/admin-graphql/2024-01/input-objects/CustomerInput) input object:

  + `acceptsMarketing`
  + `acceptsMarketingUpdatedAt`
  + `MarketingOptInLevel`

    Use the [`emailMarketingConsent`](/docs/api/admin-graphql/2024-01/objects/Customer#field-customer-emailmarketingconsent) field instead.
* **REST Admin API**: We've removed the following deprecated properties on the [`Order`](/docs/api/admin-rest/2024-01/resources/order) and [`Customer`](/docs/api/admin-rest/2024-01/resources/customer) resources:

  + `accepts_marketing`
  + `accepts_marketing_updated_at`
  + `marketing_opt_in_level`

    Use the [`email_marketing_consent`](/docs/api/admin-rest/2024-01/resources/customer#resource-object) property instead.

### [Anchor to Subscription billing attempts](/docs/api/release-notes/previous-versions/2024-01#subscription-billing-attempts)Subscription billing attempts

The [`SubscriptionBillingAttemptCreate`](/docs/api/admin-graphql/2024-01/mutations/subscriptionBillingAttemptCreate) mutation now prevents the creation of billing attempts if a subscription contract has one of the following terminal statuses:

* `EXPIRED`
* `CANCELLED`
* `STALE`

  We've also added the [`CONTRACT_TERMINATED`](/docs/api/admin-graphql/2024-01/enums/BillingAttemptUserErrorCode#value-contractterminated) error code to the `BillingAttemptUserErrorCode` enum. This new error code is returned in the case where billing attempt creation is prevented.

  [Learn how to schedule and automate the billing of subscriptions](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

### [Anchor to Subscription contracts](/docs/api/release-notes/previous-versions/2024-01#subscription-contracts)Subscription contracts

The `STALE` value on the [`SubscriptionContractSubscriptionStatus`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus) enum has been removed. Existing subscription contracts with the `STALE` status will be returned as `CANCELLED`, and you won't be able to update the status of a subscription contract to `STALE`.

Use the [`EXPIRED`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus#value-expired) or [`CANCELLED`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus#value-cancelled) values instead.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2024-01#graphql-admin-api-changes)GraphQL Admin API changes

The following are all the changes currently introduced in the 2024-01 version of the GraphQL Admin API.

### [Anchor to Abandoned checkouts](/docs/api/release-notes/previous-versions/2024-01#abandoned-checkouts)Abandoned checkouts

You can now query a single line item in an abandoned checkout by using the [`AbandonedCheckoutLineItem`](/docs/api/admin-graphql/2024-01/objects/AbandonedCheckoutLineItem) object. The [`title`](/docs/api/admin-graphql/2024-01/objects/AbandonedCheckoutLineItem#field-abandonedcheckoutlineitem-title) field on the `AbandonedCheckoutLineItem` object, which defaults to the product title, can now also accept a `null` value.

### [Anchor to App subscription discounts](/docs/api/release-notes/previous-versions/2024-01#app-subscription-discounts)App subscription discounts

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

The [`durationLimitInIntervals`](/docs/api/admin-graphql/2024-01/input-objects/AppSubscriptionDiscountInput#field-appsubscriptiondiscountinput-durationlimitinintervals) field on the `AppSubscriptionDiscountInput` input object no longer accepts `0` as a value.

To create a discount with an unlimited duration, don't specify the `durationLimitInIntervals` field.

### [Anchor to Buy X Get Y discounts](/docs/api/release-notes/previous-versions/2024-01#buy-x-get-y-discounts)Buy X Get Y discounts

Buy X Get Y discounts now support setting a fixed amount discount. You can use this option alongside the existing percentage or free item discount options for a minimum qualifying purchase.

For example, you can set a fixed amount discount to create promotions such as "Buy 2 items, get $20 off". Fixed amount discounts can be set for an automatic discount or a discount code using the [GraphQL Admin API](/docs/api/admin-graphql/2024-01/unions/DiscountEffect).

[Learn how to create and manage different types of discounts](/docs/apps/build/discounts#related-mutations-and-queries).

### [Anchor to Cancelling orders](/docs/api/release-notes/previous-versions/2024-01#cancelling-orders)Cancelling orders

You can now use the [`orderCancel`](/docs/api/admin-graphql/2024-01/mutations/orderCancel) mutation to cancel an order. The mutation enables apps to specify some options for cancellation, a reason for cancellation, and a merchant-facing staff note. For example, options for cancellation might include whether to refund a customer, restock inventory quantities, or notify a customer.

The mutation performs cancellation asynchronously in a background job and returns a [`Job`](/docs/api/admin-graphql/2024-01/objects/Job) object that you can [query](/docs/api/admin-graphql/2024-01/queries/job) to poll for the cancellation status.

**New types**

New types for cancelling orders

| Name | Type | Change |
| --- | --- | --- |
| `orderCancel` | Mutation | Added |
| `OrderCancelUserError` | Object | Added |

### [Anchor to Capturing transactions multiple times](/docs/api/release-notes/previous-versions/2024-01#capturing-transactions-multiple-times)Capturing transactions multiple times

You can now use the [`multiCapturable` field on the `OrderTransaction` object](/docs/api/admin-graphql/2024-01/objects/OrderTransaction#field-ordertransaction-multicapturable) to determine whether a transaction can be captured multiple times.

### [Anchor to Cart and checkout operations](/docs/api/release-notes/previous-versions/2024-01#cart-and-checkout-operations)Cart and checkout operations

The [`CartTransformCreate`](/docs/api/admin-graphql/2024-01/mutations/cartTransformCreate) mutation now supports a `blockOnFailure` argument that determines if cart and checkout operations should be blocked if a [Cart Transform function](/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function) fails to run. This mutation can be used as a safeguard if the Cart Transform function is considered a critical component in resolving merchandise attributes, such price, title, or image.

**New types**

New types for cart and checkout operations

| Name | Type | Change |
| --- | --- | --- |
| `blockOnFailure` | Argument | Added to the `CartTransformCreate` mutation |
| `blockOnFailure` | Field | Added to the `CartTransform` object |

### [Anchor to Checkout branding](/docs/api/release-notes/previous-versions/2024-01#checkout-branding)Checkout branding

You can now use the [`checkoutBrandingUpsert`](/docs/api/admin-graphql/2024-01/mutations/checkoutBrandingUpsert) mutation to reset branding settings to their default state without resetting each field explicitly. You can pass a `null` value to the [`checkoutBrandingInput`](/docs/api/admin-graphql/2024-01/mutations/checkoutBrandingUpsert#argument-checkoutbrandinginput) argument to clear all of the branding settings, which will revert the branding of the checkout to its default state.

You can also use the GraphQL Admin API to customize the look of the `ChoiceList` components in checkout.

**New types**

New types for checkout branding

| Name | Type | Change |
| --- | --- | --- |
| `checkoutBrandingUpsert` | Mutation | Added |
| `choiceList` | Field | Added to the `CheckoutBrandingCustomizationsInput` input object |
| `choiceList` | Field | Added to the `CheckoutBrandingCustomizations` object |

### [Anchor to Customer data erasure](/docs/api/release-notes/previous-versions/2024-01#customer-data-erasure)Customer data erasure

You can now use the GraphQL Admin API to enable merchants to handle customer data erasure requests in compliance with General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), and other data protection regulations.

To learn more about how data erasure is processed and the impact on customer data, refer to [Processing customer data requests](https://help.shopify.com/manual/privacy-and-security/privacy/processing-customer-data-requests#erase-customer-personal-data).

**New types**

New types for customer data erasure

| Name | Type | Change |
| --- | --- | --- |
| `customerRequestDataErasure` | Mutation | Added |
| `customerCancelDataErasure` | Mutation | Added |
| `CustomerRequestDataErasureUserError` | Object | Added |
| `CustomerCancelDataErasureUserError` | Object | Added |

### [Anchor to Deleting market regions](/docs/api/release-notes/previous-versions/2024-01#deleting-market-regions)Deleting market regions

You can now use the [`marketRegionsDelete`](/docs/api/admin-graphql/2024-01/mutations/marketRegionsDelete) mutation to delete a list of market regions.

[Learn more about Shopify Markets](/docs/apps/build/markets).

### [Anchor to Filtering prices](/docs/api/release-notes/previous-versions/2024-01#filtering-prices)Filtering prices

You can now use a new `query` parameter on the [`prices` connection of the `PriceList` object](/docs/api/admin-graphql/2024-01/objects/PriceList#connection-pricelist-prices) to filter prices for each product or product variant ID.

For example, `prices(first: 10, query: "product_id:1")` filters the first ten prices of a product with an ID of `gid://shopify/Product/1`.

Similarly, `prices(first: 10, query: "variant_id:1")` filters the first ten prices for a product variant with an ID of `gid://shopify/ProductVariant/1`.

### [Anchor to Financial summaries](/docs/api/release-notes/previous-versions/2024-01#financial-summaries)Financial summaries

You can now use the `financialSummaries` field on the [`FulfillmentOrderLineItem`](/docs/api/admin-graphql/2024-01/objects/FulfillmentOrderLineItem) object to retrieve the financial summary of a fulfillment order's line items.

With this change, order information that's required to calculate the financial specifics of an order is accessible using the `fulfillmentOrder.lineItems` connection and any of the `fulfillment_orders` access scopes. The same data is available using `fulfillmentOrder.order.lineItems`, but requires the `read_orders` access scope.

**New types**

New types for financial summaries

| Name | Type | Change |
| --- | --- | --- |
| `FulfillmentOrderLineItemFinancialSummary` | Object | Added |
| `FinancialSummaryDiscountAllocation` | Object | Added |
| `FinancialSummaryDiscountApplication` | Object | Added |
| `financialSummaries` | Field | Added to the `FulfillmentOrderLineItem` object |

### [Anchor to Fulfillment hold reasons](/docs/api/release-notes/previous-versions/2024-01#fulfillment-hold-reasons)Fulfillment hold reasons

A new fulfillment hold reason ([`AWAITING_RETURN_ITEMS`](/docs/api/admin-graphql/2024-01/enums/FulfillmentHoldReason#value-awaitingreturnitems)) is now applied to a [fulfillment hold](/docs/api/admin-graphql/2024-01/objects/FulfillmentHold) on a fulfillment order when a return is created with exchange items.

### [Anchor to Including translations when duplicating products](/docs/api/release-notes/previous-versions/2024-01#including-translations-when-duplicating-products)Including translations when duplicating products

You can now specify whether to include translations when you run the [`productDuplicate`](/docs/api/admin-graphql/2024-01/mutations/productDuplicate) mutation. If you specify the optional `includeTranslations` argument as `true`, then all translations that are saved on the product and its associated variants and metafields are copied over to the new product.

### [Anchor to Localizing metaobjects for different markets](/docs/api/release-notes/previous-versions/2024-01#localizing-metaobjects-for-different-markets)Localizing metaobjects for different markets

Metaobjects are now exposed as a value on the [`MarketLocalizableResourceType`](/docs/api/admin-graphql/2024-01/enums/MarketLocalizableResourceType#value-metaobject) enum. This means that metaobjects with a translatable capability are eligible for custom content by market through the GraphQL Admin API as well as the [Translate and Adapt](https://apps.shopify.com/translate-and-adapt) app. Localizable fields are determined by the metaobject type.

### [Anchor to Marketing activities: Field changes](/docs/api/release-notes/previous-versions/2024-01#marketing-activities-field-changes)Marketing activities: Field changes

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

The following breaking changes have been made to marketing activity types:

* The `channel` field on the [`marketingActivityCreateExternal`](/docs/api/admin-graphql/2024-01/mutations/marketingActivityCreateExternal) and [`marketingActivityUpdateExternal`](/docs/api/admin-graphql/2024-01/mutations/marketingActivityUpdateExternal) mutations has been renamed to `marketingChannelType`.
* `utcOffset` and `isCumulative` are now required fields on the [`marketingEngagementInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingEngagementInput) input object.
* The `fetchedAt` field has been removed from the [`marketingEngagementInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingEngagementInput) input object.
* The `utm` field has been deprecated from the [`MarketingActivityUpdateExternalInput`](/docs/api/admin-graphql/2024-01/input-objects/MarketingActivityUpdateExternalInput) input object.

### [Anchor to Marketing activites: Improvements](/docs/api/release-notes/previous-versions/2024-01#marketing-activites-improvements)Marketing activites: Improvements

We've made improvements to creating marketing activities, syncing aggregate marketing activity data, and deleting marketing activities.

**New types**

New types for marketing activities

| Name | Type | Change |
| --- | --- | --- |
| `marketingActivityUpsertExternal` | Mutation | Added. Used to sync externally managed activities without having to keep track of Shopify IDs. [Bulk mutation support](/docs/api/usage/bulk-operations/imports) has also been added to this mutation. |
| `marketingActivityCreateExternal` | Mutation | Added. Used to create a hierarchy of activities. Activities can be created to represent ads, ad groups, or campaigns. |
| `marketingActivityDeleteExternal` | Mutation | Added. Used to delete a single external marketing activity. |
| `marketingActivitiesDeleteAllExternal` | Mutation | Added. Used to enqueue a job to bulk delete all external marketing activities and cleanup data if a store owner revokes permission to sync data to Shopify. |
| `remoteId` | Field | Added. Used to reference a marketing activity in the [marketingEngagementCreate](/docs/api/admin-graphql/2024-01/mutations/marketingEngagementCreate) mutation. |
| `marketingEngagementCreate` | Mutation | Added. Used to sync aggregate data at the activity level and at the channel level. [Bulk mutation support](/docs/api/usage/bulk-operations/imports) has also been added to this mutation. |
| `marketingEngagementsDelete` | Mutation | Added. Used to enqueue a job to delete all channel-level data that was sent through the [marketingEngagementCreate](/docs/api/admin-graphql/2024-01/mutations/marketingEngagementCreate) mutation and cleanup data if a store owner revokes permission to sync data to Shopify. |

### [Anchor to Marketing fields](/docs/api/release-notes/previous-versions/2024-01#marketing-fields)Marketing fields

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

We've removed the following deprecated fields on the [`Customer`](/docs/api/admin-graphql/2024-01/objects/Customer) object and [`CustomerInput`](/docs/api/admin-graphql/2024-01/input-objects/CustomerInput) input object:

* `acceptsMarketing`
* `acceptsMarketingUpdatedAt`
* `MarketingOptInLevel`

  Use the [`emailMarketingConsent`](/docs/api/admin-graphql/2024-01/objects/Customer#field-customer-emailmarketingconsent) field instead.

### [Anchor to Metaobjects and metaobject definitions](/docs/api/release-notes/previous-versions/2024-01#metaobjects-and-metaobject-definitions)Metaobjects and metaobject definitions

We've added new fields so that you can query for the user or app that created a metaobject or metaobject definition.

**New types**

New fulfillment order webhook topics

| Name | Type | Change |
| --- | --- | --- |
| `createdByApp` | Field | Added to the `MetaobjectDefinition` object |
| `createdByStaff` | Field | Added to the `MetaobjectDefinition` object |
| `createdByApp` | Field | Added to the `Metaobject` object |
| `createdByStaff` | Field | Added to the `Metaobject` object |

### [Anchor to New metafields error code](/docs/api/release-notes/previous-versions/2024-01#new-metafields-error-code)New metafields error code

We've added the `CAPABILITY_VIOLATION` error code to the [`MetafieldsSetUserErrorCode`](/docs/api/storefront/2024-01/enums/MetafieldsSetUserErrorCode) enum. The error code is returned if you attempt to update a metafield in a way that doesn't conform to the enabled capabilities.

### [Anchor to Order editing](/docs/api/release-notes/previous-versions/2024-01#order-editing)Order editing

You can now update and remove discounts when editing orders. To learn more about using discounts with order edits, refer to [Edit an existing order](/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders#add-a-discount-to-the-variant).

**New types**

New types for order editing

| Name | Type | Change |
| --- | --- | --- |
| `orderEditUpdateDiscount` | Mutation | Added |
| `orderEditRemoveDiscount` | Mutation | Added |

### [Anchor to Order routing](/docs/api/release-notes/previous-versions/2024-01#order-routing)Order routing

The `ORDER_ROUTING_LOCATION_RULE` value has been added to the [`MetafieldOwnerType`](/docs/api/admin-graphql/2024-01/enums/MetafieldOwnerType) enum. To learn more about order routing, refer to [Order routing apps](/docs/apps/build/orders-fulfillment/order-routing-apps).

### [Anchor to Product images](/docs/api/release-notes/previous-versions/2024-01#product-images)Product images

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

We've deprecated the [`images` field on the `ProductInput` input object](/docs/api/admin-graphql/2024-01/input-objects/ProductInput#field-productinput-images).

Use the `media` argument on the [`productCreate`](/docs/api/admin-graphql/2023-10/mutations/productcreate#argument-media) and [`productUpdate`](/docs/api/admin-graphql/2023-10/mutations/productupdate#argument-media) mutations instead.

### [Anchor to Product variant images](/docs/api/release-notes/previous-versions/2024-01#product-variant-images)Product variant images

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

We've removed the deprecated `imageId` and `imageSrc` fields from the [`ProductVariantInput`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput) input object.

Use the [`mediaId`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput#field-productvariantinput-mediaid) and [`mediaSrc`](/docs/api/admin-graphql/2024-01/input-objects/ProductVariantInput#field-productvariantinput-mediasrc) fields instead.

### [Anchor to Retrieving payment details for transactions](/docs/api/release-notes/previous-versions/2024-01#retrieving-payment-details-for-transactions)Retrieving payment details for transactions

You can now use the `paymentDetails` field on the [`SuggestedOrderTransaction`](/docs/api/admin-graphql/2024-01/objects/SuggestedOrderTransaction) object to retrieve payment details that are related to a transaction.

### [Anchor to Scheduling changes to inventory quantities](/docs/api/release-notes/previous-versions/2024-01#scheduling-changes-to-inventory-quantities)Scheduling changes to inventory quantities

You can now [schedule changes to inventory quantities](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#schedule-changes-to-inventory-quantities) using the [`InventorySetScheduledChanges`](/docs/api/admin-graphql/2024-01/mutations/InventorySetScheduledChanges) mutation.
For example, if an app user creates a purchase order and adds incoming quantities for a specified inventory item at a location, then they can also create a scheduled change that states the date that the quantities are expected to be transitioning from `incoming` to `available`. Information about scheduled changes to inventory quantities can help merchants make better buying or selling decisions.

Note

The [`InventorySetScheduledChanges`](/docs/api/admin-graphql/2024-01/mutations/InventorySetScheduledChanges) mutation won't automatically change inventory quantities. To change inventory quantities, you still need to use other inventory mutations, such as [`InventoryAdjustQuantitites`](/docs/api/admin-graphql/2024-01/mutations/inventoryAdjustQuantities), [`inventorySetQuantities`](/docs/api/admin-graphql/2024-01/mutations/inventorySetQuantities), or [`inventoryMoveQuantities`](/docs/api/admin-graphql/2024-01/mutations/inventoryMoveQuantities).

**Note:**

The [`InventorySetScheduledChanges`](/docs/api/admin-graphql/2024-01/mutations/InventorySetScheduledChanges) mutation won't automatically change inventory quantities. To change inventory quantities, you still need to use other inventory mutations, such as [`InventoryAdjustQuantitites`](/docs/api/admin-graphql/2024-01/mutations/inventoryAdjustQuantities), [`inventorySetQuantities`](/docs/api/admin-graphql/2024-01/mutations/inventorySetQuantities), or [`inventoryMoveQuantities`](/docs/api/admin-graphql/2024-01/mutations/inventoryMoveQuantities).

**New types**

The following new types are available:

New types for scheduling changes to inventory quantities

| Name | Type | Change |
| --- | --- | --- |
| `InventorySetScheduledChanges` | Mutation | Added |
| `InventoryScheduledChange` | Object | Added |
| `InventoryScheduledChangeInput` | Input object | Added |
| `InventoryScheduledChangeItemInput` | Input object | Added |
| `InventorySetScheduledChangesInput` | Input object | Added |
| `scheduledChanges` | Connection | Added to the `InventoryLevel` object |
| `id` | Field | Added to the `InventoryQuantity` object. The `InventoryQuantity` object now implements a `Node` interface. |

### [Anchor to Separating and combining fulfillment order line items](/docs/api/release-notes/previous-versions/2024-01#separating-and-combining-fulfillment-order-line-items)Separating and combining fulfillment order line items

We've added more granular capabilities for separating and combining line items inside a [fulfillment order](/docs/api/admin-graphql/2024-01/objects/FulfillmentOrder) so that you can partially fulfill an order or [change the location](/docs/api/admin-graphql/2024-01/objects/FulfillmentOrderLocationForMove) of specific line items.

**New types**

The following new types are available:

New types for separating and combining fulfillment order line items

| Name | Type | Change |
| --- | --- | --- |
| `lineItemIds` | Argument | Added to the `locationsForMove` connection on the `FulfillmentOrder` object |
| `query` | Argument | Added to the `locationsForMove` connection on the `FulfillmentOrder` object |
| `locationIds` | Argument | Added to the `locationsForMove` connection on the `FulfillmentOrder` object |
| `fulfillmentOrdersForMerge` | Connection | Added to the `FulfillmentOrder` object |
| `availableLineItems` | Connection | Added to the `FulfillmentOrderLocationForMove` object |
| `unavailableLineItems` | Connection | Added to the `FulfillmentOrderLocationForMove` object |
| `availableLineItemsCount` | Field | Added to the `FulfillmentOrderLocationForMove` object |
| `unavailableLineItemsCount` | Field | Added to the `FulfillmentOrderLocationForMove` object |
| `NO_LINE_ITEMS_PROVIDED_TO_SPLIT` | Field | Added to the `FulfillmentOrderSplitUserErrorCode` enum |

**New webhook topics**

The following new webhook topics are available:

New fulfillment order webhook topics

| Name | Type | Change |
| --- | --- | --- |
| `FULFILLMENT_ORDERS_SPLIT` | Value | Added to the `WebhookSubscriptionTopic` enum |
| `FULFILLMENT_ORDERS_MERGED` | Value | Added to the `WebhookSubscriptionTopic` enum |

### [Anchor to Shopify Payments balance transactions](/docs/api/release-notes/previous-versions/2024-01#shopify-payments-balance-transactions)Shopify Payments balance transactions

You can now use the GraphQL Admin API to query transactions that are associated with a [Shopify Payments](https://help.shopify.com/manual/payments/shopify-payments) account balance.

**New types**

The following new types are available:

New types for Shopify Payments balance transactions

| Name | Type | Change |
| --- | --- | --- |
| `ShopifyPaymentsBalanceTransaction` | Object | Added |
| `ShopifyPaymentsAccount.balanceTransactions` | Connection | Added to the `ShopifyPaymentsAccount` object |
| `BALANCE_TRANSACTION` | Value | Added to the `SearchResultType` enum |

### [Anchor to Storefront access controls for custom data](/docs/api/release-notes/previous-versions/2024-01#storefront-access-controls-for-custom-data)Storefront access controls for custom data

We've modified [storefront access controls](/docs/api/admin-graphql/2024-01/enums/MetafieldStorefrontAccess) to be more explicit for [custom data](/docs/apps/build/custom-data). The changes affect how you can modify app reserved prefixes in the Shopify admin and how apps set access controls.

App reserved prefixes are configurable. For example, if you set access for `admin` to be `MERCHANT_READ` and `storefront` to be `PUBLIC_READ` then the merchant will have read-only access in the Shopify admin, and metafields will be publicly readable on storefront surface areas, including Liquid templates and the Storefront API.

Learn more about access controls for [metafields](/docs/apps/build/custom-data/permissions) and [metaobjects](/docs/apps/build/custom-data/permissions).

**New types**

The following new types are available:

New types for storefront access controls

| Name | Type | Change |
| --- | --- | --- |
| `storefront` | Field | Added to the `MetafieldAccessInput` input object |
| `storefront` | Field | Added to the `MetafieldAccessUpdateInput` input object |
| `storefront` | Field | Added to the `MetafieldAccess` object |
| `visibleToStorefrontAPI` | Field | Added to the `MetafieldDefinitionInput` input object |
| `visibleToStorefrontAPI` | Field | Added to the `MetafieldDefinitionUpdateInput` input object |
| `visibleToStorefrontAPI` | Field | Deprecated on the `MetafieldDefinition` object |
| `MetafieldStorefrontAccess` | Enum | Added |
| `INVALID_INPUT_COMBINATION` | Value | Added to the `MetafieldDefinitionCreateUserError` enum |
| `INVALID_INPUT_COMBINATION` | Value | Added to the `MetafieldDefinitionUpdateUserError` enum |

|  |  |
| --- | --- |
| Error code | Added to the `MetafieldDefinitionUpdate` mutation |

### [Anchor to Subscription billing attempts](/docs/api/release-notes/previous-versions/2024-01#subscription-billing-attempts)Subscription billing attempts

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

The [`SubscriptionBillingAttemptCreate`](/docs/api/admin-graphql/2024-01/mutations/subscriptionBillingAttemptCreate) mutation now prevents the creation of billing attempts if a subscription contract has one of the following terminal statuses:

* `EXPIRED`
* `CANCELLED`
* `STALE`

We've also added the [`CONTRACT_TERMINATED`](/docs/api/admin-graphql/2024-01/enums/BillingAttemptUserErrorCode#value-contractterminated) error code to the `BillingAttemptUserErrorCode` enum. This new error code is returned in the case where billing attempt creation is prevented.

[Learn how to schedule and automate the billing of subscriptions](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

### [Anchor to Subscription billing cycles](/docs/api/release-notes/previous-versions/2024-01#subscription-billing-cycles)Subscription billing cycles

You can now skip or unskip a [subscription billing cycle](/docs/apps/build/purchase-options/subscriptions/billing-cycles) in a single operation. Your app can also receive webhook notifications to stay in sync with Shopify data or perform an action after a subscription billing cycle is skipped or unskipped.

**New types**

The following new types are available:

New types for subscription contracts

| Name | Type | Change |
| --- | --- | --- |
| `subscriptionBillingCycleSkip` | Mutation | Added |
| `subscriptionBillingCycleUnskip` | Mutation | Added |
| `SUBSCRIPTION_BILLING_CYCLES/SKIP` | Enum | Added |
| `SUBSCRIPTION_BILLING_CYCLES/UNSKIP` | Enum | Added |

### [Anchor to Subscription contracts: Statuses](/docs/api/release-notes/previous-versions/2024-01#subscription-contracts-statuses)Subscription contracts: Statuses

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

The `STALE` value on the [`SubscriptionContractSubscriptionStatus`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus) enum has been removed. Existing subscription contracts with the `STALE` status will be returned as `CANCELLED`, and you won't be able to update the status of a subscription contract to `STALE`.

Use the [`EXPIRED`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus#value-expired) or [`CANCELLED`](/docs/api/admin-graphql/2024-01/enums/SubscriptionContractSubscriptionStatus#value-cancelled) values instead.

### [Anchor to Subscription contracts: New mutations and webhooks](/docs/api/release-notes/previous-versions/2024-01#subscription-contracts-new-mutations-and-webhooks)Subscription contracts: New mutations and webhooks

You can now update the `status` field of a [subscription contract](/docs/apps/build/purchase-options/subscriptions/contracts) using newly available mutations. We've also introduced new webhook topics that notify your app when a subscription contract's status is changed.

**New types**

The following new types are available:

New types for subscription contracts

| Name | Type | Change |
| --- | --- | --- |
| `subscriptionContractActivate` | Mutation | Added |
| `subscriptionContractPause` | Mutation | Added |
| `subscriptionContractCancel` | Mutation | Added |
| `subscriptionContractFail` | Mutation | Added |
| `subscriptionContractExpire` | Mutation | Added |
| `SubscriptionContractStatusUpdateUserError` | Enum | Added |
| `SUBSCRIPTION_CONTRACTS/ACTIVATE` | Enum | Added |
| `SUBSCRIPTION_CONTRACTS/EXPIRE` | Enum | Added |
| `SUBSCRIPTION_CONTRACTS/FAIL` | Enum | Added |
| `SUBSCRIPTION_CONTRACTS/CANCEL` | Enum | Added |
| `SUBSCRIPTION_CONTRACTS/PAUSE` | Enum | Added |

### [Anchor to Subscriptions support for automatic discounts](/docs/api/release-notes/previous-versions/2024-01#subscriptions-support-for-automatic-discounts)Subscriptions support for automatic discounts

A subscription option for automatic discounts is now available to create automatic discounts for products.

In prior API versions, the `DiscountType` classifies any automatic discount as `MANUAL`. In API version 2024-01 and higher, the [`DiscountType`](/docs/api/admin-graphql/2024-01/enums/DiscountType) enum accurately represents an automatic discount as `AUTOMATIC_DISCOUNT`.

**New types**

The following new types are available:

New types for subscriptions support of automatic discounts

| Name | Type | Change |
| --- | --- | --- |
| `AUTOMATIC_DISCOUNT` | Value | Added to the `DiscountType` enum |
| `AUTOMATIC_DISCOUNT` | Value | Added to the `type` field on the `SubscriptionManualDiscount` object |

### [Anchor to Validation logic in cart and checkout](/docs/api/release-notes/previous-versions/2024-01#validation-logic-in-cart-and-checkout)Validation logic in cart and checkout

We've made improvements to the [validation logic](/docs/apps/build/checkout/cart-checkout-validation) you can add to cart and checkout. These improvements enable merchants to ensure order compliance with their business rules.

**New types**

The following new types are available:

New types for validation logic in cart and checkout

| Name | Type | Change |
| --- | --- | --- |
| `validation` | Argument | Added to the `validationCreate` mutation |
| `validation` | Argument | Added to the `validationDelete` mutation |
| `validation` | Argument | Added to the `validationUpdate` mutation |
| `VALIDATION` | Value | Added to the `MetafieldOwnerType` enum |

### [Anchor to Vaulting card data](/docs/api/release-notes/previous-versions/2024-01#vaulting-card-data)Vaulting card data

Some credit card [payment apps](/docs/apps/build/payments) now support vaulting card data in Shopify. This enables merchants to sell subscriptions, support card on file transactions, and use a variety of selling strategies in new ways.

To support payment apps with [Subscription APIs](/docs/apps/build/purchase-options/subscriptions#subscription-apis), we've added a `processing` status to the [`customerPaymentMethodCreditCardCreate`](/docs/api/admin-graphql/2024-01/mutations/customerPaymentMethodCreditCardCreate#field-customerpaymentmethodcreditcardcreatepayload-processing) and [`customerPaymentMethodCreditCardUpdate`](/docs/api/admin-graphql/2024-01/mutations/customerPaymentMethodCreditCardUpdate#field-customerpaymentmethodcreditcardupdatepayload-processing) mutations. If `processing` is `true`, then you won't receive back payment method data, and should resend the same operation, with the same parameters, until you receive back user errors or the payment method data.

**New types**

The following new types are available:

New types for vaulting card data

| Name | Type | Change |
| --- | --- | --- |
| `processing` | Return field | Added to the `customerPaymentMethodCreditCardCreate` mutation |
| `processing` | Return field | Added to the `customerPaymentMethodCreditCardUpdate` mutation |
| `INITIATED` | Value | Added to the `OrderPaymentStatusResult` enum |
| `PENDING` | Value | Added to the `OrderPaymentStatusResult` enum |

### [Anchor to Visual representations of metaobjects](/docs/api/release-notes/previous-versions/2024-01#visual-representations-of-metaobjects)Visual representations of metaobjects

You can now use the [`thumbnailField`](/docs/api/admin-graphql/2024-01/objects/Metaobject#field-metaobject-thumbnailfield) field to retrieve a visual representation of a metaobject. A metaobject's `thumbnailField` field returns the preferred field to represent a metaobject visually. Valid field types are `file`, for file references, and `hex`, for colors.

**New types**

The following new types are available:

New types for visual representations of metaobjects

| Name | Type | Change |
| --- | --- | --- |
| `MetaobjectThumbnail` | Object | Added |
| `thumbnailField` | Field | Added to the `Metaobject` object |
| `hasThumbnailField` | Field | Added to the `MetaobjectDefinition` object |
| `thumbnail` | Field | Added to the `MetaobjectField` object |

### [Anchor to Webhook sub-topics](/docs/api/release-notes/previous-versions/2024-01#webhook-sub-topics)Webhook sub-topics

[Webhook sub-topics](/docs/apps/build/webhooks/customize/sub-topics) are an extra level of grouping available for some webhook topics. Sub-topics work with topics to enable delivery of a more specific and relevant stream of webhooks to your app.

The following webhook topics now support sub-topics:

New webhook topics that support sub-topics

| Name | Type | Change |
| --- | --- | --- |
| `METAOBJECTS_CREATE` | Webhook topic | Added to the `WebhookSubscriptionTopic` enum |
| `METAOBJECTS_UPDATE` | Webhook topic | Added to the `WebhookSubscriptionTopic` enum |
| `METAOBJECTS_DELETE` | Webhook topic | Added to the `WebhookSubscriptionTopic` enum |

**New types**

The following new types for webhook sub-topics are available:

New types for webhook sub-topics

| Name | Type | Change |
| --- | --- | --- |
| `subTopic` | Field | Added to the `WebhookSubscription` object |
| `subTopic` | Argument | Added to the `EventBridgeWebhookSubscriptionCreate` mutation |
| `subTopic` | Argument | Added to the `PubSubWebhookSubscriptionCreate` mutation |
| `subTopic` | Argument | Added to the `WebhookSubscriptionCreate` mutation |

### [Anchor to Webhook topics for discounts](/docs/api/release-notes/previous-versions/2024-01#webhook-topics-for-discounts)Webhook topics for discounts

We've introduced new webhook topics that are sent out when a discount has been created, updated, or deleted.

New types for webhook topics for discounts

| Name | Type | Change |
| --- | --- | --- |
| `DISCOUNTS_CREATE` | Value | Added to the `WebhookSubscriptionTopic` enum |
| `DISCOUNTS_UPDATE` | Value | Added to the `WebhookSubscriptionTopic` enum |
| `DISCOUNTS_DELETE` | Value | Added to the `WebhookSubscriptionTopic` enum |

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2024-01#rest-admin-api-changes)REST Admin API changes

The following are all the changes currently introduced in the 2024-01 version of the REST Admin API.

### [Anchor to Adjustment transactions](/docs/api/release-notes/previous-versions/2024-01#adjustment-transactions)Adjustment transactions

You can now view associated order details for an adjustment transaction using the Shopify Payments [Transactions](/docs/api/admin-rest/2024-01/resources/transactions) resource. If a transaction is of type `adjustment`, then order transaction details are available as an array in the `adjustment_order_transactions` property.

### [Anchor to Current quantity of line items](/docs/api/release-notes/previous-versions/2024-01#current-quantity-of-line-items)Current quantity of line items

The `current_quantity` property has been added to the [Order](/docs/api/admin-rest/2024-01/resources/order) resource to indicate a line item's current quantity after removals.

If you're using refund line items to calculate a line item's current quantity, then we recommend migrating your app to use the new `current_quantity` property, as it's a more reliable method.

### [Anchor to Financial summaries](/docs/api/release-notes/previous-versions/2024-01#financial-summaries)Financial summaries

You can now retrieve the financial summary of a fulfillment order's line items.

The following new parameters have been added to the `FulfillmentOrder` resource endpoints that [retrieve a list of fulfillment orders for a specific order](/docs/api/admin-rest/2024-01/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders), and [retrieve a specific fulfillment order](/docs/api/admin-rest/2024-01/resources/fulfillmentorder#get-fulfillment-orders-fulfillment-order-id):

* `include_financial_summaries`: The financial summary data for each fulfillment line item.
* `include_order_reference_fields`: Whether order reference fields should be returned in the response.

### [Anchor to Marketing properties](/docs/api/release-notes/previous-versions/2024-01#marketing-properties)Marketing properties

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

We've removed the following deprecated properties on the [`Order`](/docs/api/admin-rest/2024-01/resources/order) and [`Customer`](/docs/api/admin-rest/2024-01/resources/customer) resources:

* `accepts_marketing`
* `accepts_marketing_updated_at`
* `marketing_opt_in_level`

  Use the [`email_marketing_consent`](/docs/api/admin-rest/2024-01/resources/customer#resource-object) property instead.

### [Anchor to Sales tax remittance](/docs/api/release-notes/previous-versions/2024-01#sales-tax-remittance)Sales tax remittance

The `channel_liable` property on the [Order](/docs/api/admin-rest/2024-01/resources/order) resource has been updated to reflect the value indicated by the app. The property lets you inform merchants that another party is responsible for sales tax remittance, which then helps merchants better understand the tax that they are responsible for.

The `channel_liable` property can contain the following values:

* `true`: Indicates that the channel is responsible for remittance of the tax line
* `false`: Indicates that the channel isn't responsible for remittance of the tax line

  If the `channel_liable` property isn't populated, then the value is `false`.

### [Anchor to Separating and combining fulfillment order line items](/docs/api/release-notes/previous-versions/2024-01#separating-and-combining-fulfillment-order-line-items)Separating and combining fulfillment order line items

We've added [new webhook topics](/docs/api/admin-rest/2024-01/resources/webhook) that capture separating and combining line items inside a fulfillment order.

**New webhook topics**

The following new webhook topics are available:

New fulfillment order webhook topics

| Name | Type | Change |
| --- | --- | --- |
| `fulfillment_orders/split` | Webhook topic | Added to the `Webhook` resource |
| `fulfillment_orders/merged` | Webhook topic | Added to the `Webhook` resource |

---

## [Anchor to Storefront API changes](/docs/api/release-notes/previous-versions/2024-01#storefront-api-changes)Storefront API changes

The following are all the changes currently introduced in the 2024-01 version of the Storefront API.

### [Anchor to Validation logic in cart and checkout](/docs/api/release-notes/previous-versions/2024-01#validation-logic-in-cart-and-checkout)Validation logic in cart and checkout

We've made improvements to the [validation logic](/docs/apps/build/checkout/cart-checkout-validation) you can add to cart and checkout. These improvements enable merchants to ensure order compliance with their business rules.

The [`VALIDATION_CUSTOM`](/docs/api/storefront/2024-01/enums/CartErrorCode#value-validationcustom) value has been added to `CartUserError` enum.

---

## [Anchor to Payments Apps API changes](/docs/api/release-notes/previous-versions/2024-01#payments-apps-api-changes)Payments Apps API changes

The following are all the changes currently introduced in the 2024-01 version of the Payments Apps API.

### [Anchor to Vaulting card data](/docs/api/release-notes/previous-versions/2024-01#vaulting-card-data)Vaulting card data

Some credit card [payment apps](/docs/apps/build/payments) now support vaulting card data in Shopify. This enables merchants to sell subscriptions, support card on file transactions, and use a variety of selling strategies in new ways.

**New types**

The following new types are available:

New types for vaulting card data

| Name | Type | Change |
| --- | --- | --- |
| `verificationSessionReject` | Mutation | Added |
| `verificationSessionResolve` | Mutation | Added |
| `VerificationSessionStateRejected` | Object | Added |
| `VerificationSessionStateResolved` | Object | Added |
| `VerificationSessionUserError` | Object | Added |
| `VerificationSession` | Object | Added |
| `VerificationSessionRejectionReasonInput` | Input object | Added |
| `PaymentSessionThreeDSecureAuthenticationData` | Input object | Added |
| `VerificationSessionState` | Interface | Added |
| `VerificationSessionStates` | Union | Added |
| `VerificationSessionStateCode` | Enum | Added |
| `VerificationSessionStateReason` | Enum | Added |
| `networkTransactionId` | Argument | Added to the `paymentSessionResolve` mutation |

---

## [Anchor to Shopify Function APIs changes](/docs/api/release-notes/previous-versions/2024-01#shopify-function-apis-changes)Shopify Function APIs changes

The following are all the changes currently introduced in the 2024-01 version of Shopify Function APIs.

### [Anchor to Cart and Checkout Validation Function API](/docs/api/release-notes/previous-versions/2024-01#cart-and-checkout-validation-function-api)Cart and Checkout Validation Function API

We've made improvements to the [validation logic](/docs/apps/build/checkout/cart-checkout-validation) you can add to cart and checkout. These improvements enable merchants to ensure order compliance with their business rules.

The [`validation`](/docs/api/functions/reference/cart-checkout-validation/graphql/input?api%5Bversion%5D=latest) field has been added to `Input` object.

### [Anchor to Cart Transform Function API](/docs/api/release-notes/previous-versions/2024-01#cart-transform-function-api)Cart Transform Function API

The [Cart Transform Function API's `ExpandOperation`](/docs/api/functions/reference/cart-transform/graphql/common-objects/expandoperation?api%5Bversion%5D=latest) object now enables you to set fixed prices on each component of a [bundle](/docs/apps/build/product-merchandising/bundles), resulting in a bundle price that's the sum of each component. The `ExpandOperation` object also enables you to define a custom title and image for each parent line item. This update provides for more control over bundle pricing and enables bundles to be used for add-on products.

We've also added a new [`UpdateOperation`](/docs/api/functions/reference/cart-transform/graphql/common-objects/updateoperation?api%5Bversion%5D=latest) object that allows you to override the price, title, and image of a given line item. This gives you more more flexibility to make additional customizations to items in the cart.

[Learn more about the Cart Transform Function API](/docs/api/functions/reference/cart-transform).

### [Anchor to Handle as a scalar type](/docs/api/release-notes/previous-versions/2024-01#handle-as-a-scalar-type)Handle as a scalar type

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

The following fields and arguments that return a handle to identify a Function resource now use the appropriate `Handle` scalar as their type:

Fields and arguments that use `Handle` as a scalar type

| Name | Type | Change |
| --- | --- | --- |
| `handle` | Field | On the `CartDeliveryOption` object for all Function APIs |
| `handle` | Field | On the `Product` object for all Function APIs |
| `deliveryOptionHandle` | Field | On the `MoveOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/moveoperation?api%5Bversion%5D=latest)) |
| `deliveryOptionHandle` | Field | On the `RenameOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/renameoperation?api%5Bversion%5D=latest)) |
| `deliveryOptionHandle` | Field | On the `HideOperation` input object ([Delivery Customization API](/docs/api/functions/reference/delivery-customization/graphql/common-objects/hideoperation?api%5Bversion%5D=latest)) |
| `handle` | Field | On the `GateConfiguration` object for all Function APIs |
| `handle` | Argument | On the `HasGates` interface for all Function APIs |
| `handle` | Field | On the `Market` object for all Function APIs |

### [Anchor to New fields on all Shopify Function APIs](/docs/api/release-notes/previous-versions/2024-01#new-fields-on-all-shopify-function-apis)New fields on all Shopify Function APIs

The following new fields have been added to all [Shopify Function APIs](/docs/api/functions) on the `Customer` object:

* `firstName`: The customer's first name.
* `lastName`: The customer's last name.

### [Anchor to Order Routing Location Rule API](/docs/api/release-notes/previous-versions/2024-01#order-routing-location-rule-api)Order Routing Location Rule API

The [`deliveryAddress`](/docs/api/functions/reference/order-routing-location-rule/graphql/common-objects/fulfillmentgroup?api%5Bversion%5D=latest) field was added to the `FulfillmentGroup` object.

### [Anchor to Product Discount Function API](/docs/api/release-notes/previous-versions/2024-01#product-discount-function-api)Product Discount Function API

The Product Discount Function API now supports setting the [`discountApplicationStrategy` enum to the value of `ALL`](/docs/api/functions/reference/product-discounts/graphql/common-objects/discountapplicationstrategy) in the `FunctionRunResult`. You can use this option to apply all applicable discounts returned by a product discount function.

[Learn how to build a discounts experience with Shopify Functions](/docs/apps/build/discounts).

### [Anchor to Shipping Discount Function API: Field removal](/docs/api/release-notes/previous-versions/2024-01#shipping-discount-function-api-field-removal)Shipping Discount Function API: Field removal

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-01#breaking)Breaking

We've removed the deprecated `discountApplicationStrategy` field on the [`FunctionRunResult`](/docs/api/functions/reference/shipping-discounts/graphql/functionrunresult?api%5Bversion%5D=latest) object, and its predecessor, the [`FunctionResult`](/docs/api/functions/reference/shipping-discounts/graphql/functionresult?api%5Bversion%5D=latest) object.

The discount application strategy for shipping discount functions is always considered to be `ALL`. This means that all applicable discounts are returned by a shipping discount function.

### [Anchor to Shipping Discount Function API: Public availability](/docs/api/release-notes/previous-versions/2024-01#shipping-discount-function-api-public-availability)Shipping Discount Function API: Public availability

The [Shipping Discount Function API](/docs/api/functions/reference/shipping-discounts) is now publicly available to use on all merchant stores. The API can be used for the following use cases:

* Discounting specific delivery options. For example, free standard shipping only.
* Discounting shipping based on the contents of a cart. For example, buy this candle and get free shipping.
* Discounting shipping based on buyer identity. For example, discounting based on how many orders a customer has placed.

**New types**

The following new delivery option types are also available:

New delivery options types in the Shipping Discount Function API

| Name | Type | Change |
| --- | --- | --- |
| `DeliveryOptionTarget` | Input object | Added |
| `deliveryOption` | Field | Added to the `Target` object |

---

## [Anchor to Introducing the Customer Account API](/docs/api/release-notes/previous-versions/2024-01#introducing-the-customer-account-api)Introducing the Customer Account API

The [Customer Account API](/docs/api/customer) is a new API that's available as of the 2024-01 release. The API offers a secure and private way of accessing private customer-scoped data, such as customer, orders, payments, fulfillment, discounts, refunds, and metafields.

### [Anchor to Building personalized customer experiences](/docs/api/release-notes/previous-versions/2024-01#building-personalized-customer-experiences)Building personalized customer experiences

The Customer Account API enables you to build personalized customer experiences that you can use in your [Headless or Hydrogen custom storefronts](/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen). The API offers a full range of options making it possible for customers to view their orders, manage their profile, and much more.

Version 2024-01 is the base version of the Customer Account API. We strongly recommend that you update your apps to call the 2024-01 API version. To learn how to update your app to begin calling an API version, refer to [Shopify API versioning](/docs/api/usage/versioning).

You can [provide feedback](https://github.com/Shopify/hydrogen/discussions) to help shape future iterations of the Customer Account API.

Learn more about [building with the Customer Account API](/docs/storefronts/headless/building-with-the-customer-account-api).

### [Anchor to Delivery options](/docs/api/release-notes/previous-versions/2024-01#delivery-options)Delivery options

You can now query the available delivery options for a subscription contract using the [`subscriptionContractFetchDeliveryOptions`](/docs/api/customer/2024-01/mutations/subscriptionContractFetchDeliveryOptions) mutation.

You can also select an option from a delivery options result and update the delivery method on a subscription contract using the [`subscriptionContractSelectDeliveryMethod`](/docs/api/customer/2024-01/mutations/subscriptionContractSelectDeliveryMethod) mutation.

---

Was this page helpful?

YesNo