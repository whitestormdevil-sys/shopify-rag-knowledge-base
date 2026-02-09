---
source: https://shopify.dev/docs/apps/build/graphql/migrate
---

Legacy

The REST Admin API is a legacy API as of October 1, 2024. All apps and integrations should be built with the [GraphQL Admin API](/docs/api/admin-graphql). Read on to learn how to migrate from the REST Admin API to the GraphQL Admin API.

**Legacy:**

The REST Admin API is a legacy API as of October 1, 2024. All apps and integrations should be built with the [GraphQL Admin API](/docs/api/admin-graphql). Read on to learn how to migrate from the REST Admin API to the GraphQL Admin API.

GraphQL is Shopify's technology of choice for building APIs. GraphQL addresses several problems that might sound familiar to anyone who's worked with a REST API.

You can migrate your apps to use the GraphQL Admin API instead of the REST Admin API to take advantage of the [benefits of GraphQL](/docs/api/usage/graphql-basics#benefits-of-graphql-over-rest).

This section includes guides and resources to help you with the migration process.

---

## [Anchor to Why migrate to GraphQL](/docs/apps/build/graphql/migrate#why-migrate-to-graphql)Why migrate to GraphQL

The GraphQL Admin API offers several advantages over REST:

* **Request only what you need**: Unlike REST endpoints that return fixed data structures, GraphQL lets you specify exactly which fields you want. This reduces payload sizes and improves performance.
* **Single request for related data**: Retrieve information about related objects with a single request using connections, eliminating the need to chain multiple REST API calls.
* **Strongly typed schema**: GraphQL's type system provides built-in documentation and validation, making it easier to understand what data is available and how to request it.
* **Better performance**: GraphQL's calculated query cost model is more efficient than REST's request-based rate limiting, allowing you to do more with your rate limit budget.
* **Future-proof**: New Shopify features and improvements are released in GraphQL first. The REST Admin API is in maintenance mode and receives only critical updates.

---

## [Anchor to Getting started](/docs/apps/build/graphql/migrate#getting-started)Getting started

Refer to the following resources to start migrating from REST to GraphQL:

[![](/images/icons/48/growth.png)![](/images/icons/48/growth-dark.png)

Migrate to GraphQL from REST

Learn about the things that you need to consider when migrating your app from REST to GraphQL.

Migrate to GraphQL from REST

Learn about the things that you need to consider when migrating your app from REST to GraphQL.](/docs/apps/build/graphql/migrate/learn-how)

[Migrate to GraphQL from REST  
  

Learn about the things that you need to consider when migrating your app from REST to GraphQL.](/docs/apps/build/graphql/migrate/learn-how)

[![](/images/icons/48/app.png)![](/images/icons/48/app-dark.png)

Update API calls in your app

Learn how to update your REST API calls to GraphQL API calls using common API client libraries.

Update API calls in your app

Learn how to update your REST API calls to GraphQL API calls using common API client libraries.](/docs/apps/build/graphql/migrate/libraries)

[Update API calls in your app  
  

Learn how to update your REST API calls to GraphQL API calls using common API client libraries.](/docs/apps/build/graphql/migrate/libraries)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Explore GraphQL basics

Learn about the fundamentals of GraphQL.

Explore GraphQL basics

Learn about the fundamentals of GraphQL.](/docs/apps/build/graphql)

[Explore GraphQL basics  
  

Learn about the fundamentals of GraphQL.](/docs/apps/build/graphql)

---

## [Anchor to Developer tools and resources](/docs/apps/build/graphql/migrate#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to learn more about Shopify GraphQL APIs.

[![](/images/icons/48/scintillating.png)![](/images/icons/48/scintillating-dark.png)

.dev Assistant

Generate GraphQL operations, convert REST requests to GraphQL operations, and get interactive help with Shopify's AI-powered assistant.  
  
Trained on Shopify data for high accuracy.

.dev Assistant

Generate GraphQL operations, convert REST requests to GraphQL operations, and get interactive help with Shopify's AI-powered assistant.  
  
Trained on Shopify data for high accuracy.](/docs/apps/build/graphql/migrate?assistant=1)

[.dev Assistant  
  

Generate GraphQL operations, convert REST requests to GraphQL operations, and get interactive help with Shopify's AI-powered assistant.  
  
Trained on Shopify data for high accuracy.](/docs/apps/build/graphql/migrate?assistant=1)

[![](/images/icons/48/pickaxe-2.png)![](/images/icons/48/pickaxe-2-dark.png)

Shopify Dev Assistant VS Code Extension

Access AI-powered Shopify development help directly within Visual Studio Code, with automatic GraphQL query execution and GraphiQL integration.  
  
Seamlessly integrates with your local development workflow. Trained on Shopify data for high accuracy.

Shopify Dev Assistant VS Code Extension

Access AI-powered Shopify development help directly within Visual Studio Code, with automatic GraphQL query execution and GraphiQL integration.  
  
Seamlessly integrates with your local development workflow. Trained on Shopify data for high accuracy.](https://github.com/Shopify/vscode-shopify-dev-assistant)

[Shopify Dev Assistant VS Code Extension  
  

Access AI-powered Shopify development help directly within Visual Studio Code, with automatic GraphQL query execution and GraphiQL integration.  
  
Seamlessly integrates with your local development workflow. Trained on Shopify data for high accuracy.](https://github.com/Shopify/vscode-shopify-dev-assistant)

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

GraphQL Admin API reference

Consult the complete reference to Shopify’s GraphQL Admin API.

GraphQL Admin API reference

Consult the complete reference to Shopify’s GraphQL Admin API.](/docs/api/admin-graphql)

[GraphQL Admin API reference  
  

Consult the complete reference to Shopify’s GraphQL Admin API.](/docs/api/admin-graphql)

[![](/images/icons/48/pickaxe-2.png)![](/images/icons/48/pickaxe-2-dark.png)

Shopify Admin API GraphiQL explorer

Browse Shopify’s GraphQL Admin API schema and documentation.

Shopify Admin API GraphiQL explorer

Browse Shopify’s GraphQL Admin API schema and documentation.](/docs/api/usage/api-exploration/admin-graphiql-explorer)

[Shopify Admin API GraphiQL explorer  
  

Browse Shopify’s GraphQL Admin API schema and documentation.](/docs/api/usage/api-exploration/admin-graphiql-explorer)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

GraphQL Storefront API reference

Consult the complete reference to Shopify’s GraphQL Storefront API.

GraphQL Storefront API reference

Consult the complete reference to Shopify’s GraphQL Storefront API.](/docs/api/storefront)

[GraphQL Storefront API reference  
  

Consult the complete reference to Shopify’s GraphQL Storefront API.](/docs/api/storefront)

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

Shopify Storefront API GraphiQL explorer

Browse Shopify’s Storefront API schema and documentation.

Shopify Storefront API GraphiQL explorer

Browse Shopify’s Storefront API schema and documentation.](/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)

[Shopify Storefront API GraphiQL explorer  
  

Browse Shopify’s Storefront API schema and documentation.](/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)

[![](/images/icons/48/app.png)![](/images/icons/48/app-dark.png)

Shopify GraphiQL app

Explore your store's data, and test queries and mutations, using the GraphQL Admin and Storefront APIs.

Shopify GraphiQL app

Explore your store's data, and test queries and mutations, using the GraphQL Admin and Storefront APIs.](https://shopify-graphiql-app.shopifycloud.com/)

[Shopify GraphiQL app  
  

Explore your store's data, and test queries and mutations, using the GraphQL Admin and Storefront APIs.](https://shopify-graphiql-app.shopifycloud.com/)

---

Was this page helpful?

YesNo