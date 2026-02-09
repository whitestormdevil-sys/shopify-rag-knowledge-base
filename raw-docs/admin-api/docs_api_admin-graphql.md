---
source: https://shopify.dev/docs/api/admin-graphql
---

# GraphQL Admin API reference

The Admin API lets you build apps and integrations that extend and enhance the Shopify admin.

This page will help you get up and running with Shopify’s GraphQL API.

Ask assistant

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

## [Anchor to Client libraries](/docs/api/admin-graphql/latest#client-libraries)Client libraries

Use Shopify’s officially supported libraries to build fast, reliable apps with the programming languages and frameworks you already know.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-DwHxpQ4h.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-dark-BRmMldI1.svg)

React Router

The official package for React Router applications.

* [Docs](/docs/api/shopify-app-react-router)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-app-react-router)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-app-react-router#readme)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)

Node.js

The official client library for Node.js apps. No framework dependencies—works with any Node.js app.

* [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api#readme)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)

Ruby

The official client library for Ruby apps.

* [Docs](https://shopify.github.io/shopify-api-ruby/)
* [Ruby gem](https://rubygems.org/gems/shopify_api)
* [GitHub repo](https://github.com/Shopify/shopify-api-ruby)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-DNth-3tL.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-dark-Dltnwzzq.svg)

cURL

Use the [curl utility](https://curl.se/) to make API queries directly from the command line.

Other

Need a different language? Check the list of [community-supported libraries](/apps/tools/api-libraries#third-party-admin-api-libraries).

---

## [Anchor to Authentication](/docs/api/admin-graphql/latest#authentication)Authentication

All GraphQL Admin API requests require a valid Shopify access token. If you use Shopify’s [client libraries](/apps/tools/api-libraries), then this will be done for you. Otherwise, you should include your token as a `X-Shopify-Access-Token` header on all GraphQL requests.

Public and custom apps created in the Dev Dashboard generate tokens using [OAuth](/apps/auth/oauth), and custom apps made in the Shopify admin are [authenticated in the Shopify admin](/apps/auth/admin-app-access-tokens).

To keep the platform secure, apps need to request specific [access scopes](/api/usage/access-scopes) during the install process. Only request as much data access as your app needs to work.

Learn more about [getting started with authentication](/apps/auth) and [building apps](/apps/getting-started).

---

## [Anchor to Endpoints and queries](/docs/api/admin-graphql/latest#endpoints-and-queries)Endpoints and queries

GraphQL queries are executed by sending `POST` HTTP requests to the endpoint:

`https://{store_name}.myshopify.com/admin/api/2026-01/graphql.json`

Queries begin with one of the objects listed under [QueryRoot](/api/admin-graphql/2026-01/objects/queryroot). The QueryRoot is the schema’s entry-point for queries.

Queries are equivalent to making a `GET` request in REST. The example shown is a query to get the ID and title of the first three products.

Learn more about [API usage](/api/usage).

---

Note

Explore and learn Shopify's Admin API using [GraphiQL Explorer](/apps/tools/graphiql-admin-api). To build queries and mutations with shop data, install [Shopify’s GraphiQL app](https://shopify-graphiql-app.shopifycloud.com/).

**Note:**

Explore and learn Shopify's Admin API using [GraphiQL Explorer](/apps/tools/graphiql-admin-api). To build queries and mutations with shop data, install [Shopify’s GraphiQL app](https://shopify-graphiql-app.shopifycloud.com/).

---

## [Anchor to Rate limits](/docs/api/admin-graphql/latest#rate-limits)Rate limits

The GraphQL Admin API is rate-limited using calculated query costs, measured in cost points. Each field returned by a query costs a set number of points. The total cost of a query is the maximum of possible fields selected, so more complex queries cost more to run.

Learn more about [rate limits](/api/usage/limits#graphql-admin-api-rate-limits).

---

## [Anchor to Status and error codes](/docs/api/admin-graphql/latest#status-and-error-codes)Status and error codes

All API queries return HTTP status codes that contain more information about the response.

### [Anchor to 200 OK](/docs/api/admin-graphql/latest#200-ok)200 OK

GraphQL HTTP status codes are different from REST API status codes. Most importantly, the GraphQL API can return a `200 OK` response code in cases that would typically produce 4xx or 5xx errors in REST.

### [Anchor to Error handling](/docs/api/admin-graphql/latest#error-handling)Error handling

The response for the errors object contains additional detail to help you debug your operation.

The response for mutations contains additional detail to help debug your query. To access this, you must request `userErrors`.

#### Properties

errors•array

A list of all errors returned

Show error item properties

errors[n].message•string

Contains details about the error(s).

errors[n].extensions•object

Provides more information about the error(s) including properties and metadata.

Show extensions properties

errors[n].extensions.code•string

Shows error codes common to Shopify. Additional error codes may also be shown.

Show common error codes

THROTTLED

The client has exceeded the [rate limit](#rate-limits). Similar to 429 Too Many Requests.

ACCESS\_DENIED

The client doesn’t have correct [authentication](#authentication) credentials. Similar to 401 Unauthorized.

SHOP\_INACTIVE

The shop is not active. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.

INTERNAL\_SERVER\_ERROR

Shopify experienced an internal error while processing the request. This error is returned instead of 500 Internal Server Error in most circumstances.

---

### [Anchor to 4xx and 5xx status codes](/docs/api/admin-graphql/latest#4xx-and-5xx-status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an HTTP 200 errors response instead. Refer to the [200 OK section](#200-ok) above for details.

### [Anchor to 4xx and 5xx status codes](/docs/api/admin-graphql/latest#4xx-and-5xx-status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an HTTP 200 errors response instead. Refer to the [200 OK section](#200-ok) above for details.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#400-bad-request)400 Bad Request

The server will not process the request.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#402-payment-required)402 Payment Required

The shop is frozen. The shop owner will need to pay the outstanding balance to [unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-store#unfreeze-your-shopify-store) the shop.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#403-forbidden)403 Forbidden

The shop is forbidden. Returned if the store has been marked as fraudulent.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#404-not-found)404 Not Found

The resource isn’t available. This is often caused by querying for something that’s been deleted.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#423-locked)423 Locked

The shop isn’t available. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.

---

#### [Anchor to [object Object]](/docs/api/admin-graphql/latest#5xx-errors)5xx Errors

An internal error occurred in Shopify. Check out the [Shopify status page](https://www.shopifystatus.com) for more information.

---

Info

Didn’t find the status code you’re looking for? View the complete list of
[API status response and error codes](/api/usage/response-codes).

**Info:**

Didn’t find the status code you’re looking for? View the complete list of
[API status response and error codes](/api/usage/response-codes).

---

Was this page helpful?

YesNo