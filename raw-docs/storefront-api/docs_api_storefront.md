---
source: https://shopify.dev/docs/api/storefront
---

# GraphQL Storefront API

Create unique customer experiences with the Storefront API on any platform, including the web, apps, and games. The API offers a full range of commerce options making it possible for customers to view [products](/custom-storefronts/products-collections/getting-started) and [collections](/custom-storefronts/products-collections/filter-products), add products to a [cart](/custom-storefronts/cart/manage), and [check out](/custom-storefronts/checkout).

Explore [Hydrogen](/custom-storefronts/hydrogen), Shopify’s official React-based framework for building headless commerce at global scale.

Ask assistant

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

## [Anchor to Development frameworks and SDKs](/docs/api/storefront/latest#development-frameworks-and-sdks)Development frameworks and SDKs

Use Shopify’s officially supported libraries to build fast, reliable apps with the programming languages and frameworks you already know.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-DNth-3tL.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/CURL-dark-Dltnwzzq.svg)

cURL

Use the [curl utility](https://curl.se/) to make API queries directly from the command line.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/React-V80EhnnE.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/React-V80EhnnE.svg)

Hydrogen

A React-based framework for building custom storefronts on Shopify, Hydrogen has everything you need to build fast, and deliver personalized shopping experiences.

* [Docs](https://github.com/Shopify/hydrogen#readme)
* [npm package](https://www.npmjs.com/package/@shopify/hydrogen)
* [GitHub repo](https://github.com/Shopify/hydrogen)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)

Storefront API Client

The official lightweight client for any Javascript project interfacing with Storefront API and our recommended client for building custom storefronts without Hydrogen.

* [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/storefront-api-client#readme)
* [npm package](https://www.npmjs.com/package/@shopify/storefront-api-client)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/storefront-api-client)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-DwHxpQ4h.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-dark-BRmMldI1.svg)

React Router Apps

The official package for React Router apps.

* [Docs](/docs/api/shopify-app-react-router)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-app-react-router)
* [GitHub repo](https://github.com/Shopify/shopify-app-template-react-router#readme)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)

Node.js

The official client library for Node.js applications, with full TypeScript support. It has no framework dependencies, so it can be used by any Node.js app.

* [Docs](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api#readme)
* [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-DcYew0um.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Nodejs-dark-DB-77f7o.svg)

Shopify API (Apps)

The full suite library for TypeScript/JavaScript Shopify apps to access the GraphQL and REST Admin APIs and the Storefront API.

* [npm package](https://www.npmjs.com/package/@shopify/shopify-api)
* [GitHub repo](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Ruby-C1_5iUYm.svg)

Ruby

The official client library for Ruby applications. It has no framework dependencies, so it can be used by any Ruby app. This API applies a rate limit based on the IP address making the request, which will be your server’s address for all requests made by the library. Learn more about [rate limits](/api/usage/limits#rate-limits).

* [Docs](https://shopify.github.io/shopify-api-ruby/)
* [Ruby gem](https://rubygems.org/gems/shopify_api)
* [GitHub repo](https://github.com/Shopify/shopify-api-ruby)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Android-DvfCNqaF.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/Android-dark-Bu6uMCXk.svg)

Android

The official client library for Android apps.

* [Docs](https://github.com/Shopify/mobile-buy-sdk-android#readme)
* [GitHub repo](https://github.com/Shopify/mobile-buy-sdk-android)

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/IOS-BPgmboYz.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/IOS-dark-BeZqDXep.svg)

iOS

The official client library for iOS applications.

* [Docs](https://github.com/Shopify/mobile-buy-sdk-ios#readme)
* [GitHub repo](https://github.com/Shopify/mobile-buy-sdk-ios)
Other

Other libraries are available in addition to the ones listed here. Check the list of [developer tools for custom storefronts](/custom-storefronts/tools).

---

## [Anchor to Authentication](/docs/api/storefront/latest#authentication)Authentication

The Storefront API supports both tokenless access and token-based authentication.

### [Anchor to Tokenless access](/docs/api/storefront/latest#tokenless-access)Tokenless access

Tokenless access allows API queries without an access token providing access to essential features such as:

* Products and Collections
* Selling Plans
* Search
* Pages, Blogs, and Articles
* Cart (read/write)

Tokenless access has a query complexity limit of 1,000. Query complexity is calculated based on the cost of each field in the query. For more information, see the [Cost calculation](#rate-limits) section.

### [Anchor to Token-based authentication](/docs/api/storefront/latest#token-based-authentication)Token-based authentication

For access to all Storefront API features, an access token is required. The following features require token-based authentication:

* Product Tags
* Metaobjects and Metafields
* Menu (Online Store navigation)
* Customers

The Storefront API has the following types of token-based access:

* **Public access**: Used to query the API from a browser or mobile app.
* **Private access**: Used to query the API from a server or other private context, like a Hydrogen backend.

Learn more about [access tokens for the Storefront API](/api/usage/authentication#access-tokens-for-the-storefront-api).

---

## [Anchor to Endpoints and queries](/docs/api/storefront/latest#endpoints-and-queries)Endpoints and queries

The Storefront API is available only in GraphQL. There's no REST API for storefronts.

All Storefront API queries are made on a single GraphQL endpoint, which only accepts `POST` requests:

`https://{store_name}.myshopify.com/api/2026-01/graphql.json`

### [Anchor to Versioning](/docs/api/storefront/latest#versioning)Versioning

The Storefront API is [versioned](/api/usage/versioning), with new releases four times a year. To keep your app stable, make sure that you specify a supported version in the URL.

### [Anchor to GraphiQL explorer](/docs/api/storefront/latest#graphiql-explorer)GraphiQL explorer

Explore and learn Shopify's Storefront API using the [GraphiQL explorer](/custom-storefronts/tools/graphiql-storefront-api). To build queries and mutations with shop data, install [Shopify's GraphiQL app](https://shopify-graphiql-app.shopifycloud.com/).

### [Anchor to Usage limitations](/docs/api/storefront/latest#usage-limitations)Usage limitations

* Shopify Plus [bot protection](https://help.shopify.com/en/manual/checkout-settings/bot-protection) is only available for the [Cart](/custom-storefronts/cart/manage) object. It isn't available for the [Checkout](/custom-storefronts/checkout) object.
* You can't use Storefront API to duplicate existing Shopify functionality—be sure to check the API terms of service before you start.

---

## [Anchor to Directives](/docs/api/storefront/latest#directives)Directives

A directive provides a way for apps to describe additional options to the GraphQL executor. It lets GraphQL change the result of the query or mutation based on the additional information provided by the directive.

### [Anchor to Storefront Directives](/docs/api/storefront/latest#storefront-directives)Storefront Directives

@inContext (Country Code)

In the Storefront API, the `@inContext` directive takes an optional [country code argument](/api/storefront/2026-01/enums/countrycode) and applies this to the query or mutation.

This example shows how to retrieve a list of available countries and their corresponding currencies for a shop that's located in France `@inContext(country: FR)`.

* [Examples for localized pricing](/api/examples/international-pricing)
* [GQL directives spec](https://graphql.org/learn/queries/#directives)
@inContext (Language)

In the Storefront API, beyond version 2022-04, the `@inContext` directive can contextualize any query to one of a shop's available languages with an optional [language code argument](/api/storefront/2026-01/enums/LanguageCode).

This example shows how to return a product's `title`, `description`, and `options` translated into Spanish `@inContext(language: ES)`.

* [Examples for supporting multiple languages](/api/examples/multiple-languages)
* [GQL directives spec](https://graphql.org/learn/queries/#directives)
@inContext (Buyer Identity)

In the Storefront API, beyond version 2024-04, the `@inContext` directive can contextualize any query to a logged in buyer of a shop with an optional [buyer argument](/api/storefront/2026-01/input-objects/BuyerInput).

This example shows how to return a product's price `amount` contextualized for a business customer buyer `@inContext(buyer: {customerAccessToken: 'token', companyLocationId: 'gid://shopify/CompanyLocation/1'})`.

* [Example for supporting a contextualized buyer identity](/custom-storefronts/headless/b2b#step-3-contextualize-storefront-api-requests)
* [GraphQL directives spec](https://graphql.org/learn/queries/#directives)
@inContext (Visitor Consent)

In the Storefront API, beyond version 2025-10, the `@inContext` directive can contextualize any query or mutation with visitor consent information using an optional `visitorConsent` argument.

This example shows how to create a cart with visitor consent preferences `@inContext(visitorConsent: {analytics: true, preferences: true, marketing: false, saleOfData: false})`.

The consent information is automatically encoded and included in the resulting [`checkoutUrl`](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.checkoutUrl) to ensure privacy compliance throughout the checkout process. All consent fields are optional.

* [Examples for collecting and passing visitor consent with Checkout Kit](/docs/storefronts/mobile/checkout-kit/privacy-compliance)
* [GraphQL directives spec](https://graphql.org/learn/queries/#directives)
@defer

The `@defer` directive allows clients to prioritize part of a GraphQL query without having to make more requests to fetch the remaining information. It does this through streaming, where the first response contains the data that isn't deferred.

The directive accepts two optional arguments: `label` and `if`. The `label` is included in the fragment response if it's provided in the directive. When the `if` argument is `false`, the fragment isn't deferred.

This example shows how to return a product's `title` and `description` immediately, and then return the `descriptionHtml` and `options` after a short delay.

The `@defer` directive is available as a [developer preview](/docs/api/developer-previews#defer-directive-developer-preview) in `unstable`.

* [Examples for how to use `@defer`](/docs/custom-storefronts/building-with-the-storefront-api/defer)

---

## [Anchor to Rate limits](/docs/api/storefront/latest#rate-limits)Rate limits

The Storefront API is designed to support businesses of all sizes. The Storefront API will scale to support surges in buyer traffic or your largest flash sale. There are no rate limits applied on the number of requests that can be made to the API.

The Storefront API provides protection against malicious users, such as bots, from consuming a high level of capacity. If a request appears to be malicious, Shopify will respond with a `430 Shopify Security Rejection` [error code](/docs/api/usage/response-codes) to indicate potential security concerns. Ensure requests to the Storefront API include the correct [Buyer IP header](/docs/api/usage/authentication#optional-ip-header).

[Learn more about rate limits](/docs/api/usage/limits#rate-limits).

### [Anchor to Query complexity limit for tokenless access](/docs/api/storefront/latest#query-complexity-limit-for-tokenless-access)Query complexity limit for tokenless access

Tokenless access has a query complexity limit of 1,000. This limit is calculated based on the cost of each field in the query in the same way as the GraphQL Admin API. For more information on how query costs are calculated, see the [Cost calculation](/docs/api/usage/limits#rate-limits#cost-calculation) section in the API rate limits documentation.

When using tokenless access, query complexity that exceeds 1,000 will result in an error.

---

## [Anchor to Status and error codes](/docs/api/storefront/latest#status-and-error-codes)Status and error codes

All API queries return HTTP status codes that contain more information about the response.

### [Anchor to 200 OK](/docs/api/storefront/latest#200-ok)200 OK

The Storefront API can return a `200 OK` response code in cases that would typically produce 4xx errors in REST.

### [Anchor to Error handling](/docs/api/storefront/latest#error-handling)Error handling

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

extensions.code•string

Shows error codes common to Shopify. Additional error codes may also be shown.

Show common error codes

ACCESS\_DENIED

The client doesn’t have correct [authentication](#authentication) credentials. Similar to 401 Unauthorized.

SHOP\_INACTIVE

The shop is not active. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.

INTERNAL\_SERVER\_ERROR

Shopify experienced an internal error while processing the request. This error is returned instead of 500 Internal Server Error in most circumstances.

---

### [Anchor to 4xx and 5xx status codes](/docs/api/storefront/latest#4xx-and-5xx-status-codes)4xx and 5xx status codes

The 4xx and 5xx errors occur infrequently. They are often related to network communications, your account, or an issue with Shopify’s services.

Many errors that would typically return a 4xx or 5xx status code, return an HTTP 200 errors response instead. Refer to the [200 OK section](#200-ok) above for details.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#400-bad-request)400 Bad Request

The server will not process the request.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#402-payment-required)402 Payment Required

The shop is frozen. The shop owner will need to pay the outstanding balance to [unfreeze](https://help.shopify.com/en/manual/your-account/pause-close-store#unfreeze-your-shopify-store) the shop.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#403-forbidden)403 Forbidden

The shop is forbidden. Returned if the store has been marked as fraudulent.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#404-not-found)404 Not Found

The resource isn’t available. This is often caused by querying for something that’s been deleted.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#423-locked)423 Locked

The shop isn’t available. This can happen when stores repeatedly exceed API rate limits or due to fraud risk.

---

#### [Anchor to [object Object]](/docs/api/storefront/latest#5xx-errors)5xx Errors

An internal error occurred in Shopify. Check out the [Shopify status page](https://www.shopifystatus.com) for more information.

---

Info

Didn’t find the status code you’re looking for? View the complete list of
[API status response and error codes](/api/usage/response-codes).

**Info:**

Didn’t find the status code you’re looking for? View the complete list of
[API status response and error codes](/api/usage/response-codes).

---

## [Anchor to Resources](/docs/api/storefront/latest#resources)Resources

[![](/images/icons/32/custom-storefronts.png)![](/images/icons/32/custom-storefronts-dark.png)

Get started

Learn more about how the Storefront API works and how to get started with it.

Get started

Learn more about how the Storefront API works and how to get started with it.](/docs/storefronts/headless/building-with-the-storefront-api)

[Get started  
  

Learn more about how the Storefront API works and how to get started with it.](/docs/storefronts/headless/building-with-the-storefront-api)

[![](/images/icons/32/growth.png)![](/images/icons/32/growth-dark.png)

Storefront Learning Kit

Explore a downloadable package of sample GraphQL queries for the Storefront API.

Storefront Learning Kit

Explore a downloadable package of sample GraphQL queries for the Storefront API.](https://github.com/Shopify/storefront-api-learning-kit)

[Storefront Learning Kit  
  

Explore a downloadable package of sample GraphQL queries for the Storefront API.](https://github.com/Shopify/storefront-api-learning-kit)

[![](/images/icons/32/changelog.png)![](/images/icons/32/changelog-dark.png)

Developer changelog

Read about the changes currently introduced in the latest version of the Storefront API.

Developer changelog

Read about the changes currently introduced in the latest version of the Storefront API.](/changelog)

[Developer changelog  
  

Read about the changes currently introduced in the latest version of the Storefront API.](/changelog)

---

Was this page helpful?

YesNo