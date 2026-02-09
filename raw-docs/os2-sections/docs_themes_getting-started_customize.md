---
source: https://shopify.dev/docs/themes/getting-started/customize
---

As a theme developer, you can customize themes for Shopify merchants. These customizations might range from small tweaks to complete redesigns. Shopify Partners can offer theme customization services through the [Shopify Partner Directory](https://help.shopify.com/partners/directory).

In this tutorial, you'll use Shopify CLI to customize a merchant's theme and then share your progress with them.

If you're customizing a theme for a client, then you should also [review our best practices for working with merchants](/docs/storefronts/themes/best-practices/merchant-stores).

Caution

This tutorial describes customizing themes that don't use the [Shopify GitHub integration](/docs/storefronts/themes/tools/github). If your merchant uses the Shopify GitHub integration to manage their theme code, then you can request access to the repository from them, or you can push changes to the theme that's connected to a branch of the repository using Shopify CLI.

**Caution:**

This tutorial describes customizing themes that don't use the [Shopify GitHub integration](/docs/storefronts/themes/tools/github). If your merchant uses the Shopify GitHub integration to manage their theme code, then you can request access to the repository from them, or you can push changes to the theme that's connected to a branch of the repository using Shopify CLI.

---

## [Anchor to What you'll learn](/docs/storefronts/themes/getting-started/customize#what-youll-learn)What you'll learn

After you've finished this tutorial, you'll have accomplished the following:

* Gained access to the merchant's store
* Set up your local development environment
* Downloaded a copy of the merchant's theme
* Made a change and previewed it
* Shared your changes with the merchant
* Published your changes

---

## [Anchor to Requirements](/docs/storefronts/themes/getting-started/customize#requirements)Requirements

* You've installed [Shopify CLI](/docs/api/shopify-cli)
* The URL of the store that you want to work on, such as `example.myshopify.com`.

---

## [Anchor to Step 1: Request access to the merchant's store](/docs/storefronts/themes/getting-started/customize#step-1-request-access-to-the-merchants-store)Step 1: Request access to the merchant's store

To work on a merchant's theme, you should request access to their store. Working on a theme in a merchant's store lets you test it with the merchant's products and other resources.

If you haven't done so already, you should request [a collaborator account](/docs/storefronts/themes/tools/collaborator-accounts) with the **Manage themes** permission for the store. Collaborator accounts give you access to only the sections of a store that a merchant wants you to access, and don't count toward a store's [staff limit](https://help.shopify.com/manual/your-account/staff-accounts).

Note

You can also access themes using other accounts and credentials. [Learn more](/docs/storefronts/themes/tools/cli#authenticating-and-accessing-stores).

**Note:**

You can also access themes using other accounts and credentials. [Learn more](/docs/storefronts/themes/tools/cli#authenticating-and-accessing-stores).

---

## [Anchor to Step 2: Download the merchant's theme code](/docs/storefronts/themes/getting-started/customize#step-2-download-the-merchants-theme-code)Step 2: Download the merchant's theme code

If the merchant doesn't have a [GitHub repository for their theme](/docs/storefronts/themes/tools/github), then you need to download a copy of the theme code to work on it locally.

1. Run the following command to retrieve a list of all of the themes in the store. You can optionally specify the local path where the theme should be stored using the `--path` flag.

   $

   $

   shopify theme pull --store my-store
2. Select a theme from the list. Its contents are downloaded to the current folder or the specified folder.

   Tip

   If you haven't done so already, you're prompted to log in to Shopify when you run the `pull` command. Make sure that you log in using the account that was granted access to the store. If you're already logged in with an account that doesn't have appropriate access, then you can log out using `shopify auth logout`.

   **Tip:**

   If you haven't done so already, you're prompted to log in to Shopify when you run the `pull` command. Make sure that you log in using the account that was granted access to the store. If you're already logged in with an account that doesn't have appropriate access, then you can log out using `shopify auth logout`.

---

## [Anchor to Step 3: Make a customization](/docs/storefronts/themes/getting-started/customize#step-3-make-a-customization)Step 3: Make a customization

After you've downloaded the merchant's theme, you can make any necessary changes to the theme code. For example, you can add support for multiple currencies and languages in the merchant's theme using our [localization](/docs/storefronts/themes/markets/multiple-currencies-languages) tutorial, or you can make an adjustment to the theme's CSS to change its appearance.

Refer to [Next steps](#next-steps) to explore additional feature tutorials.

---

## [Anchor to Step 4: Preview your changes](/docs/storefronts/themes/getting-started/customize#step-4-preview-your-changes)Step 4: Preview your changes

After you make a change to the theme, you can run [`shopify theme dev`](/docs/api/shopify-cli/theme/theme-dev) to interact with the theme in a browser. Shopify CLI uploads the theme as a [development theme](/docs/storefronts/themes/tools/cli#development-themes) on the store that you're connected to.

The command returns a URL that hot reloads local changes to CSS and sections, allowing you to preview changes in real time using the store's data. This preview is only available in Google Chrome.

1. In a terminal, navigate to your working directory.
2. Serve your theme by using the following command:

   $

   $

   shopify theme dev
3. In Google Chrome, navigate to `http://127.0.0.1:9292` to open the theme preview.

You can also use the `dev` command to generate a [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others) and a link to the [theme editor](/docs/storefronts/themes/tools/online-editor) for the development theme.

The development theme is destroyed when you run `shopify auth logout`. If you need to share your progress with the merchant, then proceed to the next step.

---

## [Anchor to Step 5: Share your changes](/docs/storefronts/themes/getting-started/customize#step-5-share-your-changes)Step 5: Share your changes

To share your changes with the merchant, you need to upload your changes to the theme to the merchant's store. You're prompted to select the theme that you want to update. This command returns a link to the [editor](/docs/storefronts/themes/tools/online-editor) for the theme in the Shopify admin and a [preview link](https://help.shopify.com/manual/online-store/themes/adding-themes#share-a-theme-preview-with-others), both of which you can share with the merchant.

$

$

shopify theme push

Tip

If you don't want to update an existing theme in the store with your changes, then you can upload your theme to the theme library as a new, unpublished theme using the [`--unpublished`](/docs/api/shopify-cli/theme/theme-push-flags) flag.

**Tip:**

If you don't want to update an existing theme in the store with your changes, then you can upload your theme to the theme library as a new, unpublished theme using the [`--unpublished`](/docs/api/shopify-cli/theme/theme-push-flags) flag.

---

## [Anchor to Step 6: Publish the updated theme](/docs/storefronts/themes/getting-started/customize#step-6-publish-the-updated-theme)Step 6: Publish the updated theme

After the merchant approves the changes, you can publish the theme to make it live in the merchant's store. If you haven't yet pushed your changes to the store, then you need to do so before you publish the theme.

1. Enter the following command:

   $

   $

   shopify theme publish
2. Select the theme that you want to publish from the list.
3. Select `Yes` to confirm that you want to publish the specified theme.

The theme is published and is now the active theme for the store.

---

## [Anchor to Next steps](/docs/storefronts/themes/getting-started/customize#next-steps)Next steps

A theme determines the way that a Shopify [online store](https://help.shopify.com/manual/online-store) looks, feels, and functions for merchants and their customers.

Shopify themes are built using Shopify's theme templating language, [Liquid](/docs/api/liquid), along with HTML, CSS, JavaScript, and JSON. Using these languages, developers can create any look and feel that their clients want. Shopify provides several tools and best practices to accelerate the development process.

As a developer, you can build a custom theme for a specific merchant, customize a theme to meet a merchant's needs, or build a theme to sell in the Shopify Theme Store. You can also build apps that extend the functionality of a theme.

[![](/images/icons/48/blocks.png)![](/images/icons/48/blocks-dark.png)

Learn about theme architecture

Learn more about the structure of a theme, and the role of each file and folder.

Learn about theme architecture

Learn more about the structure of a theme, and the role of each file and folder.](/docs/storefronts/themes/architecture)

[Learn about theme architecture  
  

Learn more about the structure of a theme, and the role of each file and folder.](/docs/storefronts/themes/architecture)

[![](/images/icons/48/star.png)![](/images/icons/48/star-dark.png)

Review best practices

Build your theme with a set of principles to use themes to their full potential, and to create great ecommerce experiences.

Review best practices

Build your theme with a set of principles to use themes to their full potential, and to create great ecommerce experiences.](/docs/storefronts/themes/best-practices)

[Review best practices  
  

Build your theme with a set of principles to use themes to their full potential, and to create great ecommerce experiences.](/docs/storefronts/themes/best-practices)

[![](/images/icons/48/pickaxe-1.png)![](/images/icons/48/pickaxe-1-dark.png)

Build as a team

Take advantage of our developer tools to build effectively as a team.

Build as a team

Take advantage of our developer tools to build effectively as a team.](/docs/storefronts/themes/tools)

[Build as a team  
  

Take advantage of our developer tools to build effectively as a team.](/docs/storefronts/themes/tools)

[![](/images/icons/48/themes.png)![](/images/icons/48/themes-dark.png)

Implement Shopify features

Enable Shopify features or add functionality to your theme.

Implement Shopify features

Enable Shopify features or add functionality to your theme.](/docs/storefronts/themes/theme-features)

[Implement Shopify features  
  

Enable Shopify features or add functionality to your theme.](/docs/storefronts/themes/theme-features)

---

Was this page helpful?

YesNo