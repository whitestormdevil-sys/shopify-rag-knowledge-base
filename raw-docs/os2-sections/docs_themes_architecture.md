---
source: https://shopify.dev/docs/themes/architecture
---

A theme controls the organization, features, and style of a merchant's online store. Theme code is organized with a [standard directory structure](#directory-structure-and-component-types) of files specific to Shopify themes, as well as supporting assets such as images, stylesheets, and scripts. To learn how themes fit into Shopify, and learn how to set up an environment to build and test themes, refer to the [Shopify themes overview](/docs/storefronts/themes/getting-started).

Note

If you're building a theme for the [Shopify Theme Store](/docs/storefronts/themes/store), then you need to meet certain [requirements](/docs/storefronts/themes/store/requirements) for the customization options that your theme offers, your theme's style, and the features that you include.

**Note:**

If you're building a theme for the [Shopify Theme Store](/docs/storefronts/themes/store), then you need to meet certain [requirements](/docs/storefronts/themes/store/requirements) for the customization options that your theme offers, your theme's style, and the features that you include.

Theme files fall into the following general categories:

* [**Markup and features**](#markup-and-features) - These files control the layout and functionality of a theme. They use Liquid to generate the HTML markup that makes up the pages of the merchant's online store.
* [**Supporting assets**](#supporting-assets) - These files are assets, scripts, or locale files that are either called or consumed by other files in the theme.
* [**Config files**](/docs/storefronts/themes/architecture/config) - These files use JSON to store configuration data that can be customized by merchants using the [theme editor](/docs/storefronts/themes/tools/online-editor).

---

## [Anchor to Markup and features](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#markup-and-features)Markup and features

The following components determine the organization of each page:

![The layout, template, sections, and blocks work together to organize each page.](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/architecture/all-components-ofotrT_I.png)

| Number | Component | Description |
| --- | --- | --- |
| 1 | The [layout file](/docs/storefronts/themes/architecture/layouts) | The base of the theme. Use the layout file to host repeated theme elements like headers and footers. |
| 2 | The [template](/docs/storefronts/themes/architecture/templates) | The template that controls what's displayed on a page. Each theme should include different types of templates to display different types of content, such as the [home page](/docs/storefronts/themes/architecture/templates/index-template) and [products](/docs/storefronts/themes/architecture/templates/product). You can also [create multiple templates for the same resource type](/docs/storefronts/themes/architecture/templates/alternate-templates) and associate them with your store resources, to allow for variation.  JSON templates act only as a wrapper for sections, while Liquid templates contain code. |
| 3 | The [section groups](/docs/storefronts/themes/architecture/section-groups) rendered by the layout | Containers that enable merchants to add, remove, and reorder sections in areas of the layout file such as the header and footer. |
| 4 | The [sections](/docs/storefronts/themes/architecture/sections) rendered by the template | Reusable, customizable modules of content that merchants can add to JSON templates and section groups. |
| 5 | The [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks) that each section contains | Reusable, customizable modules of content that can be added to sections, removed, and reordered. |
| 6 | The [snippets](/docs/storefronts/themes/architecture/snippets) being rendered | Reusable pieces of Liquid code that can be rendered anywhere in the theme. |

Features can be introduced into themes in Liquid template files, sections, blocks, and [snippets](/docs/storefronts/themes/architecture/snippets). You can implement theme features using Liquid, CSS, and JavaScript. A theme's features determine how customers can interact with the content on an online store. For example, your theme needs to allow customers to add products to a cart by providing a [Liquid `form` tag](/docs/api/liquid/tags/form) with a `product` type.

### [Anchor to JSON with comments](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#json-with-comments)JSON with comments

Theme files with JSON support comments and trailing commas. Users can add comments within `config/settings_schema.json` and within schema tags.

For example:

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

[

{

/\* context about theme schema settings \*/

"name": "theme\_info",

"theme\_name": "Dawn",

"theme\_author": "Shopify",

"theme\_version": "1.0.0",

"theme\_documentation\_url": "https:\/\/help.shopify.com\/manual\/online-store\/themes\/os20\/themes-by-shopify\/dawn",

"theme\_support\_url": "https:\/\/support.shopify.com\/",

},

{

"name": "t:settings\_schema.colors.name",

"settings": [

{

"type": "header",

"content": "t:settings\_schema.colors.settings.header\_\_1.content", // some useful context + see trailing comma

},

...

]

Files that users typically don't edit won't persist comments or trailing commas. This includes the following:

9

1

2

3

4

templates/\*.json

sections/\*.json (section groups)

config/settings\_data.json

locales/\*.json

Note

If you're using the Assets API to fetch and parse theme files, then you'll need to adopt a JSON parser that supports comments and trailing commas. The `unstable` version of the Admin API will add an autogenerated comment at the top of files that do not persist comments. This comment header will appear in files in the next stable version of the Admin API, `2024-10`

**Note:**

If you're using the Assets API to fetch and parse theme files, then you'll need to adopt a JSON parser that supports comments and trailing commas. The `unstable` version of the Admin API will add an autogenerated comment at the top of files that do not persist comments. This comment header will appear in files in the next stable version of the Admin API, `2024-10`

---

## [Anchor to Supporting assets](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#supporting-assets)Supporting assets

You can add supporting assets to your theme to control the presentation of components and features, or to store reusable pieces of code that can be used across components.

For example, you need to add assets to style the theme. These resources help to define the aesthetic of the online store and how content sections are styled to express the merchant’s brand. The style of a theme is defined by the CSS and JavaScript applied to layout, template, and section files. Liquid and HTML that you want to reuse across your theme can be stored in [snippets](/docs/storefronts/themes/architecture#snippets). Theme CSS and JavaScript is stored in the [assets](/docs/storefronts/themes/architecture#assets) directory of the theme.

In addition, you can translate your theme into different languages using locale files. Locale files contain a set of translations for text strings that are used throughout the theme, and are stored in the [locales](/docs/storefronts/themes/architecture/locales) directory of the theme.

---

## [Anchor to Directory structure and component types](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#directory-structure-and-component-types)Directory structure and component types

Themes must use the following directory structure:

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

.

├── assets

├── blocks

├── config

├── layout

├── locales

├── sections

├── snippets

└── templates

└── customers

└── metaobject

Subdirectories, other than the ones listed, aren't supported.

To see an example of a complete theme directory structure, and the various component types, explore the [Dawn GitHub repository](https://github.com/Shopify/dawn).

Note

Only a `layout` directory containing a `theme.liquid` file is required for the theme to be uploaded to Shopify.

**Note:**

Only a `layout` directory containing a `theme.liquid` file is required for the theme to be uploaded to Shopify.

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#assets)`assets`

The `assets` directory contains all of the assets used in a theme, including image, CSS, and JavaScript files.

Use the [asset\_url](/docs/api/liquid/filters/asset_url) Liquid URL filter to reference an asset within your theme.

You can access limited Liquid functionality in non-binary asset files by appending a `.liquid` extension. Common use cases include JavaScript (`.js.liquid`) and CSS (`.css.liquid`) files. Files with this extension have access to the following features:

* The [settings object](/docs/api/liquid/objects/settings)
* Liquid [filters](/docs/api/liquid/filters)

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#config)`config`

The `config` directory contains the [config files](/docs/storefronts/themes/architecture/config) for a theme. Config files define [settings](/docs/storefronts/themes/architecture/settings) in the **Theme settings** area of the theme editor, as well as store their values.

Theme settings are a good place to host general settings such as typography and color options. Theme settings can be accessed through the [settings object](/docs/api/liquid/objects/settings).

Tip

You can also create settings for [sections](/docs/storefronts/themes/architecture/sections/section-schema#settings) and [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks). These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

**Tip:**

You can also create settings for [sections](/docs/storefronts/themes/architecture/sections/section-schema#settings) and [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks). These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#layout)`layout`

The `layout` directory contains the [layout files](/docs/storefronts/themes/architecture/layouts) for a theme, through which [template](/docs/storefronts/themes/architecture#templates) files are rendered.

Layouts are Liquid files that enable you to include content that should be repeated on multiple page types in a single location. For example, layouts are a good place to include any content you might want in your `<head>` element, as well as [section groups](/docs/storefronts/themes/architecture/section-groups) for headers and footers.

A `theme.liquid` file must exist in this folder for the theme to be uploaded to Shopify.

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#locales)`locales`

The `locales` directory contains the [locale files](/docs/storefronts/themes/architecture/locales) for a theme, which are used to provide translated content. Locale files allow you to provide a translated experience in the [theme editor](/docs/storefronts/themes/tools/online-editor), provide translations for the online store, and allow merchants to customize text in the online store.

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#sections)`sections`

The `sections` directory contains a theme’s [sections](/docs/storefronts/themes/architecture/sections) and [section groups](/docs/storefronts/themes/architecture/section-groups).

Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants. They can also include [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks) which allow merchants to add, remove, and reorder content within a section.

Section groups are JSON containers that allow merchants to add, remove, and reorder sections in areas of the layout file such as the header and footer.

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#snippets)`snippets`

The `snippets` directory contains Liquid [snippet](/docs/storefronts/themes/architecture/snippets) files that host smaller reusable snippets of code. Snippets are reusable pieces of Liquid code that can be rendered anywhere in your theme, and are invisible to merchants in the theme editor.

Tip

You can provide [LiquidDoc](/docs/storefronts/themes/tools/liquid-doc.md) definitions which will enable additional tooling support through the [Shopify VS Code Extension](/docs/storefronts/themes/tools/shopify-liquid-vscode)

**Tip:**

You can provide [LiquidDoc](/docs/storefronts/themes/tools/liquid-doc.md) definitions which will enable additional tooling support through the [Shopify VS Code Extension](/docs/storefronts/themes/tools/shopify-liquid-vscode)

### [Anchor to [object Object]](/docs/storefronts/themes/architecture?utm_campaign=social_care&utm_medium=community&utm_source=social#templates)`templates`

The `templates` directory contains a theme’s [template files](/docs/storefronts/themes/architecture/templates), which control what's rendered on each type of page.

The `templates/customers` directory contains the template files for legacy customer account pages, like login and account overview.

You can use the template to add functionality that makes sense for the page type. For example, you can add additional product recommendations to a product template, or add a comment form to an article template. You can also [create multiple versions of the same template type](/docs/storefronts/themes/architecture/templates/alternate-templates) to create custom templates for different use cases.

No templates are required. However, you need to have a matching template for any page type that you want to render. For example, to render a product page, you need at least one template of type `product`.

---

Was this page helpful?

YesNo