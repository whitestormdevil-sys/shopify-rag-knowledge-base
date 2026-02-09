---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/webhookSubscriptionCreate
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Creates a webhook subscription that notifies your [`App`](https://shopify.dev/docs/api/admin-graphql/latest/objects/App) when specific events occur in a shop. Webhooks push event data to your endpoint immediately when changes happen, eliminating the need for polling.

The subscription configuration supports multiple endpoint types including HTTPS URLs, Google Pub/Sub topics, and AWS EventBridge event sources. You can filter events using [Shopify API search syntax](https://shopify.dev/docs/api/usage/search-syntax) to receive only relevant webhooks, control which data fields are included in webhook payloads, and specify metafield namespaces to include.

---

Note

The Webhooks API version [configured in your app](https://shopify.dev/docs/apps/build/webhooks/subscribe/use-newer-api-version) determines the API version for webhook events. You can't specify it per subscription.

**Note:**

The Webhooks API version [configured in your app](https://shopify.dev/docs/apps/build/webhooks/subscribe/use-newer-api-version) determines the API version for webhook events. You can't specify it per subscription.

**Note:** The Webhooks API version <a href="https://shopify.dev/docs/apps/build/webhooks/subscribe/use-newer-api-version">configured in your app</a> determines the API version for webhook events. You can&#39;t specify it per subscription.

---

Building an app? If you only use app-specific webhooks, you won't need this. App-specific webhook subscriptions specified in your `shopify.app.toml` may be easier. They are automatically kept up to date by Shopify & require less maintenance. Please read [About managing webhook subscriptions](https://shopify.dev/docs/apps/build/webhooks/subscribe).

* topic (WebhookSubscriptionTopic!)
* webhookSubscription (WebhookSubscriptionInput!)

[Anchor to topic](/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#arguments-topic)topic •[WebhookSubscriptionTopic!](/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic) required
:   The type of event that triggers the webhook.

    Show enum values

[Anchor to webhookSubscription](/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#arguments-webhookSubscription)webhookSubscription •[WebhookSubscriptionInput!](/docs/api/admin-graphql/latest/input-objects/WebhookSubscriptionInput) required
:   Specifies the input fields for a webhook subscription.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to WebhookSubscriptionCreatePayload returns](/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#returns)WebhookSubscriptionCreatePayload returns

* userErrors ([UserError!]!)
* webhookSubscription (WebhookSubscription)

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#returns-userErrors)userErrors •[[UserError!]!](/docs/api/admin-graphql/latest/objects/UserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

[Anchor to webhookSubscription](/docs/api/admin-graphql/latest/mutations/webhookSubscriptionCreate#returns-webhookSubscription)webhookSubscription •[WebhookSubscription](/docs/api/admin-graphql/latest/objects/WebhookSubscription)
:   The webhook subscription that was created.

    Show fields

---

Was this section helpful?

YesNo