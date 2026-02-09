---
source: https://shopify.dev/docs/apps/marketing/pixels/getting-started
---

Pixels are JavaScript code snippets that run on the online store and collect [behavioral data](/docs/api/web-pixels-api/standard-events) for marketing campaign optimization and analytics. You can create a web pixel extension to subscribe your app to events that are emitted by Shopify.

---

## [Anchor to What you'll learn](/docs/apps/build/marketing-analytics/build-web-pixels#what-youll-learn)What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Create a web pixel extension.
* Configure your web pixel extension to subscribe to all events emitted by Shopify.
* Activate and test your web pixel extension.
* Deploy your web pixel extension to Shopify.

---

## [Anchor to Requirements](/docs/apps/build/marketing-analytics/build-web-pixels#requirements)Requirements

* You're a [user with app development permissions](/docs/apps/build/dev-dashboard/user-permissions) and have created [a dev store](/docs/apps/build/dev-dashboard/development-stores).
* You've [created an app](/docs/apps/build/scaffold-app) using Shopify CLI. If you previously installed Shopify CLI, then make sure you're using the [latest version](/docs/api/shopify-cli#upgrade).
* Your app can make [authenticated requests](/docs/api/admin-graphql#authentication) to the GraphQL Admin API.
* Your app has the `write_pixels` and `read_customer_events` [access scopes](/docs/api/usage/access-scopes). Learn how to [configure your access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration).

---

## [Anchor to Step 1: Create a web pixel extension](/docs/apps/build/marketing-analytics/build-web-pixels#step-1-create-a-web-pixel-extension)Step 1: Create a web pixel extension

To create a web pixel extension, you can use Shopify CLI to [generate](/docs/api/shopify-cli/app/app-generate-extension) a starter extension.

1. Navigate to your app directory:

   $

   $

   cd <directory>
2. Run the following command to create a new web pixel extension:

   $

   $

   shopify app generate extension --template web\_pixel --name my-web-pixel
3. Choose the language that you want to use:

   $

   $

   $

   $

   $

   ? What would you like to work in?

   > (1) JavaScript

   (2) TypeScript

   After the generation process has completed, a new folder is created in your app directory named `extensions`. This folder contains all of the code for your web pixel extension.

---

## [Anchor to Step 2: Define your web pixel settings](/docs/apps/build/marketing-analytics/build-web-pixels#step-2-define-your-web-pixel-settings)Step 2: Define your web pixel settings

Your web pixel needs to be configured for each store so it can properly track and associate data. The settings for your web pixel can be found at `extensions/<your_extension_name>/shopify.extension.toml`.

Inside of `shopify.extension.toml`, you can define fields that can be used by your web pixel.

In addition, configure privacy settings to integrate your pixel with [cookie banner and data sale opt out](https://help.shopify.com/manual/privacy-and-security/privacy/customer-privacy-settings) features used to help comply with privacy regulations.

To integrate with the cookie banner, use the [latest version of Shopify CLI](/docs/api/shopify-cli#upgrade) and configure the purposes required to run your pixel:

1. `analytics`: Your pixel is used to collect information about how customers interact with the site.
2. `marketing`: Your pixel is used to provide ads and marketing communications based on customer interests.
3. `preferences`: Your pixel is used to persist customer preferences and personalize the customer experience.

To configure a pixel to run without requiring consent (strictly necessary / essential), set the above purposes to `false`.

To integrate with the data sale opt out feature, configure sale of data:

4. `sale_of_data`: Your pixel is used for data sale / sharing.

The following example shows the `shopify.extension.toml` file with a description of each property, as well as a privacy settings configuration that indicates the pixel required `analytics`, `marketing` and `sale_of_data` permissions to run:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

type = "web\_pixel\_extension"

name = "my-web-pixel"

uid = "5dd0f111-62d8-91e2-8f50-8436afb95d0bfe12168a"

runtime\_context = "strict"

[customer\_privacy]

analytics = true

marketing = true

preferences = false

sale\_of\_data = "enabled"

[settings]

type = "object"

# [settings.fields.name]

# name = "name"

# description = "description"

# type = "single\_line\_text\_field"

# validations = [{...}]

# [settings.fields.name]

# name = "name"

# description = "description"

# type = "single\_line\_text\_field"

# validations = [{...}]

| Property | Description |
| --- | --- |
| `type` required | The type of extension. For web pixel extensions, this value is always `web_pixel_extension`. |
| `name` required | The name of the web pixel app extension. |
| `uid` required | The user identifier for the web pixel app extension. See [common extension properties](/docs/apps/build/app-extensions/configure-app-extensions#common-properties) for more information. |
| `runtime_context` required | The context that the web pixel extension is running in. This value must be set to `strict`. |
| `customer_privacy` | Configure privacy settings definition. If not provided, then it defaults to `marketing: true`, `analytics: true`, and `sale_of_data: "enabled"`. All four privacy purposes need to be explicitly declared if you want to override the default. |
| `customer_privacy.analytics` required | A `true` or `false` declaration that your pixel requires `analytics` permissions to run. |
| `customer_privacy.marketing` required | A `true` or `false` declaration that your pixel requires `marketing` permissions to run. |
| `customer_privacy.preferences` required | A `true` or `false` declaration that your pixel requires `preferences` permissions to run. |
| `customer_privacy.sale_of_data` required | A string `enum` declaration that your pixel requires `sale_of_data` permissions to run.    - `enabled`: Pixel qualifies as data sale and won't fire if customers opt out of data sale/sharing    - `disabled`: Pixel doesn't qualify as data sale/sharing and will fire when customers opt out of data sale/sharing    - `ldu`: Pixel qualifies as data sale / sharing, but implements a limited data use setting so that it will fire when customers opt out of data sale / sharing. |
| `settings` required | Denotes the data type of the settings definition. A `type` property with the value `object` must be provided for this section. |
| `settings.fields` required | Denotes the acceptable [metafields](/docs/apps/build/custom-data/metafields/definitions) for your settings definition. Requires a `name` and `type` field. An optional `description` and `validations` field can also be provided. |

By default, your `shopify.extension.toml` file is generated with a field named `accountID` and privacy settings configuration of `analytics`, `marketing` and `sale_of_data`, as shown in the following example:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

type = "web\_pixel\_extension"

name = "my-web-pixel"

uid = "5dd0f111-62d8-91e2-8f50-8436afb95d0bfe12168a"

runtime\_context = "strict"

[customer\_privacy]

analytics = true

marketing = true

preferences = false

sale\_of\_data = "enabled"

[settings]

type = "object"

[settings.fields.accountID]

name = "Account ID"

description = "Account ID"

type = "single\_line\_text\_field"

validations = [

{ name = "min", value = "1" }

]

Each of the fields that you define within your `settings` has a name, description, and type. The only type that is supported for web pixel is `single_line_text_field`. Validations can be provided as an optional parameter and can be used to define any constraints on a field's value. In the above example, there is a single validation to ensure that the value provided is at minimum length of 1. Further information on validation options can be found on the [metafields validation page](/docs/apps/build/custom-data/metafields/list-of-validation-options).

With the settings defined, you can now set up subscriptions to events that are emitted.

---

## [Anchor to Step 3: Subscribe to events](/docs/apps/build/marketing-analytics/build-web-pixels#step-3-subscribe-to-events)Step 3: Subscribe to events

Event subscription allows your app to listen for events that are emitted by Shopify and other developers. You can define a specific event to subscribe to or you can subscribe to all events using `analytics.subscribe`.

You can add an event subscription to your app using the `extensions/<your_extension_name>/src/index.js` file. When you run the [`generate extension` command](/docs/api/shopify-cli/app/app-generate-extension) to create the extension, a set of basic sample code is created in this file.

You can add code to enable subscription to any target events. For example, you can add the following code that subscribes to all events:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

import {register} from '@shopify/web-pixels-extension';

register(async ({analytics, browser, settings}) => {

// Retrieve or set your tracking cookies

const uid = await browser.cookie.get('your\_visitor\_cookie');

const pixelEndpoint = `https://example.com/pixel?id=${settings.accountID}&uid=${uid}`;

// Subscribe to events

analytics.subscribe('all\_events', (event) => {

// Transform the event payload to fit your schema (optional)

// Send events to third-party servers

fetch('https://example.com/pixel', {

method: 'POST',

body: JSON.stringify(payload),

keepalive: true,

});

});

});

With this code added, the web pixel is now set to listen to all events that are emitted. Refer to the [Web pixel extension API](/docs/api/web-pixels-api) for additional APIs to support other functions or to subscribe to individual events.

---

## [Anchor to Step 4: Update your app access scopes](/docs/apps/build/marketing-analytics/build-web-pixels#step-4-update-your-app-access-scopes)Step 4: Update your app access scopes

Before you can [activate a web pixel extension](#step-5-activate-a-web-pixel-extension), you must request the following [access scopes](/docs/api/usage/access-scopes) to invoke web pixel mutations in the GraphQL Admin API:

* `write_pixels`: Used to write the web pixel merchant settings
* `read_customer_events`: Used to gain access to customer events

1. In `shopify.app.toml` in the root of your app, add the `write_pixels` and `read_customer_events` access scopes:

   9

   1

   2

   3

   [access\_scopes]

   # Learn more at https://shopify.dev/docs/apps/structure/configuration#access\_scopes

   scopes = "write\_pixels,read\_customer\_events"
2. Save your configuration file. If [`app dev`](/docs/api/shopify-cli/app/app-dev) is running, the scope changes will be applied automatically. If not, start the command to connect the extension to a dev store:

   $

   $

   shopify app dev

   Note

   Connecting the extension to the store is the first step in testing your web pixel extension. However, the web pixel isn't created and configured in the dev store, and isn't subscribed to customer events, until you [run a mutation to create the web pixel](#step-5-activate-a-web-pixel-extension).

   **Note:**

   Connecting the extension to the store is the first step in testing your web pixel extension. However, the web pixel isn't created and configured in the dev store, and isn't subscribed to customer events, until you [run a mutation to create the web pixel](#step-5-activate-a-web-pixel-extension).
3. In your dev store, go to **Settings** > **Customer events**.

   The name of your app appears in the **App pixels** list with the **Disconnected** status. You'll connect your app and activate the web pixel extension in the [next step](#step-5-activate-a-web-pixel-extension).

---

## [Anchor to Step 5: Activate a web pixel extension](/docs/apps/build/marketing-analytics/build-web-pixels#step-5-activate-a-web-pixel-extension)Step 5: Activate a web pixel extension

To activate a web pixel extension, you must create a web pixel record on the store where you installed your app. You can do this using the [`webPixelCreate`](/docs/api/admin-graphql/latest/mutations/webPixelCreate) mutation. When this mutation is called, Shopify validates against the settings definition that you defined in `shopify.extension.toml`. If the settings input field doesn't match the schema that you defined, then the mutation will fail.

Note

The simplest way to execute GraphQL queries if you're developing an app is to use the [local GraphiQL instance that the CLI provides](/docs/api/usage/api-exploration/admin-graphiql-explorer#use-a-local-graphiql-instance).

**Note:**

The simplest way to execute GraphQL queries if you're developing an app is to use the [local GraphiQL instance that the CLI provides](/docs/api/usage/api-exploration/admin-graphiql-explorer#use-a-local-graphiql-instance).

1. Execute the following mutation from within your app:

   99

   1

   2

   3

   4

   5

   6

   7

   8

   9

   10

   11

   12

   13

   14

   mutation {

   # This mutation creates a web pixel, and sets the `accountID` declared in `shopify.extension.toml` to the value `123`.

   webPixelCreate(webPixel: { settings: "{\"accountID\":\"123\"}" }) {

   userErrors {

   code

   field

   message

   }

   webPixel {

   settings

   id

   }

   }

   }

   99

   1

   2

   3

   4

   5

   6

   7

   8

   9

   10

   11

   12

   13

   14

   15

   16

   17

   18

   19

   20

   21

   22

   {

   "data": {

   "webPixelCreate": {

   "userErrors": [],

   "webPixel": {

   "settings": "{\"accountID\":\"123\"}",

   "id": "gid://shopify/WebPixel/1"

   }

   }

   },

   "extensions": {

   "cost": {

   "requestedQueryCost": 10,

   "actualQueryCost": 10,

   "throttleStatus": {

   "maximumAvailable": 1000,

   "currentlyAvailable": 990,

   "restoreRate": 50

   }

   }

   }

   }
2. In your dev store, go to **Settings** > **Customer events**.

   The name of your app should appear in the **App pixels** list with the **Connected** status.

---

## [Anchor to Step 6: Test the web pixel settings](/docs/apps/build/marketing-analytics/build-web-pixels#step-6-test-the-web-pixel-settings)Step 6: Test the web pixel settings

You can test that the web pixel is configured and subscribed to all events emitted on the dev store by completing the following steps:

1. With the server running, open your dev store.
2. Right-click anywhere on the page and select **Inspect**.
3. Click **Console**.

   The `accountID` is logged in the console:

   ![The console showing AccountID being logged](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/pixels/accountID-logged-CGprR5nP.png)

---

## [Anchor to Step 7: Deploy your extension](/docs/apps/build/marketing-analytics/build-web-pixels#step-7-deploy-your-extension)Step 7: Deploy your extension

When you're ready to release your changes to users, you can create and release an [app version](/docs/apps/launch/deployment/app-versions). An app version is a snapshot of your app configuration and all extensions.

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

## [Anchor to Next steps](/docs/apps/build/marketing-analytics/build-web-pixels#next-steps)Next steps

* Consult the [customer events reference](/docs/api/web-pixels-api/standard-events) to learn about the ways of tracking and sending events with web pixels.
* Explore the [web pixel extension API](/docs/api/web-pixels-api) to learn about the sandboxing modes for web pixels, and the API references that are available for the sandbox.

---

Was this page helpful?

YesNo