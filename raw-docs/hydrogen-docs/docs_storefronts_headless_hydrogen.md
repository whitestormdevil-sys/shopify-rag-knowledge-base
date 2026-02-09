---
source: https://shopify.dev/docs/storefronts/headless/hydrogen
---

This tutorial will walk you through the process of creating a new Hydrogen storefront, linking it to your Shopify store, and then deploying it to Oxygen.

#### [Anchor to Requirements](/docs/storefronts/headless/hydrogen/getting-started#requirements)Requirements

* [Node.js v16.20+](https://nodejs.org/) and [npm v8.19+](https://www.npmjs.com/)
* [Hydrogen channel](https://apps.shopify.com/hydrogen)

---

## [Anchor to Step 1: Create a new Hydrogen storefront](/docs/storefronts/headless/hydrogen/getting-started#step-1-create-a-new-hydrogen-storefront)Step 1: Create a new Hydrogen storefront

In your terminal, create a new Hydrogen project using example data from [Mock.shop](https://mock.shop):

9

1

npm create @shopify/hydrogen@latest -- --quickstart

Note

The `--quickstart` flag is shorthand for a set of [recommended options](/docs/api/shopify-cli/hydrogen/hydrogen-init#flags-propertydetail-quickstart) for trying Hydrogen. You can drop it to see the available customizations.

**Note:**

The `--quickstart` flag is shorthand for a set of [recommended options](/docs/api/shopify-cli/hydrogen/hydrogen-init#flags-propertydetail-quickstart) for trying Hydrogen. You can drop it to see the available customizations.

You'll see a confirmation message with some details about your new project:

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

Shopify: Mock.shop

Language: JavaScript

Routes:

• Home (/ & /:catchAll)

• Page (/pages/:handle)

• Cart (/cart/\* & /discount/\*)

• Products (/products/:handle)

• Collections (/collections & /collections/:handle)

• Policies (/policies & /policies/:handle)

• Blogs (/blogs/\*)

• Account (/account/\*)

• Search (/api/predictive-search & /search)

• Robots (/robots.txt)

• Sitemap (/sitemap.xml)

---

## [Anchor to Step 2: Run the dev server](/docs/storefronts/headless/hydrogen/getting-started#step-2-run-the-dev-server)Step 2: Run the dev server

After installation, open your new project and start the dev server:

9

1

2

cd hydrogen-quickstart

shopify hydrogen dev

Once the dev server is running, open <http://localhost:3000> in your browser and you'll see [Mock.shop](https://mock.shop) inventory:

![A Hydrogen storefront showing example data from Mock.shop](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/hydrogen/mockshop-screenshot-CwtXGip4.png)


---

## [Anchor to Step 3: Link your Hydrogen project to Shopify](/docs/storefronts/headless/hydrogen/getting-started#step-3-link-your-hydrogen-project-to-shopify)Step 3: Link your Hydrogen project to Shopify

By default, your Hydrogen project displays example products from [Mock.shop](https://mock.shop). To show your own products, link your local project to Shopify, create a new storefront, and sync your environment variables.

1. Link your Hydrogen project to Shopify:

   9

   1

   npx shopify hydrogen link

   Follow the prompts to log in to your Shopify account and create a new storefront:

   9

   1

   2

   3

   4

   5

   6

   7

   ✓ my-shopify-store

   ? Select a Hydrogen storefront to link:

   ✓ Create a new storefront

   ? New storefront name:

   > hydrogen-quickstart
2. Update your project's environment variables:

   9

   1

   npx shopify hydrogen env pull

   Your terminal will show a diff like this:

   9

   1

   2

   3

   4

   5

   6

   7

   - SESSION\_SECRET="foobar"

   - PUBLIC\_STORE\_DOMAIN="mock.shop"

   + PUBLIC\_STOREFRONT\_ID=[ID]

   + PUBLIC\_STOREFRONT\_API\_TOKEN=[TOKEN]

   + PRIVATE\_STOREFRONT\_API\_TOKEN=[TOKEN]

   + PUBLIC\_CUSTOMER\_ACCOUNT\_API\_CLIENT\_ID=[ID]

   + PUBLIC\_CUSTOMER\_ACCOUNT\_API\_URL=https://shopify.com/[ID]

To confirm that the link works, run `npm run dev` and open <http://localhost:3000>. You'll now see your storefront inventory in your browser:

![A Hydrogen storefront showing data from shopify](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/hydrogen/hydrogen-store-screenshot-BXy7MtyH.png)


---

## [Anchor to Step 4: Deploy to Oxygen](/docs/storefronts/headless/hydrogen/getting-started#step-4-deploy-to-oxygen)Step 4: Deploy to Oxygen

After your Hydrogen storefront is linked, you can deploy it to Oxygen hosting to make it publicly accessible:

1. Deploy your project to Oxygen:

   9

   1

   npx shopify hydrogen deploy
2. At the prompt to pick which environment to deploy to, select **Preview**.

The Hydrogen CLI builds your storefront, creates a new Oxygen deployment, and returns a preview link in your terminal. Open the preview link in your browser see deployment URL:

![A Hydrogen storefront deployment URL on oxygen](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/custom-storefronts/hydrogen/hydrogen-store-deployment-B5rE-XTf.png)


---

## [Anchor to Next steps](/docs/storefronts/headless/hydrogen/getting-started#next-steps)Next steps

Congratulations! You've created a new Hydrogen storefront, connected it to Shopify, and made your first deployment to Oxygen.

[![](/images/icons/48/custom-storefronts.png)![](/images/icons/48/custom-storefronts-dark.png)

Hydrogen and Oxygen fundamentals

Explore the key components of the Hydrogen and Oxygen stack and how they work together

Hydrogen and Oxygen fundamentals

Explore the key components of the Hydrogen and Oxygen stack and how they work together](/docs/storefronts/headless/hydrogen/fundamentals)

[Hydrogen and Oxygen fundamentals  
  

Explore the key components of the Hydrogen and Oxygen stack and how they work together](/docs/storefronts/headless/hydrogen/fundamentals)

---

Was this page helpful?

YesNo