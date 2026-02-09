---
source: https://shopify.dev/docs/apps/build/pos/getting-started
---

This tutorial shows you how to create a simple Shopify app using only POS UI extensions. This type of app is called an extension-only app, where all of your code runs in the extension on the merchant's device. To learn more about extension-only apps, and about apps that use code hosted on a server, see [Extension-only and server-hosted apps](/docs/apps/build/pos#extension-only-and-server-hosted-apps).

The app you'll build displays a tile on the POS app home screen. When users tap the tile, the app shows a modal with a message displaying the name of the store.

---

## [Anchor to What you'll learn](/docs/apps/build/pos/getting-started#what-youll-learn)What you'll learn

In this tutorial, you'll learn how to do the following tasks:

* Scaffold an extension for a Shopify POS extension-only app using Shopify CLI.
* Add some basic functionality to the scaffolded extension.
* Test your app in Shopify POS.

---

## [Anchor to Requirements](/docs/apps/build/pos/getting-started#requirements)Requirements

* Create a [partner account](https://www.shopify.com/partners).
* Create a [dev store](/docs/apps/tools/development-stores#create-a-development-store-to-test-your-app).
* Install the latest version of [Shopify CLI](/docs/api/shopify-cli).
* Install the [Shopify POS app](https://www.shopify.com/pos/pos-app) on your [Android](https://play.google.com/store/apps/details?id=com.shopify.pos&hl=en_US) or [iOS](https://apps.apple.com/us/app/shopify-point-of-sale-pos/id686830644) device.

---

## [Anchor to Step 1: Scaffold an extension-only app](/docs/apps/build/pos/getting-started#step-1-scaffold-an-extension-only-app)Step 1: Scaffold an extension-only app

Create a framework for building an extension-only app using Shopify CLI. Run the following command in your project directory:

$

$

shopify app init

Shopify CLI will present you with a series of prompts. Respond to the prompts as follows:

* **Get started building your app:** Choose `Build an extension-only app`.
* **Which organization is this work for:** Choose the organization linked to your dev store.
* **Create this project as a new app on Shopify:** Choose `Yes, create it as a new app`.
* **App name:** Enter `my-pos-extension-app`.

When you run `shopify app init` for an extension-only app, Shopify CLI creates an app containing just configuration files and an empty folder for your extension code. This empty app doesn't do anything, but it's needed to attach your extension to.

---

## [Anchor to Step 2: Scaffold a POS UI extension](/docs/apps/build/pos/getting-started#step-2-scaffold-a-pos-ui-extension)Step 2: Scaffold a POS UI extension

Create a POS UI extension for your app using Shopify CLI by running the following commands in your project directory:

$

$

$

cd my-pos-extension-app

shopify app generate extension

When prompted to choose the type of extension, select `POS smart grid`. For the extension name, select the default name (`pos-smart-grid`).

Running this command creates the basic code and configuration files for an app that displays a tile on the POS app's smart grid. This code includes the following files:

* `shopify.extension.toml`: The [configuration file](/docs/api/pos-ui-extensions/latest#configuration) that defines your extension's [targets](/docs/api/pos-ui-extensions/latest/targets) and their corresponding code modules.
* `Tile.jsx`: Contains the code for the tile that the app creates on the POS smart grid. It renders the tile UI element and contains an `onClick` function to launch a modal when a user taps it.
* `Modal.jsx`: Contains code for the modal that launches when the tile is tapped. It renders the modal and displays the message "Welcome to the Preact extension."

To learn more about targets and UI components, see [Apps in POS](/docs/apps/build/pos) and the [POS UI extensions reference](/docs/api/pos-ui-extensions).

---

## [Anchor to Step 3: Connect the Shopify app and the extension to your dev store](/docs/apps/build/pos/getting-started#step-3-connect-the-shopify-app-and-the-extension-to-your-dev-store)Step 3: Connect the Shopify app and the extension to your dev store

Before you can install the extension on your mobile device, you need to connect the Shopify app and the extension you created to your dev store.

1. From your app's root directory (`my-pos-extension-app`), run the following command to start a local development server:

   $

   $

   shopify app dev

   This command connects your local extension to your dev store and creates a [Cloudflare tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) to serve the extension.
2. When you see the message `Ready, watching for changes in your app`, open the developer console for your dev store by pressing `p` on your keyboard.

---

## [Anchor to Step 4: Install the extension on your mobile device](/docs/apps/build/pos/getting-started#step-4-install-the-extension-on-your-mobile-device)Step 4: Install the extension on your mobile device

Install the extension in the POS app so you can test as you update your code.

1. On your mobile device, make sure you're logged into your dev store in the Shopify POS app.
2. In the developer console you opened in the previous step, click your extension's **View mobile** button to generate a QR code.
3. Scan the QR code with your device and tap the link to open the Shopify POS app.

The POS app on your device fetches your extension code from the Cloudflare tunnel URL and runs it inside the app. You should now see a new tile on the smart grid labeled **POS smart grid**. Tapping this tile opens a modal titled **POS modal** with the text “Welcome to the Preact extension.”

![Mobile device showing the POS smart grid tile](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/pos/GettingStartedScreenshot2-KjdP5ql-.png)


---

## [Anchor to Step 5: Update the smart-grid tile code](/docs/apps/build/pos/getting-started#step-5-update-the-smart-grid-tile-code)Step 5: Update the smart-grid tile code

When you created your extension, Shopify CLI added some placeholder code to a `Tile.jsx` file to render the smart-grid tile.

Update this code to change the headings on the tile:

1. Open the `Tile.jsx` file in your app's `extensions/pos-smart-grid/src` directory.
2. Replace the existing code with the code shown below.

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

   import {render} from 'preact';

   export default async () => {

   render(<Extension />, document.body);

   }

   function Extension() {

   return (

   <s-tile

   heading="Where am I?"

   subheading="Find your Shopify store"

   onClick={() => shopify.action.presentModal()}

   />

   );

   }

   This new code changes the heading and subheading of the tile from their default values.
3. Look at the tile on your device. You should see that the heading and subheadings have been updated to read "Where am I?" and "Find your Shopify store."

If you experience issues updating or loading the extension, see the [Troubleshooting](#troubleshooting) section.

---

## [Anchor to Step 6: Update the modal code](/docs/apps/build/pos/getting-started#step-6-update-the-modal-code)Step 6: Update the modal code

When you created your extension, Shopify CLI added some placeholder code to a `Modal.jsx` file to render a modal when the tile is tapped. This code displays the message "Welcome to the preact extension" that you saw when you opened the modal in [Step 4](#step-4-install-the-extension-on-your-mobile-device).

Update this code to retrieve the name of your dev store using the [GraphQL Admin API](/docs/api/admin-graphql/) and display it in the modal:

1. Open the `Modal.jsx` file in your app's `extensions/pos-smart-grid/src` directory.
2. Replace the existing code with the following.

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

   40

   41

   42

   43

   44

   45

   46

   47

   48

   49

   50

   51

   52

   53

   54

   55

   56

   57

   58

   59

   60

   import {render} from 'preact';

   // Import hooks for state management

   import {useState, useEffect} from 'preact/hooks';

   export default async () => {

   render(<Extension />, document.body);

   };

   function Extension() {

   // Set up states to track loading status of storename

   const [isLoading, setIsLoading] = useState(true);

   const [storeName, setStoreName] = useState('');

   // useEffect runs when the component mounts (modal opens)

   useEffect(() => {

   async function fetchStoreName() {

   try {

   // Define the GraphQL query to fetch the storename

   const requestBody = {

   query: `

   query {

   shop {

   name

   }

   }

   `

   };

   // Make a POST request to the GraphQL Admin API

   const response = await fetch('shopify:admin/api/graphql.json', {

   method: 'POST',

   headers: {

   'Content-Type': 'application/json',

   },

   body: JSON.stringify(requestBody)

   });

   const data = await response.json();

   // Extract the storename from the GraphQL response structure

   setStoreName(data.data.shop.name);

   } catch (error) {

   // If the API call fails, log the error and show a fallback message

   console.error('Failed to fetch store name:', error);

   setStoreName('Unknown');

   } finally {

   // Set loading to false whether the request succeeded or failed

   setIsLoading(false);

   }

   }

   // Call the function to fetch the store name

   fetchStoreName();

   }, []);

   return (

   <s-page heading='Where am I?'>

   <s-scroll-box>

   <s-box padding="small">

   <s-text>

   {isLoading ? 'Fetching store name...' : `You are in ${storeName}`}

   </s-text>

   </s-box>

   </s-scroll-box>

   </s-page>

   );

   }

This new code does the following to fetch your store's name from the GraphQL Admin API and display it in the modal:

* Imports hooks for state management.
* Sets up states to track whether the code is fetching data and to store the storename after it's been fetched.
* After rendering the modal component, finds the storename by directly accessing the GraphQL Admin API using `fetch()`.
* In the returned modal, displays "Fetching store name…" until the API call completes, then displays "You are in `${storename}`".

---

## [Anchor to Step 7: Verify your changes](/docs/apps/build/pos/getting-started#step-7-verify-your-changes)Step 7: Verify your changes

Tap the **Where am I?** tile in your POS app. You should now see a modal that displays a message with your storename:

![Mobile device showing the POS smart grid tile](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/apps/pos/GettingStartedScreenshot3-K_RS4cmS.png)


---

## [Anchor to Troubleshooting](/docs/apps/build/pos/getting-started#troubleshooting)Troubleshooting

When previewing extensions from your dev store on a mobile device, you might experience the following issues:

* After installing the extension, it disappears from the POS app's home screen.
* When updating your code, changes aren't reflected in the extension on your device.

These issues can occur due to network switches (between WiFI and cellular), Cloudflare Tunnel timeouts, or other interruptions. Additionally, closing the POS app or locking and unlocking your device can cause the app to remove the extension, especially in cases like WebSocket timeouts or when the local dev server stops.

If you encounter issues while following this tutorial, adjust your device settings and reload the extension.

### [Anchor to Device settings](/docs/apps/build/pos/getting-started#device-settings)Device settings

Change the settings on your device so that it doesn't automatically lock, and keep the POS app open after installing the extension.

### [Anchor to Reloading the extension](/docs/apps/build/pos/getting-started#reloading-the-extension)Reloading the extension

Reload the extension by following these steps:

1. If you can still see the extension's tile on your device, open the POS Dev Console in the POS app and tap **Remove dev extensions**.
2. In the terminal where your development server is running, press `Control + C` to stop the server.
3. Run `shopify app dev` to restart the server:
4. Press `p` on your keyboard to open the Developer Console.
5. Click **View mobile** to generate a new QR code.
6. Scan the QR code with your device to reload the extension.

---

## [Anchor to Next steps](/docs/apps/build/pos/getting-started#next-steps)Next steps

* If you're testing across multiple teams and won't be running the local dev server, consider using [app previews](/docs/apps/build/cli-for-apps/test-apps-locally#develop-and-test-apps-as-a-team).
* Learn how to build a [discount UI extension](/docs/apps/build/pos/tutorials/build-discount-extension), [print UI extension](/docs/apps/build/pos/tutorials/build-print-extension), or [subscription UI extension](/docs/apps/build/pos/tutorials/build-subscription-extension).
* Explore the full [reference section](/docs/api/pos-ui-extensions/latest) for targets, target APIs and Polaris web components that you can use for your POS UI extension.
* Learn how to [deploy and release an app extension](/docs/apps/deployment/app-versions).

---

Was this page helpful?

YesNo