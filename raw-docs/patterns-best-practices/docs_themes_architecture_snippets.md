---
source: https://shopify.dev/docs/themes/architecture/snippets
---

---

## [Anchor to Overview](/docs/storefronts/themes/architecture/snippets#overview)Overview

Snippets are reusable pieces of Liquid code that help you maintain consistency and reduce duplication across your theme. They let you encapsulate complex logic and markup into separate files that can be rendered anywhere in your theme.

Unlike [sections](/docs/storefronts/themes/architecture/sections) and [blocks](/docs/storefronts/themes/architecture/blocks), snippets are invisible to merchants in the theme editor. They're ideal for code that needs to be repeated throughout your theme, such as product cards, navigation elements, or form components.

---

## [Anchor to How to use snippets](/docs/storefronts/themes/architecture/snippets#how-to-use-snippets)How to use snippets

Use the `render` tag to reference snippets in your Liquid code. It accepts named parameters that you can use to pass data to the snippet.

9

1

2

3

4

5

{% render 'product-card',

product: product,

show\_price: true,

max\_description\_length: 120

%}

For additional options for passing data to snippets, see [render tag parameters](/docs/api/liquid/tags/render).

### [Anchor to Variable scoping](/docs/storefronts/themes/architecture/snippets#variable-scoping)Variable scoping

Inside snippets, you can't directly access variables that are created outside the snippet. However, you can:

* Access global objects like `product`, `collection`, and `section`
* Receive specific variables passed as parameters

  Variables created inside a snippet remain local to that snippet and aren't accessible
  outside of it.

---

## [Anchor to Documenting snippets with LiquidDoc](/docs/storefronts/themes/architecture/snippets#documenting-snippets-with-liquiddoc)Documenting snippets with LiquidDoc

[LiquidDoc](/docs/storefronts/themes/tools/liquid-doc) enables you to build and use snippets more effectively by providing a structured way to add documentation to your snippets.

This documentation integrates with development tools to provide real-time feedback, parameter validation, and code completion while you work.

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

{% doc %}

Product card snippet

@param {string} title - The title to display

@param {number} [max\_items] - Optional maximum number of items to show

@example

{% render 'example-snippet', title: 'Featured Products', max\_items: 3 %}

{% enddoc %}

Learn more about how to [use LiquidDoc to work more effectively with snippets](/docs/storefronts/themes/tools/liquid-doc).

---

## [Anchor to Next steps](/docs/storefronts/themes/architecture/snippets#next-steps)Next steps

* [Learn more about LiquidDoc](/docs/storefronts/themes/tools/liquid-doc)
* [Learn more about the render tag](/docs/api/liquid/tags/render)

---

Was this page helpful?

YesNo