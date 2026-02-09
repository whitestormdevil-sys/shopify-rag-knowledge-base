---
source: https://shopify.dev/docs/apps/online-store/theme-app-extensions/getting-started
---

Theme app extensions allow merchants to easily add dynamic elements to their themes without having to interact with Liquid templates or code. You can start building theme app extensions with [Shopify CLI](/docs/apps/build/cli-for-apps).

---

## [Anchor to What you'll learn](/docs/apps/build/online-store/theme-app-extensions/build#what-youll-learn)What you'll learn

After you've finished this tutorial, you'll have accomplished the following tasks:

* Created a theme app extension
* Previewed the theme app extension
* Tested the theme app extension
* Added onboarding instructions in your app
* Deployed and released the theme app extension

---

## [Anchor to Requirements](/docs/apps/build/online-store/theme-app-extensions/build#requirements)Requirements

* You're a [user with app development permissions](/docs/apps/build/dev-dashboard/user-permissions) and have created [a dev store](/docs/apps/build/dev-dashboard/development-stores) that uses [generated test data](/docs/apps/build/dev-dashboard/development-stores/generated-test-data).
* You've [created an app that uses Shopify CLI 3.0 or higher](/docs/apps/build/scaffold-app).
* You've installed an Online Store 2.0 theme, such as [Horizon](https://themes.shopify.com/themes/horizon/presets/horizon), that uses [JSON templates](/docs/storefronts/themes/architecture/templates/json-templates) and supports [app blocks](/docs/storefronts/themes/architecture/blocks/app-blocks).
* You've installed the [additional project dependencies](/docs/apps/launch/deployment/deploy-in-ci-cd-pipeline#additional-project-dependencies) (Ruby and Bundler).
* You understand the [theme app extensions framework](/docs/apps/build/online-store/theme-app-extensions/configuration).

---

## [Anchor to Step 1: Create a new extension](/docs/apps/build/online-store/theme-app-extensions/build#step-1-create-a-new-extension)Step 1: Create a new extension

You'll use Shopify CLI to generate a new theme app extension.

1. Navigate to the directory of the app that you want to add your extension to.
2. Run the following command to start creating the extension:

   $

   $

   shopify app generate extension
3. Select `Theme app extension` as the extension type.
4. Provide a name for your extension.

You should now have a [new extension directory](/docs/apps/build/online-store/theme-app-extensions/configuration#file-structure) that includes a working example of a theme app extension that displays product ratings.

The generated extension requires a [metafield definition](https://help.shopify.com/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions#create-a-custom-definition) with the following properties:

* **Area:** Products
* **Namespace**: demo
* **Key**: avg\_rating
* **Type**: Integer

After you create the metafield definition, set a value for the metafield on at least one product in your dev store.

---

## [Anchor to Step 2: Preview your theme app extension](/docs/apps/build/online-store/theme-app-extensions/build#step-2-preview-your-theme-app-extension)Step 2: Preview your theme app extension

You can preview your extension by running the `dev` command, which starts a local development server that supports hot reloading. This preview is available only in Google Chrome.

1. Navigate to your app directory.
2. Run the following command:

   $

   $

   shopify app dev

You can specify which theme you want to use to host your theme app extension using the `--theme <ID or name>` flag. If you don't specify a theme, then the command will upload [Dawn](https://github.com/Shopify/dawn), Shopify's example theme, to the dev store.

When you run the `dev` command, Shopify CLI builds your app and bundles your app extensions. It also walks you through multiple configuration steps. If you've already run `dev` or `deploy` for this app, then some of these steps are skipped.

To learn about the processes that are executed when you run `dev`, refer to the [Shopify CLI command reference](/docs/api/shopify-cli/app/app-dev).

3. Follow the instructions in the CLI output to preview the theme app extension. This includes the following steps:

   * Opening the host theme in the theme editor
   * Adding your app block to the theme
   * Saving the theme
4. Click the URL that's printed at the bottom of the CLI output to preview your extension.

---

## [Anchor to Step 3: Test your changes](/docs/apps/build/online-store/theme-app-extensions/build#step-3-test-your-changes)Step 3: Test your changes

Verify that your app looks and behaves correctly by testing your changes on a theme in your dev store.

1. In your dev store, go to an Online Store 2.0 theme and navigate to the [theme editor](/docs/storefronts/themes/tools/online-editor).
2. Follow the procedures for:

   * [Adding app blocks](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/apps#app-blocks)
   * [Activating app embed blocks](https://help.shopify.com/manual/online-store/themes/theme-structure/extend/apps#app-embeds)
3. Verify the app behaves as expected. For example, verify the following:

   * App embed blocks for floating components are positioned properly without obscuring page content.
   * You can use the [theme editor](/docs/storefronts/themes/tools/online-editor) to activate and deactivate app embed blocks and configure their settings.
   * You can use the theme editor to add, remove, and reposition app blocks and configure their settings.
   * App documentation, such as app onboarding instructions, is clear, accurate, and complete. To learn more about writing effective help documentation, refer to [Help documentation](https://polaris.shopify.com/content/help-documentation) in Shopify Polaris.

---

## [Anchor to Step 4: Include onboarding instructions in your app](/docs/apps/build/online-store/theme-app-extensions/build#step-4-include-onboarding-instructions-in-your-app)Step 4: Include onboarding instructions in your app

Provide instructions for what merchants need to do after installing your app. For more information, refer to the [UX guidelines](/docs/apps/build/online-store/theme-app-extensions/ux#merchant-onboarding).

---

## [Anchor to Step 5: Deploy and release the extension](/docs/apps/build/online-store/theme-app-extensions/build#step-5-deploy-and-release-the-extension)Step 5: Deploy and release the extension

When you're ready to release your changes to users, you can create and release an [app version](/docs/apps/launch/deployment/app-versions). An app version is a snapshot of your app configuration and all extensions.

Tip

To verify that your theme app extension doesn't exceed any enforced limits before you deploy, you can run the Shopify CLI [`build`](/docs/api/shopify-cli/app/app-build) command. Running the `build` command runs [Theme Check](/docs/storefronts/themes/tools/theme-check/configuration) against your extension to ensure that it's valid. For more information, refer to the [enforced limits](/docs/apps/build/online-store/theme-app-extensions/configuration#file-and-content-size-limits) on theme app extensions.

**Tip:**

To verify that your theme app extension doesn't exceed any enforced limits before you deploy, you can run the Shopify CLI [`build`](/docs/api/shopify-cli/app/app-build) command. Running the `build` command runs [Theme Check](/docs/storefronts/themes/tools/theme-check/configuration) against your extension to ensure that it's valid. For more information, refer to the [enforced limits](/docs/apps/build/online-store/theme-app-extensions/configuration#file-and-content-size-limits) on theme app extensions.

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

---

Was this page helpful?

YesNo