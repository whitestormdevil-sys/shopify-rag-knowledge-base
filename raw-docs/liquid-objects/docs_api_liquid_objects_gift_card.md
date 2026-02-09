---
source: https://shopify.dev/docs/api/liquid/objects/gift_card
---

A [gift card](https://help.shopify.com/manual/products/gift-card-products) that's been issued to a customer or a recipient.

## Properties

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-balance) 

balance**balance** [number](/docs/api/liquid/basics#number)

:   The remaining balance of the gift card in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-code) 

code**code** [string](/docs/api/liquid/basics#string)

:   The code used to redeem the gift card.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-currency) 

currency**currency** [string](/docs/api/liquid/basics#string)

:   The [ISO code](https://www.iso.org/iso-4217-currency-codes.html) of the currency that the gift card was issued in.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-customer) 

customer**customer** [customer](/docs/api/liquid/objects/customer)

:   The customer associated with the gift card.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-enabled) 

enabled**enabled** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the gift card is enabled. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-expired) 

expired**expired** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the gift card is expired. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-expires_on) 

expires\_on**expires\_on** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the gift card expires.

    If the gift card never expires, then `nil` is returned.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-initial_value) 

initial\_value**initial\_value** [number](/docs/api/liquid/basics#number)

:   The initial balance of the gift card in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted amount.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted amount.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-last_four_characters) 

last\_four\_characters**last\_four\_characters** [string](/docs/api/liquid/basics#string)

:   The last 4 characters of the code used to redeem the gift card.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-message) 

message**message** [string](/docs/api/liquid/basics#string)

:   The personalized message intended for the recipient.

    If there is no message intended for the recipient, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-pass_url) 

pass\_url**pass\_url** [string](/docs/api/liquid/basics#string)

:   The URL to download the gift card as an Apple Wallet Pass.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-product) 

product**product** [product](/docs/api/liquid/objects/product)

:   The product associated with the gift card.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-properties) 

properties**properties**

:   The [line item properties](/docs/api/liquid/objects/line_item#line_item-properties) assigned to the gift card.

    If there aren't any line item properties, then an [`EmptyDrop`](/docs/api/liquid/basics#emptydrop) is returned.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-qr_identifier) 

qr\_identifier**qr\_identifier** [string](/docs/api/liquid/basics#string)

:   A string used to generate a QR code for the gift card.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-recipient) 

recipient**recipient** [recipient](/docs/api/liquid/objects/recipient)

:   The recipient associated with the gift card.

    If there is no recipient associated with the gift card, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-send_on) 

send\_on**send\_on** [string](/docs/api/liquid/basics#string)

:   The scheduled date on which the gift card will be sent to the recipient.

    If the gift card does not have a scheduled date, then `nil` is returned.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the date.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the date.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the date.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) assigned to the gift card.

    The name doesn't include the `gift_card.` prefix, or the `.liquid` file extension.

    If a custom template isn't assigned to the gift card, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/gift_card#gift_card-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The URL to view the gift card. This URL is on the `checkout.shopify.com` domain.

    Tip

    The page at this URL is rendered through the [`gift_card.liquid` template](/themes/architecture/templates/gift-card-liquid)
    of the theme.

    **Tip:**

    The page at this URL is rendered through the [`gift_card.liquid` template](/themes/architecture/templates/gift-card-liquid)
    of the theme.

    **Tip:** The page at this URL is rendered through the <a href="/themes/architecture/templates/gift-card-liquid"><code><span class="PreventFireFoxApplyingGapToWBR">gift<wbr/>\_card.liquid</span></code> template</a>
    of the theme.

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

{

"balance": 5000,

"code": "WCGX 7X97 K9HJ DFR8",

"currency": "CAD",

"customer": {},

"enabled": true,

"expired": false,

"expires\_on": null,

"initial\_value": 5000,

"last\_four\_characters": "DFR8",

"message": null,

"send\_on": null,

"pass\_url": "https://polinas-potent-potions.myshopify.com/v1/passes/pass.com.shopify.giftcardnext/94af7fbe55d010130df8d8bc4a338d36/",

"product": {},

"properties": {},

"qr\_identifier": "shopify-giftcard-v1-3TKWJKJBM3X7PBRK",

"recipient": null,

"template\_suffix": null,

"url": "https://checkout.shopify.com/gift\_cards/56174706753/0011c591fc720d0a51b80cdb694f969e"

}

##### Example

```liquid
{
  "balance": 5000,
  "code": "WCGX 7X97 K9HJ DFR8",
  "currency": "CAD",
  "customer": {},
  "enabled": true,
  "expired": false,
  "expires_on": null,
  "initial_value": 5000,
  "last_four_characters": "DFR8",
  "message": null,
  "send_on": null,
  "pass_url": "https://polinas-potent-potions.myshopify.com/v1/passes/pass.com.shopify.giftcardnext/94af7fbe55d010130df8d8bc4a338d36/",
  "product": {},
  "properties": {},
  "qr_identifier": "shopify-giftcard-v1-3TKWJKJBM3X7PBRK",
  "recipient": null,
  "template_suffix": null,
  "url": "https://checkout.shopify.com/gift_cards/56174706753/0011c591fc720d0a51b80cdb694f969e"
}
```

[Anchor to](/docs/api/liquid/objects/gift_card#template-using) 

## Templates using gift\_card

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturegift\_card.liquid template

Theme architecture

gift\_card.liquid template](/themes/architecture/templates/gift-card-liquid)

Was this section helpful?

YesNo