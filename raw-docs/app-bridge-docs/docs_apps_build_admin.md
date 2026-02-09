---
source: https://shopify.dev/docs/apps/build/admin
---

The Shopify admin is where users configure their stores and manage their businesses. Integrating your app with the Shopify admin gives users functionality that feels familiar and can be easily found.

This guide explains the different ways that you can use Shopify Extensions to integrate your app with the Shopify admin.

---

## [Anchor to App home](/docs/apps/build/admin#app-home)App home

The primary place where users engage with your app is its app home. This is the location where merchants are directed when they navigate to your app in Shopify.

The Shopify admin provides a surface for apps to render the UX for their app home. On the web, the surface is an iframe and in the Shopify mobile app, the surface is a WebView.

![A diagram that shows the Shopify admin. The screenshot highlights an app home. The app navigation is rendered directly in the Shopify admin navigation.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/platform/embedded-app-DNIz8ulq.png)

By combining [Shopify App Bridge](/docs/api/app-bridge) and [Polaris](/docs/api/polaris), you can make your app display seamlessly in the Shopify admin. Polaris enables apps to match the visual appearance of the Shopify admin by using the same design components. App Bridge enables apps to communicate with the Shopify admin and create UI elements outside of the app's surface. Such elements include navigation menus, modals that cover the entire screen, and contextual save bars that prevent users from navigating away from the page when they have unsaved changes.

When you're building your app home, follow the [App Design Guidelines](/docs/apps/design-guidelines) and the [admin performance best practices](/docs/apps/build/performance/admin-installation-oauth) to ensure that you create a great experience for users.

---

## [Anchor to UI extensions in admin](/docs/apps/build/admin#ui-extensions-in-admin)UI extensions in admin

To display a user interface in Shopify admin, apps can include UI extensions. Shopify admin can display three types of UI extensions: admin actions, admin print actions, and admin blocks.

### [Anchor to Admin actions](/docs/apps/build/admin#admin-actions)Admin actions

[Admin actions](/docs/apps/build/admin/actions-blocks#admin-action-ui-extensions) are powered by UI extensions and enable your app to embed transactional workflows that display as modals. These UI extensions let users interact with your app directly from key pages of the Shopify admin, such as the **Products**, **Customers**, and **Orders** pages. You can also create UI extensions that become available when users select multiple resources in an index table, for example, selecting multiple products on the **Products** index page.

![An example admin action UI extension displaying as a modal on the Products page of the Shopify admin, with fields for merchants to input data.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/admin/admin-actions-and-block/action-extension-example-static-UVNY3hK_.png)

### [Anchor to Admin print actions](/docs/apps/build/admin#admin-print-actions)Admin print actions

Admin print actions are a special form of UI extension designed to let your app print documents from key pages in the Shopify admin. Unlike a typical admin actions, these UI extensions are found under the **Print** menu on orders and product pages. Additionally, they contain special APIs to let your app display a preview of a document and print it.

![An example admin print action UI extension.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/admin/admin-actions-and-block/build-an-admin-print-action/print-action-extension-example-BZoi8wgN.png)

### [Anchor to Admin blocks](/docs/apps/build/admin#admin-blocks)Admin blocks

[Admin block UI extensions](/docs/apps/build/admin/actions-blocks#admin-blocks-ui-extensions) let your app embed contextual experiences that display as cards on key pages of the Shopify admin, such as the **Products**, **Customers**, and **Orders** pages. Blocks enable your app to persistently display relevant information to users. They also let users edit your app's data and other product data. After admin block UI extensions are built and deployed, users have the option to add your app's block to resource pages and edit its location on the pages.

![An example admin block UI extension.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/admin/admin-actions-and-block/block-extension-example-static-hrwKM9nW.png)


---

## [Anchor to Admin link extensions](/docs/apps/build/admin#admin-link-extensions)Admin link extensions

[Admin link extensions](/docs/apps/build/admin/admin-links) create links from resource pages in the Shopify admin to related pages of your app. You should use them sparingly because they have the potential to disrupt user workflows with slow, full-page navigations.

---

## [Anchor to Developer tools and resources](/docs/apps/build/admin#developer-tools-and-resources)Developer tools and resources

[![](/images/icons/48/pickaxe-1.png)![](/images/icons/48/pickaxe-1-dark.png)

Shopify App Bridge

A JavaScript library that lets you embed app pages in the Shopify admin.

Shopify App Bridge

A JavaScript library that lets you embed app pages in the Shopify admin.](/docs/api/app-bridge)

[Shopify App Bridge  
  

A JavaScript library that lets you embed app pages in the Shopify admin.](/docs/api/app-bridge)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Polaris design system

Design patterns and a library of UI components, tokens, and icons to build app home pages.

Polaris design system

Design patterns and a library of UI components, tokens, and icons to build app home pages.](/docs/api/polaris)

[Polaris design system  
  

Design patterns and a library of UI components, tokens, and icons to build app home pages.](/docs/api/polaris)

[![](/images/icons/48/bfsgem.png)![](/images/icons/48/bfsgem-dark.png)

App Design Guidelines

Directives to show you what great Shopify apps look like and how they’re crafted.

App Design Guidelines

Directives to show you what great Shopify apps look like and how they’re crafted.](/docs/apps/design-guidelines/)

[App Design Guidelines  
  

Directives to show you what great Shopify apps look like and how they’re crafted.](/docs/apps/design-guidelines/)

[![](/images/icons/48/hearts.png)![](/images/icons/48/hearts-dark.png)

Performance best practices

A set of best practices for building fast and responsive apps in the Shopify admin.

Performance best practices

A set of best practices for building fast and responsive apps in the Shopify admin.](/docs/apps/build/performance/admin-installation-oauth)

[Performance best practices  
  

A set of best practices for building fast and responsive apps in the Shopify admin.](/docs/apps/build/performance/admin-installation-oauth)

---

## [Anchor to Next steps](/docs/apps/build/admin#next-steps)Next steps

* [Create an app home page](/docs/apps/build/scaffold-app) in the Shopify admin.

---

Was this page helpful?

YesNo