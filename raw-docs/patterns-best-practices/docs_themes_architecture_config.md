---
source: https://shopify.dev/docs/themes/architecture/config
---

Config files define settings in the **Theme settings** area of the theme editor, as well as store their values.

Theme settings are a good place to host general settings such as typography and color options. Theme settings can be accessed through the [settings object](/docs/api/liquid/objects/settings).

Tip

You can also create settings for [sections](/docs/storefronts/themes/architecture/sections/section-schema#settings) and [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks). These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

**Tip:**

You can also create settings for [sections](/docs/storefronts/themes/architecture/sections/section-schema#settings) and [blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks). These settings are defined as part of the parent section or block object, and appear in the theme editor with the associated object.

---

## [Anchor to Location](/docs/storefronts/themes/architecture/config#location)Location

Config files are located in the `config` directory of the theme. When the theme contains market-specific customizations, the `markets.json` file is present in this directory:

9

1

2

3

4

5

6

7

└── theme

...

├── config

| ├── settings\_data.json

| ├── settings\_schema.json

| └── markets.json

└── locales

---

## [Anchor to Subtypes](/docs/storefronts/themes/architecture/config#subtypes)Subtypes

There are up to three config files, each with their own schema and content:

| Type | Description | Required |
| --- | --- | --- |
| [**settings\_schema.json**](/docs/storefronts/themes/architecture/config/settings-schema-json) | Controls the organization and content of the **Theme settings** area of the theme editor. | Yes |
| [**settings\_data.json**](/docs/storefronts/themes/architecture/config/settings-data-json) | Contains the saved values from the settings in `settings_schema.json`. | Yes |
| [**markets.json**](/docs/storefronts/themes/architecture/config/markets-json) | Sets the source of inheritance of market-specific theme customizations. | No |

---

## [Anchor to Usage](/docs/storefronts/themes/architecture/config#usage)Usage

When working with config files, you should familiarize yourself with the following:

* [Setting types](#setting-types)
* [Accessing settings](#access-settings)
* [Theme metadata](#theme-metadata)

### [Anchor to Setting types](/docs/storefronts/themes/architecture/config#setting-types)Setting types

There are two categories of settings:

| Category | Description |
| --- | --- |
| [Input settings](/docs/storefronts/themes/architecture/settings/input-settings) | Settings that can hold a value, and are configurable by app users. |
| [Sidebar settings](/docs/storefronts/themes/architecture/settings/sidebar-settings) | Settings that can’t hold a value, and aren’t configurable by app users. They’re informational elements that can be used to provide detail and clarity for your input settings. |

### [Anchor to Access settings](/docs/storefronts/themes/architecture/config#access-settings)Access settings

Theme settings can be accessed through the [settings object](/docs/api/liquid/objects/settings). To learn more about the syntax and considerations, refer to [Access settings](/docs/storefronts/themes/architecture/settings#access-settings).

### [Anchor to Theme metadata](/docs/storefronts/themes/architecture/config#theme-metadata)Theme metadata

You can add theme metadata to the **Theme actions** menu of the theme editor. This includes information like the theme name and version, where to find theme documentation, and theme developer contact details. To learn how to include this information in your theme, refer to [Add theme metadata](/docs/storefronts/themes/architecture/config/settings-schema-json#add-theme-metadata).

---

Was this page helpful?

YesNo