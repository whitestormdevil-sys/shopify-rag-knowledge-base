---
source: https://shopify.dev/docs/apps/build/pos
---

With Shopify POS UI extensions, you can add custom functionality directly into Shopify's [point-of-sale interface](https://apps.shopify.com/shopify-pos). For example, you can offer loyalty program enrollment at checkout, or apply custom discounts based on what customers are purchasing.

This guide explains how POS UI extensions work. For a step-by-step tutorial to help you start building, see [Getting started with POS UI extensions](/docs/apps/build/pos/getting-started).

---

## [Anchor to Benefits](/docs/apps/build/pos#benefits)Benefits

Apps built with POS UI extensions provide:

* **Native performance**: Extensions render as native components for faster load times.
* **Consistent design**: Automatically match Shopify's design system and receive updates.
* **Guided development**: Use pre-built components and defined extension targets.
* **Cross-platform compatibility**: Offer an identical experience across iOS and Android platforms.

---

## [Anchor to What you can build](/docs/apps/build/pos#what-you-can-build)What you can build

Apps built with POS UI extensions can help merchants at every stage of the purchase process:

* **Discount and promotion apps**: Apply custom discounts, loyalty rewards, and special offers.
* **Inventory management tools**: Alert merchants to low inventory, show real-time product availability across all physical stores, or suggest ship-from-store options.
* **Customer relationship apps**: Update customers' profiles and purchase histories or send personalized emails or text messages after a purchase.
* **Payment and checkout enhancements**: Build custom payment flows, customize receipts, or manage gift card balances.
* **Analytics and reporting**: Display real-time sales data, staff performance metrics, and business insights.

---

## [Anchor to How it works](/docs/apps/build/pos#how-it-works)How it works

POS UI extensions are made up of three interconnected parts: **targets** that determine where your extension appears in the POS interface, **target APIs** that provide access to data and functionality based on your chosen target, and **Polaris web components** that define which interface elements you can use.

### [Anchor to Targets](/docs/apps/build/pos#targets)Targets

Targets define where in the Shopify POS interface your custom UI appears and what types of UI components you can render there. You can think of defining a target as creating a container at a particular location in the POS UI, into which you can render Polaris web components. There are three types of targets:

* **Tiles**: Used to display tiles on the smart grid.
* **Actions**: Used to launch modals or full-screen views from menu item buttons.
* **Blocks**: Used to display custom sections within screens.

For example, the target `pos.product-details.block.render` creates a hook on the product details screen where you can render a custom section.

Actions have two varieties: menu item and modal. Use these together to create buttons that launch modals: use an `.action.menu-item.render` target to render a button in a menu, and then use the corresponding `.action.render` target to render a modal when the button is tapped.

You define the targets for your extension in its [configuration file](/docs/api/pos-ui-extensions/latest#configuration). To see a full list of the targets you can define, and to learn more about using them, see the [POS UI extensions reference](/docs/api/pos-ui-extensions/latest/targets).

### [Anchor to Target APIs](/docs/apps/build/pos#target-apis)Target APIs

Target APIs read data and perform operations in Shopify POS like updating cart details, applying discounts, or showing a toast. Many of these APIs are reactive; you can subscribe to changes using standard Preact hooks and automatically perform operations or update your UI when the underlying data changes.

Available APIs vary by target type. To see which APIs can be used with which targets, and what operations each API supports, see the [POS UI extensions reference](/docs/api/pos-ui-extensions/latest/target-apis).

Extensions can also [query the GraphQL Admin API directly](/docs/api/pos-ui-extensions/latest#direct-api-access) using standard `fetch()` calls. You can use the GraphQL Admin API to perform operations like looking up a customer's order history with the [`orders`](/docs/api/admin-graphql/latest/queries/orders) query, or checking the availability of products at other locations with the [`inventoryItem`](/docs/api/admin-graphql/latest/queries/inventoryitem) or [`product`](/docs/api/admin-graphql/latest/queries/product) queries.

### [Anchor to Polaris web components](/docs/apps/build/pos#polaris-web-components)Polaris web components

Components are the building blocks you use to render your custom UI in the POS interface. Shopify's UI toolkit provides a wide range of Polaris web components like buttons, tiles, and modals that match the Shopify POS design system. You can combine components and nest them inside each other. For example, a modal can contain buttons, text, forms, and media.

To add a UI component to the POS app interface, you write code that renders that component in the target where you want it to appear. The components you can use with a target depend on that target's type. For example, tile targets like `pos.home.tile.render` can only render a tile.

To see which components your chosen targets support, see the [POS UI extensions reference](/docs/api/pos-ui-extensions/latest/polaris-web-components).

---

## [Anchor to Extension-only and server-hosted apps](/docs/apps/build/pos#extension-only-and-server-hosted-apps)Extension-only and server-hosted apps

Some extensions don't need an app hosted on a server—all the functionality runs on the merchant's device within the extension itself. We call these extension-only apps. You can follow an example to build an extension-only app in the [getting started tutorial](/docs/apps/build/pos/getting-started). Here's how data flows through an an extension-only app:

![Data flows through an extension-only app](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/pos/extension_only_app_flow-ChSt4cgR.png)

Extension-only apps have some limitations though. If you want to do any of the following, you'll need to implement a backend by hosting an app on a server that your extension connects to:

* Make calls to Shopify APIs other than the Admin API
* Integrate with external services or third-party APIs
* Store secrets or sensitive business logic

POS UI extensions are client-side JavaScript applications, like React or Vue apps. Follow the same client-side and server-side patterns you'd use in traditional web applications, and keep secrets and business logic in your server-hosted app.

The following diagram illustrates the flow of data between a POS UI extension, Shopify POS, the Shopify platform, and a server-hosted app. To follow an example of building an extension that uses a server-hosted app, see [Build a print UI extension](/docs/apps/build/pos/tutorials/build-print-extension).

![Data flows through a server-hosted app](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/pos/server_hosted_app_flow-BJPkK6qD.png)


---

## [Anchor to Developer tools and resources](/docs/apps/build/pos#developer-tools-and-resources)Developer tools and resources

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

POS UI extensions reference

Integrate with merchant workflows and offer enhanced functionality that feels native to the POS experience.

POS UI extensions reference

Integrate with merchant workflows and offer enhanced functionality that feels native to the POS experience.](/docs/api/pos-ui-extensions)

[POS UI extensions reference  
  

Integrate with merchant workflows and offer enhanced functionality that feels native to the POS experience.](/docs/api/pos-ui-extensions)

---

## [Anchor to Next steps](/docs/apps/build/pos#next-steps)Next steps

* Follow the [Getting started with POS UI extensions](/docs/apps/build/pos/getting-started) tutorial to build your first POS UI extension.
* [Build a discount extension](/docs/apps/build/pos/tutorials/build-discount-extension) that applies discounts to items in a cart.
* [Build a print UI extension](/docs/apps/build/pos/tutorials/build-print-extension) that generates, previews, and prints custom documents.
* [Build a subscription UI extension](/docs/apps/build/pos/tutorials/build-subscription-extension) that enables merchants to sell subscriptions in-store.

---

Was this page helpful?

YesNo