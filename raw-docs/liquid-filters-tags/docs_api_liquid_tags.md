---
source: https://shopify.dev/docs/api/liquid/tags
---

# Liquid reference

Liquid is a template language created by Shopify. It's available as an [open source project](https://shopify.github.io/liquid/) on GitHub, and is used by many different software projects and companies.

This reference documents the Liquid tags, filters, and objects that you can use to build [Shopify Themes](/themes).

Ask assistant

## [Anchor to What is a template language?](/docs/api/liquid#what-is-a-template-language)What is a template language?

A template language allows you to create a single template to host static content, and dynamically insert information depending on where the template is rendered. For example, you can create a product template that hosts all of your standard product attributes, such as the product image, title, and price. That template can then dynamically render those attributes with the appropriate content, depending on the current product being viewed.

---

## [Anchor to Variations of Liquid](/docs/api/liquid#variations-of-liquid)Variations of Liquid

The variation of Liquid in this reference extends the open-source version of Liquid for use with [Shopify themes](/themes). It includes tags, filters, and objects that can be used to render objects specific to Shopify stores and storefront functionality.

Shopify also uses slightly different versions of Liquid to render dynamic content for the following features. These variations aren’t included in this reference.

[![](/images/icons/32/liquidnotificationstemplate.png)![](/images/icons/32/liquidnotificationstemplate-dark.png)

Notification templates

Notification templates](https://help.shopify.com/en/manual/orders/notifications/email-variables)

[Notification templates](https://help.shopify.com/en/manual/orders/notifications/email-variables)

[![](/images/icons/32/flow.png)![](/images/icons/32/flow-dark.png)

Shopify Flow

Shopify Flow](https://help.shopify.com/en/manual/shopify-flow/reference/variables#liquid-variables)

[Shopify Flow](https://help.shopify.com/en/manual/shopify-flow/reference/variables#liquid-variables)

[![](/images/icons/32/liquidordertemplate.png)![](/images/icons/32/liquidordertemplate-dark.png)

Order printer templates

Order printer templates](https://help.shopify.com/en/manual/fulfillment/managing-orders/printing-orders/shopify-order-printer/liquid-variables-and-filters-reference)

[Order printer templates](https://help.shopify.com/en/manual/fulfillment/managing-orders/printing-orders/shopify-order-printer/liquid-variables-and-filters-reference)

[![](/images/icons/32/liquidpackingsliptemplate.png)![](/images/icons/32/liquidpackingsliptemplate-dark.png)

Packing slip templates

Packing slip templates](https://help.shopify.com/en/manual/orders/packing-slips-variable-list)

[Packing slip templates](https://help.shopify.com/en/manual/orders/packing-slips-variable-list)

---

## [Anchor to Liquid basics](/docs/api/liquid#liquid-basics)Liquid basics

Liquid is used to dynamically output objects and their properties. You can further modify that output by creating logic with tags, or directly altering it with a filter. Objects and object properties are output using one of six basic data types. Liquid also includes basic logical and comparison operators for use with tags.

[![](/images/icons/32/liquid.png)![](/images/icons/32/liquid-dark.png)

Navigate toBasics

Navigate to

Basics](/docs/api/liquid/basics)

[Navigate to - Basics](/docs/api/liquid/basics)

---

## [Anchor to Defining logic with tags](/docs/api/liquid#defining-logic-with-tags)Defining logic with tags

Liquid tags are used to define logic that tells templates what to do.

Tags are wrapped with curly brace percentage delimiters `{% %}`.
The text within the delimiters is an instruction, not content to render.

In the example to the right, the `if` tag defines the condition to be met.
If `product.available` returns `true`, then the price is displayed.
Otherwise, the “sold out” message is shown.

`{% %}`

To nest multiple tags inside one set of delimiters, use the [`liquid`](/docs/api/liquid/tags/liquid) tag.

### [Anchor to Tags with parameters](/docs/api/liquid#tags-with-parameters)Tags with parameters

Some tags accept parameters: either required or optional.
For example, the `for` tag takes an optional `limit` parameter to stop the loop at a specific index.

---

## [Anchor to Modifying output with filters](/docs/api/liquid#modifying-output-with-filters)Modifying output with filters

Liquid filters modify the output of variables and objects.

To filter the output of a tag, use the pipe character `|`, followed by the filter.
In this example, `product` is the object, `title` is its property, and `upcase` is the filter.

### [Anchor to Filters with parameters](/docs/api/liquid#filters-with-parameters)Filters with parameters

Many filters accept parameters that adjust their output.
Some parameters are required, others are optional.

### [Anchor to Using multiple filters](/docs/api/liquid#using-multiple-filters)Using multiple filters

Multiple filters can be used on one output. They're applied from left to right.

---

## [Anchor to Referencing objects](/docs/api/liquid#referencing-objects)Referencing objects

Liquid objects represent variables that you can use to build your theme. Object types include, but aren't limited to:

* Store resources, such as a collection or product and its properties
* Standard content that is used to power Shopify themes, such as `content_for_header`
* Functional elements that can be used to build interactivity, such as `paginate` and `search`

Objects might represent a single data point, or contain multiple properties. Some products might represent a related object, such as a product in a collection.

`{{ }}`

Double curly brace delimiters denote an output.

### [Anchor to Usage](/docs/api/liquid#usage)Usage

To output an object, wrap it in curly brace delimiters `{{ }}`.

To output an object's property, use dot notation.
This example outputs the `product` object's `title` property.

### [Anchor to Object access](/docs/api/liquid#object-access)Object access

Objects can be accessed in three ways:

* **Globally**: Available in any Liquid file, excluding [checkout.liquid](/themes/architecture/layouts/checkout-liquid) and [Liquid asset files](/themes/architecture#assets)
* **In templates**: Available in specific templates and their sections or blocks. For example, the [`product`](/docs/api/liquid/objects/product) object in a [product template](/themes/architecture/templates/product)
* **Through parent objects**: Returned as properties of other objects. For example, [`article`](/docs/api/liquid/objects/article) objects through [`articles`](/docs/api/liquid/objects/articles) or [`blog`](/docs/api/liquid/objects/blog)

Check each object's documentation to see how it can be accessed.

### [Anchor to Creating variables](/docs/api/liquid#creating-variables)Creating variables

To create your own variables, use variable tags like [`assign`](/docs/api/liquid/tags/assign) or [`capture`](/docs/api/liquid/tags/capture).
Syntactically, Liquid treats variables the same as objects.

---

## [Anchor to Resources & tools](/docs/api/liquid#resources-and-tools)Resources & tools

[![](/images/icons/48/cheatsheet.png)![](/images/icons/48/cheatsheet-dark.png)

Liquid Cheat Sheet

A simple reference guide to the Liquid language.

Liquid Cheat Sheet

A simple reference guide to the Liquid language.](https://www.shopify.com/partners/shopify-cheat-sheet)

[Liquid Cheat Sheet  
  

A simple reference guide to the Liquid language.](https://www.shopify.com/partners/shopify-cheat-sheet)

[![](/images/icons/48/themecheck.png)![](/images/icons/48/themecheck-dark.png)

Theme Check

Command line-based linter for themes. Also comes as an official Visual Studio Code extension.

Theme Check

Command line-based linter for themes. Also comes as an official Visual Studio Code extension.](/themes/tools/theme-check)

[Theme Check  
  

Command line-based linter for themes. Also comes as an official Visual Studio Code extension.](/themes/tools/theme-check)

[![](/images/icons/48/cli.png)![](/images/icons/48/cli-dark.png)

Shopify CLI for Themes

A powerful command-line tool for building Shopify themes, and exploring Liquid code in a REPL interface.

Shopify CLI for Themes

A powerful command-line tool for building Shopify themes, and exploring Liquid code in a REPL interface.](/themes/tools/cli)

[Shopify CLI for Themes  
  

A powerful command-line tool for building Shopify themes, and exploring Liquid code in a REPL interface.](/themes/tools/cli)

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)

Open source liquid

Liquid is an open source project on GitHub.

Open source liquid

Liquid is an open source project on GitHub.](https://github.com/Shopify/liquid)

[Open source liquid  
  

Liquid is an open source project on GitHub.](https://github.com/Shopify/liquid)

---

Was this page helpful?

YesNo