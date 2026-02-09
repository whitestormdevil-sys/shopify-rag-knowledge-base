---
source: https://shopify.dev/docs/apps/build/app-extensions
---

An app extension enables you to add your app's functionality to Shopify user interfaces. This guide introduces app extensions and how they work.

---

## [Anchor to How it works](/docs/apps/build/app-extensions#how-it-works)How it works

An app extension surfaces the functionality of your app where and when users need it most. App extensions are useful for apps that require quick, frequent actions from users.

For example, your app's actions can appear as dropdown items in Shopify admin for orders, products, customers, and other resources. You can produce interfaces that easily mimic the Shopify look-and-feel, and make your app seamlessly appear in Shopify Point of Sale (POS).

### [Anchor to Without an app extension](/docs/apps/build/app-extensions#without-an-app-extension)Without an app extension

Without an app extension, users interact directly with your app. Your app relays information to Shopify that gets surfaced back to the users through your app:

![An example of an app interacting with a users without an app extension](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/app-extensions-overview-without-DjGHfpdv.png)

### [Anchor to With an app extension](/docs/apps/build/app-extensions#with-an-app-extension)With an app extension

With an app extension, users interact with Shopify. Shopify relays information to your app that gets surfaced back to the users through your app extension in Shopify:

![An example of an app interacting with a user with an app extension](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/app-extensions-overview-with-LWTIK-zM.png)

Note

An app extension isn't an app. It's a mechanism that lets an app add features to certain defined parts of several Shopify user interfaces. Apps that use extensions must adhere to the same [authentication requirements](/docs/apps/build/authentication-authorization) and [rate limits](/docs/api/usage/limits#rate-limits) as apps that don't use extensions.

**Note:**

An app extension isn't an app. It's a mechanism that lets an app add features to certain defined parts of several Shopify user interfaces. Apps that use extensions must adhere to the same [authentication requirements](/docs/apps/build/authentication-authorization) and [rate limits](/docs/api/usage/limits#rate-limits) as apps that don't use extensions.

---

## [Anchor to Creating app extensions](/docs/apps/build/app-extensions#creating-app-extensions)Creating app extensions

You can create app extensions using [Shopify CLI](/docs/apps/build/cli-for-apps) and the [`app generate extension` command](/docs/api/shopify-cli/app/app-generate-extension).

For information about building and previewing app extensions, refer to the documentation for your extension type.

### [Anchor to Extension-only apps](/docs/apps/build/app-extensions#extension-only-apps)Extension-only apps

Extension-only apps are apps that don't have embedded app pages. Because they're made up entirely of extensions, you can host extension-only apps on Shopify.

Note

Extension-only apps can only be installed with [custom distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method).

**Note:**

Extension-only apps can only be installed with [custom distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method).

[Learn about extension-only apps that don't require a web server](/docs/apps/build/app-extensions/build-extension-only-app).

---

## [Anchor to Configuring app extensions](/docs/apps/build/app-extensions#configuring-app-extensions)Configuring app extensions

When you [generate an app extension](/docs/api/shopify-cli/app/app-generate-extension), a TOML configuration file named `shopify.extension.toml` is automatically generated in your app's extension directory. The TOML file is located in the [`extensions/` directory](/docs/apps/build/cli-for-apps/app-structure#directory-structure) of your app project.

For information about the properties that you can configure in the TOML file, refer to [Configuring app extensions](/docs/apps/build/app-extensions/configure-app-extensions).

---

## [Anchor to Versioning and deployment](/docs/apps/build/app-extensions#versioning-and-deployment)Versioning and deployment

Your app configuration and all extensions are versioned together as a single [app version](/docs/apps/launch/deployment/app-versions).

When you run the [`deploy` command](/docs/api/shopify-cli/app/app-deploy) using [Shopify CLI](/docs/api/shopify-cli), an app version is created and released. You can revert to a previous app version at any time. You can also create an app version from the Dev Dashboard.

Releasing an app version replaces the current active version that's served to stores that have your app installed. It might take several minutes for app users to be upgraded to the new version.

[Learn how to deploy extensions](/docs/apps/launch/deployment/deploy-app-versions).

---

## [Anchor to Reviews and approvals](/docs/apps/build/app-extensions#reviews-and-approvals)Reviews and approvals

Some app extensions need to be reviewed and approved before they're released to users.

If an app extension needs to be reviewed, then you can't release the related app version until you [submit it for review](/docs/apps/launch/deployment/deploy-app-versions#submit-an-app-version-for-review) and it's been approved.

To learn whether your extension type needs to be reviewed, refer to the [list of extension types](/docs/apps/build/app-extensions/list-of-app-extensions).

---

## [Anchor to Removing app extensions](/docs/apps/build/app-extensions#removing-app-extensions)Removing app extensions

If you no longer want users to use an app extension, or you want to temporarily disable an app extension, then you can remove it.

[Learn how to remove an app extension from your app](/docs/apps/build/app-extensions/remove-app-extension).

---

## [Anchor to Developer tools and resources](/docs/apps/build/app-extensions#developer-tools-and-resources)Developer tools and resources

[![](/images/icons/48/app.png)![](/images/icons/48/app-dark.png)

List of app extensions

Learn about the available app extensions that you can use to add your app's functionality to Shopify user interfaces.

List of app extensions

Learn about the available app extensions that you can use to add your app's functionality to Shopify user interfaces.](/docs/apps/build/app-extensions/list-of-app-extensions)

[List of app extensions  
  

Learn about the available app extensions that you can use to add your app's functionality to Shopify user interfaces.](/docs/apps/build/app-extensions/list-of-app-extensions)

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-dark.png)

Extension-only apps

Learn about extension-only apps that don't require a web server.

Extension-only apps

Learn about extension-only apps that don't require a web server.](/docs/apps/build/app-extensions/build-extension-only-app)

[Extension-only apps  
  

Learn about extension-only apps that don't require a web server.](/docs/apps/build/app-extensions/build-extension-only-app)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Configuring app extensions

Learn about app extension properties that you can configure in the TOML file.

Configuring app extensions

Learn about app extension properties that you can configure in the TOML file.](/docs/apps/build/app-extensions/configure-app-extensions)

[Configuring app extensions  
  

Learn about app extension properties that you can configure in the TOML file.](/docs/apps/build/app-extensions/configure-app-extensions)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

App versions

Learn about deploying and releasing app versions.

App versions

Learn about deploying and releasing app versions.](/docs/apps/launch/deployment/app-versions)

[App versions  
  

Learn about deploying and releasing app versions.](/docs/apps/launch/deployment/app-versions)

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Remove an app extension

Learn how to remove app extensions from your app.

Remove an app extension

Learn how to remove app extensions from your app.](/docs/apps/build/app-extensions/remove-app-extension)

[Remove an app extension  
  

Learn how to remove app extensions from your app.](/docs/apps/build/app-extensions/remove-app-extension)

---

## [Anchor to Next steps](/docs/apps/build/app-extensions#next-steps)Next steps

* Consult the [list of app extensions](/docs/apps/build/app-extensions/list-of-app-extensions) to determine which app extensions are versioned, which app extensions require reviews and approvals, where you manage the app extensions in Shopify, and more.

---

Was this page helpful?

YesNo