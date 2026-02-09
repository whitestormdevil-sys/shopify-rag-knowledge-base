---
source: https://shopify.dev/docs/api/release-notes/2023-04
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| April 1, 2023 | April 1, 2024 |

**What's new in 2023-04**

The following features were added in version 2023-04 of Shopify's APIs.

Highlights from the GraphQL Admin API changes:

* Metafield values can now be set for Locations
* Move and Hold mutations for FulfillmentOrders now accept specific line items
* Subscription contracts can now be created in a single operation
* Customer profiles can now be combined using the Merge API
* Functions APIs are now available for delivery and payment customizations
* Catalog APIs are now available
* Webhooks for B2B Customers have been added
* Metafield definition validations can now be updated

  Highlights from the GraphQL Storefront API changes:
* Metafields on Locations can now be queried
* Targeted product recommendations can now be generated
* Catalog APIs are now available
* A buyer's wallet preference can now be passed to the Cart
* Customer address IDs can now be used as input for delivery address preferences

  Highlights from the GraphQL Payments Apps API changes:
* The status field in the Payments Apps API has been removed.
* The previously deprecated `status` field has been removed from session-related objects.

  Highlights from the REST Admin API changes:
* Move and Hold operations for `FulfillmentOrders` now accept specific line items
* Additional filtering has been added to `FulfillmentOrders`

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2023-04#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Metaobjects can now be Translatable](/docs/api/release-notes/previous-versions/2023-04#metaobjects-can-now-be-translatable)Metaobjects can now be Translatable

[Metaobjects](/docs/apps/build/custom-data/metaobjects) can now be enabled with the [Translatable](/docs/apps/build/custom-data/metaobjects/use-metaobject-capabilities#make-your-metaobjects-translatable) capability.

### [Anchor to Changed access scope for publishing and unpublishing to current channel objects](/docs/api/release-notes/previous-versions/2023-04#changed-access-scope-for-publishing-and-unpublishing-to-current-channel-objects)Changed access scope for publishing and unpublishing to current channel objects

Calling the [`publishableUnpublishToCurrentChannel`](/docs/api/admin-graphql/2023-04/mutations/publishableUnpublishToCurrentChannel) and [`publishablePublishToCurrentChannel`](/docs/api/admin-graphql/2023-04/mutations/publishablePublishToCurrentChannel) mutations now requires the `writepublications` [access scope](/docs/api/usage/access-scopes), instead of the `writeproductslistings` access scope, which has been deprecated.

### [Anchor to The ,[object Object], access scope has been deprecated](/docs/api/release-notes/previous-versions/2023-04#the-writeproductslistings-access-scope-has-been-deprecated)The `writeproductslistings` access scope has been deprecated

The `writeproductslistings` [access scope](/docs/api/usage/access-scopes) has been deprecated. Use `writepublications` instead.

### [Anchor to The ,[object Object], field on ,[object Object], has been removed](/docs/api/release-notes/previous-versions/2023-04#the-contextrule-field-on-pricelist-has-been-removed)The `contextRule` field on `PriceList` has been removed

The `contextRule` field on [`PriceList`](/docs/api/admin-graphql/2023-04/objects/PriceList) has been removed. Existing apps should migrate to [`Catalogs`](/docs/apps/build/markets/catalogs-different-markets). Check out our [`migration guide`](/docs/apps/build/markets/migrate-to-catalogs) for more information.

### [Anchor to The ShopifyQL parse error codes have been updated](/docs/api/release-notes/previous-versions/2023-04#the-shopifyql-parse-error-codes-have-been-updated)The ShopifyQL parse error codes have been updated

The ['ParseErrorCode'](/docs/api/admin-graphql/2023-04/enums/ParseErrorCode) values have been updated. Refer to the following list of codes for more details:

### [Anchor to [object Object], codes have been updated](/docs/api/release-notes/previous-versions/2023-04#fulfillmentorderlineitemspreparedforpickupusererrorcode-codes-have-been-updated)`FulfillmentOrderLineItemsPreparedForPickupUserErrorCode` codes have been updated

The [`FulfillmentOrderLineItemsPreparedForPickupUserErrorCode`](/docs/api/admin-graphql/2023-04/enums/FulfillmentOrderLineItemsPreparedForPickupUserErrorCode) object has the following changes:

* The `FULFILLMENT_ORDER_CHANGED` error code has been removed
* The `UNABLE_TO_PREPARE_QUANTITY` error code has been added

### [Anchor to [object Object], has been replaced](/docs/api/release-notes/previous-versions/2023-04#publishedtranslation-has-been-replaced)`PublishedTranslation` has been replaced

The [`PublishedTranslation`](/docs/api/admin-graphql/2023-01/objects/PublishedTranslation) object has been replaced by [`Translation`](/docs/api/admin-graphql/2023-04/objects/Translation). All existing connections to `PublishedTranslation` now point to `Translation`. All existing fields on `PublishedTranslation` exist on `Translation`, except for the `marketId` field. Instead, `Translation` is linked directly to [`Market`](/docs/api/admin-graphql/2023-04/objects/Market) through the `market` field.

### [Anchor to Introducing ,[object Object]](/docs/api/release-notes/previous-versions/2023-04#introducing-basecartline)Introducing `BaseCartLine`

We have introduced [`BaseCartLine`](/docs/api/storefront/2023-04/interfaces/BaseCartLine) as an interface to [`CartLine`](/docs/api/storefront/2023-04/objects/CartLine). [`CartLineConnection`](/docs/api/storefront/2023-01/connections/CartLineConnection) has been updated to [`BaseCartLineConnection`](/docs/api/storefront/2023-04/connections/BaseCartLineConnection).

### [Anchor to The ,[object Object], field in the Payments Apps API has been removed](/docs/api/release-notes/previous-versions/2023-04#the-status-field-in-the-payments-apps-api-has-been-removed)The `status` field in the Payments Apps API has been removed

The previously deprecated `status` field has been removed in favour of the `state` field on the following Payments Apps API objects:

* [`PaymentSession`](/docs/api/payments-apps/2023-04/objects/PaymentSession)
* [`RefundSession`](/docs/api/payments-apps/2023-04/objects/RefundSession)
* [`CaptureSession`](/docs/api/payments-apps/2023-04/objects/CaptureSession)
* [`VoidSession`](/docs/api/payments-apps/2023-04/objects/VoidSession)

### [Anchor to New error codes in ,[object Object], enum](/docs/api/release-notes/previous-versions/2023-04#new-error-codes-in-carterrorcodes-enum)New error codes in `CartErrorCodes` enum

Two new error codes, `INVALID_DELIVERY_GROUP` and `INVALID_DELIVERY_OPTION`, have been added to the [`CartErrorCode`](/docs/api/storefront/2023-04/enums/CartErrorCode) enum.

### [Anchor to [object Object], in the REST API will now return the total unsettled set amount](/docs/api/release-notes/previous-versions/2023-04#transaction-in-the-rest-api-will-now-return-the-total-unsettled-set-amount)`Transaction` in the REST API will now return the total unsettled set amount

Requests for [Transaction](/docs/api/admin-rest/2023-04/resources/transaction) will now return `total_unsettled_set`. This represents the remaining amount to be captured on the transaction. `total_unsettled_set` is returned in both `shop` and `presentment` money objects with currency.

### [Anchor to Access to the Asset API is no longer available to public apps](/docs/api/release-notes/previous-versions/2023-04#access-to-the-asset-api-is-no-longer-available-to-public-apps)Access to the Asset API is no longer available to public apps

When requesting the Asset API, access to create, update and delete assets is no longer accessible for public apps. Refer to [this guide](/docs/apps/build/online-store/asset-legacy) for more details on the change, exemptions and how to migrate your apps.

### [Anchor to Payment properties on the ,[object Object], resource have been removed](/docs/api/release-notes/previous-versions/2023-04#payment-properties-on-the-order-resource-have-been-removed)Payment properties on the `Order` resource have been removed

The following properties have been removed from the [`Order`](/docs/api/admin-rest/2023-04/resources/order) resource:

* `gateway`
* `payment_details`
* `processing_method`

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2023-04#graphql-admin-api-changes)GraphQL Admin API changes

The following are all the changes currently introduced in the 2023-04 version of the GraphQL Admin API.

### [Anchor to The inventoryItemId field has been added to FulfillmentOrderLineItem](/docs/api/release-notes/previous-versions/2023-04#the-inventoryitemid-field-has-been-added-to-fulfillmentorderlineitem)The inventoryItemId field has been added to FulfillmentOrderLineItem

The `inventoryItemId` field can now be accessed from the [FulfillmentOrderLineItem](/docs/api/admin-graphql/2023-04/objects/FulfillmentOrderLineItem) resource.

### [Anchor to Functions APIs have been added in developer preview for delivery and payment customizations](/docs/api/release-notes/previous-versions/2023-04#functions-apis-have-been-added-in-developer-preview-for-delivery-and-payment-customizations)Functions APIs have been added in developer preview for delivery and payment customizations

The Functions APIs for delivery customizations and payment customizations are now available in a developer preview.

With these new APIs, you can hide, reorder, or rename payment and delivery options to help merchants increase conversions and stand out from the competition.

Learn more about building with delivery and payment Functions in our dev docs:

* [Delivery customization](/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)
* [Payment customization](/docs/apps/build/checkout/payments)

### [Anchor to Metafield values can now be set for Locations](/docs/api/release-notes/previous-versions/2023-04#metafield-values-can-now-be-set-for-locations)Metafield values can now be set for Locations

[Metafield](/docs/api/admin-graphql/2023-04/objects/Metafield) values can now be set for Locations via the [`locationAdd`](/docs/api/admin-graphql/2023-04/mutations/locationAdd) and [`locationEdit`](/docs/api/admin-graphql/2023-04/mutations/locationEdit) mutations.

### [Anchor to Metaobjects can now be translated](/docs/api/release-notes/previous-versions/2023-04#metaobjects-can-now-be-translated)Metaobjects can now be translated

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

[Metaobjects](/docs/apps/build/custom-data/metaobjects) can now be enabled with the [Translatable](/docs/apps/build/custom-data/metaobjects/use-metaobject-capabilities#make-your-metaobjects-translatable) capability. When enabled, all Metaobjects belonging to the definition are eligible for translations through the [Translations API](/docs/apps/build/markets/manage-translated-content) as well as the [Translate and Adapt](/docs/apps.shopify.com/translate-and-adapt) app.

### [Anchor to Access Scope has changed for publishing and unpublishing to current channel](/docs/api/release-notes/previous-versions/2023-04#access-scope-has-changed-for-publishing-and-unpublishing-to-current-channel)Access Scope has changed for publishing and unpublishing to current channel

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

Calling the [`publishableUnpublishToCurrentChannel`](/docs/api/admin-graphql/2023-01/mutations/publishableUnpublishToCurrentChannel) and [`publishablePublishToCurrentChannel`](/docs/api/admin-graphql/2023-01/mutations/publishablePublishToCurrentChannel) mutations now requires the `writepublications` [access scope](/docs/api/usage/access-scopes), instead of the `writeproductslistings` access scope, which has been deprecated.

### [Anchor to Check if a Shop is verified by Shopify tiers](/docs/api/release-notes/previous-versions/2023-04#check-if-a-shop-is-verified-by-shopify-tiers)Check if a Shop is verified by Shopify tiers

The [`MerchantApprovedSignals`](/docs/api/admin-graphql/2023-04/objects/MerchantApprovalSignals) object, which is a field on the [`Shop`](/docs/api/admin-graphql/2023-04/objects/Shop#field-shop-merchantapprovalsignals) object, has a new `verifiedByShopifyTier` field that determines what tier of pre-approval a merchant is in, if available.

### [Anchor to Move and Hold mutations for FulfillmentOrders now accept specific line items](/docs/api/release-notes/previous-versions/2023-04#move-and-hold-mutations-for-fulfillmentorders-now-accept-specific-line-items)Move and Hold mutations for FulfillmentOrders now accept specific line items

The [`fulfillmentOrderMove`](/docs/api/admin-graphql/2023-04/mutations/fulfillmentOrderMove) and [`fulfillmentOrderHold`](/docs/api/admin-graphql/2023-04/mutations/fulfillmentOrderHold) mutations have a new and optional `fulfillment_order_line_items` parameter that enables you to specify the line items you wish to hold or move.

### [Anchor to Orders can be filtered by return status](/docs/api/release-notes/previous-versions/2023-04#orders-can-be-filtered-by-return-status)Orders can be filtered by return status

The [`return_status` filter](/docs/api/admin-graphql/2023-04/queries/orders#:~:text=reference_location_id-,return_status,-risk_level) is available on the orders connection. This status corresponds to the [return status](/docs/api/admin-graphql/2023-04/enums/OrderReturnStatus) that merchants see in the **Orders** page in the Shopify admin.

For more information on Order status, check out [the help center](https://help.shopify.com/en/manual/orders/order-status).

### [Anchor to Create subscription contracts in a single operation](/docs/api/release-notes/previous-versions/2023-04#create-subscription-contracts-in-a-single-operation)Create subscription contracts in a single operation

You can now create subcription contracts in a single operation with the new [`subscriptionContractAtomicCreate`](/docs/api/admin-graphql/2023-04/mutations/subscriptionContractAtomicCreate) mutation. You can also replace a product, or update the price of a product in a subscription contract using the [`subscriptonContractProductUpdate`](/docs/api/admin-graphql/2023-04/mutations/subscriptionContractUpdate) mutation.

### [Anchor to The contextRule field on PriceList has been removed](/docs/api/release-notes/previous-versions/2023-04#the-contextrule-field-on-pricelist-has-been-removed)The contextRule field on PriceList has been removed

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The `contextRule` field on [`PriceList`](/docs/api/admin-graphql/2023-04/objects/PriceList) has been removed and deprecated in previous versions of the API. Existing apps should migrate to [`Catalogs`](/docs/apps/build/markets/catalogs-different-markets). Check out our [migration guide](/docs/apps/build/markets/migrate-to-catalogs) for more information.

### [Anchor to ShopifyQL parse error codes have been updated](/docs/api/release-notes/previous-versions/2023-04#shopifyql-parse-error-codes-have-been-updated)ShopifyQL parse error codes have been updated

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The [`ParseErrorCode`](/docs/api/admin-graphql/2023-04/enums/ParseErrorCode) values have been updated according to the following list:

**Added**

* `INVALID_DATE_RANGE`
* `EXCESS_BACKFILL_DIMENSIONS`
* `BACKFILL_DATE_RANGE_NOT_FOUND`
* `COMPARE_TO_MISSING_PERIOD`
* `EXCESS_DIMENSIONS`
* `SYNTAX_FAILED_PREDICATE`

  **Removed**
* `VISUALIZE_TYPE_NOT_FOUND`
* `FUNCTION_MODIFIER_INVALID`
* `VISUALIZE_BY_OR_OVER_NOT_FOUND`
* `VISUALIZE_CONTAINS_BY_AND_OVER`
* `BINARY_EXPRESSION_INCOMPATIBLE_TYPES`
* `VISUALIZE_EXCESS_PROJECTIONS_ALPHA`
* `EXCESS_GROUP_BY_ALL`
* `GROUP_BY_ALL_DATE_RANGE_NOT_FOUND`
* `COMPARE_TO_WITHOUT_DURING`
* `GROUP_BY_EXCESS_PROJECTIONS`

### [Anchor to Combine customer profiles with the Merge API](/docs/api/release-notes/previous-versions/2023-04#combine-customer-profiles-with-the-merge-api)Combine customer profiles with the Merge API

Use the new Customer Merge API to combine two separate [`Customer`](/docs/api/admin-graphql/2023-04/objects/Customer) records. You can use the new queries and mutations below to preview a merge, initiate a merge, and check the status of an ongoing merge.

**New queries**

* [`customerMergePreview`](/docs/api/admin-graphql/2023-04/queries/customerMergePreview)
* [`customerMergeJobStatus`](/docs/api/admin-graphql/2023-04/queries/customerMergeJobStatus)

  **New mutations**
* [`customerMerge`](/docs/api/admin-graphql/2023-04/mutations/customerMerge)

  Additionally, you can check whether a customer can be merged with another customer using the new [`Customer.mergeable`](/docs/api/admin-graphql/2023-04/objects/Customer#field-customer-mergeable) field. This field is also available on the [CustomerSegmentMember API](/docs/api/admin-graphql/2023-04/objects/CustomerSegmentMember#field-customersegmentmember-mergeable)

### [Anchor to Create app charges using the merchant's billing currency](/docs/api/release-notes/previous-versions/2023-04#create-app-charges-using-the-merchants-billing-currency)Create app charges using the merchant's billing currency

The Billing API now enables you to create app charges using currencies that match the [merchant's local billing currency](https://help.shopify.com/en/manual/your-account/manage-billing/your-invoice/local-currency#countries-and-regions-where-local-currency-billing-is-supported).

### [Anchor to Functions APIs are now available for delivery and payment customizations](/docs/api/release-notes/previous-versions/2023-04#functions-apis-are-now-available-for-delivery-and-payment-customizations)Functions APIs are now available for delivery and payment customizations

The Functions APIs for [`delivery customizations`](/docs/api/functions/reference/delivery-customization) and [`payment customizations`](/docs/api/functions/reference/payment-customization) are now available in a [developer preview](/docs/api/developer-previews). With these new APIs, you can hide, reorder, or rename payment and delivery options to help merchants increase conversions and stand out from the competition.

### [Anchor to Catalog APIs are now available](/docs/api/release-notes/previous-versions/2023-04#catalog-apis-are-now-available)Catalog APIs are now available

You can use the new [`Catalogs API`](/docs/apps/build/b2b/manage-catalogs) to create a set of rules that determine the available products and their prices in different customer contexts. The Catalogs API lets you link Shopify Markets and B2B primitives to Publications and PriceLists to customize product offerings for different audiences. The same APIs also allow you to manage product publishing for sales channels.

Previously, app charges could only be created using USD and were converted to the merchant's local currency using the exchange rate at the time the invoice is issued. By creating app charges in the merchant's billing currency, app developers can enable merchants to better budget their app spend without being exposed to currency exchange rate fluctuations.

You can use the [`shopBillingPreferences`](/docs/api/admin-graphql/2023-04/queries/shopBillingPreferences) query to retrieve the merchant's local billing currency, then pass in the currency value as input to the existing GraphQL Billing APIs.

### [Anchor to Web Pixels can now be queried without specifying an ID](/docs/api/release-notes/previous-versions/2023-04#web-pixels-can-now-be-queried-without-specifying-an-id)Web Pixels can now be queried without specifying an ID

You can now query the web pixels installed on an online store without specifying the ID using the [`webPixel`](/docs/api/admin-graphql/2023-04/queries/webPixel) query. Learn more about [web pixels](/docs/apps/build/marketing-analytics/pixels).

### [Anchor to Idempotent creation of AppUsageRecord](/docs/api/release-notes/previous-versions/2023-04#idempotent-creation-of-appusagerecord)Idempotent creation of AppUsageRecord

The [`appUsageRecordCreate`](/docs/api/admin-graphql/2023-04/mutations/appUsageRecordCreate) now supports an optional parameter `idempotencyKey`, which ensures the merchant will not be charged twice. When `idempotencyKey` is provided, the mutation will return the same response as any previous `appUsageRecordCreate` mutation calls with an identical `idempotencyKey` value for the intended shop and requesting app, rather than creating a new record and charging the merchant again.

This means that an `idempotencyKey` could be reused by an app to create [`AppUsageRecords`](/docs/api/admin-graphql/2023-04/objects/AppUsageRecord) on different shops to charge the merchant. Different apps can also use the same `idempotencyKey` on the same shop and still charge the shop. However, we recommend a UUID instead.

The `appUsageRecordCreate` mutation behaves like past API versions when the `idempotencyKey` value is not provided and creates a new record on every call.

### [Anchor to SVG files are now returned as a MediaImage](/docs/api/release-notes/previous-versions/2023-04#svg-files-are-now-returned-as-a-mediaimage)SVG files are now returned as a MediaImage

SVG files are now treated as MediaImages by the Admin API. This makes it easier to use SVGs in your online storefront.

### [Anchor to The productVariantsBulkUpdate mutation now returns data along with errors](/docs/api/release-notes/previous-versions/2023-04#the-productvariantsbulkupdate-mutation-now-returns-data-along-with-errors)The productVariantsBulkUpdate mutation now returns data along with errors

The [`productVariantsBulkUpdate`](/docs/api/admin-graphql/2023-04/mutations/productvariantsbulkupdate) mutation will now return [`Product`](/docs/api/admin-graphql/2023-04/objects/Product) and [`ProductVariant`](/docs/api/admin-graphql/2023-04/objects/ProductVariant) data even when errors are present. Previously, the mutation would always return `null` for the `Product` and `ProductVariant` data.

### [Anchor to PublishedTranslation has been replaced by Translation](/docs/api/release-notes/previous-versions/2023-04#publishedtranslation-has-been-replaced-by-translation)PublishedTranslation has been replaced by Translation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The [`PublishedTranslation`](/docs/api/admin-graphql/2023-01/objects/PublishedTranslation) object has been replaced by [`Translation`](/docs/api/admin-graphql/2023-04/objects/Translation). All existing connections to `PublishedTranslation` now point to `Translation`. All existing fields on `PublishedTranslation` exist on `Translation`, except for the `marketId` field. Instead, `Translation` is linked directly to [`Market`](/docs/api/admin-graphql/2023-04/objects/Market) through the `market` field.

### [Anchor to FulfillmentOrderLineItemsPreparedForPickupUserErrorCode codes have been updated](/docs/api/release-notes/previous-versions/2023-04#fulfillmentorderlineitemspreparedforpickupusererrorcode-codes-have-been-updated)FulfillmentOrderLineItemsPreparedForPickupUserErrorCode codes have been updated

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The [`FulfillmentOrderLineItemsPreparedForPickupUserErrorCode`](/docs/api/admin-graphql/2023-01/enums/FulfillmentOrderLineItemsPreparedForPickupUserErrorCode) object has the following changes:

* The `FULFILLMENT_ORDER_CHANGED` error code has been removed
* The `UNABLE_TO_PREPARE_QUANTITY` error code has been added

### [Anchor to Webhooks for B2B Customers have been added](/docs/api/release-notes/previous-versions/2023-04#webhooks-for-b2b-customers-have-been-added)Webhooks for B2B Customers have been added

The following webhook notifications for changes to the major entities within the B2B Customers product have been added:

* [`companies/create`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiescreate)
* [`companies/update`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiesupdate)
* [`companies/delete`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiesdelete)
* [`company_locations/create`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companylocationscreate)
* [`company_locations/update`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companieslocationsupdate)
* [`company_locations/delete`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companieslocationsdelete)
* [`company_contacts/create`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiescontractscreate)
* [`company_contacts/update`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiescontractsupdate)
* [`company_contacts/delete`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-companiescontractsdelete)

### [Anchor to Destroy delegate access tokens](/docs/api/release-notes/previous-versions/2023-04#destroy-delegate-access-tokens)Destroy delegate access tokens

You can use the [`delegateAccessTokenDestroy`](/docs/api/admin-graphql/2023-04/mutations/delegateAccessTokenDestroy) mutation to delete the delegate tokens created by the API client. For app architectures that use delegate tokens from multiple subsystems, this makes it easy to remove those delegate tokens that are unused or leaked for better application security.

### [Anchor to Additional fees fields for Orders](/docs/api/release-notes/previous-versions/2023-04#additional-fees-fields-for-orders)Additional fees fields for Orders

The [`Order`](/docs/api/admin-graphql/2023-04/objects/Order) object has the following new fields that represent additional fees. Additional fees are extra costs associated with an international package that are neither duties nor taxes.

* `additionalFees`
* `currentTotalAdditionalFeesSet`
* `originalTotalAdditionalFeesSet`

### [Anchor to Update validations of a metafield definition](/docs/api/release-notes/previous-versions/2023-04#update-validations-of-a-metafield-definition)Update validations of a metafield definition

You can now use the new `validations` field on [`MetafieldDefinitionInput`](/docs/api/admin-graphql/2023-04/input-objects/MetafieldDefinitionInput) to change the validations for a [`Metafield`](/docs/api/admin-graphql/2023-04/objects/Metafield) definition. You can also query the `validationJob` field on [`MetafieldDefinitionUpdatePayload`](/docs/api/admin-graphql/2023-04/payloads/MetafieldDefinitionUpdatePayload) to get the details of the running validation job.

### [Anchor to Server Pixels are now available to select partners](/docs/api/release-notes/previous-versions/2023-04#server-pixels-are-now-available-to-select-partners)Server Pixels are now available to select partners

Select partners can use Server Pixels to consume customer events on the server-side. These new mutations are available to those partners:

* [`serverPixelCreate`](/docs/api/admin-graphql/2023-04/mutations/serverPixelCreate)
* [`eventBridgeServerPixelUpdate`](/docs/api/admin-graphql/2023-04/mutations/eventBridgeServerPixelUpdate)
* [`pubSubServerPixelUpdate`](/docs/api/admin-graphql/2023-04/mutations/pubSubServerPixelUpdate)
* [`serverPixelDelete`](/docs/api/admin-graphql/2023-04/mutations/serverPixelDelete)

### [Anchor to You can compare columns in ShopifyqlResponse](/docs/api/release-notes/previous-versions/2023-04#you-can-compare-columns-in-shopifyqlresponse)You can compare columns in ShopifyqlResponse

You can now use the `COMPARE TO` keyword on comparison columns in `ShopifyqlResponse` to indicate the columns to be compared. Learn more about the `COMPARE TO` keyword in our [ShopifyQL Documentation](/docs/api/shopifyql/shopifyql-reference#compare-to)

### [Anchor to Added source\_location field to FulfillmentOrdersMove webhook payload](/docs/api/release-notes/previous-versions/2023-04#added-source_location-field-to-fulfillmentordersmove-webhook-payload)Added source\_location field to FulfillmentOrdersMove webhook payload

The [`FulfillmentOrdersMove`](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic#value-fulfillmentordersmoved) webhook payload is extended `source_location` field.

The [`assignedLocation`](/docs/api/admin-graphql/2023-04/objects/fulfillmentorder#field-fulfillmentorder-assignedlocation) of the `original_fulfillment_order` may be changed by the move operation. Therefore, if you need to determine the originally assigned location, then you should refer to the `source_location` field.

### [Anchor to Partial updates for bulk product variants](/docs/api/release-notes/previous-versions/2023-04#partial-updates-for-bulk-product-variants)Partial updates for bulk product variants

The [`productVariantsBulkUpdate`](/docs/api/admin-graphql/2023-01/mutations/productVariantsBulkUpdate) mutation has a new `allowPartialUpdates` parameter. By default, the mutation won't update any variant if any variant is invalid. However, when this field is set to `true`, the mutation will modify valid products variants, even if there are invalid ones.

---

## [Anchor to GraphQL Storefront API changes](/docs/api/release-notes/previous-versions/2023-04#graphql-storefront-api-changes)GraphQL Storefront API changes

### [Anchor to Metafields on Locations can now be queried](/docs/api/release-notes/previous-versions/2023-04#metafields-on-locations-can-now-be-queried)Metafields on Locations can now be queried

[Metafields](/docs/api/storefront/2023-04/objects/Metafields) belonging to a [Location](/docs/api/storefront/2023-04/objects/Location) can now be queried using the [Location](/docs/api/storefront/2023-04/objects/Location#queries) query object.

### [Anchor to Generate targeted product recommendations](/docs/api/release-notes/previous-versions/2023-04#generate-targeted-product-recommendations)Generate targeted product recommendations

The [`productRecommendations`](/docs/api/storefront/2023-04/queries/productRecommendations) query has a new optional `intent` argument of the type [`ProductRecommendationIntent`](/docs/api/storefront/2023-04/enums/ProductRecommendationIntent). By default, the value for this argument is `RELATED`.

### [Anchor to A buyer's wallet preference can be passed to the Cart](/docs/api/release-notes/previous-versions/2023-04#a-buyers-wallet-preference-can-be-passed-to-the-cart)A buyer's wallet preference can be passed to the Cart

The new `wallet_preferences` field on the [`CartBuyerIdentity`](/docs/api/storefront/2023-04/objects/CartBuyerIdentity) object allows you to pass a buyer's wallet preference and be redirected to the accelerated checkout flow. Accepted value: `shop_pay`.

### [Anchor to Introducing BaseCartLine](/docs/api/release-notes/previous-versions/2023-04#introducing-basecartline)Introducing BaseCartLine

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

We have introduced [`BaseCartLine`](/docs/api/storefront/2023-04/interfaces/BaseCartLine) as an interface to [`CartLine`](/docs/api/storefront/2023-04/objects/CartLine). [`CartLineConnection`](/docs/api/storefront/2023-04/connections/CartLineConnection) has been updated to [`BaseCartLineConnection`](/docs/api/storefront/2023-04/connections/BaseCartLineConnection).

### [Anchor to Read 3D model configuration settings from the Storefront API](/docs/api/release-notes/previous-versions/2023-04#read-3d-model-configuration-settings-from-the-storefront-api)Read 3D model configuration settings from the Storefront API

When a 3D model is customized via the no code 3D viewer configuration the properties associated with lighting, zoom, camera angle and background color are available in the Storefront API. Learn more about this feature on [Shopify Help](https://help.shopify.com/en/manual/online-store/images/3d-images).

### [Anchor to Focal Point setting for images is now available](/docs/api/release-notes/previous-versions/2023-04#focal-point-setting-for-images-is-now-available)Focal Point setting for images is now available

You can now access the [`Focal Point`](https://help.shopify.com/en/manual/online-store/images/theme-images#set-a-focal-point-on-a-theme-image) for an image. `Focal Points` can be set from the shop admin while editing image files.

### [Anchor to You can use the customer's address id as input for delivery address preferences](/docs/api/release-notes/previous-versions/2023-04#you-can-use-the-customers-address-id-as-input-for-delivery-address-preferences)You can use the customer's address id as input for delivery address preferences

You can now pass the [Customer's address id](/docs/api/storefront/2023-04/objects/Customer#connection-customer-addresses) as an input for [CartBuyerIdentity.deliveryAddressPreferences](/docs/api/storefront/2023-04/objects/CartBuyerIdentity#field-cartbuyeridentity-deliveryaddresspreferences) when creating or updating carts for authenticated customers.

---

## [Anchor to GraphQL Payments Apps API changes](/docs/api/release-notes/previous-versions/2023-04#graphql-payments-apps-api-changes)GraphQL Payments Apps API changes

### [Anchor to The status field in the Payments Apps API has been removed](/docs/api/release-notes/previous-versions/2023-04#the-status-field-in-the-payments-apps-api-has-been-removed)The status field in the Payments Apps API has been removed

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The previously deprecated `status` field has been removed in favour of the `state` field on the following Payments Apps API objects:

* [`PaymentSession`](/docs/api/payments-apps/2023-04/objects/PaymentSession)
* [`RefundSession`](/docs/api/payments-apps/2023-04/objects/RefundSession)
* [`CaptureSession`](/docs/api/payments-apps/2023-04/objects/CaptureSession)
* [`VoidSession`](/docs/api/payments-apps/2023-04/objects/VoidSession)

### [Anchor to New CartErrorCodes have been added](/docs/api/release-notes/previous-versions/2023-04#new-carterrorcodes-have-been-added)New CartErrorCodes have been added

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

Two new error codes, `INVALID_DELIVERY_GROUP` and `INVALID_DELIVERY_OPTION`, have been added to the [`CartErrorCode`](/docs/api/storefront/2023-04/enums/CartErrorCode) enum. This error code can be returned when the [`cartSelectedDeliveryOptionsUpdate`](/docs/api/storefront/2023-04/mutations/cartSelectedDeliveryOptionsUpdate) mutation is called.

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2023-04#rest-admin-api-changes)REST Admin API changes

### [Anchor to Move and Hold operations for FulfillmentOrders now accept specific line items](/docs/api/release-notes/previous-versions/2023-04#move-and-hold-operations-for-fulfillmentorders-now-accept-specific-line-items)Move and Hold operations for FulfillmentOrders now accept specific line items

The [`fulfillmentOrderMove`](/docs/api/admin-graphql/2023-04/mutations/fulfillmentOrderMove) and [`fulfillmentOrderHold`](/docs/api/admin-graphql/2023-04/mutations/fulfillmentOrderHold) operations have a new and optional `fulfillment_order_line_items` parameter that allows you to specific the line itms you wish to hold or move.

### [Anchor to Transaction will now return the total unsettled set amount](/docs/api/release-notes/previous-versions/2023-04#transaction-will-now-return-the-total-unsettled-set-amount)Transaction will now return the total unsettled set amount

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

Requests for [Transaction](/docs/api/admin-rest/2023-04/resources/transaction) will now return `total_unsettled_set`. This represents the remaining amount to be captured on the transaction. `total_unsettled_set` is returned in both `shop` and `presentment` money objects with currency.

If you are leveraging **manual capture** and the **authorized** amount from [Transaction](/docs/api/admin-rest/2023-04/resources/transaction), then you should switch to referencing `total_unsettled_set`. The authorized amount can differ from the total amount to capture due to adjustments during order finalization such as tax adjustments.

### [Anchor to Additional filtering added to FulfillmentOrders](/docs/api/release-notes/previous-versions/2023-04#additional-filtering-added-to-fulfillmentorders)Additional filtering added to FulfillmentOrders

You can now retrieve a subset of [`FulfillmentOrders`](/docs/api/admin-rest/2023-04/resources/fulfillmentorder) that are assigned to the locations owned by the app performing the request, but haven't yet been requested for fulfillment.

The `assignment_status` query parameter in the [`AssignedFulfillmentOrder`](/docs/api/admin-rest/2023-04/resources/assignedfulfillmentorder#get-assigned-fulfillment-orders) endpoint can now accept a value of `fulfillment_unsubmitted` for filtering in addition to the existing `fulfillment_requested`, `fulfillment_accepted`, and `cancellation_requested` filter values.

### [Anchor to Access to the Asset API is no longer available to public apps](/docs/api/release-notes/previous-versions/2023-04#access-to-the-asset-api-is-no-longer-available-to-public-apps)Access to the Asset API is no longer available to public apps

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

When requesting the Asset API, access to create, update and delete assets is no longer accessible for public apps. Refer to [this guide](https://shopify.dev/docs/apps/online-store/other-integration-methods/asset) for more details on the change, exemptions, and how to migrate your apps.

### [Anchor to Payment properties on the Order resource have been removed](/docs/api/release-notes/previous-versions/2023-04#payment-properties-on-the-order-resource-have-been-removed)Payment properties on the Order resource have been removed

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-04#breaking)Breaking

The following properties have been removed from the [`Order`](/docs/api/admin-rest/2023-04/resources/order) resource:

* `gateway`
* `payment_details`
* `processing_method`

### [Anchor to Additional fees fields for Orders](/docs/api/release-notes/previous-versions/2023-04#additional-fees-fields-for-orders)Additional fees fields for Orders

The [`Order`](/docs/api/admin-rest/2023-04/objects/Order) object has the following new fields that represent additional fees. Additional fees are extra costs that are associated with international packages that are neither duties nor taxes.

* `current_total_additional_fees_set`
* `original_total_additional_fees_set`

### [Anchor to Added source\_location field to FulfillmentOrdersMove webhook payload](/docs/api/release-notes/previous-versions/2023-04#added-source_location-field-to-fulfillmentordersmove-webhook-payload)Added source\_location field to FulfillmentOrdersMove webhook payload

The [`FulfillmentOrdersMove`](/docs/api/admin-rest/2023-04/resources/webhook#event-topics-fulfillment-orders-moved) webhook payload is extended `source_location` field.

The [`assignedLocation`](/docs/api/admin-graphql/2023-04/objects/fulfillmentorder#field-fulfillmentorder-assignedlocation) of the `original_fulfillment_order` may be changed by the move operation. If you need to determine the originally assigned location, then you should refer to the `source_location` field instead.

---

Was this page helpful?

YesNo