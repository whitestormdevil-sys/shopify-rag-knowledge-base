---
source: https://shopify.dev/docs/apps/build/checkout
---

Merchants use [Shopify checkout](https://help.shopify.com/manual/checkout-settings) to accept orders and receive payments wherever they sell online. To augment Shopify checkout with new functionality, build an app with extensions.

---

## [Anchor to How it works](/docs/apps/build/checkout#how-it-works)How it works

After a customer adds products to a cart, they use Shopify checkout to enter their customer, shipping, and payment information before placing the order.

To extend checkout, apps can use extensions. For example, apps can use extensions to offer a customer free shipping or other discounts, depending on the contents of their cart.

To install apps on their store, merchants can use the Shopify admin. There, they can can use the [checkout editor](/docs/apps/build/checkout/test-checkout-ui-extensions#test-the-extension-in-the-checkout-editor) to place a block for a [checkout UI extension](/docs/api/checkout-ui-extensions) in the checkout experience.

![Actions that a developer, customer, and merchant take in connection to Shopify checkout](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/checkout/what-is-checkout-BFffD-s0.png)


---

## [Anchor to Customization options](/docs/apps/build/checkout#customization-options)Customization options

There are various types of Shopify Extensions that you can use to customize checkout:

* UI extensions
* Functions
* Web pixel extensions
* Payments extensions

All customization options are easy to install and upgrade-safe, enabling merchants to benefit from Shopify releases new products such as [Shop Pay](/docs/apps/build/checkout/test-checkout-ui-extensions#test-with-shop-pay), or features such as [One-page checkout](/docs/apps/build/checkout/test-checkout-ui-extensions#one-page-checkout).

For a detailed breakdown of the technologies that can be used to customize checkout, and the ways that you can extend checkout, refer to the [options for customizing Shopify checkout](/docs/apps/build/checkout/technologies).

Note

Checkout apps and extensions have [design requirements](/docs/apps/launch/app-requirements-checklist#design-requirements-for-checkout-apps) that apply to custom apps as well as public apps. Be sure that your app meets [all requirements](/docs/apps/launch/app-requirements-checklist) for its functionality and distribution type.

**Note:**

Checkout apps and extensions have [design requirements](/docs/apps/launch/app-requirements-checklist#design-requirements-for-checkout-apps) that apply to custom apps as well as public apps. Be sure that your app meets [all requirements](/docs/apps/launch/app-requirements-checklist) for its functionality and distribution type.

---

## [Anchor to Getting started](/docs/apps/build/checkout#getting-started)Getting started

To learn how to customize and extend checkout, read the following tutorials.

### [Anchor to Checkout UI extensions tutorials](/docs/apps/build/checkout#checkout-ui-extensions-tutorials)Checkout UI extensions tutorials

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

### [Anchor to Shopify Functions tutorials](/docs/apps/build/checkout#shopify-functions-tutorials)Shopify Functions tutorials

[![](/images/icons/48/heart.png)![](/images/icons/48/heart-dark.png)

Build a discount function

Use Shopify Functions to create a new discount type for users.

Build a discount function

Use Shopify Functions to create a new discount type for users.](/docs/apps/build/discounts/build-discount-function)

[Build a discount function  
  

Use Shopify Functions to create a new discount type for users.](/docs/apps/build/discounts/build-discount-function)

[![](/images/icons/48/coin.png)![](/images/icons/48/coin-dark.png)

Create a payments function

Use Shopify Functions to hide a payment option offered to customers at checkout.

Create a payments function

Use Shopify Functions to hide a payment option offered to customers at checkout.](/docs/apps/build/checkout/payments/create-payments-function)

[Create a payments function  
  

Use Shopify Functions to hide a payment option offered to customers at checkout.](/docs/apps/build/checkout/payments/create-payments-function)

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)

Build a delivery options function

Use Shopify Functions to rename a delivery option offered to customers at checkout.

Build a delivery options function

Use Shopify Functions to rename a delivery option offered to customers at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)

[Build a delivery options function  
  

Use Shopify Functions to rename a delivery option offered to customers at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-options/build-function)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

Create a server-side validation function

Use Shopify Functions to block progress on a checkout when the cart line quantities exceed a limit.

Create a server-side validation function

Use Shopify Functions to block progress on a checkout when the cart line quantities exceed a limit.](/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)

[Create a server-side validation function  
  

Use Shopify Functions to block progress on a checkout when the cart line quantities exceed a limit.](/docs/apps/build/checkout/cart-checkout-validation/create-server-side-validation-function)

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)

Build a location rule function

Use Shopify Functions to choose a different order location during checkout.

Build a location rule function

Use Shopify Functions to choose a different order location during checkout.](/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

[Build a location rule function  
  

Use Shopify Functions to choose a different order location during checkout.](/docs/apps/build/orders-fulfillment/order-routing-apps/location-rules/build-location-rule-function)

[![](/images/icons/48/hearts.png)![](/images/icons/48/hearts-dark.png)

Add a customized bundle function

Use Shopify Functions to group products together and sell them as a single unit.

Add a customized bundle function

Use Shopify Functions to group products together and sell them as a single unit.](/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

[Add a customized bundle function  
  

Use Shopify Functions to group products together and sell them as a single unit.](/docs/apps/build/product-merchandising/bundles/add-customized-bundle-function)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Build a fulfillment constraints function

Use Shopify Functions to customize fulfillment and delivery strategies.

Build a fulfillment constraints function

Use Shopify Functions to customize fulfillment and delivery strategies.](/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)

[Build a fulfillment constraints function  
  

Use Shopify Functions to customize fulfillment and delivery strategies.](/docs/apps/build/orders-fulfillment/order-routing-apps/build-fulfillment-constraints-function)

[![](/images/icons/48/build.png)![](/images/icons/48/build-dark.png)

Build a local pickup options function

Use Shopify Functions to generate local pickup delivery options at checkout.

Build a local pickup options function

Use Shopify Functions to generate local pickup delivery options at checkout.](/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)

[Build a local pickup options function  
  

Use Shopify Functions to generate local pickup delivery options at checkout.](/docs/apps/build/orders-fulfillment/order-routing-apps/build-local-pickup-options-function)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Create a local pickup charges function

Use Shopify Functions to create local pickup charges at checkout.

Create a local pickup charges function

Use Shopify Functions to create local pickup charges at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function)

[Create a local pickup charges function  
  

Use Shopify Functions to create local pickup charges at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-methods/create-local-pickup-charges-function)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Generate a pickup points function

Use Shopify Functions to generate pickup point delivery options at checkout.

Generate a pickup points function

Use Shopify Functions to generate pickup point delivery options at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)

[Generate a pickup points function  
  

Use Shopify Functions to generate pickup point delivery options at checkout.](/docs/apps/build/checkout/delivery-shipping/delivery-methods/generate-pickup-points)

---

## [Anchor to Upgrade](/docs/apps/build/checkout#upgrade)Upgrade

Deprecated

`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid`, additional scripts, and script tags are deprecated for the **Thank you** and **Order status** pages and will be sunset on August 28, 2025.

Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations) before the deadline.

[Shopify Scripts](/docs/api/liquid/objects#script) will continue to work alongside Shopify Extensions in checkout until June 30, 2026.

**Deprecated:**

`checkout.liquid` is now unsupported for the Information, Shipping, and Payment checkout steps. `checkout.liquid`, additional scripts, and script tags are deprecated for the **Thank you** and **Order status** pages and will be sunset on August 28, 2025.

Stores that currently use `checkout.liquid` for the **Thank you** and **Order status** pages need to [upgrade to Shopify Extensions in Checkout](https://www.shopify.com/checkout#advanced-customizations) before the deadline.

[Shopify Scripts](/docs/api/liquid/objects#script) will continue to work alongside Shopify Extensions in checkout until June 30, 2026.

A report identifying your current checkout customizations is available in the Shopify admin. The report provides high-level guidance to map customizations to Shopify Extensions in Checkout. Use this report to simplify your review of your existing customizations and to help you upgrade to Shopify Extensions in Checkout faster. [Learn more](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade).

To upgrade a `checkout.liquid` customization to Shopify Extensions in Checkout, take one or more of the following actions:

1. Use a public app that's built using extensions.

   We're adding new checkout apps to the Shopify App Store on a regular basis. If there currently isn't a suitable public app for your customization, then consider simplifying your checkout temporarily and adding new apps to your store as they become available.
2. Build a custom app using extensions, or [hire a service partner](https://www.shopify.com/plus/partners/service?type=service&services%5B%5D=141) to build one for you.

In some cases, after you've upgraded you can [revert to `checkout.liquid`](https://help.shopify.com/manual/checkout-settings/checkout-extensibility/checkout-upgrade#revert-to-checkout-liquid) until its sunset dates.

If you're upgrading a store to Shopify Extensions in Checkout, we recommend planning your in-checkout, **Thank you** page, and **Order status** page upgrades together, when possible, for the following benefits:

* Avoid maintaining multiple tech stacks, like UI extensions and `checkout.liquid`.
* Apply styling once to the entire experience.
* Manage one sunset date for `checkout.liquid` rather than one date for pre-purchase pages and another for **Thank you** and **Order status** pages.

  If this isn't possible, then we recommend prioritizing the upgrade for in-checkout pages first and upgrading after-purchase pages after that.

---

## [Anchor to Best practices](/docs/apps/build/checkout#best-practices)Best practices

To optimize your app development experience, Shopify has established a set of best practices that you can refer to when developing an app that extends checkout.

Tip

We also recommend getting familiar with Polaris [accessibility](https://polaris.shopify.com/foundations/accessibility) and [content](https://polaris.shopify.com/content/merchant-to-customer) guidelines.

**Tip:**

We also recommend getting familiar with Polaris [accessibility](https://polaris.shopify.com/foundations/accessibility) and [content](https://polaris.shopify.com/content/merchant-to-customer) guidelines.

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Create multi-page extensions

Learn more about building extensions that can render on any checkout page.

Create multi-page extensions

Learn more about building extensions that can render on any checkout page.](/docs/apps/build/checkout/create-multi-page-extensions)

[Create multi-page extensions  
  

Learn more about building extensions that can render on any checkout page.](/docs/apps/build/checkout/create-multi-page-extensions)

[![](/images/icons/48/heart.png)![](/images/icons/48/heart-dark.png)

UX for checkout

Learn how to improve the quality of checkout experiences by following our UX guidelines for checkout.

UX for checkout

Learn how to improve the quality of checkout experiences by following our UX guidelines for checkout.](/docs/apps/build/checkout/ux-for-checkout)

[UX for checkout  
  

Learn how to improve the quality of checkout experiences by following our UX guidelines for checkout.](/docs/apps/build/checkout/ux-for-checkout)

[![](/images/icons/48/key.png)![](/images/icons/48/key-dark.png)

Network requests from extensions

Learn about Cross-Origin Resource Sharing (CORS) and other security considerations when making network requests to your own server.

Network requests from extensions

Learn about Cross-Origin Resource Sharing (CORS) and other security considerations when making network requests to your own server.](/docs/api/checkout-ui-extensions/latest/configuration#network-access)

[Network requests from extensions  
  

Learn about Cross-Origin Resource Sharing (CORS) and other security considerations when making network requests to your own server.](/docs/api/checkout-ui-extensions/latest/configuration#network-access)

[![](/images/icons/48/bfsgem.png)![](/images/icons/48/bfsgem-dark.png)

App Design Guidelines

Get practical guidance on how to design a user interface for the Shopify admin.

App Design Guidelines

Get practical guidance on how to design a user interface for the Shopify admin.](/docs/apps/design-guidelines/)

[App Design Guidelines  
  

Get practical guidance on how to design a user interface for the Shopify admin.](/docs/apps/design-guidelines/)

---

## [Anchor to Product roadmap](/docs/apps/build/checkout#product-roadmap)Product roadmap

Some checkout customization features are in development and will be released later this year. The following are the features on our roadmap and our estimated launch dates:

Note

This roadmap is being shared for informational purposes and is subject to change. Bug fixes and improvements will be added as we hear from the community. Share your feedback or request new features by creating a new issue in the [Shopify developer community forum](https://community.shopify.dev/).

**Note:**

This roadmap is being shared for informational purposes and is subject to change. Bug fixes and improvements will be added as we hear from the community. Share your feedback or request new features by creating a new issue in the [Shopify developer community forum](https://community.shopify.dev/).

### [Anchor to Shopify Functions](/docs/apps/build/checkout#shopify-functions)Shopify Functions

We'll continue to add new Shopify Functions APIs to further customize checkout business logic.

| Milestone | Target |
| --- | --- |
| Introduced a new [Discount API](/docs/api/functions/reference/discount) that supports any combination of product, order, and shipping savings from a single function extension | April 2025 (shipped) |
| Support for cart metafields on function input queries | July 2025 (shipped) |
| Optionally reject discount codes and return custom messages when discounts shouldn't be applied [(Discount API)](/docs/api/functions/latest/discount) | Q4 2025 (shipped) |
| Support complex conditions for "Buy X Get Y" discounts [(Discount API)](/docs/api/functions/latest/discount) | Q1 2026 |
| Changes to the [Discount API](/docs/api/functions/reference/discount) to stack multiple discounts on the same product line item | Q1 2026 |

---

Was this page helpful?

YesNo