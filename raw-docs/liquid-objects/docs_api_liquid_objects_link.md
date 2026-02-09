---
source: https://shopify.dev/docs/api/liquid/objects/link
---

A link in a [menu](https://help.shopify.com/manual/online-store/menus-and-links/drop-down-menus).

To learn about how to implement navigation in a theme, refer to [Add navigation to your theme](/themes/navigation-search/navigation).

## Properties

[Anchor to](/docs/api/liquid/objects/link#link-active) 

active**active** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the link is active. Returns `false` if not.

    A link is considered to be active if the current URL path matches, or contains, the link's [url](/docs/api/liquid/objects/link#link-url).
    For example, if the current URL path is `/blog/potion-notions/new-potions-for-spring`, then the following link URLs
    would be considered active:

    * `/blog/potion-notions/new-potions-for-spring`
    * `/blog/potion-notions`

    Tip

    The `link.active` property is useful for menu designs that highlight when top-level navigation categories are being
    viewed. For example, if a customer is viewing an article from the "Potion notions" blog, then the "Potion notions" link
    is highlighted in the menu.

    **Tip:**

    The `link.active` property is useful for menu designs that highlight when top-level navigation categories are being
    viewed. For example, if a customer is viewing an article from the "Potion notions" blog, then the "Potion notions" link
    is highlighted in the menu.

    **Tip:** The <code>link.active</code> property is useful for menu designs that highlight when top-level navigation categories are being
    viewed. For example, if a customer is viewing an article from the &quot;Potion notions&quot; blog, then the &quot;Potion notions&quot; link
    is highlighted in the menu.

[Anchor to](/docs/api/liquid/objects/link#link-child_active) 

child\_active**child\_active** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if a link's child link is active. Returns `false` if not.

    A link is considered to be active if the current URL path matches, or contains, the [URL](/docs/api/liquid/objects/link#link-url) of
    the link.

    For example, if the current URL path is `/blog/potion-notions/new-potions-for-spring`, then the following link URLs
    would be considered active:

    * `/blog/potion-notions/new-potions-for-spring`
    * `/blog/potion-notions`

[Anchor to](/docs/api/liquid/objects/link#link-child_current) 

child\_current**child\_current** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if current URL path matches a link's child link [URL](/docs/api/liquid/objects/link#link-url). Returns `false` if not.

    Note

    URL parameters are ignored when determining a match.

    Product URLs [within the context of a collection](/docs/api/liquid/filters/within) and standard product URLs are treated
    the same.

    **Note:**

    URL parameters are ignored when determining a match.

    Product URLs [within the context of a collection](/docs/api/liquid/filters/within) and standard product URLs are treated
    the same.

    **Note:** URL parameters are ignored when determining a match.</p>
    <p>Product URLs <a href="/docs/api/liquid/filters/within">within the context of a collection</a> and standard product URLs are treated
    the same.

[Anchor to](/docs/api/liquid/objects/link#link-current) 

current**current** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the current URL path matches the [URL](/docs/api/liquid/objects/link#link-url) of the link. Returns `false` if not.

    Note

    URL parameters are ignored when determining a match.

    Product URLs [within the context of a collection](/docs/api/liquid/filters/within) are treated as equal to a standard product
    URL for the same product.

    **Note:**

    URL parameters are ignored when determining a match.

    Product URLs [within the context of a collection](/docs/api/liquid/filters/within) are treated as equal to a standard product
    URL for the same product.

    **Note:** URL parameters are ignored when determining a match.</p>
    <p>Product URLs <a href="/docs/api/liquid/filters/within">within the context of a collection</a> are treated as equal to a standard product
    URL for the same product.

[Anchor to](/docs/api/liquid/objects/link#link-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the link.

[Anchor to](/docs/api/liquid/objects/link#link-levels) 

levels**levels** [number](/docs/api/liquid/basics#number)

:   The number of nested levels under the link.

[Anchor to](/docs/api/liquid/objects/link#link-links) 

links**links** array of [link](/docs/api/liquid/objects/link)

:   The child links of the link.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Check the number of links

    9

    1

    2

    3

    4

    5

    6

    7

    {% for link in linklists.main-menu.links -%}

    {% if link.links.size > 0 -%}

    - {{ link.title }} ({{ link.links.size }} children)<br>

    {%- else -%}

    - {{ link.title }}<br>

    {%- endif %}

    {%- endfor %}

    ##### Code

    ```liquid
    {% for link in linklists.main-menu.links -%}
      {% if link.links.size > 0 -%}
        - {{ link.title }} ({{ link.links.size }} children)<br>
      {%- else -%}
        - {{ link.title }}<br>
      {%- endif %}
    {%- endfor %}
    ```

    ##### Data

    ```liquid
    {
      "linklists": {
        "main-menu": {
          "links": [
            "LinkDrop",
            "LinkDrop",
            "LinkDrop"
          ]
        }
      }
    }
    ```

    ## Output

    9

    1

    2

    3

    - Home<br>

    - Catalog (2 children)<br>

    - Contact<br>

    ##### Output

    ```liquid
    - Home<br>
    - Catalog (2 children)<br>
    - Contact<br>
    ```

[Anchor to](/docs/api/liquid/objects/link#link-object) 

object**object**

:   The object associated with the link.

    The object can be one of the following:

    * [`article`](/docs/api/liquid/objects/article)
    * [`blog`](/docs/api/liquid/objects/blog)
    * [`collection`](/docs/api/liquid/objects/collection)
    * [`metaobject`](/docs/api/liquid/objects/link/docs/api/liquid/objects/metaobject)
    * [`page`](/docs/api/liquid/objects/page)
    * [`policy`](/docs/api/liquid/objects/policy)
    * [`product`](/docs/api/liquid/objects/product)

[Anchor to](/docs/api/liquid/objects/link#link-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the link.

[Anchor to](/docs/api/liquid/objects/link#link-type) 

type**type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of the link.

    | Possible values | Description |
    | --- | --- |
    | article\_link | The link points to an article. |
    | blog\_link | The link points to an blog. |
    | catalog\_link | The link points to the [catalog page](https://help.shopify.com/manual/online-store/themes/customizing-themes/change-catalog-page). |
    | collection\_link | The link points to a collection. |
    | collections\_link | The link points to the [collection list page](/themes/architecture/templates/list-collections). |
    | customer\_account\_page\_link | The link points to a [customer account page](https://shopify.dev/docs/apps/build/customer-accounts/full-page-extensions). |
    | frontpage\_link | The link points to the home page. |
    | http\_link | The link points to an external web page, or a product type or vendor collection. |
    | metaobject\_link | The link points to a metaobject page. |
    | page\_link | The link points to a [page](https://help.shopify.com/manual/online-store/themes/theme-structure/pages). |
    | policy\_link | The link points to a [policy page](https://help.shopify.com/manual/checkout-settings/refund-privacy-tos#add-links-to-your-policies-within-pages-or-on-social-media). |
    | product\_link | The link points to a product page. |
    | search\_link | The link points to the search page. |

[Anchor to](/docs/api/liquid/objects/link#link-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The URL of the link.

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

{

"active": false,

"child\_active": false,

"child\_current": false,

"current": false,

"handle": {},

"levels": 0,

"links": [],

"object": {},

"title": {},

"type": "page\_link",

"url": "/pages/contact"

}

##### Example

```liquid
{
  "active": false,
  "child_active": false,
  "child_current": false,
  "current": false,
  "handle": {},
  "levels": 0,
  "links": [],
  "object": {},
  "title": {},
  "type": "page_link",
  "url": "/pages/contact"
}
```

Was this section helpful?

YesNo