---
source: https://shopify.dev/docs/api/storefront/2024-10/queries/menu
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Retrieve a [navigation menu](https://help.shopify.com/manual/online-store/menus-and-links) by its handle.

* handle (String!)

[Anchor to handle](/docs/api/storefront/latest/queries/menu#arguments-handle)handle •[String!](/docs/api/storefront/latest/scalars/String) required
:   The navigation menu's handle.

---

Was this section helpful?

YesNo

## [Anchor to Possible returns](/docs/api/storefront/latest/queries/menu#possible-returns)Possible returns

* Menu (Menu)

[Anchor to Menu](/docs/api/storefront/latest/queries/menu#returns-Menu)Menu •[Menu](/docs/api/storefront/latest/objects/Menu)
:   A [navigation menu](https://help.shopify.com/manual/online-store/menus-and-links) representing a hierarchy
    of hyperlinks (items).

    Show fields

    [Anchor to handle](/docs/api/storefront/latest/queries/menu#returns-Menu.fields.handle)handle •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
    :   The menu's handle.

    [Anchor to id](/docs/api/storefront/latest/queries/menu#returns-Menu.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null Token access required
    :   A globally-unique ID.

    [Anchor to items](/docs/api/storefront/latest/queries/menu#returns-Menu.fields.items)items •[[MenuItem!]!](/docs/api/storefront/latest/objects/MenuItem) non-null Token access required
    :   The menu's child items.

        Show fields

    [Anchor to itemsCount](/docs/api/storefront/latest/queries/menu#returns-Menu.fields.itemsCount)itemsCount •[Int!](/docs/api/storefront/latest/scalars/Int) non-null Token access required
    :   The count of items on the menu.

    [Anchor to title](/docs/api/storefront/latest/queries/menu#returns-Menu.fields.title)title •[String!](/docs/api/storefront/latest/scalars/String) non-null Token access required
    :   The menu's title.

---

Was this section helpful?

YesNo