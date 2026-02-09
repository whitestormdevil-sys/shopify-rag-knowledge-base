---
source: https://shopify.dev/docs/api/liquid/objects/page
---

A [page](https://help.shopify.com/manual/online-store/themes/theme-structure/pages) on a store.

## Properties

[Anchor to](/docs/api/liquid/objects/page#page-author) 

author**author** [string](/docs/api/liquid/basics#string)

:   The author of the page.

[Anchor to](/docs/api/liquid/objects/page#page-content) 

content**content** [string](/docs/api/liquid/basics#string)

:   The content of the page.

[Anchor to](/docs/api/liquid/objects/page#page-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the page.

[Anchor to](/docs/api/liquid/objects/page#page-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the page.

[Anchor to](/docs/api/liquid/objects/page#page-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the page.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/page#page-published_at) 

published\_at**published\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the page was published.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/page#page-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) assigned to the page.

    The name doesn't include the `page.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the page, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/page#page-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the page.

[Anchor to](/docs/api/liquid/objects/page#page-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the page.

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

{

"author": null,

"content": "<p>Polina's Potent Potions was started by Polina in 1654.</p>\n<p>We use all-natural locally sourced ingredients for our potions.</p>",

"handle": "about-us",

"id": 83536642113,

"metafields": {},

"published\_at": "2022-05-04 17:47:03 -0400",

"template\_suffix": "",

"title": "About us",

"url": {}

}

##### Example

```liquid
{
  "author": null,
  "content": "<p>Polina's Potent Potions was started by Polina in 1654.</p>\n<p>We use all-natural locally sourced ingredients for our potions.</p>",
  "handle": "about-us",
  "id": 83536642113,
  "metafields": {},
  "published_at": "2022-05-04 17:47:03 -0400",
  "template_suffix": "",
  "title": "About us",
  "url": {}
}
```

[Anchor to](/docs/api/liquid/objects/page#template-using) 

## Templates using page

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturepage template

Theme architecture

page template](/themes/architecture/templates/page)

Was this section helpful?

YesNo