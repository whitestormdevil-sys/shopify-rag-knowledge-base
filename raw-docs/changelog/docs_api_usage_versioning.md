---
source: https://shopify.dev/docs/api/usage/versioning
---

API versioning allows Shopify to continuously evolve the platform while offering third-party developers a predictable path for feature upgrades and deprecations.

To ensure you always know about upcoming API changes, subscribe to the [developer changelog](https://shopify.dev/changelog) and always keep your contact information up to date in the Partner Dashboard.

---

## [Anchor to Versioned vs. unversioned APIs](/docs/api/usage/versioning#versioned-vs-unversioned-apis)Versioned vs. unversioned APIs

| Versioned APIs | Unversioned APIs |
| --- | --- |
| - [GraphQL Admin API](/docs/api/admin-graphql) - [Storefront API](/docs/api/storefront) - [Customer Account API](/docs/api/customer) - [Hydrogen](/docs/api/hydrogen) - [Hydrogen React](/docs/api/hydrogen-react) - [Partner API](/docs/api/partner) - [Payments Apps API](/docs/api/payments-apps) - [Checkout UI extensions](/docs/api/checkout-ui-extensions) - [Admin UI extensions](/docs/api/admin-extensions) - [POS UI extensions](/docs/api/pos-ui-extensions) - [Function APIs](/docs/api/functions) | - [Ajax API](/docs/api/ajax) - [Liquid](/docs/api/liquid) - [OAuth](/docs/apps/build/authentication-authorization) endpoints (including `AccessScope`) - Any other resources not explicitly listed as versioned |

---

## [Anchor to Release schedule](/docs/api/usage/versioning#release-schedule)Release schedule

Shopify releases a new API version every 3 months at the beginning of the quarter. Version names are date-based to be meaningful and semantically unambiguous (for example, `2023-01`). Below is an example release schedule for 2023:

| Stable version | Release date | Date stable version is supported until |
| --- | --- | --- |
| 2023-01 | January 1, 2023 | January 1, 2024 |
| 2023-04 | April 1, 2023 | April 1, 2024 |
| 2023-07 | July 1, 2023 | July 1, 2024 |
| 2023-10 | October 1, 2023 | October 1, 2024 |

Stable versions are released at 5pm UTC.

Each stable version is supported for a minimum of 12 months. This means that there are at least nine months of overlap between two consecutive stable versions. When a new stable version is introduced and contains changes that affect your app, you have nine months to test and migrate your app to the new version before support for the previous version is removed.

Tip

When a new version has an impact beyond the API, such as on the online store or the UI of the Shopify admin, a developer preview is made available in your Partner Dashboard. To learn more, see [Developer previews](/docs/api/developer-previews).

**Tip:**

When a new version has an impact beyond the API, such as on the online store or the UI of the Shopify admin, a developer preview is made available in your Partner Dashboard. To learn more, see [Developer previews](/docs/api/developer-previews).

We strongly recommend updating your apps to make requests to the latest stable API version every quarter. However, if your app uses a stable version that is no longer supported, then Shopify falls forward and responds to your request with the same behavior as the oldest supported stable version. For example, when Shopify removes `2023-07`, API requests to version `2023-07` will be served version `2023-10`, because that will be the oldest supported stable version.

If your request doesn't include a version, then the API also defaults to the oldest supported stable version. However, we do not recommend relying on this behaviour for adopting deprecated changes. As you update your app, you should specify the API version with every request. By making your app version aware, you anchor your code to a specific set of features that are guaranteed to behave in the same way for the supported timeframe.

**Example version support schedule**

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/versioning/api-release-schedule-Ccntohwl.png)


---

## [Anchor to Making requests to an API version](/docs/api/usage/versioning#making-requests-to-an-api-version)Making requests to an API version

Shopify API versions are explicitly declared in the URLs that your app makes requests to:

* GraphQL Admin API URL: `/admin/api/{api_version}/graphql.json`
* Storefront API URL: `/api/{api_version}/graphql.json`
* Payments Apps API URL: `/payments_apps/api/{api_version}/graphql.json`

For example, the following URLs make requests to version `2026-01`:

* GraphQL Admin API URL: `/admin/api/2026-01/graphql.json`
* Storefront API URL: `/api/2026-01/graphql.json`
* Payments Apps API URL: `/payments_apps/api/2026-01/graphql.json`

There are several supported versions of the APIs available, and you specify the version that you want to use by substituting the version name in the URL. There are three types of API versions: stable, release candidate, and unstable.

Shopify's API responses contain the header `X-Shopify-API-Version`, which returns the API version that was used to execute the request. When you keep your app updated, this matches the API version that's specified in your request. If the returned version is different, then your app is out of date and is using the default API version.

Note

If you're using the Admin API and writing your app in Ruby, Python or Node, then you can use the [official libraries](/docs/api) to interact with the Admin API and set the API version easily.
Additionally, if you are using any of the Storefront SDKs, note that each new released SDK sets the API version for you. To find out what version of the API is support by [each SDK version](/docs/storefronts/headless/additional-sdks) see the release notes for that version of the SDK.

Webhooks are also versioned. To learn how to select a webhook API version, see [Versioned webhooks](/docs/api/usage/versioning#webhooks).

**Note:**

If you're using the Admin API and writing your app in Ruby, Python or Node, then you can use the [official libraries](/docs/api) to interact with the Admin API and set the API version easily.
Additionally, if you are using any of the Storefront SDKs, note that each new released SDK sets the API version for you. To find out what version of the API is support by [each SDK version](/docs/storefronts/headless/additional-sdks) see the release notes for that version of the SDK.

Webhooks are also versioned. To learn how to select a webhook API version, see [Versioned webhooks](/docs/api/usage/versioning#webhooks).

---

## [Anchor to Stable API versions](/docs/api/usage/versioning#stable-api-versions)Stable API versions

Stable API versions provide a supported interface that will not change for at least a year, with the following caveats:

* GraphQL `Enum` types will retroactively add new values that represent new application features. You should assume that enums are *not* exhaustive, and integrate them into your own application logic with a catch-all clause.
* We may issue security fixes; these will be as backwards-compatible as possible while addressing a vulnerability.

Refresh schema introspection caches periodically to track these changes.

---

## [Anchor to Release candidates](/docs/api/usage/versioning#release-candidates)Release candidates

Release candidates let you see what changes are scheduled for release in the next stable version so that you can begin updating your app as early as possible. API release candidates are made available on the same date that we release our stable versions. For example, when version `2023-01` is released on January 1, 2023, the release candidate for version `2023-04` will also become available.

Both backwards-incompatible and backwards-compatible changes can be added to the release candidate so that they're available to you ahead of the stable release. For this reason, we recommend that you don't use release candidates in production.

---

## [Anchor to Unstable API versions](/docs/api/usage/versioning#unstable-api-versions)Unstable API versions

There is always an unstable version of the APIs available. The unstable versions contain features and changes that are still in progress, and we make backwards-incompatible and backwards-compatible changes to them regularly. Generally, changes appear in the unstable version before a stable release, but there is no guarantee that changes in the unstable version will eventually be released. A feature might be added to an unstable version but then be removed later.

You can use the unstable API versions to test new changes and features early, but you should not use them in production.

For example, you can use the following API URLs to make requests to the unstable API:

* GraphQL Admin API request: `https://{shop}.myshopify.com/admin/api/unstable/graphql.json`
* Storefront API request: `https://{shop}.myshopify.com/api/unstable/graphql.json`
* Payments Apps API request: `https://{shop}.myshopify.com/payments_apps/api/unstable/graphql.json`

---

## [Anchor to Deprecation practices](/docs/api/usage/versioning#deprecation-practices)Deprecation practices

Part of a Shopify API can be deprecated if it becomes unnecessary, unsafe, or outdated. It's marked as deprecated when it's removed in a newer version of the API. The deprecation is then retroactively applied to previous stable versions of the API. When a deprecation is introduced, any further details and any relevant migration information is announced in the [developer changelog](https://shopify.dev/changelog).

Because each version is supported for a minimum of a year, there are always at least 9 months of overlap between versions for you to update your app to support deprecations.

### [Anchor to Removing parts of a Shopify API](/docs/api/usage/versioning#removing-parts-of-a-shopify-api)Removing parts of a Shopify API

Any fields or types that have been deprecated in a release will be removed in a subsequent release. For example, a field that's deprecated in `2023-07` might be removed in `2023-10`.

### [Anchor to Apps using deprecated resources](/docs/api/usage/versioning#apps-using-deprecated-resources)Apps using deprecated resources

![Screenshot of user warnings for unsupported apps](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/versioning/oauth-warning-eQmRzHFk.png)

If a public app or sales channel continues to use unsupported resources after the upgrade deadline, it will be delisted from the Shopify App Store. Also, users who install an unsupported public app, unsupported custom app, or unsupported sales channel will see a warning during the installation process.

![Screenshot of user installs blocked for unsupported apps](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/versioning/oauth-blocked-WwJ_aTxm.png)

If your app continues to use unsupported API resources, users will be blocked from installing the app for a minimum of seven days.

![Screenshot of user warnings with unsupported apps installed](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/versioning/app-status-notifications-C2jnwy84.png)

In the Shopify admin, users will see warning messages indicating that the app is unsupported. These warnings are shown to users only if the app makes calls to unsupported resources after the upgrade deadline. Warnings are removed seven days after the last use of unsupported resources is detected. Warnings can't be manually removed by you or by the user.

Warning

If you use the Shopify API in a standalone app that requires updates, such as a desktop app or mobile app, then your users will need to update before the upgrade deadline to ensure their app continues working. This might mean you'll have to update well ahead of the migration deadline, so that your users then have time to update their apps. Any calls to unsupported resources could result in your app being delisted or users being warned about or blocked from installing your app.

**Warning:**

If you use the Shopify API in a standalone app that requires updates, such as a desktop app or mobile app, then your users will need to update before the upgrade deadline to ensure their app continues working. This might mean you'll have to update well ahead of the migration deadline, so that your users then have time to update their apps. Any calls to unsupported resources could result in your app being delisted or users being warned about or blocked from installing your app.

### [Anchor to Deprecation practices](/docs/api/usage/versioning#deprecation-practices)Deprecation practices

When Shopify deprecates a field in a GraphQL API, the change is communicated in one or more of the following ways:

* The [API health report](/docs/api/usage/versioning/api-health) lists which resources require changes.
* A deprecation warning for the field is shown in API client tools, such as Shopify's [GraphQL Explorer](/docs/api/usage/api-exploration/admin-graphiql-explorer):

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/guides/graphiql-deprecation-warning-CIEoF1sI.png)

* A notice about the deprecation is posted in the the [developer changelog](https://shopify.dev/changelog).
* The API reference is updated to identify the deprecated fields and applicable alternatives.
* If there is an imminent backwards-incompatible change that affects your app, then the [emergency developer contact](/docs/api/usage/versioning/updates) for your app might be contacted about the deprecation.

---

## [Anchor to Webhooks](/docs/api/usage/versioning#webhooks)Webhooks

Webhook payloads can change between API versions, similar to API response payloads. You can select the API version that you want to use for webhooks, and that version will be used for all webhooks that are sent to your app.

When your selected API version becomes unsupported, Shopify falls forward to using the next supported stable version. Webhooks include the `X-Shopify-Api-Version` request header to indicate the API version that was used to generate the webhook. If this value is different than the version that you selected, then your selected API version is no longer supported.

When your app is affected by the webhook changes in a newer API version, you should update your app before support for your selected API version is removed.

Learn more about [managing webhook versions](/docs/apps/build/webhooks).

---

Was this page helpful?

YesNo