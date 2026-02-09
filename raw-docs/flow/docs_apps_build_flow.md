---
source: https://shopify.dev/docs/apps/build/flow
---

[Shopify Flow](https://apps.shopify.com/flow) is an app that allows merchants to customize their store through automation. As a developer, you can integrate your app with the Flow platform through custom tasks, such as triggers and actions.

![A workflow for a low stock notification displaying a trigger, condition, and action](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/flow/example-workflow-inventory-quantity-changed-9tECTTxk.png)

This guide introduces you to the different extensions you can create, building a Flow trigger and action, and considerations when making changes to your extensions.

---

## [Anchor to Why build for Flow](/docs/apps/build/flow#why-build-for-flow)Why build for Flow

Building for Flow can help you to increase the value of your app by allowing merchants to automate their business processes. For example, suppose that you have a review app. After a review is created, merchants might want to send a notification (using email, Slack, or SMS), award loyalty points, and more. If you build the `Review created` trigger, Flow allows merchants to do any of those actions with your app. By integrating with Flow, you can:

* **Improve integrations between your app, Shopify, and other apps**: Any task you build can be used with the triggers and actions that Flow already provides, which immediately connects your app to thousands of new features.
* **Save development time**: Rather than building and maintaining direct integrations with many other apps, you can integrate with Flow and provide similar value to your merchants.
* **Improved visibility**: Merchants can discover your templates or tasks in Flow, even if they don't have your app installed. Additionally, when you integrate with Flow, you receive a **Works with Flow** badge on your listing in the Shopify App Store. Your app will also be listed in the [Flow app directory](https://apps.shopify.com/collections/connectors-for-shopify-flow).

---

## [Anchor to What you can build](/docs/apps/build/flow#what-you-can-build)What you can build

As a Partner you can build one or more tasks related to your app for your merchants to use. These merchants need to have both your app and Shopify Flow installed. Shopify Flow includes the following task types:

| Extension type | Description | Example |
| --- | --- | --- |
| [Trigger](/docs/apps/build/flow/triggers) | An event that starts a workflow, and can be something that happens in a store or in an app. | A new order is created in a merchant's online store. |
| Condition | A rule that determines whether an action will be taken. As a developer you cannot create a condition task. | A condition is set to check whether the total amount paid for the order is over $200.00. |
| [Action](/docs/apps/build/flow/actions) | A task that's executed in a store or in an app when certain conditions are met. | If the total amount paid for the order is over $200.00, then a tag is added to the customer account that placed the order. |
| [Template](/docs/apps/build/flow/templates) | An example that demonstrates how your task works for a key use case. Templates are available through Flow's template library. | A workflow that sends an internal email when your trigger runs. |

---

## [Anchor to Plans supported](/docs/apps/build/flow#plans-supported)Plans supported

Flow is an optional app that's available to Shopify merchants on any paid plan. Flow is widely adopted by Shopify merchants, especially those with stores on Shopify Plus.

Flow features [differ by plan](https://help.shopify.com/en/manual/shopify-flow). For apps, the primary difference is that if you have a [custom app](https://help.shopify.com/en/manual/apps/app-types/custom-apps), your Flow app extensions are available only to a [Shopify Plus](https://www.shopify.com/plus) store that has your app installed.

---

## [Anchor to Templates](/docs/apps/build/flow#templates)Templates

A template in Shopify Flow is an example workflow that can be copied into a merchant's shop. Templates help merchants automate a specific use case with minimal or no additional configuration. Flow's template library offers hundreds of templates with features to filter, browse, and search. You can  [create a template](/docs/apps/build/flow/templates/create-a-template)  for Shopify Flow that showcases your custom triggers and actions and help merchants do more.

---

## [Anchor to Getting started](/docs/apps/build/flow#getting-started)Getting started

[![](/images/icons/48/key.png)![](/images/icons/48/key-dark.png)

Learn more about triggers

Connect your app to Shopify Flow so that your app can send an event that starts a workflow.

Learn more about triggers

Connect your app to Shopify Flow so that your app can send an event that starts a workflow.](/docs/apps/build/flow/triggers)

[Learn more about triggers  
  

Connect your app to Shopify Flow so that your app can send an event that starts a workflow.](/docs/apps/build/flow/triggers)

[![](/images/icons/48/star.png)![](/images/icons/48/star-dark.png)

Learn more about actions

Connect your app to Shopify Flow so that your app receives data when a workflow action runs.

Learn more about actions

Connect your app to Shopify Flow so that your app receives data when a workflow action runs.](/docs/apps/build/flow/actions)

[Learn more about actions  
  

Connect your app to Shopify Flow so that your app receives data when a workflow action runs.](/docs/apps/build/flow/actions)

[![](/images/icons/48/filesystem.png)![](/images/icons/48/filesystem-dark.png)

Learn more about Flow templates

Create workflow templates to showcase your triggers and actions.

Learn more about Flow templates

Create workflow templates to showcase your triggers and actions.](/docs/apps/build/flow/templates)

[Learn more about Flow templates  
  

Create workflow templates to showcase your triggers and actions.](/docs/apps/build/flow/templates)

[![](/images/icons/48/changelog.png)![](/images/icons/48/changelog-dark.png)

Lifecycle events

Get notified about events related to your Flow triggers and actions.

Lifecycle events

Get notified about events related to your Flow triggers and actions.](/docs/apps/build/flow/track-lifecycle-events)

[Lifecycle events  
  

Get notified about events related to your Flow triggers and actions.](/docs/apps/build/flow/track-lifecycle-events)

[![](/images/icons/48/clicode.png)![](/images/icons/48/clicode-dark.png)

Migrate legacy Flow extensions

Learn how to migrate your existing extensions from the Partner Dashboard to CLI-managed.

Migrate legacy Flow extensions

Learn how to migrate your existing extensions from the Partner Dashboard to CLI-managed.](/docs/apps/build/flow/migrate-legacy-extensions)

[Migrate legacy Flow extensions  
  

Learn how to migrate your existing extensions from the Partner Dashboard to CLI-managed.](/docs/apps/build/flow/migrate-legacy-extensions)

---

Was this page helpful?

YesNo