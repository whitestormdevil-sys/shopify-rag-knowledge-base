---
source: https://shopify.dev/docs/apps/build/discounts
---

Discount apps integrate with the Shopify admin to provide discount types for app users. This guide introduces the ways that you can extend your app code into Shopify checkout and customize the discount experience.

* Use the [GraphQL Admin API](#build-with-the-graphql-admin-api) to create and manage [discounts that are native to Shopify](https://help.shopify.com/manual/discounts/discount-types).
* Use [Shopify Functions](#build-with-shopify-functions) to extend your app code into Shopify checkout and create discount functionality that isn't offered out of the box with Shopify.
* Build configuration UIs with [Admin UI extensions](/docs/apps/build/discounts/ux-for-discounts#admin-ui-extensions-vs-react-router-app-ui) or [React Router App UI](/docs/apps/build/discounts/ux-for-discounts#admin-ui-extensions-vs-react-router-app-ui), to allow merchants to configure the discount functionality in the Shopify admin.

---

## [Anchor to Build with the GraphQL Admin API](/docs/apps/build/discounts#build-with-the-graphql-admin-api)Build with the GraphQL Admin API

The [GraphQL Admin API](/docs/api/admin-graphql) enables you to create and manage Shopify discounts.

### [Anchor to Discount methods](/docs/apps/build/discounts#discount-methods)Discount methods

You can create discounts that are either applied automatically, or applied with discount codes.

The following table describes the different discount methods you can use as part of your app using the GraphQL Admin API:

| Discount method | Description | Example use cases |
| --- | --- | --- |
| Automatic discount | A discount that's automatically applied at checkout and on a cart if prerequisites are met. | - A [Buy X Get Y or Spend X Get Y automatic discount](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate) - A [percentage or fixed-amount automatic discount](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) |
| Code discount | A discount that customers can redeem using a specific code. Merchants can create and share discount codes individually with customers. | - A [Buy X Get Y or Spend X Get Y code discount](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate) - A [percentage or fixed-amount code discount](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate) - A [free shipping code discount](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingCreate) |

Visit the Shopify Help Center to learn about the limitations and considerations that apply to each discount type:

* [Automatic discounts](https://help.shopify.com/manual/discounts/discount-types#automatic-discounts)
* [Code discounts](https://help.shopify.com/manual/discounts/discount-types#considerations-for-creating-discount-codes)

### [Anchor to Access scopes](/docs/apps/build/discounts#access-scopes)Access scopes

To use discount-related GraphQL mutations when building with the GraphQL Admin API, your app needs to request the following [access scopes](/docs/api/usage/access-scopes) for a Shopify store:

| Access scope | Required or optional? | Description |
| --- | --- | --- |
| `write_discounts` | Required | Allows apps to create and update Shopify discounts |
| `read_customers` | Optional | Allows apps to query a store's customers |
| `read_products` | Optional | Allows apps to query a store's products |
| `read_shipping` | Optional | Allows apps to query the countries that a store ships to |

---

## [Anchor to Build with Shopify Functions](/docs/apps/build/discounts#build-with-shopify-functions)Build with Shopify Functions

[Shopify Functions](/docs/apps/build/functions) enable you to create discount functionality that isn't offered out of the box with Shopify. For example, a discount Function can be used to create a single discount that can reduce the price of a product and shipping rate at once, or volume discounts with different discount rates when a line item quantity meets defined thresholds.

When you create and deploy an app with a Function, you can define a new discount type. After merchants install the app, they can create discounts using these custom discount types. Shopify executes the Function to calculate discounts in real-time when buyers add products to their cart.

![How a developer can create, test, and deploy a Function](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/functions/create-test-deploy-B8EIsTvz.png)

### [Anchor to How discounts are applied](/docs/apps/build/discounts#how-discounts-are-applied)How discounts are applied

Shopify's discount system allows for targeted price reductions across different parts of the shopping experience. Discounts can be applied to the following:

* **Cart lines**: Reductions applied to specific products in the cart
* **Order subtotals**: Discounts applied to the entire purchase amount
* **Shipping rates**: Reductions in shipping costs

  When you create a Discount, you can specify where the discount should be applied by defining discount classes on a discount instance. These classes determine which part of the cart the discount Function targets, enabling Shopify to correctly calculate and apply the appropriate price reduction during checkout.

### [Anchor to Discount classes](/docs/apps/build/discounts#discount-classes)Discount classes

Discount classes are used to define the effect of a discount on a cart. The discount's `discountClasses` field determines which Function targets will be executed during checkout.

App discounts built with the Discount Function API can return operations that use Order and Product discount classes in their [`CartLinesDiscountsGenerateRunResult`](/docs/api/functions/reference/discount/graphql/cartlinesdiscountsgeneraterunresult) and the Shipping class in [`CartDeliveryOptionsDiscountsGenerateRunResult`](/docs/api/functions/reference/discount/graphql/cartdeliveryoptionsdiscountsgeneraterunresult).

| Discount Class | API Target | Description |
| --- | --- | --- |
| Order | [`CartLinesDiscountsGenerateRunResult`](/docs/api/functions/reference/discount/graphql/cartlinesdiscountsgeneraterunresult) | Applies discounts to the entire cart through cart operations |
| Product | [`CartLinesDiscountsGenerateRunResult`](/docs/api/functions/reference/discount/graphql/cartlinesdiscountsgeneraterunresult) | Applies discounts to specific products through cart operations |
| Shipping | [`CartDeliveryOptionsDiscountsGenerateRunResult`](/docs/api/functions/reference/discount/graphql/cartdeliveryoptionsdiscountsgeneraterunresult) | Applies discounts to shipping rates through delivery operations |

---

## [Anchor to Related mutations and queries](/docs/apps/build/discounts#related-mutations-and-queries)Related mutations and queries

Explore the following resources to manage discounts in your app. Use mutations to craft, modify, and remove discounts, and use queries to retrieve detailed listings.

### [Anchor to Automatic discount mutations](/docs/apps/build/discounts#automatic-discount-mutations)Automatic discount mutations

The following table outlines some common mutations for creating, updating, and deleting [automatic](#discount-methods) discounts:

| Discount type | Mutations |
| --- | --- |
| Buy X Get Y or Spend X Get Y | [discountAutomaticBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyCreate) [discountAutomaticBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBxgyUpdate) [discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete) |
| Percentage or fixed amount | [discountAutomaticBasicCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicCreate) [discountAutomaticBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticBasicUpdate) [discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete) |
| Free shipping | [discountAutomaticFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingCreate) [discountAutomaticFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticFreeShippingUpdate) [discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete) |
| App | [discountAutomaticAppCreate](/docs/api/admin-graphql/latest/mutations/discountAutomaticAppCreate) [discountAutomaticAppUpdate](/docs/api/admin-graphql/latest/mutations/discountAutomaticAppUpdate) [discountAutomaticDelete](/docs/api/admin-graphql/latest/mutations/discountAutomaticDelete) |

### [Anchor to Code discount mutations](/docs/apps/build/discounts#code-discount-mutations)Code discount mutations

The following table outlines some common mutations for creating, updating, and deleting [code](#discount-methods) discounts:

| Discount type | Mutations |
| --- | --- |
| Buy X Get Y or Spend X Get Y | [discountCodeBxgyCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyCreate) [discountCodeBxgyUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBxgyUpdate) [discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete) |
| Percentage or fixed amount | [discountCodeBasicCreate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate) [discountCodeBasicUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeBasicUpdate) [discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete) |
| Free shipping | [discountCodeFreeShippingCreate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingCreate) [discountCodeFreeShippingUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeFreeShippingUpdate) [discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete) |
| App | [discountCodeAppCreate](/docs/api/admin-graphql/latest/mutations/discountCodeAppCreate) [discountCodeAppUpdate](/docs/api/admin-graphql/latest/mutations/discountCodeAppUpdate) [discountCodeDelete](/docs/api/admin-graphql/latest/mutations/discountCodeDelete) |
| Bulk actions | [discountCodeBulkActivate](/docs/api/admin-graphql/latest/mutations/discountcodebulkactivate) [discountCodeBulkDeactivate](/docs/api/admin-graphql/latest/mutations/discountcodebulkdeactivate) [discountCodeBulkDelete](/docs/api/admin-graphql/latest/mutations/discountcodebulkdelete) |

### [Anchor to Queries](/docs/apps/build/discounts#queries)Queries

The following table outlines some common queries for interacting with [automatic and code](#discount-methods) discounts.

| Discount type | Queries |
| --- | --- |
| Automatic discounts | [automaticDiscountNode](/docs/api/admin-graphql/latest/queries/automaticDiscountNode) [automaticDiscountNodes](/docs/api/admin-graphql/latest/queries/automaticDiscountNodes) |
| Code discounts | [codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode) [codeDiscountNodes](/docs/api/admin-graphql/latest/queries/codeDiscountNodes) |

---

## [Anchor to Getting started](/docs/apps/build/discounts#getting-started)Getting started

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Build a Discount Function

Learn how to create a Discount Function that applies discounts to cart lines, order subtotal, and shipping rates.

Build a Discount Function

Learn how to create a Discount Function that applies discounts to cart lines, order subtotal, and shipping rates.](/docs/apps/build/discounts/build-discount-function)

[Build a Discount Function  
  

Learn how to create a Discount Function that applies discounts to cart lines, order subtotal, and shipping rates.](/docs/apps/build/discounts/build-discount-function)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Build a UI extension

Add configuration to your discounts experience using metafields and build a user interface with UI extensions.

Build a UI extension

Add configuration to your discounts experience using metafields and build a user interface with UI extensions.](/docs/apps/build/discounts/build-ui-extension)

[Build a UI extension  
  

Add configuration to your discounts experience using metafields and build a user interface with UI extensions.](/docs/apps/build/discounts/build-ui-extension)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Build a React Router app UI

Add configuration to your discounts experience using metafields and build a user interface with React Router.

Build a React Router app UI

Add configuration to your discounts experience using metafields and build a user interface with React Router.](/docs/apps/build/discounts/build-ui-with-react-router)

[Build a React Router app UI  
  

Add configuration to your discounts experience using metafields and build a user interface with React Router.](/docs/apps/build/discounts/build-ui-with-react-router)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Add network access

Learn how to add network access to your Discount Function to query external systems for discount validation.

Add network access

Learn how to add network access to your Discount Function to query external systems for discount validation.](/docs/apps/build/discounts/network-access)

[Add network access  
  

Learn how to add network access to your Discount Function to query external systems for discount validation.](/docs/apps/build/discounts/network-access)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Reject invalid discount codes

Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.

Reject invalid discount codes

Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.](/docs/apps/build/discounts/discount-rejections)

[Reject invalid discount codes  
  

Learn how to build a Discount Function that rejects invalid discount codes and displays custom error messages.](/docs/apps/build/discounts/discount-rejections)

---

## [Anchor to Developer tools and resources](/docs/apps/build/discounts#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to learn more about building with Shopify Functions:

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-dark.png)

Shopify Functions

Customize the backend logic that powers parts of Shopify.

Shopify Functions

Customize the backend logic that powers parts of Shopify.](/docs/apps/build/functions)

[Shopify Functions  
  

Customize the backend logic that powers parts of Shopify.](/docs/apps/build/functions)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Input queries and metafields

Make your code reusable by replacing hard-coded variables in your Function with metafield values.

Input queries and metafields

Make your code reusable by replacing hard-coded variables in your Function with metafield values.](/docs/apps/build/functions/input-queries/metafields-for-input-queries)

[Input queries and metafields  
  

Make your code reusable by replacing hard-coded variables in your Function with metafield values.](/docs/apps/build/functions/input-queries/metafields-for-input-queries)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Admin UI extension components

Build your user interface using Admin UI extension components.

Admin UI extension components

Build your user interface using Admin UI extension components.](/docs/api/admin-extensions/components)

[Admin UI extension components  
  

Build your user interface using Admin UI extension components.](/docs/api/admin-extensions/components)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Shopify App Bridge

Build your user interface using components from Shopify App Bridge library.

Shopify App Bridge

Build your user interface using components from Shopify App Bridge library.](/docs/api/app-bridge)

[Shopify App Bridge  
  

Build your user interface using components from Shopify App Bridge library.](/docs/api/app-bridge)

---

Was this page helpful?

YesNo