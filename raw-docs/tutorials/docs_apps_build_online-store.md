---
source: https://shopify.dev/docs/apps/build/online-store
---

You can expose your app's features to millions of merchants' customers by integrating your app with online stores.

Shopify provides a flexible platform for app development, allowing developers to use [Liquid templates](/docs/api/liquid), host assets on [the Shopify CDN](/docs/storefronts/themes/best-practices/performance/platform#shopify-cdn), and deploy with a versioning release pipeline. This enables merchants to provide a customized shopping experience for their customers.

This guide explains the methods that you can use to integrate your app with online stores.

Caution

If your app integrates with a Shopify theme and you plan to submit it to the Shopify App Store, you must use [theme app extensions](/docs/apps/build/online-store/theme-app-extensions).

**Caution:**

If your app integrates with a Shopify theme and you plan to submit it to the Shopify App Store, you must use [theme app extensions](/docs/apps/build/online-store/theme-app-extensions).

---

## [Anchor to Theme app extensions](/docs/apps/build/online-store#theme-app-extensions)Theme app extensions

Theme app extensions provide your app with two integration types that extend themes in the online store: app blocks and app embed blocks. These integration types take advantage of [Online Store 2.0 features](https://shopify.dev/themes/os20/migration#added-functionality-and-support). Every new app that you submit to the Shopify App Store needs to use theme app extensions to integrate with online store themes.

Theme app extensions don't edit theme code, which provides the following benefits:

* Reduced risk of an app introducing breaking changes to the theme
* Minimized app support debt
* Increased app adoption by offering users a cleaner experience for app integration and customization.
* Increased user retention owing to a graceful, out of the box integration experience.

---

## [Anchor to Other integration methods for themes](/docs/apps/build/online-store#other-integration-methods-for-themes)Other integration methods for themes

You can use the `ScriptTag` resource alongside theme app extensions to provide specific types of support for vintage themes.

If your app integrates with a Shopify theme and you plan to submit it to the Shopify App Store, you must use [theme app extensions](/docs/apps/build/online-store/theme-app-extensions).

Caution

If your app uses the `ScriptTag` resource to edit theme code, then merchants might not be able to upgrade their themes. This results in a poor merchant experience and could negatively impact your ability to attract new app users and retain existing users.

**Caution:**

If your app uses the `ScriptTag` resource to edit theme code, then merchants might not be able to upgrade their themes. This results in a poor merchant experience and could negatively impact your ability to attract new app users and retain existing users.

### [Anchor to Requirements](/docs/apps/build/online-store#requirements)Requirements

If your app adds a visible element to an online store, then the element needs to be deactivated by default so that merchants can either preview or edit the element before activating it. You need to provide merchants with instructions on how to activate either the visible element or the app.

If uninstalling your app leaves code behind in the theme, then you need to provide merchants with instructions on how to remove the code completely, so that they can remain on their theme upgrade path. When a merchant removes the code, leaving even an extra line break or space will take the theme off its upgrade path.

If your app edits theme code and a merchant changes their published theme, then you need to update your app to work on the new theme.

---

## [Anchor to Other integration method for the online store](/docs/apps/build/online-store#other-integration-method-for-the-online-store)Other integration method for the online store

An app proxy forwards requests made to a configurable route on an online store's origin to an external origin to display data on a store page. For example, an app proxy can forward requests from `https://{shop}.myshopify.com/admin/themes/app/my-app` to your app server. App proxies allow you to share data with an online store without worrying about Cross-origin Security Concerns (CORS).

The contents of an app proxy response can be just about anything, from static assets like CSS, JavaScript, and images, to dynamic responses like Liquid templates or JSON data.

---

## [Anchor to What integration method should I use?](/docs/apps/build/online-store#what-integration-method-should-i-use)What integration method should I use?

Review the following app use cases to determine which integration method you should use.

| Use case | Integration method |
| --- | --- |
| Your app injects inline content on a page | [App blocks for themes](/docs/apps/build/online-store/theme-app-extensions/configuration#app-blocks-for-themes) |
| Your app doesn't have a UI component or it adds a floating or overlaid element to a theme | [App embed blocks](/docs/apps/build/online-store/theme-app-extensions/configuration#example-app-embed-block-code) |
| You want to retrieve customer-facing values through an API | [Storefront API](/docs/storefronts/headless/building-with-the-storefront-api)  **Note:** The linked content describes using the Storefront API for custom storefronts. However, most of this information also applies to using the Storefront API in apps that integrate with online stores. |
| Your app injects inline content on a page and you want to add support for vintage themes | [ScriptTags API](/docs/apps/build/online-store/script-tag-legacy) |
| Your app must modify the code of vintage themes | [Asset REST Admin API resource](/docs/apps/build/online-store/asset-legacy) (not recommended) |
| You want to forward requests made to a route on an online store's origin to an external origin to display data on a store page | [App proxies](/docs/apps/build/online-store/display-dynamic-data) |

---

## [Anchor to Considerations for building online store apps](/docs/apps/build/online-store#considerations-for-building-online-store-apps)Considerations for building online store apps

If your app interacts with a store's theme, then you need to make sure that the app also works in the [theme editor](/docs/storefronts/themes/tools/online-editor) environment. If necessary, you can set your app to [detect the theme editor](/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#detect-the-theme-editor), so that you can adjust your app to work in that environment.

If your app extends the online store, then you might want to integrate Shopify theme components and patterns. When you're building your app, you can use the [guides for building Shopify themes](/docs/storefronts/themes) to learn how to implement features for the online store. This information will help you to build an app that feels like a part of a merchant's theme, and behaves as expected with other online store features. Below are a few guides to get you started:

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Building with sections and blocks

Review design principles for building purposeful, flexible blocks for Shopify themes.

Building with sections and blocks

Review design principles for building purposeful, flexible blocks for Shopify themes.](/docs/storefronts/themes/best-practices/templates-sections-blocks)

[Building with sections and blocks  
  

Review design principles for building purposeful, flexible blocks for Shopify themes.](/docs/storefronts/themes/best-practices/templates-sections-blocks)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Support multiple currencies and languages

Learn how to support country selection and use dynamic URLs for themes.

Support multiple currencies and languages

Learn how to support country selection and use dynamic URLs for themes.](/docs/storefronts/themes/markets/multiple-currencies-languages)

[Support multiple currencies and languages  
  

Learn how to support country selection and use dynamic URLs for themes.](/docs/storefronts/themes/markets/multiple-currencies-languages)

---

## [Anchor to Remote products](/docs/apps/build/online-store#remote-products)Remote products

Products from other stores may be present on a merchant's storefront, if the store has opted in to displaying them.

If your app uses the [Cart Ajax API](/docs/api/ajax/reference/cart), you may need to adjust its behavior for remote products:

* For free shipping qualifications or applying cart discounts, you should exclude remote products from the calculations. Remote products have their own shipping arrangements from their origin stores, and discounts should only apply to owned products.
* For abandoned cart recovery, you should exclude remote products because the remote product URLs will expire after some time, making recovery attempts unreliable.
* For other use cases that rely on the [Cart Ajax API](/docs/api/ajax/reference/cart), decide whether your logic should exclude remote products.

Remote products are not provided to [Shopify Function inputs](/docs/api/functions/latest#input), and Shopify Function operations cannot target remote products.

### [Anchor to Identifying remote products](/docs/apps/build/online-store#identifying-remote-products)Identifying remote products

Remote products can be identified in the [Cart Ajax API](/docs/api/ajax/reference/cart) response by the presence of [`remote: true`](/docs/api/ajax/reference/cart#json-of-a-cart-with-remote-products) on the cart line items.

Remote products will be present in [Storefront API](/docs/api/storefront/latest/queries/cart) responses, however they are not currently identifiable by any distinguishing properties. Support for this is coming soon.

---

## [Anchor to Tools and resources](/docs/apps/build/online-store#tools-and-resources)Tools and resources

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Use JavaScript responsibly

Follow our principles for optimizing your JavaScript.

Use JavaScript responsibly

Follow our principles for optimizing your JavaScript.](/docs/storefronts/themes/best-practices/performance)

[Use JavaScript responsibly  
  

Follow our principles for optimizing your JavaScript.](/docs/storefronts/themes/best-practices/performance)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Verify theme support for app blocks

Verify whether an online store's published theme supports your theme app extension or requires another method of app integration.

Verify theme support for app blocks

Verify whether an online store's published theme supports your theme app extension or requires another method of app integration.](/docs/apps/build/online-store/verify-support)

[Verify theme support for app blocks  
  

Verify whether an online store's published theme supports your theme app extension or requires another method of app integration.](/docs/apps/build/online-store/verify-support)

---

## [Anchor to Next steps](/docs/apps/build/online-store#next-steps)Next steps

* [Add app blocks and app embedded blocks with theme app extensions](/docs/apps/build/online-store/theme-app-extensions)
* [Use the Asset or ScriptTag integration methods](/docs/apps/build/online-store/script-tag-legacy)
* [Use the App proxies integration method](/docs/apps/build/online-store/display-dynamic-data)

---

Was this page helpful?

YesNo