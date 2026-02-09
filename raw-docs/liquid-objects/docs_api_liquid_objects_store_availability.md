---
source: https://shopify.dev/docs/api/liquid/objects/store_availability
---

A variant's inventory information for a physical store location.

If a location doesn't stock a variant, then there won't be a `store_availability` for that variant and location.

---

Note

The `store_availability` object is defined only if one or more locations has [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup)
enabled.

**Note:**

The `store_availability` object is defined only if one or more locations has [local pickup](https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup)
enabled.

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">store<wbr/>\_availability</span></code> object is defined only if one or more locations has <a href="https://help.shopify.com/manual/shipping/setting-up-and-managing-your-shipping/local-methods/local-pickup">local pickup</a>
enabled.

---

## Properties

[Anchor to](/docs/api/liquid/objects/store_availability#store_availability-available) 

available**available** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant has available inventory at the location. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/store_availability#store_availability-location) 

location**location** [location](/docs/api/liquid/objects/location)

:   The location that the variant is stocked at.

[Anchor to](/docs/api/liquid/objects/store_availability#store_availability-pick_up_enabled) 

pick\_up\_enabled**pick\_up\_enabled** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the location has pickup enabled. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/store_availability#store_availability-pick_up_time) 

pick\_up\_time**pick\_up\_time** [string](/docs/api/liquid/basics#string)

:   The amount of time that it takes for pickup orders to be ready at the location.

    Tip

    This value can be configured in the Shopify admin. To learn more, visit the [Shopify Help Center](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/local-pickup-for-online-orders#manage-preferences-for-a-local-pickup-location).

    **Tip:**

    This value can be configured in the Shopify admin. To learn more, visit the [Shopify Help Center](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/local-pickup-for-online-orders#manage-preferences-for-a-local-pickup-location).

    **Tip:** This value can be configured in the Shopify admin. To learn more, visit the <a href="https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/local-pickup-for-online-orders#manage-preferences-for-a-local-pickup-location">Shopify Help Center</a>.

9

1

2

3

4

5

6

{

"available": true,

"location": {},

"pick\_up\_enabled": true,

"pick\_up\_time": "Usually ready in 24 hours"

}

##### Example

```liquid
{
  "available": true,
  "location": {},
  "pick_up_enabled": true,
  "pick_up_time": "Usually ready in 24 hours"
}
```

Was this section helpful?

YesNo