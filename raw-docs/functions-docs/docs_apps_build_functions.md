---
source: https://shopify.dev/docs/apps/build/functions
---

Functions availability

* Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions. Only stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use [custom apps](https://help.shopify.com/manual/apps/app-types/custom-apps) that contain [Shopify Function APIs](/docs/api/functions).
* Some Shopify Functions capabilities are available only to stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan). See [Shopify Function APIs](/docs/api/functions#availability-of-shopify-functions) for details.

**Functions availability:**

* Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions. Only stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan) can use [custom apps](https://help.shopify.com/manual/apps/app-types/custom-apps) that contain [Shopify Function APIs](/docs/api/functions).
* Some Shopify Functions capabilities are available only to stores on a [Shopify Plus plan](https://help.shopify.com/manual/intro-to-shopify/pricing-plans/plans-features/shopify-plus-plan). See [Shopify Function APIs](/docs/api/functions#availability-of-shopify-functions) for details.

Shopify Functions allow developers to customize the backend logic of Shopify. This guide introduces how Shopify Functions work and the benefits of using Shopify Functions.



---

## [Anchor to How Shopify Functions work](/docs/apps/build/functions#how-shopify-functions-work)How Shopify Functions work

Function [extension targets](/docs/apps/build/app-extensions/configure-app-extensions#targets) inject code into the backend logic of Shopify. The following diagram shows how Shopify invokes a function which has been configured for an extension target:

![A diagram showing how Shopify invokes a function which has been configured for an extension target.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/functions/extension-targets-C0IXZY73.png)

* **Function input:** The [function input](/docs/api/functions/latest#input) is a JSON object which is the result of a GraphQL input query you define. Input queries allow you to select the specific data you need for your function, such as cart line product data or metafields.
* **Function logic:** The [function logic](/docs/api/functions/latest#function) is written in any language that can compile a WebAssembly module which meets [function requirements](/docs/apps/build/functions/programming-languages/webassembly-for-functions). Function templates and client libraries are available for [Rust](/docs/apps/build/functions/programming-languages/rust-for-functions) and [JavaScript](/docs/apps/build/functions/programming-languages/javascript-for-functions).

  Caution

  Shopify strongly recommends [Rust](/docs/apps/build/functions/programming-languages/rust-for-functions) as the most performant language choice to avoid your function failing with large carts.

  **Caution:**

  Shopify strongly recommends [Rust](/docs/apps/build/functions/programming-languages/rust-for-functions) as the most performant language choice to avoid your function failing with large carts.
* **Function output:** The [function output](/docs/api/functions/latest#output) is a JSON document that describes the operations you'd like Shopify to carry out.

  GraphQL schemas provided by Shopify specify the targets, available inputs, and expected outputs for a [Functions API](/docs/api/functions).

---

## [Anchor to Lifecycle of a Shopify Function](/docs/apps/build/functions#lifecycle-of-a-shopify-function)Lifecycle of a Shopify Function

The following diagram shows an example lifecycle of a Shopify Function:

* **App developers** create and deploy apps that contain functions.
* **Merchants** install the app on their Shopify store and configure the function. An API call is made with the function configuration.
* **Customers** interact with a Shopify store and **Shopify** executes the function.

  For example, an app developer might create and deploy an app with a function that defines a new discount type. The merchant can then install the app on their Shopify store and create a new discount from a discount type provided by the app. Shopify executes the function to calculate the discount when a customer adds a product to their cart.

  Shopify Functions are never invoked directly by URL or otherwise. Shopify invokes them as-needed within the customer journey.

![A diagram showing the creating and deploying phases in Shopify Functions](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/functions/create-test-deploy-B8EIsTvz.png)


---

## [Anchor to Getting started](/docs/apps/build/functions#getting-started)Getting started

Learn how to use Shopify Functions by following one of our use case tutorials:

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

## [Anchor to Developer tools and resources](/docs/apps/build/functions#developer-tools-and-resources)Developer tools and resources

Explore the developer tools and resources available for Shopify Functions.

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Shopify Function APIs reference

Learn about the available APIs for Shopify Functions.

Shopify Function APIs reference

Learn about the available APIs for Shopify Functions.](/docs/api/functions)

[Shopify Function APIs reference  
  

Learn about the available APIs for Shopify Functions.](/docs/api/functions)

[![](/images/icons/48/rust.png)![](/images/icons/48/rust-dark.png)

Language support

Learn about the language support and tooling that are available in Shopify Functions.

Language support

Learn about the language support and tooling that are available in Shopify Functions.](/docs/apps/build/functions/programming-languages)

[Language support  
  

Learn about the language support and tooling that are available in Shopify Functions.](/docs/apps/build/functions/programming-languages)

---

## [Anchor to Deleting functions](/docs/apps/build/functions#deleting-functions)Deleting functions

To delete a Shopify Function, you need to remove the relevant files from your app's `/extensions` directory, and then redeploy your app. [Learn more about removing a Shopify Function](/docs/apps/build/app-extensions/remove-app-extension#remove-a-cli-managed-app-extension).

When you delete a function, the following behavior occurs:

* The function, including all associated [function owners](/docs/apps/build/functions/input-queries/metafields-for-input-queries#how-it-works), is permanently deleted.
* The function no longer runs, and becomes inaccessible to any Shopify stores that have your app installed.

---

## [Anchor to Next steps](/docs/apps/build/functions#next-steps)Next steps

* Learn about how data is [input to and output from Shopify Functions](/docs/api/functions/latest#function-anatomy).
* Explore [the references for each Function API](/docs/api/functions).

---

Was this page helpful?

YesNo