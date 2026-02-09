---
source: https://shopify.dev/docs/api/release-notes/2023-10
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| October 1, 2023 | October 1, 2024 |

**What's new in 2023-10**

The following features were added in version 2023-10 of Shopify's APIs:

Highlights from the GraphQL and REST Admin API changes:

* We've added the `compareAtPriceRange` field to `Product`, which returns the minimum and maximum compare-at prices across a product's variants
* You can now identify the variant that was used to model a bundle after it was purchased by querying the `productvariantid` field of `LineItemGroup`.
* We've added `STAFF` to the `OrderCancelReason` GraphQL type, as a reason for canceling orders due to staff error.
* Apps can now change the name and address of fulfillment service locations.
* More flexible primary markets for multi-country stores
* We've added a `cancellation` field to the GraphQL Admin API's `Order` object. Query this field for more details about an order's cancelation, such as any staff-provided notes on why the order was cancelled on a POS app.

  Highlights from the Storefront API changes:
* Cart line items are now ordered in reverse chronological order based on when they were added.

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2023-10#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to More flexible primary markets](/docs/api/release-notes/previous-versions/2023-10#more-flexible-primary-markets)More flexible primary markets

As of API version 2023-10, primary markets can be customized in three new ways:

* Transactions can be set to any supported currency, regardless of a shop's currency.
* Countries can be set independently of the primary market's currency. For example, it's possible to combine Canada and USD.
* Price lists can be created, allowing for fixed prices and percentage adjustments for the primary market.

  Apps might need to be updated if they previously assumed that the primary market's currency and country were the same.

### [Anchor to Deprecated fields on the Customer object](/docs/api/release-notes/previous-versions/2023-10#deprecated-fields-on-the-customer-object)Deprecated fields on the Customer object

As of API version 2023-10, the following fields on the [`Customer`](/docs/api/admin-graphql/latest/objects/Customer) object have been deprecated:

* `averageOrderAmount`
* `averageOrderAmountV2`

### [Anchor to Deprecated property on the UsageCharge resource](/docs/api/release-notes/previous-versions/2023-10#deprecated-property-on-the-usagecharge-resource)Deprecated property on the UsageCharge resource

The [`UsageCharge`](/docs/api/admin-rest/latest/resources/usagecharge) resource's `billing_on` property has been deprecated.

### [Anchor to Fulfillment service location name and address](/docs/api/release-notes/previous-versions/2023-10#fulfillment-service-location-name-and-address)Fulfillment service location name and address

Apps can change the name and address of their fulfillment service locations using the GraphQL Admin API's [`LocationEdit`](/docs/api/admin-graphql/latest/mutations/locationEdit) mutation.

The mutation returns a new user error with the `CANNOT_MODIFY_ONLINE_ORDER_FULFILLMENT_FOR_FS_LOCATION` code if apps attempt to update the `fulfillsOnlineOrders` field for a fulfillment service location. This field can only be modified on manual locations.

In API version 2023-10, apps require the `write_fulfillments` access scope to edit a fulfillment service's location. Otherwise, the following error is returned:
`Access denied for locationEdit field. Required access: write_fulfillments access scope is required to edit the location associated with a fulfillment service.`

### [Anchor to Deprecated field on the ShopResourceLimits object](/docs/api/release-notes/previous-versions/2023-10#deprecated-field-on-the-shopresourcelimits-object)Deprecated field on the ShopResourceLimits object

The `skuResourceLimits` field on the GraphQL Admin API's [`ShopResourceLimits`](/docs/api/admin-graphql/latest/objects/ShopResourceLimits) object is deprecated.

We're no longer enforcing a limit of SKUs at the shop level. Instead, use `maxProductVariants` to determine the limit of variants at the product level.

### [Anchor to MetafieldDefinitionUpdate mutation: access input type changed](/docs/api/release-notes/previous-versions/2023-10#metafielddefinitionupdate-mutation-access-input-type-changed)MetafieldDefinitionUpdate mutation: access input type changed

The `access` field on the GraphQL Admin API's [`MetafieldDefinitionUpdateInput`](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionUpdateInput#top) input object has changed from type `MetafieldAccessInput`  to type `MetafieldAccessUpdateInput`. This is part of a broader API change to introduce support for explicit access grants. Refer to [the changelog](https://shopify.dev/changelog/introducing-explicit-access-grants-for-app-owned-metafields) for details.

### [Anchor to Simplified metafield interactions with default namespaces](/docs/api/release-notes/previous-versions/2023-10#simplified-metafield-interactions-with-default-namespaces)Simplified metafield interactions with default namespaces

The `namespace` field on the GraphQL Admin and Storefront APIs is now optional when you create, update, or query metafields and metafield definitions.

We've updated all relevant mutations and queries to accommodate this change. When an app interacts with metafields, the default namespace is the [app-reserved namespace](/docs/apps/build/custom-data/ownership#reserved-prefixes).

### [Anchor to Deprecated metafield.id](/docs/api/release-notes/previous-versions/2023-10#deprecated-metafieldid)Deprecated metafield.id

The metafield(id) query is no longer supported.

Query metafields using the `HasMetafields` connection of metafield owners. If necessary, you can still query by ID using the Node interface.

### [Anchor to Primary markets support multiple domains](/docs/api/release-notes/previous-versions/2023-10#primary-markets-support-multiple-domains)Primary markets support multiple domains

The following changes have been introduced to the Markets API:

* A new `Market.webPresences` connection has been added
* The pre-existing `Market.webPresence` field now returns the primary domain web presence for a primary market with more than one web presence.
* The `marketWebPresenceCreate` mutation now enables you to add web presences to the primary market.
* The required `marketId` argument has been removed from the `marketWebPresenceUpdate` and `marketWebPresenceDelete` mutations. Use the new, required `webPresenceId`` argument instead.

### [Anchor to App Revenue Attribution Record API Depreciated](/docs/api/release-notes/previous-versions/2023-10#app-revenue-attribution-record-api-depreciated)App Revenue Attribution Record API Depreciated

The App Revenue Attribution API has been removed.

`appRevenueAttributionRecordCreate` and `appRevenueAttributionRecordDelete` are no longer supported in this and future API versions.

This change removes tracking for external app revenue attributions that occur outside of the Billing API. You can now [use Google Analytics](https://www.shopify.com/partners/blog/google-analytics-app-install-event?shpxid=f10f5b0c-B636-4F96-63AB-61F65339867D) to track app installations that are driven by Shopify App Store Ads. Link these metrics to external app revenue, to calculate ad-related metrics such as ad-related return on ad spend.

### [Anchor to Removal of Shop.shopifyPaymentsAccount](/docs/api/release-notes/previous-versions/2023-10#removal-of-shopshopifypaymentsaccount)Removal of Shop.shopifyPaymentsAccount

We're removing the deprecated `Shop.shopifyPaymentsAccount` field. Use the `shopifyPaymentsAccount` query instead.

### [Anchor to Changes to Subscription Billing Attempt creation behavior](/docs/api/release-notes/previous-versions/2023-10#changes-to-subscription-billing-attempt-creation-behavior)Changes to Subscription Billing Attempt creation behavior

The [`SubscriptionBillingAttemptCreate`](/docs/api/admin-graphql/latest/mutations/subscriptionBillingAttemptCreate) mutation now limits the creation of Billing Attempts based on the Fraud Analysis result on the Subscription Contract’s [Origin Order](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-subscriptioncontract-originorder).

We've added the `CONTRACT_UNDER_REVIEW` error code to the GraphQL Admin API's [`BillingAttemptUserErrorCode`](/docs/api/admin-graphql/latest/enums/BillingAttemptUserErrorCode) enum. This new error code is returned when a Billing Attempt creation is prevented. In previous API versions, this action returned the `INVALID` error code.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2023-10#graphql-admin-api-changes)GraphQL Admin API changes

The following are all the changes introduced in the 2023-10 version of the GraphQL Admin API.

### [Anchor to New error code added for ,[object Object]](/docs/api/release-notes/previous-versions/2023-10#new-error-code-added-for-metafielddefinitionupdate)New error code added for `MetafieldDefinitionUpdate`

As of API version 2023-10, we've added the `METAOBJECT_DEFINITION_CHANGED` error code to the `MetafieldDefinitionUpdateUserErrorCode` enum. This new error code is returned if you attempt to update a `metaobject_reference` metafield definition so that it references a different metaobject definition. Previously, this action would result in an `INTERNAL_SERVER_ERROR`.

Learn more about [`METAOBJECT_DEFINITION_CHANGED`](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionUpdateUserErrorCode#value-metaobjectdefinitionchanged).

### [Anchor to More order information on the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-10#more-order-information-on-the-fulfillmentorder-object)More order information on the `FulfillmentOrder` object

As of API version 2023-10, we've added the following fields to the `FulfillmentOrder` object:

* `orderId`
* `orderName`
* `orderProcessedAt`
* `channelId`

  With this change, the order information that's required to fulfill an order is accessible on the `fulfillmentOrder` object with any of the `fulfillment_orders` access scopes. The same data is available using `fulfillmentOrder.order`, but this requires the `read_orders` access scope.

  Learn more about [`FulfillmentOrder`](/docs/api/admin-graphql/latest/objects/FulfillmentOrder).

### [Anchor to serviceCode is available on the DeliveryMethod API](/docs/api/release-notes/previous-versions/2023-10#servicecode-is-available-on-the-deliverymethod-api)serviceCode is available on the DeliveryMethod API

As of the API version 2023-10, you can use the `DeliveryMethod` object to get the value of the `serviceCode` chosen for the related `FulfillmentOrder`. The `DeliveryMethod` object is now accessible through any of the fulfillment order scopes.

Learn more about [`DeliveryMethod`](/docs/api/admin-graphql/latest/objects/DeliveryMethod).

### [Anchor to Making the primary market more flexible](/docs/api/release-notes/previous-versions/2023-10#making-the-primary-market-more-flexible)Making the primary market more flexible

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, you can customize the primary market in three new ways:

* The currency can be set to any currency independent of the merchant's shop currency.
* The country can be set independently of the primary market's currency, such that combinations like Canada and USD are now possible.
* Price lists can be created, allowing you to set fixed prices and percentage adjustments for the primary market.

### [Anchor to Automatic free shipping discount](/docs/api/release-notes/previous-versions/2023-10#automatic-free-shipping-discount)Automatic free shipping discount

You can now offer automatic free shipping discounts using the [`discountAutomaticFreeshippingUpdate`](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate) and [`discountAutomaticFreeshippingCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate) mutations.

### [Anchor to New webhook topic added for publication delete events](/docs/api/release-notes/previous-versions/2023-10#new-webhook-topic-added-for-publication-delete-events)New webhook topic added for publication delete events

As of API version 2023-10, a new webhook topic `PUBLICATIONS_DELETE` is added. This webhook fires whenever a publication is deleted and requires the `read_publications` scope.

### [Anchor to New ,[object Object], field on the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-10#new-customeraccountsv2-field-on-the-shop-object)New `CustomerAccountsV2` field on the `Shop` object

As of API version 2023-10, you can query the [`CustomerAccountsV2`](/docs/api/admin-graphql/latest/objects/Shop#field-shop-customeraccountsv2) field on the `Shop` object to get information about the shop's customer accounts settings. `CustomerAccountsV2` enables you to adapt your app's behaviour to a merchant's customer accounts settings.

Learn more about [`CustomerAccountsV2`](/docs/api/admin-graphql/latest/objects/CustomerAccountsV2).

### [Anchor to averageOrderAmount fields removed from the Customer object](/docs/api/release-notes/previous-versions/2023-10#averageorderamount-fields-removed-from-the-customer-object)averageOrderAmount fields removed from the Customer object

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, the following `Customer` fields have been deprecated:

* `averageOrderAmount`
* `averageOrderAmountV2`.

  Learn more about the [`Customer`](/docs/api/admin-graphql/latest/objects/Customer) object.

### [Anchor to [object Object], available on ,[object Object]](/docs/api/release-notes/previous-versions/2023-10#url-available-on-mediaimageoriginalsource)`url` available on `MediaImage.originalSource`

As of API version 2023-10, the `url` field is available on the `MediaImage` object's [`originalSource`](/docs/api/admin-graphql/latest/objects/mediaimage#field-mediaimage-originalsource) field.

This will be a signed URL that's valid only for a short period of time. The URL provides access to the uncompressed image that was originally uploaded.

### [Anchor to Fulfillment constraints built on Shopify Functions](/docs/api/release-notes/previous-versions/2023-10#fulfillment-constraints-built-on-shopify-functions)Fulfillment constraints built on Shopify Functions

As of API version 2023-10, you can use the Fulfillment Constraints API for a higher degree of customization when you defined fulfillment and delivery strategies. With this API, checkout won’t return any shipping rates if the configured constraints can’t be met.

For example, you can specify that certain products must be fulfilled from a specific location, based on buyer information, cart information, or metafields.

Learn more about [Fulfillment constraints](/docs/api/functions/reference/fulfillment-constraints).

### [Anchor to Apps can now change the name and address of their fulfillment service locations](/docs/api/release-notes/previous-versions/2023-10#apps-can-now-change-the-name-and-address-of-their-fulfillment-service-locations)Apps can now change the name and address of their fulfillment service locations

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, apps can change the name and address of their fulfillment service locations using the [`LocationEdit`](/docs/api/admin-graphql/latest/mutations/locationedit) mutation.

When a fulfillment service is created, Shopify also creates a new location and associates this with the new fulfillment service. The location inherits its name from the fulfillment service.

Apps can now update the name and address of this location. For example, when a fulfillment service is created, it inherits the country of the shop. If the fulfillment service is located in a different country from the shop, then apps can update the location to accurately reflect the fulfillment service's address.

### [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2023-10#breaking-changes)Breaking changes

#### [Anchor to New user error when editing locations](/docs/api/release-notes/previous-versions/2023-10#new-user-error-when-editing-locations)New user error when editing locations

The `LocationEdit` mutation will return a new user error with the `CANNOT_MODIFY_ONLINE_ORDER_FULFILLMENT_FOR_FS_LOCATION` code when you try to update the `fulfillsOnlineOrders` field for a fulfillment service location. This field can only be modified on manual locations. Fulfillment service locations are always enabled to fulfill online orders.

#### [Anchor to New authorization check when attempting to edit a fulfillment service location](/docs/api/release-notes/previous-versions/2023-10#new-authorization-check-when-attempting-to-edit-a-fulfillment-service-location)New authorization check when attempting to edit a fulfillment service location

In API version 2023-10, attempting to edit the location belonging to a fulfillment service without having the `write_fulfillments` access scope returns the following access denied error:

Note

Access denied for locationEdit field. Required access: `write_fulfillments` access scope is required to edit the location associated with a fulfillment service.

**Note:**

Access denied for locationEdit field. Required access: `write_fulfillments` access scope is required to edit the location associated with a fulfillment service.

Earlier API versions returned a user error with the `NOT_FOUND` code.

### [Anchor to Breaking changes to ShopResourceLimits API: Deprecate "skuResourceLimits"](/docs/api/release-notes/previous-versions/2023-10#breaking-changes-to-shopresourcelimits-api-deprecate-skuresourcelimits)Breaking changes to ShopResourceLimits API: Deprecate "skuResourceLimits"

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of GraphQL Admin API version 2023-10, we're deprecating the "skuResourceLimits" field from the `ShopResourceLimits` query object. We're no longer enforcing a limit of SKUs at a shop level. Instead, please use "maxProductVariants" to determine the limit of variants at a product level.

Learn more about [`ShopResourceLimits`](/docs/api/admin-graphql/latest/objects/ShopResourceLimits).

### [Anchor to Access input type changed on ,[object Object], mutation](/docs/api/release-notes/previous-versions/2023-10#access-input-type-changed-on-metafielddefinitionupdate-mutation)Access input type changed on `metafieldDefinitionUpdate` mutation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, we're changing the input field type of `MetafieldDefinitionUpdateInput.access` from `MetafieldAccessInput` to `MetafieldAccessUpdateInput`. This change is part of a broader API change to introduce support for explicit access grants.

Note

This change affects a small number of apps. You aren't likely affected unless you're defining a variable of type `MetafieldAccessInput` for the access property in a `MetafieldDefinitionUpdate` mutation.

**Note:**

This change affects a small number of apps. You aren't likely affected unless you're defining a variable of type `MetafieldAccessInput` for the access property in a `MetafieldDefinitionUpdate` mutation.

### [Anchor to Simplify metafield interaction with default namespaces](/docs/api/release-notes/previous-versions/2023-10#simplify-metafield-interaction-with-default-namespaces)Simplify metafield interaction with default namespaces

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, the GraphQL Admin and Storefront APIs have made the namespace field optional when creating, updating, or querying metafields and metafield definitions. We've updated all relevant mutations and queries to accommodate this change.

Learn more about the [GraphQL Admin API](/docs/api/admin-graphql/latest/queries/metafield) and [Storefront API](/docs/api/storefront) documentation for Metafields.

### [Anchor to Deprecation of ,[object Object], query](/docs/api/release-notes/previous-versions/2023-10#deprecation-of-metafieldid-query)Deprecation of `metafield(id)` query

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, the `metafield(id)` query is no longer supported. Metafields should be queried using the `HasMetafields` connection of metafield owners. If necessary, metafields can be queried by ID using the `Node` interface.

### [Anchor to Renderable and online store capabilities for metaobjects](/docs/api/release-notes/previous-versions/2023-10#renderable-and-online-store-capabilities-for-metaobjects)Renderable and online store capabilities for metaobjects

As of API version 2023-10, we're introducing new metaobject capabilities to enable SEO attributes and make entries renderable in the online store. These capabilities make it possible to render landing pages from metaobject entries.

Both capabilities can be enabled and configured independently when creating and updating a metaobject definition.

### [Anchor to Multiple domains on primary markets](/docs/api/release-notes/previous-versions/2023-10#multiple-domains-on-primary-markets)Multiple domains on primary markets

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, you can have multiple domains on the primary market. The following changes have been introduced to the Markets API:

* New `Market.webPresences` connection has been added
* Pre-existing `Market.webPresence` field will return the primary domain web presence for a primary market with multiple web presences
* `marketWebPresenceCreate` mutation will now allow adding additional web presences to the primary market
* The required `marketId` argument has been removed from the `marketWebPresenceUpdate` and `marketWebPresenceDelete` mutations. The new required `webPresenceId` argument should be used instead

### [Anchor to Staff error as an order cancel reason](/docs/api/release-notes/previous-versions/2023-10#staff-error-as-an-order-cancel-reason)Staff error as an order cancel reason

As of 2023-10, we have added `STAFF` to the `OrderCancelReason` GraphQL type to serve as a reason for canceling orders due to staff errors.

### [Anchor to New field to query order cancellations](/docs/api/release-notes/previous-versions/2023-10#new-field-to-query-order-cancellations)New field to query order cancellations

As of 2023-10, we've added a new field `cancellation` to `Order` graphQL object. This field can provide additional details about the order cancellation, such as staff provided notes on why the order was cancelled. This data is currently available for some orders cancelled on Point of Sale app.

### [Anchor to Order Routing Location Rule API — Developer Preview](/docs/api/release-notes/previous-versions/2023-10#order-routing-location-rule-api--developer-preview)Order Routing Location Rule API — Developer Preview

The Order Routing Location Rule API is now available in a developer preview. You can use this new Shopify Functions API to write custom order routing rules that determine how to best fulfill and ship orders, based on the needs of the merchant.

### [Anchor to New compare-at price range field on Product API](/docs/api/release-notes/previous-versions/2023-10#new-compare-at-price-range-field-on-product-api)New compare-at price range field on Product API

As of version 2023-10 of the GrapqhQL Admin API, we've added the `compareAtPriceRange` field to `Product` which will return the minimum and maximum compare-at prices across a product's variants.

### [Anchor to Manage Quantity Price Breaks for B2B Customers](/docs/api/release-notes/previous-versions/2023-10#manage-quantity-price-breaks-for-b2b-customers)Manage Quantity Price Breaks for B2B Customers

As of the `2023-10` version of the Admin GraphQL API, you can view the `quantityPriceBreaks` for a product variant on `priceListPrice` and `productVariantContextualPricing`. Additionally, you will be able to use the `quantityPricingByVariantUpdate` mutation to manage quantity price breaks, quantity rules, and fixed prices for multiple variants.

### [Anchor to App Revenue Attribution Record API Depreciated](/docs/api/release-notes/previous-versions/2023-10#app-revenue-attribution-record-api-depreciated)App Revenue Attribution Record API Depreciated

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of **October 2023**, the App Revenue Attribution API has been removed.

`appRevenueAttributionRecordCreate` and `appRevenueAttributionRecordDelete` are no longer supported in this and future API versions.

This change removes tracking for external app revenue attributions that occur outside of the Billing API. Partners can now use [Google Analytics to track Shopify App Store Ads installs](https://www.shopify.com/partners/blog/google-analytics-app-install-event) - which can be linked to external app revenue to calculate ad related return on ad spend and other ads related metrics.

### [Anchor to Removing ,[object Object], on Admin API](/docs/api/release-notes/previous-versions/2023-10#removing-shopshopifypaymentsaccount-on-admin-api)Removing `Shop.shopifyPaymentsAccount` on Admin API

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of `2023-10`, we're removing the deprecated `Shop.shopifyPaymentsAccount` field. Use the [shopifyPaymentsAccount](https://shopify.dev/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount) query instead.

### [Anchor to Shopify Protect protection status on Admin API](/docs/api/release-notes/previous-versions/2023-10#shopify-protect-protection-status-on-admin-api)Shopify Protect protection status on Admin API

As of the latest `unstable` version and upcoming `2023-10` version of the Admin GraphQL API, you can use the `shopifyProtect` field of `Order` to view the protection status of Shop Pay orders. The protection status is established asynchronously from the `orders/create` webhook so you can also listen to the `orders/shopify_protect_eligibility_changed` webhook to know when the protection status is created or updated.

By providing a clear view of an order’s protection status, we're empowering developers to make more informed decisions. For instance, fraud protection apps can avoid redundant costs for merchants when a Shop Pay order is already protected.

Learn more about Shopify Protect’s protection status on [Shopify.dev](https://shopify.dev/docs/api/admin-graphql/unstable/objects/Order#field-order-shopifyprotect).

### [Anchor to Changes to subscription billing attempt creation behavior](/docs/api/release-notes/previous-versions/2023-10#changes-to-subscription-billing-attempt-creation-behavior)Changes to subscription billing attempt creation behavior

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

The [`SubscriptionBillingAttemptCreate`](/docs/api/admin-graphql/latest/mutations/subscriptionBillingAttemptCreate) mutation now limits the creation of billing attempts based on the [fraud analysis](https://help.shopify.com/en/manual/orders/fraud-analysis) result on the subscription contract’s [origin order](/docs/api/admin-graphql/latest/objects/SubscriptionContract#field-subscriptioncontract-originorder).

As of API version 2023-10, we've added the `CONTRACT_UNDER_REVIEW` error code to the `BillingAttemptUserErrorCode` enum. This new error code is returned in the case where Billing Attempt creation is prevented. In previous API versions, this action will return the `INVALID` error code.

Learn more about [subscription contracts and billing attempts](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

---

## [Anchor to GraphQL Storefront API changes](/docs/api/release-notes/previous-versions/2023-10#graphql-storefront-api-changes)GraphQL Storefront API changes

### [Anchor to Simplify metafield interaction with default namespaces](/docs/api/release-notes/previous-versions/2023-10#simplify-metafield-interaction-with-default-namespaces)Simplify metafield interaction with default namespaces

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, the GraphQL Admin and Storefront APIs have made the namespace field optional when creating, updating, or querying metafields and metafield definitions. We've updated all relevant mutations and queries to accommodate this change. When an app interacts with metafields, the default namespace is the [app-reserved namespace](/docs/apps/build/custom-data/ownership#reserved-prefixes).

This update does not affect API calls that explicitly specify a namespace. However, it simplifies the process of interacting with namespaces by removing the need to provide a namespace field when the default is suitable. As a result, Apps can now create and query Metafields without the requirement of specifying a namespace.

Learn more in the [Admin API](https://shopify.dev/docs/api/admin-graphql/latest/queries/metafield) and [Storefront API](https://shopify.dev/docs/api/storefront) documentation for Metafields.

### [Anchor to Renderable and Online Store capabilities for metaobjects](/docs/api/release-notes/previous-versions/2023-10#renderable-and-online-store-capabilities-for-metaobjects)Renderable and Online Store capabilities for metaobjects

As of API version 2023-10, we're introducing new metaobject capabilities to enable SEO attributes and make entries renderable in the online store. These capabilities make it possible to render landing pages from metaobject entries.

The renderable capability enables setting SEO metadata attributes on your metaobjects. These attributes are accessible in Liquid and via the Storefront API.

The Online Store capability makes your metaobjects render as web pages in the Online Store by assigning a theme template and defining a URL.

Both capabilities can be enabled and configured independently when creating and updating a metaobject definition.

Learn more about the `renderable` and `onlineStore` capabilities on [Shopify.dev](https://shopify.dev/docs/apps/custom-data/metaobjects/capabilities)

### [Anchor to Staff error as Order cancel reason](/docs/api/release-notes/previous-versions/2023-10#staff-error-as-order-cancel-reason)Staff error as Order cancel reason

As of 2023-10, we have added `STAFF` to the `OrderCancelReason` GraphQL type to serve as a reason for canceling orders due to staff errors.

Learn more about `OrderCancelReason` on [Shopify.dev](https://shopify.dev/docs/api/admin-graphql/latest/enums/OrderCancelReason).

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2023-10#rest-admin-api-changes)REST Admin API changes

### [Anchor to Removal of UsageCharge billing\_on field on Admin REST API](/docs/api/release-notes/previous-versions/2023-10#removal-of-usagecharge-billing_on-field-on-admin-rest-api)Removal of UsageCharge billing\_on field on Admin REST API

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-10#breaking)Breaking

As of API version 2023-10, the `UsageCharge` resource's `billing_on` property is deprecated.

Learn more about the [`UsageCharge`](/docs/api/admin-rest/latest/resources/usagecharge) resource.

### [Anchor to Staff error as an order cancel reason](/docs/api/release-notes/previous-versions/2023-10#staff-error-as-an-order-cancel-reason)Staff error as an order cancel reason

As of API version 2023-10, we've added `STAFF` to the `OrderCancelReason` GraphQL type to serve as a reason for canceling orders due to staff errors.

Learn more about [`OrderCancelReason`](/docs/api/admin-graphql/latest/OrderCancelReason).

---

Was this page helpful?

YesNo