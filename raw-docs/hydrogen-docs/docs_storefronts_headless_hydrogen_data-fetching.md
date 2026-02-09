---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/data-fetching
---

Hydrogen uses [Remix `loader` functions](https://remix.run/docs/main/route/loader) to handle all queries to the Storefront API, Customer Account API, and [third-party data sources](/docs/storefronts/headless/hydrogen/data-fetching/third-party).

Loading data efficiently is important to keeping your Hydrogen app fast and performant. Follow these examples and best practices to ensure your Hydrogen storefront is delivering the fastest experience for customers.

---

## [Anchor to Query Shopify APIs](/docs/storefronts/headless/hydrogen/data-fetching#query-shopify-apis)Query Shopify APIs

Hydrogen provides built-in API clients for the Storefront API and the Customer Account API.

### [Anchor to Query the Storefront API](/docs/storefronts/headless/hydrogen/data-fetching#query-the-storefront-api)Query the Storefront API

The following is an example of how the `/products/:handle` route can query the Storefront API and then render that product data in a component.

Tip

This example demonstrates a simple version of this pattern. However, it can be extended to cover more complex behaviors, including more robust error handling, GraphQL query fragments and directives, deferred loading for non-critical data, server-side caching for non-personalized data, and more.

**Tip:**

This example demonstrates a simple version of this pattern. However, it can be extended to cover more complex behaviors, including more robust error handling, GraphQL query fragments and directives, deferred loading for non-critical data, server-side caching for non-personalized data, and more.

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

import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function

export async function loader({params, context}) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

});

return {product};

}

// Render the component using data returned by the loader

export default function Product() {

const {product} = useLoaderData();

return (

<h1>{product.title}</h1>

)

}

// Query the product title by its ID

const PRODUCT\_QUERY = `#graphql

product(handle: $handle) {

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

import {useLoaderData} from '@shopify/remix-oxygen';

import type { LoaderArgs } from '@shopify/remix-oxygen';

import type { Product } from '@shopify/hydrogen/storefront-api-types';

// Fetch and return API data with a Remix loader function

export async function loader({params, context}: LoaderArgs) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

});

return {product};

}

// Render the component using data returned by the loader

export default function Product() {

const {product} = useLoaderData<typeof loader>();

return (

<h1>{product.title}</h1>

)

}

// Query the product title by its ID

const PRODUCT\_QUERY = `#graphql

product(handle: $handle) {

title

}

`

##### JavaScript

```liquid
import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
  });
  return {product};
}

// Render the component using data returned by the loader
export default function Product() {
  const {product} = useLoaderData();
  return (
    <h1>{product.title}</h1>
  )
}

// Query the product title by its ID
const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    title
  }`
```

##### TypeScript

```liquid
import {useLoaderData} from '@shopify/remix-oxygen';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
  });
  return {product};
}

// Render the component using data returned by the loader
export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return (
    <h1>{product.title}</h1>
  )
}

// Query the product title by its ID
const PRODUCT_QUERY = `#graphql
  product(handle: $handle) {
    title
  }
`
```

### [Anchor to Query the Customer Account API](/docs/storefronts/headless/hydrogen/data-fetching#query-the-customer-account-api)Query the Customer Account API

The following is an example of how the `/account/order/:id` route can query the Customer Account API to display information about a single order. This example assumes that a customer is logged in.

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

30

31

32

33

34

35

36

37

38

import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function

export async function loader({params, context}) {

const orderId = atob(params.id);

const {data, errors} = await context.customerAccount.query(

CUSTOMER\_ORDER\_QUERY,

{

variables: {orderId},

},

);

if ((errors && errors.length) || !(data && data.order)) {

throw new Error('Order not found');

}

return {order: data.order};

}

// Render the component using data returned by the loader

export default function Order() {

const {order} = useLoaderData();

if (order) {

return (

<h1>{order.name}</h1>

)

}

}

// Query the order name by its ID

const CUSTOMER\_ORDER\_QUERY = `#graphql

query Order($orderId: ID!) {

order(id: $orderId) {

name

}

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

30

31

32

33

34

35

36

37

38

39

import {useLoaderData} from '@shopify/remix-oxygen';

import type { LoaderArgs } from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function

export async function loader({params, context}: LoaderArgs) {

const orderId = atob(params.id);

const {data, errors} = await context.customerAccount.query(

CUSTOMER\_ORDER\_QUERY,

{

variables: {orderId},

},

);

if (errors?.length || !data?.order) {

throw new Error('Order not found');

}

return {order: data.order};

}

// Render the component using data returned by the loader

export default function Order() {

const {order} = useLoaderData();

if (order) {

return (

<h1>{order.name}</h1>

)

}

}

// Query the order name by its ID

const CUSTOMER\_ORDER\_QUERY = `#graphql

query Order($orderId: ID!) {

order(id: $orderId) {

name

}

}`

##### JavaScript

```liquid
import {useLoaderData} from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}) {
  const orderId = atob(params.id);

  const {data, errors} = await context.customerAccount.query(
    CUSTOMER_ORDER_QUERY,
    {
      variables: {orderId},
    },
  );

  if ((errors && errors.length) || !(data && data.order)) {
    throw new Error('Order not found');
  }

  return {order: data.order};
}

// Render the component using data returned by the loader
export default function Order() {
  const {order} = useLoaderData();

  if (order) {
    return (
      <h1>{order.name}</h1>
    )
  }
}

// Query the order name by its ID
const CUSTOMER_ORDER_QUERY = `#graphql
  query Order($orderId: ID!) {
    order(id: $orderId) {
      name
    }
  }`
```

##### TypeScript

```liquid
import {useLoaderData} from '@shopify/remix-oxygen';
import type { LoaderArgs } from '@shopify/remix-oxygen';

// Fetch and return API data with a Remix loader function
export async function loader({params, context}: LoaderArgs) {
  const orderId = atob(params.id);

  const {data, errors} = await context.customerAccount.query(
    CUSTOMER_ORDER_QUERY,
    {
      variables: {orderId},
    },
  );

  if (errors?.length || !data?.order) {
    throw new Error('Order not found');
  }

  return {order: data.order};
}

// Render the component using data returned by the loader
export default function Order() {
  const {order} = useLoaderData();

  if (order) {
    return (
      <h1>{order.name}</h1>
    )
  }
}

// Query the order name by its ID
const CUSTOMER_ORDER_QUERY = `#graphql
  query Order($orderId: ID!) {
    order(id: $orderId) {
      name
    }
  }`
```

---

## [Anchor to Caching loaded data](/docs/storefronts/headless/hydrogen/data-fetching#caching-loaded-data)Caching loaded data

Hydrogen caches Storefront API data by default. It also includes a set of utilities to customize caching rules for individual API queries. Consult the [Hydrogen caching docs](/docs/storefronts/headless/hydrogen/caching) for more details about configuring server-side cache rules, including creating your own custom caching rules.

Note

To avoid storing Personally Identifiable Information (PII) or other sensitive data, the Customer Account API client doesn't cache any requests. Caching this information could lead to unauthorized access or data breaches, compromising user privacy and security.

**Note:**

To avoid storing Personally Identifiable Information (PII) or other sensitive data, the Customer Account API client doesn't cache any requests. Caching this information could lead to unauthorized access or data breaches, compromising user privacy and security.

The following simplified example shows how to cache data for longer when querying for the product title, which is an API resource that typically doesn't change frequently:

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

import {useLoaderData} from '@shopify/remix-oxygen';

export async function loader({params, context}) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

// Pass a `cache` option with your query to customize API request caching.

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

import {useLoaderData} from '@remix-run/react';

import type { LoaderArgs } from '@shopify/remix-oxygen';

import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {

const {handle} = params;

const {storefront} = context;

const {product} = await storefront.query(PRODUCT\_QUERY, {

variables: {handle},

// Pass a `cache` option with your query to customize API request caching.

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
    // Pass a `cache` option with your query to customize API request caching.
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
import {useLoaderData} from '@remix-run/react';
import type { LoaderArgs } from '@shopify/remix-oxygen';
import type { Product } from '@shopify/hydrogen/storefront-api-types';

export async function loader({params, context}: LoaderArgs) {
  const {handle} = params;
  const {storefront} = context;
  const {product} = await storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Pass a `cache` option with your query to customize API request caching.
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

## [Anchor to Next steps](/docs/storefronts/headless/hydrogen/data-fetching#next-steps)Next steps

* Learn more about [caching Shopify API data with Hydrogen](/docs/storefronts/headless/hydrogen/caching)
* [Paginate your Hydrogen data queries](/docs/storefronts/headless/hydrogen/data-fetching/pagination) to work with large product collections
* Explore the Storefront API with Hydrogen’s [built-in GraphiQL client](/docs/storefronts/headless/hydrogen/data-fetching/graphiql)

---

Was this page helpful?

YesNo