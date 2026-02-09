---
source: https://shopify.dev/docs/api/admin-rest
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

# REST Admin API reference

The Admin API lets you build apps and integrations that extend and enhance the Shopify admin.

Some newer platform features may only be available in [GraphQL](/docs/api/admin-graphql).

Ask assistant

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

## [Anchor to Client libraries](/docs/api/admin-rest#client-libraries)Client libraries

Use Shopify’s officially supported libraries to build fast, reliable apps with the programming languages and frameworks you already know.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-DNth-3tL.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-dark-Dltnwzzq.svg)

cURL

Use the [curl utility](https://curl.se/) to make API queries directly from the command line.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Remix-CsgrNfMr.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Remix-dark-pBuEP-h0.svg)

Remix

The official package for Remix applications, with full TypeScript support.

* [Docs](/docs/api/shopify-app-remix)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-app-remix)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-app-remix#readme)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)

Node.js

The official client library for Node.js applications, with full TypeScript support. It has no framework dependencies, so it can be used by any Node.js app.

* [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api#readme)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)

Ruby

The official client library for Ruby apps.

* [Docs](https://shopify.github.io/shopify-api-ruby/)
* [Ruby gem](https://rubygems.org/gems/shopify_api)
* [GitHub repo](https://github.com/Shopify/shopify-api-ruby)
Other

Need a different language? Check the list of [community-supported libraries](/apps/tools/api-libraries#third-party-admin-api-libraries).

---

## [Anchor to Authentication](/docs/api/admin-rest#authentication)Authentication

All REST Admin API queries require a valid Shopify access token.

Public and custom apps created in the Dev Dashboard generate tokens using [OAuth](https://shopify.dev/apps/auth/oauth), and custom apps made in the Shopify admin are [authenticated in the Shopify admin](/apps/auth/admin-app-access-tokens). To simplify the authentication process, use one of the recommended Shopify client libraries.

Include your token as a `X-Shopify-Access-Token` header on all API queries. Using Shopify’s supported [client libraries](/apps/tools/api-libraries) can simplify this process.

To keep the platform secure, apps need to request specific [access scopes](/api/usage/access-scopes) during the install process. Only request as much data access as your app needs to work.

Learn more about [getting started with authentication](/apps/auth) and [building apps](/apps/getting-started).

---

## [Anchor to Endpoints and requests](/docs/api/admin-rest#endpoints-and-requests)Endpoints and requests

Admin REST API endpoints are organized by resource type. You’ll need to use different endpoints depending on your app’s requirements.

All Admin REST API endpoints follow this pattern:

`https://{store_name}.myshopify.com/admin/api/2026-01/{resource}.json`

POST

Example POST request

Create a new product.

This example illustrates how to create a new product using the Product resource and the `/admin/api/2026-01/products.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.

GET

Example GET request

Retrieve a single product.

This example illustrates how to retrieve information for a single product using the Product resource and the `admin/api/2026-01/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.

PUT

Example PUT request

Update a product.

This example illustrates how to update a product using the Product resource and the `admin/api/2026-01/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.

DEL

Example DELETE request

Delete a product.

This example illustrates how to delete a product using the Product resource and the `admin/api/2026-01/products/{product_id}.json` endpoint. Replace `{store_name}` with your store’s domain and `{access_token}` with the access token you generated in the Authentication section.

The Admin API is versioned, with new releases four times per year. To keep your app stable, make sure you specify a supported version in the URL. Learn more about [API versioning](/api/usage/versioning).

All REST endpoints support [cursor-based pagination](/api/usage/pagination-rest). All requests produce HTTP [response status codes](/api/usage/response-codes).

Learn more about [API usage](/api/usage).

---

## [Anchor to Rate limits](/docs/api/admin-rest#rate-limits)Rate limits

The REST Admin API supports a limit of 40 requests per app per store per minute. This allotment replenishes at a rate of 2 requests per second. The rate limit is increased by a factor of 10 for Shopify Plus stores.

### [Anchor to Usage limitations](/docs/api/admin-rest#usage-limitations)Usage limitations

REST Admin API supports a limit of **40 requests per app per store per minute**.

Past the limit, the API will return a `429 Too Many Requests` error.

All REST API responses include the `X-Shopify-Shop-Api-Call-Limit` header, which shows how many requests the client has made, and the total number allowed per minute.

A `429` response will also include a `Retry-After` header with the number of seconds to wait until retrying your query.

Learn more about [rate limits](/api/usage/limits#rest-admin-api-rate-limits).

---

## [Anchor to Status and error codes](/docs/api/admin-rest#status-and-error-codes)Status and error codes

All API queries return HTTP status codes that can tell you more about the response.

---

#### [Anchor to [object Object]](/docs/api/admin-rest#401-unauthorized)401 Unauthorized

The client doesn’t have correct [authentication](#authentication) credentials.

---

#### [Anchor to [object Object]](/docs/api/admin-rest#402-payment-required)402 Payment Required

The shop is frozen. The shop owner will need to pay the outstanding balance to [unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-store#unfreeze-your-shopify-store) the shop.

---

#### [Anchor to [object Object]](/docs/api/admin-rest#403-forbidden)403 Forbidden

The server is refusing to respond. This is typically caused by incorrect [access scopes](/api/usage/access-scopes).

---

#### [Anchor to [object Object]](/docs/api/admin-rest#404-not-found)404 Not Found

The requested resource was not found but could be available again in the future.

---

#### [Anchor to [object Object]](/docs/api/admin-rest#422-unprocessable-entity)422 Unprocessable Entity

The request body contains semantic errors. This is typically caused by incorrect formatting, omitting required fields, or logical errors such as initiating a checkout for an out-of-stock product.

---

#### [Anchor to [object Object]](/docs/api/admin-rest#429-too-many-requests)429 Too Many Requests

The client has exceeded the [rate limit](#rate-limits).

---

#### [Anchor to [object Object]](/docs/api/admin-rest#5xx-errors)5xx Errors

An internal error occurred in Shopify. Check out the [Shopify status page](https://www.shopifystatus.com) for more information.

---

Didn’t find the status code you’re looking for?

View the complete list of [API status response and error codes](/api/usage/response-codes).

**Didn’t find the status code you’re looking for?:**

View the complete list of [API status response and error codes](/api/usage/response-codes).

---

Was this page helpful?

YesNo