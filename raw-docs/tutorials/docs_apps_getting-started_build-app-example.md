---
source: https://shopify.dev/docs/apps/getting-started/build-app-example
---

After you scaffold an app, you can add your own functionality to pages inside and outside of the Shopify admin.

In this tutorial, you'll scaffold an app that makes QR codes for products. When the QR code is scanned, it takes the user to a checkout that's populated with the product, or to the product page. The app logs every time the QR code is scanned, and exposes scan metrics to the app user.

Follow along with this tutorial to build a sample app, or clone the completed sample app.

## [Anchor to What you'll learn](/docs/apps/build/build?framework=reactRouter#what-youll-learn)What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Update the [Prisma](https://www.prisma.io/) database included in the app template.
* Use the [@shopify/shopify-app-react-router](https://www.npmjs.com/package/@shopify/shopify-app-react-router) package to authenticate users and query data.
* Use [Polaris web components](/docs/api/app-home/polaris-web-components) to create a UI that adheres to Shopify's [App Design Guidelines](/docs/apps/design-guidelines).
* Use [Shopify App Bridge](/docs/api/app-bridge) to add interactivity to your app.

[](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/qr-code-react-router-CjCMx544.mp4)

## Requirements

[Scaffold an app](/docs/apps/build/scaffold-app)

Scaffold an app that uses the [React Router template](https://github.com/Shopify/shopify-app-template-react-router).

[Install `qrcode`](https://www.npmjs.com/package/qrcode)

Enables creation of QR codes.

[Install `@shopify/polaris-icons`](https://www.npmjs.com/package/@shopify/polaris-icons)

Provides placeholder images for the UI.

[Install `tiny-invariant`](https://www.npmjs.com/package/tiny-invariant)

Allows loaders to easily throw errors.

## Project

Framework:

React Router 

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-DwHxpQ4h.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/ReactRouter-dark-BRmMldI1.svg)

React Router

[View on GitHub](https://github.com/Shopify/example-app--qr-code--remix/blob/upgrade-to-react-router/)

## [Anchor to Add the QR code data model to your database](/docs/apps/build/build?framework=reactRouter#add-the-qr-code-data-model-to-your-database)Add the QR code data model to your database

To store your QR codes, you need to add a table to the database included in your template.

Info

The single table in the template's Prisma schema is the `Session` table. It stores the tokens for each store that installs your app, and is used by the [@shopify/shopify-app-session-storage-prisma](https://www.npmjs.com/package/@shopify/shopify-app-session-storage-prisma) package to manage sessions.

**Info:**

The single table in the template's Prisma schema is the `Session` table. It stores the tokens for each store that installs your app, and is used by the [@shopify/shopify-app-session-storage-prisma](https://www.npmjs.com/package/@shopify/shopify-app-session-storage-prisma) package to manage sessions.

### [Anchor to Create the table](/docs/apps/build/build?framework=reactRouter#create-the-table)Create the table

Add a `QRCode` model to your Prisma schema. The model should contain the following fields:

* `id`: The primary key for the table.
* `title`: The app user-specified name for the QR code.
* `shop`: The store that owns the QR code.
* `productId`: The product that this QR code is for.
* `productHandle`: Used to create the destination URL for the QR code.
* `productVariantId`: Used to create the destination URL for the QR code.
* `destination`: The destination for the QR code.
* `scans`: The number times that the QR code been scanned.
* `createdAt`: The date and time when the QR code was created.

---

The `QRCode` model contains the key identifiers that the app uses to retrieve Shopify product and variant data. At runtime, additional product and variant properties are retrieved and used to populate the UI.

### [Anchor to Migrate the database](/docs/apps/build/build?framework=reactRouter#migrate-the-database)Migrate the database

After you add your schema, you need to migrate the database to create the table.

1. Run the following command to create the table in Prisma:

   9

   1

   npm run prisma migrate dev -- --name add-qrcode-table

   9

   1

   yarn prisma migrate dev --name add-qrcode-table

   9

   1

   pnpm run prisma migrate dev --name add-qrcode-table

   ##### npm

   ```liquid
   npm run prisma migrate dev -- --name add-qrcode-table
   ```

   ##### Yarn

   ```liquid
   yarn prisma migrate dev --name add-qrcode-table
   ```

   ##### pnpm

   ```liquid
   pnpm run prisma migrate dev --name add-qrcode-table
   ```
2. To confirm that your migration worked, open [Prisma Studio](https://www.prisma.io/docs/concepts/components/prisma-studio):

   9

   1

   npm run prisma studio

   9

   1

   yarn prisma studio

   9

   1

   pnpm run prisma studio

   ##### npm

   ```liquid
   npm run prisma studio
   ```

   ##### Yarn

   ```liquid
   yarn prisma studio
   ```

   ##### pnpm

   ```liquid
   pnpm run prisma studio
   ```

   Prisma Studio opens in your browser.
3. In Prisma Studio, click the **QRCode** tab to view the table.

You should see a table with the columns that you created, and no data.

## [Anchor to Get QR code and product data](/docs/apps/build/build?framework=reactRouter#get-qr-code-and-product-data)Get QR code and product data

After you create your database, add code to retrieve data from the table.

Supplement the QR code data in the database with product information.

### [Anchor to Create the model](/docs/apps/build/build?framework=reactRouter#create-the-model)Create the model

Create a model to get and validate QR codes.

Create an `/app/models` folder. In that folder, create a new file called `QRCode.server.js`.

### [Anchor to Get QR codes](/docs/apps/build/build?framework=reactRouter#get-qr-codes)Get QR codes

Create a function to get a single QR code for your QR code form, and a second function to get multiple QR codes for your app's index page. You'll [create a QR code form](#create-a-qr-code-form) later in this tutorial.

QR codes stored in the database can be retrieved using the Prisma `FindFirst` and `FindMany` queries.

### [Anchor to Get the QR code image](/docs/apps/build/build?framework=reactRouter#get-the-qr-code-image)Get the QR code image

A QR code takes the user to `/qrcodes/$id/scan`, where `$id` is the ID of the QR code. Create a function to construct this URL, and then use the `qrcode` package to return a base 64-encoded QR code image `src`.

---

### [Anchor to Get the destination URL](/docs/apps/build/build?framework=reactRouter#get-the-destination-url)Get the destination URL

Scanning a QR code takes the user to one of two places:

* The product details page
* A checkout with the product in the cart

Create a function to conditionally construct this URL depending on the destination that the merchant selects.

### [Anchor to Retrieve additional product and variant data](/docs/apps/build/build?framework=reactRouter#retrieve-additional-product-and-variant-data)Retrieve additional product and variant data

The QR code from Prisma needs to be supplemented with product data. It also needs the QR code image and destination URL.

Create a function that queries the [GraphQL Admin API](/docs/api/admin-graphql) for the product title, and the first featured product image's URL and alt text. It should also return an object with the QR code data and product data, and use the `getDestinationUrl` and `getQRCodeImage` functions that you created to get the destination URL's QR code image.

---

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

### [Anchor to Validate QR codes](/docs/apps/build/build?framework=reactRouter#validate-qr-codes)Validate QR codes

To create a valid QR code, the app user needs to provide a title, and select a product and destination. Add a function to ensure that, when the user submits the form to create a QR code, values exist for all of the required fields.

The action for the QR code form will return errors from this function.

## [Anchor to Create a QR code form](/docs/apps/build/build?framework=reactRouter#create-a-qr-code-form)Create a QR code form

Create a form that allows the app user to manage QR codes.

To create this form, you'll use a [Route module](https://reactrouter.com/start/framework/route-module), [Polaris web components](/docs/api/app-home/polaris-web-components) and [App Bridge](/docs/api/app-bridge).

### [Anchor to Set up the form route](/docs/apps/build/build?framework=reactRouter#set-up-the-form-route)Set up the form route

Create a form that can create, update or delete a QR code.

In the `app` > `routes` folder, create a new file called `app.qrcodes.$id.jsx`.

---

#### [Anchor to Dynamic segments](/docs/apps/build/build?framework=reactRouter#dynamic-segments)Dynamic segments

This route uses a [dynamic segment route](https://reactrouter.com/start/framework/routing#dynamic-segments) to match the URL for creating a new QR code and editing an existing one.

If the user is creating a QR code, the URL is `/app/qrcodes/new`. If the user is updating a QR code, the URL is `/app/qrcodes/1`, where `1` is the ID of the QR code that the user is updating.

#### [Anchor to React Router layouts](/docs/apps/build/build?framework=reactRouter#react-router-layouts)React Router layouts

The React Router template includes a [layout](https://reactrouter.com/start/framework/routing#layout-routes) at `app/routes/app.jsx`. This layout should be used for authenticated routes that render inside the Shopify admin. It's responsible for configuring App Bridge and Polaris web components, and authenticating the user using [shopify-app-react-router](https://www.npmjs.com/package/@shopify/shopify-app-react-router).

---

[App Bridge](/docs/api/app-bridge)[Polaris web components](/docs/api/app-home/polaris-web-components)

[App Bridge](/docs/api/app-bridge) [Polaris web components](/docs/api/app-home/polaris-web-components)

### [Anchor to Authenticate the user](/docs/apps/build/build?framework=reactRouter#authenticate-the-user)Authenticate the user

Authenticate the route using `shopify-app-react-router`.

---

If the user isn't authenticated, `authenticate.admin` handles the necessary redirects. If the user is authenticated, then the method returns an admin object.

You can use the `authenticate.admin` method for the following purposes:

* Getting information from the session, such as the `shop`
* Accessing the [GraphQL Admin API](/docs/api/admin-graphql)
* Within methods to require and request billing

---

[Authenticating admin requests](/docs/api/shopify-app-react-router/v0/authenticate/admin)[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

[Authenticating admin requests](/docs/api/shopify-app-react-router/v0/authenticate/admin) [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

### [Anchor to Return a JSON Response](/docs/apps/build/build?framework=reactRouter#return-a-json-response)Return a JSON Response

Return JSON data that can be used to populate the QR code form.

If the `id` parameter is `new`, return JSON with an empty title, and product for the destination. If the `id` parameter isn't `new`, then return the JSON from `getQRCode` to populate the QR code state.

---

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

GraphQL Admin API](/docs/api/admin-graphql)

### [Anchor to Manage the form state](/docs/apps/build/build?framework=reactRouter#manage-the-form-state)Manage the form state

Maintain the state of the QR code form state using the following variables:

* `initialFormState`: The initial state of the form. This only changes when the user submits the form. This state is copied from `useLoaderData` into React state.
* `formState`: When the user changes the title, selects a product, or changes the destination, this state is updated. This state is copied from `useLoaderData` into React state.
* `errors`: If the app user doesn't fill all of the QR code form fields, then the action returns errors to display. This is the return value of `validateQRCode`, which is accessed through the `useActionData` hook.
* `isSaving`: Keeps track of the network state using `useNavigation`. This state is used to disable buttons and show loading states.
* `isDirty`: Determines if the form has changed. This is used to enable save buttons when the app user has changed the form contents, or disable them when the form contents haven't changed.

---

### [Anchor to Add a product selector](/docs/apps/build/build?framework=reactRouter#add-a-product-selector)Add a product selector

Using the App Bridge `ResourcePicker` action, add a modal that allows the user to select a product. Save the selection to form state.

![Screenshot showing a App Bridge modal for selecting products](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/select-product-react-router-K8Shzgr0.png)

---

[ResourcePicker](/docs/api/app-home/apis/resource-picker)

[ResourcePicker](/docs/api/app-home/apis/resource-picker)

### [Anchor to Submit](/docs/apps/build/build?framework=reactRouter#submit)Submit

Use `useSubmit` to add the ability to save and delete a QR Code.

---

### [Anchor to Lay out the form](/docs/apps/build/build?framework=reactRouter#lay-out-the-form)Lay out the form

Using Polaris web components, build the layout for the form. Use `s-page`, `s-section`, and `s-box` with `slot="aside"` to structure the page. The page should have two columns.

---

Polaris is the design system for the Shopify admin. Using Polaris web components ensures that your UI is accessible, responsive, and displays consistently with the Shopify Admin.

[Polaris web components](/docs/api/app-home/polaris-web-components)[s-page](/docs/api/app-home/polaris-web-components/structure/page)[s-section](/docs/api/app-home/polaris-web-components/layout-and-structure/section)[s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box)

[Polaris web components](/docs/api/app-home/polaris-web-components) [s-page](/docs/api/app-home/polaris-web-components/structure/page) [s-section](/docs/api/app-home/polaris-web-components/layout-and-structure/section) [s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box)

### [Anchor to Add breadcrumbs](/docs/apps/build/build?framework=reactRouter#add-breadcrumbs)Add breadcrumbs

Use an App Bridge `s-page` component to display a title that indicates to the user whether they're creating or editing a QR code. Include a breadcrumb link to go back to the [QR code list](#list-qr-codes).

---

[Title Bar](/docs/api/app-home/app-bridge-web-components/title-bar)

[Title Bar](/docs/api/app-home/app-bridge-web-components/title-bar)

### [Anchor to Add a title field](/docs/apps/build/build?framework=reactRouter#add-a-title-field)Add a title field

Use `s-text-field` for updating the title. It should `setFormState`, have some `details` and show title errors from `useActionData`.

---

[s-text-field](/docs/api/app-home/polaris-web-components/forms/textfield)

[s-text-field](/docs/api/app-home/polaris-web-components/forms/textfield)

### [Anchor to Add a way to select the product](/docs/apps/build/build?framework=reactRouter#add-a-way-to-select-the-product)Add a way to select the product

If the user hasn't selected a product, then display a `s-button` with an `onClick` for `selectProduct`.

If the user has selected a product, use `s-image` to display the product image. Use `s-clickable`, `s-box`, `s-image` and `s-icon` to display the product image. Use `s-box` and `s-stack` to layout the UI.

---

[s-button](/docs/api/app-home/polaris-web-components/actions/button)[s-image](/docs/api/app-home/polaris-web-components/images/image)[s-clickable](/docs/api/app-home/polaris-web-components/actions/clickable)[s-image](/docs/api/app-home/polaris-web-components/media-and-visuals/image)[s-icon](/docs/api/app-home/polaris-web-components/media-and-visuals/icon)[s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box)[s-stack](/docs/api/app-home/polaris-web-components/layout-and-structure/box)

[s-button](/docs/api/app-home/polaris-web-components/actions/button) [s-image](/docs/api/app-home/polaris-web-components/images/image) [s-clickable](/docs/api/app-home/polaris-web-components/actions/clickable) [s-image](/docs/api/app-home/polaris-web-components/media-and-visuals/image) [s-icon](/docs/api/app-home/polaris-web-components/media-and-visuals/icon) [s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box) [s-stack](/docs/api/app-home/polaris-web-components/layout-and-structure/box)

### [Anchor to Add destination options](/docs/apps/build/build?framework=reactRouter#add-destination-options)Add destination options

Use `s-select` to render different destinations. It should `setFormState` when `onChange` occurs.

If the user is editing a QR code, use a `s-link` to link to the destination URL in a new tab.

---

[s-select](/docs/api/app-home/polaris-web-components/forms/select)[s-link](/docs/api/app-home/polaris-web-components/actions/link)

[s-select](/docs/api/app-home/polaris-web-components/forms/select) [s-link](/docs/api/app-home/polaris-web-components/actions/link)

### [Anchor to Display a preview of the QR code](/docs/apps/build/build?framework=reactRouter#display-a-preview-of-the-qr-code)Display a preview of the QR code

After saving a QR code, or when editing an existing QR code, provide ways to preview the QR code that the app user created.

Use `s-box` with `slot="aside"` to position the preview as an aside.

If a QR code is available, then use `s-image` to render the QR code. If no QR code is available, then use `s-text` with `color="subdued"`.

Add buttons to preview the public URL, and to download the QR code

---

[s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box)[s-image](/docs/api/app-home/polaris-web-components/images/image)[s-text](/docs/api/app-home/polaris-web-components/typography/text)[s-button](/docs/api/app-home/polaris-web-components/actions/button)

[s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box) [s-image](/docs/api/app-home/polaris-web-components/images/image) [s-text](/docs/api/app-home/polaris-web-components/typography/text) [s-button](/docs/api/app-home/polaris-web-components/actions/button)

### [Anchor to Add save bar](/docs/apps/build/build?framework=reactRouter#add-save-bar)Add save bar

Use `shopify.saveBar` and `ui-save-bar` to render **Save** and **Discard** buttons.

Use the `useSubmit` hook to save the form data.

Copy the data that Prisma needs from `formState` and set the `cleanFormState` to the current `formState`.

---

[App Bridge save bar](/docs/api/app-home/app-bridge-web-components/ui-save-bar)

[App Bridge save bar](/docs/api/app-home/app-bridge-web-components/ui-save-bar)

### [Anchor to Create, update, or delete a QR code](/docs/apps/build/build?framework=reactRouter#create-update-or-delete-a-qr-code)Create, update, or delete a QR code

Create an `action` to create, update, or delete a QR code.

The `action` should use the store from the session. This ensures that the app user can only create, update, or delete QR codes for their own store.

The action should return errors for incomplete data using your `validateQRCode` function.

If the action deletes a QR code, redirect the app user to the index page. If the action creates a QR code, redirect to `app/qrcodes/$id`, where `$id` is the ID of the newly created QR code.

---

## [Anchor to List QR codes](/docs/apps/build/build?framework=reactRouter#list-qr-codes)List QR codes

To allow app users to navigate to QR codes, list the QR codes in the app home.

### [Anchor to Load QR codes](/docs/apps/build/build?framework=reactRouter#load-qr-codes)Load QR codes

In the app's index route, load the QR codes using a `loader`.

The `loader` should load QR codes using the `qrcodes` function from [`app/models/QRCode.server.js`](#get-qr-code-and-product-data), and return them.

---

### [Anchor to Create an empty state](/docs/apps/build/build?framework=reactRouter#create-an-empty-state)Create an empty state

If there are no QR codes, construct an empty state display using `s-section`, `s-grid`, `s-box`, `s-heading` and `s-paragraph`. Use `s-button` to link to the QR code form for creating a new QR Code.

![Screenshot showing a Polaris EmptyState](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/empty-state-react-router-Cj2HaAfD.png)

---

[s-section](/docs/api/app-home/polaris-web-components/layout-and-structure/section)[s-grid](/docs/api/app-home/polaris-web-components/layout-and-structure/grid)[s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box)[s-heading](/docs/api/app-home/polaris-web-components/typography/heading)[s-paragraph](/docs/api/app-home/polaris-web-components/typography/paragraph)[s-button](/docs/api/app-home/polaris-web-components/actions/button)

[s-section](/docs/api/app-home/polaris-web-components/layout-and-structure/section) [s-grid](/docs/api/app-home/polaris-web-components/layout-and-structure/grid) [s-box](/docs/api/app-home/polaris-web-components/layout-and-structure/box) [s-heading](/docs/api/app-home/polaris-web-components/typography/heading) [s-paragraph](/docs/api/app-home/polaris-web-components/typography/paragraph) [s-button](/docs/api/app-home/polaris-web-components/actions/button)

### [Anchor to Create an index table](/docs/apps/build/build?framework=reactRouter#create-an-index-table)Create an index table

If there are QR codes present, then use a `s-table` to list them.

The table should have columns for the QR code title, product, the date the QR code was created, and the number of times the QR code was scanned. The title `s-table-header` should use `listSlot="primary"`.

![Screenshot showing a Polaris table](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/index-table-react-router-N07JF0sI.png)

---

[s-table](/docs/api/app-home/polaris-web-components/layout-and-structure/table)

[s-table](/docs/api/app-home/polaris-web-components/layout-and-structure/table)

### [Anchor to Create index table rows](/docs/apps/build/build?framework=reactRouter#create-index-table-rows)Create index table rows

Map over each QR code and render a `s-table-row`. Make sure each row has an `s-table-cell` for the QR code title, product, the date the QR code was created, and the number of times the QR code was scanned.

---

[s-table-row](/docs/api/app-home/polaris-web-components/layout-and-structure/table)[s-table-cell](/docs/api/app-home/polaris-web-components/layout-and-structure/table)[s-image](/docs/api/app-home/polaris-web-components/images/image)[s-text](/docs/api/app-home/polaris-web-components/typography/text)[s-link](/docs/api/app-home/polaris-web-components/actions/link)

[s-table-row](/docs/api/app-home/polaris-web-components/layout-and-structure/table) [s-table-cell](/docs/api/app-home/polaris-web-components/layout-and-structure/table) [s-image](/docs/api/app-home/polaris-web-components/images/image) [s-text](/docs/api/app-home/polaris-web-components/typography/text) [s-link](/docs/api/app-home/polaris-web-components/actions/link)

### [Anchor to Warn if a product is deleted](/docs/apps/build/build?framework=reactRouter#warn-if-a-product-is-deleted)Warn if a product is deleted

A merchant can delete a product after creating a QR code for it. The data returned from `supplementQRCode` includes an `isDeleted` property. `isDeleted` is true if the product title returned from the [GraphQL Admin API](/docs/api/admin-graphql) is an empty string.

Use `s-badge` to render a warning to the user if a product is deleted.

---

[s-badge](/docs/api/app-home/polaris-web-components/feedback-and-status-indicators/badge)

[s-badge](/docs/api/app-home/polaris-web-components/feedback-and-status-indicators/badge)

### [Anchor to Lay out the page](/docs/apps/build/build?framework=reactRouter#lay-out-the-page)Lay out the page

After you create your empty state and index table, adjust the layout of the index page to return the markup that you created.

Create a layout using Polaris components. Render the empty state and table inside a Polaris `Card`.

Use the Polaris `s-page` component to render the title bar with a title. Add a primary button to navigate to the QR code creation form.

---

[s-page](/docs/api/app-home/polaris-web-components/structure/page)[s-button](/docs/api/app-home/polaris-web-components/actions/button)[Title Bar](/docs/api/app-home/app-bridge-web-components/title-bar)

[s-page](/docs/api/app-home/polaris-web-components/structure/page) [s-button](/docs/api/app-home/polaris-web-components/actions/button) [Title Bar](/docs/api/app-home/app-bridge-web-components/title-bar)

## [Anchor to Add a public QR code route](/docs/apps/build/build?framework=reactRouter#add-a-public-qr-code-route)Add a public QR code route

Make QR codes scannable by customers by exposing them using a public URL. When a customer scans a QR code, the scan count should increment, and the customer should be redirected to the destination URL.

### [Anchor to Create a public QR code route](/docs/apps/build/build?framework=reactRouter#create-a-public-qr-code-route)Create a public QR code route

Create a public page to render a QR code.

In the `app` > `routes` folder, create a new file called `qrcodes.$id.jsx`.

---

Because the `qrcodes.$id.jsx` doesn't require authentication or need to be rendered inside of the Shopify admin, it doesn't use the [app layout](#set-up-the-form-route).

### [Anchor to Load the QR code](/docs/apps/build/build?framework=reactRouter#load-the-qr-code)Load the QR code

Create a `loader` to load the QR code on the external route.

In the function, check that there's an ID in the URL. If there isn't, throw an error using `tiny-invariant`.

If there's an ID in the URL, load the QR code with that ID using Prisma:

* If there is no matching QR code ID in the table, throw an error using `tiny-invariant`.
* If there is a matching ID, return the QR code.

---

### [Anchor to Render a public QR code image](/docs/apps/build/build?framework=reactRouter#render-a-public-qr-code-image)Render a public QR code image

In the route's default `export`, render an `img` tag for the QR code image. Scanning this image takes the user to the destination URL. This is the next route to implement.

## [Anchor to Redirect the customer to the destination URL](/docs/apps/build/build?framework=reactRouter#redirect-the-customer-to-the-destination-url)Redirect the customer to the destination URL

When a QR code is scanned, redirect the customer to the destination URL. You can also increment the QR code scan count to reflect the number of times the QR code has been used.

### [Anchor to Create the scan route](/docs/apps/build/build?framework=reactRouter#create-the-scan-route)Create the scan route

Create a public route that handles QR code scans.

In the `app` > `routes` folder, create a new file called `qrcodes.$id.scan.jsx`.

### [Anchor to Validate the QR code ID](/docs/apps/build/build?framework=reactRouter#validate-the-qr-code-id)Validate the QR code ID

Create a `loader` function to load the QR code from the database.

In this function, check there is an ID in the URL. If the ID isn't present, then throw an error using `tiny-invariant`.

Load the QR code from the Prisma database. If a QR code with the specified ID doesn't exist, then throw an error using `tiny-invariant`.

---

### [Anchor to Increment the scan count](/docs/apps/build/build?framework=reactRouter#increment-the-scan-count)Increment the scan count

If the `loader` returns a QR code, then increment the scan count in the database.

Redirect to the destination URL for the QR code using `getDestinationUrl` and the `redirect` utility.

---

### [Anchor to Redirect](/docs/apps/build/build?framework=reactRouter#redirect)Redirect

The `loader` should return the destination URL for the QR code it incremented. Use `getDestinationUrl` from [`appmodels/QRCode.server.js`](#get-qr-code-and-product-data) to get that URL. Use `redirect` to redirect the user to that URL.

---

## [Anchor to Preview and test your app](/docs/apps/build/build?framework=reactRouter#preview-and-test-your-app)Preview and test your app

Use the CLI to preview your app. If you make changes, you'll see those changes hot reload in the browser.

### [Anchor to Start your server](/docs/apps/build/build?framework=reactRouter#start-your-server)Start your server

Run the Shopify CLI `dev` command to build your app and preview it on your dev store.

1. In a terminal, navigate to your app directory.
2. Either start or restart your server to build and preview your app:

   9

   1

   shopify app dev
3. Press `p` to open the developer console. In the developer console page, click on the preview link for your app home.
4. If you're prompted to install the app, then click **Install**.

### [Anchor to Test the QR code index and form](/docs/apps/build/build?framework=reactRouter#test-the-qr-code-index-and-form)Test the QR code index and form

Follow these steps to test the routes that are exposed to the app user in the Shopify admin. These routes include the app index and the QR code form.

1. In the index page for your app home, click **Create QR code** to go to the QR code form.

   The QR code form opens at `/app/qrcode/new`. The title of the page is **Create QR code**.
2. Try to submit the QR code form with an empty title, or without selecting a product.

   An error is returned.
3. Create a few QR codes for different products and destinations.
4. Click the **QR codes** breadcrumb to return to the index page.

   The QR code list is populated with the QR codes that you created:

   ![Screenshot showing the QR code list](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/complete-react-router-app-Dk7P9Iqp.png)
5. Select a QR code from the list.

   The QR code form opens at `/app/qrcode/<id>`. The title of the page is **Edit QR code**:

   ![Screenshot showing the QR code form](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/qr-code-form-react-router-BQP3lycb.png)
6. On the **Edit QR code** page, click **Delete**.

You're taken back to the index page, and the deleted QR code is removed from the list.

### [Anchor to Test QR code scanning functionality](/docs/apps/build/build?framework=reactRouter#test-qr-code-scanning-functionality)Test QR code scanning functionality

Scan the QR code that you created in the previous step.

1. From the app index page, click an existing QR code or create a new one.
2. On the QR code form, click **Go to public URL**.

   A new tab opens for the public URL for the QR code.
3. Scan the QR code with your phone.

   You're taken the destination URL.
4. Return to your app index page.

   The scan count for the QR code that just scanned is incremented.

## [Anchor to Tutorial complete!](/docs/apps/build/build?framework=reactRouter#tutorial-complete)Tutorial complete!

Congratulations! You built a QR code app using React Router, Polaris web components, App Bridge and Prisma. Keep the momentum going with these related tutorials and resources.

### [Anchor to Next steps](/docs/apps/build/build?framework=reactRouter#next-steps)Next steps

[![](/images/icons/32/gear.png)![](/images/icons/32/gear-dark.png)

Use webhooks

You can use webhooks to stay in sync with Shopify, or execute code after a specific event occurs in the store.

For example, if a merchant updates a product's handle, you can use the `products/update` webhook to trigger an update to the handle in your database.

Use webhooks

You can use webhooks to stay in sync with Shopify, or execute code after a specific event occurs in the store.

For example, if a merchant updates a product's handle, you can use the `products/update` webhook to trigger an update to the handle in your database.](/docs/apps/webhooks)

[Use webhooks  
  

You can use webhooks to stay in sync with Shopify, or execute code after a specific event occurs in the store.

For example, if a merchant updates a product's handle, you can use the `products/update` webhook to trigger an update to the handle in your database.](/docs/apps/webhooks)

[![](/images/icons/32/graphql.png)![](/images/icons/32/graphql-dark.png)

Explore the GraphQL Admin API

The GraphQL Admin API lets you read and write Shopify data, including products, customers, orders, inventory, fulfillment, and more.

Explore the GraphQL Admin API to learn about the available types and operations.

Explore the GraphQL Admin API

The GraphQL Admin API lets you read and write Shopify data, including products, customers, orders, inventory, fulfillment, and more.

Explore the GraphQL Admin API to learn about the available types and operations.](/docs/api/admin-graphql)

[Explore the GraphQL Admin API  
  

The GraphQL Admin API lets you read and write Shopify data, including products, customers, orders, inventory, fulfillment, and more.

Explore the GraphQL Admin API to learn about the available types and operations.](/docs/api/admin-graphql)

[![](/images/icons/32/apps.png)![](/images/icons/32/apps-dark.png)

Learn more about extending Shopify

Learn about the most common places where apps can add functionality to the Shopify platform, and the related APIs and tools available for building.

Learn more about extending Shopify

Learn about the most common places where apps can add functionality to the Shopify platform, and the related APIs and tools available for building.](/docs/apps/getting-started/app-surfaces)

[Learn more about extending Shopify  
  

Learn about the most common places where apps can add functionality to the Shopify platform, and the related APIs and tools available for building.](/docs/apps/getting-started/app-surfaces)

[![](/images/icons/32/apps.png)![](/images/icons/32/apps-dark.png)

Select an app distribution method

Decide how you want to share your app with users. For example, you might make your app available in the Shopify App Store, and bill customers for usage.

Select an app distribution method

Decide how you want to share your app with users. For example, you might make your app available in the Shopify App Store, and bill customers for usage.](/docs/apps/distribution)

[Select an app distribution method  
  

Decide how you want to share your app with users. For example, you might make your app available in the Shopify App Store, and bill customers for usage.](/docs/apps/distribution)

[![](/images/icons/32/build.png)![](/images/icons/32/build-dark.png)

Deploy your app

Follow our guide to deploy your React Router app to a testing or production environment.

Deploy your app

Follow our guide to deploy your React Router app to a testing or production environment.](/docs/apps/launch/deployment)

[Deploy your app  
  

Follow our guide to deploy your React Router app to a testing or production environment.](/docs/apps/launch/deployment)

Was this page helpful?

YesNo