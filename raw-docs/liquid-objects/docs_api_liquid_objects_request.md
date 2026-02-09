---
source: https://shopify.dev/docs/api/liquid/objects/request
---

Information about the current URL and the associated page.

## Properties

[Anchor to](/docs/api/liquid/objects/request#request-design_mode) 

design\_mode**design\_mode** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the request is being made from within the theme editor. Returns `false` if not.

    You can use `request.design_mode` to control theme behavior depending on whether the theme is being viewed in the editor.
    For example, you can prevent session data from being tracked by tracking scripts in the theme editor.

    Caution

    You shouldn't use `request.design_mode` to change customer-facing functionality. The theme editor preview should match
    what the merchant's customers see on the live store.

    **Caution:**

    You shouldn't use `request.design_mode` to change customer-facing functionality. The theme editor preview should match
    what the merchant's customers see on the live store.

    **Caution:** You shouldn&#39;t use <code><span class="PreventFireFoxApplyingGapToWBR">request.design<wbr/>\_mode</span></code> to change customer-facing functionality. The theme editor preview should match
    what the merchant&#39;s customers see on the live store.

[Anchor to](/docs/api/liquid/objects/request#request-host) 

host**host** [string](/docs/api/liquid/basics#string)

:   The domain that the request is hosted on.

[Anchor to](/docs/api/liquid/objects/request#request-locale) 

locale**locale** [shop\_locale](/docs/api/liquid/objects/shop_locale)

:   The locale of the request.

[Anchor to](/docs/api/liquid/objects/request#request-origin) 

origin**origin** [string](/docs/api/liquid/basics#string)

:   The protocol and host of the request.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Create a context-aware absolute URL

    You can use `request.origin` with any object, object property, or filter that returns a relative URL to build a context-aware absolute URL.

    9

    1

    {{ product.selected\_variant.url | default: product.url | prepend: request.origin }}

    ##### Code

    ```liquid
    {{ product.selected_variant.url | default: product.url | prepend: request.origin }}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "selected_variant": null,
        "url": "/products/health-potion"
      },
      "request": {
        "origin": "https://polinas-potent-potions.myshopify.com"
      }
    }
    ```

    ## Output

    9

    1

    https://polinas-potent-potions.myshopify.com/products/health-potion

    ##### Output

    ```liquid
    https://polinas-potent-potions.myshopify.com/products/health-potion
    ```

[Anchor to](/docs/api/liquid/objects/request#request-page_type) 

page\_type**page\_type** [string](/docs/api/liquid/basics#string) from a set of values

:   The type of page being requested.

    | Possible values |
    | --- |
    | 404 |
    | article |
    | blog |
    | captcha |
    | cart |
    | collection |
    | list-collections |
    | customers/account |
    | customers/activate\_account |
    | customers/addresses |
    | customers/login |
    | customers/order |
    | customers/register |
    | customers/reset\_password |
    | gift\_card |
    | index |
    | metaobject |
    | page |
    | password |
    | policy |
    | product |
    | search |

[Anchor to](/docs/api/liquid/objects/request#request-path) 

path**path** [string](/docs/api/liquid/basics#string)

:   The path of the request.

    Note

    If the current path is for a page that doesn't exist, then `nil` is returned.

    **Note:**

    If the current path is for a page that doesn't exist, then `nil` is returned.

    **Note:** If the current path is for a page that doesn&#39;t exist, then <code>nil</code> is returned.

[Anchor to](/docs/api/liquid/objects/request#request-visual_preview_mode) 

visual\_preview\_mode**visual\_preview\_mode** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the request is being made from within the theme editor's visual section preview. Returns `false` if not.

    You can use `request.visual_preview_mode` to control theme behavior depending on whether the theme is being viewed in the editor's visual section preview.
    For example, you can remove any scripts that interefere with how the section is displayed.

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

{

"design\_mode": false,

"host": "polinas-potent-potions.myshopify.com",

"locale": {},

"origin": "https://polinas-potent-potions.myshopify.com",

"page\_type": "index",

"path": "/",

"visual\_preview\_mode": false

}

##### Example

```liquid
{
  "design_mode": false,
  "host": "polinas-potent-potions.myshopify.com",
  "locale": {},
  "origin": "https://polinas-potent-potions.myshopify.com",
  "page_type": "index",
  "path": "/",
  "visual_preview_mode": false
}
```

Was this section helpful?

YesNo