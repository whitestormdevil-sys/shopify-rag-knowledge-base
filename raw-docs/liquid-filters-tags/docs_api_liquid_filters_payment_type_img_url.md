---
source: https://shopify.dev/docs/api/liquid/filters/payment_type_img_url
---

9

1

string | payment\_type\_img\_url

returns [string](/docs/api/liquid/basics#string)

Returns the URL for an SVG image of a given [payment type](/docs/api/liquid/objects/shop#shop-enabled_payment_types).

9

1

2

3

{% for type in shop.enabled\_payment\_types %}

<img src="{{ type | payment\_type\_img\_url }}" width="50" height="50" />

{% endfor %}

##### Code

```liquid
{% for type in shop.enabled_payment_types %}
<img src="{{ type | payment_type_img_url }}" width="50" height="50" />
{% endfor %}
```

##### Data

```liquid
{
  "shop": {
    "enabled_payment_types": [
      "visa",
      "master",
      "american_express",
      "paypal",
      "diners_club",
      "discover"
    ]
  }
}
```

## Output

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

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/visa-65d650f7.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/master-54b5a7ce.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/american\_express-1efdc6a3.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/paypal-a7c68b85.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/diners\_club-678e3046.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment\_icons/discover-59880595.svg" width="50" height="50" />

##### Output

```liquid
<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/visa-65d650f7.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/master-54b5a7ce.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/american_express-1efdc6a3.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/paypal-a7c68b85.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/diners_club-678e3046.svg" width="50" height="50" />

<img src="//polinas-potent-potions.myshopify.com/cdn/shopifycloud/storefront/assets/payment_icons/discover-59880595.svg" width="50" height="50" />
```

Was this page helpful?

YesNo