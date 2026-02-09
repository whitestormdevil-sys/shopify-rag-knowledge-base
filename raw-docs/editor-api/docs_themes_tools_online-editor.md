---
source: https://shopify.dev/docs/themes/tools/online-editor
---

The [theme editor](https://shopify.com/admin/themes/current/editor) is a tool that lets merchants customize the content and appearance of their store, and preview changes to their theme in real time.

As a theme developer, you can allow merchants to customize their theme in the theme editor by introducing [settings](#allowing-for-customization-through-the-theme-editor), and by dividing your theme functionality into [modular sections and blocks](/docs/storefronts/themes/best-practices/templates-sections-blocks).

You need to [integrate your theme with the theme editor](#integrating-your-theme-with-the-theme-editor) to create a seamless editing experience for merchants. In the theme editor preview, the merchant should see exactly what will appear in the storefront when the theme is live.

![The theme editor in the Shopify admin](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/theme_editor-fhUF7rbL.png)


---

## [Anchor to Accessing the theme editor through the Shopify admin](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-through-the-shopify-admin)Accessing the theme editor through the Shopify admin

Merchants can access the theme editor in the Shopify admin.

1. From the Shopify admin, go to **Online Store** > **Themes**.
2. Find the theme that you want to edit, and then click **Customize**.

---

## [Anchor to Accessing the theme editor during development](/docs/storefronts/themes/tools/online-editor#accessing-the-theme-editor-during-development)Accessing the theme editor during development

To understand how your theme settings appear to merchants, you can preview your theme in the theme editor. You can access the theme editor during development by using the following methods:

* Run your theme as a [development theme](/docs/storefronts/themes/tools/cli#development-themes) or [push your theme to a store](/docs/api/shopify-cli/theme/theme-push) using [Shopify CLI](/docs/api/shopify-cli/theme)
* Connect a GitHub branch to your store using the [Shopify GitHub integration](/docs/storefronts/themes/tools/github)
* Upload your theme as a ZIP to a Shopify store

You should choose the preview method that makes the most sense for your current development process.

---

## [Anchor to Allowing for customization through the theme editor](/docs/storefronts/themes/tools/online-editor#allowing-for-customization-through-the-theme-editor)Allowing for customization through the theme editor

The settings that a merchant can access in the theme editor are controlled by the theme. Settings can be specified in the following places:

* The theme's [config/settings\_schema.json](/docs/storefronts/themes/architecture/settings) file
* The setting attributes for each [section](/docs/storefronts/themes/architecture/sections/section-schema#settings) that's included in the theme.

When a merchant configures these settings using the theme editor, their configurations are saved. Learn more about [theme settings, and the types of settings that you can add to your theme](/docs/storefronts/themes/architecture/settings).

---

## [Anchor to Live preview](/docs/storefronts/themes/tools/online-editor#live-preview)Live preview

The theme editor can preview certain input settings as merchants interact with them, instead of refreshing the entire storefront preview after the merchant makes a selection.

The following input setting categories support live preview:

* [Color settings](#color-settings)
* [Text settings](#text-settings)

### [Anchor to Color settings](/docs/storefronts/themes/tools/online-editor#color-settings)Color settings

The theme editor can show a live preview of input settings that return a [`color` object](/docs/api/liquid/objects/color), including [color](/docs/storefronts/themes/architecture/settings/input-settings#color) and [color\_background](/docs/themes/architecture/settings/input-settings#color_background).

To allow the theme editor to preview color setting changes live, reference the setting in a `{% style %}` tag in a Liquid template, a section, or a snippet. You can reference the `color` object directly, or the one of the following properties of the object:

* `red`
* `green`
* `blue`
* `rgb`

#### [Anchor to Limitations](/docs/storefronts/themes/tools/online-editor#limitations)Limitations

The theme editor can't provide a live preview for color settings in the following cases:

* **Filtered settings**: The theme editor can't provide a live preview for color settings that have Liquid filters applied. For example, `{{ settings.colors_accent_2.rgb | replace ' ', ',' }}` can't be previewed live.
* **Stylesheets**: The theme editor can't provide a live preview for color settings that are referenced in stylesheets that are stored in the `/assets` directory of a theme. Instead, we recommend declaring a CSS variable in your `theme.liquid` layout file and referencing it in your theme's CSS files.

Refer to [theme.liquid](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/layout/theme.liquid#L67) and [base.css](https://github.com/Shopify/dawn/blob/d902375db0a71d5d2d6091eea242b71a42aa16ad/assets/base.css#L5) in Dawn for an example implementation.

### [Anchor to Text settings](/docs/storefronts/themes/tools/online-editor#text-settings)Text settings

The theme editor can show a live preview of plain or rich text settings. This includes the following settings:

* [text](/docs/storefronts/themes/architecture/settings/input-settings#text)
* [textarea](/docs/storefronts/themes/architecture/settings/input-settings#textarea)
* [inline\_richtext](/docs/themes/architecture/settings/input-settings#inline_richtext)
* [richtext](/docs/storefronts/themes/architecture/settings/input-settings#richtext)

To allow the theme editor to preview text settings live, the code where the setting is referenced must meet the following criteria:

* The setting value must be the only child of its parent HTML element:

|  |  |
| --- | --- |
| do | 9  1  <h1>{{ section.settings.title }}</h1> |
| do | 9  1  <h1><span className="icon">...</span> <span>{{ section.settings.title }}</span></h1> |
| don't | 9  1  <h1><span className="icon">...</span> {{ section.settings.title }}</h1> |

* There must be no Liquid filters applied to the setting value, other than the [`escape` filter](/docs/api/liquid/filters/escape):

|  |  |
| --- | --- |
| do | 9  1  <h1>{{ section.settings.title | escape }}</h1> |
| don't | 9  1  <h1>{{ section.settings.title | replace: ' ', '-' }}</h1> |

* The setting must not be preceded by, followed by, or wrapped by other Liquid markup inside of the parent HTML element:

|  |  |
| --- | --- |
| do | 9  1  2  3  {%- when 'heading' -%}  <h1>{{ block.settings.title }}</h1>  {%- endwhen -%} |
| don't | 9  1  2  3  4  <h1>  {%- assign title = block.settings.title -%}  {{ title }}  </h1> |
| don't | 9  1  2  3  4  5  <h1>  {%- when 'heading' -%}  {{ block.settings.title }}  {%- endwhen -%}  </h1> |

* The element must not be hidden when the page loads:

|  |  |
| --- | --- |
| don't | 9  1  2  3  {%- unless block.settings.title == blank -%}  <h1>{{ block.settings.title }}</h1>  {%- endunless -%} |

---

## [Anchor to Integrating your theme with the theme editor](/docs/storefronts/themes/tools/online-editor#integrating-your-theme-with-the-theme-editor)Integrating your theme with the theme editor

You need to make sure that your theme behaves in the editor the same way it would in the storefront. In some cases, you need to adjust your theme's behavior when it's being previewed in the theme editor to give merchants this experience.

To make your theme context-aware, you need to integrate with the theme editor.

Integrating with the theme editor allows you to do the following:

* Disable any code that should be run only when the theme is viewed by a customer
* Enable or disable any code that should be run only when the theme is being edited
* Make sure that any necessary code is run or cleaned up when a section is added, removed, customized, or moved

### [Anchor to Detecting the theme editor](/docs/storefronts/themes/tools/online-editor#detecting-the-theme-editor)Detecting the theme editor

Caution

You shouldn't use these methods to change the storefront preview that's displayed in the theme editor. In most cases, the preview that merchants see in the theme editor should match what their customers see on the live store.

A use case for this variable is to prevent theme editor session data from being included in any page tracking scripts. Another use case is working with a third-party API that returns and outputs any errors to the theme editor but never to the live store.

**Caution:**

You shouldn't use these methods to change the storefront preview that's displayed in the theme editor. In most cases, the preview that merchants see in the theme editor should match what their customers see on the live store.

A use case for this variable is to prevent theme editor session data from being included in any page tracking scripts. Another use case is working with a third-party API that returns and outputs any errors to the theme editor but never to the live store.

#### [Anchor to Using Liquid](/docs/storefronts/themes/tools/online-editor#using-liquid)Using Liquid

The [`request.design_mode`](/docs/themes/liquid/reference/objects/request#request-design_mode) global variable can be used in your theme's Liquid files to detect whether the storefront is being viewed in the theme editor. The value of the variable is set to `true` when viewing the theme editor. Otherwise, it's set to `false`.

9

1

2

3

{% if request.design\_mode %}

<!-- This will only render in the theme editor -->

{% endif %}

#### [Anchor to Using JavaScript](/docs/storefronts/themes/tools/online-editor#using-javascript)Using JavaScript

The `Shopify.designMode` global variable can be used in your theme's JavaScript files to detect whether the storefront is being viewed in the theme editor. The value of the variable is set to `true` when viewing the theme editor. Otherwise, it's set to `undefined`.

9

1

2

3

if (Shopify.designMode) {

// This will only happen in the theme editor

}

### [Anchor to Reacting to theme editor JavaScript events](/docs/storefronts/themes/tools/online-editor#reacting-to-theme-editor-javascript-events)Reacting to theme editor JavaScript events

When a merchant interacts with a section or block in the theme editor, or activates or deactivates the [theme editor preview inspector](https://help.shopify.com/manual/online-store/themes/customizing-themes/edit#preview-inspector), the theme editor emits JavaScript events. To learn about the actions that your code should take to account for these events, refer to [Integrate sections with the theme editor](/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks).

---

Was this page helpful?

YesNo