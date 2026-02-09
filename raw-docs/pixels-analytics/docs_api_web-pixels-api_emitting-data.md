---
source: https://shopify.dev/docs/api/web-pixels-api/emitting-data
---

# Emitting Data

App users and app developers can publish custom customer events from online store theme liquid files, [theme app extensions](/docs/apps/online-store/theme-app-extensions), [checkout UI extensions](/docs/api/checkout-ui-extensions/latest/extension-points-overview) and [customer account UI extensions](/docs/api/customer-account-ui-extensions/latest/targets). When custom customer events are published they can be accessed by all custom pixels and app pixels.

Ask assistant

---

## [Anchor to Publishing custom events](/docs/api/web-pixels-api/emitting-data#publishing-custom-events)Publishing custom events

The `analytics.publish` method is available in different contexts for publishing custom events. The `analytics.publish` method takes an `event_name` and some `event_data` as parameters. The object passed into the `event_data` field is shared with subscribers to the event using the `customData` field. If you haven't set up a way for users to define custom transformation of payloads, then your app pixels might not be able to parse these custom fields. Custom pixels, though, can be changed by the users to translate custom fields to a service’s required format.

UI Extensions

In Checkout and Customer Accounts, you can publish custom events from your UI extensions. For more information, refer to the [analytics checkout extension point on the StandardApi](https://shopify.dev/docs/api/checkout-ui-extensions/latest/apis).

**UI Extensions:**

In Checkout and Customer Accounts, you can publish custom events from your UI extensions. For more information, refer to the [analytics checkout extension point on the StandardApi](https://shopify.dev/docs/api/checkout-ui-extensions/latest/apis).

Important

To ensure the quality of standard events, partners and merchants cannot publish standard events. `Shopify.analytics.publish` only exposes the method to publish custom events.

To avoid collision with standard events, custom events should be prefixed with the app name or a unique identifier. For example, `my_app:event_name`.

**Important:**

To ensure the quality of standard events, partners and merchants cannot publish standard events. `Shopify.analytics.publish` only exposes the method to publish custom events.

To avoid collision with standard events, custom events should be prefixed with the app name or a unique identifier. For example, `my_app:event_name`.

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

/\*\*

\* In the online store you can access the `analytics.publish` method on the Shopify object.

\* Inside theme app extensions or within the `<script>` tag of theme.liquid files, you can

\* insert the following code to publish your custom pixels.

\*/

/\*\*

\* event\_data

\* type: Object

\* description: An object that contains metadata about the event.

\*/

const event\_data = {sample\_event\_data: 1};

/\*\*

\* @param: event\_name

\* @param: event\_data

\*

\*/

Shopify.analytics.publish('my\_store:event\_name', event\_data);

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

// In UI extensions, you can publish custom events from the

// standard UI extension API.

/\*\*

\* event\_data

\* type: Object

\* description: An object that contains metadata about the event.

\*/

const event\_data = {sample\_event\_data: 1};

/\*\*

\* @param: event\_name

\* @param: event\_data

\*/

analytics.publish('my\_app:event\_name', event\_data);

##### Online Store

```liquid
/**
 * In the online store you can access the `analytics.publish` method on the Shopify object.
 * Inside theme app extensions or within the `<script>` tag of theme.liquid files, you can
 * insert the following code to publish your custom pixels.
 */

/**
 * event_data
 * type: Object
 * description: An object that contains metadata about the event.
 */
const event_data = {sample_event_data: 1};

/**
 * @param: event_name
 * @param: event_data
 *
 */
Shopify.analytics.publish('my_store:event_name', event_data);
```

##### UI Extension

```liquid
// In UI extensions, you can publish custom events from the
// standard UI extension API.

/**
 * event_data
 * type: Object
 * description: An object that contains metadata about the event.
 */
const event_data = {sample_event_data: 1};

/**
 * @param: event_name
 * @param: event_data
 */
analytics.publish('my_app:event_name', event_data);
```

---

## [Anchor to Subscribing to custom events](/docs/api/web-pixels-api/emitting-data#subscribing-to-custom-events)Subscribing to custom events

You can subscribe to custom events like you would standard events. Anything published to the custom event is passed to the `customData` field.

Caution

Custom events can be published by users, other developers and even visitors from their browser console. Be mindful when processing any custom events.

**Caution:**

Custom events can be published by users, other developers and even visitors from their browser console. Be mindful when processing any custom events.

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

// Subscribe from web pixel app extension

import {register} from '@shopify/web-pixels-extension';

register(({analytics}) => {

analytics.subscribe('my\_app:my\_custom\_event', (event) => {

/\*

event = {

id: "123",

clientId: "2cabc5d8-e728-4359-9173-4b31265cbac0",

name: "my\_custom\_event",

timestamp: "2011-10-05T14:48:00.000Z",

context: { ... },

customData: {

foo: { bar: '123' },

abc: { def: 'geh' }

}

}

\*/

});

});

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

// Publishing from a UI Extension

analytics.publish('my\_app:my\_custom\_event', {

foo: {

bar: '123',

},

abc: {

def: 'geh',

},

});

##### Subscribe

```liquid
// Subscribe from web pixel app extension
import {register} from '@shopify/web-pixels-extension';

register(({analytics}) => {
  analytics.subscribe('my_app:my_custom_event', (event) => {
    /*
      event = {
        id: "123",
        clientId: "2cabc5d8-e728-4359-9173-4b31265cbac0",
        name: "my_custom_event",
        timestamp: "2011-10-05T14:48:00.000Z",
        context: { ... },
        customData: {
          foo: { bar: '123' },
          abc: { def: 'geh' }
        }
      }
    */
  });
});
```

##### Publish

```liquid
// Publishing from a UI Extension
analytics.publish('my_app:my_custom_event', {
  foo: {
    bar: '123',
  },
  abc: {
    def: 'geh',
  },
});
```

![Subscribing to custom events](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/web-pixels-api/checkout-ui-B60ruC42.png)

---

## [Anchor to Visitor API](/docs/api/web-pixels-api/emitting-data#visitor-api)Visitor API

The `analytics.visitor` method helps merchants to identify visitors to their store. The method is primarily intended for use cases involving visitor-provided information to aid Shopify, and app features that use the data to enhance the customer experience.

For example, if a visitor submits their email address to receive a 30% off coupon, then the email can be relayed to a Partner app using Server Pixels to power loyalty features. The storefront experience can be personalized based on existing information that the merchant already has about the customer. It's important to ensure that, when utilizing this API, all necessary notices and consent in the visitor's region are provided.

Important

After integrating successfully, you’ll need to inform Partner Support for the data to be processed. Failure to do so will mean that the data is not utilized by the merchant’s shop.

**Important:**

After integrating successfully, you’ll need to inform Partner Support for the data to be processed. Failure to do so will mean that the data is not utilized by the merchant’s shop.

App Id

App developers should provide an `appId` to identify themselves when they call the visitor API on the online store. Calling the visitor API without providing an `appId` can degrade data quality, which makes it difficult for merchants to manage their data. To find your `appId`, you can use the [GraphQL Admin API](/docs/api/admin-graphql/latest/queries/app). In UI Extensions, you don't need to provide an `appId` because these are managed automatically.

**App Id:**

App developers should provide an `appId` to identify themselves when they call the visitor API on the online store. Calling the visitor API without providing an `appId` can degrade data quality, which makes it difficult for merchants to manage their data. To find your `appId`, you can use the [GraphQL Admin API](/docs/api/admin-graphql/latest/queries/app). In UI Extensions, you don't need to provide an `appId` because these are managed automatically.

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

/\*\*

\* In the online store, you can access the `analytics.visitor` method on the Shopify object.

\* Inside theme app extensions or within the `<script>` tag of liquid files, you can

\* insert the following code to publish your custom pixels.

\*/

/\*\*

\* @param {Object} visitorInfo - The parameters for the visitor information.

\* @param {string} [visitorInfo.phone] - The phone number.

\* @param {string} [visitorInfo.email] - The email address.

\* @param {Object} [options] - Additional settings and context for calls to visitor.

\* @param {string} [options.appId] - The App Id of the calling app.

\* @returns {boolean} - Returns `true` if the visitor method was successful, and returns `false` if the payload was rejected. This method will raise an error if there is an issue with the payload.

\*/

// Usage:

Shopify.analytics.visitor(

{

email: 'someEmail@example.com',

phone: '+1 555 555 5555',

},

{

appId: '1234',

},

);

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

// In UI Extension, you can emit visitor information from

// your extensions using the analytics API within

// the StandardAPI.

/\*\*

\* @param {Object} visitorInfo - The parameters for the visitor information.

\* @param {string} [visitorInfo.phone] - The phone number.

\* @param {string} [visitorInfo.email] - The email address.

\* @returns {Promise<VisitorResult>} - Returns a VisitorResult object.

\* @see https://shopify.dev/docs/api/checkout-ui-extensions/unstable/apis/standardapi#properties-propertydetail-analytics

\*/

analytics

.visitor({

email: 'someEmail@example.com',

phone: '+1 555 555 5555',

})

.then((result) => {

if (result.type === 'success') {

console.log(`Success`);

} else {

console.log(`Error`, result.error);

}

});

##### Online Store

```liquid
/**
 * In the online store, you can access the `analytics.visitor` method on the Shopify object.
 * Inside theme app extensions or within the `<script>` tag of liquid files, you can
 * insert the following code to publish your custom pixels.
 */

/**
 * @param {Object} visitorInfo - The parameters for the visitor information.
 * @param {string} [visitorInfo.phone] - The phone number.
 * @param {string} [visitorInfo.email] - The email address.
 * @param {Object} [options] - Additional settings and context for calls to visitor.
 * @param {string} [options.appId] - The App Id of the calling app.
 * @returns {boolean} - Returns `true` if the visitor method was successful, and returns `false` if the payload was rejected. This method will raise an error if there is an issue with the payload.
 */

// Usage:
Shopify.analytics.visitor(
  {
    email: 'someEmail@example.com',
    phone: '+1 555 555 5555',
  },
  {
    appId: '1234',
  },
);
```

##### UI Extension

```liquid
// In UI Extension, you can emit visitor information from
// your extensions using the analytics API within
// the StandardAPI.

/**
 * @param {Object} visitorInfo - The parameters for the visitor information.
 * @param {string} [visitorInfo.phone] - The phone number.
 * @param {string} [visitorInfo.email] - The email address.
 * @returns {Promise<VisitorResult>} - Returns a VisitorResult object.
 * @see https://shopify.dev/docs/api/checkout-ui-extensions/unstable/apis/standardapi#properties-propertydetail-analytics
 */
analytics
  .visitor({
    email: 'someEmail@example.com',
    phone: '+1 555 555 5555',
  })
  .then((result) => {
    if (result.type === 'success') {
      console.log(`Success`);
    } else {
      console.log(`Error`, result.error);
    }
  });
```

---

Was this page helpful?

YesNo