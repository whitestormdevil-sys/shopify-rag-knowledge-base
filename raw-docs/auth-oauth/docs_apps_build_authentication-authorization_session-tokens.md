---
source: https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens
---

A session token is a mechanism that lets your embedded app authenticate the requests that it makes between the client side and your app's backend.

Note

All embedded apps need to use session tokens because third-party cookies won't work with browsers that restrict cross-domain data access.
If your embedded app still uses cookies and could pose a risk to users, then as part of our [app quality check process](/docs/apps/launch/app-store-review/app-quality-checks) you might be contacted and requested to migrate your app to use session tokens. This request will require immediate action.

**Note:**

All embedded apps need to use session tokens because third-party cookies won't work with browsers that restrict cross-domain data access.
If your embedded app still uses cookies and could pose a risk to users, then as part of our [app quality check process](/docs/apps/launch/app-store-review/app-quality-checks) you might be contacted and requested to migrate your app to use session tokens. This request will require immediate action.

The following video provides a short introduction to session tokens:



---

## [Anchor to How session tokens work](/docs/apps/build/authentication-authorization/session-tokens#how-session-tokens-work)How session tokens work

This section describes the authentication and request flows associated with session tokens, and the lifetime of a session token. It also provides information about implementing both OAuth and session token authentication for embedded apps.

### [Anchor to Authentication flow using a session token](/docs/apps/build/authentication-authorization/session-tokens#authentication-flow-using-a-session-token)Authentication flow using a session token

When your embedded app first loads, it's unauthenticated and serves up the frontend code for your app. Your app renders a user interface skeleton or loading screen to the user.

After the frontend code has loaded, your app calls a [Shopify App Bridge action](/docs/api/app-bridge/previous-versions/actions) to get the session token. Your app includes the session token in an authorization header when it makes any HTTPS requests to its backend.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/partners/jwt-auth-flow-DC23sv78.png)

### [Anchor to Request flow using a session token](/docs/apps/build/authentication-authorization/session-tokens#request-flow-using-a-session-token)Request flow using a session token

The session token is signed using the shared secret between your app and Shopify so that your backend can verify if the request is valid.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/auth/jwt-request-flow-DDQ5Q8bW.png)

### [Anchor to Lifetime of a session token](/docs/apps/build/authentication-authorization/session-tokens#lifetime-of-a-session-token)Lifetime of a session token

The lifetime of a session token is one minute. Session tokens must be fetched using Shopify App Bridge on each request to make sure that stale tokens aren't used.

### [Anchor to OAuth and session tokens](/docs/apps/build/authentication-authorization/session-tokens#oauth-and-session-tokens)OAuth and session tokens

Tip

You can use [Shopify CLI](/docs/apps/build/cli-for-apps) to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an embedded app that uses [session tokens](/docs/apps/build/authentication-authorization/session-tokens) and [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange).

**Tip:**

You can use [Shopify CLI](/docs/apps/build/cli-for-apps) to generate a starter app with boilerplate code that handles authentication and authorization. The starter app includes code for an embedded app that uses [session tokens](/docs/apps/build/authentication-authorization/session-tokens) and [token exchange](/docs/apps/build/authentication-authorization/access-tokens/token-exchange).

Session tokens are for authentication, and aren't a replacement for [authorization](/docs/apps/build/authentication-authorization#authorization). Learn more about the [difference between authentication and authorization](/docs/apps/build/authentication-authorization#authentication-vs-authorization).

Unlike API access tokens, session tokens can't be used to make authenticated requests to Shopify APIs. An API access token is what you use to send requests from your app's backend to Shopify so that you can fetch specific data from the user's shop.

For example, to [make authenticated requests](/docs/apps/build/authentication-authorization/access-tokens/token-exchange#step-3-make-authenticated-requests) to the [GraphQL Admin API](/docs/api/admin-graphql), your app must store the access token it receives during the OAuth flow. To contrast, session tokens are used by your app's backend to verify the embedded request coming from your app's frontend.

The following diagram shows the authentication process using session tokens and API access tokens:

![Diagram showing authentication process using sessions tokens and API access tokens](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/partners/auth-mechanisms-4HBrY0T6.png)


---

## [Anchor to Anatomy of a session token](/docs/apps/build/authentication-authorization/session-tokens#anatomy-of-a-session-token)Anatomy of a session token

Session tokens use the [JSON Web Token (JWT)](https://jwt.io) format and contain information about the merchant that's currently using your embedded app.

A session token consists of a header, payload, and signature. For an interactive example, refer to [JWT.io](https://jwt.io/), where you can experiment with setting different values for each section. Shopify recommends that you use your test app's credentials when testing on JWT.io.

For the most part, you shouldn't have to manage the anatomical details of session tokens. In most scenarios, you'll use a library, such as `authenticated_fetch` from [app-bridge](https://www.npmjs.com/package/@shopify/app-bridge), which generates and includes the session token in your requests. On the backend, you can use middleware similar to `validateAuthenticatedSession` in [@shopify/shopify-app-express](https://github.com/Shopify/shopify-app-js/blob/main/packages/apps/shopify-app-express/docs/reference/validateAuthenticatedSession.md).

After a Shopify session token is decoded, it has the following fields:

### [Anchor to Header](/docs/apps/build/authentication-authorization/session-tokens#header)Header

The values in the header are constant and never change.

9

1

2

3

4

{

"alg": "HS256",

"typ": "JWT"

}

* `alg`: The algorithm used to encode the JWT.
* `typ`: The [(type) header parameter](https://tools.ietf.org/html/rfc7519#section-5.1) used by session token to declare the media type.

### [Anchor to Payload](/docs/apps/build/authentication-authorization/session-tokens#payload)Payload

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

{

"iss": "<shop-name.myshopify.com/admin>",

"dest": "<shop-name.myshopify.com>",

"aud": "<client ID>",

"sub": "<user ID>",

"exp": "<time in seconds>",

"nbf": "<time in seconds>",

"iat": "<time in seconds>",

"jti": "<random UUID>",

"sid": "<session ID>"

"sig": "<signature>"

}

* `iss`: The shop's admin domain.
* `dest`: The shop's domain.
* `aud`: The client ID of the receiving app.
* `sub`: The [User](/docs/api/admin-rest/latest/resources/user) that the session token is intended for.
* `exp`: When the session token expires.
* `nbf`: When the session token activates.
* `iat`: When the session token was issued.
* `jti`: A secure random UUID.
* `sid`: A unique session ID per user and app.
* `sig`: Shopify signature.

### [Anchor to Example payload](/docs/apps/build/authentication-authorization/session-tokens#example-payload)Example payload

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

{

"iss"=>"https://exampleshop.myshopify.com/admin",

"dest"=>"https://exampleshop.myshopify.com",

"aud"=>"client-id-123",

"sub"=>"42",

"exp"=>1591765058,

"nbf"=>1591764998,

"iat"=>1591764998,

"jti"=>"f8912129-1af6-4cad-9ca3-76b0f7621087",

"sid"=>"aaea182f2732d44c23057c0fea584021a4485b2bd25d3eb7fd349313ad24c685",

"sig"=>"f07cf3740270c17fb61c700b2f0f2e7f2f4fc8cc48426221738f7a39e4c475bf",

}

Note

All times are in UNIX timestamp format.

**Note:**

All times are in UNIX timestamp format.

---

## [Anchor to Limitations](/docs/apps/build/authentication-authorization/session-tokens#limitations)Limitations

[Session token authentication](/docs/apps/build/authentication-authorization/session-tokens/set-up-session-tokens) is only fully supported for single-page apps. You can only use session tokens for a multi-page app if you convert it to behave like a single-page app. For an example, refer to the [Turbolinks and JWT sample app](https://github.com/Shopify/turbolinks-jwt-sample-app).

Caution

In some cases, ad blockers can interfere with session tokens. If you're submitting your app to the Shopify App Store and the automated check for session tokens is hanging, then try disabling your ad blocker and interacting with your app to record the required session data.

**Caution:**

In some cases, ad blockers can interfere with session tokens. If you're submitting your app to the Shopify App Store and the automated check for session tokens is hanging, then try disabling your ad blocker and interacting with your app to record the required session data.

---

## [Anchor to Sample apps](/docs/apps/build/authentication-authorization/session-tokens#sample-apps)Sample apps

* [Sample single-page embedded app using Rails and React](https://github.com/Shopify/next-gen-auth-app-demo)
* [Sample server-side rendered Rails app converted using Turbolinks](https://github.com/Shopify/turbolinks-jwt-sample-app)

---

## [Anchor to Next steps](/docs/apps/build/authentication-authorization/session-tokens#next-steps)Next steps

* Set up your embedded app to [authenticate using session tokens](/docs/apps/build/authentication-authorization/session-tokens/set-up-session-tokens).

---

Was this page helpful?

YesNo