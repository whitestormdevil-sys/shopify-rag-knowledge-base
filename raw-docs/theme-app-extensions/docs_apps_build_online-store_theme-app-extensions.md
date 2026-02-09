---
source: https://shopify.dev/docs/apps/build/online-store/theme-app-extensions
---

Theme app extensions allow merchants to easily add dynamic elements to their themes without having to interact with Liquid templates or code. For example, dynamic elements can include product reviews, prices, ratings, or interactive 3D models of products. Theme app extensions can integrate with Online Store 2.0 themes.

---

## [Anchor to Benefits of using theme app extensions](/docs/apps/build/online-store/theme-app-extensions#benefits-of-using-theme-app-extensions)Benefits of using theme app extensions

* Theme app extensions automatically expose your app in the theme editor. You can leverage the editor’s visual editing capabilities without needing to replicate them in your app.
* You can deploy your app at the same time to all online stores that use it. You also have access to [versioning](/docs/apps/build/app-extensions#versioning-and-deployment), and [asset hosting on the Shopify CDN](/docs/apps/build/online-store/theme-app-extensions/configuration#performance).
* A single set of integration logic and instructions works for all themes.
* Merchants won't need to manually edit their theme code.

---

## [Anchor to Theme app extensions resources](/docs/apps/build/online-store/theme-app-extensions#theme-app-extensions-resources)Theme app extensions resources

Theme app extensions contain the following resources:

* Blocks - Liquid files that act as the entry point for what you want to inject in a theme. The following block types are supported:

  + [App blocks](/docs/apps/build/online-store/theme-app-extensions/configuration#app-blocks-for-themes)
  + [App embed blocks](/docs/apps/build/online-store/theme-app-extensions/configuration#app-embed-blocks)
* Assets - CSS, JavaScript, and other static app content that gets injected into themes.
* Snippets - Reusable Liquid snippets that can be used across multiple blocks.

  Learn more about the [theme app extensions framework](/docs/apps/build/online-store/theme-app-extensions/configuration).

---

## [Anchor to Designing for the best merchant experience](/docs/apps/build/online-store/theme-app-extensions#designing-for-the-best-merchant-experience)Designing for the best merchant experience

Apps built in the theme app extension framework don't edit theme code, which decreases the risk of introducing breaking changes to the theme, makes it easier to iterate on the content of the integration, and provides for a better merchant experience.

Merchants can use the [theme editor](/docs/storefronts/themes/tools/online-editor) to configure exposed settings and add app blocks in theme sections for precise positioning in a page's layout.

---

## [Anchor to Resources](/docs/apps/build/online-store/theme-app-extensions#resources)Resources

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)

Dawn

Explore Shopify's Online Store 2.0 reference theme, built to support app blocks.

Dawn

Explore Shopify's Online Store 2.0 reference theme, built to support app blocks.](https://github.com/Shopify/dawn)

[Dawn  
  

Explore Shopify's Online Store 2.0 reference theme, built to support app blocks.](https://github.com/Shopify/dawn)

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-dark.png)

Shopify CLI

Learn about Shopify CLI, which is used for creating and registering theme app extensions and for version control.

Shopify CLI

Learn about Shopify CLI, which is used for creating and registering theme app extensions and for version control.](/docs/apps/build/cli-for-apps)

[Shopify CLI  
  

Learn about Shopify CLI, which is used for creating and registering theme app extensions and for version control.](/docs/apps/build/cli-for-apps)

---

## [Anchor to Next steps](/docs/apps/build/online-store/theme-app-extensions#next-steps)Next steps

* [Get started with theme app extensions](/docs/apps/build/online-store/theme-app-extensions/build)
* [Review the theme app extensions framework](/docs/apps/build/online-store/theme-app-extensions/configuration)
* [Understand the UX guidelines for theme app extensions](/docs/apps/build/online-store/theme-app-extensions/ux)
* [Update your app to use theme app extensions](/docs/apps/build/online-store/theme-app-extensions/migrate)

---

Was this page helpful?

YesNo