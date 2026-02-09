---
source: https://shopify.dev/docs/apps/build/online-store/app-proxies
---

App proxies take requests to Shopify URLs, and proxy them to your app.
This allows you to fetch and display data on a storefront from an external source.

A Shopify app can have only one proxy route configured.
Any paths under this root URL will proxy to your app.

---

## [Anchor to How it works](/docs/apps/build/online-store/app-proxies#how-it-works)How it works

Shopify will proxy a storefront URL to your app based on your [app proxy configuration](/docs/apps/build/cli-for-apps/app-configuration#app_proxy):

9

1

2

3

4

[app\_proxy]

url = "/my-app-proxy"

prefix = "apps"

subpath = "my-custom-path"

In this example:

* `https://<shop_url>/apps/my-custom-path` will proxy to `https://<application_url>/my-app-proxy`.
* `https://<shop_url>/apps/my-custom-path/child-route` will proxy to `https://<application_url>/my-app-proxy/child-route`.

Configuring an app proxy requires the `write_app_proxy` [access scope](docs/api/usage/access-scopes#authenticated-access-scopes).

Note

You can also configure an app proxy in the Dev Dashboard by navigating to **Apps** > **{your app}** > **Versions** > **Create a version** > **App proxy**. However, Shopify recommends [file-based configuration](/docs/apps/build/cli-for-apps/app-configuration) which can be source controlled and deployed via Shopify CLI.

**Note:**

You can also configure an app proxy in the Dev Dashboard by navigating to **Apps** > **{your app}** > **Versions** > **Create a version** > **App proxy**. However, Shopify recommends [file-based configuration](/docs/apps/build/cli-for-apps/app-configuration) which can be source controlled and deployed via Shopify CLI.

---

## [Anchor to Getting started](/docs/apps/build/online-store/app-proxies#getting-started)Getting started

Use the following steps to create an app proxy using the Shopify React Router template.

### [Anchor to Requirements](/docs/apps/build/online-store/app-proxies#requirements)Requirements

* You're a [user with app development permissions](/docs/apps/build/dev-dashboard/user-permissions) and have created a [dev store](/docs/apps/build/dev-dashboard/development-stores).

* You're using the latest version of [Shopify CLI](/docs/api/shopify-cli).
* You're using the latest version of [Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/).

* You've [created an app that uses the React Router template](/docs/apps/build/scaffold-app).

### [Anchor to Step 1: Create the proxy route](/docs/apps/build/online-store/app-proxies#step-1-create-the-proxy-route)Step 1: Create the proxy route

1. If it's not already running, start the `shopify app dev` command.

   $

   $

   shopify app dev
2. Create a route in your app to [handle proxy requests](/docs/apps/build/online-store/display-dynamic-data#how-it-works) at `app/routes/my-app-proxy.jsx`:

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

   import { authenticate } from "../shopify.server";

   import { useLoaderData } from "react-router";

   export const loader = async ({ request }) => {

   // Use the authentication API from the React Router template

   await authenticate.public.appProxy(request);

   // Read URL parameters added by Shopify when proxying

   const url = new URL(request.url);

   return {

   shop: url.searchParams.get("shop"),

   loggedInCustomerId: url.searchParams.get("logged\_in\_customer\_id"),

   };

   };

   export default function MyAppProxy() {

   const { shop, loggedInCustomerId } = useLoaderData();

   return <div>{`Hello world from ${loggedInCustomerId || "not-logged-in"} on ${shop}`}</div>;

   }

### [Anchor to Step 2: Update configuration](/docs/apps/build/online-store/app-proxies#step-2-update-configuration)Step 2: Update configuration

1. In `shopify.app.toml` in the root of your app, add the `write_app_proxy` [access scope](/docs/apps/build/authentication-authorization/app-installation/manage-access-scopes).

   9

   1

   2

   [access\_scopes]

   scopes = "write\_app\_proxy"
2. In the same app configuration file, add your [app proxy configuration](#app-proxy-properties):

   9

   1

   2

   3

   4

   [app\_proxy]

   url = "/my-app-proxy"

   prefix = "apps"

   subpath = "my-custom-path"

### [Anchor to Step 3: Test the app proxy](/docs/apps/build/online-store/app-proxies#step-3-test-the-app-proxy)Step 3: Test the app proxy

1. The `shopify app dev` command will automatically update the app on your dev store.
2. Test the proxy by opening the proxied path on your storefront. In this example that's `https://<shop_url>/apps/my-custom-path`.

Note

Because [users can customize](#user-customization) the `prefix` and `subpath` values, they are immutable on a store after installation. Once you set these values in your `shopify.app.toml`, to change them during development you must use your dev store admin. You can also uninstall and reinstall the app to reinitialize the proxied path.

**Note:**

Because [users can customize](#user-customization) the `prefix` and `subpath` values, they are immutable on a store after installation. Once you set these values in your `shopify.app.toml`, to change them during development you must use your dev store admin. You can also uninstall and reinstall the app to reinitialize the proxied path.

---

## [Anchor to App proxy properties](/docs/apps/build/online-store/app-proxies#app-proxy-properties)App proxy properties

All properties are required.

| Property | Description |
| --- | --- |
| `url` | This can either be:  * A relative URL for your proxy endpoint. Shopify will prepend your app URL during `shopify app dev` and `shopify app deploy.` * An absolute URL for your proxy endpoint. If [enabled in your app config](/docs/apps/build/cli-for-apps/app-configuration#build), Shopify will update the host name with your app URL during `shopify app dev`. |
| `prefix` | The first part of the proxy URL on the shop. It must match an [allowed value](/docs/apps/build/cli-for-apps/app-configuration#app_proxy) (`a`, `apps`, `community`, or `tools`). |
| `subpath` | The second part of the proxy URL on the shop. It may contain letters, numbers, underscores, and hyphens up to 30 characters. The value may not be `admin`, `services`, `password`, or `login`. |

---

## [Anchor to User customization](/docs/apps/build/online-store/app-proxies#user-customization)User customization

Users can change the subpath or prefix of app proxies in Shopify Admin by navigating to **Settings** > **Apps and sales channels** > **{your app}** > **App proxy** > **Customize URL**.

While users can change this information to get a friendlier URL that fits their store's information architecture, these changes don't affect the root destination URL for your proxy endpoint.

Because these values are configurable by users, changes to the `subpath` and `prefix` in your app will only apply to new app installations.

---

## [Anchor to Liquid response](/docs/apps/build/online-store/app-proxies#liquid-response)Liquid response

App proxies support [Liquid](/docs/api/liquid), Shopify's template language. An app proxy response that contains Liquid will be rendered with store data into HTML like it was part of the store's theme.

If the HTTP response from the proxy URL has `Content-Type: application/liquid` set in its headers, then Shopify renders any Liquid code in the request body in the context of the shop using the shop's theme. Otherwise, the response is returned directly to the client. Also, any [30x redirects](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#3xx_Redirection) are followed.

---

## [Anchor to Disallowed headers](/docs/apps/build/online-store/app-proxies#disallowed-headers)Disallowed headers

Due to security concerns, the following headers are stripped from app proxy responses:

* `Accept-Patch`
* `Accept-Ranges`
* `Connection`
* `Cookie`
* `Date`
* `Delta-Base`
* `IM`
* `P3P`
* `Pragma`
* `Preference-Applied`
* `Proxy-Authenticate`
* `Public-Key-Pins`
* `Server`
* `Service-Worker-Allowed`
* `Set-Cookie`
* `Trailer`
* `Tk`
* `Warning`
* `X-Powered-By`

---

## [Anchor to Next steps](/docs/apps/build/online-store/app-proxies#next-steps)Next steps

* If you're not using the React Router template, then you can [build your own authentication for app proxies](/docs/apps/build/online-store/app-proxies/authenticate-app-proxies).
* Explore the [app configuration reference](/docs/apps/build/cli-for-apps/app-configuration#app_proxy) for app proxies.

---

Was this page helpful?

YesNo