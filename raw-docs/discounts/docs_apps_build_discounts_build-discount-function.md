---
source: https://shopify.dev/docs/apps/build/discounts/build-discount-function
---

With [Shopify Functions](/docs/apps/build/functions), you can create a new type of discount that applies to cart lines, order subtotal, and shipping rates.

In this tutorial, you'll use Shopify Functions to create a new type of discount that does three things:

* Reduces the price of a cart line by 20%
* Discounts the order subtotal by 10%
* Provides free shipping

After creating the discount, you can test it out in your store.

Migrate your existing discount functions

To learn how to migrate your existing Discount Functions to use the [Discount API](/docs/api/functions/reference/discount), refer to [Migrate to the Discount API](/docs/apps/build/discounts/migrate-discount-api).

**Migrate your existing discount functions:**

To learn how to migrate your existing Discount Functions to use the [Discount API](/docs/api/functions/reference/discount), refer to [Migrate to the Discount API](/docs/apps/build/discounts/migrate-discount-api).

## [Anchor to What you'll learn](/docs/apps/build/discounts/build-discount-function?extension=rust#what-youll-learn)What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Use the Shopify CLI to add a Discount Function to an app
* Review the configuration of your discount function
* Review the input queries associated with your discount function
* Review the function logic associated with your discount function
* Use GraphiQL to create a discount and configure it to work with your function
* Test your discount function and view its logs

![A checkout summary that lists discounts for all three classes](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/discounts/multi-class-DqNqJQCF.png)

## Requirements

[Create a Partner account](https://www.shopify.com/partners)

[Create a dev store](/docs/apps/tools/development-stores#create-a-development-store-to-test-your-app)

[Create an app](/docs/apps/getting-started/create)

Create an that has the `write_discounts` and `read_products` [access
scopes](/docs/api/usage/access-scopes), using the [latest version of Shopify CLI](/docs/api/shopify-cli#upgrade).

[Install Node.js](https://nodejs.org/en/download)

Install Node.js 22 or higher.

[You've installed rust](https://www.rust-lang.org/tools/install)

On Windows, Rust requires the [Microsoft C++ Build Tools](https://docs.microsoft.com/en-us/windows/dev-environment/rust/setup). Make sure to select the **Desktop development with C++** workload when installing the tools.

[You've installed the `wasm32-unknown-unknown` target](https://doc.rust-lang.org/rustc/platform-support/wasm32-unknown-unknown.html)

To ensure compatibility with the latest version of Rust, install the `wasm32-unknown-unknown` target.

## Project

Extension:

Rust JavaScript 

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Rust-BI4G1lv1.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Rust-dark-CiWTztgq.svg)

Rust

[View on GitHub](https://github.com/Shopify/discounts-reference-app/blob/main/examples/rust/default)

## [Anchor to Create the Discount Function](/docs/apps/build/discounts/build-discount-function?extension=rust#create-the-discount-function)Create the Discount Function

To create a Discount Function, you'll use the Shopify CLI, which generates starter code for your Function.

1. Navigate to your app's directory:

   9

   1

   cd directory
2. Run the following command to create a new Discount Function:

   9

   1

   shopify app generate extension --template discount --name discount-function-rs
3. Choose the language that you want to use. For this tutorial, select `Rust`.

Info

Steps 2-4 review the generated code. To proceed directly to deploying and testing your Discount Function, jump to [Step 5](#update-your-apps-access-scopes).

**Info:**

Steps 2-4 review the generated code. To proceed directly to deploying and testing your Discount Function, jump to [Step 5](#update-your-apps-access-scopes).

## [Anchor to Review the Discount Function Configuration](/docs/apps/build/discounts/build-discount-function?extension=rust#review-the-discount-function-configuration)Review the Discount Function Configuration

The `shopify.extension.toml` file defines the Discount Function's metadata, targets, and build configuration.

### [Anchor to Metadata](/docs/apps/build/discounts/build-discount-function?extension=rust#metadata)Metadata

The `[[extensions]]` section defines the Function metadata. This includes the Function's handle, name, description, and type. The `name` and `description` are displayed on the **Discount** page of your Shopify admin.

Info

Shopify provides localization tools, and you can use them to localize the name and description of Discount Functions. To learn more, refer to [localizing your Shopify app](/docs/apps/build/localize-your-app).

**Info:**

Shopify provides localization tools, and you can use them to localize the name and description of Discount Functions. To learn more, refer to [localizing your Shopify app](/docs/apps/build/localize-your-app).

### [Anchor to Targets](/docs/apps/build/discounts/build-discount-function?extension=rust#targets)Targets

The `[[extensions.targeting]]` sections define the Function targets. Each section includes a `target`, `input_query`, and `export` property.

The [`target`](/docs/apps/build/app-extensions/configure-app-extensions#targets) property defines where the Function is applied. The Discount API has two [`run` targets](/docs/api/functions/reference/discount/graphql):

* `cart.lines.discounts.generate.run` - The Function can apply discounts to cart lines and order subtotals.
* `cart.delivery-options.discounts.generate.run` - The Function can apply discounts to shipping rates.

The `input_query` property is the path to the Function's input query file. This file defines the Function's [input parameters](/docs/api/functions/reference/discount/graphql/input).

The `export` property specifies the build entrypoint that will run for a specified target. This will usually be the function name of your main export.

### [Anchor to Build configuration](/docs/apps/build/discounts/build-discount-function?extension=rust#build-configuration)Build configuration

The `[extensions.build]` section defines the build configuration for your Function. This includes the build `command`, the build `path` and a `watch` property which allows you to watch for changes to the Function. Refer to Shopify Functions [configuration properties](/docs/api/functions/latest#configuration) for more information.

  

Note

Depending on your app type, you may have to define the `[extensions.ui]` or `[extensions.ui.paths]` section.

Refer to [Build a discounts UI with Admin UI Extensions](/docs/apps/build/discounts/build-ui-extension) or [Build a discounts UI with React Router](/docs/apps/build/discounts/build-ui-with-react-router) to learn more about building UIs to configure Functions.

**Note:**

Depending on your app type, you may have to define the `[extensions.ui]` or `[extensions.ui.paths]` section.

Refer to [Build a discounts UI with Admin UI Extensions](/docs/apps/build/discounts/build-ui-extension) or [Build a discounts UI with React Router](/docs/apps/build/discounts/build-ui-with-react-router) to learn more about building UIs to configure Functions.

## [Anchor to Review the input queries for your Function](/docs/apps/build/discounts/build-discount-function?extension=rust#review-the-input-queries-for-your-function)Review the input queries for your Function

[Input queries](/docs/apps/build/functions/input-output) are used to define the input that the Discount Function needs. The result of those queries will be given as input parameters to the export functions.

### [Anchor to [object Object], input](/docs/apps/build/discounts/build-discount-function?extension=rust#cart_lines_discounts_generate_rungraphql-input)`cart_lines_discounts_generate_run.graphql` input

The result of this query is provided as input to the `cart.lines.discounts.generate.run` target. Refer to [Discount API](/docs/api/functions/reference/discount) for more information about the input data available to your Function.

### [Anchor to [object Object], input](/docs/apps/build/discounts/build-discount-function?extension=rust#cart_delivery_options_discounts_generate_rungraphql-input)`cart_delivery_options_discounts_generate_run.graphql` input

The result of this query is provided as input to the `cart.delivery-options.discounts.generate.run` Function. Refer to [Discount API](/docs/api/functions/reference/discount) for more information about the input data available to your Function.

## [Anchor to Review the logic of your Function](/docs/apps/build/discounts/build-discount-function?extension=rust#review-the-logic-of-your-function)Review the logic of your Function

To specify how a Discount Function should apply discounts, update its logic. This logic can make use of the input parameters provided to the Function, and should output discount operations.

Note

Your Function should only return operations for `discountClasses` that the discount applies to. For example, if the discount is configured to apply to `PRODUCT` and `ORDER`, but not `SHIPPING`, your Function should only return operations for `PRODUCT` and `ORDER`.

**Note:**

Your Function should only return operations for `discountClasses` that the discount applies to. For example, if the discount is configured to apply to `PRODUCT` and `ORDER`, but not `SHIPPING`, your Function should only return operations for `PRODUCT` and `ORDER`.

### [Anchor to Review your cart run Function logic](/docs/apps/build/discounts/build-discount-function?extension=rust#review-your-cart-run-function-logic)Review your cart run Function logic

This is the entry point for cart line and order subtotal discount calculation logic. The name must match the `export` property in the `[[extensions.targeting]]` section of your Function's configuration and must output [`CartOperations`](/docs/api/functions/reference/discount/graphql/common-objects/cartoperation).

In this example, the Function checks whether the discount applies to `PRODUCT` and `ORDER` and applies two discounts: 10% off the entire order subtotal, plus an additional 20% off the highest cart line subtotal.

### [Anchor to Review your delivery run Function logic](/docs/apps/build/discounts/build-discount-function?extension=rust#review-your-delivery-run-function-logic)Review your delivery run Function logic

This is the entry point for shipping rate discount calculation logic. The name must match the `export` property in the `[[extensions.targeting]]` section of your Function's configuration and must output [`DeliveryOperations`](/docs/api/functions/reference/discount/graphql/common-objects/deliveryoperation).

In this example, the Function checks whether the discount applies to `SHIPPING` and reduces the first delivery group by 100%, offering free shipping.

## [Anchor to Update your app's access scopes](/docs/apps/build/discounts/build-discount-function?extension=rust#update-your-apps-access-scopes)Update your app's access scopes

You must request the `write_discounts` [access scope](/docs/api/usage/access-scopes) to give your app the permissions that it needs to create and update discounts.

In `shopify.app.toml`, located in the root of your app, add the `write_discounts` scope to the `access_scopes` array.

### [Anchor to Start your app to preview changes](/docs/apps/build/discounts/build-discount-function?extension=rust#start-your-app-to-preview-changes)Start your app to preview changes

1. Save your updated configuration TOML file.
2. Start `app dev` if it's not already running:

   9

   1

   shopify app dev

   The configuration TOML file changes will be applied automatically on the development store.

Note

The `app dev` command automatically watches files that match the [build.watch](/docs/api/functions/configuration#properties) glob pattern. When it detects a change, it builds your Function and updates the Function extension's draft so that you can preview changes immediately.

**Note:**

The `app dev` command automatically watches files that match the [build.watch](/docs/api/functions/configuration#properties) glob pattern. When it detects a change, it builds your Function and updates the Function extension's draft so that you can preview changes immediately.

## [Anchor to Create a discount in your store](/docs/apps/build/discounts/build-discount-function?extension=rust#create-a-discount-in-your-store)Create a discount in your store

In this step, you'll use GraphiQL, an in-browser tool for testing GraphQL, to create a discount that applies a line-item price adjustment, an order-wide percentage discount, and free shipping. Then you'll link this discount to the Function that you created.
GraphiQL is an in-browser tool for writing, validating, and testing GraphQL queries.

Info

You can also build a discount interface using [Admin UI Extensions](/docs/apps/build/discounts/build-ui-extension) and configure your Functions using [Metafields](/docs/api/functions/reference/discount/graphql/common-objects/metafield).

**Info:**

You can also build a discount interface using [Admin UI Extensions](/docs/apps/build/discounts/build-ui-extension) and configure your Functions using [Metafields](/docs/api/functions/reference/discount/graphql/common-objects/metafield).

### [Anchor to Open the GraphiQL interface for the Shopify Admin API](/docs/apps/build/discounts/build-discount-function?extension=rust#open-the-graphiql-interface-for-the-shopify-admin-api)Open the GraphiQL interface for the Shopify Admin API

1. Open the GraphiQL interface by pressing `g` in the terminal window where you started your app.
2. On the GraphiQL interface, for **API Version**, select the latest stable release.

### [Anchor to Get the handle of your Function](/docs/apps/build/discounts/build-discount-function?extension=rust#get-the-handle-of-your-function)Get the handle of your Function

1. Use your function handle in GraphQL mutations instead of querying for the function ID.

   Your function handle is defined in `shopify.extension.toml` as `handle`:

   9

   1

   2

   3

   4

   5

   [[extensions]]

   name = "discount-function"

   handle = "discount-function-rs"

   type = "function"

   uid = "3d664979-ccd6-e9dd-4497-41289ece62373715032a"

   Note

   If you're upgrading to API version 2025-10 or later, you no longer need to query for function IDs. Use your stable function handle instead, which remains consistent across environments.

   **Note:**

   If you're upgrading to API version 2025-10 or later, you no longer need to query for function IDs. Use your stable function handle instead, which remains consistent across environments.

### [Anchor to Create the discount](/docs/apps/build/discounts/build-discount-function?extension=rust#create-the-discount)Create the discount

To create a discount in your store, use the [`discountAutomaticAppCreate`](/docs/api/admin-graphql/latest/mutations/discountAutomaticAppCreate) mutation.

1. For `functionHandle`, provide the Function handle from the [previous step](#get-the-handle-of-your-function).
2. Add the [`discountClasses`](/docs/api/functions/reference/discount/graphql/common-objects/discountclass) field to your mutation based on the business requirements.

  

You should receive a GraphQL response that includes the ID of the created discount.
If the response includes any `userErrors`, then review them, check that your mutation and `functionHandle` are correct, and try the request again.

Troubleshooting

If you receive a `Could not find Function` error, then confirm the following:

* `shopify app dev` is running.
* The function handle is correct.
* Your app has the `write_discounts` access scope.

## [Anchor to Test the Discount Function](/docs/apps/build/discounts/build-discount-function?extension=rust#test-the-discount-function)Test the Discount Function

### [Anchor to View your discount](/docs/apps/build/discounts/build-discount-function?extension=rust#view-your-discount)View your discount

In your Shopify admin, go to **Discounts**. You should now see the **Cart line, Order, and Shipping discount** that you created.

![A list of all active discounts for the store.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/discounts/functions-discount-list-multi-class-bMqqn_8b.png)

### [Anchor to Deactivate other discounts](/docs/apps/build/discounts/build-discount-function?extension=rust#deactivate-other-discounts)Deactivate other discounts

Deactivate or delete all other discounts, to ensure that the **Cart line, Order, and Shipping** discount is the only active discount.

### [Anchor to Build a cart](/docs/apps/build/discounts/build-discount-function?extension=rust#build-a-cart)Build a cart

Open your dev store and build a cart with a single item in it.

### [Anchor to Validate discount application](/docs/apps/build/discounts/build-discount-function?extension=rust#validate-discount-application)Validate discount application

On the cart page, you should see that your Discount Function has applied a discount to a cart line and the order subtotal.
Once you navigate to the checkout page and fill in your shipping address, you will see the discounts applied to the shipping rates.

![A checkout summary that shows cart line, subtotal, and shipping discounts](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/discounts/multi-class-DqNqJQCF.png)

### [Anchor to Review the Function execution](/docs/apps/build/discounts/build-discount-function?extension=rust#review-the-function-execution)Review the Function execution

1. In the terminal where `shopify app dev` is running, review your Function executions.

   When [testing Functions on development stores](/docs/apps/build/functions/test-debug-functions#test-your-function-on-a-development-store), the `dev` output shows Function executions, debug logs you've added, and a link to a local file containing full execution details.
2. In a new terminal window, use the Shopify CLI command [`app function replay`](/docs/api/shopify-cli/app/app-function-replay) to [replay a Function execution locally](/docs/apps/build/functions/test-debug-functions#execute-the-function-locally-using-shopify-cli). This lets you debug your Function without triggering it again on Shopify.

   $

   $

   shopify app function replay
3. Select the Function execution from the top of the list. Press `q` to quit when you are finished debugging.

## [Anchor to Deploy your app](/docs/apps/build/discounts/build-discount-function?extension=rust#deploy-your-app)Deploy your app

When you're ready to release your changes to users, you can create and release an [app version](/docs/apps/launch/deployment/app-versions). An app version is a snapshot of your app configuration and all extensions.

1. Navigate to your app directory.
2. Run the following command.

   Optionally, you can provide a name or message for the version using the `--version` and `--message` flags.

   $

   $

   shopify app deploy

Releasing an app version replaces the current active version that's served to stores that have your app installed. It might take several minutes for app users to be upgraded to the new version.

Tip

If you want to create a version, but avoid releasing it to users, then run the `deploy` command with a `--no-release` flag.
You can release the unreleased app version using Shopify CLI's [`release`](/docs/api/shopify-cli/app/app-release) command, or through the Dev Dashboard.

**Tip:**

If you want to create a version, but avoid releasing it to users, then run the `deploy` command with a `--no-release` flag.
You can release the unreleased app version using Shopify CLI's [`release`](/docs/api/shopify-cli/app/app-release) command, or through the Dev Dashboard.

## [Anchor to Tutorial complete!](/docs/apps/build/discounts/build-discount-function?extension=rust#tutorial-complete)Tutorial complete!

You've successfully created a discount function using Shopify Functions. You can now use this Function to apply discounts targeting cart lines, order subtotals, and shipping rates.

---

### [Anchor to Next Steps](/docs/apps/build/discounts/build-discount-function?extension=rust#next-steps)Next Steps

[![](/images/icons/32/build.png)![](/images/icons/32/build-dark.png)

Build a UI extension to configure your discount Function

Add configuration to your discounts experience using metafields and build a user interface for your Function.

Build a UI extension to configure your discount Function

Add configuration to your discounts experience using metafields and build a user interface for your Function.](/docs/apps/build/discounts/build-ui-extension)

[Build a UI extension to configure your discount Function  
  
Add configuration to your discounts experience using metafields and build a user interface for your Function.](/docs/apps/build/discounts/build-ui-extension)

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

Add network access to your discount Function

Learn how to add network access to your discount Function to query an external system for discount code validation.

Add network access to your discount Function

Learn how to add network access to your discount Function to query an external system for discount code validation.](/docs/apps/build/discounts/network-access)

[Add network access to your discount Function  
  
Learn how to add network access to your discount Function to query an external system for discount code validation.](/docs/apps/build/discounts/network-access)

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

Learn more about discount code rejections

Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.

Learn more about discount code rejections

Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.](/docs/apps/build/discounts/discount-rejections)

[Learn more about discount code rejections  
  
Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.](/docs/apps/build/discounts/discount-rejections)

[![](/images/icons/32/gear.png)![](/images/icons/32/gear-dark.png)

Review the UX guidelines

Review the UX guidelines to learn how to implement discounts in user interfaces.

Review the UX guidelines

Review the UX guidelines to learn how to implement discounts in user interfaces.](/docs/apps/build/discounts/ux-for-discounts)

[Review the UX guidelines  
  
Review the UX guidelines to learn how to implement discounts in user interfaces.](/docs/apps/build/discounts/ux-for-discounts)

[![](/images/icons/32/app.png)![](/images/icons/32/app-dark.png)

Learn more about deploying app versions

Learn more about deploying app versions to Shopify

Learn more about deploying app versions

Learn more about deploying app versions to Shopify](/docs/apps/launch/deployment/deploy-app-versions)

[Learn more about deploying app versions  
  
Learn more about deploying app versions to Shopify](/docs/apps/launch/deployment/deploy-app-versions)

Was this page helpful?

YesNo