---
source: https://shopify.dev/docs/api/checkout-extensions
---

Checkout app extensions make it easy for developers to extend their app code into checkout and customize many aspects of the checkout experience. Shopify provides the tools and resources for building checkout UI extensions on the [checkout steps](/docs/apps/build/checkout/technologies), [post-purchase page](/docs/apps/build/checkout/product-offers#post-purchase-product-offers), and [**Thank you** and **Order status** pages](/docs/apps/build/checkout/thank-you-order-status).

---

## [Anchor to Checkout UI extensions](/docs/api/checkout-extensions#checkout-ui-extensions)Checkout UI extensions

Checkout UI extensions let you add custom workflows and functionality at defined points of the checkout process, and are built into apps using [target APIs and UI components](/docs/api/checkout-ui-extensions).

Plus

[Checkout UI extensions](/docs/api/checkout-ui-extensions) that render on the information and shipping and payment steps in checkout are available only to stores on a [Shopify Plus](https://www.shopify.com/plus) plan.

**Plus:**

[Checkout UI extensions](/docs/api/checkout-ui-extensions) that render on the information and shipping and payment steps in checkout are available only to stores on a [Shopify Plus](https://www.shopify.com/plus) plan.

---

## [Anchor to Post-purchase extensions](/docs/api/checkout-extensions#post-purchase-extensions)Post-purchase extensions

Post-purchase extensions let you add new UI and functionality to the post-purchase page, and are built into apps using [extension points APIs](/docs/api/checkout-extensions/post-purchase/api) and [UI components](/docs/api/checkout-extensions/post-purchase/components) provided by Shopify.

Tip

Learn how JWTs (JSON web tokens) [need to be structured](/docs/api/checkout-extensions/post-purchase/jwt-specification) for use in post-purchase extensions.

**Tip:**

Learn how JWTs (JSON web tokens) [need to be structured](/docs/api/checkout-extensions/post-purchase/jwt-specification) for use in post-purchase extensions.

---

## [Anchor to Thank you and Order status page extensions](/docs/api/checkout-extensions#thank-you-and-order-status-page-extensions)Thank you and Order status page extensions

Checkout UI extensions can be developed for the **Thank you** page and the **Order status** page with similar [target APIs and UI components](/docs/api/checkout-ui-extensions). Extensions that appear after a purchase has been completed will be available to all plans except Shopify Starter.

---

## [Anchor to Getting started](/docs/api/checkout-extensions#getting-started)Getting started

Learn how to use checkout app extensions by following one of our use case tutorials:

[![](/images/icons/48/filesystem.png)![](/images/icons/48/filesystem-dark.png)

Pre-purchase product offers

Build a pre-purchase upsell offer that prompts the customer to add a product to their order.

Pre-purchase product offers

Build a pre-purchase upsell offer that prompts the customer to add a product to their order.](/docs/apps/build/checkout/product-offers/build-a-pre-purchase-offer)

[Pre-purchase product offers  
  

Build a pre-purchase upsell offer that prompts the customer to add a product to their order.](/docs/apps/build/checkout/product-offers/build-a-pre-purchase-offer)

[![](/images/icons/48/star.png)![](/images/icons/48/star-dark.png)

Post-purchase checkout extensions

Create a basic example of a post-purchase checkout extension.

Post-purchase checkout extensions

Create a basic example of a post-purchase checkout extension.](/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer)

[Post-purchase checkout extensions  
  

Create a basic example of a post-purchase checkout extension.](/docs/apps/build/checkout/product-offers/build-a-post-purchase-offer)

[![](/images/icons/48/marketplaces.png)![](/images/icons/48/marketplaces-dark.png)

Thank you and order status extensions

Build a survey that asks customers how they heard about the store after they made a purchase.

Thank you and order status extensions

Build a survey that asks customers how they heard about the store after they made a purchase.](/docs/apps/build/checkout/thank-you-order-status/add-survey)

[Thank you and order status extensions  
  

Build a survey that asks customers how they heard about the store after they made a purchase.](/docs/apps/build/checkout/thank-you-order-status/add-survey)

[![](/images/icons/48/flag.png)![](/images/icons/48/flag-dark.png)

Custom banners

Learn how to add a custom banner to checkout.

Custom banners

Learn how to add a custom banner to checkout.](/docs/apps/build/checkout/fields-banners/add-banner)

[Custom banners  
  

Learn how to add a custom banner to checkout.](/docs/apps/build/checkout/fields-banners/add-banner)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Custom fields

Learn how to add custom fields to checkout that customers can use to add delivery instructions to their order.

Custom fields

Learn how to add custom fields to checkout that customers can use to add delivery instructions to their order.](/docs/apps/build/checkout/fields-banners/add-field)

[Custom fields  
  

Learn how to add custom fields to checkout that customers can use to add delivery instructions to their order.](/docs/apps/build/checkout/fields-banners/add-field)

[![](/images/icons/48/key.png)![](/images/icons/48/key-dark.png)

Client-side validation

Use a checkout UI extension to validate fields at checkout and block customer progress.

Client-side validation

Use a checkout UI extension to validate fields at checkout and block customer progress.](/docs/apps/build/checkout/cart-checkout-validation/create-client-side-validation)

[Client-side validation  
  

Use a checkout UI extension to validate fields at checkout and block customer progress.](/docs/apps/build/checkout/cart-checkout-validation/create-client-side-validation)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Header

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout header with custom images, including the back to cart link.

Header

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout header with custom images, including the back to cart link.](/docs/apps/build/checkout/customize-header)

[Header  
  

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout header with custom images, including the back to cart link.](/docs/apps/build/checkout/customize-header)

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)

Footer

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout footer with store policies.

Footer

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout footer with store policies.](/docs/apps/build/checkout/customize-footer)

[Footer  
  

Use a checkout UI extension and the GraphQL Admin API's checkout branding types to customize the checkout footer with store policies.](/docs/apps/build/checkout/customize-footer)

[![](/images/icons/48/marketplaces.png)![](/images/icons/48/marketplaces-dark.png)

Address autocomplete

Build an extension to customize the address autocomplete provider for the delivery and billing address forms in checkout.

Address autocomplete

Build an extension to customize the address autocomplete provider for the delivery and billing address forms in checkout.](/docs/apps/build/checkout/delivery-shipping/address-autocomplete/build-autocomplete)

[Address autocomplete  
  

Build an extension to customize the address autocomplete provider for the delivery and billing address forms in checkout.](/docs/apps/build/checkout/delivery-shipping/address-autocomplete/build-autocomplete)

---

## [Anchor to Next steps](/docs/api/checkout-extensions#next-steps)Next steps

* Learn about the [resources available](/docs/api/checkout-ui-extensions) for building checkout UI extensions.
* Learn about the [extension points](/docs/api/checkout-extensions/post-purchase/api) available to post-purchase checkout extensions.

---

Was this page helpful?

YesNo