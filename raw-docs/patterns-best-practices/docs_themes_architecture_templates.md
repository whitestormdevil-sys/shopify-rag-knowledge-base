---
source: https://shopify.dev/docs/themes/architecture/templates
---

Templates control what's rendered on each type of page in a theme.

Each page type in an online store has an associated template type. You can use the template to add functionality that makes sense for the page type. For example, to render a product page, the theme needs at least one template of type `product`. Similarly, to render a metaobject page, the theme needs at least one template of type `metaobject/{metaobject-type}`, for example: `metaobject/book` or `metaobject/author`, depending on the type of metaobject definition.

You can create [multiple versions of the same template type](/docs/storefronts/themes/architecture/templates/alternate-templates) to create custom templates for different use cases. For example, you can create a separate product template for outerwear products, or a separate page template for pages with video content.

![Templates control what is rendered on each type of page in a theme.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/architecture/template-Ca5gymyj.png)

Templates control what is rendered on each type of page in a theme.



---

## [Anchor to JSON vs. Liquid](/docs/storefronts/themes/architecture/templates#json-vs-liquid)JSON vs. Liquid

There are two different file types you can use for a theme template: JSON and Liquid. These template file types can be used to build multiple [template types](#template-types), each of which represents a type of content in a merchant's online store.

| Type | Description |
| --- | --- |
| JSON | JSON templates are data files with the `.json` file extension. These templates let you easily populate your template with content from [sections](/docs/storefronts/themes/architecture/sections). Sections can be added, removed, or rearranged by merchants using the theme editor.  If you're using a JSON template, then any HTML or Liquid code needs to be included in a section that's referenced by the template.  To learn more, refer to [JSON templates](/docs/storefronts/themes/architecture/templates/json-templates). |
| Liquid | Liquid templates are [Liquid](/docs/api/liquid) markup files, with the `.liquid` file extension. You can add Liquid and HTML directly to Liquid templates.  To learn more, refer to [Liquid templates](/docs/storefronts/themes/architecture/templates/liquid-templates). |

### [Anchor to Choosing JSON vs Liquid](/docs/storefronts/themes/architecture/templates#choosing-json-vs-liquid)Choosing JSON vs Liquid

If you want to use [sections](/docs/storefronts/themes/architecture/sections) in a template, then you should use a JSON template.

JSON templates provide more flexibility for merchants to add, remove, and reorder sections, including app sections. Additionally, they minimize the amount of data in [settings\_data.json](/docs/storefronts/themes/architecture/config/settings-data-json). Instead, data is stored directly in the template, which improves the performance of the theme editor.

---

## [Anchor to Template types](/docs/storefronts/themes/architecture/templates#template-types)Template types

Each available template type represents a type of content in a merchant's online store. No template types are required. However, you must have a matching template for any page type that you want to render. For example, to render a product page, you need at least one template of type `product`.

You can have a maximum of 1000 JSON templates in your theme, across all template types. For example, if you have 20 JSON product templates, 10 JSON page templates, and 5 JSON collection templates, then you can add up to 965 additional templates to the theme.

You can use the following template types in your theme. To learn more about each template type, click on the template name.

| Type | Description |
| --- | --- |
| [404](/docs/storefronts/themes/architecture/templates/404) | Renders page content that is shown to customers if they enter an invalid URL for the store. |
| [article](/docs/storefronts/themes/architecture/templates/article) | Renders the article page, which contains the full content of the article, as well as an optional comments section for customers. This template is used for items like individual posts in a blog. |
| [blog](/docs/storefronts/themes/architecture/templates/blog) | Renders the blog page, which lists all articles within a blog. |
| [cart](/docs/storefronts/themes/architecture/templates/cart) | Renders the `/cart` page, which provides an overview of the contents of a customer’s cart. |
| [collection](/docs/storefronts/themes/architecture/templates/collection) | Renders the collection page, which lists all products within a collection. |
| [gift\_card.liquid](/docs/storefronts/themes/architecture/templates/gift-card-liquid) | Renders the gift card page, which displays the gift card issued to a customer upon purchase.  This must be a Liquid template. |
| [index](/docs/storefronts/themes/architecture/templates/index-template) | Renders the home page of the store, located at the root URL (`/`). |
| [list-collections](/docs/storefronts/themes/architecture/templates/list-collections) | Renders the collection list page, which lists all the store's collections. This page is located at the `/collections` URL of the store. |
| [page](/docs/storefronts/themes/architecture/templates/page) | Renders the shop’s pages, such as **About us** and **Contact us**. |
| [password](/docs/storefronts/themes/architecture/templates/password) | Renders the `/password` page, which is a landing page shown when you [add password protection to your online store](https://help.shopify.com/manual/online-store/themes/password-page). This page includes a message that is editable by merchants, and the password form for customers to gain access to the store. |
| [product](/docs/storefronts/themes/architecture/templates/product) | Renders the product page, which contains a product's media and content, as well as a form for customers to select a variant and add it to the cart. |
| [robots.txt.liquid](/docs/storefronts/themes/architecture/templates/robots-txt-liquid) | Renders the `robots.txt` file, which is hosted at the `/robots.txt` URL. This file tells search engines which pages can, or can't, be crawled on a site.  This must be a Liquid template. |
| [search](/docs/storefronts/themes/architecture/templates/search) | Renders the `/search` page, which displays the results of a [storefront search](https://help.shopify.com/manual/online-store/storefront-search). |
| [metaobject](/docs/storefronts/themes/architecture/templates/metaobject) | Renders metaobject pages, such as “artists” or “authors”. To render each metaobject entry as an individual page, the metaobject definition must have the web page capability. |

Note

The `gift_card` and `robots.txt` templates can't be JSON templates, so you must make them Liquid templates. Other template types support either template file type.

**Note:**

The `gift_card` and `robots.txt` templates can't be JSON templates, so you must make them Liquid templates. Other template types support either template file type.

### [Anchor to Legacy customer account templates](/docs/storefronts/themes/architecture/templates#legacy-customer-account-templates)Legacy customer account templates

Shopify has a new version of customer accounts, so you can exclude these legacy customer account templates from your theme. When a merchant publishes a theme that excludes these templates, they’ll be upgraded to the new version of customer accounts. Legacy customer accounts will eventually be deprecated. Learn more about [customer account versions](https://help.shopify.com/manual/customers/customer-accounts)

| Type | Description |
| --- | --- |
| [customers/account](/docs/storefronts/themes/architecture/templates/customers-account) | Renders the customer account page, which provides an overview of the customer’s account. |
| [customers/activate\_account](/docs/storefronts/themes/architecture/templates/customers-activate-account) | Renders the customer account activation page, which hosts the form for activating a customer account. |
| [customers/addresses](/docs/storefronts/themes/architecture/templates/customers-addresses) | Renders the customer addresses page, which allows customers to view and manage their current addresses, as well as add new ones. |
| [customers/login](/docs/storefronts/themes/architecture/templates/customers-login) | Renders the customer login page, which hosts the form for logging into a customer account. |
| [customers/order](/docs/storefronts/themes/architecture/templates/customers-order) | Renders the customer order page, which displays the details of a customer’s past orders. |
| [customers/register](/docs/storefronts/themes/architecture/templates/customers-register) | Renders the customer register page, which hosts the form for customer account creation. |
| [customers/reset\_password](/docs/storefronts/themes/architecture/templates/customers-reset-password) | Renders the password reset page, which hosts the form to reset the password for a customer account. |

---

## [Anchor to Location](/docs/storefronts/themes/architecture/templates#location)Location

Template files are located in the `templates` directory of the theme:

9

1

2

3

4

5

6

7

└── theme

├── layout

├── templates

| ├── 404.json

| ├── article.json

| ...

...

---

## [Anchor to Content](/docs/storefronts/themes/architecture/templates#content)Content

The content that you can include in a template depends on whether it is a JSON template or a Liquid template.

You should always keep the goal of the template type in mind when deciding what content you want to include in a template. For example, a product template, or a section in the product template, should always include the [`product` object](/docs/api/liquid/objects/product), which renders product details, and the [product form tag](/docs/api/liquid/tags/form#form-product), which lets customers add a product variant to the cart. Depending on your template type and approach, you might want to include these items in a [section](/docs/storefronts/themes/architecture/sections) that you reference in the template.

---

Was this page helpful?

YesNo