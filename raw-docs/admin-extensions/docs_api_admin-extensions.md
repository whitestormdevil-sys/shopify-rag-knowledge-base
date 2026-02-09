---
source: https://shopify.dev/docs/api/admin-extensions
---

# Admin UI extensions

Admin UI extensions make it possible to surface contextual app functionality within the Shopify Admin interface.

Ask assistant

Choose a version:

2026-01 latest2025-10 2025-07 2025-04 2025-01 2024-10 2024-07 2024-04 2024-01 2023-10 

2026-01latest

## [Anchor to Getting started](/docs/api/admin-extensions/latest#getting-started)Getting started

Use the [Shopify CLI](/docs/api/shopify-cli) to [generate a new extension](/apps/tools/cli/commands#generate-extension) within your app.

If you already have a Shopify app, you can skip right to the last command shown here.

Make sure you're using Shopify CLI `v3.85.3` or higher. You can check your version by running `shopify version`.

![Admin extension example](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/admin-extensions/2023-10/action-extension-example-D3UyRVWo.gif)

---

## [Anchor to Optional ESLint configuration](/docs/api/admin-extensions/latest#optional-eslint-configuration)Optional ESLint configuration

If your app is using ESLint, update your configuration to include the new global `shopify` object.

---

## [Anchor to Scaffolded with Preact](/docs/api/admin-extensions/latest#scaffolded-with-preact)Scaffolded with Preact

UI Extensions are scaffolded with [Preact](https://preactjs.com/) by default.

This means that you can use Preact patterns and principles within your extension. Since Preact is included as a standard dependency, you have access to all of its features including [hooks](https://preactjs.com/guide/v10/hooks/) like `useState` and `useEffect` for managing component state and side effects.

You can also use [Preact Signals](https://preactjs.com/guide/v10/signals) for reactive state management, and take advantage of standard web APIs just like you would in a regular Preact application.

---

## [Anchor to Handling events](/docs/api/admin-extensions/latest#handling-events)Handling events

Handling events in UI extensions are the same as you would handle them in a web app. You can use the `addEventListener` method to listen for events on the components or use the `on[event]` property to listen for events from the components.

When using Preact, event handlers can be registered by passing props beginning with `on`, and the event handler name is case-insensitive. For example, the JSX `<s-button onClick={fn}>` registers `fn` as a "click" event listener on the button.

---

## [Anchor to Using forms](/docs/api/admin-extensions/latest#using-forms)Using forms

When building a Block extension you may use the [Form component](/docs/api/admin-extensions/latest/components/forms/form) to integrate with the contextual save bar of the resource page. The Form component provides a way to manage form state and submit data to your app's backend or directly to Shopify using Direct API access.

Whenever an input field is changed, the Form component will automatically update the dirty state of the resource page. When the form is submitted or reset the relevant callback in the form component will get triggered.

Using this, you can control what defines a component to be dirty by utilizing the Input's defaultValue property.

Rules:

* When the defaultValue is set, the component will be considered dirty if the value of the input is different from the defaultValue.You may update the defaultValue when the form is submitted to reset the dirty state of the form.
* When the defaultValue is not set, the component will be considered dirty if the value of the input is different from the initial value or from the last dynamic update to the input's value that wasn't triggered by user input.

  Note: In order to trigger the dirty state, each input must have a name attribute.

---

## [Anchor to Picking resources](/docs/api/admin-extensions/latest#picking-resources)Picking resources

Use the Resource Picker and Picker API's to allow users to select resources for your extension to use.

Resource Picker

Use the `resourcePicker` API to display a search-based interface to help users find and select one or more products, collections, or product variants, and then return the selected resources to your extension. Both the app and the user must have the necessary permissions to access the resources selected.

Picker

Use the `picker` API to display a search-based interface to help users find and select one or more custom data types that you provide, such as product reviews, email templates, or subscription options.

---

## [Anchor to Deploying](/docs/api/admin-extensions/latest#deploying)Deploying

Use the Shopify CLI to [deploy your app and its extensions](/docs/apps/deployment/extension).

---

## [Anchor to Tutorials and resources](/docs/api/admin-extensions/latest#tutorials-and-resources)Tutorials and resources

Deepen your understanding of Admin UI extensions with these tutorials and resources.

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

TutorialGet started building your first admin extension

Tutorial

Get started building your first admin extension](/docs/apps/admin/admin-actions-and-blocks/build-an-admin-action)

[Tutorial - Get started building your first admin extension](/docs/apps/admin/admin-actions-and-blocks/build-an-admin-action)

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

Component APIsSee all available components

Component APIs

See all available components](/docs/api/admin-extensions/components)

[Component APIs - See all available components](/docs/api/admin-extensions/components)

[![](/images/icons/32/app.png)![](/images/icons/32/app-dark.png)

ReferenceView a list of available extension targets

Reference

View a list of available extension targets](/docs/api/admin-extensions/2026-01/extension-targets)

[Reference - View a list of available extension targets](/docs/api/admin-extensions/2026-01/extension-targets)

[![](/images/icons/32/globe.png)![](/images/icons/32/globe-dark.png)

Network featuresLearn about the network features available to admin extensions

Network features

Learn about the network features available to admin extensions](/docs/api/admin-extensions/2026-01/network-features)

[Network features - Learn about the network features available to admin extensions](/docs/api/admin-extensions/2026-01/network-features)

[![](/images/icons/32/pickaxe-1.png)![](/images/icons/32/pickaxe-1-dark.png)

Using formsUse the Form component to integrate with the contextual save bar of the resource page

Using forms

Use the Form component to integrate with the contextual save bar of the resource page](/docs/api/admin-extensions/#using-forms)

[Using forms - Use the Form component to integrate with the contextual save bar of the resource page](#using-forms)

[![](/images/icons/32/pickaxe-1.png)![](/images/icons/32/pickaxe-1-dark.png)

Picking resourcesPrompt the user to select resources

Picking resources

Prompt the user to select resources](/docs/api/admin-extensions/#picking-resources)

[Picking resources - Prompt the user to select resources](#picking-resources)

[![](/images/icons/32/pickaxe-1.png)![](/images/icons/32/pickaxe-1-dark.png)

Figma kitUse the Figma kit to design your extension

Figma kit

Use the Figma kit to design your extension](https://www.figma.com/community/file/1554895871000783188/polaris-ui-kit-community)

[Figma kit - Use the Figma kit to design your extension](https://www.figma.com/community/file/1554895871000783188/polaris-ui-kit-community)

---

Was this page helpful?

YesNo