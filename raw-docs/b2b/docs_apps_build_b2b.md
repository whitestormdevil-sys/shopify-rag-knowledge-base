---
source: https://shopify.dev/docs/apps/build/b2b
---

Plus

Only stores on the [Shopify Plus](https://www.shopify.com/plus) plan can use apps with B2B features.

**Plus:**

Only stores on the [Shopify Plus](https://www.shopify.com/plus) plan can use apps with B2B features.

In business-to-business (B2B) commerce, merchants sell directly to other companies. When a company is the customer, there are often multiple contacts and locations, pre-negotiated payment terms, and catalogs to manage. All of these factors complicate expanding a business into the B2B space.

You can use the [GraphQL Admin API](/docs/api/admin-graphql) to build apps and features that help Shopify merchants to manage their B2B commerce. For example, you can build B2B-specific interfaces for managing [company locations](/docs/apps/build/b2b/manage-client-company-locations), [draft orders and invoicing](/docs/apps/build/b2b/draft-orders), and [catalogs](/docs/apps/build/b2b/manage-catalogs).

In this guide, you'll learn how B2B objects work, and how to use the GraphQL Admin API to build common B2B features.

---

## [Anchor to Features](/docs/apps/build/b2b#features)Features

The GraphQL Admin API's B2B resources enable you to do the following tasks:

* [Create companies](/docs/apps/build/b2b/start-building) and [attach information](/docs/apps/build/b2b/manage-client-company-locations) to the company, such as company contacts and company locations.
* [Associate catalogs](/docs/apps/build/b2b/start-building#step-2-create-a-b2b-catalog) with company locations to offer exclusive product selections and negotiated pricing levels to contacts at different company locations within a company.
* [Query B2B orders](/docs/api/admin-graphql/latest/queries/orders) and [create draft orders](/docs/apps/build/b2b/draft-orders) to send to company contacts for approval and invoicing.
* [Import B2B orders](/docs/apps/build/b2b/import-orders) for merchants with B2B operations outside of Shopify.

---

## [Anchor to How it works](/docs/apps/build/b2b#how-it-works)How it works

The GraphQL Admin API provides several company-related objects to help with managing the B2B experience between merchants and their company customers, including the following objects:

| Object | Description |
| --- | --- |
| `Company` | Information about the business entity that makes a B2B purchase.  A company contains locations and contacts. |
| `CompanyLocation` | A single location or branch of the company.  A company location contains information such as billing addresses and shipping addresses. You can also assign [catalogs](/docs/api/admin-graphql/unstable/interfaces/catalog), [tax exemptions](/docs/api/admin-graphql/latest/enums/TaxExemption), [payment terms](/docs/apps/build/b2b/manage-client-company-locations#step-3-associate-payment-terms-with-a-company-location), and other useful information to a company location. |
| `CompanyContact` | A person that acts on behalf of the company.  A company contact is associated with a retail [customer](/docs/api/admin-graphql/latest/objects/Customer) record. |

The following diagram shows how company locations and company contacts relate to a company. A B2B order or draft order can be associated with the company, a specific company location, or a specific company contact. However, catalogs can be assigned only to a company location.

![Diagram of the B2B on Shopify company object](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/b2b/b2b-company-object-CD4WCxtl.png)

### [Anchor to B2B lifecycle](/docs/apps/build/b2b#b2b-lifecycle)B2B lifecycle

The following diagram shows an example lifecycle in which merchants, company contacts, Shopify, and apps interact with B2B resources:

![B2B on Shopify lifecycle diagram](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/b2b/b2b-app-flow-CnBawHV_.png)

1. A merchant creates a [company](/docs/apps/build/b2b/start-building#step-1-create-a-company), attaching details like company contacts and company locations. A merchant can also create [draft orders](/docs/apps/build/b2b/start-building#step-3-create-a-draft-order-for-a-company) for company contacts to review and approve.
2. A company contact logs in with an account that's attached to a company to select products for purchase, review draft orders, and complete checkout.
3. Shopify creates a transaction and an order for the purchase.
4. Apps use the GraphQL Admin API to create related integrations, such as order management interfaces, B2B fulfillment solutions, customer loyalty programs, and customer relationship management (CRM) tools.

---

## [Anchor to Limitations](/docs/apps/build/b2b#limitations)Limitations

* Only merchants on the [Shopify Plus](https://www.shopify.com/plus) plan can use apps with [B2B features](#features).
* Only [dev stores](https://help.shopify.com/en/partners/building-stores-for-merchants/creating-a-development-store), [Shopify Plus Partners](https://www.shopify.ca/plus/partners), and [Shopify affiliates](https://help.shopify.com/en/affiliates/about) are able to access the GraphQL Admin API's B2B resources. Shopify Plus Partners need to use a [sandbox organization](https://help.shopify.com/en/partners/dashboard/managing-stores/plus-sandbox-organizations).
* B2B doesn't support purchase options, such as [subscriptions](/docs/apps/build/purchase-options/subscriptions), [pre-orders](/docs/apps/build/purchase-options/deferred), and [try before you buy](/docs/apps/build/purchase-options/deferred).

---

## [Anchor to Developer tools and resources](/docs/apps/build/b2b#developer-tools-and-resources)Developer tools and resources

Explore the following developer tools and resources to learn more about building with B2B.

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Company object

Consult the GraphQL Admin API reference to learn more about the `Company` object.

Company object

Consult the GraphQL Admin API reference to learn more about the `Company` object.](/docs/api/admin-graphql/latest/objects/Company)

[Company object  
  

Consult the GraphQL Admin API reference to learn more about the `Company` object.](/docs/api/admin-graphql/latest/objects/Company)

[![](/images/icons/48/graphql.png)![](/images/icons/48/graphql-dark.png)

Catalog object

Consult the GraphQL Admin API reference to learn more about the `Catalog` object.

Catalog object

Consult the GraphQL Admin API reference to learn more about the `Catalog` object.](/docs/api/admin-graphql/unstable/interfaces/Catalog)

[Catalog object  
  

Consult the GraphQL Admin API reference to learn more about the `Catalog` object.](/docs/api/admin-graphql/unstable/interfaces/Catalog)

---

## [Anchor to Next steps](/docs/apps/build/b2b#next-steps)Next steps

* [Get started](/docs/apps/build/b2b/start-building) building for B2B.

---

Was this page helpful?

YesNo