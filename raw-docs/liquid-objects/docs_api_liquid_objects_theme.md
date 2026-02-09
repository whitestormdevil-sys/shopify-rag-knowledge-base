---
source: https://shopify.dev/docs/api/liquid/objects/theme
---

Information about the current theme.

deprecated

Deprecated because the values of this object's properties are subject to change, so can't be relied on within the theme.

If you want to link to the theme editor for the published theme, then you can use the URL path `/admin/themes/current/editor`.

While this object is deprecated in Liquid and shouldn't be used, you can still access it through the [REST Admin API](/api/admin-rest/current/resources/theme).

**deprecated:**

Deprecated because the values of this object's properties are subject to change, so can't be relied on within the theme.

If you want to link to the theme editor for the published theme, then you can use the URL path `/admin/themes/current/editor`.

While this object is deprecated in Liquid and shouldn't be used, you can still access it through the [REST Admin API](/api/admin-rest/current/resources/theme).

## Properties

[Anchor to](/docs/api/liquid/objects/theme#theme-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the theme.

[Anchor to](/docs/api/liquid/objects/theme#theme-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the theme.

[Anchor to](/docs/api/liquid/objects/theme#theme-role) 

role**role** [string](/docs/api/liquid/basics#string) from a set of values

:   The role of the theme.

    | Possible values | Description |
    | --- | --- |
    | main | The theme is published. Customers see it when they visit the online store. |
    | unpublished | The theme is unpublished. Customers can't see it. |
    | demo | The theme is installed on the store as a demo. The theme can't be published until the merchant buys the full version. |
    | development | The theme is used for development. The theme can't be published, and is temporary. |

9

1

2

3

4

5

{

"id": 124051750977,

"name": "Dawn",

"role": "main"

}

##### Example

```liquid
{
  "id": 124051750977,
  "name": "Dawn",
  "role": "main"
}
```

Was this section helpful?

YesNo