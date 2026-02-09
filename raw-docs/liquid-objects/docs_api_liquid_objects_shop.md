---
source: https://shopify.dev/docs/api/liquid/objects/shop
---

Information about the store, such as the store address, the total number of products, and various settings.

## Properties

[Anchor to](/docs/api/liquid/objects/shop#shop-accepts_gift_cards) 

accepts\_gift\_cards**accepts\_gift\_cards** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the store accepts gift cards. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/shop#shop-address) 

address**address** [address](/docs/api/liquid/objects/address)

:   The address of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-brand) 

brand**brand** [brand](/docs/api/liquid/objects/brand)

:   The [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets) for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-collections_count) 

collections\_count**collections\_count** [number](/docs/api/liquid/basics#number)

:   The number of collections in the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-currency) 

currency**currency** [string](/docs/api/liquid/basics#string)

:   The currency of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-customer_accounts_enabled) 

customer\_accounts\_enabled**customer\_accounts\_enabled** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the store shows a login link. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/shop#shop-customer_accounts_optional) 

customer\_accounts\_optional**customer\_accounts\_optional** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if customer accounts are optional to complete checkout. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/shop#shop-description) 

description**description** [string](/docs/api/liquid/basics#string)

:   The [description](https://help.shopify.com/manual/online-store/setting-up/preferences#edit-the-title-and-meta-description)
    of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-domain) 

domain**domain** [string](/docs/api/liquid/basics#string)

:   The primary domain of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-email) 

email**email** [string](/docs/api/liquid/basics#string)

:   The [sender email](https://help.shopify.com/manual/intro-to-shopify/initial-setup/setup-your-email#change-your-sender-email-address)
    of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-enabled_currencies) 

enabled\_currencies**enabled\_currencies** array of [currency](/docs/api/liquid/objects/currency)

:   The currencies that the store accepts.

    Tip

    You can get the store's currency with [`shop.currency`](/docs/api/liquid/objects/shop#shop-currency).

    **Tip:**

    You can get the store's currency with [`shop.currency`](/docs/api/liquid/objects/shop#shop-currency).

    **Tip:** You can get the store&#39;s currency with <a href="/docs/api/liquid/objects/shop#shop-currency"><code>shop.currency</code></a>.

[Anchor to](/docs/api/liquid/objects/shop#shop-enabled_payment_types) 

enabled\_payment\_types**enabled\_payment\_types** array of [string](/docs/api/liquid/basics#string)

:   The accepted payment types on the store.

    The payment types are based on the store's enabled [payment providers](https://help.shopify.com/manual/payments) and
    the customer's current region and currency.

    Tip

    You can output an `svg` logo for each payment type with the [`payment_type_svg_tag` filter](/docs/api/liquid/filters/payment_type_svg_tag).
    Alternatively, you can get the source URL for each `svg` with the [`payment_type_img_url` filter](/docs/api/liquid/filters/payment_type_img_url).

    **Tip:**

    You can output an `svg` logo for each payment type with the [`payment_type_svg_tag` filter](/docs/api/liquid/filters/payment_type_svg_tag).
    Alternatively, you can get the source URL for each `svg` with the [`payment_type_img_url` filter](/docs/api/liquid/filters/payment_type_img_url).

    **Tip:** You can output an <code>svg</code> logo for each payment type with the <a href="/docs/api/liquid/filters/payment\_type\_svg\_tag"><code><span class="PreventFireFoxApplyingGapToWBR">payment<wbr/>\_type<wbr/>\_svg<wbr/>\_tag</span></code> filter</a>.
    Alternatively, you can get the source URL for each <code>svg</code> with the <a href="/docs/api/liquid/filters/payment\_type\_img\_url"><code><span class="PreventFireFoxApplyingGapToWBR">payment<wbr/>\_type<wbr/>\_img<wbr/>\_url</span></code> filter</a>.

[Anchor to](/docs/api/liquid/objects/shop#shop-id) 

id**id** [string](/docs/api/liquid/basics#string)

:   The ID of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the store.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/shop#shop-money_format) 

money\_format**money\_format** [currency](/docs/api/liquid/objects/currency)

:   The money format of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-money_with_currency_format) 

money\_with\_currency\_format**money\_with\_currency\_format** [currency](/docs/api/liquid/objects/currency)

:   The money format of the store with the currency included.

[Anchor to](/docs/api/liquid/objects/shop#shop-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   The name of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-password_message) 

password\_message**password\_message** [string](/docs/api/liquid/basics#string)

:   The password page message of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-permanent_domain) 

permanent\_domain**permanent\_domain** [string](/docs/api/liquid/basics#string)

:   The `.myshopify.com` domain of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-phone) 

phone**phone** [string](/docs/api/liquid/basics#string)

:   The phone number of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-policies) 

policies**policies** array of [policy](/docs/api/liquid/objects/policy)

:   The policies for the store.

    The policies are set in the store's [Policies settings](https://www.shopify.com/admin/settings/legal).

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the policies

    9

    1

    2

    3

    4

    5

    <ul>

    {%- for policy in shop.policies %}

    <li>{{ policy.title }}</li>

    {%- endfor %}

    </ul>

    ##### Code

    ```liquid
    <ul>
    {%- for policy in shop.policies %}
      <li>{{ policy.title }}</li>
    {%- endfor %}
    </ul>
    ```

    ##### Data

    ```liquid
    {
      "shop": {
        "policies": [
          "<p>We have a 30-day return policy, which means you have 30 days after receiving your item to request a return. ...</p>",
          "<p>This Privacy Policy describes how polinas-potent-potions.myshopify.com (the “Site” or “we”) collects, uses, and discloses your Personal Information when you visit or make a purchase from the Site. ...</p>",
          "<strong>OVERVIEW</strong> <br> This website is operated by Polina's Potent Potions. Throughout the site, the terms “we”, “us” and “our” refer to Polina's Potent Potions. ...",
          "<meta charset=\"utf-8\">\n<p data-mce-fragment=\"1\">All orders are processed within X to X business days (excluding weekends and holidays) after receiving your order confirmation email. You will receive another notification when your order has shipped. ...&nbsp;</p>\n<h3 data-mce-fragment=\"1\"></h3>"
        ]
      }
    }
    ```

    ## Output

    9

    1

    2

    3

    4

    5

    6

    <ul>

    <li>Refund policy</li>

    <li>Privacy policy</li>

    <li>Terms of service</li>

    <li>Shipping policy</li>

    </ul>

    ##### Output

    ```liquid
    <ul>
      <li>Refund policy</li>
      <li>Privacy policy</li>
      <li>Terms of service</li>
      <li>Shipping policy</li>
    </ul>
    ```

[Anchor to](/docs/api/liquid/objects/shop#shop-privacy_policy) 

privacy\_policy**privacy\_policy** [policy](/docs/api/liquid/objects/policy)

:   The privacy policy for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-products_count) 

products\_count**products\_count** [number](/docs/api/liquid/basics#number)

:   The number of products in the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-published_locales) 

published\_locales**published\_locales** array of [shop\_locale](/docs/api/liquid/objects/shop_locale)

:   The locales (languages) that are published on the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-refund_policy) 

refund\_policy**refund\_policy** [policy](/docs/api/liquid/objects/policy)

:   The refund policy for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-secure_url) 

secure\_url**secure\_url** [string](/docs/api/liquid/basics#string)

:   The full URL of the store, with an `https` protocol.

[Anchor to](/docs/api/liquid/objects/shop#shop-shipping_policy) 

shipping\_policy**shipping\_policy** [policy](/docs/api/liquid/objects/policy)

:   The shipping policy for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-subscription_policy) 

subscription\_policy**subscription\_policy** [policy](/docs/api/liquid/objects/policy)

:   The subscription policy for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-terms_of_service) 

terms\_of\_service**terms\_of\_service** [policy](/docs/api/liquid/objects/policy)

:   The terms of service for the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-types) 

types**types** array of [string](/docs/api/liquid/basics#string)

:   All of the product types in the store.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the product types

    9

    1

    2

    3

    {% for type in shop.types %}

    {{- type | link\_to\_type }}

    {% endfor %}

    ##### Code

    ```liquid
    {% for type in shop.types %}
      {{- type | link_to_type }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "shop": {
        "types": [
          "",
          "Animals & Pet Supplies",
          "Baking Flavors & Extracts",
          "Container",
          "Cooking & Baking Ingredients",
          "Dried Flowers",
          "Fruits & Vegetables",
          "Gift Cards",
          "Health",
          "Health & Beauty",
          "Invisibility",
          "Love",
          "Music & Sound Recordings",
          "Seasonings & Spices",
          "Water"
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

    12

    13

    14

    15

    16

    17

    18

    19

    20

    21

    22

    23

    24

    25

    26

    27

    28

    29

    Unknown Type

    <a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>

    <a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>

    <a href="/collections/types?q=Container" title="Container">Container</a>

    <a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>

    <a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>

    <a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>

    <a href="/collections/types?q=Gift%20Cards" title="Gift Cards">Gift Cards</a>

    <a href="/collections/types?q=Health" title="Health">Health</a>

    <a href="/collections/types?q=Health%20%26%20Beauty" title="Health &amp; Beauty">Health & Beauty</a>

    <a href="/collections/types?q=Invisibility" title="Invisibility">Invisibility</a>

    <a href="/collections/types?q=Love" title="Love">Love</a>

    <a href="/collections/types?q=Music%20%26%20Sound%20Recordings" title="Music &amp; Sound Recordings">Music & Sound Recordings</a>

    <a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>

    <a href="/collections/types?q=Water" title="Water">Water</a>

    ##### Output

    ```liquid
    Unknown Type

    <a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>

    <a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>

    <a href="/collections/types?q=Container" title="Container">Container</a>

    <a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>

    <a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>

    <a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>

    <a href="/collections/types?q=Gift%20Cards" title="Gift Cards">Gift Cards</a>

    <a href="/collections/types?q=Health" title="Health">Health</a>

    <a href="/collections/types?q=Health%20%26%20Beauty" title="Health &amp; Beauty">Health & Beauty</a>

    <a href="/collections/types?q=Invisibility" title="Invisibility">Invisibility</a>

    <a href="/collections/types?q=Love" title="Love">Love</a>

    <a href="/collections/types?q=Music%20%26%20Sound%20Recordings" title="Music &amp; Sound Recordings">Music & Sound Recordings</a>

    <a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>

    <a href="/collections/types?q=Water" title="Water">Water</a>
    ```

[Anchor to](/docs/api/liquid/objects/shop#shop-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The full URL of the store.

[Anchor to](/docs/api/liquid/objects/shop#shop-vendors) 

vendors**vendors** array of [string](/docs/api/liquid/basics#string)

:   All of the product vendors for the store.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the vendors

    9

    1

    2

    3

    {% for vendor in shop.vendors %}

    {{- vendor | link\_to\_vendor }}

    {% endfor %}

    ##### Code

    ```liquid
    {% for vendor in shop.vendors %}
      {{- vendor | link_to_vendor }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "shop": {
        "vendors": [
          "Clover's Apothecary",
          "Polina's Potent Potions",
          "Ted's Apothecary Supply"
        ]
      }
    }
    ```

    ## Output

    9

    1

    2

    3

    4

    5

    <a href="/collections/vendors?q=Clover%27s%20Apothecary" title="Clover&#39;s Apothecary">Clover's Apothecary</a>

    <a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

    <a href="/collections/vendors?q=Ted%27s%20Apothecary%20Supply" title="Ted&#39;s Apothecary Supply">Ted's Apothecary Supply</a>

    ##### Output

    ```liquid
    <a href="/collections/vendors?q=Clover%27s%20Apothecary" title="Clover&#39;s Apothecary">Clover's Apothecary</a>

    <a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>

    <a href="/collections/vendors?q=Ted%27s%20Apothecary%20Supply" title="Ted&#39;s Apothecary Supply">Ted's Apothecary Supply</a>
    ```

## Deprecated Properties

[Anchor to](/docs/api/liquid/objects/shop#shop-enabled_locales) 

enabled\_locales**enabled\_locales** array of [shop\_locale](/docs/api/liquid/objects/shop_locale) Deprecated

:   The locales (languages) that are published on the store.

    Deprecated

    Deprecated because the name didn't make it clear that the returned locales were published.

    The `shop.enabled_locales` property has been replaced by [`shop.published_locales`](/docs/api/liquid/objects/shop#shop-published_locales).

    **Deprecated:**

    Deprecated because the name didn't make it clear that the returned locales were published.

    The `shop.enabled_locales` property has been replaced by [`shop.published_locales`](/docs/api/liquid/objects/shop#shop-published_locales).

[Anchor to](/docs/api/liquid/objects/shop#shop-locale) 

locale**locale** [shop\_locale](/docs/api/liquid/objects/shop_locale) Deprecated

:   The currently active locale (language).

    Deprecated

    Deprecated because this value is contextual to the request and not a property of the shop resource.

    The `shop.locale` property has been replaced by [request.locale](/docs/api/liquid/objects/request#request-locale).

    **Deprecated:**

    Deprecated because this value is contextual to the request and not a property of the shop resource.

    The `shop.locale` property has been replaced by [request.locale](/docs/api/liquid/objects/request#request-locale).

[Anchor to](/docs/api/liquid/objects/shop#shop-metaobjects) 

metaobjects**metaobjects** Deprecated

:   All of the [metaobjects](/docs/api/liquid/objects/metaobject) of the store.

    Deprecated

    The `shop.metaobjects` property has been replaced by [`metaobjects`](/docs/api/liquid/objects/metaobjects).

    **Deprecated:**

    The `shop.metaobjects` property has been replaced by [`metaobjects`](/docs/api/liquid/objects/metaobjects).

[Anchor to](/docs/api/liquid/objects/shop#shop-taxes_included) 

taxes\_included**taxes\_included** [boolean](/docs/api/liquid/basics#boolean) Deprecated

:   Returns `true` if prices include taxes. Returns `false` if not.

    Deprecated

    Deprecated because whether or not prices have taxes included is dependent on the customer's country.

    The `shop.taxes_included` property has been replaced by [cart.taxes\_included](/docs/api/liquid/objects/cart#cart-taxes_included).

    **Deprecated:**

    Deprecated because whether or not prices have taxes included is dependent on the customer's country.

    The `shop.taxes_included` property has been replaced by [cart.taxes\_included](/docs/api/liquid/objects/cart#cart-taxes_included).

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

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

{

"accepts\_gift\_cards": true,

"address": {},

"brand": {},

"collections\_count": 7,

"currency": "CAD",

"customer\_accounts\_enabled": true,

"customer\_accounts\_optional": true,

"description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",

"domain": "polinas-potent-potions.myshopify.com",

"email": "polinas.potent.potions@gmail.com",

"enabled\_currencies": [],

"enabled\_locales": [],

"enabled\_payment\_types": [

"visa",

"master",

"american\_express",

"paypal",

"diners\_club",

"discover"

],

"id": 56174706753,

"locale": "en",

"metafields": {},

"metaobjects": {},

"money\_format": "${{amount}}",

"money\_with\_currency\_format": "${{amount}} CAD",

"name": "Polina&#39;s Potent Potions",

"password\_message": "Our store will be opening when the moon is in the seventh house!!",

"permanent\_domain": "polinas-potent-potions.myshopify.com",

"phone": "416-123-1234",

"policies": [],

"privacy\_policy": {},

"products\_count": 19,

"published\_locales": [],

"refund\_policy": {},

"secure\_url": "https://polinas-potent-potions.myshopify.com",

"shipping\_policy": {},

"subscription\_policy": null,

"taxes\_included": false,

"terms\_of\_service": {},

"types": [

"",

"Animals & Pet Supplies",

"Baking Flavors & Extracts",

"Container",

"Cooking & Baking Ingredients",

"Dried Flowers",

"Fruits & Vegetables",

"Gift Cards",

"Health",

"Health & Beauty",

"Invisibility",

"Love",

"Music & Sound Recordings",

"Seasonings & Spices",

"Water"

],

"url": "https://polinas-potent-potions.myshopify.com",

"vendors": [

"Clover's Apothecary",

"Polina's Potent Potions",

"Ted's Apothecary Supply"

]

}

##### Example

```liquid
{
  "accepts_gift_cards": true,
  "address": {},
  "brand": {},
  "collections_count": 7,
  "currency": "CAD",
  "customer_accounts_enabled": true,
  "customer_accounts_optional": true,
  "description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",
  "domain": "polinas-potent-potions.myshopify.com",
  "email": "polinas.potent.potions@gmail.com",
  "enabled_currencies": [],
  "enabled_locales": [],
  "enabled_payment_types": [
    "visa",
    "master",
    "american_express",
    "paypal",
    "diners_club",
    "discover"
  ],
  "id": 56174706753,
  "locale": "en",
  "metafields": {},
  "metaobjects": {},
  "money_format": "${{amount}}",
  "money_with_currency_format": "${{amount}} CAD",
  "name": "Polina&#39;s Potent Potions",
  "password_message": "Our store will be opening when the moon is in the seventh house!!",
  "permanent_domain": "polinas-potent-potions.myshopify.com",
  "phone": "416-123-1234",
  "policies": [],
  "privacy_policy": {},
  "products_count": 19,
  "published_locales": [],
  "refund_policy": {},
  "secure_url": "https://polinas-potent-potions.myshopify.com",
  "shipping_policy": {},
  "subscription_policy": null,
  "taxes_included": false,
  "terms_of_service": {},
  "types": [
    "",
    "Animals & Pet Supplies",
    "Baking Flavors & Extracts",
    "Container",
    "Cooking & Baking Ingredients",
    "Dried Flowers",
    "Fruits & Vegetables",
    "Gift Cards",
    "Health",
    "Health & Beauty",
    "Invisibility",
    "Love",
    "Music & Sound Recordings",
    "Seasonings & Spices",
    "Water"
  ],
  "url": "https://polinas-potent-potions.myshopify.com",
  "vendors": [
    "Clover's Apothecary",
    "Polina's Potent Potions",
    "Ted's Apothecary Supply"
  ]
}
```

Was this section helpful?

YesNo