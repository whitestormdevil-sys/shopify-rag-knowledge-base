---
source: https://shopify.dev/docs/api/liquid/objects/selling_plan_group
---

Information about a specific group of [selling plans](/apps/subscriptions/selling-plans) that include any of a
product's variants.

Selling plans are grouped based on shared [selling plan option names](/docs/api/liquid/objects/selling_plan_option#selling_plan_option-name).

To learn about how to support selling plans in your theme, refer to [Purchase options](/themes/pricing-payments/purchase-options).

## Properties

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-app_id) 

app\_id**app\_id** [string](/docs/api/liquid/basics#string)

:   An optional string provided by an app to identify selling plan groups created by that app.

    If the app doesn't provide a value, then `nil` is returned.

    Tip

    You can use this property, with the [`where` filter](/docs/api/liquid/filters/where), to filter the
    [`product.selling_plan_groups` array](/docs/api/liquid/objects/product#product-selling_plan_groups) for all selling plan groups
    from a specific app.

    **Tip:**

    You can use this property, with the [`where` filter](/docs/api/liquid/filters/where), to filter the
    [`product.selling_plan_groups` array](/docs/api/liquid/objects/product#product-selling_plan_groups) for all selling plan groups
    from a specific app.

    **Tip:** You can use this property, with the <a href="/docs/api/liquid/filters/where"><code>where</code> filter</a>, to filter the
    <a href="/docs/api/liquid/objects/product#product-selling\_plan\_groups"><code><span class="PreventFireFoxApplyingGapToWBR">product.selling<wbr/>\_plan<wbr/>\_groups</span></code> array</a> for all selling plan groups
    from a specific app.

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the selling plan group.

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the selling plan group.

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-options) 

options**options** array of [selling\_plan\_group\_option](/docs/api/liquid/objects/selling_plan_group_option)

:   The selling plan group options.

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-selling_plan_selected) 

selling\_plan\_selected**selling\_plan\_selected** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the currently selected selling plan is part of the selling plan group. Returns `false` if not.

    Note

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:**

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:** The selected selling plan is determined by the <code><span class="PreventFireFoxApplyingGapToWBR">selling<wbr/>\_plan</span></code> URL parameter.

[Anchor to](/docs/api/liquid/objects/selling_plan_group#selling_plan_group-selling_plans) 

selling\_plans**selling\_plans** array of [selling\_plan](/docs/api/liquid/objects/selling_plan)

:   The selling plans in the group.

9

1

2

3

4

5

6

7

8

{

"app\_id": "gid://shopify/App/66228322305",

"id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",

"name": "1 Week(s), 4 Week(s)",

"options": [],

"selling\_plan\_selected": false,

"selling\_plans": []

}

##### Example

```liquid
{
  "app_id": "gid://shopify/App/66228322305",
  "id": "e88ff8fdb3c39c89b564859e34542e0b982076d6",
  "name": "1 Week(s), 4 Week(s)",
  "options": [],
  "selling_plan_selected": false,
  "selling_plans": []
}
```

Was this section helpful?

YesNo