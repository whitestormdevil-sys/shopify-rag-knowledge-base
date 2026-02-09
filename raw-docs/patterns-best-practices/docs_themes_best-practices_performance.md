---
source: https://shopify.dev/docs/themes/best-practices/performance
---

Performance is an important factor for merchants when they choose a theme for their online store. When you build or customize a theme, you should build with performance in mind. Optimizing your theme for performance is key to the success of the merchants that you support and to the experiences of their customers. Performance directly influences [conversion rates](https://www.shopify.com/enterprise/site-performance-page-speed-ecommerce), repeat business, and [search engine rankings](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html).

When a theme is submitted to the [Shopify Theme Store](/docs/storefronts/themes/store), the theme's tested on a benchmark shop to determine its performance score. To be accepted into the Shopify Theme Store, a theme must have a minimum average lighthouse performance score of 60 across the home page, product page, and collection page. You can run a similar test on your theme using a [development store](#run-a-lighthouse-audit-using-shopify-data).

[Learn more about performance testing for themes in the Shopify Theme Store](/docs/storefronts/themes/store/requirements#6-lighthouse-performance-and-accessibility).

Note

Shopify built [Dawn](https://github.com/Shopify/dawn) with performance in mind. You can explore the Dawn repository to see how Shopify applies these principles.

**Note:**

Shopify built [Dawn](https://github.com/Shopify/dawn) with performance in mind. You can explore the Dawn repository to see how Shopify applies these principles.

---

## [Anchor to Optimizing for performance](/docs/storefronts/themes/best-practices/performance#optimizing-for-performance)Optimizing for performance

Consider the following best practices for optimizing the performance of your theme.

### [Anchor to Optimize your JavaScript](/docs/storefronts/themes/best-practices/performance#optimize-your-javascript)Optimize your JavaScript

Optimize the JavaScript in your theme using the following principles.

#### [Anchor to Reduce JavaScript usage](/docs/storefronts/themes/best-practices/performance#reduce-javascript-usage)Reduce JavaScript usage

Consider building your theme using primarily HTML and CSS. JavaScript shouldn't be required for the basic functionality of your theme, such as finding or purchasing products. Instead, you should only use JavaScript as a progressive enhancement, and only where there is no HTML or CSS solution available.

CSS parses and renders much faster than JavaScript, so wherever possible, you should use CSS features for building interactivity. You can find more information on the internet by searching the phrase "using CSS instead of JavaScript". One example is the blog [5 things you can do with CSS instead of JavaScript](https://blog.logrocket.com/5-things-you-can-do-with-css-instead-of-javascript/) by Juan Martín García.

Your minified JavaScript bundle size should be 16 KB or less. Shopify [automatically minifies](/docs/storefronts/themes/best-practices/performance/platform#minification) JavaScript when it's requested by the storefront.

#### [Anchor to Avoid namespace collisions](/docs/storefronts/themes/best-practices/performance#avoid-namespace-collisions)Avoid namespace collisions

Namespaces allow you to place variables into unique containers so that you can prevent collisions in the global scope. However, JavaScript minifiers rename JavaScript variables to be shorter, which can cause collisions.

To avoid namespace collisions in the global scope, wrap JavaScript values in a `function` scope. Values defined in a `function` scope are available only within the scope of that function, so there's no risk of collision with other variables that are defined on the global scope.

The following example shows you how to wrap minified and renamed JavaScript variables in a `function` scope:

9

1

2

3

(function () {

var a; function b() {}

})();

For example, the [Immediately Invoked Function Expression](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) (IIFE) pattern is a JavaScript function that runs as soon as it's defined. The IIFE pattern ensures that script-defined values are scoped to the function that the IIFE creates, so there isn't a risk of values colliding in the global namespace.

Note

Scripts injected in themes should always be wrapped in an IIFE to prevent global namespace collisions.

**Note:**

Scripts injected in themes should always be wrapped in an IIFE to prevent global namespace collisions.

#### [Anchor to Reduce your dependency on external frameworks and libraries](/docs/storefronts/themes/best-practices/performance#reduce-your-dependency-on-external-frameworks-and-libraries)Reduce your dependency on external frameworks and libraries

If you need to use JavaScript, consider avoiding introducing third-party frameworks, libraries, and dependencies. Instead, use native browser features and modern DOM APIs whenever possible. Including JavaScript libraries in your package can lead to large bundle sizes, slow load times, and a poor experience for customers. Frameworks such as React, Angular, and Vue, and large utility libraries such as jQuery have significant performance costs. Avoid introducing polyfill libraries for very old browsers (anything that doesn't support `async`/`await`). If you use a [browserslist](https://github.com/browserslist/browserslist), then you can target browsers with a > 1% marketshare.

#### [Anchor to Avoid parser-blocking scripts](/docs/storefronts/themes/best-practices/performance#avoid-parser-blocking-scripts)Avoid parser-blocking scripts

Parser-blocking scripts block the construction and rendering of the DOM until the script is loaded, parsed, and executed. They also create congestion on the network and significantly delay page rendering. This impacts metrics like [First Contentful Paint](https://web.dev/fcp/) and [Largest Contentful Paint](https://web.dev/lcp/). Use `defer` or `async` attributes on your script tags to avoid this.

### [Anchor to Preload key resources, defer or avoid loading others](/docs/storefronts/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others)Preload key resources, defer or avoid loading others

Preloading resources allows the browser to download resources before they are discovered. Choosing to load some resources later and using system resources helps you to reduce the size of the initial package of resources that needs to be downloaded before a customer can meaningfully interact with the page.

#### [Anchor to Use resource hints to preload key resources](/docs/storefronts/themes/best-practices/performance#use-resource-hints-to-preload-key-resources)Use resource hints to preload key resources

You can add up to two resource hints to your code per template by using one of the following:

* The [`preload_tag`](/docs/api/liquid/filters/preload_tag) filter
* The `preload` keyword argument on the [`stylesheet_tag`](/docs/api/liquid/filters/stylesheet_tag) or [`image_tag`](/docs/api/liquid/filters#image_tag) filters

When Shopify renders a page with preload instructions, it will send a preload resource hint as a Link header on subsequent requests.

You should use resource hints sparingly. For example, consider preloading only render-blocking stylesheets that are needed for initial functionality of the page, such as above-the-fold content.

#### [Anchor to Lazy load below-the-fold images](/docs/storefronts/themes/best-practices/performance#lazy-load-below-the-fold-images)Lazy load below-the-fold images

Load images only when they're needed on a page, and consider using placeholders until customers scroll down the page. This can also help with perceived performance as the page looks like it's loading quicker than it actually is. Rather than using a library, you should pass a `loading: 'lazy'` attribute to your image tag using the [`image_tag` filter](/docs/api/liquid/filters/image_tag):

9

1

{{ settings.favicon | image\_url: width: 200 | image\_tag: loading: 'lazy' }}

Anything that appears above the fold shouldn't be lazy-loaded. Above-the-fold content is the content a viewer sees on page load before they scroll down the page. Above-the-fold resources should be considered critical assets, and should be loaded normally.

Info

For a more complex example using responsive images, refer to [Use responsive images](#use-responsive-images).

**Info:**

For a more complex example using responsive images, refer to [Use responsive images](#use-responsive-images).

#### [Anchor to Load non-critical resources on interaction](/docs/storefronts/themes/best-practices/performance#load-non-critical-resources-on-interaction)Load non-critical resources on interaction

Your page might contain code for a component or resource that isn't always used. You can load these resources using an [import on interaction](https://addyosmani.com/blog/import-on-interaction/) pattern to avoid loading, parsing, and executing unnecessary code.

#### [Anchor to Consider using a system font](/docs/storefronts/themes/best-practices/performance#consider-using-a-system-font)Consider using a system font

Using a [system font](/docs/storefronts/themes/architecture/settings/fonts#system-fonts) avoids the client needing to download another resource before the online store's text can be rendered.

### [Anchor to Host assets on Shopify servers](/docs/storefronts/themes/best-practices/performance#host-assets-on-shopify-servers)Host assets on Shopify servers

Deliver as much as you can from the Shopify content delivery network (CDN). Using the same host for your assets avoids unnecessary HTTP connections and allows the server to prioritize delivery of blocking resources using HTTP/2 prioritization.

In a Shopify context, you can do this by adding your assets to the theme's [/assets](/docs/storefronts/themes/architecture#assets) folder, either manually by using the [GitHub Integration](/docs/storefronts/themes/tools/github), or by using the `Asset` [REST Admin API resource](/docs/api/admin-rest/latest/resources/asset). You can create links to these assets using [URL filters](/docs/api/liquid/filters/hosted_file-filters). [Learn more about the Shopify CDN](/docs/storefronts/themes/best-practices/performance/platform).

### [Anchor to Use responsive images](/docs/storefronts/themes/best-practices/performance#use-responsive-images)Use responsive images

Viewing large images on a small device can be frustrating and can slow down page load speed. Using responsive images automatically resizes them to fit the device screen that customers are using.

Specifying an image size ensures that you download the smallest possible image without degrading quality. The storefront requests the image size that's going to be displayed, and then cuts down the file size downloaded from the CDN. This reduces reliance on browser-side scaling.

You can add responsive images to your theme by using the [`image_tag` filter](/docs/api/liquid/filters/image_tag). This filter returns a srcset for the image using a smart default set of widths. You can adjust the srcset sizes that the filter returns using the `sizes` keyword argument.

9

1

{{ product.featured\_image | image\_url: width: 2000 | image\_tag }}

9

1

2

3

4

5

6

7

8

9

<img

src="/content/assets/images//cdn.shopify.com/s/files/1/0251/7476/9720/files/.png?v=1580676830&amp;width=2000"

alt=""

srcset="//cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=352 352w,

//cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=832 832w,

//cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=1200 1200w,

//cdn.shopify.com/s/files/1/0251/7476/9720/files/teal-polo.png?v=1580676830&amp;width=1920 1920w"

width="2000"

height="2007" />

### [Anchor to Optimize Liquid code](/docs/storefronts/themes/best-practices/performance#optimize-liquid-code)Optimize Liquid code

You can edit almost all of the Liquid that is used to render your store. There are efficient and inefficient ways of writing Liquid code. Doing complex operations repeatedly can increase your Liquid render time, which impacts your overall store speed.

For example, if you want to order the products in a collection by price, you should do that before you loop through the products in your collection, and not as part of the loop code. This is because the order of the products does not change for each product, and calculating the order of the products adds processing time to the request.

Run the [Shopify Theme Inspector for Chrome](/docs/storefronts/themes/tools/theme-inspector) to identify the lines of code that are slowing down pages in your online store. Read a walkthrough of analyzing your Liquid using this tool [on the Shopify Engineering blog](https://shopify.engineering/in-depth-liquid-render-analysis-shopify-theme-inspector-chrome-extension).

### [Anchor to Use Theme Check to identify performance issues](/docs/storefronts/themes/best-practices/performance#use-theme-check-to-identify-performance-issues)Use Theme Check to identify performance issues

You can use [Theme Check](/docs/storefronts/themes/tools/theme-check/configuration) to identify possible performance issues in your theme code, including large CSS and JS bundles, references to remote assets, and parser-blocking JavaScript. [Learn more about Theme Check](/docs/storefronts/themes/tools/theme-check/configuration).

---

## [Anchor to Testing for performance](/docs/storefronts/themes/best-practices/performance#testing-for-performance)Testing for performance

Shopify offers a [Web Performance Dashboard & Reports](https://help.shopify.com/en/manual/online-store/web-performance/performance-reports) that helps you to understand the performance of your store. This tool helps you can understand how your store performs across industry standards for loading speed, interactivity, and visual stability, better known as [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals). The Web Performance Dashboard & Reports is calculated using [Real User Monitoring (RUM)](https://web.dev/articles/vitals-measurement-getting-started) data and aims to provide you with a reliable performance signal and actionable insights on how to improve.

Note

The following queries are currently available only in the `unstable` version of the GraphQL Admin API.

**Note:**

The following queries are currently available only in the `unstable` version of the GraphQL Admin API.

You also have access to [PerformanceMetrics](https://shopify.dev/docs/api/admin-graphql/unstable/queries/performanceMetrics) and [PerformanceEvents](https://shopify.dev/docs/api/admin-graphql/unstable/queries/performanceEvents) to obtain web performance metric data and Shopify event data.

Info

Learn more about [web performance and core web vitals](https://performance.shopify.com/pages/getting-started-with-performance).

**Info:**

Learn more about [web performance and core web vitals](https://performance.shopify.com/pages/getting-started-with-performance).

Since real user data is needed here, you may still choose to use [Lighthouse performance scores](https://web.dev/performance-scoring/) on shops with no / low traffic. You can run Lighthouse audits manually or using CI, or you can review the speed scores of stores that you manage.

### [Anchor to Run a Lighthouse audit using Shopify data](/docs/storefronts/themes/best-practices/performance#run-a-lighthouse-audit-using-shopify-data)Run a Lighthouse audit using Shopify data

Use the following process to emulate the tests that Shopify runs to determine an online store's speed score. Shopify runs a similar test against themes before they are accepted into the [Shopify Theme Store](/docs/storefronts/themes/store). You can run a similar test against your theme to understand how it performs.

1. Create a [development store](/docs/storefronts/themes/tools/development-stores).
2. [Import](https://help.shopify.com/manual/products/import-export/import-products) the [test product csv](/csv/theme-performance-shop-product-data.csv) to the store. The store should have no other collections, products, or variants.
3. In your development store, beside **Online Store**, click the eye icon to preview your store.
4. From the preview URL, copy the value of the `_bt` parameter.

   If your preview URL doesn't have a `_bt` parameter, then your development store might have been created before August 2020. To learn how to find a preview URL for these stores, refer to [Development stores created before August 2020](#development-stores-created-before-august-2020).
5. Get the URLs for the pages that you want to audit. You should test the home page (*h*), any product page (*p*), and any collection page (*c*).
6. Append your theme's `_bt` value to the end of each URL.

   For example, the url `https://{shop}.myshopify.com/products/sunglasses` becomes `https://{shop}.myshopify.com/products/sunglasses?_bt=value-you-copied`.
7. Visit [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/#devtools), and follow the steps to run a report for each of your pages. Note the mobile score for each page.
8. Apply this formula to your results: [(*p* \* 31) + (*c* \* 33) + (*h* \* 13)] / 77. The result is your theme's speed score.

#### [Anchor to Development stores created before August 2020](/docs/storefronts/themes/best-practices/performance#development-stores-created-before-august-2020)Development stores created before August 2020

If your development store was created before August 2020, then follow these steps to get preview links to test:

1. On the **Themes** page of your development store, choose the theme that you want to test.
2. Click **Actions** > **Preview**. A preview of the theme opens.
3. At the bottom right of the page, in the preview bar, click **Share Preview**. A modal will open with your preview url.
4. In the modal, click **Copy link**.
5. For each page that you want to test, replace the base URL with the preview URL.

   For example, to test the `sunglasses` product, you might change the URL from `https://{shop}.myshopify.com/products/sunglasses` to `https://12345678.shopifypreview.com/products/sunglasses`.

Info

You can repeat this process multiple times and use the median of the scores to get a more accurate result.

**Info:**

You can repeat this process multiple times and use the median of the scores to get a more accurate result.

### [Anchor to Use Lighthouse CI to catch performance issues early](/docs/storefronts/themes/best-practices/performance#use-lighthouse-ci-to-catch-performance-issues-early)Use Lighthouse CI to catch performance issues early

If you use a continuous integration (CI) process for your themes during development, then you can add a CI check to make sure that changes to your theme code don't have a significant negative impact to your performance score. You can do so using [the Shopify Lighthouse CI GitHub action](/docs/storefronts/themes/tools/lighthouse-ci), a Shopify-developed GitHub action that uploads your theme code to a benchmark shop and then measures and calculates your speed score.

---

## [Anchor to Next steps](/docs/storefronts/themes/best-practices/performance#next-steps)Next steps

* [Learn about theme accessibility best practices](/docs/storefronts/themes/best-practices/accessibility)
* [Submit your theme to the Shopify Theme Store](/docs/storefronts/themes/store)

---

Was this page helpful?

YesNo