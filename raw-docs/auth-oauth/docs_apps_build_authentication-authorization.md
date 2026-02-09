---
source: https://shopify.dev/docs/apps/build/authentication-authorization
---

This guide introduces the different methods of authenticating and authorizing apps with Shopify’s platform. Make sure that you understand the differences between the types of authentication and authorization methods before you begin your development process.

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

---

## [Anchor to Authentication vs. authorization](/docs/apps/build/authentication-authorization#authentication-vs-authorization)Authentication vs. authorization

Authentication is the process of verifying the identity of the user or the app. To keep transactions on Shopify’s platform [safe and secure](/docs/apps/build/compliance/privacy-law-compliance), all apps connecting with Shopify APIs must authenticate when making API requests.

Authorization is the process of giving permissions to apps. When an app user installs a Shopify app they authorize the app, enabling the app to acquire an access token. For example, an app might be authorized to access orders and product data in a store.

---

## [Anchor to Types of authentication and authorization methods](/docs/apps/build/authentication-authorization#types-of-authentication-and-authorization-methods)Types of authentication and authorization methods

The authentication and authorization methods that your app needs to use depends on the tool that you used to create your app, and the components that your app uses.

### [Anchor to Authentication](/docs/apps/build/authentication-authorization#authentication)Authentication

* Embedded apps need to authenticate their incoming requests with [session tokens](/docs/apps/build/authentication-authorization/session-tokens).
* Apps that are not embedded need to implement their own authentication method for incoming requests.

### [Anchor to Authorization](/docs/apps/build/authentication-authorization#authorization)Authorization

Authorization encompasses the installation of an app and the means to acquire an access token.

To avoid unnecessary redirects and page flickers during the app installation process, you should [configure your app's required access scopes using Shopify CLI](/docs/apps/build/cli-for-apps/app-configuration). This allows Shopify to [manage the installation process for you](/docs/apps/build/authentication-authorization/app-installation).

If you aren't able to use Shopify CLI to configure your app, then your app will install as part of the [authorization code grant flow](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant). This provides a degraded user experience.

If you're building an app for your own organization and don't require user interaction, you can use the [client credentials grant](/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant) to acquire access tokens.

The following table outlines the supported installation and token acquisition flows for various app configurations.

Whenever possible, you should create embedded apps that use Shopify managed installation and token exchange.

| Type of app | Supported installation flows | Supported token acquisition flows |
| --- | --- | --- |
| Embedded app | - [Shopify managed installation (recommended)](/docs/apps/build/authentication-authorization/app-installation) - [Installation during authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) | - [Token exchange (recommended)](/docs/apps/build/authentication-authorization/access-tokens/token-exchange) - [Authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) |
| Non-embedded app | - [Shopify managed installation (recommended)](/docs/apps/build/authentication-authorization/app-installation) - [Installation during authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) | - [Authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) |
| Admin-created custom app | - Installed upon generation in the Shopify admin | - [Generate in the Shopify admin](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) |

OAuth 2.0 is the industry-standard protocol for authorizing or giving permissions to apps. The following video illustrates how OAuth works at Shopify. Note that this video was created before [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange) was introduced, and might use the term "OAuth" interchangeably with "authorization code grant."



---

## [Anchor to Getting started](/docs/apps/build/authentication-authorization#getting-started)Getting started

* Authenticate your embedded app using [session tokens](/docs/apps/build/authentication-authorization/session-tokens).
* Authorize your embedded app using a session token with [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange).
* Authorize your app that is not embedded with [authorization code grant](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant).
* Authenticate your app created in the Shopify admin with [access tokens](/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin).

---

## [Anchor to Tools](/docs/apps/build/authentication-authorization#tools)Tools

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

Was this page helpful?

YesNo