---
source: https://shopify.dev/docs/api/release-notes/2024-10
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| October 1, 2024 | October 1, 2025 |

---

## [Anchor to Highlights](/docs/api/release-notes/2024-10#highlights)Highlights

Here are some highlights of version 2024-10 of Shopify's APIs:

* [**Abandoned checkouts**](/docs/api/admin-graphql/latest/objects/AbandonedCheckout): We've added new types that are associated with the `AbandonedCheckout` object. This object replaces the [`Abandoned checkouts`](/docs/api/admin-rest/latest/resources/abandoned-checkouts) resource in the REST Admin API.
* [**`app_scopes/update` webhook**](/docs/api/webhooks/latest?reference=toml#list-of-topics-app/scopes_update): Apps can now subscribe to the `app/scopes_update` webhook topic. This webhook is triggered when the granted access scopes for the installed app on a shop have been modified.
* [**Cart warnings**](/docs/storefronts/headless/building-with-the-storefront-api/cart/cart-warnings): Storefront API cart mutations now include warnings to show automatic changes that occurred while executing a mutation.
* [**Fulfillment constraints**](/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function): You can now associate a fulfillment constraint function to one or multiple delivery methods, such as `SHIPPING` and `PICKUP`. The function will only run under the context of the specified delivery methods.
* [**Gift cards**](/docs/api/admin-graphql/2024-10/queries/giftCard): You can now use new gift cards and gift card transaction types in all apps and shops, with no additional approval scopes or flags required.
* [**Metafield capabilities**](/docs/apps/build/custom-data/metafields/use-metafield-capabilities): Create an automated collection based on metafield values for a given definition. Then, filter products based on metafield values for that definition.
* [**`Products` query attributes**](/docs/api/admin-graphql/latest/queries/products#argument-query): We've added new attributes to the `products` query, which include `publication_ids`, `variant_id`, and `variant_title`.
* [**`StaffMember` improvements**](/docs/api/admin-graphql/latest/objects/StaffMember): We've made several improvements to the `StaffMember` object. These improvements enable apps using the REST Admin API's [`User`](/docs/api/admin-rest/latest/resources/user) resource to migrate to using the GraphQL Admin API's `StaffMember` object.
* [**Subscription contracts**](/docs/api/customer/2024-10/objects/SubscriptionContract): New types for subscription contracts are now available in the Customer Account API.

---

## [Anchor to Breaking changes](/docs/api/release-notes/2024-10#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Cart warnings](/docs/api/release-notes/2024-10#cart-warnings)Cart warnings

Inventory errors about stock levels are no longer included in the `userErrors` of cart mutations in the Storefront API. Inventory errors are now available in the `warnings` return field, and contain the following explicit values:

* `MERCHANDISE_NOT_ENOUGH_STOCK`
* `MERCHANDISE_OUT_OF_STOCK`

Warnings are available on all cart mutations to show automatic changes that occurred while executing the mutation. You can use warnings to manage items in your cart or display information to a buyer. For example, you can remove out-of-stock lines from a cart by using the [`target`](/docs/api/storefront/2024-10/mutations/cartLinesRemove#field-cartlinesremovepayload-warnings) field included in the `warning` as the input to the `cartLinesRemove` mutation.

[Learn more about cart warnings](/docs/storefronts/headless/building-with-the-storefront-api/cart/cart-warnings).

### [Anchor to Changed enum value for ,[object Object]](/docs/api/release-notes/2024-10#changed-enum-value-for-orderdisplayfulfillmentstatus)Changed enum value for `OrderDisplayFulfillmentStatus`

The [`OrderDisplayFulfillmentStatus`](/docs/api/admin-graphql/2024-10/enums/OrderDisplayFulfillmentStatus) enum now returns a `REQUEST_DECLINED` value for an order that has had its fulfillment request rejected by a third-party fulfillment service. In API versions prior to 2024-10, orders in the request rejected state return an `UNFULFILLED` status.

### [Anchor to Event query enhancements](/docs/api/release-notes/2024-10#event-query-enhancements)Event query enhancements

We've made the [`CommentEvent.subject`](/docs/api/admin-graphql/2024-10/objects/CommentEvent#field-subject) field nullable. `null` is returned when the subject's underlying data has been deleted. You must update your code to handle cases where `subject` might return `null`. For example, revise existing logic that assumes the field will always contain data, and implement checks or fallback mechanisms to manage situations where the `subject` data has been deleted.

We've also deprecated the [`deletionEvents`](/docs/api/admin-graphql/2024-10/queries/deletionEvents) query in favour of events that indicate deletion. Update your code to remove any reliance on `deletionEvents`, and use the new event structure. To support querying events, we've added the following types:

Types for events

| Name | Type | Change |
| --- | --- | --- |
| `action` | field | Added to `Event` interface |
| `event` | Query | Added |
| `events` | Query | Added |
| `eventsCount` | Query | Added |
| `events` | Connection | Added to `Article`, `Blog`, `Comment`, `Page`, `Product`, and `ProductVariant` objects |
| `EventSubjectType` | Enum | Added |
| `arguments` | field | Added to `BasicEvent` object |
| `subject` | field | Added to `BasicEvent` object |
| `subjectID` | field | Added to `BasicEvent` object |
| `subjectType` | field | Added to `BasicEvent` object |

### [Anchor to Fulfillment by Amazon](/docs/api/release-notes/2024-10#fulfillment-by-amazon)Fulfillment by Amazon

As of API version 2024-10, the [`shippingMethods`](/docs/api/admin-graphql/2024-10/objects/FulfillmentService#field-shippingmethods) field on the `FulfillmentService` object has been deprecated. The [`shippingMethods`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderSubmitFulfillmentRequest#argument-shippingmethod) argument on the `fulfillmentOrderSubmitFulfillmentRequest` mutation has also been deprecated.

The shipping method associated with the fulfillment service provider applied only to the **Fulfill By Amazon** fulfillment service. The Fulfillment by Amazon feature isn't supported as of March 30, 2023. To continue using Amazon fulfillment, merchants need to set up a [multi-channel fulfillment solution](https://help.shopify.com/manual/shipping/fulfillment-services/amazon#activate-fulfillment-by-amazon), as recommended by Amazon.

### [Anchor to Fulfillment holds](/docs/api/release-notes/2024-10#fulfillment-holds)Fulfillment holds

As of API version 2024-10, apps can't [release fulfillment holds](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderReleaseHold) unless they have write access to them. You need to request the following access scopes for your app:

* `write_merchant_managed_fulfillment_orders`: Allows your app to release holds on fulfillment orders assigned to a merchant-managed location
* `write_third_party_fulfillment_orders`: Allows your app to release holds on fulfillment orders assigned to a third-party location
* `write_marketplace_fulfillment_orders`: Allows your app to release holds on fulfillment orders which belong to one of your marketplace's orders

If your app doesn't have sufficient access scopes to release a hold, then a user error with the [`INVALID_ACCESS`](/docs/api/admin-graphql/2024-10/enums/FulfillmentOrderReleaseHoldUserErrorCode#value-fulfillmentordernotfound) code is returned and the hold isn't released.

We've deprecated the [`fulfillmentOrdersReleaseHolds`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrdersReleaseHolds) mutation. Use the [`fulfillmentOrderReleaseHold`](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold) mutation instead.

We've also deprecated the `GREATER_THAN_ZERO` and `INVALID_LINE_ITEM_QUANTITY` [error codes](/docs/api/admin-graphql/2024-10/enums/FulfillmentOrderReleaseHoldUserErrorCode) on the `fulfillmentOrderReleaseHold` mutation.

We've also added the [`heldByRequestingApp`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-heldbyrequestingapp) field to the `FulfillmentHold` object. If you have the `read_apps` scope enabled on your app, then you'll only be able to read the [`heldBy`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-heldby) field on the `FulfillmentHold` object. Use the `heldByRequestingApp` field instead if you need to confirm whether your app created the fulfillment hold.

Additionally, the `fulfillmentOrderHold` mutation now returns the fulfillment hold that was created in a new [`fulfillmentHold` return field](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderHold#field-fulfillmentorderholdpayload-fulfillmenthold).

### [Anchor to Gift cards](/docs/api/release-notes/2024-10#gift-cards)Gift cards

We've improved the [`GiftCard`](/docs/api/admin-graphql/2024-10/objects/GiftCard) types and have introduced several new types for working with gift cards. The gift card types are now open to all apps and shops, with no additional approval scopes or flags required.

**Developer action required**

* The [`giftCardDisable`](/docs/api/admin-graphql/2024-07/mutations/giftCardDisable) mutation has been removed. Use [`giftCardDeactivate`](/docs/api/admin-graphql/2024-10/mutations/giftCardDeactivate) instead.
* The [`disabledAt`](/docs/api/admin-graphql/2024-07/objects/GiftCard#field-disabledat) field on the `GiftCard` object has been removed. Use the [`deactivatedAt`](/docs/api/admin-graphql/2024-10/objects/GiftCard#field-deactivatedat) field instead.

The following types for gift cards are now available:

Available types for gift cards

| Name | Type | Change |
| --- | --- | --- |
| `CUSTOMER_NOT_FOUND` | Value | Added to `GiftCardErrorCode` enum |
| `deactivatedAt` | Field | Added to `GiftCard` object |
| `GiftCardCreateInput` | Input object | Added |
| `giftCardCredit` | Mutation | Added |
| `GiftCardCreditInput` | Input object | Added |
| `GiftCardCreditTransaction` | Object | Added |
| `giftCardDebit` | Mutation | Added |
| `GiftCardDebitInput` | Input object | Added |
| `GiftCardDebitTransaction` | Object | Added |
| `giftCardDeactivate` | Mutation | Added |
| `GiftCardRecipient` | Object | Added |
| `GiftCardRecipientInput` | Input object | Added |
| `giftCardSendNotificationToCustomer` | Mutation | Added |
| `giftCardSendNotificationToRecipient` | Mutation | Added |
| `GiftCardTransaction` | Interface | Added |
| `GiftCardTransactionUserError` | Object | Added |
| `recipientAttributes` | Field | Added to `GiftCard` object |
| `recipientAttributes` | Field | Added to `GiftCardCreateInput` input object |
| `recipientAttributes` | Field | Added to `GiftCardUpdateInput` input object |
| `RECIPIENT_NOT_FOUND` | Value | Added to `GiftCardErrorCode` enum |
| `transactions` | Connection | Added to `GiftCard` object |
| `updatedAt` | Field | Added to `GiftCard` object |

### [Anchor to Improvements to the ,[object Object], type](/docs/api/release-notes/2024-10#improvements-to-the-staffmember-type)Improvements to the `StaffMember` type

`Shop.staffMembers` has been deprecated. Use the [`staffMembers`](/docs/api/admin-graphql/2024-10/queries/staffMembers) query instead.

### [Anchor to Location error codes](/docs/api/release-notes/2024-10#location-error-codes)Location error codes

We've removed the `HAS_OPEN_TRANSFERS_ERROR` and `FAILED_TO_RELOCATE_OPEN_TRANSFERS` error codes from the [`LocationDeactivateUserErrorCode`](/docs/api/admin-graphql/2024-10/enums/LocationDeactivateUserErrorCode) enum. If you're explicitly checking for either of these error codes in your app, then you should remove references to them.

### [Anchor to Location resource](/docs/api/release-notes/2024-10#location-resource)Location resource

If your app retrieves a [`Location`](/docs/api/admin-rest/2024-10/resources/location) resource using the REST Admin API, then you need to request the `read_locations` access scope.

If your app reads a [`Location`](/docs/api/admin-graphql/2024-10/objects/Location) resource without the [`read_locations` access scope](/docs/api/usage/access-scopes), then a [403 Forbidden error](/docs/api/admin-rest#status_and_error_codes) is returned.

### [Anchor to Metafield definitions](/docs/api/release-notes/2024-10#metafield-definitions)Metafield definitions

We've deprecated the `definitions.visibleToStorefrontApi` argument on the [`standardMetafieldDefinitionEnable`](/docs/api/admin-graphql/unstable/mutations/standardMetafieldDefinitionsEnable#argument-definitions) and [`standardMetafieldDefinitionsEnable`](/docs/api/admin-graphql/unstable/mutations/standardMetafieldDefinitionsEnable#argument-definitions) mutations. Use the `definitions.access` argument on these mutations instead.

Note

The `definitions.access` argument allows you to specify more granular [permissions](/docs/apps/build/custom-data/permissions) when enabling a [standard metafield definition template](/docs/api/admin-graphql/2024-10/objects/StandardMetafieldDefinitionTemplate).

**Note:**

The `definitions.access` argument allows you to specify more granular [permissions](/docs/apps/build/custom-data/permissions) when enabling a [standard metafield definition template](/docs/api/admin-graphql/2024-10/objects/StandardMetafieldDefinitionTemplate).

### [Anchor to Online store](/docs/api/release-notes/2024-10#online-store)Online store

We've deprecated the [`OnlineStorePage`](/docs/api/admin-graphql/2024-10/objects/OnlineStorePage), [`OnlineStoreArticle`](/docs/api/admin-graphql/2024-10/objects/OnlineStoreArticle), and [`OnlineStoreBlog`](/docs/api/admin-graphql/2024-10/objects/OnlineStoreBlog) objects. Use the [`Page`](/docs/api/admin-graphql/2024-10/objects/Page), [`Article`](/docs/api/admin-graphql/2024-10/objects/Article), and [`Blog`](/docs/api/admin-graphql/2024-10/objects/Blog) objects instead.

You can now read and modify pages, articles, blogs, and comments. The following types are now available:

Types for the online store

| Name | Type | Change |
| --- | --- | --- |
| `pageCreateInput` | Input object | Added |
| `pageUpdateInput` | Input object | Added |
| `pageCreate` | Mutation | Added |
| `pageUpdate` | Mutation | Added |
| `pageDelete` | Mutation | Added |
| `page` | Query | Added |
| `pages` | Query | Added |
| `pagesCount` | Query | Added |
| `PAGE` | Value | Added to `TranslatableResourceType` enum |
| `ArticleAuthor` | Object | Added |
| `ArticleBlogInput` | Input object | Added |
| `ArticleCreateInput` | Input object | Added |
| `ArticleImageInput` | Input object | Added |
| `ArticleUpdateInput` | Input object | Added |
| `articleCreate` | Mutation | Added |
| `articleUpdate` | Mutation | Added |
| `articleDelete` | Mutation | Added |
| `article` | Query | Added |
| `articles` | Query | Added |
| `ARTICLE` | Value | Added to `TranslatableResourceType` enum |
| `AuthorInput` | Input object | Added |
| `BlogCreateInput` | Input object | Added |
| `BlogUpdateInput` | Input object | Added |
| `BlogFeed` | Object | Added |
| `blogCreate` | Mutation | Added |
| `blogUpdate` | Mutation | Added |
| `blogDelete` | Mutation | Added |
| `blog` | Query | Added |
| `blogs` | Query | Added |
| `blogsCount` | Query | Added |
| `BLOG` | Value | Added to `TranslatableResourceType` enum |
| `Comment` | Object | Added |
| `CommentAuthor` | Object | Added |
| `commentApprove` | Mutation | Added |
| `commentSpam` | Mutation | Added |
| `commentNotSpam` | Mutation | Added |
| `commentDelete` | Mutation | Added |
| `comment` | Query | Added |
| `comments` | Query | Added |
| `CommentStatus` | Enum | Added |
| `CommentPolicy` | Enum | Added |
| `MENU` | Value | Added to `TranslatableResourceType` enum |

### [Anchor to Order line items](/docs/api/release-notes/2024-10#order-line-items)Order line items

We've removed the `lineItemsMutable` connection on the `Order` object. Use the [`lineItems`](/docs/api/admin-graphql/2024-10/objects/Order#connection-lineitems) connection on the `Order` object instead.

### [Anchor to Order management apps](/docs/api/release-notes/2024-10#order-management-apps)Order management apps

The `write_third_party_fulfillment_orders` access scope no longer allows [order management apps](/docs/apps/build/orders-fulfillment/order-management-apps) to fulfill fulfillment orders assigned to locations that are owned by other fulfillment service apps. Order management apps will still be able to access and manage these orders, but fulfillment creation will be prohibited.

The `write_assigned_fulfillment_orders` and `write_merchant_managed_fulfillment_orders` access scopes remain unchanged. Fulfillment service apps can still fulfill orders that are assigned to them, as long as they're granted the `write_assigned_fulfillment_orders` access scope. Fulfillment orders that are assigned to merchant-managed locations are still fulfillable by order management apps, as long as they're granted the `write_merchant_managed_fulfillment_orders` access scope.

Apps can confirm whether fulfillment creation is possible by querying supported actions using the [GraphQL Admin API](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder#field-supportedactions). If the fulfillment order is assigned to a merchant-managed location or to the fulfillment service performing the query and it's in a fulfillable state, then the `CREATE_FULFILLMENT` action is returned as a possible option.

### [Anchor to Pickup locations](/docs/api/release-notes/2024-10#pickup-locations)Pickup locations

You can now use the [`destination`](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder#field-destination) field on the `fulfillmentOrder` object to retrieve the pickup location for a fulfillment order.

As of API version 2024-10, the `destination` field returns a [`FulfillmentOrderDestination`](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrderDestination) object instead of `null` for fulfillment orders that don't have an associated shipping address. If the fulfillment order doesn't have a shipping address, then the address-related fields within the `FulfillmentOrderDestination` object are set to `null`.

### [Anchor to PriceRule types removed](/docs/api/release-notes/2024-10#pricerule-types-removed)PriceRule types removed

As of API version 2024-10, we've removed `PriceRule` types from the GraphQL Admin API. The associated queries and mutations have been deprecated since API version 2023-03. Use the [`discountNode`](/docs/api/admin-graphql/2024-10/queries/discountNode) query instead.

The following types have been removed:

* `PriceRuleUserError` object
* `PriceRuleCustomerSelectionInput` input object
* `PriceRuleDiscountCodeInput` input object
* `PriceRuleEntitlementToPrerequisiteQuantityRatioInput` input object
* `PriceRuleInput` input object
* `PriceRuleItemEntitlementsInput` input object
* `PriceRuleItemPrerequisitesInput` input object
* `PriceRuleMoneyRangeInput` input object
* `PriceRulePrerequisiteToEntitlementQuantityRatioInput` input object
* `PriceRuleQuantityRangeInput` input object
* `PriceRuleShippingEntitlementsInput` input object
* `PriceRuleValidityPeriodInput` input object
* `PriceRuleValueInput` input object
* `priceRuleSavedSearches` query
* `PriceRuleActivate` mutation
* `PriceRuleCreate` mutation
* `PriceRuleDeactivate` mutation
* `PriceRuleDelete` mutation
* `PriceRuleDiscountCodeCreate` mutation
* `PriceRuleDiscountCodeUpdate` mutation
* `PriceRuleUpdate` mutation
* `priceRule` field on the `QueryRoot` object
* `priceRules` connection on the `QueryRoot` object
* `priceRules` connection on the `Shop` object
* `priceRuleSavedSearches` connection on the `Shop` object

### [Anchor to Product duplications](/docs/api/release-notes/2024-10#product-duplications)Product duplications

The [`productDuplicateAsyncV2`](/docs/api/admin-graphql/2024-10/mutations/productDuplicateAsyncV2) mutation has been removed. We've added the [`synchronous`](/docs/api/admin-graphql/2024-10/mutations/productDuplicate#argument-synchronous) argument to the `productDuplicate` mutation, allowing you to choose whether the product duplication should be processed synchronously or asynchronously.

* **Asynchronous duplication:** By setting the `synchronous` field to `false` in the `productDuplicate` mutation, the operation operates asynchronously, and returns a [`ProductDuplicateOperation`](/docs/api/admin-graphql/2024-10/objects/ProductDuplicateOperation) object.
* **Operation tracking:** You can track the status of the asynchronous duplication by querying the operation ID through the [`productOperation`](/docs/api/admin-graphql/2024-10/queries/productOperation#argument-id) query.

### [Anchor to Product input](/docs/api/release-notes/2024-10#product-input)Product input

We've removed the `input` argument on the [`productCreate`](/docs/api/admin-graphql/2024-10/mutations/productCreate) and [`productUpdate`](/docs/api/admin-graphql/2024-10/mutations/productUpdate) mutations.

Use the following `product` arguments instead:

* [`ProductCreateInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductCreateInput) on the `productCreate` mutation
* [`ProductUpdateInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductUpdateInput) on the `productUpdate` mutation

### [Anchor to Product media](/docs/api/release-notes/2024-10#product-media)Product media

We've made changes to how you work with product media by replacing the current media ID inputs with file inputs and expanding media capabilities:

* The `mediaIds` field on the [`ProductSetInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductSetInput) input object has been removed. Use the [`files`](/docs/api/admin-graphql/2024-10/input-objects/ProductSetInput#field-files) field instead to associate files to a product.
* The `mediaId` field on the [`ProductVariantSetInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductVariantSetInput) input object has been removed. Use the [`file`](/docs/api/admin-graphql/2024-10/input-objects/ProductVariantSetInput#field-file) field instead to associate a file with the product variant.
* The [`FileSetInput`](/docs/api/admin-graphql/2024-10/input-objects/FileSetInput) input object is now available for working with existing media and creating new files. This input object is a derivative of the [`FileCreateInput`](/docs/api/admin-graphql/2024-10/input-objects/FileCreateInput) input object, with an added `id` field.

### [Anchor to Product mutations](/docs/api/release-notes/2024-10#product-mutations)Product mutations

We've removed the following deprecated product mutations from the GraphQL Admin API:

* [`productAppendImages`](/docs/api/admin-graphql/2024-07/mutations/productAppendImages) is removed. Use the [`productCreateMedia`](/docs/api/admin-graphql/2024-10/mutations/productCreateMedia) mutation instead.
* [`productDeleteImages`](/docs/api/admin-graphql/2024-07/mutations/productDeleteImages) is removed. Use the [`productDeleteMedia`](/docs/api/admin-graphql/2024-10/mutations/productDeleteMedia) mutation instead.
* [`productImageUpdate`](/docs/api/admin-graphql/2024-07/mutations/productImageUpdate) is removed. Use the [`productDeleteMedia`](/docs/api/admin-graphql/2024-10/mutations/productDeleteMedia). Use the [`productUpdateMedia`](/docs/api/admin-graphql/2024-10/mutations/productUpdateMedia) mutation instead.
* [`productReorderImages`](/docs/api/admin-graphql/2024-07/mutations/productReorderImages) is removed. Use the [`productReorderMedia`](/docs/api/admin-graphql/2024-10/mutations/productReorderMedia) mutation instead.

### [Anchor to Product variant mutations](/docs/api/release-notes/2024-10#product-variant-mutations)Product variant mutations

We've deprecated the following singular product variant mutations in favor of their equivalent bulk versions:

* [`productVariantCreate`](/docs/api/admin-graphql/2024-07/mutations/productvariantcreate) is deprecated. Use the [`productVariantsBulkCreate`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkcreate) mutation instead.
* [`productVariantUpdate`](/docs/api/admin-graphql/2024-07/mutations/productvariantupdate) is deprecated. Use the [`productVariantsBulkUpdate`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkupdate) mutation instead.
* [`productVariantDelete`](/docs/api/admin-graphql/2024-07/mutations/productvariantdelete) is deprecated. Use the [`productVariantsBulkDelete`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkdelete) mutation instead.

### [Anchor to ProductImage value removed](/docs/api/release-notes/2024-10#productimage-value-removed)ProductImage value removed

The `PRODUCTIMAGE` value has been removed from the [`MetafieldOwnerType`](/docs/api/admin-graphql/2024-10/enums/MetafieldOwnerType) enum. Use `MEDIA_IMAGE` instead.

### [Anchor to ProductInput fields removed](/docs/api/release-notes/2024-10#productinput-fields-removed)ProductInput fields removed

We've removed the following deprecated `ProductInput` fields from the GraphQL Admin API:

* `bodyHTML` is removed. Use the [`descriptionHtml`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-descriptionhtml) field instead.
* `privateMetaFields` is removed. Use the [`productOptions`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-productoptions) field instead.
* `standardizedProductType` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.
* `productCategory` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.
* `customProductType` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.

### [Anchor to Removed fields on ,[object Object], object](/docs/api/release-notes/2024-10#removed-fields-on-shopfeatures-object)Removed fields on `ShopFeatures` object

The following deprecated fields on the [`ShopFeatures`](/docs/api/admin-graphql/2024-10/objects/ShopFeatures) object have been removed:

* `avalaraAvatax`
* `branding`
* `captcha`
* `dynamicRemarketing`
* `harmonizedSystemCode`
* `liveView`
* `onboardingVisual`
* `reports`
* `showMetrics`

  Instead of the `branding` field, use [`Shop.plan.shopifyPlus`](/docs/api/admin-graphql/2024-10/objects/Shop#field-plan) instead.

### [Anchor to Removed ,[object Object], on Fulfillment mutations](/docs/api/release-notes/2024-10#removed-v2-on-fulfillment-mutations)Removed `V2` on Fulfillment mutations

We've deprecated the [`fulfillmentCreateV2`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreateV2) and [`fulfillmentTrackingInfoUpdateV2`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentTrackingInfoUpdateV2) mutations. Use the [`fulfillmentCreate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreate) and [`fulfillmentTrackingInfoUpdate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentTrackingInfoUpdate) mutations instead.
The behavior of the new mutations remains the same as the previous ones. The only change is the removal of `V2` to ensure consistent naming across all mutations.

### [Anchor to Reverse fulfillment orders](/docs/api/release-notes/2024-10#reverse-fulfillment-orders)Reverse fulfillment orders

The [`reverseDeliveryDispose`](/docs/api/admin-graphql/2024-07/mutations/reverseDeliveryDispose) mutation is deprecated. Use the [`reverseFulfillmentOrderDispose`](/docs/api/admin-graphql/2024-10/mutations/reverseFulfillmentOrderDispose) mutation instead.

The [`fulfillmentLineItem`](/docs/api/admin-graphql/2024-10/objects/ReverseFulfillmentOrderLineItem#field-fulfillmentlineitem) field on the `ReverseFulfillmentOrderLineItem` object is now nullable. A `ReverseFulfillmentOrderLineItem` object won't always be associated with a `FulfillmentLineItem` object. The non-null `fulfillmentLineItem` field on API versions prior to 2024-10 returns an error when the fulfillment line item doesn't exist.

[Learn more about managing reverse fulfillment orders](/docs/apps/build/orders-fulfillment/returns-apps/manage-reverse-fulfillment-orders).

### [Anchor to Setting available inventory quantity](/docs/api/release-notes/2024-10#setting-available-inventory-quantity)Setting available inventory quantity

We've deprecated the ability to set the available quantity on the [`inventoryActivate`](/docs/api/admin-graphql/2024-10/mutations/inventoryActivate) mutation for inventory items that are already in an active state. Use the [`inventorySetQuantities`](/docs/api/admin-graphql/2024-10/mutations/inventorySetQuantities) mutation instead.

We've also added the [`INVALID_QUANTITY_TOO_LOW`](/docs/api/admin-graphql/2024-10/enums/InventorySetQuantitiesUserErrorCode#value-invalidquantitytoolow) value to the `InventorySetQuantitiesUserErrorCode` enum. The error code is returned if you run the `inventorySetQuantities` mutation and a quantity is less than negative one billion.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/2024-10#graphql-admin-api-changes)GraphQL Admin API changes

Version 2024-10 of the GraphQL Admin API introduces the following changes:

### [Anchor to Abandoned checkouts](/docs/api/release-notes/2024-10#abandoned-checkouts)Abandoned checkouts

We've added new types that are associated with the [`AbandonedCheckout`](/docs/api/admin-graphql/2024-10/objects/AbandonedCheckout) object. This object replaces the [`Abandoned checkouts`](/docs/api/admin-rest/2024-10/resources/abandoned-checkouts) resource in the REST Admin API.

The following new types are available:

New types related to abandoned checkouts

| Name | Type | Change |
| --- | --- | --- |
| `UnitPriceMeasurement` | Object | Added |
| `abandonedCheckouts` | Query | Added |
| `abandonedCheckoutsCount` | Query | Added |
| `totalWeight` | Field | Added to `AbandonedCheckout` object |
| `referringSite` | Field | Added to `AbandonedCheckout` object |
| `landingSite` | Field | Added to `AbandonedCheckout` object |
| `gateway` | Field | Added to `AbandonedCheckout` object |
| `currencyCode` | Field | Added to `AbandonedCheckout` object |
| `presentmentCurrencyCode` | Field | Added to `AbandonedCheckout` object |
| `token` | Field | Added to `AbandonedCheckout` object |
| `cartToken` | Field | Added to `AbandonedCheckout` object |
| `customAttributes` | Field | Added to `AbandonedCheckout` object |
| `note` | Field | Added to `AbandonedCheckout` object |
| `totalLineItemsPriceSet` | Field | Added to `AbandonedCheckout` object |
| `subtotalPriceSet` | Field | Added to `AbandonedCheckout` object |
| `discountCodes` | Field | Added to `AbandonedCheckout` object |
| `totalDiscountSet` | Field | Added to `AbandonedCheckout` object |
| `totalTaxSet` | Field | Added to `AbandonedCheckout` object |
| `totalDutiesSet` | Field | Added to `AbandonedCheckout` object |
| `taxLines` | Field | Added to `AbandonedCheckout` object |
| `taxesIncluded` | Field | Added to `AbandonedCheckout` object |
| `closedAt` | Field | Added to `AbandonedCheckout` object |
| `completedAt` | Field | Added to `AbandonedCheckout` object |
| `updatedAt` | Field | Added to `AbandonedCheckout` object |
| `createdAt` | Field | Added to `AbandonedCheckout` object |
| `shippingLines` | Field | Added to `AbandonedCheckout` object |
| `billingAddress` | Field | Added to `AbandonedCheckout` object |
| `shippingAddress` | Field | Added to `AbandonedCheckout` object |
| `customer` | Field | Added to `AbandonedCheckout` object |
| `name` | Field | Added to `AbandonedCheckout` object |
| `AbandonedCheckoutShippingLine` | Object | Added |
| `taxLines` | Field | Added to `AbandonedCheckoutLineItem` object |
| `discountAllocations` | Field | Added to `AbandonedCheckoutLineItem` object |
| `requiresShipping` | Field | Added to `AbandonedCheckoutLineItem` object |
| `weight` | Field | Added to `AbandonedCheckoutLineItem` object |
| `fulfillmentService` | Field | Added to `AbandonedCheckoutLineItem` object |
| `presentmentVariantTitle` | Field | Added to `AbandonedCheckoutLineItem` object |
| `presentmentTitle` | Field | Added to `AbandonedCheckoutLineItem` object |
| `source` | Field | Added to `TaxLines` object |
| `unitPriceMeasurement` | Field | Added to `ProductVariant` object |

### [Anchor to Adding page links in navigation menus](/docs/api/release-notes/2024-10#adding-page-links-in-navigation-menus)Adding page links in navigation menus

You can now add links to the [**Orders**](https://admin.shopify.com/orders), [**Customer profiles**](https://admin.shopify.com/customers), and [**Settings**](https://admin.shopify.com/settings) pages in navigation menus.

You can use the GraphQL Admin API to update menus that include these pages, and add activated full page extensions to menus, when [customer account UI extensions](/docs/api/customer-account-ui-extensions) are available for general release. Merchants will also be able to customize their customer account navigation menu. For more information, refer to the [product roadmap](/docs/apps/build/customer-accounts#product-roadmap).

To learn more, refer to the following GraphQL reference documentation:

* [`menuCreate`](/docs/api/admin-graphql/2024-10/mutations/menuCreate) mutation
* [`menuUpdate`](/docs/api/admin-graphql/2024-10/mutations/menuUpdate) mutation
* [`menu`](/docs/api/admin-graphql/2024-10/queries/menus) query

### [Anchor to App feedback](/docs/api/release-notes/2024-10#app-feedback)App feedback

We've added the [`feedbackGeneratedAt`](/docs/api/admin-graphql/2024-10/objects/AppFeedback#field-feedbackgeneratedat) and [`state`](/docs/api/admin-graphql/2024-10/objects/AppFeedback#field-state) fields to the [`AppFeedback`](/docs/api/admin-graphql/2024-10/objects/AppFeedback) object. This field represents the date and time when the app feedback was generated. It conveys the state of the feedback and whether it requires merchant action.

### [Anchor to App scopes webhook](/docs/api/release-notes/2024-10#app-scopes-webhook)App scopes webhook

Apps can now subscribe to the [`app/scopes_update`](/docs/api/webhooks/2024-10?reference=toml#list-of-topics-app/scopes_update) webhook topic. This webhook is triggered when the granted access scopes for the installed app on a shop have been modified. It allows apps to keep track of the granted access scopes of their installations.

### [Anchor to Automatic app discounts](/docs/api/release-notes/2024-10#automatic-app-discounts)Automatic app discounts

We've added the `recurringCycleLimit` and `appliesOnSubscription` fields on the [`DiscountAutomaticApp`](/docs/api/admin-graphql/2024-10/objects/DiscountAutomaticApp) object and [`DiscountAutomaticAppInput`](/docs/api/admin-graphql/2024-10/input-objects/DiscountAutomaticAppInput) input object.

The fields enable merchants to use [automatic app discounts](/docs/apps/build/discounts#discount-methods) for subscriptions, and apply the discounts for a pre-determined number of cycles. Developers can use the fields in their automatic app [discount functions](/docs/apps/build/discounts/build-discount-function).

### [Anchor to Business entities](/docs/api/release-notes/2024-10#business-entities)Business entities

Large merchants with an established international presence need to be able to specify which of their business entities handles sales for a given buyer context. You can now use the GraphQL Admin API to query fields related to the business entities that are enabled on a store.

The following new types are available:

New types related to business entities

| Name | Type | Change |
| --- | --- | --- |
| `businessEntities` | Query | Added |
| `businessEntity` | Query | Added |
| `BusinessEntity` | Object | Added |
| `BusinessEntityAddress` | Object | Added |
| `businessEntity` | Field | Added to `Payout` object |
| `merchantBusinessEntity` | Field | Added to `Order` object |

### [Anchor to Cart and checkout validations](/docs/api/release-notes/2024-10#cart-and-checkout-validations)Cart and checkout validations

We've added the [`MAX_VALIDATIONS_ACTIVATED`](/docs/api/admin-graphql/2024-10/enums/ValidationUserErrorCode#value-maxvalidationsactivated) error code to the `ValidationUserErrorCode` enum. The error code is returned when your app exceeds the maximum of five [validation functions](/docs/apps/build/checkout/cart-checkout-validation) in checkout.

### [Anchor to Cash transactions on POS](/docs/api/release-notes/2024-10#cash-transactions-on-pos)Cash transactions on POS

We've added the [`totalCashRoundingAdjustment`](/docs/api/admin-graphql/2024-10/objects/Order#field-totalcashroundingadjustment) field to the `Order` object, which allows you to query the total rounding adjustment applied on cash payments or refund transactions in an order on Point of Sale (POS).

Cash transactions on POS are now automatically rounded to the nearest denominations for the some currencies and countries, like CAD (Canada), AUD (Australia), NZD (New Zealand), EUR (Switzerland, Belgium, Finland), DKK (Denmark), Sweden (SEK) and Norway (NOK).

### [Anchor to Changed enum value for OrderDisplayFulfillmentStatus](/docs/api/release-notes/2024-10#changed-enum-value-for-orderdisplayfulfillmentstatus)Changed enum value for OrderDisplayFulfillmentStatus

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The [`OrderDisplayFulfillmentStatus`](/docs/api/admin-graphql/2024-10/enums/OrderDisplayFulfillmentStatus) enum now returns a `REQUEST_DECLINED` value for an order that has had its fulfillment request rejected by a third-party fulfillment service. In API versions prior to 2024-10, orders in the request rejected state return an `UNFULFILLED` status.

### [Anchor to Collections count](/docs/api/release-notes/2024-10#collections-count)Collections count

We've added the [`collectionsCount`](/docs/api/admin-graphql/2024-10/queries/collectionsCount) query, which enables you to retrieve a count of all collections in a shop. This includes published and unpublished collections, and custom and smart collections.

### [Anchor to Company location staff members](/docs/api/release-notes/2024-10#company-location-staff-members)Company location staff members

We've added the [`CompanyLocationStaffMemberAssignment`](/docs/api/admin-graphql/2024-10/objects/CompanyLocationStaffMemberAssignment) object, which allows you to retrieve staff members assigned to a company location.

You can assign and remove staff members for a company location using the [`CompanyLocationAssignStaffMembers`](/docs/api/admin-graphql/2024-10/mutations/companyLocationAssignStaffMembers) and [`CompanyLocationRemoveStaffMembers`](/docs/api/admin-graphql/2024-10/mutations/companyLocationRemoveStaffMembers) mutations.

### [Anchor to Customer account invite](/docs/api/release-notes/2024-10#customer-account-invite)Customer account invite

You can now use the [`customerSendAccountInvite`](/docs/api/admin-graphql/2024-10/mutations/customerSendAccountInviteEmail) mutation to send an email invitation to a customer so that they can create a [classic customer](https://help.shopify.com/manual/customers/customer-accounts) account.

We've also added the [`CustomerSendAccountInviteEmailUserError`](/docs/api/admin-graphql/2024-10/objects/CustomerSendAccountInviteEmailUserError) that defines errors for the [`customerSendAccountInvite`](/docs/api/admin-graphql/2024-10/mutations/customerSendAccountInviteEmail) mutation.

### [Anchor to Customer addresses pagination](/docs/api/release-notes/2024-10#customer-addresses-pagination)Customer addresses pagination

We've added the [`addressesV2`](/docs/api/admin-graphql/2024-10/objects/Customer#connection-addressesv2) connection to the [`Customer`](/docs/api/customer/2024-10/objects/Customer) object. The `addressesV2` connection supports paginating through a customer's addresses, which enables you to retrieve a subset of results at a time.

### [Anchor to Customer payment methods](/docs/api/release-notes/2024-10#customer-payment-methods)Customer payment methods

We've added the [`FAILED_TO_RETRIEVE_BILLING_ADDRESS`](/docs/api/admin-graphql/2024-10/enums/CustomerPaymentMethodRevocationReason#value-failedtoretrievebillingaddress) value on the `CustomerPaymentMethodRevocationReason` enum. The value is returned when a customer payment method is missing the billing address field.

### [Anchor to Deleting a fulfillment service](/docs/api/release-notes/2024-10#deleting-a-fulfillment-service)Deleting a fulfillment service

We've introduced the [`inventoryAction`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentServiceDelete#argument-inventoryaction) argument on the `fulfillmentServiceDelete` mutation. You can use the argument to specify how to handle inventory when you delete a fulfillment service. Valid values:

* `KEEP`: Converts a fulfillment service's locations to be merchant-owned. The inventory at the locations becomes the merchant's responsibility. If `KEEP` is provided, then the merchant must have a [sufficient remaining quota of locations on their Shopify plan](https://help.shopify.com/manual/locations/setting-up-your-locations#location-quantity-limit) for the operation to succeed. Otherwise, an error is returned.
* `DELETE`: Deletes the inventory at the location and then the location itself. You can only use this option when there are no outstanding fulfillments.
* `TRANSFER`: Relocates the inventory to a specified `destinationLocationId`. If you specify either `KEEP` or `DELETE`, then you can't also specify a `destinationLocationId`.

### [Anchor to Delivery options](/docs/api/release-notes/2024-10#delivery-options)Delivery options

The [`presentedName`](/docs/api/admin-graphql/2024-10/objects/DeliveryMethod#field-presentedname) field has been added to the `DeliveryMethod` object. The `presentedName` field represents the name of the delivery option that was presented to the customer during checkout.

### [Anchor to Deposits for payment terms](/docs/api/release-notes/2024-10#deposits-for-payment-terms)Deposits for payment terms

You can now set up a percentage-based deposit requirement for your payment terms using the [`DepositInput`](/docs/api/admin-graphql/2024-10/input-objects/DepositInput#field-percentage) input object. Set up payment terms on company locations using the [`CompanyCreate`](/docs/api/admin-graphql/2024-10/mutations/companyCreate), [`CompanyLocationCreate`](/docs/api/admin-graphql/2024-10/mutations/CompanyLocationCreate), and [`CompanyLocationUpdate`](/docs/api/admin-graphql/2024-10/mutations/CompanyLocationUpdate) mutations.

[Learn more about deposits](https://help.shopify.com/manual/b2b/payment-terms#deposits).

### [Anchor to Discount totals](/docs/api/release-notes/2024-10#discount-totals)Discount totals

You can now query the total number of discounts on a shop, automatic and code-based, using the [`discountNodesCount`](/docs/api/admin-graphql/2024-10/queries/discountNodesCount) query.

### [Anchor to Duties on orders](/docs/api/release-notes/2024-10#duties-on-orders)Duties on orders

We've added the [`dutiesIncluded`](/docs/api/admin-graphql/2024-10/objects/Order#field-dutiesincluded) field to `Order` object.

### [Anchor to Event query enhancements](/docs/api/release-notes/2024-10#event-query-enhancements)Event query enhancements

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've made the [`CommentEvent.subject`](/docs/api/admin-graphql/2024-10/objects/CommentEvent#field-subject) field nullable. `null` is returned when the subject's underlying data has been deleted. You must update your code to handle cases where `subject` might return `null`. For example, revise existing logic that assumes the field will always contain data, and implement checks or fallback mechanisms to manage situations where the `subject` data has been deleted.

We've also deprecated the [`deletionEvents`](/docs/api/admin-graphql/2024-10/queries/deletionEvents) query in favour of events that indicate deletion. Update your code to remove any reliance on `deletionEvents`, and use the new event structure. To support querying events, we've added the following types:

Types for events

| Name | Type | Change |
| --- | --- | --- |
| `action` | field | Added to `Event` interface |
| `event` | Query | Added |
| `events` | Query | Added |
| `eventsCount` | Query | Added |
| `events` | Connection | Added to `Article`, `Blog`, `Comment`, `Page`, `Product`, and `ProductVariant` objects |
| `EventSubjectType` | Enum | Added |
| `arguments` | field | Added to `BasicEvent` object |
| `subject` | field | Added to `BasicEvent` object |
| `subjectID` | field | Added to `BasicEvent` object |
| `subjectType` | field | Added to `BasicEvent` object |

### [Anchor to Filtering orders](/docs/api/release-notes/2024-10#filtering-orders)Filtering orders

You can now filter orders by the number of items they contain using the [`subtotalLineItemsQuantity`](/docs/api/admin-graphql/2024-10/objects/Order#field-subtotallineitemsquantity) field on the `Order` object.

You can also filter by an exact number of items, or within a specified range, using the [`subtotal_line_items_quantity`](/docs/api/admin-graphql/2024-10/queries/orders#argument-query) query filter.

### [Anchor to Filtering products](/docs/api/release-notes/2024-10#filtering-products)Filtering products

We've added [new attributes to the `products` query](/docs/api/admin-graphql/2024-10/queries/products#argument-query). You can now filter products by the following attributes:

* `publication_ids`: The IDs of product publications.
* `variant_id`: The ID of the product variant.
* `variant_title`: The title of the product variant.

### [Anchor to Fulfillment by Amazon](/docs/api/release-notes/2024-10#fulfillment-by-amazon)Fulfillment by Amazon

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

As of API version 2024-10, the [`shippingMethods`](/docs/api/admin-graphql/2024-10/objects/FulfillmentService#field-shippingmethods) field on the `FulfillmentService` object has been deprecated. The [`shippingMethods`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderSubmitFulfillmentRequest#argument-shippingmethod) argument on the `fulfillmentOrderSubmitFulfillmentRequest` mutation has also been deprecated.

The shipping method associated with the fulfillment service provider applied only to the **Fulfill By Amazon** fulfillment service. The Fulfillment by Amazon feature isn't supported as of March 30, 2023. To continue using Amazon fulfillment, merchants need to set up a [multi-channel fulfillment solution](https://help.shopify.com/manual/shipping/fulfillment-services/amazon#activate-fulfillment-by-amazon), as recommended by Amazon.

### [Anchor to Fulfillment holds](/docs/api/release-notes/2024-10#fulfillment-holds)Fulfillment holds

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

As of API version 2024-10, apps can't [release fulfillment holds](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderReleaseHold) unless they have write access to them. You need to request the following access scopes for your app:

* `write_merchant_managed_fulfillment_orders`: Allows your app to release holds on fulfillment orders assigned to a merchant-managed location
* `write_third_party_fulfillment_orders`: Allows your app to release holds on fulfillment orders assigned to a third-party location
* `write_marketplace_fulfillment_orders`: Allows your app to release holds on fulfillment orders which belong to one of your marketplace's orders

If your app doesn't have sufficient access scopes to release a hold, then a user error with the [`INVALID_ACCESS`](/docs/api/admin-graphql/2024-10/enums/FulfillmentOrderReleaseHoldUserErrorCode#value-fulfillmentordernotfound) code is returned and the hold isn't released.

We've deprecated the [`fulfillmentOrdersReleaseHolds`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrdersReleaseHolds) mutation. Use the [`fulfillmentOrderReleaseHold`](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold) mutation instead.

We've also deprecated the `GREATER_THAN_ZERO` and `INVALID_LINE_ITEM_QUANTITY` [error codes](/docs/api/admin-graphql/2024-10/enums/FulfillmentOrderReleaseHoldUserErrorCode) on the [`fulfillmentOrderReleaseHold`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderReleaseHold) mutation.

We've added the [`id`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-id) field to the `FulfillmentHold` object. We've also added an optional [`holdIds`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderReleaseHold#argument-holdIds) argument to the `fulfillmentOrderReleaseHold` mutation. The `holdIds` argument enables apps to release a hold by ID, ensuring that only the intended hold is released.

The [`heldByRequestingApp`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-heldbyrequestingapp) field is now available on the `FulfillmentHold` object. As of API version 2024-10, you'll only be able to read the [`heldBy`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-heldby) field on the `FulfillmentHold` object if you have the `read_apps` scope enabled on your app. Use the `heldByRequestingApp` field instead if you need to confirm whether your app created the fulfillment hold.

Additionally, the `fulfillmentOrderHold` mutation now returns the fulfillment hold that was created in a new [`fulfillmentHold` return field](/docs/api/admin-graphql/2024-10/mutations/fulfillmentOrderHold#field-fulfillmentorderholdpayload-fulfillmenthold).

As well, we've added a localized, [`displayReason`](/docs/api/admin-graphql/2024-10/objects/FulfillmentHold#field-displayreason) field to the `FulfillmentHold` object. You can use this field to query a human-readable reason when a fulfillment is on hold.

### [Anchor to Fulfillment orders webhook](/docs/api/release-notes/2024-10#fulfillment-orders-webhook)Fulfillment orders webhook

You can now use the `created_fulfillment_hold` field on the [`fulfillment_orders/placed_on_hold`](/docs/api/webhooks/2024-10?reference=toml#list-of-topics-fulfillment_orders/placed_on_hold) webhook to retrieve the fulfillment hold that was created.

A fulfillment hold is deleted when a hold is released. As a result, it's possible that `FulfillmentOrder.FulfillmentHolds` is empty by the time the subscriber receives the webhook. The new `created_fulfillment_hold` field always shows the hold that was created, regardless of whether it has already been released and deleted.

### [Anchor to Gift cards](/docs/api/release-notes/2024-10#gift-cards)Gift cards

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

### [Anchor to Gift cards](/docs/api/release-notes/2024-10#gift-cards)Gift cards

We've improved the [`GiftCard`](/docs/api/admin-graphql/2024-10/objects/GiftCard) types and have introduced several new types for working with gift cards. The gift card types are now open to all apps and shops, with no additional approval scopes or flags required.

**Developer action required**

* The [`giftCardDisable`](/docs/api/admin-graphql/2024-07/mutations/giftCardDisable) mutation has been removed. Use [`giftCardDeactivate`](/docs/api/admin-graphql/2024-10/mutations/giftCardDeactivate) instead.
* The [`disabledAt`](/docs/api/admin-graphql/2024-07/objects/GiftCard#field-disabledat) field on the `GiftCard` object has been removed. Use the [`deactivatedAt`](/docs/api/admin-graphql/2024-10/objects/GiftCard#field-deactivatedat) field instead.

The following types for gift cards are now available:

Available types for gift cards

| Name | Type | Change |
| --- | --- | --- |
| `CUSTOMER_NOT_FOUND` | Value | Added to `GiftCardErrorCode` enum |
| `deactivatedAt` | Field | Added to `GiftCard` object |
| `GiftCardCreateInput` | Input object | Added |
| `giftCardCredit` | Mutation | Added |
| `GiftCardCreditInput` | Input object | Added |
| `GiftCardCreditTransaction` | Object | Added |
| `giftCardDebit` | Mutation | Added |
| `GiftCardDebitInput` | Input object | Added |
| `GiftCardDebitTransaction` | Object | Added |
| `giftCardDeactivate` | Mutation | Added |
| `GiftCardRecipient` | Object | Added |
| `GiftCardRecipientInput` | Input object | Added |
| `giftCardSendNotificationToCustomer` | Mutation | Added |
| `giftCardSendNotificationToRecipient` | Mutation | Added |
| `GiftCardTransaction` | Interface | Added |
| `GiftCardTransactionUserError` | Object | Added |
| `recipientAttributes` | Field | Added to `GiftCard` object |
| `recipientAttributes` | Field | Added to `GiftCardCreateInput` input object |
| `recipientAttributes` | Field | Added to `GiftCardUpdateInput` input object |
| `RECIPIENT_NOT_FOUND` | Value | Added to `GiftCardErrorCode` enum |
| `transactions` | Connection | Added to `GiftCard` object |
| `updatedAt` | Field | Added to `GiftCard` object |

### [Anchor to Improvements to the Shop object](/docs/api/release-notes/2024-10#improvements-to-the-shop-object)Improvements to the Shop object

We've added the [`accountOwner`](/docs/api/admin-graphql/2024-10/objects/Shop#field-accountowner) field to the `Shop` object. You can use the field to retrieve information about the account owner of a shop. The `accountOwner` field returns a [`StaffMember`](/docs/api/admin-graphql/2024-10/objects/StaffMember) object.

### [Anchor to Improvements to the StaffMember type](/docs/api/release-notes/2024-10#improvements-to-the-staffmember-type)Improvements to the StaffMember type

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've made several improvements to the [`StaffMember`](/docs/api/admin-graphql/2024-10/objects/StaffMember) object. These improvements enable apps using the REST Admin API's [`User`](/docs/api/admin-rest/2024-10/resources/user) resource to migrate to using the GraphQL Admin API's `StaffMember` object.

* `Shop.staffMembers` has been deprecated. Use the [`staffMembers`](/docs/api/admin-graphql/2024-10/queries/staffMembers) query instead.
* We've added the following new fields to the `StaffMember` object:
  + [`accountType`](/docs/api/admin-graphql/2024-10/objects/StaffMember#field-accounttype)
  + [`bio`](/docs/api/admin-graphql/2024-10/objects/StaffMember#field-bio)
  + [`receiveAnnouncements`](/docs/api/admin-graphql/2024-10/objects/StaffMember#field-receiveannouncements)
  + [`url`](/docs/api/admin-graphql/2024-10/objects/StaffMember#field-url)
* You can retrieve the staff member making the API request with the [`currentStaffMember`](/docs/api/admin-graphql/2024-10/queries/currentStaffMember) query.

### [Anchor to Inventory items](/docs/api/release-notes/2024-10#inventory-items)Inventory items

You can now use the optional [`stockAtLegacyLocation`](/docs/api/admin-graphql/2024-10/mutations/inventoryActivate#argument-stockatlegacylocation) argument on the `inventoryActivate` mutation. Setting the argument to `true` allows inventory to be activated if the location ID that's provided is associated with a fulfillment service that doesn't permit SKU sharing.

* If an item is activated at a location that doesn't permit SKU sharing, then the item will be deactivated at all other locations.
* If an item is currently active at a location that doesn't permit SKU sharing, and you want to activate that item at another location, then you need to set the `stockAtLegacyLocation` argument to `true`.

### [Anchor to Inventory quantities](/docs/api/release-notes/2024-10#inventory-quantities)Inventory quantities

You can use the `ProductSetInventoryInput` input object to specify [inventory quantities for individual product variants](/docs/api/admin-graphql/2024-10/input-objects/ProductVariantSetInput#field-inventoryquantities) and set [`available` or `on_hand` quantities](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states) for new and existing product variants on locations specified.

### [Anchor to Linked metafield value error code](/docs/api/release-notes/2024-10#linked-metafield-value-error-code)Linked metafield value error code

We've added the [`LINKED_METAFIELD_VALUE_WITHOUT_LINKED_OPTION`](/docs/api/admin-graphql/2024-10/enums/ProductOptionsCreateUserErrorCode#value-linkedmetafieldvaluewithoutlinkedoption) error code to the `ProductOptionsCreateUserError` enum. This error code is returned when the `linkedMetafieldValue` can't be specified for an option that isn't linked to a metafield.

### [Anchor to Local payment methods](/docs/api/release-notes/2024-10#local-payment-methods)Local payment methods

We've added the [`LocalPaymentMethodsPaymentDetails`](/docs/api/admin-graphql/2024-10/objects/LocalPaymentMethodsPaymentDetails) object, which allows you to query the details of a [local payment method](https://help.shopify.com/manual/payments/shopify-payments/local-payment-methods) that's related to a transaction.

### [Anchor to Location error codes](/docs/api/release-notes/2024-10#location-error-codes)Location error codes

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've removed the `HAS_OPEN_TRANSFERS_ERROR` and `FAILED_TO_RELOCATE_OPEN_TRANSFERS` error codes from the[`LocationDeactivateUserErrorCode`](/docs/api/admin-graphql/2024-10/enums/LocationDeactivateUserErrorCode) enum. If you're explicitly checking for either of these error codes in your app, then you should remove references to them.

### [Anchor to Metafield capabilities](/docs/api/release-notes/2024-10#metafield-capabilities)Metafield capabilities

[Metafield capabilities](/docs/api/admin-graphql/2024-10/objects/MetafieldCapabilities) provide a way to include logic with your [metafields](/docs/api/admin-rest/2024-10/resources/metafield). When you create a metafield definition, you can now enable `capabilities` that provide additional behaviors.

You can enable the following capabilities:

* [**Smart collection**](/docs/apps/build/custom-data/metafields/use-metafield-capabilities#smart-collection): Create an automated collection based on metafield values for a given definition.
* [**Admin filterable**](/docs/apps/build/custom-data/metafields/use-metafield-capabilities#admin-filterable): Filter products based on metafield values for a definition.

  [Learn more about using metafield capabilities](/docs/apps/build/custom-data/metafields/use-metafield-capabilities).

### [Anchor to Metafield definitions](/docs/api/release-notes/2024-10#metafield-definitions)Metafield definitions

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've deprecated the `definitions.visibleToStorefrontApi` argument on the [`standardMetafieldDefinitionEnable`](/docs/api/admin-graphql/unstable/mutations/standardMetafieldDefinitionsEnable#argument-definitions) and [`standardMetafieldDefinitionsEnable`](/docs/api/admin-graphql/unstable/mutations/standardMetafieldDefinitionsEnable#argument-definitions) mutations. Use the `definitions.access` argument on these mutations instead.

Note

The `definitions.access` argument allows you to specify more granular [permissions](/docs/apps/build/custom-data/permissions) when enabling a [standard metafield definition template](/docs/api/admin-graphql/latest/objects/StandardMetafieldDefinitionTemplate).

**Note:**

The `definitions.access` argument allows you to specify more granular [permissions](/docs/apps/build/custom-data/permissions) when enabling a [standard metafield definition template](/docs/api/admin-graphql/latest/objects/StandardMetafieldDefinitionTemplate).

### [Anchor to Metafield definition webhooks](/docs/api/release-notes/2024-10#metafield-definition-webhooks)Metafield definition webhooks

You can subscribe to [`MetafieldDefinition`](/docs/api/admin-graphql/2024-10/enums/WebhookSubscriptionTopic#value-metafielddefinitionscreate) webhook changes under the webhook topics:

* [`METAFIELD_DEFINITIONS_CREATE`](/docs/api/admin-graphql/2024-10/enums/WebhookSubscriptionTopic#value-metafielddefinitionscreate)
* [`METAFIELD_DEFINITIONS_UPDATE`](/docs/api/admin-graphql/2024-10/enums/WebhookSubscriptionTopic#value-metafielddefinitionsupdate)
* [`METAFIELD_DEFINITIONS_DELETE`](/docs/api/admin-graphql/2024-10/enums/WebhookSubscriptionTopic#value-metafielddefinitionsdelete)

### [Anchor to Metafield-linked product options](/docs/api/release-notes/2024-10#metafield-linked-product-options)Metafield-linked product options

In the 2024-04 API version release, we introduced the ability to use the [`productOptionsCreate`](/docs/api/admin-graphql/2024-10/mutations/productOptionsCreate), [`productCreate`](/docs/api/admin-graphql/2024-10/mutations/productCreate), and [`productOptionUpdate`](/docs/api/admin-graphql/2024-10/mutations/productOptionUpdate) mutations to create [metafield-linked product options](/docs/apps/build/product-merchandising/products-and-collections/metafield-linked).

As of API version 2024-10, we've added more fields and error codes to support linking metafields to product options.

**Available types**

New types for managing metafield-linked product options

| Name | Type | Change |
| --- | --- | --- |
| `linkedMetafield` | Field | Added to `OptionSetInput` input object |
| `linkedMetafieldValue` | Field | Added to `VariantOptionValueInput` input object |
| `CANNOT_COMBINE_LINKED_AND_NONLINKED_OPTION_VALUES` | Error code | Added to `ProductSetUserErrorCode` enum |
| `INVALID_METAFIELD_VALUE_FOR_LINKED_OPTION` | Error code | Added to `ProductSetUserErrorCode` enum |
| `DUPLICATE_LINKED_OPTION` | Error code | Added to `ProductSetUserErrorCode` enum |
| `LINKED_OPTIONS_NOT_SUPPORTED_FOR_SHOP` | Error code | Added to `ProductSetUserErrorCode` enum |
| `LINKED_METAFIELD_DEFINITION_NOT_FOUND` | Error code | Added to `ProductSetUserErrorCode` enum |

### [Anchor to Metafields support for the cartTransformCreate mutation](/docs/api/release-notes/2024-10#metafields-support-for-the-carttransformcreate-mutation)Metafields support for the cartTransformCreate mutation

We've added the [`metafields`](/docs/api/admin-graphql/2024-10/mutations/cartTransformCreate#argument-metafields) argument to the `cartTransformCreate` mutation. You can use the argument to set metafields for a [`CartTransform`](/docs/api/admin-graphql/2024-10/objects/CartTransform) object at creation without needing to call the [`metafieldsSet`](/docs/api/admin-graphql/2024-10/mutations/metafieldsSet) mutation in a subsequent call.

[Learn more about the Cart Transform Function API](/docs/api/functions/reference/cart-transform).

### [Anchor to Online store](/docs/api/release-notes/2024-10#online-store)Online store

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've deprecated the [`OnlineStorePage`](/docs/api/admin-graphql/2024-10/objects/OnlineStorePage), [`OnlineStoreArticle`](/docs/api/admin-graphql/2024-10/objects/OnlineStoreArticle), and [`OnlineStoreBlog`](/docs/api/admin-graphql/2024-10/objects/OnlineStoreBlog) objects. Use the [`Page`](/docs/api/admin-graphql/2024-10/objects/Page), [`Article`](/docs/api/admin-graphql/2024-10/objects/Article), and [`Blog`](/docs/api/admin-graphql/2024-10/objects/Blog) objects instead.

You can now read and modify pages, articles, blogs, and comments. The following types are now available:

Types for the online store

| Name | Type | Change |
| --- | --- | --- |
| `pageCreateInput` | Input object | Added |
| `pageUpdateInput` | Input object | Added |
| `pageCreate` | Mutation | Added |
| `pageUpdate` | Mutation | Added |
| `pageDelete` | Mutation | Added |
| `page` | Query | Added |
| `pages` | Query | Added |
| `pagesCount` | Query | Added |
| `PAGE` | Value | Added to `TranslatableResourceType` enum |
| `ArticleAuthor` | Object | Added |
| `ArticleBlogInput` | Input object | Added |
| `ArticleCreateInput` | Input object | Added |
| `ArticleImageInput` | Input object | Added |
| `ArticleUpdateInput` | Input object | Added |
| `articleCreate` | Mutation | Added |
| `articleUpdate` | Mutation | Added |
| `articleDelete` | Mutation | Added |
| `article` | Query | Added |
| `articles` | Query | Added |
| `ARTICLE` | Value | Added to `TranslatableResourceType` enum |
| `AuthorInput` | Input object | Added |
| `BlogCreateInput` | Input object | Added |
| `BlogUpdateInput` | Input object | Added |
| `BlogFeed` | Object | Added |
| `blogCreate` | Mutation | Added |
| `blogUpdate` | Mutation | Added |
| `blogDelete` | Mutation | Added |
| `blog` | Query | Added |
| `blogs` | Query | Added |
| `blogsCount` | Query | Added |
| `BLOG` | Value | Added to `TranslatableResourceType` enum |
| `Comment` | Object | Added |
| `CommentAuthor` | Object | Added |
| `commentApprove` | Mutation | Added |
| `commentSpam` | Mutation | Added |
| `commentNotSpam` | Mutation | Added |
| `commentDelete` | Mutation | Added |
| `comment` | Query | Added |
| `comments` | Query | Added |
| `CommentStatus` | Enum | Added |
| `CommentPolicy` | Enum | Added |
| `MENU` | Value | Added to `TranslatableResourceType` enum |

### [Anchor to Optional access scopes](/docs/api/release-notes/2024-10#optional-access-scopes)Optional access scopes

We've added the [`optionalAccessScopes`](/docs/api/admin-graphql/2024-10/objects/App#field-optionalaccessscopes) field to the `App` object so that apps can declare some scopes as optional within their configuration. This field allows merchants to progressively grant apps access to data in their store.

### [Anchor to Order adjustments](/docs/api/release-notes/2024-10#order-adjustments)Order adjustments

We've added the [`OrderAdjustment`](/docs/api/admin-graphql/2024-10/objects/OrderAdjustment) object, which represents the difference between a calculated and an actual refund amount. We've also added the [`orderAdjustment`](/docs/api/admin-graphql/2024-10/objects/Refund#connection-orderadjustments) connection on the `Refund` object, allowing you to retrieve order adjustments that are attached to a refund.

### [Anchor to Order create](/docs/api/release-notes/2024-10#order-create)Order create

You can now use the [`orderCreate`](/docs/api/admin-graphql/2024-10/mutations/orderCreate) mutation to create an order.

### [Anchor to Order line items](/docs/api/release-notes/2024-10#order-line-items)Order line items

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've removed the `lineItemsMutable` connection on the `Order` object. Use the [`lineItems`](/docs/api/admin-graphql/2024-10/objects/Order#connection-lineitems) connection on the `Order` object instead.

### [Anchor to Order management apps](/docs/api/release-notes/2024-10#order-management-apps)Order management apps

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The `write_third_party_fulfillment_orders` access scope no longer allows [order management apps](/docs/apps/build/orders-fulfillment/order-management-apps) to fulfill fulfillment orders assigned to locations that are owned by other fulfillment service apps. Order management apps will still be able to access and manage these orders, but fulfillment creation will be prohibited.

The `write_assigned_fulfillment_orders` and `write_merchant_managed_fulfillment_orders` access scopes remain unchanged. Fulfillment service apps can still fulfill orders that are assigned to them, as long as they're granted the `write_assigned_fulfillment_orders` access scope. Fulfillment orders that are assigned to merchant-managed locations are still fulfillable by order management apps, as long as they're granted the `write_merchant_managed_fulfillment_orders` access scope.

Apps can confirm whether fulfillment creation is possible by querying supported actions using the [GraphQL Admin API](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder#field-supportedactions). If the fulfillment order is assigned to a merchant-managed location or to the fulfillment service performing the query and it's in a fulfillable state, then the `CREATE_FULFILLMENT` action is returned as a possible option.

### [Anchor to Order status](/docs/api/release-notes/2024-10#order-status)Order status

We've added the [`statusPageUrl`](/docs/api/admin-graphql/2024-10/objects/Order#field-statuspageurl) field to the `Order` object, allowing you to retrieve the URL where the customer can check the order's current status.

### [Anchor to Pickup locations](/docs/api/release-notes/2024-10#pickup-locations)Pickup locations

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

You can now use the [`destination`](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrder#field-destination) field on the `fulfillmentOrder` object to retrieve the pickup location for a fulfillment order.

As of API version 2024-10, the `destination` field returns a [`FulfillmentOrderDestination`](/docs/api/admin-graphql/2024-10/objects/FulfillmentOrderDestination) object instead of `null` for fulfillment orders that don't have an associated shipping address. If the fulfillment order doesn't have a shipping address, then the address-related fields within the `FulfillmentOrderDestination` object are set to `null`.

### [Anchor to PriceRule types removed](/docs/api/release-notes/2024-10#pricerule-types-removed)PriceRule types removed

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

As of API version 2024-10, we've removed `PriceRule` types from the GraphQL Admin API. The associated queries and mutations have been deprecated since API version 2023-03. Use the [`discountNode`](/docs/api/admin-graphql/2024-10/queries/discountNode) query instead.

The following types have been removed:

* `PriceRuleUserError` object
* `PriceRuleCustomerSelectionInput` input object
* `PriceRuleDiscountCodeInput` input object
* `PriceRuleEntitlementToPrerequisiteQuantityRatioInput` input object
* `PriceRuleInput` input object
* `PriceRuleItemEntitlementsInput` input object
* `PriceRuleItemPrerequisitesInput` input object
* `PriceRuleMoneyRangeInput` input object
* `PriceRulePrerequisiteToEntitlementQuantityRatioInput` input object
* `PriceRuleQuantityRangeInput` input object
* `PriceRuleShippingEntitlementsInput` input object
* `PriceRuleValidityPeriodInput` input object
* `PriceRuleValueInput` input object
* `priceRuleSavedSearches` query
* `PriceRuleActivate` mutation
* `PriceRuleCreate` mutation
* `PriceRuleDeactivate` mutation
* `PriceRuleDelete` mutation
* `PriceRuleDiscountCodeCreate` mutation
* `PriceRuleDiscountCodeUpdate` mutation
* `PriceRuleUpdate` mutation
* `priceRule` field on the `QueryRoot` object
* `priceRules` connection on the `QueryRoot` object
* `priceRules` connection on the `Shop` object
* `priceRuleSavedSearches` connection on the `Shop` object

### [Anchor to ProductImage value removed](/docs/api/release-notes/2024-10#productimage-value-removed)ProductImage value removed

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The `PRODUCTIMAGE` value has been removed from the [`MetafieldOwnerType`](/docs/api/admin-graphql/2024-10/enums/MetafieldOwnerType) enum. Use `MEDIA_IMAGE` instead.

### [Anchor to ProductInput fields removed](/docs/api/release-notes/2024-10#productinput-fields-removed)ProductInput fields removed

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've removed the following deprecated `ProductInput` fields from the GraphQL Admin API:

* `bodyHTML` is removed. Use the [`descriptionHtml`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-descriptionhtml) field instead.
* `privateMetaFields` is removed. Use the [`productOptions`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-productoptions) field instead.
* `standardizedProductType` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.
* `productCategory` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.
* `customProductType` is removed. Use the [`category`](/docs/api/admin-graphql/2024-10/input-objects/ProductInput#field-category) field instead.

### [Anchor to Product deletions](/docs/api/release-notes/2024-10#product-deletions)Product deletions

We've added the [`synchronous`](/docs/api/admin-graphql/2024-10/mutations/productDelete#argument-synchronous) argument to the [`productDelete`](/docs/api/admin-graphql/2024-10/mutations/productDelete) mutation. The field allows you to choose whether a product should be deleted synchronously or asynchronously.

* **Asynchronous deletion:** By setting the `synchronous` field to `false` in the `productDelete` mutation, the operation proceeds asynchronously, and returns a [`ProductDeleteOperation`](/docs/api/admin-graphql/2024-10/objects/ProductDeleteOperation) object.
* **Operation tracking:** You can track the status of the asynchronous deletion by querying the operation ID through the [`productOperation`](/docs/api/admin-graphql/2024-10/queries/productOperation#argument-id) query.

### [Anchor to Product duplications](/docs/api/release-notes/2024-10#product-duplications)Product duplications

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The [`productDuplicateAsyncV2`](/docs/api/admin-graphql/2024-10/mutations/productDuplicateAsyncV2) mutation has been removed. We've added the [`synchronous`](/docs/api/admin-graphql/2024-10/mutations/productDuplicate#argument-synchronous) argument to the `productDuplicate` mutation, allowing you to choose whether the product duplication should be processed synchronously or asynchronously.

* **Asynchronous duplication:** By setting the `synchronous` field to `false` in the `productDuplicate` mutation, the operation operates asynchronously, and returns a [`ProductDuplicateOperation`](/docs/api/admin-graphql/2024-10/objects/ProductDuplicateOperation) object.
* **Operation tracking:** You can track the status of the asynchronous duplication by querying the operation ID through the [`productOperation`](/docs/api/admin-graphql/2024-10/queries/productOperation#argument-id) query.

### [Anchor to Product input](/docs/api/release-notes/2024-10#product-input)Product input

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've removed the `input` argument on the [`productCreate`](/docs/api/admin-graphql/2024-10/mutations/productCreate) and [`productUpdate`](/docs/api/admin-graphql/2024-10/mutations/productUpdate) mutations.

Use the following `product` arguments instead:

* [`ProductCreateInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductCreateInput) on the `productCreate` mutation
* [`ProductUpdateInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductUpdateInput) on the `productUpdate` mutation

### [Anchor to Product media](/docs/api/release-notes/2024-10#product-media)Product media

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've made changes to how you work with product media by replacing the current media ID inputs with file inputs and expanding media capabilities:

* The `mediaIds` field on the [`ProductSetInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductSetInput) input object has been removed. Use the [`files`](/docs/api/admin-graphql/2024-10/input-objects/ProductSetInput#field-files) field instead to associate files to a product.
* The `mediaId` field on the [`ProductVariantSetInput`](/docs/api/admin-graphql/2024-10/input-objects/ProductVariantSetInput) input object has been removed. Use the [`file`](/docs/api/admin-graphql/2024-10/input-objects/ProductVariantSetInput#field-file) field instead to associate a file with the product variant.
* The [`FileSetInput`](/docs/api/admin-graphql/2024-10/input-objects/FileSetInput) input object is now available for working with existing media and creating new files. This input object is a derivative of the [`FileCreateInput`](/docs/api/admin-graphql/2024-10/input-objects/FileCreateInput) input object, with an added `id` field.

### [Anchor to Product mutations](/docs/api/release-notes/2024-10#product-mutations)Product mutations

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've removed the following deprecated product mutations from the GraphQL Admin API:

* [`productAppendImages`](/docs/api/admin-graphql/2024-07/mutations/productAppendImages) is removed. Use the [`productCreateMedia`](/docs/api/admin-graphql/2024-10/mutations/productCreateMedia) mutation instead.
* [`productDeleteImages`](/docs/api/admin-graphql/2024-07/mutations/productDeleteImages) is removed. Use the [`productDeleteMedia`](/docs/api/admin-graphql/2024-10/mutations/productDeleteMedia) mutation instead.
* [`productImageUpdate`](/docs/api/admin-graphql/2024-07/mutations/productImageUpdate) is removed. Use the [`productUpdateMedia`](/docs/api/admin-graphql/2024-10/mutations/productUpdateMedia) mutation instead.
* [`productReorderImages`](/docs/api/admin-graphql/2024-07/mutations/productReorderImages) is removed. Use the [`productReorderMedia`](/docs/api/admin-graphql/2024-10/mutations/productReorderMedia) mutation instead.

### [Anchor to Product restrictions](/docs/api/release-notes/2024-10#product-restrictions)Product restrictions

We've added the [`restrictedForResource`](/docs/api/admin-graphql/2024-10/objects/Product#field-restrictedforresource) field to the `Product` object. The field allows you to query product restrictions for a given [`CalculatedOrder`](/docs/api/admin-graphql/2024-10/objects/CalculatedOrder) object, and returns both the restricted status and the reason for the restriction.

### [Anchor to Product taxonomy](/docs/api/release-notes/2024-10#product-taxonomy)Product taxonomy

We've deprecated the [`PRODUCT_TAXONOMY_NODE_ID`](/docs/api/admin-graphql/2024-10/enums/CollectionRuleColumn#value-producttaxonomynodeid) value on the `CollectionRuleColumn` enum, which is used when creating automated collections. Use the [`PRODUCT_CATEGORY_ID`](/docs/api/admin-graphql/2024-10/enums/CollectionRuleColumn#value-producttaxonomynodeid) value instead.
For more information, refer to the [developer changelog](/changelog/introducing-product_category_id-in-collectionrulecolumn-and-deprecating-product_taxonomy_node_id-for-automated-collection-creation).

### [Anchor to Product variant mutations](/docs/api/release-notes/2024-10#product-variant-mutations)Product variant mutations

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've deprecated the following singular product variant mutations in favor of their equivalent bulk versions:

* [`productVariantCreate`](/docs/api/admin-graphql/2024-07/mutations/productvariantcreate) is deprecated. Use the [`productVariantsBulkCreate`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkcreate) mutation instead.
* [`productVariantUpdate`](/docs/api/admin-graphql/2024-07/mutations/productvariantupdate) is deprecated. Use the [`productVariantsBulkUpdate`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkupdate) mutation instead.
* [`productVariantDelete`](/docs/api/admin-graphql/2024-07/mutations/productvariantdelete) is deprecated. Use the [`productVariantsBulkDelete`](/docs/api/admin-graphql/2024-10/mutations/productvariantsbulkdelete) mutation instead.

### [Anchor to Product variants count](/docs/api/release-notes/2024-10#product-variants-count)Product variants count

We've added the [`productVariantsCount`](/docs/api/admin-graphql/2024-10/queries/productVariantsCount) query to the GraphQL Admin API to provide parity with the [REST Admin API's `ProductVariant` count endpoint](/docs/api/admin-rest/2024-10/resources/product-variant#get-products-product-id-variants-count).

### [Anchor to Product variants strategy](/docs/api/release-notes/2024-10#product-variants-strategy)Product variants strategy

We've added the [`variantStrategy`](/docs/api/admin-graphql/2024-10/mutations/productOptionsCreate#argument-variantstrategy) argument to the `productOptionsCreate` mutation, which enables more precise control over product variant configuration and inventory management.

The `variantStrategy` argument includes the following input fields:

* `CREATE`: Generates new product variants for all possible combinations of option values.
* `LEAVE_AS_IS`: Updates existing variants to include new option values, without creating new variants.

### [Anchor to Products webhook topics](/docs/api/release-notes/2024-10#products-webhook-topics)Products webhook topics

The [`PRODUCTS_CREATE`](/docs/api/webhooks/2024-10?reference=graphql#list-of-topics-products_create) and [`PRODUCTS_UPDATE`](/docs/api/webhooks/2024-10?reference=graphql#list-of-topics-products_update) webhook payloads now contain the following fields:

* `has_variants_that_requires_components`: Indicates whether a product has a variant that's a [product bundle](/docs/apps/build/product-merchandising/bundles). The field mirrors the [`hasVariantsThatRequiresComponents`](/docs/api/admin-graphql/2024-10/objects/Product#field-product-hasvariantsthatrequirescomponents) field on the `Product` object.
* `category`: Information about the product category associated with a product. The [`category`](/docs/api/admin-graphql/2024-10/objects/Product#field-category) field exposes a trimmed version of fields that are available on the `Product` object.

### [Anchor to Redirects count](/docs/api/release-notes/2024-10#redirects-count)Redirects count

You can now use the [`urlRedirectsCount`](/docs/api/admin-graphql/2024-10/queries/urlRedirectsCount) query to retrieve a count of redirects. Previously, this functionality was only available using the REST Admin API.

### [Anchor to Refunding multiple shipping lines](/docs/api/release-notes/2024-10#refunding-multiple-shipping-lines)Refunding multiple shipping lines

You can now refund multiple shipping lines using the [`shipping`](/docs/api/admin-graphql/2024-10/input-objects/RefundInput#field-shipping) field on the `RefundInput` input object or [`refundShipping`](/docs/api/admin-graphql/2024-10/input-objects/ReturnRefundInput#field-refundshipping) field on the `ReturnRefundInput` input object.

For more information, refer to the [developer changelog](/changelog/refunding-orders-with-multiple-shipping-lines-returns-accurate-data).

### [Anchor to Removed fields on ShopFeatures object](/docs/api/release-notes/2024-10#removed-fields-on-shopfeatures-object)Removed fields on ShopFeatures object

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The following deprecated fields on the [`ShopFeatures`](/docs/api/admin-graphql/2024-10/objects/ShopFeatures) object have been removed:

* `avalaraAvatax`
* `branding`
* `captcha`
* `dynamicRemarketing`
* `harmonizedSystemCode`
* `liveView`
* `onboardingVisual`
* `reports`
* `showMetrics`

Instead of the `branding` field, use [`Shop.plan.shopifyPlus`](/docs/api/admin-graphql/2024-10/objects/Shop#field-plan) instead.

### [Anchor to Removed V2 on Fulfillment mutations](/docs/api/release-notes/2024-10#removed-v2-on-fulfillment-mutations)Removed V2 on Fulfillment mutations

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've deprecated the [`fulfillmentCreateV2`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreateV2) and [`fulfillmentTrackingInfoUpdateV2`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentTrackingInfoUpdateV2) mutations. Use the [`fulfillmentCreate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentCreate) and [`fulfillmentTrackingInfoUpdate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentTrackingInfoUpdate) mutations instead.

The behavior of the new mutations remains the same as the previous ones. The only change is the removal of `V2` to ensure consistent naming across all mutations.

### [Anchor to Return approvals and rejections](/docs/api/release-notes/2024-10#return-approvals-and-rejections)Return approvals and rejections

We've added the `notifyCustomer` field on the [`ReturnApproveRequestInput`](/docs/api/admin-graphql/2024-10/input-objects/ReturnApproveRequestInput#field-notifycustomer) input object and the [`ReturnDeclineRequestInput`](/docs/api/admin-graphql/2024-10/input-objects/ReturnDeclineRequestInput#field-notifycustomer) input object.

We've also added the [`declineNote`](/docs/api/admin-graphql/2024-10/input-objects/ReturnDeclineRequestInput#field-declinenote) field on the `ReturnDeclineRequestInput` input object, which represents the notification message that's sent to a customer about their declined return request.

### [Anchor to Reverse fulfillment orders](/docs/api/release-notes/2024-10#reverse-fulfillment-orders)Reverse fulfillment orders

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

The [`reverseDeliveryDispose`](/docs/api/admin-graphql/2024-07/mutations/reverseDeliveryDispose) mutation is deprecated. Use the [`reverseFulfillmentOrderDispose`](/docs/api/admin-graphql/2024-10/mutations/reverseFulfillmentOrderDispose) mutation instead.

The [`fulfillmentLineItem`](/docs/api/admin-graphql/2024-10/objects/ReverseFulfillmentOrderLineItem#field-fulfillmentlineitem) field on the `ReverseFulfillmentOrderLineItem` object is now nullable. A `ReverseFulfillmentOrderLineItem` object won't always be associated with a `FulfillmentLineItem` object. The non-null `fulfillmentLineItem` field on API versions prior to 2024-10 returns an error when the fulfillment line item doesn't exist.

[Learn more about managing reverse fulfillment orders](/docs/apps/build/orders-fulfillment/returns-apps/manage-reverse-fulfillment-orders).

### [Anchor to Rounding adjustments on cash amounts](/docs/api/release-notes/2024-10#rounding-adjustments-on-cash-amounts)Rounding adjustments on cash amounts

We've added the [`amountRounding`](/docs/api/admin-graphql/2024-10/objects/OrderTransaction#field-amountrounding) field on the `OrderTransaction` object. The `amountRounding` field represents the rounding adjustment applied on a cash amount in presentment currency.

### [Anchor to Setting available inventory quantity](/docs/api/release-notes/2024-10#setting-available-inventory-quantity)Setting available inventory quantity

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

We've deprecated the ability to set the available quantity on the [`inventoryActivate`](/docs/api/admin-graphql/2024-10/mutations/inventoryActivate) mutation for inventory items that are already in an active state. Use the [`inventorySetQuantities`](/docs/api/admin-graphql/2024-10/mutations/inventorySetQuantities) mutation instead.

We've also added the [`INVALID_QUANTITY_TOO_LOW`](/docs/api/admin-graphql/2024-10/enums/InventorySetQuantitiesUserErrorCode#value-invalidquantitytoolow) value to the `InventorySetQuantitiesUserErrorCode` enum. The error code is returned if you run the `inventorySetQuantities` mutation and a quantity is less than negative one billion.

### [Anchor to Shop owner name](/docs/api/release-notes/2024-10#shop-owner-name)Shop owner name

We've added the [`shopOwnerName`](/docs/api/admin-graphql/2024-10/objects/Shop#field-shopownername) field to the `Shop` object. The field returns the shop owner's first and last name.

### [Anchor to Shopify Payments disputes](/docs/api/release-notes/2024-10#shopify-payments-disputes)Shopify Payments disputes

You can now use the [`ShopifyPaymentsDispute`](/docs/api/admin-graphql/2024-10/objects/ShopifyPaymentsDispute) object to query all Shopify Payments disputes that are associated with a store.

We've also added the [`ADVANCE`](/docs/api/admin-graphql/2024-10/enums/ShopifyPaymentsTransactionType#value-advance) and [`ADVANCE_FUNDING`](/docs/api/admin-graphql/2024-10/enums/ShopifyPaymentsTransactionType#value-advancefunding) values to the `ShopifyPaymentsTransactionType` enum.

### [Anchor to Shopify Payments payouts](/docs/api/release-notes/2024-10#shopify-payments-payouts)Shopify Payments payouts

We've added the [`advanceFees`](/docs/api/admin-graphql/2024-10/objects/ShopifyPaymentsPayoutSummary#field-advancefees) and [`advanceGross`](/docs/api/admin-graphql/2024-10/objects/ShopifyPaymentsPayoutSummary#field-advancegross) fields to the `ShopifyPaymentsPayoutSummary` object.

### [Anchor to Subscription billing attempts](/docs/api/release-notes/2024-10#subscription-billing-attempts)Subscription billing attempts

We've added the [`transactions`](/docs/api/admin-graphql/2024-10/objects/SubscriptionBillingAttempt#connection-transactions) connection to the `SubscriptionBillingAttempt` object. The connection returns the transactions that are created by billing attempts.

### [Anchor to Subscription contracts](/docs/api/release-notes/2024-10#subscription-contracts)Subscription contracts

We've added the [`lastBillingAttemptErrorType`](/docs/api/admin-graphql/2024-10/objects/SubscriptionContract#field-lastbillingattempterrortype) field to the `SubscriptionContract` object. You can use this field to determine the billing error type when a billing attempt fails.

### [Anchor to Tender transactions](/docs/api/release-notes/2024-10#tender-transactions)Tender transactions

We've added the [`order`](/docs/api/admin-graphql/2024-10/objects/TenderTransaction#field-order) field to the `TenderTransaction` object. You can use the field to retrieve an order that's related to a transaction with financial impact on a store's balance sheet. If the order has been deleted, then the value is `null`.

### [Anchor to Translatable resources](/docs/api/release-notes/2024-10#translatable-resources)Translatable resources

We've added the [`ONLINE_STORE_THEME_APP_EMBED`](/docs/api/admin-graphql/2024-10/enums/TranslatableResourceType#value-onlinestorethemeappembed) value to the `TranslatableResourceType` enum. You can use this value to query the translatable content for an embedded app.

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/2024-10#rest-admin-api-changes)REST Admin API changes

Legacy

The REST Admin API is a legacy API as of October 1, 2024. All apps and integrations should be built with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

**Legacy:**

The REST Admin API is a legacy API as of October 1, 2024. All apps and integrations should be built with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Version 2024-10 of the REST Admin API introduces the following changes:

### [Anchor to Business entities](/docs/api/release-notes/2024-10#business-entities)Business entities

Large merchants with an established international presence need to be able to specify which of their business entities handles sales for a given buyer context. You can now use the REST Admin API to request the business entity ID (`merchant_business_entity_id`) associated with an [order](/docs/api/admin-rest/2024-10/resources/order).

### [Anchor to Comment events](/docs/api/release-notes/2024-10#comment-events)Comment events

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

On the [`Event`](/docs/api/admin-rest/2024-10/resources/event) resource, we now return `null` when underlying subject data has been deleted. You must update your code to handle `null` cases. For example, revise existing logic that assumes the field will always contain data, and implement checks or fallback mechanisms to manage situations where subject data has been deleted.

### [Anchor to Delivery options](/docs/api/release-notes/2024-10#delivery-options)Delivery options

The `presented_name` property has been added to the [`FulfillmentOrder`](/docs/api/admin-rest/2024-10/resources/fulfillmentorder) resource. The `presented_name` property represents the name of the delivery option that was presented to the customer during checkout.

### [Anchor to Location resource](/docs/api/release-notes/2024-10#location-resource)Location resource

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

If your app retrieves a [`Location`](/docs/api/admin-rest/2024-10/resources/location) resource, then you need to request the `read_locations` access scope.

If your app reads a `Location` resource without the `read_locations` access scope, then a [403 Forbidden error](/docs/api/admin-rest#status_and_error_codes) is returned.

### [Anchor to Products webhook topics](/docs/api/release-notes/2024-10#products-webhook-topics)Products webhook topics

The [`products/create`](/docs/api/webhooks/2024-10?reference=rest#list-of-topics-products/create) and [`products/update`](/docs/api/webhooks/2024-10?reference=rest#list-of-topics-products/update) webhook payloads now contain the following properties:

* `has_variants_that_requires_components`: Indicates whether a product has a variant that's a [product bundle](/docs/apps/build/product-merchandising/bundles)
* `category`: Information about the product category that's associated with a product

### [Anchor to Refunding multiple shipping lines](/docs/api/release-notes/2024-10#refunding-multiple-shipping-lines)Refunding multiple shipping lines

You can now refund multiple shipping lines using the [`Refunds`](/docs/api/admin-rest/2024-10/resources/refund) resource in the REST Admin API.

For more information, refer to the [developer changelog](/changelog/refunding-orders-with-multiple-shipping-lines-returns-accurate-data).

### [Anchor to Rounding adjustments on cash amounts](/docs/api/release-notes/2024-10#rounding-adjustments-on-cash-amounts)Rounding adjustments on cash amounts

We've added the [`amount_rounding`](/docs/api/admin-rest/2024-10/resources/transaction#resource-object) property on the `Transaction` resource. The `amount_rounding` property represents the rounding adjustment applied on a cash amount in presentment currency.

---

## [Anchor to Storefront API changes](/docs/api/release-notes/2024-10#storefront-api-changes)Storefront API changes

Version 2024-10 of the Storefront API introduces the following changes:

### [Anchor to Cart warnings](/docs/api/release-notes/2024-10#cart-warnings)Cart warnings

#### [Anchor to Breaking](/docs/api/release-notes/2024-10#breaking)Breaking

Inventory errors about stock levels are no longer included in the `userErrors` of cart mutations. Inventory errors are now available in the `warnings` return field, and contain the following explicit values:

* `MERCHANDISE_NOT_ENOUGH_STOCK`
* `MERCHANDISE_OUT_OF_STOCK`

Warnings are available on all cart mutations to show automatic changes that occurred while executing the mutation. You can use warnings to manage items in your cart or display information to a buyer. For example, you can remove out-of-stock lines from a cart by using the [`target`](/docs/api/storefront/2024-10/mutations/cartLinesRemove#field-cartlinesremovepayload-warnings) field included in the `warning` as the input to the `cartLinesRemove` mutation.

[Learn more about cart warnings](/docs/storefronts/headless/building-with-the-storefront-api/cart/cart-warnings).

### [Anchor to Shop Pay installments pricing](/docs/api/release-notes/2024-10#shop-pay-installments-pricing)Shop Pay installments pricing

We've added `ShopPayInstallmentsPricing` fields to the [`Shop`](/docs/api/storefront/2024-10/objects/Shop) and [`ProductVariant`](/docs/api/storefront/2024-10/objects/ProductVariant) types. In the future, Hydrogen will support using these fields to display the [Shop Pay installments banner](https://help.shopify.com/manual/payments/shop-pay-installments/product-banner) on the product page. These require the `unauthenticated_read_shop_pay_installments_pricing` access scope.

### [Anchor to Combined listings support](/docs/api/release-notes/2024-10#combined-listings-support)Combined listings support

You can now query [combined listings](/docs/apps/build/product-merchandising/combined-listings) products.

The [`options`](/docs/api/storefront/2024-10/objects/Product#field-options) field on the `Product` object returns options and values for both parent and child products. We've also added the following fields to simplify working with complex products:

* [`Product.adjacentVariants`](/docs/api/storefront/2024-10/objects/Product#field-adjacentvariants)
* [`Product.selectedOrFirstAvailableVariant`](/docs/api/storefront/2024-10/objects/Product#field-selectedorfirstavailablevariant)
* [`Product.encodedVariantAvailability`](/docs/api/storefront/2024-10/objects/Product#field-encodedvariantavailability)
* [`Product.encodedVariantExistence`](/docs/api/storefront/2024-10/objects/Product#field-encodedvariantexistence)
* [`ProductOptionValue.firstSelectableVariant`](/docs/api/storefront/2024-10/objects/ProductOptionValue#field-firstselectablevariant)

In the future, you'll be able to use these fields in [Hydrogen](/docs/api/hydrogen) to build option pickers and display combined listings and other complex products on a storefront.

---

## [Anchor to Shopify Function APIs changes](/docs/api/release-notes/2024-10#shopify-function-apis-changes)Shopify Function APIs changes

Version 2024-10 of the Shopify Function APIs introduces the following changes:

### [Anchor to Fulfillment constraints](/docs/api/release-notes/2024-10#fulfillment-constraints)Fulfillment constraints

You can now associate a [fulfillment constraint function](/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function) to one or multiple delivery methods, such as `SHIPPING` and `PICKUP`. The function will only run under the context of the specified delivery methods.

We've added the [`deliveryMethodTypes`](/docs/api/admin-graphql/2024-10/objects/FulfillmentConstraintRule#field-deliverymethodtypes) field to the `FulfillmentConstraintRule` object. You can use the [`fulfillmentConstraintRuleCreate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentConstraintRuleCreate) mutation to register your fulfillment constraint function and associate it with one or more delivery methods.

Use the [`fulfillmentConstraintRuleUpdate`](/docs/api/admin-graphql/2024-10/mutations/fulfillmentConstraintRuleUpdate) mutation to update delivery methods for an existing registered function.

### [Anchor to Metafields support for the cartTransformCreate mutation](/docs/api/release-notes/2024-10#metafields-support-for-the-carttransformcreate-mutation)Metafields support for the cartTransformCreate mutation

We've added the [`metafields`](/docs/api/admin-graphql/2024-10/mutations/cartTransformCreate#argument-metafields) argument to the `cartTransformCreate` mutation. You can use the argument to set metafields for a [`CartTransform`](/docs/api/admin-graphql/2024-10/objects/CartTransform) object at creation without needing to call the [`metafieldsSet`](/docs/api/admin-graphql/2024-10/mutations/metafieldsSet) mutation in a subsequent call.

[Learn more about the Cart Transform Function API](/docs/api/functions/reference/cart-transform).

---

## [Anchor to Customer Account API changes](/docs/api/release-notes/2024-10#customer-account-api-changes)Customer Account API changes

Version 2024-10 of the Customer Account API introduces the following changes:

### [Anchor to Deposits for payment terms](/docs/api/release-notes/2024-10#deposits-for-payment-terms)Deposits for payment terms

You can now query the [percentage-based deposit requirement](/docs/api/customer/2024-10/objects/DepositPercentage) for your payment terms on company locations.

[Learn more about deposits](https://help.shopify.com/manual/b2b/payment-terms#deposits).

### [Anchor to Subscription contracts](/docs/api/release-notes/2024-10#subscription-contracts)Subscription contracts

We've added new types for subscription contracts. The `customer_read_own_subscription_contracts` permission is now required to query subscription contracts and the `customer_write_own_subscription_contracts` permission is required to run subscription contracts mutations.

The following new types for managing subscription contracts are available:

New types for managing subscription contracts

| Name | Type | Change |
| --- | --- | --- |
| `SubscriptionBillingCycleInput` | Input object | Added |
| `SubscriptionBillingCycleSelector` | Input object | Added |
| `SubscriptionDeliveryMethodInput` | Input object | Added |
| `SubscriptionDeliveryMethodLocalDeliveryInput` | Input object | Added |
| `SubscriptionDeliveryMethodPickupInput` | Input object | Added |
| `SubscriptionDeliveryMethodShippingInput` | Input object | Added |
| `SubscriptionContractStatusUpdateUserError` | Object | Added |
| `SubscriptionContractUserError` | Object | Added |
| `SubscriptionDeliveryMethodLocalDeliveryOption` | Object | Added |
| `SubscriptionDeliveryMethodLocalDelivery` | Object | Added |
| `SubscriptionDeliveryMethodPickupOption` | Object | Added |
| `SubscriptionDeliveryMethodPickup` | Object | Added |
| `SubscriptionDeliveryMethodShippingOption` | Object | Added |
| `SubscriptionDeliveryMethodShipping` | Object | Added |
| `SubscriptionLine` | Object | Added |
| `SubscriptionLocalDeliveryOption` | Object | Added |
| `SubscriptionPickupOption` | Object | Added |
| `SubscriptionMailingAddress` | Object | Added |
| `SubscriptionShippingOption` | Object | Added |
| `SubscriptionDeliveryMethod` | Union | Added |
| `SubscriptionDeliveryOption` | Union | Added |
| `SubscriptionContractBase` | Interface | Added |
| `address` | Argument | Added to `SubscriptionContractFetchDeliveryOptions` mutation |

---

Was this page helpful?

YesNo