---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/seo
---

Optimizing Hydrogen for search engines and social media requires configuring the following things:

1. [Meta tags and descriptions](#meta-tags)
2. [sitemap.xml](#sitemap-xml)
3. [robots.txt](#robots-txt)

This guide walks you through the process of setting up each one.

Note

This isn't a comprehensive guide to SEO best practices. Check the Shopify blog for more resources on [commerce SEO](https://www.shopify.com/ca/blog/ecommerce-seo-beginners-guide).

**Note:**

This isn't a comprehensive guide to SEO best practices. Check the Shopify blog for more resources on [commerce SEO](https://www.shopify.com/ca/blog/ecommerce-seo-beginners-guide).

---

## [Anchor to Meta tags](/docs/storefronts/headless/hydrogen/seo#meta-tags)Meta tags

Hydrogen uses Remix's built-in `meta` features for SEO tags, and includes the [`getSeoMeta` utility](/docs/api/hydrogen/current/utilities/getseometa), which makes it easier and more consistent to render SEO meta tags.

Note

Remix
Check out the Remix docs on [`meta` exports](https://remix.run/docs/en/main/route/meta) for more details.

**Note:**

Remix
Check out the Remix docs on [`meta` exports](https://remix.run/docs/en/main/route/meta) for more details.

The `getSeoMeta` utility accepts SEO metadata about the current route, then renders the corresponding HTML meta tags in your document `<head>`:

9

1

2

3

4

5

export const meta = () => {

return getSeoMeta({

title: 'Example title',

});

};

9

1

2

3

4

5

6

7

<head>

<!-- ... -->

<title>Example title</title>

<meta property="og:title" content="Example title" />

<meta property="twitter:title" content="Example title" />

<!-- ... -->

</head>

##### JSX input

```liquid
export const meta = () => {
  return getSeoMeta({
    title: 'Example title',
  });
};
```

##### HTML output

```liquid
<head>
  <!-- ... -->
  <title>Example title</title>
  <meta property="og:title" content="Example title" />
  <meta property="twitter:title" content="Example title" />
  <!-- ... -->
</head>
```

It includes support for titles, descriptions, images, canonical URLs, JSON-LD and more. Check the [getSeoMeta reference](/docs/api/hydrogen/current/utilities/getseometa) for a complete list of supported features.

### [Anchor to Step 1: Import ,[object Object], and use it in your ,[object Object], exports](/docs/storefronts/headless/hydrogen/seo#step-1-import-getseometa-and-use-it-in-your-meta-exports)Step 1: Import `getSeoMeta` and use it in your `meta` exports

The SEO data you want will vary by route. For example, you'll want to render different tags on a product page versus the home page. The following example code shows how the basic pattern applies across all your storefront routes:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

import {getSeoMeta} from '@shopify/hydrogen';

// ...

export async function loader() {

return {

//...

// Return an SEO object in your loader data

seo: {

title: "Storefront name",

description: "Storefront description, including relevant keywords to help new customers find your page",

},

};

}

// Pass the loader data to the meta export

export const meta = ({data}) => {

// pass your SEO object to getSeoMeta()

return getSeoMeta(data.seo);

};

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

import {getSeoMeta} from '@shopify/hydrogen';

import {type MetaFunction} from '@react-router';

// ...

export async function loader({context}: LoaderFunctionArgs) {

return {

//...

// Return an SEO object in your loader data

seo: {

title: "Storefront name",

description: "Storefront description, including relevant keywords to help new customers find your page",

},

};

}

// Pass the loader data to the meta export

export const meta: MetaFunction<typeof loader> = ({data}) => {

// pass your SEO object to getSeoMeta()

return getSeoMeta(data.seo);

};

##### JavaScript

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader() {
   return {
     //...
     // Return an SEO object in your loader data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

// Pass the loader data to the meta export
export const meta = ({data}) => {
  // pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};
```

##### TypeScript

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
import {type MetaFunction} from '@react-router';
// ...
export async function loader({context}: LoaderFunctionArgs) {
   return {
     //...
     // Return an SEO object in your loader data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

// Pass the loader data to the meta export
export const meta: MetaFunction<typeof loader> = ({data}) => {
  // pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};
```

### [Anchor to Step 2: Merge SEO data from nested routes](/docs/storefronts/headless/hydrogen/seo#step-2-merge-seo-data-from-nested-routes)Step 2: Merge SEO data from nested routes

Often, two or more nested routes are returning SEO data. In general, you'll want to use the most specific SEO tags available for your route.

For example, if you're on the product page, you want to show a title and description of your product, not the store name and description from the root route.

The following code examples show how to return SEO data from a nested product route, then merge it with SEO data from the root route. By mapping over SEO data returned by all nested routes, The most specific SEO data "wins", overwriting SEO data from higher in the routing structure:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

import {getSeoMeta} from '@shopify/hydrogen';

// ...

export async function loader({context}) {

return {

//...

// Return basic shop SEO data

seo: {

title: "Storefront name",

description: "Storefront description, including relevant keywords to help new customers find your page",

},

};

}

export const meta = ({data}) => {

// Pass your SEO object to getSeoMeta()

return getSeoMeta(data.seo);

};

// Switch to the "Product handle route" to see how these relate

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

import {getSeoMeta} from '@shopify/hydrogen';

// ...

export async function loader({context}) {

const {product} = await context.storefront.query(/\* GraphQL query \*/);

return {

//...

// Return product SEO data

seo: {

title: product.seo.title || product.title,

description: product.seo.description || product.description,

// ...this could also include image URLs, prices, and more

},

};

}

/// Pass all product loader data to the meta export

export const meta = ({matches}) => {

// Map data from all routes. More specific SEO data from nested routes

// overrides more general SEO data from parent routes.

return getSeoMeta(...matches.map((match) => match.data.seo));

};

##### Root route

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader({context}) {
   return {
     //...
     // Return basic shop SEO data
     seo: {
       title: "Storefront name",
       description: "Storefront description, including relevant keywords to help new customers find your page",
     },
   };
 }

export const meta = ({data}) => {
  // Pass your SEO object to getSeoMeta()
  return getSeoMeta(data.seo);
};

// Switch to the "Product handle route" to see how these relate
```

##### Product handle route

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export async function loader({context}) {
   const {product} = await context.storefront.query(/* GraphQL query */);
   return {
     //...
     // Return product SEO data
     seo: {
       title: product.seo.title || product.title,
       description: product.seo.description || product.description,
       // ...this could also include image URLs, prices, and more
     },
   };
 }

/// Pass all product loader data to the meta export
export const meta = ({matches}) => {
  // Map data from all routes. More specific SEO data from nested routes
  // overrides more general SEO data from parent routes.
  return getSeoMeta(...matches.map((match) => match.data.seo));
};
```

### [Anchor to Step 3 (Optional): Intercept and override route SEO data](/docs/storefronts/headless/hydrogen/seo#step-3-optional-intercept-and-override-route-seo-data)Step 3 (Optional): Intercept and override route SEO data

You can implement your own logic inside `meta` exports to customize the SEO metadata that each route returns.

As an example, by default Hydrogen removes query parameters from canonical URLs. If you wanted to add them back, the following is an example of how you could do that:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

import {getSeoMeta} from '@shopify/hydrogen';

// ...

export const meta = ({data, location}) => {

return getSeoMeta(data.seo).map((meta) => {

if (meta.rel === 'canonical') {

return {

...meta,

// Overwrite the default value of meta.href to append the URL params

href: meta.href + location.search,

};

}

return meta;

});

};

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

import {getSeoMeta} from '@shopify/hydrogen';

import {type MetaFunction} from '@react-router';

// ...

export const meta: MetaFunction<typeof loader> = ({data, location}) => {

return getSeoMeta(data.seo).map((meta) => {

if (meta.rel === 'canonical') {

return {

...meta,

// Overwrite the default value of meta.href to append the URL params

href: meta.href + location.search,

};

}

return meta;

});

};

##### JavaScript

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
// ...
export const meta = ({data, location}) => {
  return getSeoMeta(data.seo).map((meta) => {
    if (meta.rel === 'canonical') {
      return {
        ...meta,
        // Overwrite the default value of meta.href to append the URL params
        href: meta.href + location.search,
      };
    }
    return meta;
  });
};
```

##### TypeScript

```liquid
import {getSeoMeta} from '@shopify/hydrogen';
import {type MetaFunction} from '@react-router';
// ...
export const meta: MetaFunction<typeof loader> = ({data, location}) => {
  return getSeoMeta(data.seo).map((meta) => {
    if (meta.rel === 'canonical') {
      return {
        ...meta,
        // Overwrite the default value of meta.href to append the URL params
        href: meta.href + location.search,
      };
    }
    return meta;
  });
};
```

---

## [Anchor to sitemap.xml](/docs/storefronts/headless/hydrogen/seo#sitemapxml)sitemap.xml

Hydrogen's base template includes [`sitemap.xml`](https://github.com/Shopify/hydrogen/blob/main/templates/skeleton/app/routes/%5Bsitemap.xml%5D.tsx) and [`sitemap.$type.$page.xml`](https://github.com/Shopify/hydrogen/blob/main/templates/skeleton/app/routes/sitemap.%24type.%24page%5B.xml%5D.tsx) routes by default. If your project doesn't already have these files, then you can generate them with the following Shopify CLI command:

9

1

npx shopify hydrogen generate route sitemap

By default, the sitemap files are [cached](/docs/storefronts/headless/hydrogen/caching) for 24 hours.

### [Anchor to Limitations](/docs/storefronts/headless/hydrogen/seo#limitations)Limitations

* When you add or remove pages, the sitemap is automatically updated within one day. Similarly, if you unpublish a product, then the product is removed automatically from the sitemap.

---

## [Anchor to robots.txt](/docs/storefronts/headless/hydrogen/seo#robotstxt)robots.txt

Hydrogen's base template includes a [`robots.txt` route](https://github.com/Shopify/hydrogen/blob/main/templates/skeleton/app/routes/%5Brobots.txt%5D.tsx) by default. If your project doesn't already have a `robots.txt` file, you can generate a new one with the Hydrogen CLI:

9

1

npx shopify hydrogen generate route robots

By default, Hydrogen's `robots.txt` file is [cached](/docs/storefronts/headless/hydrogen/caching) for 24 hours.

### [Anchor to robots.txt on Oxygen](/docs/storefronts/headless/hydrogen/seo#robotstxt-on-oxygen)robots.txt on Oxygen

If you [deploy to Oxygen](/docs/storefronts/headless/hydrogen/deployments), then your `robots.txt` file is only served in your public [production environment](/docs/storefronts/headless/hydrogen/environments), and only if you have a custom domain set.

If you make a non-production deployment accessible with a [shareable link](/docs/storefronts/headless/hydrogen/deployments#shareable-links) or an [auth bypass token](/docs/api/shopify-cli/hydrogen/hydrogen-deploy#flags-propertydetail-authbypasstoken), then Oxygen overrides the deployment's `robots.txt` file with a `disallow` rule for all bots and crawlers. This prevents exposing content prematurely, as well as potential SEO harm from duplicated content.

---

## [Anchor to Next steps](/docs/storefronts/headless/hydrogen/seo#next-steps)Next steps

[![](/images/icons/48/analytics.png)![](/images/icons/48/analytics-dark.png)

Track analytics with Hydrogen

Implement analytics for your Hydrogen project, with Shopify and third-party services

Track analytics with Hydrogen

Implement analytics for your Hydrogen project, with Shopify and third-party services](/docs/storefronts/headless/hydrogen/analytics)

[Track analytics with Hydrogen  
  

Implement analytics for your Hydrogen project, with Shopify and third-party services](/docs/storefronts/headless/hydrogen/analytics)

---

Was this page helpful?

YesNo