---
source: https://shopify.dev/docs/apps/marketing
---

This guide describes the ways that you can help merchants with marketing their Shopify store, and provides some resources you can explore to extend your app's functionality.

---

## [Anchor to How it works](/docs/apps/build/marketing-analytics#how-it-works)How it works

After a merchant launches their store, they might want to explore options for increasing traffic and converting visitors into customers. Whether a merchant is selling online or in person, developing a marketing plan can help them to choose marketing tactics that are right for their store.

You can help merchants with marketing their Shopify stores in the following ways:

* Set up a [web pixel app extension](#web-pixel-app-extension) to collect behavioral data for marketing campaign optimization and analytics.
* Use [customer segments](#customer-segments) to conduct marketing activities.
* [Connect a marketing app to Shopify](#connecting-a-marketing-app-to-shopify) to create and manage marketing efforts in your app or on a platform outside of Shopify.
* [Manage meta tags for SEO](#meta-tags-for-seo) to help customers find an online store in search engines or social media.

---

## [Anchor to Web pixel app extension](/docs/apps/build/marketing-analytics#web-pixel-app-extension)Web pixel app extension

Pixels are JavaScript code snippets that run on the online store and collect behavioral data, referred to as [customer events](/docs/api/web-pixels-api/standard-events), for marketing campaign optimization and analytics.

Web pixel app extensions provide developers with a simplified process for managing and processing behavioral data, by loading pixels in a secure sandbox environment with APIs for subscribing to customer events. Web pixel app extensions provide the following benefits to app users and developers:

* Eliminate or minimize the need for users to add tracking code
* Securely access all surfaces, like storefront, checkout and post-purchase pages
* Control what data the developers have access to
* Avoid performance and privacy alerts
* Provide a smaller pixel code libraries with the removal of excess DOM manipulation code

For more information, refer to [Web pixels](/docs/apps/build/marketing-analytics/pixels).

---

## [Anchor to Customer segments](/docs/apps/build/marketing-analytics#customer-segments)Customer segments

![A diagram showing the relationship between a segment, segment member, and shop](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/apps/segmentation/segment-flow-DPcMOW_n.png)

A segment is a group of members (commonly customers) that meet specific criteria. Segments enable users to conduct marketing activities, access information that helps to inform a business decision, or learn more about certain segment member behaviors.

For example, a segment might include members that bought a particular product. A user could then send a targeted email to the members of that segment.

Segment members can belong to multiple segments.

For more information, refer to [Customer segments](/docs/apps/build/marketing-analytics/customer-segments).

---

## [Anchor to Connecting a marketing app to Shopify](/docs/apps/build/marketing-analytics#connecting-a-marketing-app-to-shopify)Connecting a marketing app to Shopify

You can use the GraphQL Admin API to create and manage marketing efforts in your app or on a platform outside of Shopify. By integrating with Shopify, apps can connect their data, and app users can access a complete picture of how their marketing efforts are performing.

Note

You don't need to use a [marketing activities app extension](/docs/apps/build/marketing-analytics/marketing-activities) to connect a marketing app to Shopify.

**Note:**

You don't need to use a [marketing activities app extension](/docs/apps/build/marketing-analytics/marketing-activities) to connect a marketing app to Shopify.

---

## [Anchor to Marketing automation action](/docs/apps/build/marketing-analytics#marketing-automation-action)Marketing automation action

[Shopify marketing automations](https://help.shopify.com/manual/promoting-marketing/create-marketing/create-marketing-automations) is a workflow tool that lets merchants set up marketing automations and campaigns. The Shopify marketing automations tool is built into the Shopify admin.

If you want merchants to execute your app's marketing activities based on conditions in their store, then you can create a marketing automation action. When the action is triggered, you can send information about the marketing activity back to Shopify for display and reporting purposes.

For more information, refer to [Marketing automation actions](/docs/apps/build/marketing-analytics/automations/create-marketing-automation-actions).

Note

You don't need to create a marketing activity app extension to create a marketing automation action.

**Note:**

You don't need to create a marketing activity app extension to create a marketing automation action.

---

## [Anchor to Meta tags for SEO](/docs/apps/build/marketing-analytics#meta-tags-for-seo)Meta tags for SEO

You can change the way a product, page, collection, blog, or article appears in search engine results by updating the resource's meta tags. The meta tags are the page title and the meta description, which are part of the resource's search engine listing.

For example, when you create a product, the page title and meta description for the product page defaults to the product title and description.

You can change these default values by managing metafields with the [GraphQL Admin API](/docs/api/admin-graphql/latest/objects/metafield).

For more information, refer to [Manage meta tags for SEO](/docs/apps/build/marketing-analytics/optimize-storefront-seo).

---

## [Anchor to Next steps](/docs/apps/build/marketing-analytics#next-steps)Next steps

* Learn how you can [use web pixels](/docs/apps/build/marketing-analytics/pixels) on an online store to collect behavioral data for marketing campaign optimization and analytics.
* [Use segments](/docs/apps/build/marketing-analytics/customer-segments) to conduct marketing activities.
* Use metafields to change the way a store's pages appear in search engine results by [updating the meta tags](/docs/apps/build/marketing-analytics/optimize-storefront-seo).

---

Was this page helpful?

YesNo