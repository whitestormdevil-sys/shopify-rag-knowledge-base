---
source: https://shopify.dev/docs/api/app-bridge
---

The App Bridge library provides APIs that enable Shopify apps to render UI in the Shopify [app home](/docs/apps/build/admin) surface.

Apps built with Shopify App Bridge are more performant, flexible, and seamlessly integrate with the Shopify admin. You can use Shopify App Bridge with [Polaris](/docs/api/polaris) to provide a consistent and intuitive user experience that matches the rest of the Shopify admin.

On the web, your app renders in an iframe and in the [Shopify mobile app](https://www.shopify.com/install) it renders in a WebView.

Note

App Bridge components don't render as part of the app's component hierarchy. They're React-like wrappers around JavaScript messages that communicate with the Shopify admin. The Shopify admin does the UI rendering.

**Note:**

App Bridge components don't render as part of the app's component hierarchy. They're React-like wrappers around JavaScript messages that communicate with the Shopify admin. The Shopify admin does the UI rendering.

![A diagram of the Shopify admin. The screenshot highlights an App Bridge component, which is controlled by the app but rendered by Shopify. The screenshot also highlights the other parts of the Shopify admin, which are rendered by Shopify, and the app surface, which is rendered by the app with Polaris React.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/tools/app-bridge-polaris-render-eOuCZf_w.png)

App Bridge enables you to do the following from your app home:

* Render a [navigation menu](/docs/api/app-home/app-bridge-web-components/app-nav) on the left of the Shopify admin.
* Render a [save bar](/docs/api/app-home/apis/save-bar) above the top bar of the Shopify admin.
* Render a [title bar](/docs/api/app-home/app-bridge-web-components/title-bar) with primary and secondary actions.

  The latest version of App Bridge is built on top of web components and APIs to provide a flexible and familiar development environment. Your app can invoke these [APIs](/docs/api/app-home) using vanilla JavaScript functions.

---

## [Anchor to Polaris](/docs/api/app-bridge#polaris)Polaris

Inside the app surface, we encourage you to use [Polaris](/docs/api/polaris) so you create familiar and consistent user experiences between your app and the Shopify admin. You can refer to the [App Design Guidelines](/docs/apps/design-guidelines) to create familiar and consistent user experiences.

---

## [Anchor to Next steps](/docs/api/app-bridge#next-steps)Next steps

* [Getting started with Shopify App Bridge](/docs/api/app-home)
* [Authenticate an embedded app using session tokens](/docs/apps/build/authentication-authorization/session-tokens/set-up-session-tokens)

---

Was this page helpful?

YesNo