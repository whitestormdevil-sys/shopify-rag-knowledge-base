---
source: https://shopify.dev/docs/api/usage/authentication
---

This guide introduces you to the authentication and authorization methods that you will use to connect to Shopify's APIs.

---

## [Anchor to Admin API access for Shopify apps](/docs/api/usage/authentication#admin-api-access-for-shopify-apps)Admin API access for Shopify apps

You can [use Shopify CLI to generate a starter app](/docs/apps/build/scaffold-app) with boilerplate code that handles authentication and authorization.
The starter app includes code for an embedded app that follows app best practices:

* Authorizing your app using [session tokens](/docs/apps/build/authentication-authorization/session-tokens) and [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange).
* Installing on stores using [Shopify managed installation](/docs/apps/build/authentication-authorization/app-installation).

  You should use this starter app unless you need to scaffold an app that is not embedded.

[![](/images/icons/48/globe.png)![](/images/icons/48/globe-dark.png)

Scaffold an app

Scaffold an app that follows all authentication and authorization best practices.

Scaffold an app

Scaffold an app that follows all authentication and authorization best practices.](/docs/apps/build/scaffold-app)

[Scaffold an app  
  

Scaffold an app that follows all authentication and authorization best practices.](/docs/apps/build/scaffold-app)

To learn more about the authentication and authorization methods that you can use for Shopify apps, and the libraries that you can use to simplify your implementation, refer to [authentication and authorization](/docs/apps/build/authentication-authorization).

---

## [Anchor to Access tokens for the Storefront API](/docs/api/usage/authentication#access-tokens-for-the-storefront-api)Access tokens for the Storefront API

The [Storefront API](/docs/api/storefront) supports both [tokenless](/docs/api/storefront#tokenless-access) and token-based access. For token-based access, requests require a valid Shopify access token. The following types of tokens are available:

* [**Public access tokens**](#getting-started-with-public-access): Used to make requests from client-side applications, such as a browser or mobile app.
* [**Private access tokens**](#getting-started-with-private-access): Used to make requests from a server or other private context.

  Apps can have a maximum of 100 active storefront access tokens per shop.

### [Anchor to Getting started with public access](/docs/api/usage/authentication#getting-started-with-public-access)Getting started with public access

Public access tokens enable your app to make Storefront API requests from public contexts like a browser. With public access, capacity scales with the number of buyers based on customer IP. In most cases, this is the IP of someone browsing your site or using your mobile app. Learn more about Storefront API [rate limits](/docs/api/usage/limits#rate-limits#storefront-api-rate-limits).

To use public access, you need to create a public access token for your app by making a request to the GraphQL Admin API's [`storefrontAccessTokenCreate`](/docs/api/admin-graphql/latest/mutations/storefrontAccessTokenCreate) mutation. Alternatively, you can create a [custom app in the Shopify admin](https://help.shopify.com/en/manual/apps/custom-apps), and retrieve your Storefront API access token and manage access scopes from there.

To query the Storefront API with a public access token, include it as an `X-Shopify-Storefront-Access-Token` header on all client-side requests.

### [Anchor to Getting started with private access](/docs/api/usage/authentication#getting-started-with-private-access)Getting started with private access

Private access tokens let you make authenticated, server-side queries to the Storefront API.

Caution

Unlike public access tokens, private access tokens should be treated as secret and not used on the client-side. We recommend only requesting the scopes that your app needs, to reduce the security risk if the token leaks.

**Caution:**

Unlike public access tokens, private access tokens should be treated as secret and not used on the client-side. We recommend only requesting the scopes that your app needs, to reduce the security risk if the token leaks.

To start using private access, you can use the following methods:

* Add the Headless channel to your Shopify admin.
* Create a [delegate access token](/docs/apps/build/authentication-authorization/access-tokens/use-delegate-tokens) for your custom app.
* Request [unauthenticated scopes](/docs/api/usage/access-scopes#unauthenticated-access-scopes) on an existing access token.

### [Anchor to Making server-side requests](/docs/api/usage/authentication#making-server-side-requests)Making server-side requests

To query the Storefront API with a private access token:

1. Include the `Shopify-Storefront-Private-Token` header with the private access token.

In some cases, a request to the Storefront API isn't linked to buyer traffic, such as during a static site build, however when making server-side requests to the Storefront API as a result of buyer traffic, be sure to also:

2. Include the `Shopify-Storefront-Buyer-IP` (case-sensitive) header with the IP address of the buyer. This allows Shopify to accurately enforce IP-level bot and platform protection, to help your storefront manage traffic from a single user consuming a high level of capacity, such as a bot.

   Caution

   Failure to include the `Shopify-Storefront-Buyer-IP` (case-sensitive) header, can result in sub-optimal user experiences, including throttled API requests, limited Bot Protection, and unauthenticated flows at checkout as Shopify will not be able to differentiate requests from different buyers.

   **Caution:**

   Failure to include the `Shopify-Storefront-Buyer-IP` (case-sensitive) header, can result in sub-optimal user experiences, including throttled API requests, limited Bot Protection, and unauthenticated flows at checkout as Shopify will not be able to differentiate requests from different buyers.

---

## [Anchor to Tools](/docs/api/usage/authentication#tools)Tools

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Shopify CLI

A command-line tool to help you build Shopify apps faster

Shopify CLI

A command-line tool to help you build Shopify apps faster](/docs/apps/build/cli-for-apps)

[Shopify CLI  
  

A command-line tool to help you build Shopify apps faster](/docs/apps/build/cli-for-apps)

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)

shopify\_api

Shopify’s official Ruby gem for interacting with the Admin API

shopify\_api

Shopify’s official Ruby gem for interacting with the Admin API](https://github.com/Shopify/shopify-api-ruby)

[shopify\_api  
  

Shopify’s official Ruby gem for interacting with the Admin API](https://github.com/Shopify/shopify-api-ruby)

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)

@shopify/shopify-api

Shopify’s official Node library for interacting with the Storefront and Admin APIs, handling OAuth, webhooks, and billing

@shopify/shopify-api

Shopify’s official Node library for interacting with the Storefront and Admin APIs, handling OAuth, webhooks, and billing](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

[@shopify/shopify-api  
  

Shopify’s official Node library for interacting with the Storefront and Admin APIs, handling OAuth, webhooks, and billing](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

[![](/images/icons/48/node_api.png)![](/images/icons/48/node_api-dark.png)

@shopify/admin-api-client

Shopify’s official lightweight Node library for interacting with the Admin API

@shopify/admin-api-client

Shopify’s official lightweight Node library for interacting with the Admin API](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/admin-api-client)

[@shopify/admin-api-client  
  

Shopify’s official lightweight Node library for interacting with the Admin API](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/admin-api-client)

---

## [Anchor to Next steps](/docs/api/usage/authentication#next-steps)Next steps

* Authenticate your embedded app using [session tokens](/docs/apps/build/authentication-authorization/session-tokens).
* Authorize your embedded app using a session token with [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange).
* Authorize your app that is not embedded with [authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant).
* Authenticate your app created in the Shopify admin with [access tokens](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin).

---

Was this page helpful?

YesNo