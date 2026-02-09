---
source: https://shopify.dev/docs/themes/best-practices/performance/platform
---

Learn about the infrastructure that Shopify provides to make the online store, and your theme, faster.

---

## [Anchor to Shopify CDN](/docs/storefronts/themes/best-practices/performance/platform#shopify-cdn)Shopify CDN

Shopify provides merchants a world class content delivery network (CDN) backed by [Cloudflare](https://cloudflare.com/). Using a CDN means that your online store will load quickly around the globe.

Files delivered over the Shopify CDN are minified and compressed automatically using [Brotli](https://github.com/google/brotli) and [gzip](https://en.wikipedia.org/wiki/Gzip), reducing the size of the files the browser must download. Requests use [HTTP/3](https://developers.cloudflare.com/http3/) and [TLS 1.3](https://www.cloudflare.com/learning-resources/tls-1-3/) to further enhance request performance and security.

Most asset URLs are rendered using the domain `cdn.shopify.com`. In certain cases, such as images or stylesheets loaded on a storefront, assets are loaded using the storefront domain, in the format `{shop}.myshopify.com/cdn`. This is done to improve performance by maximizing connection reuse in the browser.

### [Anchor to Short delays for images in your store](/docs/storefronts/themes/best-practices/performance/platform#short-delays-for-images-in-your-store)Short delays for images in your store

Using a CDN means that all of your online store images are cached at thousands of servers around the world. When you make changes to your images, Shopify informs the CDN that the images have changed. To do this, Shopify uses the [`asset_url`](/docs/api/liquid/filters/asset_url) filter, which automatically appends version numbers to all of the URLs that it generates. For example, a version number appended to the end of a URL might look like this: `?v=1384022871`.

If you link to an image without using the `asset_url` filter and upload a new version of the same image, then the image on your online store might not change to the new version for a day or more.

Supported query parameters

Only specific query parameters are recognized for versioning. The supported format uses the `v` parameter for version (for example, `?v=1384022871`). Query parameters that aren't on the allowlist, such as appending a raw timestamp value without the `v=` prefix or using arbitrary parameter names, won't bust the cache.

**Supported query parameters:**

Only specific query parameters are recognized for versioning. The supported format uses the `v` parameter for version (for example, `?v=1384022871`). Query parameters that aren't on the allowlist, such as appending a raw timestamp value without the `v=` prefix or using arbitrary parameter names, won't bust the cache.

### [Anchor to CSS syntax to ensure automatic updates](/docs/storefronts/themes/best-practices/performance/platform#css-syntax-to-ensure-automatic-updates)CSS syntax to ensure automatic updates

If you reference an image directly in your CSS, then the URL will be static and won't carry the asset version that Shopify updates automatically.

To make sure that your images are automatically updated, change your CSS syntax to include the [`asset_url`](/docs/api/liquid/filters/asset_url) filter.

For example, if your CSS looks like this:

9

1

background: url(bg.gif);

then change it to look like this:

9

1

background: url({{ 'bg.gif' | asset\_url }});

---

## [Anchor to Server-side rendering](/docs/storefronts/themes/best-practices/performance/platform#server-side-rendering)Server-side rendering

Storefront Renderer (SFR) is a server-side renderer that handles storefront requests. SFR is dedicated to serving storefront requests as fast as possible.

Our storefront renderer significantly improves performance for cache misses - instances where a page or other requested data isn't found in the cache memory and has to be retrieved from other cache levels or the main memory.

---

## [Anchor to Minification](/docs/storefronts/themes/best-practices/performance/platform#minification)Minification

Shopify automatically minifies CSS files, as well as JavaScript files that use valid syntax to ES5, when they're requested by the storefront. Minified JavaScript and CSS files are cached until the next time the file is updated.

Minification allows the browser to download less data, resulting in shorter load times.

Shopify delivers the original version of a JavaScript or CSS file if it meets one of the following criteria:

* The minified file would be larger than the original file. This might happen if a file is already minified with better compression.
* It has the extension `.min.js` or `.min.css`.

Tip

Minification might remove debugger statements from code. To debug your code, you can temporarily change your file extension to `.min.js` or `.min.css`.

**Tip:**

Minification might remove debugger statements from code. To debug your code, you can temporarily change your file extension to `.min.js` or `.min.css`.

---

## [Anchor to Speculation rules](/docs/storefronts/themes/best-practices/performance/platform#speculation-rules)Speculation rules

To improve buyer experience on Shopify stores, Shopify automatically injects [speculation rules](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API) in [supporting browsers](https://developer.mozilla.org/docs/Web/API/Speculation_Rules_API#html.elements.script.type.speculationrules).

The rules we output aim to provide largest speed gains without introducing issues with data usage, caching, or analytics. Themes can add extra rules of their own based on specific requirements and opportunities.

---

## [Anchor to Polyfills](/docs/storefronts/themes/best-practices/performance/platform#polyfills)Polyfills

Shopify automatically includes the [`es-module-shims`](https://github.com/guybedford/es-module-shims) polyfill library in the storefront when needed. This library enhances compatibility for modern JavaScript module features, primarily [**import maps**](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/script/type/importmap), across different browsers.

Import maps are a standard web platform feature allowing developers to control how JavaScript modules are resolved, similar to server-side package managers. While widely supported in the latest versions of major browsers, older browser versions might lack native support for import maps or other newer module features that `es-module-shims` polyfills, such as using [multiple import maps](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/script/type/importmap#browser_compatibility) in the same document.

In your theme code, you can use features like `<script type="importmap">` tags and standard `<script type="module">` tags without needing to manage browser-specific compatibility concerns for module loading yourself. Shopify ensures this polyfill is included and will maintain it as long as necessary to support a reasonable range of browser versions used by buyers.

Tip

If possible, rely on this platform-provided polyfill for import map functionality. Avoid loading a separate version of `es-module-shims` or similar polyfills, as this could lead to conflicts or unnecessary overhead.

**Tip:**

If possible, rely on this platform-provided polyfill for import map functionality. Avoid loading a separate version of `es-module-shims` or similar polyfills, as this could lead to conflicts or unnecessary overhead.

---

## [Anchor to Pagination limits](/docs/storefronts/themes/best-practices/performance/platform#pagination-limits)Pagination limits

Shopify limits pagination of arrays of objects to 25,000 objects. Pagination deep into large arrays is resource intensive and can slow down other requests. To keep all requests performant a limit of 25,000 was put in place that balances performance with practical use-cases.

Pagination above 25,000 items suggest a more suitable design can be found to help buyers narrow down their search to a manageable amount of items before paging through all results. If you're finding yourself constrained by this limitation [see how you can add filters to your shop](https://help.shopify.com/en/manual/online-store/search-and-discovery/filters).

This limit is also enforced on count queries. Counts are accurate up to 25,000 items. For arrays with more items 25,001 is returned as the count signaling that there are more than 25,000 items in the array.

---

Was this page helpful?

YesNo