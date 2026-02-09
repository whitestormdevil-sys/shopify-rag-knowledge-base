---
source: https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens
---

Tip

You can use Shopify CLI to [generate a starter app](/docs/apps/build/scaffold-app) with boilerplate code that handles authorization. This is the recommended method.

**Tip:**

You can use Shopify CLI to [generate a starter app](/docs/apps/build/scaffold-app) with boilerplate code that handles authorization. This is the recommended method.

The Shopify platform provides two ways for apps to acquire an access token: token exchange and authorization code grant. Embedded apps should use token exchange, while non-embedded apps need to use authorization code grant.

---

## [Anchor to Token exchange](/docs/apps/build/authentication-authorization/access-tokens#token-exchange)Token exchange

[OAuth 2.0 token exchange](https://datatracker.ietf.org/doc/html/rfc8693) allows apps to exchange a [session token](/docs/apps/build/authentication-authorization/session-tokens) for an access token. The session token is only available for embedded apps and can be acquired using App Bridge.

[Generating a starter app](/docs/apps/build/scaffold-app) handles authentication automatically. However, refer to [this guide](/docs/apps/build/authentication-authorization/access-tokens/token-exchange) for more details or if you need to implement token exchange yourself.

### [Anchor to Request flow using token exchange API](/docs/apps/build/authentication-authorization/access-tokens#request-flow-using-token-exchange-api)Request flow using token exchange API

The following diagram illustrates the token exchange flow from the point at which a merchant interacts with the app to the point at which the app receives an access token and can [make authenticated API requests](/docs/apps/build/authentication-authorization/access-tokens/token-exchange#step-3-make-authenticated-requests).

![Request flow using token exchange API](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/auth/token-exchange-overview-HkSbDn_6.svg)


---

## [Anchor to Authorization code grant](/docs/apps/build/authentication-authorization/access-tokens#authorization-code-grant)Authorization code grant

For non-embedded apps, Shopify uses OAuth 2.0’s [authorization code grant flow](https://tools.ietf.org/html/rfc6749#section-4.1) to issue access tokens on behalf of merchants. The OAuth flow enables merchants to authorize apps to access store data. For example, a merchant might authorize an app to access order and product data.

The following diagram illustrates the authorization code grant flow based on the actions of the user, your app, and Shopify:

![Flowchart of the OAuth credential granting process](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/oauth-BVV3KNFj.png)

1. The user makes a request to install the app.
2. The app redirects to Shopify to load the grant screen and requests the user to authorize the required scopes. For apps that have requested API access scopes via [`TOML` file](/docs/apps/build/cli-for-apps/app-structure#root-configuration-files), the grant screen might display before the app redirects to Shopify.
3. The user authorizes the app by consenting to the requested scopes.
4. The app receives an authorization grant. This is a temporary credential representing the authorization.
5. The app requests an access token by authenticating with Shopify and presenting the authorization grant.
6. Shopify authenticates the app, validates the authorization grant, and then issues and returns an access token. The app can now request data from Shopify.
7. The app uses the access token to make requests to the Shopify API.
8. Shopify validates the access token and returns the requested data.

### [Anchor to Ways to implement authorization code grant](/docs/apps/build/authentication-authorization/access-tokens#ways-to-implement-authorization-code-grant)Ways to implement authorization code grant

Shopify provides multiple resources to help you to authorize your app with authorization code grant. The resource you use depends on whether you're creating a new app, and the app's language and structure.

* If you're creating a new app, then Shopify recommends using [Shopify CLI to create your app](/docs/apps/build/scaffold-app). This starter app uses [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange) and [session tokens](/docs/apps/build/authentication-authorization/session-tokens).
* If you're implementing authorization code grant for an existing app, an app that isn't embedded, or you don't want to use an app template, then we recommend using a [Shopify Admin API library](/docs/api#official-shopify-admin-api-libraries). These libraries provide methods for authenticating with authorization code grant (except React Router, which uses token exchange), and are used by Shopify app templates. Using a library makes your implementation faster and your app more secure. Refer to [Implement authorization code grant manually](/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) for more information.

---

Was this page helpful?

YesNo