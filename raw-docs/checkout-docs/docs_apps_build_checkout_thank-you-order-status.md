---
source: https://shopify.dev/docs/apps/build/checkout/thank-you-order-status
---

The **Thank you** and **Order status** pages are shown to customers at the end of checkout and can be customized using checkout UI extensions. This guide introduces how extensions on the pages work, and provides some resources for getting started.

---

## [Anchor to How it works](/docs/apps/build/checkout/thank-you-order-status#how-it-works)How it works

You can use a [UI extension](/docs/api/checkout-ui-extensions) to add custom content to the **Thank you** and **Order status** pages. The **Thank you** page is displayed to a customer as an initial purchase confirmation after they complete a checkout. If a customer attempts to return to the **Thank you** page or check their order status later on, then they're shown the **Order status** page instead.

The customer can refresh or revisit the page throughout the order creation and fulfillment process to review the details of their order, and any updates. For example, customers often visit the **Order status** page after clicking on a link in the order confirmation email.

![The customer pathways to reach the Thank you and Order status pages.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/checkout/thank-you-order-status/how-it-works-CjGrr6mB.png)

You can use a UI extension on the **Thank you** and **Order status** pages to add custom content such as:

| Example | Description | Page(s) |
| --- | --- | --- |
| Survey requests | Ask a customer to complete a survey after they've completed checkout. | **Thank you** |
| Product reviews | Ask a customer to complete a feedback form when they revisit their purchase. | **Order status** |
| Upsell offers | Prompt a customer to add more products to their initial order after they've completed payment through order editing. | **Order status** |
| Social sharing | Display additional social media content at the end of checkout. | **Thank you** and **Order status** |
| Download links | Offer download links for digital goods. | **Thank you** and **Order status** |

Note that for extensions on the **Thank you** page (target `purchase.thank-you`), the order is not yet created when these extensions are displayed. However, the order id **is** available. You can use [`OrderConfirmationApi`](/docs/api/checkout-ui-extensions/latest/apis/order#orderconfirmationapi) to obtain the order [confirmation number](https://help.shopify.com/en/manual/orders/status-tracking/confirmation-numbers), or the order id. Use the order id to uniquely identify the order, and to fetch additional information about the order using the GraphQL API after order creation is complete.

For extensions on the **Order status** page (target `customer-account.order-status`), the order is always available. Use the [`OrderStatusApi`](/docs/api/checkout-ui-extensions/latest/apis/order#orderstatusapi) to obtain details about the order, such as its id, name, and confirmation number.

---

## [Anchor to Limitations](/docs/apps/build/checkout/thank-you-order-status#limitations)Limitations

* There's no support for APIs that directly mutate an order using a UI extension. You can use `fetch` to make network calls to web services for your extension needs. For extensions that need to make changes to the order being created, consider making a [post-purchase extension](/docs/apps/build/checkout/product-offers#post-purchase-product-offers).

---

## [Anchor to Getting started](/docs/apps/build/checkout/thank-you-order-status#getting-started)Getting started

Follow the getting started tutorial to learn how to build extensions for the **Thank you** and **Order status** pages.

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)

Add custom content to Thank you and Order status pages

Learn how to add a survey to the **Thank you** and **Order status** pages.

Add custom content to Thank you and Order status pages

Learn how to add a survey to the **Thank you** and **Order status** pages.](/docs/apps/build/checkout/thank-you-order-status/add-survey)

[Add custom content to Thank you and Order status pages  
  

Learn how to add a survey to the **Thank you** and **Order status** pages.](/docs/apps/build/checkout/thank-you-order-status/add-survey)

---

## [Anchor to Developer tools and resources](/docs/apps/build/checkout/thank-you-order-status#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to get familiar with building **Thank you** and **Order status** page extensions.

[![](/images/icons/48/build.png)![](/images/icons/48/build-dark.png)

Checkout UI extensions API reference

Consult the API reference for checkout UI targets and their respective types.

Checkout UI extensions API reference

Consult the API reference for checkout UI targets and their respective types.](/docs/api/checkout-ui-extensions/latest/extension-targets-overview)

[Checkout UI extensions API reference  
  

Consult the API reference for checkout UI targets and their respective types.](/docs/api/checkout-ui-extensions/latest/extension-targets-overview)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Components for checkout UI extensions

Learn about the components that are available in checkout UI extensions.

Components for checkout UI extensions

Learn about the components that are available in checkout UI extensions.](/docs/api/checkout-ui-extensions/latest/components)

[Components for checkout UI extensions  
  

Learn about the components that are available in checkout UI extensions.](/docs/api/checkout-ui-extensions/latest/components)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Checkout extension configuration

Learn about the properties that you can configure in your checkout UI extension.

Checkout extension configuration

Learn about the properties that you can configure in your checkout UI extension.](/docs/api/checkout-ui-extensions/latest/configuration)

[Checkout extension configuration  
  

Learn about the properties that you can configure in your checkout UI extension.](/docs/api/checkout-ui-extensions/latest/configuration)

[![](/images/icons/48/heart.png)![](/images/icons/48/heart-dark.png)

UX guidelines for Thank you and Order status pages

Improve the quality of your **Thank you** and **Order status** pages by following our UX guidelines.

UX guidelines for Thank you and Order status pages

Improve the quality of your **Thank you** and **Order status** pages by following our UX guidelines.](/docs/apps/build/checkout/thank-you-order-status/ux-for-thank-you-order-status)

[UX guidelines for Thank you and Order status pages  
  

Improve the quality of your **Thank you** and **Order status** pages by following our UX guidelines.](/docs/apps/build/checkout/thank-you-order-status/ux-for-thank-you-order-status)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

UX guidelines for Announcement Bar extensions

Explore UX guidelines that you can refer to when building UI extensions for the Announcement Bar on the **Thank you** and **Customer Account** pages.

UX guidelines for Announcement Bar extensions

Explore UX guidelines that you can refer to when building UI extensions for the Announcement Bar on the **Thank you** and **Customer Account** pages.](/docs/apps/build/checkout/thank-you-order-status/ux-for-announcement-bar)

[UX guidelines for Announcement Bar extensions  
  

Explore UX guidelines that you can refer to when building UI extensions for the Announcement Bar on the **Thank you** and **Customer Account** pages.](/docs/apps/build/checkout/thank-you-order-status/ux-for-announcement-bar)

---

Was this page helpful?

YesNo