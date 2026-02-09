---
source: https://shopify.dev/docs/api/release-notes/2023-07
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| July 1, 2023 | July 1, 2024 |

**What's new in 2023-07**

The following features were added in version 2023-07 of Shopify's APIs.

Highlights from the GraphQL Admin API changes:

* Additional fees as a sale line type
* New mutation for removing a `CompanyContact` from a `Company`
* Creation of the new Customer Merge API
* Transition of application credit creation to the Partner API
* New mutations `fulfillmentOrderSplit` and `fulfillmentOrderMerge` that enable splitting and merging fulfillment orders
* Sort orders by total item quantity
* Specify a custom filename when using the `fileCreate` mutation

Highlights from the GraphQL Storefront API changes:

* Search and predictive search are now available
* Local pickup inventory availability is now available

Highlights from the REST Admin API changes:

* Transition of application credit creation to the Partner API
* Discount class for `applied_discounts` and `discount_allocations` is now available on a line item for the [`Checkout`](/docs/api/admin-rest/2023-07/resources/checkout) resource
* The `tax_exempt` field is now available on the `Order` resource
* The [`ONLINE_STORE_POST_PURCHASE_CROSS_SELL`](/docs/api/admin-graphql/2023-07/enums/FulfillmentHoldReason#value-onlinestorepostpurchasecrosssell) fulfillment hold reason is now available

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2023-07#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Deprecating creation of application credits through the Admin API](/docs/api/release-notes/previous-versions/2023-07#deprecating-creation-of-application-credits-through-the-admin-api)Deprecating creation of application credits through the Admin API

Creating app credits through the Admin API is now deprecated. This affects both the [REST resource](/docs/api/admin-rest/2023-07/resources/applicationcredit#post-application-credits) and the [GraphQL mutation](/docs/api/admin-graphql/2023-07/mutations/appCreditCreate).

Moving forward, create app credits using the new [`appCreditCreate`](/docs/api/partner/2023-07/mutations/appCreditCreate) mutation in the Partner API. This change will now allow Partners to issue credits to stores that have uninstalled their app.

Learn more about [awarding app credits](/docs/apps/launch/billing/award-app-credits).

### [Anchor to Breaking changes to the product\_feeds webhook topics](/docs/api/release-notes/previous-versions/2023-07#breaking-changes-to-the-product_feeds-webhook-topics)Breaking changes to the product\_feeds webhook topics

The following major changes have been introduced to the `product_feeds` webhook topics:

* Deprecation of the use of `bulk` in favour of `full` for the [`product_feeds/full_sync`](/docs/api/admin-rest/2023-07/resources/webhook#event-topics-product-feeds-full-sync) webhook topic. To continue receiving full sync notifications, use the [`productFullSync`](/docs/api/admin-graphql/2023-07/mutations/productFullSync) mutation instead of `productBulkSync`.
* The spelling of the `occurred_at` field in the metadata for `product_feeds` notifications has been corrected.

### [Anchor to Creation of region-specific subfolders on country-code top-level domains (ccTLDs)](/docs/api/release-notes/previous-versions/2023-07#creation-of-region-specific-subfolders-on-country-code-top-level-domains-cctlds)Creation of region-specific subfolders on country-code top-level domains (ccTLDs)

You can now create region-specific subfolders on ccTLDs such as `shop.ca` or `shop.fr`. This is a departure from the previous behaviour where subfolders could only be created on generic top-level domains (gTLDs).

### [Anchor to New error code added to inventory quantity mutations](/docs/api/release-notes/previous-versions/2023-07#new-error-code-added-to-inventory-quantity-mutations)New error code added to inventory quantity mutations

The error code `item_not_stocked_at_location` has been added to the [`inventorySetOnHandQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventorySetOnHandQuantities), [`inventoryAdjustQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventoryAdjustQuantities), and [`inventoryMoveQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventoryMoveQuantities) mutations. This error code is returned when you attempt to change inventory quantities for an item that isn't stocked at the specified location.

### [Anchor to No automatic creation of a subfolder web presence for a single-country market](/docs/api/release-notes/previous-versions/2023-07#no-automatic-creation-of-a-subfolder-web-presence-for-a-single-country-market)No automatic creation of a subfolder web presence for a single-country market

As of API version 2023-07, a subfolder web presence for a single-country market is no longer automatically created.

To maintain the existing functionality, use the [`marketWebPresenceCreate`](/docs/api/admin-graphql/2023-07/mutations/marketWebPresenceCreate) mutation following the creation of a market. Passing the country code of the market region as the `subfolderSuffix` will create the corresponding web presence.

### [Anchor to Mandatory provision of the ,[object Object], field in the Payments Apps API](/docs/api/release-notes/previous-versions/2023-07#mandatory-provision-of-the-chargebackliability-field-in-the-payments-apps-api)Mandatory provision of the `chargebackLiability` field in the Payments Apps API

As of version 2023-07 of the Payments Apps API, the [`chargebackLiability`](/docs/api/payments-apps/2023-07/input-objects/PaymentSessionThreeDSecureAuthenticationData#field-paymentsessionthreedsecureauthenticationdata-chargebackliability) field must be provided in the 3-D Secure [`PaymentSessionThreeDSecureAuthenticationData`](/docs/api/payments-apps/2023-07/input-objects/PaymentSessionThreeDSecureAuthenticationData) input object. This change allows merchants to better manage their orders.

Learn more about the [Payments Apps API and 3-D Secure](/docs/apps/build/payments/credit-card/use-the-cli).

### [Anchor to Removal of the ,[object Object], field on order shipping lines](/docs/api/release-notes/previous-versions/2023-07#removal-of-the-delivery_category-field-on-order-shipping-lines)Removal of the `delivery_category` field on order shipping lines

As of API version 2023-07, we're deprecating the order shipping line `delivery_category` property. The property hasn't been in use since `2020-06-12` and will no longer be present.

### [Anchor to Translate filter settings](/docs/api/release-notes/previous-versions/2023-07#translate-filter-settings)Translate filter settings

As of API version 2023-07, we're introducing a new capability to translate filters.

When enabled, all filter labels will be eligible for translations through the [Translations API](/docs/apps/build/markets/manage-translated-content) as well as the [Translate and Adapt](https://apps.shopify.com/translate-and-adapt?shpxid=c0b0c0ff-6A02-4274-4021-DD5A9A2B85A9) app.

### [Anchor to Use of Flow action extensions to update marketing activity delivery status](/docs/api/release-notes/previous-versions/2023-07#use-of-flow-action-extensions-to-update-marketing-activity-delivery-status)Use of Flow action extensions to update marketing activity delivery status

We're deprecating the [`abandonmentEmailStateUpdate`](/docs/api/admin-graphql/2023-07/mutations/abandonmentEmailStateUpdate) mutation. Instead, you can use the [`abandonmentUpdateActivitiesDeliveryStatuses`](/docs/api/admin-graphql/2023-07/mutations/abandonmentUpdateActivitiesDeliveryStatuses) to update the delivery status of marketing activities created using a Flow action extension.

### [Anchor to Use of ,[object Object], on ,[object Object], endpoint](/docs/api/release-notes/previous-versions/2023-07#use-of-total_count-on-customersegmentmemberconnection-endpoint)Use of `total_count` on `CustomerSegmentMemberConnection` endpoint

You can now use `total_count` on the [`CustomerSegmentMemberConnection`](/docs/api/admin-graphql/2023-07/connections/CustomerSegmentMemberConnection) endpoint, which provides the total count of a specified customer segment. Additionally, the `total_count` field on [`SegmentStatistics`](/docs/api/admin-graphql/2023-07/objects/SegmentStatistics) object has been removed. The new `total_count` functionality makes it easier to know the count of members of a specified segment.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2023-07#graphql-admin-api-changes)GraphQL Admin API changes

The following are all the changes introduced in the 2023-07 version of the GraphQL Admin API.

### [Anchor to New API to update marketing activity delivery status](/docs/api/release-notes/previous-versions/2023-07#new-api-to-update-marketing-activity-delivery-status)New API to update marketing activity delivery status

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of 2023-07, you can use the [`abandonmentUpdateActivitiesDeliveryStatuses`](/docs/api/admin-graphql/2023-07/mutations/abandonmentUpdateActivitiesDeliveryStatuses) to update the delivery status of marketing activities created via Flow action extension. We're deprecating the [`abandonmentEmailStateUpdate`](/docs/api/admin-graphql/2023-07/mutations/abandonmentEmailStateUpdate) mutation since it's being replaced by the new API.

### [Anchor to New error codes added to ,[object Object], mutation](/docs/api/release-notes/previous-versions/2023-07#new-error-codes-added-to-fileupdate-mutation)New error codes added to `fileUpdate` mutation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, the [new error codes](/docs/api/admin-graphql/2023-07/enums/FilesErrorCode) `FILENAME_ALREADY_EXISTS` and `INVALID_FILENAME` have been added to the [`fileUpdate`](/docs/api/admin-graphql/2023-07/mutations/fileUpdate) mutation. These error codes are returned when you attempt to update the filename (URL Handle) and the input either matches an existing filename (URL Handle) or it's invalid.

### [Anchor to New field ,[object Object], on the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#new-field-taxexempt-on-the-order-object)New field `taxExempt` on the `Order` object

As of GraphQL Admin API 2023-07, the `taxExempt` field has been added to the [`Order`](/docs/api/admin-graphql/2023-07/objects/Order) object. You can use this field to determine whether an order was exempt from taxes.

Orders can be exempt from taxes if the **Charge taxes** option was disabled during the creation of a draft order, or if the order was created for a customer with the **Collect tax** option disabled.

Note

Any products that are tax exempt in an order aren't considered when calculating the `taxExempt` field.

**Note:**

Any products that are tax exempt in an order aren't considered when calculating the `taxExempt` field.

### [Anchor to Tax partners can now configure the state of a tax app configuration](/docs/api/release-notes/previous-versions/2023-07#tax-partners-can-now-configure-the-state-of-a-tax-app-configuration)Tax partners can now configure the state of a tax app configuration

We've added the [`taxAppConfigure`](/docs/api/admin-graphql/2023-07/mutations/taxAppConfigure) mutation, which enables selected tax partners to configure the state of an existing integrated tax service. This extended control provides Partners with more flexibility and adaptability in managing tax services, ensuring a smoother, more efficient operation for their app.

### [Anchor to Additional fees as a sale line type](/docs/api/release-notes/previous-versions/2023-07#additional-fees-as-a-sale-line-type)Additional fees as a sale line type

As of API version 2023-07, sales records can now be of type [`AdditonalFeeSale`](/docs/api/admin-graphql/2023-07/objects/AdditionalFeeSale), which represents a sale associated with an additional fee charge.

For more information on this new type implementation, refer to the [sale interface](/docs/api/admin-graphql/2023-07/interfaces/Sale).

### [Anchor to Subfolders can now exist on ccTLD domains](/docs/api/release-notes/previous-versions/2023-07#subfolders-can-now-exist-on-cctld-domains)Subfolders can now exist on ccTLD domains

As of API version 2023-07, you can now create region-specific subfolders on country-code top-level domains (ccTLDs), such as `shop.ca` or `shop.fr`. Previously, subfolders could only be created on generic top-level domains (gTLDs).

### [Anchor to New mutation for removing a ,[object Object], from a Company](/docs/api/release-notes/previous-versions/2023-07#new-mutation-for-removing-a-companycontact-from-a-company)New mutation for removing a `CompanyContact` from a Company

As of API version 2023-07, you can use the [`companyContactRemoveFromCompany`](/docs/api/admin-graphql/2023-07/mutations/companyContactRemoveFromCompany) mutation to remove a company contact from a company, even if they have placed orders on behalf of the company.

### [Anchor to Webhooks for B2B Customers Flow primitives](/docs/api/release-notes/previous-versions/2023-07#webhooks-for-b2b-customers-flow-primitives)Webhooks for B2B Customers Flow primitives

As of API version 2023-07, we're providing [additional webhook notifications](/docs/api/admin-graphql/2023-07/enums/WebhookSubscriptionTopic) for changes to the major entities within the B2B Customers product. These hooks enable better integration with Flow. The following webhooks are provided:

* `company_contact_roles/assign`
* `company_contact_roles/revoke`

[Learn more about the webhooks](/docs/api/admin-rest/2023-07/resources/webhook#event-topics).

### [Anchor to [object Object], field is available behind beta flag on the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#exchangev2-field-is-available-behind-beta-flag-on-the-order-object)`ExchangeV2` field is available behind beta flag on the `Order` object

As of API version 2023-07, you can use the `exchangeV2` field on the [`Order`](/docs/api/admin-graphql/2023-07/objects/Order) object to get a better exchange (an `exchangeV2` object value). This helps ERP partners properly integrate optimal exchange values.

[Learn more](https://docs.google.com/document/d/1miy-zl9wP5CI7x_ZeTHUFOlE6EiFXxFlrx9hgSHsrVc/edit#heading=h.zcwwdnbswa1k).

### [Anchor to Shop Promise details presented to buyer at checkout](/docs/api/release-notes/previous-versions/2023-07#shop-promise-details-presented-to-buyer-at-checkout)Shop Promise details presented to buyer at checkout

The [`DeliveryMethod`](/docs/api/admin-graphql/2023-07/objects/DeliveryMethod) object now has a `brandedPromise` field that can be used to determine if an order was branded with **Shop Promise** at checkout.

Additionally, the [`MailingAddress`](/docs/api/admin-graphql/2023-07/objects/MailingAddress) object now includes the `timeZone` field, which you can use with the `DeliveryMethod`'s `maxDeliveryDateTime` field, to determine the date and time according to the time zone of the destination address.

Learn more about [Shop Promise eligibility](https://www.shopify.com/shop-promise).

### [Anchor to Breaking changes to Product Feeds API](/docs/api/release-notes/previous-versions/2023-07#breaking-changes-to-product-feeds-api)Breaking changes to Product Feeds API

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, we're introducing the following breaking changes to the product feeds webhook topics:

* Deprecated use of `bulk` in favour of `full` for the [`product_feeds/full_sync`](/docs/api/admin-rest/2023-07/resources/webhook#event-topics-product-feeds-full-sync) webhook topic
* Corrected spelling of `occurred_at` field in metadata for `product_feeds` notifications metadata

Partners who want to continue receiving full sync notifications should start using the [`productFullSync`](/docs/api/admin-graphql/2023-07/mutations/productFullSync) mutation instead of [`productBulkSync`](/docs/api/admin-graphql/2023-07/mutations/productBulkSync).

### [Anchor to Introducing the new Customer Merge API](/docs/api/release-notes/previous-versions/2023-07#introducing-the-new-customer-merge-api)Introducing the new Customer Merge API

As of API version 2023-07, you can now use the Customer Merge API to combine two separate customer profiles with certain non-blocking criteria. You can use the new mutations and queries to do the following tasks:

* [Preview a customer merge](/docs/api/admin-graphql/2023-07/queries/customerMergePreview)
* [Merge two customers](/docs/api/admin-graphql/2023-07/mutations/customerMerge)
* [Follow the status of an ongoing merge](/docs/api/admin-graphql/2023-07/queries/customerMergeJobStatus)

Additionally, you can check whether a customer can be merged with another customer using the new [`Customer.mergeable`](/docs/api/admin-graphql/2023-07/objects/Customer#field-customer-mergeable) field. This field is also available on the [`CustomerSegmentMember.mergeable`](/docs/api/admin-graphql/2023-07/objects/CustomerSegmentMember#field-customersegmentmember-mergeable) object.

[Learn more about merging customer profiles](https://help.shopify.com/manual/customers/manage-customers#merging-customer-profiles).

### [Anchor to Adding metafield attributes to the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#adding-metafield-attributes-to-the-customersegmentmember-object)Adding metafield attributes to the `CustomerSegmentMember` object

As of API version 2023-07, the [`CustomerSegmentMember`](/docs/api/admin-graphql/2023-07/objects/CustomerSegmentMember) object now has the attributes and connections to access the metafields associated to the customer.

### [Anchor to Added ,[object Object], attribute to the ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#added-acceptsmultiplevalues-attribute-to-the-segmenteventfilterparameter-object)Added `acceptsMultipleValues` attribute to the `SegmentEventFilterParameter` object

As of API version 2023-07, the [`SegmentEventFilterParameter`](/docs/api/admin-graphql/2023-07/objects/SegmentEventFilterParameter) object now has the attribute `acceptsMultipleValues` to denote if the parameter can handle multiple values. For example, the `id` parameter for the `products_purchased` function can accept multiple values, such as `products_purchased(id: (2012162031638, 1012132033639) = false`.

Learn more about [segment query language](/docs/api/shopifyql/segment-query-language-reference).

### [Anchor to Function parameter values can be queried](/docs/api/release-notes/previous-versions/2023-07#function-parameter-values-can-be-queried)Function parameter values can be queried

As of API version 2023-07, you can use the new `functionParameterQueryName` argument on [`segmentValueSuggestions`](/docs/api/admin-graphql/2023-07/queries/segmentValueSuggestions) to query for function parameter value suggestions for customer segmentation.

For example, the `products_purchased` filter has the function parameter `id`: `products_purchased(id: '2012162031638') = true`. To retrieve a list of possible product IDs to use for the `id` function parameter, provide `filterQueryName: 'products_purchased', functionParameterQueryName: 'id'` as arguments to the `segmentValueSuggestions` query.

### [Anchor to Additional webhook subscription topics for customer tags](/docs/api/release-notes/previous-versions/2023-07#additional-webhook-subscription-topics-for-customer-tags)Additional webhook subscription topics for customer tags

As of API version 2023-07, Shopify's providing additional webhook subscription topics for customer tags:

* `CUSTOMER_TAGS_ADDED`
* `CUSTOMER_TAGS_REMOVED`

[Learn more about these webhooks](/docs/api/admin-graphql/2023-07/enums/WebhookSubscriptionTopic).

### [Anchor to Transition of application credit creation to the Partner API](/docs/api/release-notes/previous-versions/2023-07#transition-of-application-credit-creation-to-the-partner-api)Transition of application credit creation to the Partner API

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, we're deprecating creating app credits through the Admin API. Both the [REST resource](/docs/api/admin-rest/2023-07/resources/applicationcredit#post-application-credits), and the [GraphQL mutation](/docs/api/admin-graphql/2023-07/mutations/appCreditCreate) include the capability to create app credits deprecated. Going forward, you should create app credits using the [`appCreditCreate`](/docs/api/partner/2023-07/mutations/appCreditCreate) mutation in the Partner API.

This change enables us to implement new features for creating app credits, such as allowing Partners to issue credits to stores that have uninstalled their app.

### [Anchor to Purchase order numbers added to ,[object Object], and ,[object Object], objects](/docs/api/release-notes/previous-versions/2023-07#purchase-order-numbers-added-to-order-and-draftorder-objects)Purchase order numbers added to `Order` and `DraftOrder` objects

As of API version 2023-07, we've added a new field called `poNumber` to the [`Order`](/docs/api/admin-graphql/2023-07/objects/Order) and [`DraftOrder`](/docs/api/admin-graphql/2023-07/objects/DraftOrder) objects.

The [`OrderInput`](/docs/api/admin-graphql/2023-07/input-objects/OrderInput) and [`DraftOrderInput`](/docs/api/admin-graphql/2023-07/input-objects/DraftOrderInput) input objects now accept a `poNumber`. This sets the purchase order number during [`orderUpdate`](/docs/api/admin-graphql/2023-07/mutations/orderUpdate), [`draftOrderUpdate`](/docs/api/admin-graphql/2023-07/mutations/draftOrderUpdate), and [`draftOrderCreate`](/docs/api/admin-graphql/2023-07/mutations/draftOrderCreate) mutations.

### [Anchor to New field ,[object Object], on ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#new-field-ismarketplace-on-channeldefinition-object)New field `isMarketplace` on `ChannelDefinition` object

As of API version 2023-07, you can use the new field `isMarketplace` on the [`ChannelDefinition`](/docs/api/admin-graphql/2023-07/objects/ChannelDefinition) object to check if a channel definition represents a marketplace, such as shops on Facebook, Instagram, or Buy on Google.

The new `isMarketplace` field indicates whether any object that references `ChannelDefinition` is related to a marketplace channel. For example, you can determine if an order was placed on a channel that's a marketplace or if the store has available channels that are marketplaces.

### [Anchor to New field ,[object Object], on ,[object Object], object](/docs/api/release-notes/previous-versions/2023-07#new-field-type-on-translatablecontent-object)New field `type` on `TranslatableContent` object

As of API version 2023-07, you can use the new field `type` on [`TranslatableContent`](/docs/api/admin-graphql/2023-07/objects/TranslatableContent) to get the type of the translatable content.

The new `type` field gives more information about the underlying translatable content which enables you to conditionally render UI elements, such as input fields.

Learn more about the [`LocalizableContentType`](/docs/api/admin-graphql/2023-07/enums/LocalizableContentType) object.

### [Anchor to New ,[object Object], webhook](/docs/api/release-notes/previous-versions/2023-07#new-tax_partners-update-webhook)New `tax_partners/update` webhook

As of API version 2023-07, the `tax_partners/update` webhook is available.

The `tax_partners/update` webhook is called whenever a tax partner is added or updated. Partners can use this webhook to determine when a merchant has made changes to the partner's tax app.

[Learn more about these webhooks](/docs/api/admin-graphql/2023-04/enums/WebhookSubscriptionTopic).

### [Anchor to Translate filter settings](/docs/api/release-notes/previous-versions/2023-07#translate-filter-settings)Translate filter settings

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, we're introducing a new capability to translate filters.

When enabled, all filter labels will be eligible for translations through the [Translations API](/docs/apps/build/markets/manage-translated-content) as well as the [Translate and Adapt](https://apps.shopify.com/translate-and-adapt?shpxid=c0b0c0ff-6A02-4274-4021-DD5A9A2B85A9) app.

### [Anchor to [object Object], field added to ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#duplicateresolutionmode-field-added-to-filecreate)`duplicateResolutionMode` field added to `fileCreate`

As of API version 2023-07, you can use the new `duplicateResolutionMode` field on the [`fileCreate`](/docs/api/admin-graphql/2023-07/mutations/fileCreate) mutation to control how duplicate filenames are handled.

### [Anchor to [object Object], fulfillment hold reason](/docs/api/release-notes/previous-versions/2023-07#online_store_post_purchase_cross_sell-fulfillment-hold-reason)`ONLINE_STORE_POST_PURCHASE_CROSS_SELL` fulfillment hold reason

As of API version 2023-07, you can determine whether fulfillment has been placed on hold for a post-purchase with the reason [`ONLINE_STORE_POST_PURCHASE_CROSS_SELL`](/docs/api/admin-graphql/2023-07/objects/FulfillmentHold).

### [Anchor to Splitting and merging fulfillment orders](/docs/api/release-notes/previous-versions/2023-07#splitting-and-merging-fulfillment-orders)Splitting and merging fulfillment orders

As of API version 2023-07, you can split and merge fulfillment orders. You can split a single fulfillment order into multiple fulfillment orders by dividing the line items across multiple fulfillment orders. You can also merge fulfillment orders together into a single fulfillment order.

Learn more about the [`fulfillmentOrderSplit`](/docs/api/admin-graphql/2023-07/mutations/fulfillmentOrderSplit) and [`fulfillmentOrderMerge`](/docs/api/admin-graphql/2023-07/mutations/fulfillmentOrderMerge) mutations.

### [Anchor to Update bytes in-place using ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#update-bytes-in-place-using-fileupdate)Update bytes in-place using `fileUpdate`

As of API version 2023-07, you can use the [`fileUpdateInput`](/docs/api/admin-graphql/2023-07/input-objects/FileUpdateInput) input object to provide an `originalSource`, which is used to update the bytes of a file. Passing `originalSource` when updating is supported for media images and generic files.

Using this functionality makes it easy to do an in-place update of an existing file.

### [Anchor to Inventory states](/docs/api/release-notes/previous-versions/2023-07#inventory-states)Inventory states

As of API version 2023-07, there are new mutations that enable you to alter the inventory quantities at a location. State quantities `reserved` and `on_hand` are adjustable through the API. In addition, there are queries to retrieve quantities for every state.

For more information, refer to [Inventory management apps](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states).

### [Anchor to New error code added to inventory quantity mutations](/docs/api/release-notes/previous-versions/2023-07#new-error-code-added-to-inventory-quantity-mutations)New error code added to inventory quantity mutations

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, a new error code `item_not_stocked_at_location` has been added to the [`inventorySetOnHandQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventorySetOnHandQuantities), [`inventoryAdjustQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventoryAdjustQuantities), and [`inventoryMoveQuantities`](/docs/api/admin-graphql/2023-07/mutations/inventoryMoveQuantities) mutations. This error code is returned when you attempt to change inventory quantities for an item that isn't stocked at the specified location.

[Learn more about managing inventory quantities](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#step-3-manage-inventory-quantities).

### [Anchor to [object Object], support for ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#metafieldsset-support-for-mediaimage)`metafieldsSet` support for `MediaImage`

As of API version 2023-07, you can use the [`metafieldsSet`](/docs/api/admin-graphql/2023-07/mutations/metafieldsSet) mutation to set metafields on images using `MediaImage` GIDs.

### [Anchor to Deprecation of image-related fields in product and product variants mutations](/docs/api/release-notes/previous-versions/2023-07#deprecation-of-image-related-fields-in-product-and-product-variants-mutations)Deprecation of image-related fields in product and product variants mutations

As of API version 2023-07, we're deprecating a set of fields used for associating images with products and variants:

* **[`ProductInput`](/docs/api/admin-graphql/2023-07/input-objects/ProductInput)**: `images` field deprecation. Use the newly introduced `media` field instead.
* **[`ProductVariantInput`](/docs/api/admin-graphql/2023-07/input-objects/ProductVariantInput)**: `imageId` and `imageSrc` field deprecation. Use `mediaId` and `mediaSrc` instead.
* **[`ProductVariantsBulkInput`](/docs/api/admin-graphql/2023-07/input-objects/ProductVariantsBulkInput)**: `imageSrc` field deprecation. Use `mediaSrc` instead.

### [Anchor to [object Object], access setting for app-owned metafields](/docs/api/release-notes/previous-versions/2023-07#public_read-access-setting-for-app-owned-metafields)`PUBLIC_READ` access setting for app-owned metafields

As of API version 2023-07, you can now apply a `PUBLIC_READ` access setting to your metafield definitions. If your metafield definition is `PUBLIC_READ`, this means the following:

* The merchant can read the metafields on the definition.
* All installed applications with proper access scopes can read the metafields on the definition.
* Only the owner of the definition can write metafields.

This new setting builds upon the `PRIVATE`, `MERCHANT_READ`, and `MERCHANT_READ_WRITE` access settings that were [released in January 2023](https://shopify.dev/changelog/access-controls-for-app-metafields).

Learn more about [access controls](/docs/apps/build/custom-data/ownership#reserved-prefixes).

Note

The `access` field can only be set when the definition is in your own [reserved namespace](/docs/apps/build/custom-data/ownership#reserved-prefixes).

**Note:**

The `access` field can only be set when the definition is in your own [reserved namespace](/docs/apps/build/custom-data/ownership#reserved-prefixes).

### [Anchor to Moving ,[object Object], field from ,[object Object], to ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#moving-total_count-field-from-segmentstatistics-to-customersegmentmemberconnection)Moving `total_count` field from `SegmentStatistics` to `CustomerSegmentMemberConnection`

As of API version 2023-07, you can now use `total_count` on the [`CustomerSegmentMemberConnection`](/docs/api/admin-graphql/2023-07/connections/CustomerSegmentMemberConnection) endpoint, which provides the total count of a specified customer segment.

Additionally, the `total_count` field on [`SegmentStatistics`](/docs/api/admin-graphql/2023-07/objects/SegmentStatistics) object has been removed. The new `total_count` functionality makes it easier to know the count of members of a specified segment.

### [Anchor to Creating a single-country market will no longer automatically create a subfolder web presence for this market](/docs/api/release-notes/previous-versions/2023-07#creating-a-single-country-market-will-no-longer-automatically-create-a-subfolder-web-presence-for-this-market)Creating a single-country market will no longer automatically create a subfolder web presence for this market

As of API version 2023-07, we're no longer automatically creating a subfolder web presence for a single-country market. To maintain existing behaviour, you can follow up creating a market with the [`marketWebPresenceCreate`](/docs/api/admin-graphql/2023-07/mutations/marketWebPresenceCreate) mutation. Passing in the country code of the market region as the `subfolderSuffix` creates the corresponding web presence.

### [Anchor to Unknown sale type](/docs/api/release-notes/previous-versions/2023-07#unknown-sale-type)Unknown sale type

As of API version 2023-07, we're introducing sales type `UnknownSale` with line type `UNKNOWN` that represents new types of sales that might be added in the future and don't exist on older versions.

This is a complimentary object type for the [`SalesLineType` UNKNOWN](/docs/api/admin-graphql/2023-07/enums/SaleLineType#value-unknown) and implements the [`Sale`](/docs/api/admin-graphql/2023-07/interfaces/Sale) interface.

### [Anchor to Adding the ability to sort orders by total item quantity](/docs/api/release-notes/previous-versions/2023-07#adding-the-ability-to-sort-orders-by-total-item-quantity)Adding the ability to sort orders by total item quantity

As of API version 2023-07, we've added `TOTAL_ITEM_QUANTITY` to [`OrderSortKeys`](/docs/api/admin-graphql/2023-07/enums/OrderSortKeys) so that you can sort orders by the total quantity of items.

### [Anchor to Manage quantity rules for B2B customers](/docs/api/release-notes/previous-versions/2023-07#manage-quantity-rules-for-b2b-customers)Manage quantity rules for B2B customers

As of API version 2023-07, you can use the [`quantityRulesAdd`](/docs/api/admin-graphql/2023-07/mutations/quantityRulesAdd) and [`quantityRulesDelete`](/docs/api/admin-graphql/2023-07/mutations/quantityRulesDelete) mutations to manage product variant minimums, maximums, and increments for B2B customers. Use the `quantityRules` field on the [`ProductVariantContextualPricing`](/docs/api/admin-graphql/2023-07/objects/ProductVariantContextualPricing) object to view the quantity rules applied for the `companyLocationId` input.

[Learn more about quantity rules](/docs/api/admin-graphql/2023-07/objects/QuantityRule).

### [Anchor to Sale attribution edits now can be subscribed using the ,[object Object], webhook](/docs/api/release-notes/previous-versions/2023-07#sale-attribution-edits-now-can-be-subscribed-using-the-orders-updated-webhook)Sale attribution edits now can be subscribed using the `orders/updated` webhook

As of API version 2023-07, you can now subscribe to the `orders/updated` webhook to be notified of any sale attribution edits to an order. When a staff attribution edit is made on POS, the `orders/updated` webhook fires. The payload includes a new `attributed_staffs` field under `line_items`. This new field will reflect the new attributions on the order after the edit.

A user can edit the staff attributions on multiple line items at once on POS. In this case, the webhook payload could include multiple updated line items with different attributions applied to them.

[Learn more about the `orders/updated` webhook](/docs/api/admin-rest/2023-07/resources/webhook#event-topics).

Note

The payload in the `orders/create` webhook will also be updated to include `attributed_staffs`.

**Note:**

The payload in the `orders/create` webhook will also be updated to include `attributed_staffs`.

### [Anchor to Specify a custom filename using ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#specify-a-custom-filename-using-filecreate)Specify a custom filename using `fileCreate`

As of API version 2023-07, you can now specify a custom `filename` when using the [`fileCreate`](/docs/api/admin-graphql/2023-07/mutations/fileCreate) mutation to create files that will appear in the Shopify admin.

### [Anchor to Update a filename using ,[object Object]](/docs/api/release-notes/previous-versions/2023-07#update-a-filename-using-fileupdate)Update a filename using `fileUpdate`

As of API version 2023-07, we've added a new field called `filename` to the [`fileUpdate`](/docs/api/admin-graphql/2023-07/mutations/fileUpdate) mutation. This new field allows you to update the `filename` of both generic files and images.

---

## [Anchor to GraphQL Storefront API changes](/docs/api/release-notes/previous-versions/2023-07#graphql-storefront-api-changes)GraphQL Storefront API changes

### [Anchor to Search and predictive search are now available](/docs/api/release-notes/previous-versions/2023-07#search-and-predictive-search-are-now-available)Search and predictive search are now available

As of API version 2023-07, you can now use `search` and `predictiveSearch` queries to enable natural language search on your custom storefronts.

The [`search`](/docs/api/storefront/2023-07/queries/search) query returns the most relevant search results among product, page and article resource types. Merchants can use the [Shopify Search & Discovery app](https://apps.shopify.com/search-and-discovery) to change the default value of the resource types and customize search results.

The [`predictiveSearch`](/docs/api/storefront/2023-07/queries/predictiveSearch) query helps you implement a predictive search dropdown interface where suggested results are displayed immediately as buyers type into the search bar.

[Learn more](/docs/storefronts/headless/building-with-the-storefront-api/search-discovery).

### [Anchor to Determining local pickup inventory availability](/docs/api/release-notes/previous-versions/2023-07#determining-local-pickup-inventory-availability)Determining local pickup inventory availability

As of API version 2023-07, you can now use the `quantityAvailable` field on the [`StoreAvailability`](/docs/api/storefront/2023-07/objects/StoreAvailability) object to determine the inventory available for a product variant at a particular local pickup location.

---

## [Anchor to GraphQL Payments Apps API changes](/docs/api/release-notes/previous-versions/2023-07#graphql-payments-apps-api-changes)GraphQL Payments Apps API changes

### [Anchor to New ,[object Object], field for onsite credit card payments apps with 3-D Secure](/docs/api/release-notes/previous-versions/2023-07#new-chargebackliability-field-for-onsite-credit-card-payments-apps-with-3-d-secure)New `chargebackLiability` field for onsite credit card payments apps with 3-D Secure

#### [Anchor to Action-required](/docs/api/release-notes/previous-versions/2023-07#action-required)Action-required

As of API version 2023-07, you must provide the [`chargebackLiability`](/docs/api/payments-apps/2023-07/input-objects/PaymentSessionThreeDSecureAuthenticationData#field-paymentsessionthreedsecureauthenticationdata-chargebackliability) field in the 3-D Secure [`PaymentSessionThreeDSecureAuthenticationData`](/docs/api/payments-apps/2023-07/input-objects/PaymentSessionThreeDSecureAuthenticationData) input object. Merchants will benefit from this information to better manage their orders.

Learn more about the [Payments Apps API and 3-D Secure](/docs/apps/build/payments/credit-card/use-the-cli).

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2023-07#rest-admin-api-changes)REST Admin API changes

### [Anchor to Transition of application credit creation to the Partner API](/docs/api/release-notes/previous-versions/2023-07#transition-of-application-credit-creation-to-the-partner-api)Transition of application credit creation to the Partner API

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, we're deprecating creating app credits through the Admin API. Both the [REST resource](/docs/api/admin-rest/2023-07/resources/applicationcredit#post-application-credits) and the [GraphQL mutation](/docs/api/admin-graphql/2023-07/mutations/appCreditCreate) include the capability to create app credits deprecated. Going forward, you should create app credits using the [`appCreditCreate`](/docs/api/partner/2023-07/mutations/appCreditCreate) mutation in the Partner API.

This change allows Shopify to implement new features for app credit creation, such as allowing Partners to issue credits to stores that have uninstalled their app.

### [Anchor to Removal of the ,[object Object], field on order shipping lines](/docs/api/release-notes/previous-versions/2023-07#removal-of-the-delivery_category-field-on-order-shipping-lines)Removal of the `delivery_category` field on order shipping lines

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2023-07#breaking)Breaking

As of API version 2023-07, we're deprecating the order shipping line `delivery_category` property. The property hasn't been in use since `2020-06-12` and will no longer be present.

### [Anchor to Purchase order numbers added to ,[object Object], and ,[object Object], objects](/docs/api/release-notes/previous-versions/2023-07#purchase-order-numbers-added-to-order-and-draftorder-objects)Purchase order numbers added to `Order` and `DraftOrder` objects

As of API version 2023-07, we've added a new field called `poNumber` to the [`Order`](/docs/api/admin-rest/2023-07/resources/order) and [`DraftOrder`](/docs/api/admin-rest/2023-07/resources/draftorder) resources.

### [Anchor to Discount class for ,[object Object], and ,[object Object], on a line item in the ,[object Object], resource](/docs/api/release-notes/previous-versions/2023-07#discount-class-for-applied_discounts-and-discount_allocations-on-a-line-item-in-the-checkout-resource)Discount class for `applied_discounts` and `discount_allocations` on a line item in the `Checkout` resource

As of API version 2023-07, the [`Checkout`](/docs/api/admin-rest/2023-07/resources/checkout) resource includes the `discount_class` attribute in the `line_items[n].applied_discounts` and `line_items[n].discount_allocations`.

The `discount_class` identifies the type of discount applied to a line\_item:

**`PRODUCT`**: Denotes a product class discount that applies to specific products only.
**`ORDER`**: Denotes an order class discount that applies across all line items.

### [Anchor to New field tax\_exempt on the ,[object Object], resource](/docs/api/release-notes/previous-versions/2023-07#new-field-tax_exempt-on-the-order-resource)New field tax\_exempt on the `Order` resource

As of API version 2023-07, we've added the `tax_exempt` field to the [`Order`](/docs/api/admin-rest/2023-07/resources/order) resource. You can use this field to determine whether an order was exempt from taxes.

Orders can be exempt from taxes if the **Charge taxes** option was disabled during the creation of a draft order, or if the order was created for a customer with the **Collect tax** option disabled.

Note

Any products that are tax exempt in an order aren't considered when calculating the `tax_exempt` field.

**Note:**

Any products that are tax exempt in an order aren't considered when calculating the `tax_exempt` field.

### [Anchor to [object Object], fulfillment hold reason](/docs/api/release-notes/previous-versions/2023-07#online_store_post_purchase_cross_sell-fulfillment-hold-reason)`ONLINE_STORE_POST_PURCHASE_CROSS_SELL` fulfillment hold reason

As of API version 2023-07, you can determine whether a fulfillment has been placed on hold for a post-purchase with the reason `ONLINE_STORE_POST_PURCHASE_CROSS_SELL`.

[Learn more](/docs/api/admin-graphql/2023-07/objects/FulfillmentHold).

### [Anchor to Splitting and merging fulfillment orders](/docs/api/release-notes/previous-versions/2023-07#splitting-and-merging-fulfillment-orders)Splitting and merging fulfillment orders

As of API version 2023-07, you can split and merge fulfillment orders. You can split a single fulfillment order into multiple fulfillment orders by dividing the line items across multiple fulfillment orders. You can also merge fulfillment orders together into a single fulfillment order.

[Learn more about the `FulfillmentOrder` resource](/docs/api/admin-rest/2023-07/resources/fulfillmentorder).

### [Anchor to Sale attribution edits now can be subscribed using the ,[object Object], webhook](/docs/api/release-notes/previous-versions/2023-07#sale-attribution-edits-now-can-be-subscribed-using-the-orders-updated-webhook)Sale attribution edits now can be subscribed using the `orders/updated` webhook

As of API version 2023-07, you can now subscribe to the `orders/updated` webhook to be notified of any sale attribution edits to an order. When a staff attribution edit is made on POS, the `orders/updated` webhook fires. The payload includes a new `attributed_staffs` field under `line_items`. This new field will reflect the new attributions on the order after the edit.

A user can edit the staff attributions on multiple line items at once on POS. In this case, the webhook payload could include multiple updated line items with different attributions applied to them.

[Learn more about the `orders/updated` webhook](/docs/api/admin-rest/2023-07/resources/webhook).

Note

The payload in the `orders/create` webhook will also be updated to include `attributed_staffs`.

**Note:**

The payload in the `orders/create` webhook will also be updated to include `attributed_staffs`.

---

Was this page helpful?

YesNo