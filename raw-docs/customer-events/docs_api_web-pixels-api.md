---
source: https://shopify.dev/docs/api/web-pixels-api
---

# Web Pixels API

The Web Pixels API gives you access to a set of controlled APIs for accessing browser APIs and subscribing to customer events, within one of our Lax or Strict sandboxes.

Ask assistant

## [Anchor to App Web Pixels](/docs/api/web-pixels-api#app-web-pixels)App Web Pixels

For app developers integrating app web pixels, pixels are loaded in a strict sandbox. To initialize the web pixel extension API you can import the `@shopify/web-pixels-extension package` for stronger typing and register your pixel. Once initialized, the `api` object (the **Standard API**) has access to the following properties:

* [`analytics`](/docs/api/web-pixels-api/standard-api/analytics): Provides access to Shopify's customer event API
* [`browser`](/docs/api/web-pixels-api/standard-api/browser): Provides access to specific browser methods that asynchronously execute in the top frame (cookie, localStorage, sessionStorage)
* [`init`](/docs/api/web-pixels-api/standard-api/init): A JSON object containing a snapshot of the page at time of page render.
  + Contains a context field that provides the Context of the page at the time of page render
  + Contains a data field that provides access to the Cart and Customer objects at the time of page render
* [`settings`](/docs/api/web-pixels-api/standard-api/settings): Provides access to the settings JSON object as set by the [GraphQL Admin API](https://shopify.dev/docs/apps/marketing/pixels/getting-started#step-5-create-a-web-pixel-setting-for-the-store) (Web pixel app extensions only)

To learn more about these Standard API properties, or how to create app pixels, please view the following documentation.

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceStandard API

API Reference

Standard API](/docs/api/web-pixels-api/standard-api)

[API Reference - Standard API](/docs/api/web-pixels-api/standard-api)

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

API ReferenceApp Pixel Tutorial

API Reference

App Pixel Tutorial](https://shopify.dev/docs/apps/marketing/pixels/getting-started)

[API Reference - App Pixel Tutorial](https://shopify.dev/docs/apps/marketing/pixels/getting-started)

[![](/images/icons/32/gear.png)![](/images/icons/32/gear-dark.png)

API ReferenceApp Pixel FAQ

API Reference

App Pixel FAQ](https://help.shopify.com/en/manual/promoting-marketing/pixels/app-pixels)

[API Reference - App Pixel FAQ](https://help.shopify.com/en/manual/promoting-marketing/pixels/app-pixels)

---

## [Anchor to Custom Web Pixels](/docs/api/web-pixels-api#custom-web-pixels)Custom Web Pixels

Custom Pixels are loaded within a lax sandbox and configured within the pixel manager interface in the Shopify admin. For this developer interface, the `analytics`, `browser` and the `init` variables on the `api` object have already been deconstructed for you, and you can call them without having to write any additional boilerplate code.

Unavailable Settings Property

Unlike with App Pixels, custom pixels do not have access to the `settings` property

**Unavailable Settings Property:**

Unlike with App Pixels, custom pixels do not have access to the `settings` property

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceStandard API

API Reference

Standard API](/docs/api/web-pixels-api/standard-api)

[API Reference - Standard API](/docs/api/web-pixels-api/standard-api)

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

API ReferenceCustom Pixel Tutorial

API Reference

Custom Pixel Tutorial](https://help.shopify.com/en/manual/promoting-marketing/pixels/custom-pixels)

[API Reference - Custom Pixel Tutorial](https://help.shopify.com/en/manual/promoting-marketing/pixels/custom-pixels)

---

## [Anchor to Customer Events Reference](/docs/api/web-pixels-api#customer-events-reference)Customer Events Reference

After setting up your App Pixel or Custom Pixel, you can use these pixels to subscribe to additional customer events.
We publish and maintain a list of commonly used standard events such as `page_viewed`, `product_viewed` and checkout progression events.

If you would like additional events not covered by our list, you can create, publish and subscribe to your own custom events.

To subscribe to
multiple events at once you can use: `all_events`, `all_standard_events`, `all_custom_events`, `all_dom_events`. Please take note that
the contents of these event subscriptions are subject to change as events are added or modified. Please view the following documentation for
more details about customer events:

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceStandard Events

API Reference

Standard Events](/docs/api/web-pixels-api/standard-events)

[API Reference - Standard Events](/docs/api/web-pixels-api/standard-events)

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceCustom Events

API Reference

Custom Events](/docs/api/web-pixels-api/emitting-data)

[API Reference - Custom Events](/docs/api/web-pixels-api/emitting-data)

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceDOM Events

API Reference

DOM Events](/docs/api/web-pixels-api/dom-events)

[API Reference - DOM Events](/docs/api/web-pixels-api/dom-events)

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferenceAdvanced DOM Events

API Reference

Advanced DOM Events](/docs/api/web-pixels-api/advanced-dom-events)

[API Reference - Advanced DOM Events](/docs/api/web-pixels-api/advanced-dom-events)

[![](/images/icons/32/blocks.png)![](/images/icons/32/blocks-dark.png)

API ReferencePixel Privacy

API Reference

Pixel Privacy](/docs/api/web-pixels-api/pixel-privacy)

[API Reference - Pixel Privacy](/docs/api/web-pixels-api/pixel-privacy)

---

Was this page helpful?

YesNo