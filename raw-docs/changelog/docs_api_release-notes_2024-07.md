---
source: https://shopify.dev/docs/api/release-notes/2024-07
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| July 1, 2024 | July 1, 2025 |

---

## [Anchor to Highlights](/docs/api/release-notes/previous-versions/2024-07#highlights)Highlights

Here are some highlights of version 2024-07 of Shopify's APIs:

* [Apply discount codes to a draft order](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput) and decide whether to accept automatic discounts when a [draft order is calculated](/docs/api/admin-graphql/latest/mutations/draftOrderCalculate).
* Identify fulfillment orders containing deliveries to [pickup point locations](/docs/api/admin-graphql/latest/enums/DeliveryMethodType).
* The [`PRODUCTS_CREATE`](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-productscreate) and [`PRODUCTS_UPDATE`](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-productsupdate) webhook payloads now contain information about the media on a product.
* Use the `metafields` and `metafieldDefinitions` connections on the [`OnlineStoreArticle`](/docs/api/admin-graphql/latest/objects/OnlineStoreArticle#connections), [`OnlineStoreBlog`](/docs/api/admin-graphql/latest/objects/OnlineStoreBlog#connections), and [`OnlineStorePage`](/docs/api/admin-graphql/latest/objects/OnlineStorePage#connections) objects. Metafields are also now supported on the [`SellingPlan`](/docs/api/admin-graphql/latest/objects/SellingPlan) object.
* Use the [`files`](/docs/api/admin-graphql/latest/queries/files) query to retrieve 3D models and external videos.
* The [`MobilePlatformApplication`](/docs/api/admin-graphql/latest/unions/MobilePlatformApplication) type facilitates the development and operational integration of shared web credentials and app link systems for Shopify mobile apps on both iOS and Android platforms.
* Use the Storefront API to [manage gift cards on a cart](#storefront-api-changes).
* Use the payment customization function to more easily [hide](/docs/api/functions/reference/payment-customization/graphql/common-objects/hideoperation?api%5Bversion%5D=2024-07) accelerated checkout methods.

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2024-07#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Billing attempts](/docs/api/release-notes/previous-versions/2024-07#billing-attempts)Billing attempts

Similar to creating a new order through checkout, the availability of inventory is now checked during the billing attempt process.

If product variants are configured to [prevent overselling](https://help.shopify.com/manual/products/inventory/getting-started-with-inventory/selling-when-out-of-stock) and one or more items in the subscription contract are out of stock, then the billing attempt will fail with the [`INSUFFICIENT_INVENTORY`](/docs/api/admin-graphql/latest/enums/SubscriptionBillingAttemptErrorCode#value-insufficientinventory) error code.

Learn more about [subscription contracts and billing attempts](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

### [Anchor to Cart-level discounts](/docs/api/release-notes/previous-versions/2024-07#cart-level-discounts)Cart-level discounts

The `discountedPriceSet` and `discountedPrice` fields on the [`ShippingLine`](/docs/api/admin-graphql/2023-07/objects/ShippingLine) object now include cart-level discounts applied to an order, including the free shipping discount, when calculating the discounted price.

In API versions prior to 2024-07, you needed to subtract the `discountAllocations` from `discountedPriceSet` or `discountedPrice` fields to get an accurate value. If you do this in API version 2024-07 and higher, then you'll subtract the same discount twice.

### [Anchor to Cart wallet preferences](/docs/api/release-notes/previous-versions/2024-07#cart-wallet-preferences)Cart wallet preferences

We've deprecated the following types in the Storefront API:

* `walletPreferences` argument on the [`CartBuyerIdentityInput`](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput) input object
* `walletPreferences` field on the [`CartBuyerIdentity`](/docs/api/storefront/latest/objects/CartBuyerIdentity) object

Use [`CartBuyerIdentityInput.preferences.wallet`](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput#field-cartbuyeridentityinput-preferences) instead.

### [Anchor to Checkout types removed](/docs/api/release-notes/previous-versions/2024-07#checkout-types-removed)Checkout types removed

We've removed checkout types from the Storefront API, following their [deprecation in the 2024-04 API version](/docs/api/release-notes/previous-versions/2024-04#deprecations-storefront-api-and-rest-admin-api).

For more information, refer to the [developer changelog](/changelog/deprecation-of-checkout-apis).

### [Anchor to Deprecation of REST resources](/docs/api/release-notes/previous-versions/2024-07#deprecation-of-rest-resources)Deprecation of REST resources

The [`Checkout`](/docs/api/admin-rest/latest/resources/checkout) resource is now deprecated. For more information, refer to the [Developer changelog](/changelog/deprecation-of-checkout-apis).

We've also deprecated all endpoints on the [`Country`](/docs/api/admin-rest/latest/resources/country) and [`Province`](/docs/api/admin-rest/latest/resources/province) resources. For a complete list of affected endpoints, and the GraphQL type equivalents to use instead, refer to the [Developer changelog](/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api).

### [Anchor to Filtering customers](/docs/api/release-notes/previous-versions/2024-07#filtering-customers)Filtering customers

The following [`customer`](/docs/api/customer/latest/queries/customer) query filters in the [search syntax](/docs/api/usage/search-syntax) have been deprecated:

* `accepts_marketing`
* `city`
* `company`
* `country`
* `customer_date`
* `email_marketing_state`
* `last_abandoned_order_date`
* `order_date`
* `orders_count`
* `province`
* `sms_marketing_state`
* `state`
* `tag`
* `tag_note`
* `territory_code`
* `total_spent`

You can filter customers by these attributes using [segments](/docs/apps/build/marketing-analytics/customer-segments) instead.

### [Anchor to Inventory item data](/docs/api/release-notes/previous-versions/2024-07#inventory-item-data)Inventory item data

Prior to API version 2024-07, you could send inventory item data using [`ProductVariant`](/docs/api/admin-graphql/2024-04/objects/ProductVariant#mutations) mutations or on the [`InventoryItemUpdate`](/docs/api/admin-graphql/2024-04/mutations/inventoryItemUpdate) mutation. Each of these places has a different input object type with very similar fields, and with some fields showing up in one mutation instead of the other.

As of API version 2024-07, the two input types are unified. [`InventoryItemInput`](/docs/api/admin-graphql/latest/input-objects/InventoryItemInput) is now the input object type on the [`inventoryItemUpdate`](/docs/api/admin-graphql/latest/mutations/inventoryItemUpdate) mutation instead of the [`InventoryItemUpdateInput`](/docs/api/admin-graphql/latest/input-objects/InventoryItemUpdateInput) input object.

### [Anchor to Location object](/docs/api/release-notes/previous-versions/2024-07#location-object)Location object

The [`Location`](/docs/api/admin-graphql/latest/objects/Location) object is now gated by the `read_locations` access scope. If you attempt to read the `Location` object without the `read_locations` access scope, then an access denied error is returned.

### [Anchor to Marketing activity improvements](/docs/api/release-notes/previous-versions/2024-07#marketing-activity-improvements)Marketing activity improvements

You can now use the `urlParameterValue` field as a tracking parameter in the [`marketingActivityCreateInput`](/docs/api/admin-graphql/latest/input-objects/MarketingActivityCreateInput#field-marketingactivitycreateinput-urlparametervalue) and [`marketingActivityUpdateInput`](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateInput#field-marketingactivityupdateinput-urlparametervalue) input objects. This field is currently only available to select partners. Most partners should continue to use UTMs for tracking parameters.

Additionally, the [`MarketingActivityUserError`](/docs/api/admin-graphql/latest/objects/MarketingActivityUserError) enum is now a required type on the `userError` field for the `marketingEngagementCreate` mutation.

### [Anchor to Metafield access controls](/docs/api/release-notes/previous-versions/2024-07#metafield-access-controls)Metafield access controls

Apps can now query the [`access`](/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-metafielddefinition-access) field of metafield definitions that [they have access to but don't own](/docs/apps/build/custom-data/ownership). Previously, an `AuthorizationError` error was returned when accessing the field for metafield definitions that an app didn't have permissions to manage.

Note

Querying the [`grants`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) field on the `MetafieldAccess` object still requires permissions to manage the metafield definition and an error is returned if an app queries the field with insufficient permissions.

**Note:**

Querying the [`grants`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) field on the `MetafieldAccess` object still requires permissions to manage the metafield definition and an error is returned if an app queries the field with insufficient permissions.

The `admin` and `storefront` fields on the [`MetafieldAccess`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) object now return values in more cases instead of `null`. For example, metafields that don't have associated access grants return `PUBLIC_READ_WRITE` for `admin` access and `LEGACY_LIQUID_ONLY` for `storefront`. In addition, definitions that were created with a storefront access of `NONE` now return `NONE` instead of `null`. As of API version 2024-07, you can set `PUBLIC_READ_WRITE` as the `admin` access control.

Additionally, the `admin` and `storefront` fields on the [`MetafieldAccessInput`](/docs/api/admin-graphql/latest/input-objects/MetafieldAccessInput) input object now use dedicated input enum types, [`MetafieldAdminAccessInput`](/docs/api/admin-graphql/latest/enums/MetafieldAdminAccessInput) and [`MetafieldStorefrontAccessInput`](/docs/api/admin-graphql/latest/enums/MetafieldStorefrontAccessInput), respectively.

The following new types are available:

New types associated with metafield access controls

| Name | Type | Change |
| --- | --- | --- |
| `PUBLIC_READ_WRITE` | Value | Added to the `MetafieldAdminAccess` enum |
| `LEGACY_LIQUID_ONLY` | Value | Added to the `MetafieldStorefrontAccess` enum |
| `MetafieldAdminAccessInput` | Enum | Added |
| `MetafieldStorefrontAccessInput` | Enum | Added |

### [Anchor to Payment method names](/docs/api/release-notes/previous-versions/2024-07#payment-method-names)Payment method names

Previously, the [`PaymentCustomizationPaymentMethod`](/docs/api/functions/reference/payment-customization/graphql/common-objects/paymentcustomizationpaymentmethod?api%5Bversion%5D=2024-07) object returned multiple payment methods with the name "Shopify Payments" when a store has wallets enabled through Shopify Payments (for example, Apple Pay or Google Pay). This made it impossible for app developers to target the credit card or a specific wallet option for hide, rename, or move operations.

To fix this issue, we've changed the `name` value for wallets to the following values:

| Payment method | API version 2024-04 and lower | API version 2024-07 and higher |
| --- | --- | --- |
| Credit card | `"Shopify Payments"` | `"Shopify Payments"` |
| Apple Pay | `"Shopify Payments"` | `"Apple Pay"` |
| Google Pay | `"Shopify Payments"` | `"Google Pay"` |
| Meta Pay | `"Shopify Payments"` | `"Meta Pay"` |
| Shop Pay | `"Shopify Payments"` | `"Shop Pay"` |

### [Anchor to Product feed variant images](/docs/api/release-notes/previous-versions/2024-07#product-feed-variant-images)Product feed variant images

As of API version 2024-07, the variant image field in the `PRODUCT_FEEDS_INCREMENTAL_SYNC` and `PRODUCT_FEEDS_FULL_SYNC` [webhook subscription topics](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic) won't return an image unless one has been set. Previously, the variant image field would return the product's first image when an image wasn't explicitly set for the variant.

If this change doesn't work for your use case, then you can replicate the old behavior by assigning the first product image to the variant.

### [Anchor to Product variants](/docs/api/release-notes/previous-versions/2024-07#product-variants)Product variants

We've removed several fields on product variants that are duplicates of linked inventory items. For a complete list of changes to the GraphQL Admin API, and to learn more about the types that you can use instead, refer to the [developer changelog](/changelog/product-variant-field-cleanup).

### [Anchor to Product taxonomy](/docs/api/release-notes/previous-versions/2024-07#product-taxonomy)Product taxonomy

We've deprecated the `allProductCategories` field on the `Shop` object. Use the [`allProductCategoriesList`](/docs/api/admin-graphql/latest/objects/Shop#field-shop-allproductcategorieslist) field on the `Shop` object instead.

### [Anchor to Refunds](/docs/api/release-notes/previous-versions/2024-07#refunds)Refunds

Shopify's suggestion for a refund is now inclusive of payable charges, such as exchange items and fees, alongside returns.

The [`Return.suggestedRefund`](/docs/api/admin-graphql/latest/objects/Return#field-return-suggestedrefund) query and [`ReturnRefund`](/docs/api/admin-graphql/latest/mutations/returnRefund) mutation now have a different expectation on the refund amount. The refund amount considers exchange line items and fees on the return, as well as any outstanding amount owed by the buyer on an order. Previously, the refund amount logic only accounted for return line items.

### [Anchor to Removals of types and fields](/docs/api/release-notes/previous-versions/2024-07#removals-of-types-and-fields)Removals of types and fields

We've removed the following types and fields from the GraphQL Admin API:

Removals of types and fields from the GraphQL Admin API

| Name | Type | Change |
| --- | --- | --- |
| `ShippingLabel` | Object | [Removed](/docs/api/admin-graphql/latest/objects/ShippingLabel). |
| `location` field | `Order` object | Removed. Use the `retailLocation` field on the `Order` object instead. |
| `order` field | `CalculatedOrder` object | Removed. Use the `originalOrder` field on the `CalculatedOrder` object instead. |
| `productBased` field | `FulfillmentService` object | [Removed](/docs/api/admin-graphql/latest/objects/FulfillmentService). Non-product based fulfillment services are no longer supported. |

We've removed the following types and fields from the Storefront API:

Removals of types and fields from the Storefront API

| Name | Type | Change |
| --- | --- | --- |
| `ShopPayPaymentRequestContactFieldInput` | Input object | Removed. Shipping address is now read from the payment method. |
| `shippingAddress` field | `ShopPayPaymentRequestInput` input object | Removed. Shipping address is now read from the payment method. |
| `amount` field | `ShopPayPaymentRequestLineItemInput` input object | Removed. Use the `finalLinePrice` field instead. |
| `amount` field | `ShopPayPaymentRequestLineItem` object | Removed. Use the `finalLinePrice` field instead. |

### [Anchor to ShopifyQL](/docs/api/release-notes/previous-versions/2024-07#shopifyql)ShopifyQL

We've deprecated the [`shopifyqlQuery`](/docs/api/admin-graphql/latest/queries/shopifyqlQuery) query. Use the [GraphQL Admin API](/docs/api/admin-graphql) instead to extract data for your use cases.

### [Anchor to Sorting customers](/docs/api/release-notes/previous-versions/2024-07#sorting-customers)Sorting customers

The following [`CustomerSortKeys`](/docs/api/admin-graphql/latest/enums/CustomerSortKeys) are now deprecated:

* `LAST_ORDER_DATE`
* `ORDERS_COUNT`
* `TOTAL_SPENT`

You can order customers by these attributes if you filter customers using [segments](/docs/apps/build/marketing-analytics/customer-segments).

### [Anchor to Synchronous input improvements for ,[object Object], mutation](/docs/api/release-notes/previous-versions/2024-07#synchronous-input-improvements-for-productset-mutation)Synchronous input improvements for `productSet` mutation

The [`productSet`](/docs/api/admin-graphql/latest/mutations/productSet) mutation now defaults to running synchronously unless the input parameter `synchronous` is set to `false`.

We've also increased the input limit on product variants to the existing asynchronous limit. API versions prior to 2024-07 had a limit of 100 variants. You should set `synchronous` to `false` if you need to consider input complexity / size, or are experiencing timeouts.

### [Anchor to Webhook sub-topics](/docs/api/release-notes/previous-versions/2024-07#webhook-sub-topics)Webhook sub-topics

The `subTopic` field has been removed from the [`WebhookSubscription`](/docs/api/admin-graphql/latest/objects/WebhookSubscription) object. Use the [`filter`](/docs/api/admin-graphql/latest/objects/WebhookSubscription#field-webhooksubscription-filter) field instead.

### [Anchor to Writing metafield values](/docs/api/release-notes/previous-versions/2024-07#writing-metafield-values)Writing metafield values

You can now use the [`metafieldsSet`](/docs/api/customer/latest/mutations/metafieldsSet) mutation to assign metafield values on [`Customer`](/docs/api/customer/latest/objects/Customer), [`Order`](/docs/api/customer/latest/objects/Order), [`Company`](/docs/api/customer/latest/objects/Company), and [`CompanyLocation`](/docs/api/customer/latest/objects/CompanyLocation) objects.

As part of this change, the Customer Account API needs to be granted explicit read or read/write access to metafield definitions to have access to metafield values. This represents a breaking change because as of API version 2024-07, metafield definitions without [access permissions](#metafield-access-controls) will not be available to the Customer Account API.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2024-07#graphql-admin-api-changes)GraphQL Admin API changes

Version 2024-07 of the GraphQL Admin API introduces the following changes:

### [Anchor to Billing attempts](/docs/api/release-notes/previous-versions/2024-07#billing-attempts)Billing attempts

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

Similar to creating a new order through checkout, the availability of inventory is now checked during the billing attempt process.

Where product variants are configured to [prevent overselling](https://help.shopify.com/manual/products/inventory/getting-started-with-inventory/selling-when-out-of-stock) and one or more items in the contract are out of stock, then the billing attempt will fail with the new [`INSUFFICIENT_INVENTORY`](/docs/api/admin-graphql/latest/enums/SubscriptionBillingAttemptErrorCode#value-insufficientinventory) error code.

Learn more about [subscription contracts and billing attempts](/docs/apps/build/purchase-options/subscriptions/contracts/build-a-subscription-contract#step-4-create-a-billing-attempt).

### [Anchor to Cart-level discounts](/docs/api/release-notes/previous-versions/2024-07#cart-level-discounts)Cart-level discounts

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The `discountedPriceSet` and `discountedPrice` fields on the [`ShippingLine`](/docs/api/admin-graphql/2023-07/objects/ShippingLine) object now include cart-level discounts applied to an order, including the free shipping discount, when calculating the discounted price.

In API versions prior to 2024-07, you needed to subtract the `discountAllocations` from `discountedPriceSet` or `discountedPrice` fields to get an accurate value. If you do this in API version 2024-07 and higher, then you'll subtract the same discount twice.

### [Anchor to Cash transactions](/docs/api/release-notes/previous-versions/2024-07#cash-transactions)Cash transactions

You can now query the cash transactions that are associated with each cash tracking session. The new [`cashTransactions`](/docs/api/admin-graphql/latest/objects/CashTrackingSession#connection-cashtransactions) connection returns all of the cash order transactions that affected the amount in the cash drawer during a cash tracking session.

### [Anchor to Checkout branding](/docs/api/release-notes/previous-versions/2024-07#checkout-branding)Checkout branding

You can use the [`checkoutBrandingUpsert`](/docs/api/admin-graphql/latest/mutations/checkoutBrandingUpsert) mutation to configure the styling and visibility of dividers in checkout.

With this change, the dividers below the header, above the footer, between the main and order summary columns, and between sections in the main column can now be customized with visibility, style, and width controls.

The following new types are available:

New types related to checkout branding

| Name | Type | Change |
| --- | --- | --- |
| `divided` | Field | Added to `CheckoutBrandingFooterInput` input object |
| `divided` | Field | Added to `CheckoutBrandingFooter` object |
| `divided` | Field | Added to `CheckoutBrandingHeaderInput` input object |
| `divided` | Field | Added to `CheckoutBrandingHeader` object |

### [Anchor to Checkout profiles](/docs/api/release-notes/previous-versions/2024-07#checkout-profiles)Checkout profiles

You can now query the [`typOspPagesActive`](/docs/api/admin-graphql/latest/objects/CheckoutProfile#field-checkoutprofile-typosppagesactive) field on the `CheckoutProfiles` object. The `typOspPagesActive` field returns the status of the [**Thank you** and **Order status** pages](/docs/apps/build/checkout/thank-you-order-status) on a checkout profile, providing insight as to whether the pages have enabled [Shopify Extensions in Checkout](https://help.shopify.com/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

If `typOspPagesActive` is `true`, then both the **Thank you** and **Order status** pages have enabled Shopify Extensions in Checkout, and render the appropriate [checkout UI extensions](/docs/api/checkout-ui-extensions) while also making use of [web pixel extensions](/docs/apps/build/marketing-analytics/pixels), and [Functions](/docs/api/functions/current). If `typOspPagesActive` is `false`, then the **Thank you** and **Order status** pages still use scripts and other deprecated features.

### [Anchor to Combined listings](/docs/api/release-notes/previous-versions/2024-07#combined-listings)Combined listings

[Combined listings](/docs/apps/build/product-merchandising/combined-listings) bring together products that are merchandised by an option, such as color, model, or dimension, for enhanced display in the product details page.

As of API version 2024-07, you can use the GraphQL Admin API to [manage combined listings](/docs/apps/build/product-merchandising/combined-listings/build-for-combined-listings).

### [Anchor to Data sales and sharing opt-outs](/docs/api/release-notes/previous-versions/2024-07#data-sales-and-sharing-opt-outs)Data sales and sharing opt-outs

We've added the [`dataSaleOptOut`](/docs/api/admin-graphql/latest/mutations/dataSaleOptOut) mutation, which opts a customer out of data sales and sharing, and supports compliance with US state laws like CCPA and CPRA. The `dataSaleOptOut` mutation also applies the opt-out to the [Customer Privacy API](/docs/api/customer-privacy).

We've also added the [`dataSaleOptOut`](/docs/api/admin-graphql/latest/objects/Customer#field-customer-datasaleoptout) field to the `Customer` object.

To learn more about data sales and sharing opt-outs, refer to [Configuring customer privacy settings](https://help.shopify.com/manual/privacy-and-security/privacy/customer-privacy-settings/privacy-settings).

### [Anchor to Delivery promise](/docs/api/release-notes/previous-versions/2024-07#delivery-promise)Delivery promise

We've added the [`DeliveryPromiseProvider`](/docs/api/admin-graphql/latest/objects/DeliveryPromiseProvider) object, which represents an entity, such as a third-party service, that can provide delivery estimates on behalf of a store.

Each `DeliveryPromiseProvider` object is associated with a shop [`Location`](/docs/api/admin-graphql/latest/objects/Location).

A `DeliveryPromiseProvider` object can be created or updated using the [`deliveryPromiseProviderUpsert`](/docs/api/admin-graphql/latest/mutations/deliveryPromiseProviderUpsert) mutation, and retrieved using the [`deliveryPromiseProvider`](/docs/api/admin-graphql/latest/queries/deliveryPromiseProvider) query.

### [Anchor to Discounts](/docs/api/release-notes/previous-versions/2024-07#discounts)Discounts

[`DraftOrderInput`](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput) now accepts [`discountCodes`](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#field-draftorderinput-discountcodes), [`acceptAutomaticDiscounts`](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#field-draftorderinput-acceptautomaticdiscounts), and [`allowDiscountCodesInCheckout`](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#field-draftorderinput-allowdiscountcodesincheckout). These optional input fields allow you to apply discount codes to a draft order and decide whether to accept automatic discounts when a [draft order is calculated](/docs/api/admin-graphql/latest/mutations/draftOrderCalculate).

We've also added the [`platformDiscounts`](/docs/api/admin-graphql/latest/objects/DraftOrder#field-draftorder-platformdiscounts) field which provides details about how the platform discount has been allocated across the draft order line items, the discount type, its name, and more.

The following new types are available:

New types related to discounts

| Name | Type | Change |
| --- | --- | --- |
| `platformDiscounts` | Field | Added to `DraftOrder` object |
| `discountCodes` | Field | Added to `DraftOrder` object |
| `acceptAutomaticDiscounts` | Field | Added to `DraftOrder` object |
| `allowDiscountCodesInCheckout` | Field | Added to `DraftOrder` object |
| `warnings` | Field | Added to `DraftOrder` object |
| `DraftOrderDiscountNotAppliedWarning` | Object | Added |
| `DraftOrderPlatformDiscountAllocation` | Object | Added |
| `DraftOrderPlatformDiscount` | Object | Added |
| `DraftOrderWarning` | Object | Added |
| `platformDiscounts` | Field | Added to `CalculatedDraftOrder` object |
| `discountCodes` | Field | Added to `CalculatedDraftOrder` object |
| `acceptAutomaticDiscounts` | Field | Added to `CalculatedDraftOrder` object |
| `warnings` | Field | Added to `CalculatedDraftOrder` object |
| `approximateDiscountedUnitPriceSet` | Field | Added to `DraftOrderLineItem` object |
| `DraftOrderPlatformDiscountAllocationTarget` | Union | Added |

### [Anchor to Duplicate product variant values](/docs/api/release-notes/previous-versions/2024-07#duplicate-product-variant-values)Duplicate product variant values

The [`DUPLICATE_VALUE`](/docs/api/admin-graphql/latest/enums/ProductSetUserErrorCode#value-duplicatedvalue) error code has been added to the `ProductSetUserErrorCode` enum.

The `id` field on the [`ProductVariantSetInput`](/docs/api/admin-graphql/latest/input-objects/ProductVariantSetInput) input object now has validation support to prevent duplicate values. This enhancement ensures that there are no collisions when updating variants.

### [Anchor to Exchanges](/docs/api/release-notes/previous-versions/2024-07#exchanges)Exchanges

You can now use the GraphQL Admin API to interact with exchanges.

The [`returnCreate`](/docs/api/admin-graphql/latest/mutations/returnCreate) mutation can now take exchange line items with optional discounts, return shipping fees, and restocking fees to be applied to return lines. A return with exchange line items will also create a new [`FulfillmentOrder`](/docs/api/admin-graphql/latest/objects/FulfillmentOrder) for the new items to be sent to the customer.

Note

Canceling a return does affect the fulfillment of exchange items. [Learn more about how exchanges are processed](https://help.shopify.com/manual/orders/refunds-returns/creating-returns#restock-and-fulfill).

**Note:**

Canceling a return does affect the fulfillment of exchange items. [Learn more about how exchanges are processed](https://help.shopify.com/manual/orders/refunds-returns/creating-returns#restock-and-fulfill).

You can use the [`returnLineItemRemoveFromReturn`](/docs/api/admin-graphql/latest/mutations/returnLineItemRemoveFromReturn) mutation to remove return lines from a return. With [returns creating sales](https://shopify.dev/changelog/return-mutation-will-update-sales-previously-unchanged-until-time-of-refund), removing a return line from a return will also reversely impact return sales.

Additionally, you can use the [`returnCalculate`](/docs/api/admin-graphql/latest/queries/returnCalculate) query to calculate financials before return creation, including inputs for return lines, exchange lines, fees and discounts. [Learn how to use the `returnCalculate` query](/docs/apps/build/orders-fulfillment/returns-apps/build-return-management#step-2-optional-calculate-return-financials).

The following new types are available:

New types related to exchanges

| Name | Type | Change |
| --- | --- | --- |
| `CalculateExchangeLineItemInput` | Input object | Added |
| `CalculateReturnInput` | Input object | Added |
| `CalculateReturnLineItemInput` | Input object | Added |
| `ExchangeLineItemAppliedDiscountInput` | Input object | Added |
| `ExchangeLineItemAppliedDiscountValueInput` | Input object | Added |
| `ExchangeLineItemInput` | Input object | Added |
| `RestockingFeeInput` | Input object | Added |
| `ReturnEditSetRestockingFeeInput` | Input object | Added |
| `ReturnLineItemRemoveFromReturnInput` | Input object | Added |
| `ReturnShippingFeeInput` | Input object | Added |
| `exchangeLineItems` | Field | Added to `ReturnInput` input object |
| `returnShippingFee` | Field | Added to `ReturnInput` input object |
| `restockingFee` | Field | Added to `ReturnLineItemInput` input object |
| `CalculatedExchangeLineItem` | Object | Added |
| `CalculatedRestockingFee` | Object | Added |
| `CalculatedReturnFee` | Object | Added |
| `CalculatedReturnLineItem` | Object | Added |
| `CalculatedReturnShippingFee` | Object | Added |
| `CalculatedReturn` | Object | Added |
| `ReturnLineItemRemoveFromReturn` | Mutation | Added |

### [Anchor to Filtering customers](/docs/api/release-notes/previous-versions/2024-07#filtering-customers)Filtering customers

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The following [`customer`](/docs/api/customer/latest/queries/customer) query filters in the [search syntax](/docs/api/usage/search-syntax) have been deprecated:

* `accepts_marketing`
* `city`
* `company`
* `country`
* `customer_date`
* `email_marketing_state`
* `last_abandoned_order_date`
* `order_date`
* `orders_count`
* `province`
* `sms_marketing_state`
* `state`
* `tag`
* `tag_note`
* `territory_code`
* `total_spent`

You can filter customers by these attributes using [segments](/docs/apps/build/marketing-analytics/customer-segments) instead.

### [Anchor to Filter parameters for webhook subscriptions](/docs/api/release-notes/previous-versions/2024-07#filter-parameters-for-webhook-subscriptions)Filter parameters for webhook subscriptions

When you create, update, or query a webhook subscription, you can now include a filter parameter. Filter parameters, which are specified using [Shopify search syntax](/docs/api/usage/search-syntax), allow you to specify conditions as to when webhooks should be emitted for a subscription.

### [Anchor to Fulfillment constraint rules](/docs/api/release-notes/previous-versions/2024-07#fulfillment-constraint-rules)Fulfillment constraint rules

We've added the [`MAXIMUM_FULFILLMENT_CONSTRAINT_RULES_REACHED`](/docs/api/admin-graphql/latest/enums/FulfillmentConstraintRuleCreateUserErrorCode#value-maximumfulfilllmentconstraintrulesreached) error code to the `fulfillmentConstraintRuleCreate` mutation. The error code is returned when you add more than a maximum of ten fulfillment constraint rules to a store.

### [Anchor to Fulfillment orders](/docs/api/release-notes/previous-versions/2024-07#fulfillment-orders)Fulfillment orders

You can now access assigned fulfillment orders from the [`assignedFulfillmentOrders`](/docs/api/admin-graphql/latest/objects/queryroot#connection-assignedfulfillmentorders) connection on the `QueryRoot` object instead of from the pre-existing [`assignedFulfillmentOrders`](/docs/api/admin-graphql/latest/objects/Shop#connection-assignedfulfillmentorders) connection on the `Shop` object. This change includes the deprecation of the `Shop.assignedFulfillmentOrders` query in favour of the newly added `QueryRoot.assignedFulfillmentOrders` query.

The [`DeliveryMethodType`](/docs/api/admin-graphql/latest/enums/DeliveryMethodType) enum also now includes the `PICKUP_POINT` value to identify [fulfillment orders](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-fulfillmentorder-deliverymethod) containing deliveries to pickup point locations.

[Learn how to generate pickup point options](/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points).

### [Anchor to Fulfillment order line items](/docs/api/release-notes/previous-versions/2024-07#fulfillment-order-line-items)Fulfillment order line items

The [`variant`](/docs/api/admin-graphql/latest/objects/FulfillmentOrderLineItem#field-fulfillmentorderlineitem-variant) field has been added to the `FulfillmentOrderLineItem` object.

The field enables order management apps to reference the specific product details that are related to each fulfillment order line item without needing to directly compare SKUs in the order line items.

[Learn more about order management apps](/docs/apps/build/orders-fulfillment#order-management-apps).

### [Anchor to GraphQL completeness](/docs/api/release-notes/previous-versions/2024-07#graphql-completeness)GraphQL completeness

We've added new types to the GraphQL Admin API to provide parity with the following REST resources: [`CarrierService`](/docs/api/admin-rest/latest/resources/carrierservice), [`Customer`](/docs/api/admin-rest/latest/resources/customer), [`Fulfillment`](/docs/api/admin-rest/latest/resources/fulfillment), [`FulfillmentEvent`](/docs/api/admin-rest/latest/resources/fulfillmentevent), [`FulfillmentService`](/docs/api/admin-rest/latest/resources/fulfillmentservice), [`InventoryItem`](/docs/api/admin-rest/latest/resources/inventoryitem), [`Location`](/docs/api/admin-rest/latest/resources/location), [`Order`](/docs/api/admin-rest/latest/resources/order), and [`Product`](/docs/api/admin-rest/latest/resources/product).

New types on the GraphQL Admin API

| Name | Type | Change |
| --- | --- | --- |
| `DeliveryCarrierServiceCreateInput` | Input object | Added |
| `DeliveryCarrierServiceUpdateInput` | Input object | Added |
| `carrierServiceCreate` | Mutation | Added |
| `carrierServiceUpdate` | Mutation | Added |
| `carrierServiceDelete` | Mutation | Added |
| `active` | Field | Added to the `DeliveryCarrierService` object |
| `supportsServiceDiscovery` | Field | Added to the `DeliveryCarrierService` object |
| `callbackUrl` | Field | Added to the `DeliveryCarrierService` object |
| `carrierServices` | Field | Added to `QueryRoot` object |
| `customersCount` | Query | Added |
| `fulfillmentsCount` | Field | Added to `Order` object |
| `createdAt` | Field | Added to `FulfillmentEvent` object |
| `trackingSupport` | Field | Added to `FulfillmentService` object |
| `InventoryQuantityInput` | Input object | Added |
| `InventorySetQuantitiesInput` | Input object | Added |
| `inventorySetQuantities` | Mutation | Added |
| `locationsCount` | Query | Added |
| `ordersCount` | Query | Added |
| `staffMember` | Field | Added to `Order` object |
| `sourceName` | Field | Added to `Order` object |
| `orderDelete` | Mutation | Added |
| `OrderDeleteUserError` | Object | Added |
| `publishedProductsCount` | Query | Added |
| `webhookSubscriptionsCount` | Query | Added |

### [Anchor to Included fields on webhook subscriptions](/docs/api/release-notes/previous-versions/2024-07#included-fields-on-webhook-subscriptions)Included fields on webhook subscriptions

The [`includeFields`](/docs/api/admin-graphql/latest/objects/WebhookSubscription#field-webhooksubscription-includefields) that are specified on a webhook subscription are now available for all webhook topics. Previously, some webhook topics weren't respecting the `includeFields` configuration.

### [Anchor to Improvements to ShopPolicy object](/docs/api/release-notes/previous-versions/2024-07#improvements-to-shoppolicy-object)Improvements to ShopPolicy object

We've added new fields to the [`ShopPolicy`](/docs/api/admin-graphql/latest/objects/ShopPolicy) object. A `ShopPolicy` is a policy that a merchant has configured for their store, such as their refund or privacy policy.

New fields on the ShopPolicy object

| Name | Type | Change |
| --- | --- | --- |
| `title` | Field | Added |
| `createdAt` | Field | Added |
| `updatedAt` | Field | Added |

### [Anchor to Improvements to Shopify Payments payouts and balance transactions](/docs/api/release-notes/previous-versions/2024-07#improvements-to-shopify-payments-payouts-and-balance-transactions)Improvements to Shopify Payments payouts and balance transactions

We've made several improvements to Shopify Payments payouts and balance transactions in the GraphQL Admin API to provide parity with the REST Admin API:

* You can now use [Shopify's API search syntax](/docs/api/usage/search-syntax) to filter and sort payouts using the `sortKey` and `savedSearchId` parameters. This functionality allows you to efficiently search and organize payouts based on specific criteria such as `ledger_type`, `status`, `amount`, `currency`, and `issued_at`.
* You can now use the following new fields on the [`ShopifyPaymentsBalanceTransaction`](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsBalanceTransaction) object:

  + `sourceID`: Represents the ID of the object that led to the transaction.
  + `sourceOrderTransactionID`: Indicates the ID of the order transaction that triggered the balance transaction. If the `sourceType` is an adjustment, then this value is `null`.
  + `adjustmentOrderTransactions`: An array of associated order transactions that resulted in the balance transaction. If the `sourceType` is not an adjustment, then this array is null. Each object in the array includes `adjustmentReason`, which specifies the reason for the adjustment associated with the transaction. If the `sourceType` is not an adjustment, then value is `null`.

### [Anchor to Inventory error code](/docs/api/release-notes/previous-versions/2024-07#inventory-error-code)Inventory error code

The [`LEDGER_DOCUMENT_INVALID`](/docs/api/admin-graphql/latest/enums/InventorySetScheduledChangesUserErrorCode#value-ledgerdocumentinvalid) error code has been added to the [`inventorySetScheduledChanges`](/docs/api/admin-graphql/latest/mutations/inventorySetScheduledChanges) mutation.
The error code is returned when the `ledgerDocumentUri` provided is not a valid URI.

### [Anchor to Inventory item data](/docs/api/release-notes/previous-versions/2024-07#inventory-item-data)Inventory item data

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

Prior to API version 2024-07, you could send inventory item data using [`ProductVariant`](/docs/api/admin-graphql/2024-04/objects/ProductVariant#mutations) mutations or on the [`InventoryItemUpdate`](/docs/api/admin-graphql/2024-04/mutations/inventoryItemUpdate) mutation. Each of these places has a different input object type with very similar fields, and with some fields showing up in one mutation instead of the other.

As of API version 2024-07, the two input types are unified. [`InventoryItemInput`](/docs/api/admin-graphql/latest/input-objects/InventoryItemInput) is now the input object type on the [`inventoryItemUpdate`](/docs/api/admin-graphql/latest/mutations/inventoryItemUpdate) mutation instead of the [`InventoryItemUpdateInput`](/docs/api/admin-graphql/latest/input-objects/InventoryItemUpdateInput) input object.

### [Anchor to Location object](/docs/api/release-notes/previous-versions/2024-07#location-object)Location object

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The [`Location`](/docs/api/admin-graphql/latest/objects/Location) object is now gated by the `read_locations` access scope. If you attempt to read the `Location` object without the `read_locations` access scope, then an access denied error is returned.

### [Anchor to Marketing activity improvements](/docs/api/release-notes/previous-versions/2024-07#marketing-activity-improvements)Marketing activity improvements

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

You can now use the `urlParameterValue` field as a tracking parameter in the [`marketingActivityCreateInput`](/docs/api/admin-graphql/latest/input-objects/MarketingActivityCreateInput#field-marketingactivitycreateinput-urlparametervalue) and [`marketingActivityUpdateInput`](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateInput#field-marketingactivityupdateinput-urlparametervalue) input objects. This field is currently only available to select partners. Most partners should continue to use UTMs for tracking parameters.
Additionally, the [`MarketingActivityUserError`](/docs/api/admin-graphql/latest/objects/MarketingActivityUserError) enum is now a required type on the `userError` field for the `marketingEngagementCreate` mutation.

### [Anchor to Media included in product webhooks](/docs/api/release-notes/previous-versions/2024-07#media-included-in-product-webhooks)Media included in product webhooks

The [`PRODUCTS_CREATE`](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-productscreate) and [`PRODUCTS_UPDATE`](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic#value-productsupdate) webhook payloads now contain information about the media on a product.

### [Anchor to Media references](/docs/api/release-notes/previous-versions/2024-07#media-references)Media references

You can now use the [`fileUpdate`](/docs/api/admin-graphql/latest/mutations/fileUpdate) mutation to connect files to products.

The following new types are available:

New types associated with media references

| Name | Type | Change |
| --- | --- | --- |
| `referencesToAdd` | Field | Added to `FileUpdateInput` input object |
| `referencesToRemove` | Field | Added to `FileUpdateInput` input object |
| `UNSUPPORTED_FILE_REFERENCE` | Value | Added to `FilesErrorCode` enum |

### [Anchor to Menus on the Online Store](/docs/api/release-notes/previous-versions/2024-07#menus-on-the-online-store)Menus on the Online Store

You can now use the GraphQL Admin API to read and modify menus on the Online Store.

The following new types are available:

New types associated with menus on the Online Store

| Name | Type | Change |
| --- | --- | --- |
| `Menu` | Object | Added |
| `MenuItem` | Object | Added |
| `MenuItemCreateInput` | Input object | Added |
| `MenuItemUpdateInput` | Input object | Added |
| `menuCreate` | Mutation | Added |
| `menuUpdate` | Mutation | Added |
| `menuDelete` | Mutation | Added |
| `menu` | Query | Added |
| `menus` | Query | Added |
| `MenuItemType` | Enum | Added |
| `menu` | Field | Added to `QueryRoot` object |

### [Anchor to Metafield access controls](/docs/api/release-notes/previous-versions/2024-07#metafield-access-controls)Metafield access controls

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

Apps can now query the [`access`](/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-metafielddefinition-access) field of metafield definitions that [they have access to but don't own](/docs/apps/build/custom-data/ownership). Previously, an `AuthorizationError` error was returned when accessing the field for metafield definitions that an app didn't have permissions to manage.

Note

Querying the [`grants`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) field on the `MetafieldAccess` object still requires permissions to manage the metafield definition and an error is returned if an app queries the field with insufficient permissions.

**Note:**

Querying the [`grants`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) field on the `MetafieldAccess` object still requires permissions to manage the metafield definition and an error is returned if an app queries the field with insufficient permissions.

The `admin` and `storefront` fields on the [`MetafieldAccess`](/docs/api/admin-graphql/latest/objects/MetafieldAccess#field-metafieldaccess-grants) object now return values in more cases instead of `null`. For example, metafields that don't have associated access grants return `PUBLIC_READ_WRITE` for `admin` access and `LEGACY_LIQUID_ONLY` for `storefront`. In addition, definitions that were created with a storefront access of `NONE` now return `NONE` instead of `null`. As of API version 2024-07, you can set `PUBLIC_READ_WRITE` as the `admin` access control.

Additionally, the `admin` and `storefront` fields on the [`MetafieldAccessInput`](/docs/api/admin-graphql/latest/input-objects/MetafieldAccessInput) input object now use dedicated input enum types, [`MetafieldAdminAccessInput`](/docs/api/admin-graphql/latest/enums/MetafieldAdminAccessInput) and [`MetafieldStorefrontAccessInput`](/docs/api/admin-graphql/latest/enums/MetafieldStorefrontAccessInput), respectively.

The following new types are available:

New types associated with metafield access controls

| Name | Type | Change |
| --- | --- | --- |
| `PUBLIC_READ_WRITE` | Value | Added to the `MetafieldAdminAccess` enum |
| `LEGACY_LIQUID_ONLY` | Value | Added to the `MetafieldStorefrontAccess` enum |
| `MetafieldAdminAccessInput` | Enum | Added |
| `MetafieldStorefrontAccessInput` | Enum | Added |

### [Anchor to Metafield connections for OnlineStore objects](/docs/api/release-notes/previous-versions/2024-07#metafield-connections-for-onlinestore-objects)Metafield connections for OnlineStore objects

You can now use the `metafields` and `metafieldDefinitions` connections on the [`OnlineStoreArticle`](/docs/api/admin-graphql/latest/objects/OnlineStoreArticle#connections), [`OnlineStoreBlog`](/docs/api/admin-graphql/latest/objects/OnlineStoreBlog#connections), and [`OnlineStorePage`](/docs/api/admin-graphql/latest/objects/OnlineStorePage#connections) objects. Previously, you could only retrieve metafields and metafield definitions connections using the REST Admin API.

### [Anchor to Metafield definitions and constraints](/docs/api/release-notes/previous-versions/2024-07#metafield-definitions-and-constraints)Metafield definitions and constraints

We've added new types for reading standard conditional metafields and filtering metafield definitions by constraints:

New types for reading standard conditional metafields and filtering metafield definitions by constraints

| Name | Type | Change |
| --- | --- | --- |
| `MetafieldDefinitionConstraints` | Object | Added |
| `MetafieldDefinitionConstraintValue` | Object | Added |
| `MetafieldDefinitionConstraintSubtypeIdentifier` | Input object | Added |
| `MetafieldDefinitionConstraintStatus` | Enum | Added |
| `MetafieldDefinitionCreateUserError` | Enum | Added |
| `MetafieldDefinitionUpdateUserError` | Enum | Added |
| `constraints` | Field | Added to `MetafieldDefinition` object |
| `constraintSubtype` | Field | Added to `metafieldDefinitions` query |
| `constraintStatus` | Field | Added to `metafieldDefinitions` query |
| `constraintSubtype` | Argument | Added to `standardMetafieldDefinitionTemplates` query |
| `constraintStatus` | Argument | Added to `standardMetafieldDefinitionTemplates` query |
| `excludeActivated` | Argument | Added to `standardMetafieldDefinitionTemplates` query |

### [Anchor to Metafield error code](/docs/api/release-notes/previous-versions/2024-07#metafield-error-code)Metafield error code

We've added a new error code for mutations that set metafields. The [`INTERNAL_ERROR`](/docs/api/admin-graphql/latest/enums/MetafieldsSetUserErrorCode#value-internalerror) error code has been added to the `MetafieldsSetUserErrorCode` enum.

### [Anchor to Metafield JSON value](/docs/api/release-notes/previous-versions/2024-07#metafield-json-value)Metafield JSON value

The [`Metafield`](/docs/api/admin-graphql/latest/objects/Metafield) and [`MetaobjectField`](/docs/api/admin-graphql/latest/objects/MetaobjectField) objects now have a `jsonValue` field that returns the stored value as a `JSON` scalar.

By using the `jsonValue` field, metafield values that are stored as `JSON` strings don't have to be parsed on the client-side. The field is set for all metafield types and is also available in all [Function APIs](/docs/api/functions). The `jsonValue` field can be used in Function input queries to improve function performance and reduce the instructions needed to parse JSON metafield values, which are commonly used for function configuration.

### [Anchor to Metafields reserved namespaces](/docs/api/release-notes/previous-versions/2024-07#metafields-reserved-namespaces)Metafields reserved namespaces

We've added the [`RESERVED_NAMESPACE_ORPHANED_METAFIELDS`](/docs/api/admin-graphql/latest/enums/MetafieldDefinitionDeleteUserErrorCode) error code to the `MetafieldDefinitionDelete` mutation.

### [Anchor to Missing payment information for subscriptions](/docs/api/release-notes/previous-versions/2024-07#missing-payment-information-for-subscriptions)Missing payment information for subscriptions

The [`MISSING_CUSTOMER_PAYMENT_METHOD`](/docs/api/admin-graphql/latest/enums/SubscriptionDraftErrorCode#value-missingcustomerpaymentmethod) error code is now returned when payment information is missing on the [`subscriptionDraftCommit`](/docs/api/admin-graphql/latest/mutations/subscriptionDraftCommit) mutation.

### [Anchor to Metaobjects](/docs/api/release-notes/previous-versions/2024-07#metaobjects)Metaobjects

We've added the [`DISPLAY_NAME_CONFLICT`](/docs/api/admin-graphql/latest/enums/MetaobjectUserErrorCode#value-displaynameconflict) error code value to the `MetaobjectUserErrorCode` enum.

### [Anchor to Online store password protection](/docs/api/release-notes/previous-versions/2024-07#online-store-password-protection)Online store password protection

You can now retrieve information about the storefront password of an online store using the [`OnlineStorePasswordProtection`](/docs/api/admin-graphql/latest/objects/OnlineStorePasswordProtection) and [`OnlineStore`](/docs/api/admin-graphql/latest/objects/OnlineStore) objects.

### [Anchor to Optional fields on ProductSetInput](/docs/api/release-notes/previous-versions/2024-07#optional-fields-on-productsetinput)Optional fields on ProductSetInput

The [`variants`](/docs/api/admin-graphql/latest/input-objects/ProductSetInput#field-productsetinput-variants) and [`productOptions`](/docs/api/admin-graphql/latest/input-objects/ProductSetInput#field-productsetinput-productoptions) fields on the `ProductSetInput` input object are now optional. In API versions prior to 2024-07, the `variants` and `productOptions` fields were required.

### [Anchor to Order capture](/docs/api/release-notes/previous-versions/2024-07#order-capture)Order capture

Shopify Plus merchants using Shopify Payments are able to partially capture authorizations more than once. However, you might know that the capture you're about to perform will be the last one. To reflect this, we've added the [`finalCapture`](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#field-ordercaptureinput-finalcapture) field to the `orderCaptureInput` input object.

When you know you're capturing an authorization for the last time, setting the `finalCapture` field to `true` releases any uncaptured funds back to your customer. Doing so is likely to increase customer satisfaction and decrease the risk of chargebacks.

For merchants not on the Shopify Plus plan, the `finalCapture` field has no effect: these authorizations can only be captured once, and uncaptured funds are always returned immediately to the customer.

Currently, the `finalCapture` field only applies to transactions made through Shopify Payments. When capturing authorizations processed through other gateways, `finalCapture` must either be omitted, or set to `null`.

### [Anchor to Order transactions](/docs/api/release-notes/previous-versions/2024-07#order-transactions)Order transactions

You can now use the [`transactionsCount`](/docs/api/admin-graphql/latest/objects/Order#field-order-transactionscount) field on the `Order` object to return the number of transactions associated with a given order.

We've also added the [`authorizationExpiresAt`](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-ordertransaction-authorizationexpiresat) field on the `OrderTransaction` object. The `authorizationExpiresAt` field is available only to stores on a Shopify Plus plan and is populated only for Shopify Payments authorizations.

### [Anchor to Product bundles](/docs/api/release-notes/previous-versions/2024-07#product-bundles)Product bundles

We've added the [`customAttributes`](/docs/api/admin-graphql/latest/objects/LineItemGroup#field-lineitemgroup-customattributes) field on the `LineItemGroup` object, which allows you to query a list of attributes that represent custom features or special requests. A line item group is also known as a bundle.

Apps can now also do the following:

* Retrieve a bundle item's components on a draft order by using the `bundleComponents` field on the [`DraftOrderBundleLineItemComponentInput`](/docs/api/admin-graphql/latest/input-objects/DraftOrderBundleLineItemComponentInput#field-draftorderbundlelineitemcomponentinput-bundlecomponents) input object.
* Add a bundle item to a draft order by including the [`bundleComponents`](/docs/api/admin-graphql/latest/input-objects/DraftOrderInput#field-draftorderinput-bundlecomponents) field on the `draftOrderLineItemInput` input object.

Additionally, the [`CartTransform`](/docs/api/functions/reference/cart-transform/graphql/common-objects/carttransform) function now automatically runs on all draft orders.

[Learn more about bundles](/docs/apps/build/product-merchandising/bundles).

The following new types are available for creating and updating product bundles:

New types for creating and updating product bundles

| Name | Type | Change |
| --- | --- | --- |
| `ProductBundleComponentOptionSelectionValue` | Object | Added |
| `ProductBundleComponentOptionSelection` | Object | Added |
| `ProductBundleComponentQuantityOptionValue` | Object | Added |
| `ProductBundleComponentQuantityOption` | Object | Added |
| `ProductBundleComponent` | Object | Added |
| `ProductBundleOperation` | Object | Added |
| `ProductBundleMutationUserError` | Object | Added |
| `ProductBundleComponentInput` | Input object | Added |
| `ProductBundleComponentOptionSelectionInput` | Input object | Added |
| `ProductBundleComponentQuantityOptionInput` | Input object | Added |
| `ProductBundleComponentQuantityOptionValueInput` | Input object | Added |
| `ProductBundleCreateInput` | Input object | Added |
| `ProductBundleUpdateInput` | Input object | Added |
| `productBundleCreate` | Mutation | Added |
| `productBundleUpdate` | Mutation | Added |
| `ProductBundleComponentOptionSelectionStatus` | Enum | Added |
| `bundleComponents` | Field | Added to `Product` object |

### [Anchor to Product feed variant images](/docs/api/release-notes/previous-versions/2024-07#product-feed-variant-images)Product feed variant images

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

As of API version 2024-07, the variant image field in the `PRODUCT_FEEDS_INCREMENTAL_SYNC` and `PRODUCT_FEEDS_FULL_SYNC` [webhook subscription topics](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic) won't return an image unless one has been set. Previously, the variant image field would return the product's first image when an image wasn't explicitly set for the variant.

If this change doesn't work for your use case, then you can replicate the old behavior by assigning the first product image to the variant.

### [Anchor to Product options error code](/docs/api/release-notes/previous-versions/2024-07#product-options-error-code)Product options error code

The [`LINKED_METAFIELD_DEFINITION_NOT_FOUND`](/docs/api/admin-graphql/latest/enums/ProductOptionUpdateUserErrorCode#value-linkedmetafielddefinitionnotfound) value has been added to the `ProductOptionUpdateUserErrorCode` enum.

### [Anchor to Promise provider data](/docs/api/release-notes/previous-versions/2024-07#promise-provider-data)Promise provider data

You can now use the [`sourceReference`](/docs/api/admin-graphql/latest/objects/DeliveryMethod#field-deliverymethod-sourcereference) field on the `DeliveryMethod` object to return promise provider data associated with a delivery promise.

### [Anchor to Product query](/docs/api/release-notes/previous-versions/2024-07#product-query)Product query

You can now use the `published_at` filter on the [`product`](/docs/api/admin-graphql/latest/queries/product) query to determine the date and time when a product was published to the Online Store.

### [Anchor to Product taxonomy](/docs/api/release-notes/previous-versions/2024-07#product-taxonomy)Product taxonomy

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The following types now have a `category` field, which accepts the global ID (GID) of a taxonomy category that's specified by a merchant:

* [`ProductInput`](/docs/api/admin-graphql/unstable/input-objects/ProductInput#field-productinput-category) input object
* [`Shop`](/docs/api/admin-graphql/latest/objects/Shop#field-shop-allproductcategorieslist) object
* [`MetafieldReference`](/docs/api/admin-graphql/latest/unions/MetafieldReference#value-product) union

We've also deprecated the `allProductCategories` field on the `Shop` object. Use the [`allProductCategoriesList`](/docs/api/admin-graphql/latest/objects/Shop#field-shop-allproductcategorieslist) field on the `Shop` object instead.

### [Anchor to Product translations](/docs/api/release-notes/previous-versions/2024-07#product-translations)Product translations

You can now use the [`includesTranslations`](/docs/api/admin-graphql/latest/input-objects/ProductDuplicateAsyncInput#field-productduplicateasyncinput-includetranslations) field on the `ProductDuplicateAsyncInput` input object to specify whether to include translations when running the [`productDuplicateAsyncV2`](/docs/api/admin-graphql/latest/mutations/productDuplicateAsyncV2) mutation.

If `includesTranslations` is set to `true`, then all translations that are saved on the product, its variants, and its metafields are copied over to the new product.

### [Anchor to Product variants](/docs/api/release-notes/previous-versions/2024-07#product-variants)Product variants

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've removed several fields on product variants that are duplicates of linked inventory items. For a complete list of changes to the GraphQL Admin API, and to learn more about the types that you can use instead, refer to the [developer changelog](/changelog/product-variant-field-cleanup).

### [Anchor to Querying media in files](/docs/api/release-notes/previous-versions/2024-07#querying-media-in-files)Querying media in files

You can now use the [`files`](/docs/api/admin-graphql/latest/queries/files) query to retrieve 3D models and external videos.

The following new types are available:

Types associated with querying media in files

| Name | Type | Change |
| --- | --- | --- |
| `File` | Interface | Added to `Model3d` object |
| `File` | Interface | Added to `ExternalVideo` object |
| `MODEL_3D` | Value | Added to `FileContentType` enum |
| `EXTERNAL_VIDEO` | Value | Added to `FileContentType` enum |

### [Anchor to Removals of types and fields](/docs/api/release-notes/previous-versions/2024-07#removals-of-types-and-fields)Removals of types and fields

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've removed the following types and fields from the GraphQL Admin API:

Removals of types and fields from the GraphQL Admin API

| Name | Type | Change |
| --- | --- | --- |
| `ShippingLabel` | Object | [Removed](/docs/api/admin-graphql/latest/objects/ShippingLabel). |
| `location` field | `Order` object | Removed. Use the `retailLocation` field on the `Order` object instead. |
| `order` field | `CalculatedOrder` object | Removed. Use the `originalOrder` field on the `CalculatedOrder` object instead. |
| `productBased` field | `FulfillmentService` object | [Removed](/docs/api/admin-graphql/latest/objects/FulfillmentService). Non-product based fulfillment services are no longer supported. |

### [Anchor to Retail locations](/docs/api/release-notes/previous-versions/2024-07#retail-locations)Retail locations

You can now use the [`retailLocation`](/docs/api/admin-graphql/latest/objects/Order#field-order-retaillocation) field on the `Order` object to query the physical location where a retail order is created or completed.

### [Anchor to Refund line items](/docs/api/release-notes/previous-versions/2024-07#refund-line-items)Refund line items

You can now use the [`id`](/docs/api/admin-graphql/latest/objects/RefundLineItem#field-refundlineitem-id) field on the `RefundLineItem` object to return the global ID of the specified refund line item object.

### [Anchor to Refunds](/docs/api/release-notes/previous-versions/2024-07#refunds)Refunds

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

Shopify's suggestion for a refund is now inclusive of payable charges, such as exchange items and fees, alongside returns.

The [`Return.suggestedRefund`](/docs/api/admin-graphql/latest/objects/Return#field-return-suggestedrefund) query and [`ReturnRefund`](/docs/api/admin-graphql/latest/mutations/returnRefund) mutation now have a different expectation on the refund amount. The refund amount considers exchange line items and fees on the return, as well as any outstanding amount owed by the buyer on an order. Previously, the refund amount logic only accounted for return line items.

### [Anchor to Returns](/docs/api/release-notes/previous-versions/2024-07#returns)Returns

As of API version 2024-07, the [`Return.returnLineItems`](/docs/api/admin-graphql/latest/objects/Return#connection-returnlineitems) connection is an interface type. This change is designed to accommodate more diverse return item types in the future, and provides more flexibility in handling returns.

To maintain compatibility with existing implementations, adjust your queries to use an inline fragment. The following adjustment ensures that queries continue to function correctly with the new interface type:

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

returnLineItems(first: 30) {

edges {

cursor

node {

... on ReturnLineItem {

id

...ReturnLineItemAttributes

}

}

}

}

### [Anchor to Selling plans](/docs/api/release-notes/previous-versions/2024-07#selling-plans)Selling plans

Metafields are now supported on the [`SellingPlan`](/docs/api/admin-graphql/latest/objects/SellingPlan) object.

The following new types are available:

Types associated with metafields on selling plans

| Name | Type | Change |
| --- | --- | --- |
| `hasMetafields` | Interface | Added |
| `hasMetafieldDefinitions` | Interface | Added |
| `metafields` | Field | Added to `SellingPlanInput` input object |
| `SELLING_PLAN` | value | Added to `MetafieldOwnerType` enum |
| `INVALID_INPUT` | value | Added to `SellingPlanGroupUserErrorCode` enum |

### [Anchor to Set metafields using compare-and-swap (CAS)](/docs/api/release-notes/previous-versions/2024-07#set-metafields-using-compare-and-swap-cas)Set metafields using compare-and-swap (CAS)

You can now set metafields using compare-and-swap (CAS) with the [`compareDigest`](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#field-metafieldssetinput-comparedigest) field on the [`metafieldsSet`](/docs/api/admin-graphql/latest/mutations/metafieldsSet) mutation. By using CAS, you can properly handle concurrency requests.

### [Anchor to Shopify mobile apps](/docs/api/release-notes/previous-versions/2024-07#shopify-mobile-apps)Shopify mobile apps

As of API version 2024-07, we're introducing a new [`MobilePlatformApplication`](/docs/api/admin-graphql/latest/unions/MobilePlatformApplication) type. This type facilitates the development and operational integration of shared web credentials and app link systems for Shopify mobile apps on both iOS and Android platforms.

The following new types are available:

Types associated with Shopify mobile apps

| Name | Type | Change |
| --- | --- | --- |
| `AndroidApplication` | Object | Added |
| `AppleApplication` | Object | Added |
| `MobilePlatformApplicationCreateInput` | Input object | Added |
| `MobilePlatformApplication` | Union | Added |
| `mobilePlatformApplicationCreate` | Mutation | Added |
| `MobilePlatformApplicationDelete` | Mutation | Added |
| `MobilePlatformApplicationUpdate` | Mutation | Added |
| `MobilePlatformApplicationUserError` | Enum | Added |
| `mobilePlatformApplication` | Query | Added |
| `mobilePlatformApplications` | Query | Added |

### [Anchor to Shopify Payments balance transactions](/docs/api/release-notes/previous-versions/2024-07#shopify-payments-balance-transactions)Shopify Payments balance transactions

New types for Shopify Payments balance transactions

| Name | Type | Change |
| --- | --- | --- |
| `ShopifyPaymentsAssociatedOrder` | Object | Added |
| `ShopifyPaymentsBalanceTransactionAssociatedPayout` | Object | Added |
| `amount` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `fee` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `associatedOrder` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `sourceType` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `type` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `associatedPayout` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |
| `test` | Field | Added to `ShopifyPaymentsBalanceTransaction` object |

### [Anchor to ShopifyQL](/docs/api/release-notes/previous-versions/2024-07#shopifyql)ShopifyQL

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've deprecated the [`shopifyqlQuery`](/docs/api/admin-graphql/latest/queries/shopifyqlQuery) query. Use the [GraphQL Admin API](/docs/api/admin-graphql) instead to extract data for your use cases.

### [Anchor to Sorting customers](/docs/api/release-notes/previous-versions/2024-07#sorting-customers)Sorting customers

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The following [`CustomerSortKeys`](/docs/api/admin-graphql/latest/enums/CustomerSortKeys) are now deprecated:

* `LAST_ORDER_DATE`
* `ORDERS_COUNT`
* `TOTAL_SPENT`

You can order customers by these attributes if you filter customers using [segments](/docs/apps/build/marketing-analytics/customer-segments).

### [Anchor to Store credit at checkout](/docs/api/release-notes/previous-versions/2024-07#store-credit-at-checkout)Store credit at checkout

You can now use the [`StoreCreditAccount`](/docs/api/admin-graphql/latest/objects/storeCreditAccount) object to retrieve information about the monetary balance that can be redeemed at checkout for purchases in the store.

### [Anchor to Synchronous input improvement for productSet mutation](/docs/api/release-notes/previous-versions/2024-07#synchronous-input-improvement-for-productset-mutation)Synchronous input improvement for productSet mutation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The [`productSet`](/docs/api/admin-graphql/latest/mutations/productSet) mutation now defaults to running synchronously unless the input parameter `synchronous` is set to `false`.

We've also increased the input limit on product variants to the existing asynchronous limit. API versions prior to 2024-07 had a limit of 100 variants. You should set `synchronous` to `false` if you need to consider input complexity / size, or are experiencing timeouts.

### [Anchor to Tax collection improvements](/docs/api/release-notes/previous-versions/2024-07#tax-collection-improvements)Tax collection improvements

We've added 14 additional [`LocalizationExtensionsKey`](/docs/api/admin-graphql/latest/enums/LocalizationExtensionKey) values to support the collection of tax and shipping credentials in several new countries.

### [Anchor to Translatable content types](/docs/api/release-notes/previous-versions/2024-07#translatable-content-types)Translatable content types

You can now use the following metafield definition types to save link-related content:

* [`LINK`](/docs/api/admin-graphql/latest/enums/LocalizableContentType#value-link): A link consisting of an anchor text and URL
* [`LIST_LINK`](/docs/api/admin-graphql/latest/enums/LocalizableContentType#value-listlink): A list of link metafields

[Learn more about metafields](/docs/apps/build/custom-data/metafields).

### [Anchor to Validation status for shipping addresses](/docs/api/release-notes/previous-versions/2024-07#validation-status-for-shipping-addresses)Validation status for shipping addresses

You can now use the [`validationResultSummary`](/docs/api/admin-graphql/latest/objects/MailingAddress#field-mailingaddress-validationresultsummary) field on the `MailingAddress` object to query the validation status of a shipping address. Possible values are `ERROR`, `WARNING`, `NO_ISSUES`, and `NULL`. A `NULL` value indicates that the address has not undergone validation.

[Learn more about how Shopify validates customer addresses](https://help.shopify.com/manual/orders/manage-orders/shipping-address-validation).

### [Anchor to Webhook sub-topics](/docs/api/release-notes/previous-versions/2024-07#webhook-sub-topics)Webhook sub-topics

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The `subTopic` field has been removed from the [`WebhookSubscription`](/docs/api/admin-graphql/latest/objects/WebhookSubscription) object. Use the [`filter`](/docs/api/admin-graphql/latest/objects/WebhookSubscription#field-webhooksubscription-filter) field instead.

### [Anchor to Webhook topics](/docs/api/release-notes/previous-versions/2024-07#webhook-topics)Webhook topics

We've added the following new webhook topics to the GraphQL Admin API:

New webhook topics in the GraphQL Admin API

| Name | Description |
| --- | --- |
| `PRODUCT_FEEDS_FULL_SYNC_FINISH` | Triggers when a full sync finishes for a product feed |
| `CUSTOMER_ACCOUNT_SETTINGS_UPDATE` | Triggers when merchants change customer account settings |

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2024-07#rest-admin-api-changes)REST Admin API changes

Version 2024-07 of the REST Admin API introduces the following changes:

### [Anchor to Adjustment reason for Shopify Payments transactions](/docs/api/release-notes/previous-versions/2024-07#adjustment-reason-for-shopify-payments-transactions)Adjustment reason for Shopify Payments transactions

The Shopify Payments [`Transactions`](/docs/api/admin-rest/latest/resources/transactions) resource now returns the `adjustment_reason` property to describe the reason an adjustment was made.

### [Anchor to Deprecation of REST resources](/docs/api/release-notes/previous-versions/2024-07#deprecation-of-rest-resources)Deprecation of REST resources

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

The [`Checkout`](/docs/api/admin-rest/latest/resources/checkout) resource is now deprecated. For more information, refer to the [Developer changelog](/changelog/deprecation-of-checkout-apis).

We've also deprecated all endpoints on the [`Country`](/docs/api/admin-rest/latest/resources/country) and [`Province`](/docs/api/admin-rest/latest/resources/province) resources. For a complete list of affected endpoints, and the GraphQL type equivalents to use instead, refer to the [Developer changelog](/changelog/deprecation-notice-country-and-province-endpoints-in-admin-rest-api).

### [Anchor to New properties on the FulfillmentOrder resource](/docs/api/release-notes/previous-versions/2024-07#new-properties-on-the-fulfillmentorder-resource)New properties on the FulfillmentOrder resource

The following properties have been added to `delivery_method` property on the [`FulfillmentOrder`](/docs/api/admin-rest/latest/resources/fulfillmentorder) resource:

* `branded_promise`: The branded promise that was presented to the customer during checkout. For example, "Shop Promise".
* `additional_information`: The additional information to consider when performing the delivery.
* `service_code`: A reference to the shipping method.
* `source_reference`: The promise provider data associated with delivery promise.

### [Anchor to Order editing](/docs/api/release-notes/previous-versions/2024-07#order-editing)Order editing

The [`orders/edited`](/docs/api/admin-rest/latest/resources/webhook#event-topics-orders-edited) webhook payload now includes a `committed_at` field. You can use this field to identify when an edit to an order is finalized.

---

## [Anchor to Storefront API changes](/docs/api/release-notes/previous-versions/2024-07#storefront-api-changes)Storefront API changes

Version 2024-07 of the Storefront API introduces the following changes:

### [Anchor to Cart billing address](/docs/api/release-notes/previous-versions/2024-07#cart-billing-address)Cart billing address

You can now use the [`cartBillingAddressUpdate`](/docs/api/storefront/latest/mutations/cartbillingaddressupdate) mutation to associate a billing address with a cart.

### [Anchor to Cart error code](/docs/api/release-notes/previous-versions/2024-07#cart-error-code)Cart error code

The [`NOTE_TOO_LONG`](/docs/api/storefront/latest/enums/CartErrorCode#value-notetoolong) error code is now returned in cart mutations when a note exceeds the maximum limit of 5000 characters.

### [Anchor to Cart wallet preferences](/docs/api/release-notes/previous-versions/2024-07#cart-wallet-preferences)Cart wallet preferences

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've deprecated the following types:

* `walletPreferences` argument on the [`CartBuyerIdentityInput`](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput) input object
* `walletPreferences` field on the [`CartBuyerIdentity`](/docs/api/storefront/latest/objects/CartBuyerIdentity) object

  Use [`CartBuyerIdentityInput.preferences.wallet`](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput#field-cartbuyeridentityinput-preferences) instead.

### [Anchor to Checkout types removed](/docs/api/release-notes/previous-versions/2024-07#checkout-types-removed)Checkout types removed

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've removed checkout types from the Storefront API, following their [deprecation in the 2024-04 API version](/docs/api/release-notes/previous-versions/2024-04#deprecations-storefront-api-and-rest-admin-api).

For more information, refer to the [developer changelog](/changelog/deprecation-of-checkout-apis).

### [Anchor to Discount computations](/docs/api/release-notes/previous-versions/2024-07#discount-computations)Discount computations

We've added the [`targetType`](/docs/api/storefront/latest/interfaces/CartDiscountAllocation#field-cartdiscountallocation-targettype) field to the `CartDiscountAllocation` interface. The `targetType` field ensures comprehensive discount calculations, which are crucial for payment integrations.

### [Anchor to Gift cards](/docs/api/release-notes/previous-versions/2024-07#gift-cards)Gift cards

You can now manage gift cards on a cart in the following ways:

* **When creating a cart**: Add the `giftCardCodes` field to the [`CartInput`](/docs/api/storefront/latest/input-objects/cartinput) input object.
* **After a cart is created**: Run the [`cartGiftCardCodesUpdate`](/docs/api/storefront/latest/mutations/cartGiftCardCodesUpdate) mutation.
* **Querying for applied gift cards**: Use the [`appliedGiftCards`](/docs/api/storefront/latest/objects/Cart#field-cart-appliedgiftcards) field.

  The following new types are available:

  New types for managing gift cards on a cart

  | Name | Type | Change |
  | --- | --- | --- |
  | `cartGiftCardCodesUpdate` | Mutation | Added |
  | `giftCardCodes` | Field | Added to `CartInput` |
  | `appliedGiftCards` | Field | Added to `Cart` object |

### [Anchor to Removals of types and fields](/docs/api/release-notes/previous-versions/2024-07#removals-of-types-and-fields)Removals of types and fields

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

We've removed the following types and fields from the Storefront API:

Removals of types and fields from the Storefront API

| Name | Type | Change |
| --- | --- | --- |
| `ShopPayPaymentRequestContactFieldInput` | Input object | Removed. Shipping address is now read from the payment method. |
| `shippingAddress` field | `ShopPayPaymentRequestInput` input object | Removed. Shipping address is now read from the payment method. |
| `amount` field | `ShopPayPaymentRequestLineItemInput` input object | Removed. Use the `finalLinePrice` field instead. |
| `amount` field | `ShopPayPaymentRequestLineItem` object | Removed. Use the `finalLinePrice` field instead. |

### [Anchor to Shop Pay payment request checkouts](/docs/api/release-notes/previous-versions/2024-07#shop-pay-payment-request-checkouts)Shop Pay payment request checkouts

You can now use the following types to manage Shop Pay payment request checkouts:

New types for managing Shop Pay payment request checkouts

| Name | Type | Change |
| --- | --- | --- |
| `ShopPayPaymentRequestContactField` | Object | Added |
| `ShopPayPaymentRequestDeliveryMethod` | Object | Added |
| `ShopPayPaymentRequestDiscount` | Object | Added |
| `ShopPayPaymentRequestImage` | Object | Added |
| `ShopPayPaymentRequestReceipt` | Object | Added |
| `ShopPayPaymentRequestSession` | Object | Added |
| `ShopPayPaymentRequestShippingLine` | Object | Added |
| `ShopPayPaymentRequestTotalShippingPrice` | Object | Added |
| `ShopPayPaymentRequest` | Object | Added |
| `ShopPayPaymentRequestDeliveryMethodInput` | Input object | Added |
| `ShopPayPaymentRequestDiscountInput` | Input object | Added |
| `ShopPayPaymentRequestImageInput` | Input object | Added |
| `ShopPayPaymentRequestInput` | Input object | Added |
| `ShopPayPaymentRequestLineItemInput` | Input object | Added |
| `ShopPayPaymentRequestLineItem` | Input object | Added |
| `ShopPayPaymentRequestShippingLineInput` | Input object | Added |
| `ShopPayPaymentRequestTotalShippingPriceInput` | Input object | Added |
| `shopPayPaymentRequestSessionCreate` | Mutation | Added |
| `shopPayPaymentRequestSessionSubmit` | Mutation | Added |

### [Anchor to Single-use delivery addresses](/docs/api/release-notes/previous-versions/2024-07#single-use-delivery-addresses)Single-use delivery addresses

Carts now support single-use delivery addresses with the `oneTimeUse` field on the [DeliveryAddressInput](/docs/api/storefront/latest/input-objects/DeliveryAddressInput) input object.

You can use the `oneTimeUse` field to pass a delivery address that shouldn't be saved to the customer's account after checkout. For example, you might want to use this field for one-time gifting purposes.

---

## [Anchor to Shopify Function APIs changes](/docs/api/release-notes/previous-versions/2024-07#shopify-function-apis-changes)Shopify Function APIs changes

Version 2024-07 of the Shopify Function APIs introduces the following changes:

### [Anchor to Metafields support on selling plans](/docs/api/release-notes/previous-versions/2024-07#metafields-support-on-selling-plans)Metafields support on selling plans

The `HasMetafields` interface is now available on the `SellingPlan` object associated with each [Function API](/docs/api/functions#available-apis).

### [Anchor to Order Routing Location Rule API](/docs/api/release-notes/previous-versions/2024-07#order-routing-location-rule-api)Order Routing Location Rule API

We've added the `lines` field to the [`FulfillmentGroup`](/docs/api/functions/reference/order-routing-location-rule/graphql/common-objects/fulfillmentgroup?api%5Bversion%5D=2024-07) object. The `lines` field returns a list of cart lines containing information about the items that are part of the fulfillment group.

### [Anchor to Payment Customization API](/docs/api/release-notes/previous-versions/2024-07#payment-customization-api)Payment Customization API

API clients installed on Shopify Plus stores can now make use of the optional [`placements`](/docs/api/functions/reference/payment-customization/graphql/common-objects/hideoperation?api%5Bversion%5D=2024-07) argument in the `hide` operation. This allows you to explicitly hide payment methods from the accelerated checkout or payment selection.

[Learn more about payment customization functions](/docs/apps/build/checkout/payments).

### [Anchor to Payment method names](/docs/api/release-notes/previous-versions/2024-07#payment-method-names)Payment method names

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

Previously, the [`PaymentCustomizationPaymentMethod`](/docs/api/functions/reference/payment-customization/graphql/common-objects/paymentcustomizationpaymentmethod?api%5Bversion%5D=2024-07) object returned multiple payment methods with the name "Shopify Payments" when a store has wallets enabled through Shopify Payments (for example, Apple Pay or Google Pay). This made it impossible for app developers to target the credit card or a specific wallet option for hide, rename, or move operations.

To fix this issue, we've changed the `name` value for wallets to the following values:

| Payment method | API version 2024-04 and lower | API version 2024-07 and higher |
| --- | --- | --- |
| Credit card | "Shopify Payments" | "Shopify Payments" |
| Apple Pay | "Shopify Payments" | "Apple Pay" |
| Google Pay | "Shopify Payments" | "Google Pay" |
| Meta Pay | "Shopify Payments" | "Meta Pay" |
| Shop Pay | "Shopify Payments" | "Shop Pay" |

### [Anchor to Product Discount API](/docs/api/release-notes/previous-versions/2024-07#product-discount-api)Product Discount API

The Product Discount API now supports [`CartLineTarget`](/docs/api/functions/reference/product-discounts/graphql/common-objects/cartlinetarget) object, which enables you to apply discounts on specific cart lines. This functionality was historically only possible with Shopify Scripts.

You can use the `CartLineTarget` object to link discounts to attributed cart lines such as upsell products, free gifts with purchase, or buyer customized products.

---

## [Anchor to Customer Account API changes](/docs/api/release-notes/previous-versions/2024-07#customer-account-api-changes)Customer Account API changes

Version 2024-07 of the Customer Account API introduces the following changes:

### [Anchor to Financial status of an order](/docs/api/release-notes/previous-versions/2024-07#financial-status-of-an-order)Financial status of an order

You can now determine whether the financial status of an order is expired using the [`EXPIRED`](/docs/api/customer/latest/enums/OrderFinancialStatus#value-expired) value on the `OrderFinancialStatus` enum.

### [Anchor to Set metafields using compare-and-swap (CAS)](/docs/api/release-notes/previous-versions/2024-07#set-metafields-using-compare-and-swap-cas)Set metafields using compare-and-swap (CAS)

You can now set metafields using compare-and-swap (CAS) with the [`compareDigest`](/docs/api/customer/latest/input-objects/MetafieldsSetInput#field-metafieldssetinput-comparedigest) field on the [`metafieldsSet`](/docs/api/customer/latest/mutations/metafieldsSet) mutation. By using CAS, you can properly handle concurrency requests.

### [Anchor to Store credit at checkout](/docs/api/release-notes/previous-versions/2024-07#store-credit-at-checkout)Store credit at checkout

Customers who are [authenticated with a customer account](/docs/api/customer) can now review and spend their [store credit](/docs/api/customer/latest/objects/Customer#connection-storecreditaccounts) at checkout.

### [Anchor to Writing metafield values](/docs/api/release-notes/previous-versions/2024-07#writing-metafield-values)Writing metafield values

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-07#breaking)Breaking

You can now use the [`metafieldsSet`](/docs/api/customer/latest/mutations/metafieldsSet) mutation to assign metafield values on [`Customer`](/docs/api/customer/latest/objects/Customer), [`Order`](/docs/api/customer/latest/objects/Order), [`Company`](/docs/api/customer/latest/objects/Company), and [`CompanyLocation`](/docs/api/customer/latest/objects/CompanyLocation) objects.

As part of this change, the Customer Account API needs to be granted explicit read or read/write access to metafield definitions to have access to metafield values. This represents a breaking change because as of API version 2024-07, metafield definitions without [access permissions](#metafield-access-controls) will not be available to the Customer Account API.

---

Was this page helpful?

YesNo