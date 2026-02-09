---
source: https://shopify.dev/docs/api/liquid/objects/linklist
---

A [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus) in a store.

To learn about how to implement navigation in a theme, refer to [Add navigation to your theme](/themes/navigation-search/navigation).

## Properties

[Anchor to](/docs/api/liquid/objects/linklist#linklist-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the menu.

[Anchor to](/docs/api/liquid/objects/linklist#linklist-levels) 

levels**levels** [number](/docs/api/liquid/basics#number)

:   The number of nested levels in the menu.

    Note

    There's a maximum of 3 levels.

    **Note:**

    There's a maximum of 3 levels.

    **Note:** There&#39;s a maximum of 3 levels.

[Anchor to](/docs/api/liquid/objects/linklist#linklist-links) 

links**links** array of [link](/docs/api/liquid/objects/link)

:   The links in the menu.

[Anchor to](/docs/api/liquid/objects/linklist#linklist-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the menu.

9

1

2

3

4

5

6

{

"handle": "main-menu",

"levels": 2,

"links": [],

"title": "Main menu"

}

##### Example

```liquid
{
  "handle": "main-menu",
  "levels": 2,
  "links": [],
  "title": "Main menu"
}
```

Was this section helpful?

YesNo