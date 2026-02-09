---
source: https://shopify.dev/docs/api/release-notes/2024-04
---

Note

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

**Note:**

We're no longer publishing API release notes. Instead, you can find the latest updates on Shopify APIs in our [developer changelog](https://shopify.dev/changelog). You can filter updates by area. For example, you can filter API updates by the API name and version, such as GraphQL Admin API changes in version 2025-04.

The API version release date and the date that the version is no longer supported

| Release date | Date version is no longer supported |
| --- | --- |
| April 1, 2024 | April 1, 2025 |

---

## [Anchor to Highlights](/docs/api/release-notes/previous-versions/2024-04#highlights)Highlights

Here are some highlights of version 2024-04 of Shopify's APIs:

### [Anchor to Deprecations: Storefront API and REST Admin API](/docs/api/release-notes/previous-versions/2024-04#deprecations-storefront-api-and-rest-admin-api)Deprecations: Storefront API and REST Admin API

This release deprecates the following parts of Shopify's APIs:

* [Storefront API](#storefront-api-changes): `Checkout` mutations, queries, and types
* [REST Admin API](#rest-admin-api-changes): `Checkout` resource

These items will sunset on April 1, 2025 (API version 2025-04). Before then, migrate your apps to:

* [Cart API](/docs/storefronts/headless/building-with-the-storefront-api/cart/manage). To learn more, read [Migrate to the Storefront Cart API](/docs/storefronts/headless/building-with-the-storefront-api/cart/migrate-to-cart-api).
* [Checkout Kit](/docs/storefronts/mobile/checkout-kit). This library enables one-page checkout for iOS, Android, and React Native apps.

For more information, refer to [Deprecation of Checkout APIs](/changelog/deprecation-of-checkout-apis).

### [Anchor to GraphQL Admin API](/docs/api/release-notes/previous-versions/2024-04#graphql-admin-api)GraphQL Admin API

The [GraphQL Admin API](#graphql-admin-api-changes) now includes new product types that support up to 2048 variants, increasing per-product variant support from our historical maximum of 100. As part of these changes, GraphQL types and REST resources for managing product variants and options are deprecated.

All public apps that are built on existing GraphQL product APIs or REST product APIs must migrate to the [new GraphQL product APIs](/docs/apps/build/graphql/migrate/new-product-model) by February 1, 2025.

Custom apps that are built using the existing GraphQL product APIs must [migrate](/docs/apps/build/graphql/migrate/new-product-model) to the new GraphQL product APIs by April 1, 2025.

Custom apps that are built on REST will also need to [migrate](/docs/apps/build/graphql/migrate/new-product-model) if they need to support more than 100 variants.

Custom apps that don't need to support more than 100 variants can continue to use the deprecated REST product APIs. However, please note the following:

* Developers should expect that the GraphQL API will be the only supported API over the long term and will be made aware of these timelines as they become available.
* The deprecated REST product APIs are in maintenance mode. All new features and support will be built only for the new GraphQL product APIs.
* Any merchant using custom apps that are built with these deprecated APIs will not be able to increase their variant limit past 100.

---

## [Anchor to Breaking changes](/docs/api/release-notes/previous-versions/2024-04#breaking-changes)Breaking changes

These changes require special attention. If your app uses these API resources, and you don’t adjust your usage of the resources according to the following instructions, then your app might break when you update to this API version.

### [Anchor to Checkout API Deprecation](/docs/api/release-notes/previous-versions/2024-04#checkout-api-deprecation)Checkout API Deprecation

We've deprecated the Checkout APIs. For more information, refer to [Deprecation of Checkout APIs](/changelog/deprecation-of-checkout-apis).

### [Anchor to Count field unification](/docs/api/release-notes/previous-versions/2024-04#count-field-unification)Count field unification

Fields that returned a count of resources are removed and replaced with new count fields that have consistent API design and improved features. Count fields are now standalone fields with a common naming pattern and their own arguments instead of being a field under a connection type.

### [Anchor to Inventory mutations and fields removal](/docs/api/release-notes/previous-versions/2024-04#inventory-mutations-and-fields-removal)Inventory mutations and fields removal

The following fields and mutations are removed:

* `InventoryLevel.available`
* `InventoryLevel.incoming`
* `InventoryLevel.deactivationAlertHtml`
* `Mutation.InventoryAdjustQuantity`
* `Mutation.InventoryBulkAdjustQuantityAtLocation`

Replace `InventoryLevel.available` and `InventoryLevel.incoming` with `InventoryLevel.quantities`.

Replace `InventoryLevel.deactivationAlertHtml` with `InventoryLevel.deactivationAlert`.

Replace `Mutation.InventoryAdjustQuantity` and `Mutation.InventoryBulkAdjustQuantityAtLocation` with `Mutation.InventoryAdjustQuantities` or `Mutation.InventoryMoveQuantities`.

### [Anchor to Locale fields on ,[object Object]](/docs/api/release-notes/previous-versions/2024-04#locale-fields-on-marketwebpresence)Locale fields on `MarketWebPresence`

The following fields on the `MarketWebPresence` object no longer return locale strings and instead make use of the `ShopLocale` type:

* `defaultLocale`
* `alternateLocales`

Update your API calls using `MarketWebPresence.defaultLocale` or `MarketWebPresence.alternateLocales` to use the `ShopLocale` type.

### [Anchor to Fulfillment request validation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-request-validation)Fulfillment request validation

We now validate that there are no duplicate fulfillment orders in requests to create a fulfillment.

**GraphQL Admin API**

You can no longer have have multiples of the same `fulfillmentOrderId` in a single request to the [`fulfillmentCreateV2`](/docs/api/admin-graphql/2024-04/mutations/fulfillmentCreateV2) mutation.

Instead, you must combine any payload with the same `fulfillmentOrderId` into one group.

**REST Admin API**

You can no longer have multiples of the same `fulfillment_order_id` within the `line_items_by_fulfillment_order` parameter, for POST calls to the REST Admin API that [create a fulfillment for one or many fulfillment orders](/docs/api/admin-rest/2024-01/resources/fulfillment#post-fulfillments).

Instead, you must combine any payload with the same `fulfillment_order_id` into one group.

### [Anchor to [object Object], deprecation](/docs/api/release-notes/previous-versions/2024-04#ordertransactionreceipt-deprecation)`OrderTransaction.receipt` deprecation

The `OrderTransaction.receipt` field has been removed, and is replaced by `receiptJson`.

### [Anchor to Payment and billing error codes and mapping](/docs/api/release-notes/previous-versions/2024-04#payment-and-billing-error-codes-and-mapping)Payment and billing error codes and mapping

Payment error codes and mappings have changed. For detailed information on the changes, refer to the [changelog](https://shopify.dev/changelog/new-error-codes-and-updated-error-code-mapping-for-payment-and-billing).

### [Anchor to Sunset of ,[object Object], mutation, GraphQL Admin API](/docs/api/release-notes/previous-versions/2024-04#sunset-of-productduplicateasync-mutation-graphql-admin-api)Sunset of `productDuplicateAsync` mutation, GraphQL Admin API

We've removed the `productDuplicateAsync` mutation, which has been deprecated since version 2023-07, from the GraphQL Admin API.

Use the [`productDuplicateAsyncV2`](/docs/api/admin-graphql/2024-04/mutations/productDuplicateAsyncV2) mutation instead.

---

## [Anchor to Customer Account API](/docs/api/release-notes/previous-versions/2024-04#customer-account-api)Customer Account API

Version 2024-04 of the Customer Account API introduces the following changes:

### [Anchor to Company and CompanyLocation metafields](/docs/api/release-notes/previous-versions/2024-04#company-and-companylocation-metafields)Company and CompanyLocation metafields

You now have read access to metafields on [`Company`](/docs/api/customer/2024-04/objects/Company) and [`CompanyLocation`](/docs/api/customer/2024-04/objects/CompanyLocation) objects on the Customer Account API.

Learn more about the [`Metafield`](/docs/api/customer/2024-04/objects/Metafield) object on the Customer Account API.

---

## [Anchor to GraphQL Admin API changes](/docs/api/release-notes/previous-versions/2024-04#graphql-admin-api-changes)GraphQL Admin API changes

Version 2024-04 of the GraphQL Admin API introduces the following changes:

### [Anchor to Additional information for delivery methods](/docs/api/release-notes/previous-versions/2024-04#additional-information-for-delivery-methods)Additional information for delivery methods

The [`DeliveryMethodAdditionalInformation`](/docs/api/admin-graphql/2024-04/objects/DeliveryMethodAdditionalInformation) object has been added, which supports additional information on delivery methods to assist during the delivery process.

The [`additionalInformation`](/docs/api/admin-graphql/2024-04/objects/DeliveryMethod#field-deliverymethod-additionalinformation) field is added to the `deliveryMethod` object, which enables additional information to be read when performing a delivery.

### [Anchor to Charge custom amounts](/docs/api/release-notes/previous-versions/2024-04#charge-custom-amounts)Charge custom amounts

* The [`amount`](/docs/api/admin-graphql/2024-04/mutations/orderCreateMandatePayment#argument-amount) argument has been added to the `orderCreateMandatePayment` mutation.

  Use this argument to specify custom amounts to be charged from a vaulted card for Shopify Plus merchants.

### [Anchor to Checkout header and footer customization](/docs/api/release-notes/previous-versions/2024-04#checkout-header-and-footer-customization)Checkout header and footer customization

The [`CheckoutBranding`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding) object now enables you to customize the header and footer that displays at **Checkout** and **Thank you** pages to represent a merchant's brand. In the object and mutation, header and footer customizations are available on the [`customizations`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding#field-checkoutbranding-customizations) data object.

For example, you can hide the logo, breadcrumbs, default footer content, and **Back to cart** link, and control the footer position and alignment. On one-page checkout, you can customize the back to cart link with a custom icon.

The following new fields are available:

New types for customizing headers and footers

| Name | Type | Change |
| --- | --- | --- |
| `buyerJourney` (breadcrumbs) | Field | Added |
| `cartLink` | Field | Added |
| `cart_link` | Field | Added to the `header` field |
| `colorScheme` | Field | Added |
| `footer` | Field | Added |
| `padding` | Field | Added |

Learn how to customize the [header](/docs/apps/build/checkout/customize-header) and [footer](/docs/apps/build/checkout/customize-footer) for common use cases, using the GraphQL Admin API and checkout UI extensions.

### [Anchor to Checkout section styling](/docs/api/release-notes/previous-versions/2024-04#checkout-section-styling)Checkout section styling

You can now use the [`CheckoutBranding`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding) object to style sections of checkout and order summary. Section styling is used to highlight or contour the look of a page, creating high visual impact and expressiveness in structured content.

In the object and mutation, section customizations are available on the [`customizations`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding#field-checkoutbranding-customizations) and [`design-system`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding#field-checkoutbranding-designsystem) data objects.

The following are the data structures, which illustrate the customization capabilities now available through the API:

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

designSystem {

colors {

schemes {

scheme3 {

base {

background

text

border

icon

accent

decorative

}

control {

background

text

border

icon

accent

decorative

selected {

background

text

border

icon

accent

decorative

}

}

primaryButton {

background

text

border

icon

accent

decorative

hover {

background

text

border

icon

accent

decorative

}

}

secondaryButton {

background

text

border

icon

accent

decorative

hover {

background

text

border

icon

accent

decorative

}

}

}

scheme4 {

base {

background

text

border

icon

accent

decorative

}

control {

background

text

border

icon

accent

decorative

selected {

background

text

border

icon

accent

decorative

}

}

primaryButton {

background

text

border

icon

accent

decorative

hover {

background

text

border

icon

accent

decorative

}

}

secondaryButton {

background

text

border

icon

accent

decorative

hover {

background

text

border

icon

accent

decorative

}

}

}

}

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

customizations {

main {

section {

background

colorScheme

cornerRadius

border

borderStyle

borderWidth

padding

shadow

}

}

orderSummary {

section {

background

colorScheme

cornerRadius

border

borderStyle

borderWidth

padding

shadow

}

}

expressCheckout {

button {

cornerRadius

}

}

}

##### design-system

```liquid
designSystem {
  colors {
    schemes {
      scheme3 {
        base {
          background
          text
          border
          icon
          accent
          decorative
        }
        control {
          background
          text
          border
          icon
          accent
          decorative
          selected {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
        primaryButton {
          background
          text
          border
          icon
          accent
          decorative
          hover {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
        secondaryButton {
          background
          text
          border
          icon
          accent
          decorative
          hover {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
      }
      scheme4 {
        base {
          background
          text
          border
          icon
          accent
          decorative
        }
        control {
          background
          text
          border
          icon
          accent
          decorative
          selected {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
        primaryButton {
          background
          text
          border
          icon
          accent
          decorative
          hover {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
        secondaryButton {
          background
          text
          border
          icon
          accent
          decorative
          hover {
            background
            text
            border
            icon
            accent
            decorative
          }
        }
      }
    }
  }
}
```

##### customizations

```liquid
customizations {
  main {
    section {
      background
      colorScheme
      cornerRadius
      border
      borderStyle
      borderWidth
      padding
      shadow
    }
  }
  orderSummary {
    section {
      background
      colorScheme
      cornerRadius
      border
      borderStyle
      borderWidth
      padding
      shadow
    }
  }
  expressCheckout {
    button {
      cornerRadius
    }
  }
}
```

To learn more, refer to our tutorial on [checkout section styling](/docs/apps/build/checkout/styling/customize-sections).

### [Anchor to Checkout color schemes](/docs/api/release-notes/previous-versions/2024-04#checkout-color-schemes)Checkout color schemes

The [`CheckoutBranding`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding) object now supports configuring two new color schemes, `scheme3` and `scheme4`.

Previously, only two color schemes were available. Now you can configure up to four schemes and assign any of them to the following sections in the [`customizations`](/docs/api/admin-graphql/2024-04/objects/CheckoutBranding#field-checkoutbranding-designsystem) data object:

* `main`
* `main.section`
* `orderSummary`
* `orderSummary.section`

### [Anchor to Code-based discounts on line items](/docs/api/release-notes/previous-versions/2024-04#code-based-discounts-on-line-items)Code-based discounts on line items

The `withCodeDiscounts` argument has been added to the `LineItem` object's [`discountedTotalSet`](/docs/api/admin-graphql/2024-04/objects/LineItem#field-lineitem-discountedtotalset) field.

Use this field to either include or exclude line item discounts that originate from a discount code.

### [Anchor to Count field unification](/docs/api/release-notes/previous-versions/2024-04#count-field-unification)Count field unification

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

Fields that returned a count of resources are removed and replaced with new count fields that have consistent API design and improved features. Count fields are now standalone fields with a common naming pattern and their own arguments instead of being a field under a connection type.

Instead of varying `Int` or `UnsignedInt64` return types, all count fields now return a `Count` object type with precision and `count` fields.

Some count fields now accept filter arguments matching that of a neighboring connection, such as [`products`](/docs/api/admin-graphql/2024-04/queries/products) and [`productsCount`](/docs/api/admin-graphql/2024-04/queries/productsCount).

For detailed information on the changes, [refer to the changelog](/changelog/unification-of-count-fields).

### [Anchor to Create options linked to metafields](/docs/api/release-notes/previous-versions/2024-04#create-options-linked-to-metafields)Create options linked to metafields

You can now use the `productOptionsCreate`, `productCreate`, and `productOptionUpdate` mutations to create [metafield-linked product options](/docs/apps/build/product-merchandising/products-and-collections/metafield-linked).

Metafield-linked product options are only available in Shopify taxonomy early access.

[Learn more](/docs/apps/build/product-merchandising/products-and-collections/metafield-linked) about metafield-linked product options.

### [Anchor to Customer redaction support](/docs/api/release-notes/previous-versions/2024-04#customer-redaction-support)Customer redaction support

The error code `CUSTOMER_REDACTED` has been added to the [`subscriptionContractAtomicCreate`](/docs/api/admin-graphql/2024-04/mutations/subscriptionContractAtomicCreate) and [`subscriptionContractCreate`](/docs/api/admin-graphql/2024-04/mutations/subscriptionContractCreate) mutations.

This error code is returned when you create new subscription contracts for customers whose data is scheduled for redaction or has been redacted.

[Learn more](https://help.shopify.com/en/manual/customers/manage-customers#part-c3168705890cfe54) about erasing a customer's personal data.

Learn more about customer redaction here.

### [Anchor to Customer subscription contracts](/docs/api/release-notes/previous-versions/2024-04#customer-subscription-contracts)Customer subscription contracts

The [`subscriptionContract`](/docs/api/customer/2024-04/objects/Customer#field-customer-subscriptioncontract) and [`subscriptionContracts`](/docs/api/customer/2024-04/objects/Customer#connection-subscriptioncontracts) fields have been added to the `Customer` object.

Use these fields to query for all subscription contracts that belong to a customer, or to query for a specific subscription contract, respectively.

### [Anchor to Custom storefront attribution for abandonment events](/docs/api/release-notes/previous-versions/2024-04#custom-storefront-attribution-for-abandonment-events)Custom storefront attribution for abandonment events

The [`isFromCustomStorefront`](/docs/api/admin-graphql/2024-04/objects/Abandonment#field-abandonment-isfromcustomstorefront) field has been added to the `Abandonment` object, enabling you to determine whether an abandonment event comes from a custom storefront channel.

### [Anchor to Error codes for creating product media](/docs/api/release-notes/previous-versions/2024-04#error-codes-for-creating-product-media)Error codes for creating product media

The following error codes have been added to the [`FilesErrorCode`](/docs/api/admin-graphql/2024-04/enums/FilesErrorCode) enum:

* `PRODUCT_MEDIA_LIMIT_EXCEEDED`: Thrown when you exceed the limit of 250 media items per product
* `MISSING_ARGUMENTS`: Thrown when zero arguments are provided with the media file upload

### [Anchor to Fulfillment request validation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-request-validation)Fulfillment request validation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

We now validate that there are no duplicate fulfillment orders in requests to create a fulfillment.

You can no longer have multiples of the same `fulfillmentOrderId` in a request to the [`fulfillmentCreateV2`](/docs/api/admin-graphql/2024-04/mutations/fulfillmentCreateV2) mutation.

Instead, you must combine any payload with the same `fulfillmentOrderId` into one group.

### [Anchor to Fulfillment service opt-in deprecation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-service-opt-in-deprecation)Fulfillment service opt-in deprecation

The `fulfillmentOrdersOptIn` field on the [`FulfillmentService`](/docs/api/admin-graphql/2024-04/objects/FulfillmentService) object, along with its related types, is being deprecated because the migration to the Fulfillment Orders API is complete. All properly functioning fulfillment services now have the `fulfillmentOrdersOptIn` field set to `true`.

In the 2024-04 API version, the `fulfillmentOrdersOptIn` field becomes nullable and defaults to `true` in the `fulfillmentServiceCreate` mutation. This field will be removed from the mutation input in the next API version.

To prepare for the 2024-07 API version release, stop supplying the `fulfillmentOrdersOptIn` parameter when you create a new fulfillment service.

### [Anchor to Google Cloud Pub/Sub webhook duplicate error handling](/docs/api/release-notes/previous-versions/2024-04#google-cloud-pub-sub-webhook-duplicate-error-handling)Google Cloud Pub/Sub webhook duplicate error handling

The [`TAKEN`](/docs/api/admin-graphql/2024-04/mutations/pubSubWebhookSubscriptionCreate#field-pubsubwebhooksubscriptioncreatepayload-usererrors) enum value has been added to the list of error codes in `PubSubWebhookSubscriptionCreatePayload` returns, indicating when an address for the webhook topic has already been taken.

### [Anchor to Inventory management when updating fulfillment services](/docs/api/release-notes/previous-versions/2024-04#inventory-management-when-updating-fulfillment-services)Inventory management when updating fulfillment services

The [`inventory_management`](/docs/api/admin-graphql/2024-04/mutations/fulfillmentServiceUpdate#argument-inventorymanagement) argument has been added to the `fulfillmentServiceUpdate` mutation.

Use this field to specify whether the fulfillment service tracks product inventory and provides updates to Shopify.

### [Anchor to Inventory mutations and fields removal](/docs/api/release-notes/previous-versions/2024-04#inventory-mutations-and-fields-removal)Inventory mutations and fields removal

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

The following fields and mutations are removed:

* `InventoryLevel.available`
* `InventoryLevel.incoming`
* `InventoryLevel.deactivationAlertHtml`
* `Mutation.InventoryAdjustQuantity`
* `Mutation.InventoryBulkAdjustQuantityAtLocation`

Replace `InventoryLevel.available` and `InventoryLevel.incoming` with `InventoryLevel.quantities`.

Replace `InventoryLevel.deactivationAlertHtml` with `InventoryLevel.deactivationAlert`.

Replace `Mutation.InventoryAdjustQuantity` and `Mutation.InventoryBulkAdjustQuantityAtLocation` with `Mutation.InventoryAdjustQuantities` or `Mutation.InventoryMoveQuantities`.

[Learn more](/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states) about how to use the new fields.

### [Anchor to Locale fields return](/docs/api/release-notes/previous-versions/2024-04#locale-fields-return)Locale fields return

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

The following fields on the `MarketWebPresence` object no longer return locale strings and instead make use of the `ShopLocale` object:

* `defaultLocale`
* `alternateLocales`

Update your API calls using `MarketWebPresence.defaultLocale` or `MarketWebPresence.alternateLocales` to use the [`ShopLocale`](/docs/api/admin-graphql/2024-04/objects/ShopLocale) object instead.

### [Anchor to Media type query for product connection](/docs/api/release-notes/previous-versions/2024-04#media-type-query-for-product-connection)Media type query for product connection

The `media` connection on the `Product` object now includes a [`media_type`](/docs/api/admin-graphql/2024-04/objects/Product#connection-media-query-query-filter-media_type) filter on its `query` argument. The following are the valid values:

* `IMAGE`
* `VIDEO`
* `MODEL_3D`
* `EXTERNAL_VIDEO`

Use this filter to search the media that's associated with a product, such as images, 3D models, or videos.

### [Anchor to Metafield capability violation error code](/docs/api/release-notes/previous-versions/2024-04#metafield-capability-violation-error-code)Metafield capability violation error code

We've added the `CAPABILITY_VIOLATION` error code to additional mutations that write metafields.

### [Anchor to New fulfillment order assignment status](/docs/api/release-notes/previous-versions/2024-04#new-fulfillment-order-assignment-status)New fulfillment order assignment status

The [`FULFILLMENT_UNSUBMITTED`](/docs/api/admin-graphql/2024-04/enums/FulfillmentOrderAssignmentStatus#value-fulfillmentunsubmitted) value has been added to the set of `FulfillmentOrderAssignmentStatus` enum.

Use this value to filter fulfillment orders for which the merchant hasn't yet requested fulfillment.

### [Anchor to New fulfillment order search options](/docs/api/release-notes/previous-versions/2024-04#new-fulfillment-order-search-options)New fulfillment order search options

You can now use the following new sort options in the [fulfillmentOrders](/docs/api/admin-graphql/2024-04/queries/fulfillmentOrders) query.

* `createdAt`: The date that the fulfillment order was created.
* `fulfillBy`: The date by which the fulfillment order should be fulfilled by the merchant.

### [Anchor to New fulfillment order sort key](/docs/api/release-notes/previous-versions/2024-04#new-fulfillment-order-sort-key)New fulfillment order sort key

The [`UPDATED_AT`](/docs/api/admin-graphql/2024-04/enums/FulfillmentOrderSortKeys#value-updatedat) enum value has been added to the set of `FulfillmentOrderSortKeys`.

Use this value to prioritize your work on fulfillment orders, and reduce the query cost when you're sorting and searching through other filters.

[Learn more](/docs/api/admin-graphql/2024-04/queries/fulfillmentOrders) about sort and search parameters for fulfillment orders.

### [Anchor to New inventory item fields and product variant deprecations](/docs/api/release-notes/previous-versions/2024-04#new-inventory-item-fields-and-product-variant-deprecations)New inventory item fields and product variant deprecations

The following new fields are exposed on the `InventoryItem` object and its related input types, and some fields on `ProductVariant`, and related input types, that were marked as deprecated. These changes are all in support of removing long-deprecated fields on `ProductVariant` and removing the duplicated fields between `ProductVariant` and `InventoryItem`.

The following changes were made to `InventoryItem` and related input types:

| Name | Type | Change |
| --- | --- | --- |
| `InventoryItem.measurement` | Field | Added |
| `InventoryItemInput.harmonizedSystemCode` `InventoryItemInput.measurement`  `InventoryItemInput.requiresShipping` | Field Field  Field | Added Added  Added |
| `InventoryItemMeasurement` | Object | Added |
| `InventoryItemMeasurement.weight` | Field | Added |
| `InventoryItemMeasurementInput` | Input object | Added |
| `InventoryItemMeasurementInput.weight` | Field | Added |

The following changes were made to `ProductVariant` and related input types:

| Name | Type | Change |
| --- | --- | --- |
| `ProductVariant.fulfillmentServiceEditable` `ProductVariant.weight`  `ProductVariant.weightUnit` | Field Field  Field | Deprecated Deprecated  Deprecated |
| `ProductVariantInput.harmonizedSystemCode` `ProductVariantInput.requiresShipping`  `ProductVariantInput.weight`  `ProductVariantInput.weightUnit` | Field Field  Field  Field | Deprecated Deprecated  Deprecated  Deprecated |
| `ProductVariantsBulkInput.harmonizedSystemCode` `ProductVariantsBulkInput.requiresShipping`  `ProductVariantsBulkInput.weight`  `ProductVariantsBulkInput.weightUnit` | Field Field  Field | Deprecated Deprecated  Deprecated |

### [Anchor to Order payment status transaction](/docs/api/release-notes/previous-versions/2024-04#order-payment-status-transaction)Order payment status transaction

The [`transactions`](/docs/api/admin-graphql/2024-04/objects/OrderPaymentStatus#field-orderpaymentstatus-transactions) field has been added to the `OrderPaymentStatus` object.

Use this field to retrieve the transaction that's associated with an order's payment.

### [Anchor to Order risk deprecation](/docs/api/release-notes/previous-versions/2024-04#order-risk-deprecation)Order risk deprecation

The [`OrderRisk`](/docs/api/admin-graphql/2024-04/objects/OrderRisk) object and associated fields are deprecated.

Use the new [`OrderRiskAssessment`](/docs/api/admin-graphql/2024-04/objects/OrderRiskAssessment) object and related types instead. For example, to create assessments, you can use the new [`orderRiskAssessmentCreate`](/docs/api/admin-graphql/2024-04/mutations/orderRiskAssessmentCreate) mutation.

We've also added the new [`ORDERS_RISK_ASSESSMENT_CHANGED`](/docs/api/admin-graphql/2024-04/enums/WebhookSubscriptionTopic#value-ordersriskassessmentchanged) webhook, which is triggered when a new risk assessment is available on an order.

### [Anchor to Payment and error code mapping](/docs/api/release-notes/previous-versions/2024-04#payment-and-error-code-mapping)Payment and error code mapping

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

The following fields have been added to the [`SubscriptionBillingAttemptErrorCode`](/docs/api/admin-graphql/2024-04/enums/SubscriptionBillingAttemptErrorCode) enum:

* `CARD_NUMBER_INCORRECT`
* `INSUFFICIENT_FUNDS`
* `PAYPAL_ERROR_GENERAL`
* `PURCHASE_TYPE_NOT_SUPPORTED`
* `FRAUD_SUSPECTED`

Additionally, payment error code mappings have changed, and codes from payment processors have changed. For more information, refer to the [changelog](/changelog/new-error-codes-and-updated-error-code-mapping-for-payment-and-billing).

### [Anchor to Product model and components changes](/docs/api/release-notes/previous-versions/2024-04#product-model-and-components-changes)Product model and components changes

We've introduced a new product model that includes enhancing product-related components in the GraphQL Admin API. These changes include deprecating product-related components.

* The number of variants and options are no longer fixed at 100 and 3, respectively. Instead, the limits can vary by shop. We expect to have most shops support an initial rollout of 2K variants and 3+ options.
* We've introduced new mutations and fields for managing product options.
* We've elevated options and option values as first class entities within the data model.
* We've separated variant and option operations from product operations. Depending on your workflow, we recommend that you start managing your product variants using bulk product variant mutations.
* A `variant_gids` field will be retroactively added to all webhook versions. Product webhooks will return a full variants payload for the first 100 records, and only the variant\_ids for variants 101+.

Learn more about [working with products in GraphQL](/docs/apps/build/product-merchandising/products-and-collections/add-data), and refer to the GraphQL Admin API reference for information about product mutations and deprecated fields.

### [Anchor to Product taxonomy](/docs/api/release-notes/previous-versions/2024-04#product-taxonomy)Product taxonomy

Shopify has introduced a public product taxonomy, serving as an open-source, standardized, and global classification of products sold on Shopify. This taxonomy, composed of product categories, attributes, and attribute values, is utilized across Shopify and integrated with numerous marketplaces.

This feature enables developers to navigate the taxonomy tree for categories, attributes, and values.

To support this change the following types have been deprecated and replaced in favor of `queryRoot.taxonomy.categories`:

* `queryRoot.productTaxonomy`
* `queryRoot.productTaxonomyNodes`
* The `ProductTaxonomyNode` type has been replaced with a `TaxonomyCategory` type.
* The `productCategory` field on the [`Product`](/docs/api/admin-graphql/2024-04/objects/Product) object has been deprecated and replaced by [`category`](/docs/api/admin-graphql/2024-04/objects/Product#field-product-category). This field points towards the new [`TaxonomyCategory`](/docs/api/admin-graphql/2024-04/objects/TaxonomyCategory) object.

View the latest product taxonomy on the [taxonomy explorer](https://shopify.github.io/product-taxonomy/releases/latest/).

### [Anchor to Receipt field removal](/docs/api/release-notes/previous-versions/2024-04#receipt-field-removal)Receipt field removal

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

The `OrderTransaction.receipt` field has been removed, and is replaced by [`receiptJson`](/docs/api/admin-graphql/2024-04/objects/OrderTransaction#field-ordertransaction-receiptjson).

### [Anchor to Return sales and exchange APIs](/docs/api/release-notes/previous-versions/2024-04#return-sales-and-exchange-apis)Return sales and exchange APIs

Returns now create corresponding sales entries.

* The [`ReturnAgreement`](/docs/api/admin-graphql/2024-04/interfaces/SalesAgreement#value-returnagreementorder) type has been added to the `SalesAgreement` interface.
* The [`RETURN`](/docs/api/admin-graphql/2024-04/enums/OrderActionType#value-return) value has been added to the `OrderActionType` enum.
* The [`FEE`](/docs/api/admin-graphql/2024-04/enums/SaleLineType#value-fee) value has been added to the `SaleLineType` enum. Fees can be of the type `RestockingFee` or `ReturnShippingFee`, which represent corresponding fees on a return.

Any GraphQL Admin API consumers of `OrderActionType` or `SaleLineType` need to accept these new enum values. Previous versions of the Admin API will show these values as `UNKNOWN`.

You can now view [`ExchangeLineItems`](/docs/api/admin-graphql/2024-04/objects/ExchangeLineItem) on their associated return. This provides context on returns that will be resolved with an exchange.

A new webhook `returns/update` has been added. This webhook fires when fees or line items on a return are modified or removed. All returns webhooks will now display restock and shipping fees, as well as exchange line items.

Dispositions can no longer be created for canceled reverse fulfillment orders. This will result in the new error code `INVALID_STATE`.

### [Anchor to Shipping lines on order editing](/docs/api/release-notes/previous-versions/2024-04#shipping-lines-on-order-editing)Shipping lines on order editing

You can now add new shipping lines or remove existing shipping lines when editing an order. You can also continue to query removed shipping lines.

For detailed information, [refer to the changelog](/changelog/add-and-remove-shipping-lines-with-new-mutations-on-the-order-editing-api).

### [Anchor to Shipping line price with currency](/docs/api/release-notes/previous-versions/2024-04#shipping-line-price-with-currency)Shipping line price with currency

The [`priceWithCurrency`](/docs/api/admin-graphql/2024-04/input-objects/ShippingLineInput#field-shippinglineinput-pricewithcurrency) field has been added to the `ShippingLineInput` input object, providing the price of the shipping rate, with currency.

### [Anchor to Transaction details on voided transactions](/docs/api/release-notes/previous-versions/2024-04#transaction-details-on-voided-transactions)Transaction details on voided transactions

You can now void a transaction, and receive the corresponding transaction details, using the [`transactionVoid`](/docs/api/admin-graphql/2024-04/mutations/transactionVoid) mutation.

---

## [Anchor to REST Admin API changes](/docs/api/release-notes/previous-versions/2024-04#rest-admin-api-changes)REST Admin API changes

Version 2024-04 of the REST Admin API introduces the following changes:

### [Anchor to Checkout deprecation](/docs/api/release-notes/previous-versions/2024-04#checkout-deprecation)Checkout deprecation

The [`Checkout`](/docs/api/admin-rest/2023-07/resources/checkout) resource is deprecated and will sunset on April 1, 2025. For more information, refer to [Deprecation of Checkout APIs](/changelog/deprecation-of-checkout-apis).

### [Anchor to Fulfillment request validation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-request-validation)Fulfillment request validation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

We now validate that there are no duplicate fulfillment orders in requests to create a fulfillment.

You can no longer have multiples of the same `fulfillment_order_id` within the `line_items_by_fulfillment_order` parameter, for POST calls to the REST Admin API that [create a fulfillment for one or many fulfillment orders](/docs/api/admin-rest/2024-01/resources/fulfillment#post-fulfillments).

Instead, you must combine any payload with the same `fulfillment_order_id` into one group.

### [Anchor to Fulfillment service opt-in deprecation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-service-opt-in-deprecation)Fulfillment service opt-in deprecation

The `fulfillmentOrdersOptIn` property on the [`FulfillmentService`](/docs/api/admin-rest/2024-04/resources/fulfillmentservice) resource, along with the related endpoints, is being deprecated as the migration to the Fulfillment Orders API has been completed. All properly functioning fulfillment services now have the `fulfillmentOrdersOptIn` property set to `true`.

In the 2024-04 API version, the `fulfillmentOrdersOptIn` property becomes nullable and defaults to true in the [`POST FulfillmentService`](/docs/api/admin-rest/2024-04/resources/fulfillmentservice#post-fulfillment-services) endpoint. This field will be removed from the endpoint parameters in the next API version.

To prepare for the 2024-07 API version release, stop supplying the `fulfillmentOrdersOptIn` parameter when creating a new fulfillment service.

### [Anchor to Product model and components changes](/docs/api/release-notes/previous-versions/2024-04#product-model-and-components-changes)Product model and components changes

We've introduced a new product model that include deprecating product-related resources in the REST Admin API.

Learn more about [migrating to GraphQL](/docs/apps/build/graphql/migrate) and [working with products in GraphQL](/docs/apps/build/product-merchandising/products-and-collections/add-data).

### [Anchor to Order risk deprecation](/docs/api/release-notes/previous-versions/2024-04#order-risk-deprecation)Order risk deprecation

The [`OrderRisk`](/docs/api/admin-rest/2024-04/resources/order-risk) resource and associated endpoints are deprecated.

Use the new [`OrderRiskAssessment`](/docs/api/admin-graphql/2024-04/objects/OrderRiskAssessment) GraphQL Admin API object and related types instead. For example, to create assessments, use the new [`orderRiskAssessmentCreate`](/docs/api/admin-graphql/2024-04/mutations/orderRiskAssessmentCreate) mutation on the GraphQL Admin API.

We've also added the new [`ORDERS_RISK_ASSESSMENT_CHANGED`](/docs/api/admin-graphql/2024-04/enums/WebhookSubscriptionTopic#value-ordersriskassessmentchanged) webhook for the GraphQL Admin API, which is triggered when a new risk assessment is available on an order.

### [Anchor to Shipping lines on order editing](/docs/api/release-notes/previous-versions/2024-04#shipping-lines-on-order-editing)Shipping lines on order editing

Removed shipping lines continue to be returned in the payload of the `Order` resource. You can determine whether a shipping line has been removed by checking the value of the new attribute `is_removed`.

For detailed information, [refer to the changelog](/changelog/add-and-remove-shipping-lines-with-new-mutations-on-the-order-editing-api).

---

## [Anchor to Shopify Function APIs changes](/docs/api/release-notes/previous-versions/2024-04#shopify-function-apis-changes)Shopify Function APIs changes

Version 2024-04 of the Shopify Function APIs introduces the following changes:

### [Anchor to Cart transform API set line properties](/docs/api/release-notes/previous-versions/2024-04#cart-transform-api-set-line-properties)Cart transform API set line properties

We've added the ability to set line properties using cart transform operations.

The `attributes` field has been added to the [`MergeOperation`](/docs/api/functions/reference/cart-transform/graphql/common-objects/mergeoperation) and [`ExpandedItem`](/docs/api/functions/reference/cart-transform/graphql/common-objects/expandeditem) objects, which enable you to add `CartLine` attributes to the parent line and component line, respectively.

### [Anchor to Fulfillment request validation](/docs/api/release-notes/previous-versions/2024-04#fulfillment-request-validation)Fulfillment request validation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

You can no longer have multiples of the same `fulfillment_order_id` within the GraphQL Admin API's [`fulfillmentCreateV2`](/docs/api/admin-graphql/2024-04/mutations/fulfillmentCreateV2) mutation.

Instead, you must combine any payload with the same `fulfillment_order_id` into one group.

### [Anchor to Sunset product duplicate async mutation](/docs/api/release-notes/previous-versions/2024-04#sunset-product-duplicate-async-mutation)Sunset product duplicate async mutation

#### [Anchor to Breaking](/docs/api/release-notes/previous-versions/2024-04#breaking)Breaking

We've removed the `productDuplicateAsync` mutation, which has been deprecated since version 2023-07, from the GraphQL Admin API.

Use the [`productDuplicateAsyncV2`](/docs/api/admin-graphql/2024-04/mutations/productDuplicateAsyncV2) mutation instead.

---

## [Anchor to Storefront API changes](/docs/api/release-notes/previous-versions/2024-04#storefront-api-changes)Storefront API changes

Version 2024-04 of the Storefront API introduces the following changes:

### [Anchor to Address validation in cart](/docs/api/release-notes/previous-versions/2024-04#address-validation-in-cart)Address validation in cart

The following error codes have been added to the [`CartUserError`](/docs/api/storefront/2024-04/objects/CartUserError) object, to validate addresses:

* `ADDRESS_FIELD_CONTAINS_EMOJIS`
* `ADDRESS_FIELD_CONTAINS_HTML_TAGS`
* `ADDRESS_FIELD_CONTAINS_URL`
* `ADDRESS_FIELD_DOES_NOT_MATCH_EXPECTED_PATTERN`
* `ADDRESS_FIELD_IS_REQUIRED`
* `ADDRESS_FIELD_IS_TOO_LONG`
* `INVALID_ZIP_CODE_FOR_PROVINCE`
* `INVALID_ZIP_CODE_FOR_COUNTRY`
* `ZIP_CODE_NOT_SUPPORTED`
* `PROVINCE_NOT_FOUND`
* `UNSPECIFIED_ADDRESS_ERROR`

For error code descriptions, consult the reference for the [`code`](/docs/api/storefront/2024-04/objects/CartUserError#field-cartusererror-code) field on `CartUserError`

The [`deliveryAddressValidationStrategy`](/docs/api/storefront/2024-04/input-objects/DeliveryAddressInput#field-deliveryaddressinput-deliveryaddressvalidationstrategy) field has been added to the `DeliveryAddressInput` input object, to define the available validation strategies for delivery addresses. The following enum values are added:

* `COUNTRY_CODE_ONLY` (default): Only the country code is validated
* `STRICT`: All fields in the address are validated according to Shopify's checkout rules. If the address fails validation, then the cart won't be updated.

### [Anchor to Checkout deprecations](/docs/api/release-notes/previous-versions/2024-04#checkout-deprecations)Checkout deprecations

The following `Checkout` mutations, queries, and types are deprecated and will sunset on April 1, 2025:

Deprecated checkout types for the Storefront API

| Name | Type |
| --- | --- |
| [`CheckoutLineItemConnection`](/docs/api/storefront/unstable/connections/CheckoutLineItemConnection) | Connection |
| [`DiscountApplicationConnection`](/docs/api/storefront/unstable/connections/DiscountApplicationConnection) | Connection |
| [`FulfillmentLineItemConnection`](/docs/api/storefront/unstable/connections/FulfillmentLineItemConnection) | Connection |
| [`OrderConnection`](/docs/api/storefront/unstable/connections/OrderConnection) | Connection |
| [`OrderLineItemConnection`](/docs/api/storefront/unstable/connections/OrderLineItemConnection) | Connection |
| [`CheckoutErrorCode`](/docs/api/storefront/unstable/enums/CheckoutErrorCode) | Enum |
| [`DiscountApplicationAllocationMethod`](/docs/api/storefront/unstable/enums/DiscountApplicationAllocationMethod) | Enum |
| [`DiscountApplicationTargetSelection`](/docs/api/storefront/unstable/enums/DiscountApplicationTargetSelection) | Enum |
| [`DiscountApplicationTargetType`](/docs/api/storefront/unstable/enums/DiscountApplicationTargetType) | Enum |
| [`OrderCancelReason`](/docs/api/storefront/unstable/enums/OrderCancelReason) | Enum |
| [`OrderFulfillmentStatus`](/docs/api/storefront/unstable/enums/OrderFulfillmentStatus) | Enum |
| [`PaymentTokenType`](/docs/api/storefront/unstable/enums/PaymentTokenType) | Enum |
| [`TransactionKind`](/docs/api/storefront/unstable/enums/TransactionKind) | Enum |
| [`TransactionStatus`](/docs/api/storefront/unstable/enums/TransactionStatus) | Enum |
| [`CheckoutAttributesUpdateV2Input`](/docs/api/storefront/unstable/input-objects/CheckoutAttributesUpdateV2Input) | Input |
| [`CheckoutBuyerIdentityInput`](/docs/api/storefront/unstable/input-objects/CheckoutBuyerIdentityInput) | Input |
| [`CheckoutCreateInput`](/docs/api/storefront/unstable/input-objects/CheckoutCreateInput) | Input |
| [`CheckoutLineItemInput`](/docs/api/storefront/unstable/input-objects/CheckoutLineItemInput) | Input |
| [`CheckoutLineItemUpdateInput`](/docs/api/storefront/unstable/input-objects/CheckoutLineItemUpdateInput) | Input |
| [`CreditCardPaymentInputV2`](/docs/api/storefront/unstable/input-objects/CreditCardPaymentInputV2) | Input |
| [`TokenizedPaymentInputV3`](/docs/api/storefront/unstable/input-objects/TokenizedPaymentInputV3) | Input |
| [`DiscountApplication`](/docs/api/storefront/unstable/interfaces/DiscountApplication) | Interface |
| [`checkoutAttributesUpdateV2`](/docs/api/storefront/unstable/mutations/checkoutAttributesUpdateV2) | Mutation |
| [`checkoutCreate`](/docs/api/storefront/unstable/mutations/checkoutCreate) | Mutation |
| [`checkoutCompleteFree`](/docs/api/storefront/unstable/mutations/checkoutCompleteFree) | Mutation |
| [`checkoutCompleteWithCreditCardV2`](/docs/api/storefront/unstable/mutations/checkoutCompleteWithCreditCardV2) | Mutation |
| [`checkoutCompleteWithTokenizedPaymentV3`](/docs/api/storefront/unstable/mutations/checkoutCompleteWithTokenizedPaymentV3) | Mutation |
| [`checkoutCustomerAssociateV2`](/docs/api/storefront/unstable/mutations/checkoutCustomerAssociateV2) | Mutation |
| [`checkoutCustomerDisassociateV2`](/docs/api/storefront/unstable/mutations/checkoutCustomerDisassociateV2) | Mutation |
| [`checkoutDiscountCodeApplyV2`](/docs/api/storefront/unstable/mutations/checkoutDiscountCodeApplyV2) | Mutation |
| [`checkoutDiscountCodeRemove`](/docs/api/storefront/unstable/mutations/checkoutDiscountCodeRemove) | Mutation |
| [`checkoutEmailUpdateV2`](/docs/api/storefront/unstable/mutations/checkoutEmailUpdateV2) | Mutation |
| [`checkoutGiftCardRemoveV2`](/docs/api/storefront/unstable/mutations/checkoutGiftCardRemoveV2) | Mutation |
| [`checkoutGiftCardsAppend`](/docs/api/storefront/unstable/mutations/checkoutGiftCardsAppend) | Mutation |
| [`checkoutLineItemsAdd`](/docs/api/storefront/unstable/mutations/checkoutLineItemsAdd) | Mutation |
| [`checkoutLineItemsRemove`](/docs/api/storefront/unstable/mutations/checkoutLineItemsRemove) | Mutation |
| [`checkoutLineItemsReplace`](/docs/api/storefront/unstable/mutations/checkoutLineItemsReplace) | Mutation |
| [`checkoutLineItemsUpdate`](/docs/api/storefront/unstable/mutations/checkoutLineItemsUpdate) | Mutation |
| [`checkoutShippingAddressUpdateV2`](/docs/api/storefront/unstable/mutations/checkoutShippingAddressUpdateV2) | Mutation |
| [`checkoutShippingLineUpdate`](/docs/api/storefront/unstable/mutations/checkoutShippingLineUpdate) | Mutation |
| [`AvailableShippingRates`](/docs/api/storefront/unstable/objects/AvailableShippingRates) | Object |
| [`AppliedGiftCard`](/docs/api/storefront/unstable/objects/AppliedGiftCard) | Object |
| [`AutomaticDiscountApplication`](/docs/api/storefront/unstable/objects/AutomaticDiscountApplication) | Object |
| [`Checkout`](/docs/api/storefront/unstable/objects/Checkout) | Object |
| [`CheckoutUserError`](/docs/api/storefront/unstable/objects/CheckoutUserError) | Object |
| [`CheckoutLineItem`](/docs/api/storefront/unstable/objects/CheckoutLineItem) | Object |
| [`CheckoutLineItemEdge`](/docs/api/storefront/unstable/objects/CheckoutLineItemEdge) | Object |
| [`CheckoutBuyerIdentity`](/docs/api/storefront/unstable/objects/CheckoutBuyerIdentity) | Object |
| [`DiscountAllocation`](/docs/api/storefront/unstable/objects/DiscountAllocation) | Object |
| [`DiscountApplicationEdge`](/docs/api/storefront/unstable/objects/DiscountApplicationEdge) | Object |
| [`DiscountCodeApplication`](/docs/api/storefront/unstable/objects/DiscountCodeApplication) | Object |
| [`Fulfillment`](/docs/api/storefront/unstable/objects/Fulfillment) | Object |
| [`FulfillmentLineItemEdge`](/docs/api/storefront/unstable/objects/FulfillmentLineItemEdge) | Object |
| [`ManualDiscountApplication`](/docs/api/storefront/unstable/objects/ManualDiscountApplication) | Object |
| [`Order`](/docs/api/storefront/unstable/objects/Order) | Object |
| [`OrderLineItem`](/docs/api/storefront/unstable/objects/OrderLineItem) | Object |
| [`OrderLineItemEdge`](/docs/api/storefront/unstable/objects/OrderLineItemEdge) | Object |
| [`checkoutAttributesUpdateV2Payload`](/docs/api/storefront/unstable/payloads/CheckoutAttributesUpdateV2Payload) | Payload |
| [`checkoutCompleteFreePayload`](/docs/api/storefront/unstable/payloads/checkoutCompleteFreePayload) | Payload |
| [`checkoutCompleteWithCreditCardV2Payload`](/docs/api/storefront/unstable/payloads/checkoutCompleteWithCreditCardV2Payload) | Payload |
| [`checkoutCompleteWithTokenizedPaymentV3Payload`](/docs/api/storefront/unstable/payloads/checkoutCompleteWithTokenizedPaymentV3Payload) | Payload |
| [`checkoutCustomerAssociateV2Payload`](/docs/api/storefront/unstable/payloads/checkoutCustomerAssociateV2Payload) | Payload |
| [`checkoutCustomerDisassociateV2Payload`](/docs/api/storefront/unstable/payloads/checkoutCustomerDisassociateV2Payload) | Payload |
| [`checkoutDiscountCodeRemovePayload`](/docs/api/storefront/unstable/payloads/checkoutDiscountCodeRemovePayload) | Payload |
| [`checkoutEmailUpdateV2Payload`](/docs/api/storefront/unstable/payloads/checkoutEmailUpdateV2Payload) | Payload |
| [`checkoutGiftCardRemoveV2Payload`](/docs/api/storefront/unstable/payloads/checkoutGiftCardRemoveV2Payload) | Payload |
| [`checkoutGiftCardsAppendPayload`](/docs/api/storefront/unstable/payloads/checkoutGiftCardsAppendPayload) | Payload |
| [`checkoutLineItemsAddPayload`](/docs/api/storefront/unstable/payloads/checkoutLineItemsAddPayload) | Payload |
| [`checkoutLineItemsRemovePayload`](/docs/api/storefront/unstable/payloads/checkoutLineItemsRemovePayload) | Payload |
| [`checkoutLineItemsReplacePayload`](/docs/api/storefront/unstable/payloads/checkoutLineItemsReplacePayload) | Payload |
| [`checkoutLineItemsUpdatePayload`](/docs/api/storefront/unstable/payloads/checkoutLineItemsUpdatePayload) | Payload |
| [`checkoutShippingAddressUpdateV2Payload`](/docs/api/storefront/unstable/payloads/checkoutShippingAddressUpdateV2Payload) | Payload |
| [`checkoutShippingLineUpdatePayload`](/docs/api/storefront/unstable/payloads/checkoutShippingLineUpdatePayload) | Payload |

For more information, refer to [Deprecation of Checkout APIs](/changelog/deprecation-of-checkout-apis).

### [Anchor to Delivery group types](/docs/api/release-notes/previous-versions/2024-04#delivery-group-types)Delivery group types

The [`groupType`](/docs/api/storefront/2024-04/objects/CartDeliveryGroup#field-cartdeliverygroup-grouptype) field has been added to the `CartDeliveryGroup` objects. The field accepts the following enum values:

* **`ONE_TIME_PURCHASE`**: The delivery group only contains merchandise that's either a one-time purchase or the first delivery of subscription merchandise.
* **`SUBSCRIPTION`**: The delivery group only contains subscription merchandise.

  Use the `groupType` field to determine whether a delivery group represents a single delivery or a recurring delivery.

### [Anchor to Metafields model 3D reference type](/docs/api/release-notes/previous-versions/2024-04#metafields-model-3d-reference-type)Metafields model 3D reference type

The `MODEL_3D` enum value on the [`mediaContentType`](/docs/api/storefront/2024-04/objects/Model3d#field-model3d-mediacontenttype) field has been added to the `Model3d` object.

---

Was this page helpful?

YesNo