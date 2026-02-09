---
source: https://shopify.dev/docs/themes/pricing-payments/installments
---

[Shop Pay Installments](https://help.shopify.com/manual/payments/shop-pay-installments) allows customers to pay for orders between 50 USD and 3,000 USD in 4 interest-free installments.

The Shop Pay Installments banner lets customers know that they have the option to pay in installments. It includes a **Learn more** link that opens a pop-up which shows how much the installment amount is, more information about installments, and any required disclosures.

|  |  |
| --- | --- |
| Shop Pay Installments banner on the product page | Shop Pay Installments banner on the cart page |
| Shop Pay Installments banner 'Learn more' pop-up | |

In this tutorial, you'll learn how to add a Shop Pay Installments banner to the following locations:

* [The product form](#add-the-banner-to-the-product-form)
* [The cart form](#add-the-banner-to-the-cart-form)

---

## [Anchor to Requirements](/docs/storefronts/themes/pricing-payments/installments#requirements)Requirements

Depending on where you want to add the Shop Pay Installments banner, you need to do one, or both, of the following:

* Add a [product form](/docs/api/liquid/tags/form#form-product) to a template. A product form can be added to any template that can access the [`product` object](/docs/api/liquid/objects/product).
* Add a [cart form](/docs/api/liquid/tags/form#form-cart) to a template. A cart form can be added to any template that can access the [`cart` object](/docs/api/liquid/objects/cart).

---

## [Anchor to Resources](/docs/storefronts/themes/pricing-payments/installments#resources)Resources

To implement this feature, you'll use the following:

* The [`form`](/docs/api/liquid/objects/form) object
* The [`payment_terms`](/docs/api/liquid/filters/payment_terms) filter

Tip

The `payment_terms` filter requires the `form` object from the Liquid [product form](/docs/api/liquid/tags/form#form-product) or [cart form](/docs/api/liquid/tags/form#form-cart). If your theme doesn't use these forms, then you can convert an HTML form to Liquid by [specifying any HTML attributes](/docs/api/liquid/tags/form#form-html-attributes) you need on the form.

**Tip:**

The `payment_terms` filter requires the `form` object from the Liquid [product form](/docs/api/liquid/tags/form#form-product) or [cart form](/docs/api/liquid/tags/form#form-cart). If your theme doesn't use these forms, then you can convert an HTML form to Liquid by [specifying any HTML attributes](/docs/api/liquid/tags/form#form-html-attributes) you need on the form.

---

## [Anchor to Implementing a Shop Pay Installments banner](/docs/storefronts/themes/pricing-payments/installments#implementing-a-shop-pay-installments-banner)Implementing a Shop Pay Installments banner

The Shop Pay Installments banner can be added to the following locations:

* [The product form](#add-the-banner-to-the-product-form)
* [The cart form](#add-the-banner-to-the-cart-form)

Note

The Shop Pay Installments banner appears only if Shop Pay Installments is enabled in the merchant's store.

**Note:**

The Shop Pay Installments banner appears only if Shop Pay Installments is enabled in the merchant's store.

### [Anchor to Add the banner to the product form](/docs/storefronts/themes/pricing-payments/installments#add-the-banner-to-the-product-form)Add the banner to the product form

To add a Shop Pay installments banner to the [product form](/docs/api/liquid/tags/form#form-product), you need to add a reference to the [`form` object](/docs/api/liquid/objects/form), with the [`payment_terms`](/docs/api/liquid/filters/payment_terms) filter applied, between the opening and closing `form` tags:

9

1

2

3

4

5

{% form 'product', product %}

<!-- product price -->

{{ form | payment\_terms }}

...

{% endform %}

The reference should be below the product price so that price and payment information is grouped together.

Note

The installments banner automatically updates based on the currently selected variant. The currently selected variant is noted by a form input with an attribute of `name="id"`.

**Note:**

The installments banner automatically updates based on the currently selected variant. The currently selected variant is noted by a form input with an attribute of `name="id"`.

If your theme doesn't include the price inside the product form, then you can create a second instance of the product form near the price display to host the installments banner. Inside this second form, you need to include a hidden `<input />` that notes the currently selected variant. This hidden input needs to be updated as the variant selection changes.

9

1

2

3

4

5

6

<!-- product price -->

{% form 'product', product %}

<input type="hidden" name="id" value="{{ product.selected\_or\_first\_available\_variant.id }}" />

{{ form | payment\_terms }}

{% endform %}

The `payment_terms` filter can be used anywhere that you can use a product form. It's commonly used in the [product template](/docs/storefronts/themes/architecture/templates/product), or a section inside of the template.

### [Anchor to Add the banner to the cart form](/docs/storefronts/themes/pricing-payments/installments#add-the-banner-to-the-cart-form)Add the banner to the cart form

To add a Shop Pay installments banner to the [cart form](/docs/api/liquid/tags/form#form-cart), you need to add a reference to the [`form` object](/docs/api/liquid/objects/form), with the [`payment_terms`](/docs/api/liquid/filters/payment_terms) filter applied, between the opening and closing `form` tags:

9

1

2

3

4

5

{% form 'cart', cart %}

<!-- cart subtotal -->

{{ form | payment\_terms }}

...

{% endform %}

The reference should be below the cart subtotal price so that price and payment information is grouped together.

The `payment_terms` filter can be used anywhere that you can use a cart form. It's commonly used in the [cart template](/docs/storefronts/themes/architecture/templates/cart), or a section inside of the template.

#### [Anchor to Updating the banner with cart total changes](/docs/storefronts/themes/pricing-payments/installments#updating-the-banner-with-cart-total-changes)Updating the banner with cart total changes

To stay updated with the cart total, the banner parses for the subtotal price based on the attribute `data-cart-subtotal`. Most free Shopify themes have this attribute on their subtotal display by default, so the banner will update automatically. If your banner doesn't update automatically, then you need to add the `data-cart-subtotal` attribute to your subtotal display.

9

1

<span data-cart-subtotal>{{ cart.total\_price | money }}</span>

---

Was this page helpful?

YesNo