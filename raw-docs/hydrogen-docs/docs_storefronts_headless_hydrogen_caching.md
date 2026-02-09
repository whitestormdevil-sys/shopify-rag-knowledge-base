---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/caching
---

Hydrogen and Oxygen provide built-in caching to speed up Hydrogen storefronts. The caching API is based on the web-standard [`Cache-Control` API](#cache-control-api).

By default, Hydrogen automatically caches [Storefront API](/docs/api/storefront) data when using Hydrogen’s built-in API client. You can customize or disable caching behavior for every request. You can optionally extend Hydrogen’s built-in utilities to [cache data from third-party APIs](/docs/storefronts/headless/hydrogen/caching/third-party).

Customer Account API data is never cached, because it’s personalized for each user.

---

## [Anchor to Caching strategies](/docs/storefronts/headless/hydrogen/caching#caching-strategies)Caching strategies

Hydrogen includes recommended caching strategies to help you determine which cache control header to set. The following table lists the available caching strategies and their associated cache control headers and cache durations:

| Caching strategy | Cache control header | Cache duration |
| --- | --- | --- |
| `CacheShort()` | `public, max-age=1, stale-while-revalidate=9` | 10 seconds |
| `CacheLong()` | `public, max-age=3600, stale-while-revalidate=82800` | 1 day |
| `CacheNone()` | `no-store` | No cache |
| `CacheCustom()` | Define your own cache control header | Custom |

### [Anchor to Default caching strategy](/docs/storefronts/headless/hydrogen/caching#default-caching-strategy)Default caching strategy

By default, each sub-request applies a strategy with the following cache options, which revalidates data after one second and caches it for up to one day:

9

1

public, max-age=1, stale-while-revalidate=86399

---

## [Anchor to Subrequest caching](/docs/storefronts/headless/hydrogen/caching#subrequest-caching)Subrequest caching

You can configure the caching strategy for Storefront API data by passing a `cache` option with your query.

The following simplified example shows a component that displays product titles. Because titles don't change often, it caches the data using the `CacheLong()` strategy.

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

22

23

24

25

26

import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({params, context}) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

// Product titles change less often, so they can be cached with CacheLong().

cache: storefront.CacheLong()

});

return {product};

}

export default function Product() {

const {product} = useLoaderData();

return (

<h1>{product.title}</h1>

)

}

const PRODUCT\_QUERY = `#graphql

product(handle: $handle) {

id

title

}`

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

22

23

24

25

26

27

28

29

import {useLoaderData} from '@react-router';

import type { LoaderArgs } from '@shopify/remix-oxygen';

import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

// Product titles change less often, therefore CacheLong().

cache: storefront.CacheLong()

});

return {product};

}

export default function Product() {

const {product} = useLoaderData<typeof loader>();

return (

<h1>{product.title}</h1>

)

}

const PRODUCT\_QUERY = `#graphql

product(handle: $handle) {

id

title

}

`

##### JavaScript

```liquid
import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;

  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Product titles change less often, so they can be cached with CacheLong().
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }`
```

##### TypeScript

```liquid
import {useLoaderData} from '@react-router';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;

  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Product titles change less often, therefore CacheLong().
    cache: storefront.CacheLong()
  });
  return {product};
}

export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return (
    <h1>{product.title}</h1>
  )
}

const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    id
    title
  }
`
```

---

## [Anchor to Custom caching strategies](/docs/storefronts/headless/hydrogen/caching#custom-caching-strategies)Custom caching strategies

If you don't want to use the [caching strategies](#caching-strategies) built into Hydrogen, then you can create your own with the `CacheCustom()` function. This function accepts options compatible with the [Cache-Control API](#cache-control-api).

The following strategy directs clients to revalidate the cached data when it’s no longer fresh, not to transform the data, and to consider it fresh for a maximum of 30 seconds:

9

1

2

3

4

storefront.CacheCustom({

mode: 'must-revalidate, no-transform',

maxAge: 30,

})

9

1

2

3

4

storefront.CacheCustom({

mode: 'must-revalidate, no-transform',

maxAge: 30,

})

##### JavaScript

```liquid
storefront.CacheCustom({
  mode: 'must-revalidate, no-transform',
  maxAge: 30,
})
```

##### TypeScript

```liquid
storefront.CacheCustom({
  mode: 'must-revalidate, no-transform',
  maxAge: 30,
})
```

---

## [Anchor to Cache-Control API](/docs/storefronts/headless/hydrogen/caching#cache-control-api)Cache-Control API

Hydrogen and Oxygen caching strategies are compatible with the HTTP Header [`Cache-Control` API](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), with a small number of [exceptions](#cache-control-api-exceptions).

The following options are available when creating a custom caching strategy with `CacheCustom()`:

| Option | Type | Description |
| --- | --- | --- |
| `mode` | String | One or more comma-separated directives for how caches should handle response data. Accepts `public`, `private`, `no-store`, `must-revalidate`, and `no-transform`. |
| `maxAge` | Number | The length of time, in seconds, to cache the response. |
| `staleWhileRevalidate` | Number | The length of time, in seconds, to serve a stale response while fetching a fresh one in the background. |
| `sMaxAge` | Number | The length of time, in seconds, that proxies or CDNs can store the response. |
| `staleIfError` | Number | The length of time, in seconds, for the browser to serve a cached response instead when it receives a 5xx error.   Note that`staleIfError` is ignored when caching sub-requests. Instead, use `staleWhileRevalidate` to return stale data if errors are thrown during the revalidation period. |

### [Anchor to Cache-Control API exceptions](/docs/storefronts/headless/hydrogen/caching#cache-control-api-exceptions)Cache-Control API exceptions

The `no-cache` directive isn't supported by Oxygen because it instructs the browser not to use the cached data until the server returns a `304 (Not Modified)` status from server. However, Oxygen doesn't return the `304` response status code, so this directive has no effect.

---

Was this page helpful?

YesNo