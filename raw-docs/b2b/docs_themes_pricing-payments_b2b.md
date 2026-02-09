---
source: https://shopify.dev/docs/themes/pricing-payments/b2b
---

Many merchants conduct business-to-business (B2B) commerce, where they sell directly to other companies.

To help manage B2B transactions, merchants can create [companies](/docs/api/liquid/objects/company). A company can be associated with one or more [customers](/docs/api/liquid/objects/customer), and can have one or more [locations](/docs/api/liquid/objects/company_location). For an individual transaction, a B2B customer must select a location for the transaction to be associated with.

Tip

To learn about the merchant experience in setting up B2B, visit the [Shopify Help Center](https://help.shopify.com/manual/b2b).

**Tip:**

To learn about the merchant experience in setting up B2B, visit the [Shopify Help Center](https://help.shopify.com/manual/b2b).

In this tutorial, you'll learn how to support B2B customers with a location picker.

---

## [Anchor to Resources](/docs/storefronts/themes/pricing-payments/b2b#resources)Resources

To support B2B customers in your theme, you'll use the following objects and object properties that contain B2B information:

* [`company`](/docs/api/liquid/objects/company)
* [`company_location`](/docs/api/liquid/objects/company_location)
* [`customer.b2b?`](/docs/api/liquid/objects/customer#customer-b2b?)
* [`customer.company_available_locations`](/docs/api/liquid/objects/customer#customer-company_available_locations)
* [`customer.current_company`](/docs/api/liquid/objects/customer#customer-current_company)
* [`customer.current_location`](/docs/api/liquid/objects/customer#customer-current_location)

---

## [Anchor to Implementing a company location picker](/docs/storefronts/themes/pricing-payments/b2b#implementing-a-company-location-picker)Implementing a company location picker

If the current customer is a B2B customer, then you should give them the ability to choose the company location that they're purchasing for with a location picker.

Your location picker code should do the following:

1. Check whether the customer is a B2B customer using `customer.b2b?`
2. If `customer.b2b?` is `true`, then display the following:
   * The current company and location of the customer.
   * If `customer.company_available_locations` has a size greater than 1, then display a list of the currently unselected locations.

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

{% if customer.b2b? %}

<div>

<h2>Welcome, {{ customer.name }} from {{ customer.current\_company.name }}!</h2>

<p>You are purchasing for the {{ customer.current\_location.name }} location.</p>

{% if customer.company\_available\_locations.size > 1 %}

<h3>Select a different location:</h3>

<ul>

{% for location in customer.company\_available\_locations %}

{% unless location.current? %}

<li>

<a href="{{ location.url\_to\_set\_as\_current }}">{{ location.name }}</a>

</li>

{% endunless %}

{% endfor %}

</ul>

{% endif %}

</div>

{% endif %}

---

## [Anchor to Show content based on company or location](/docs/storefronts/themes/pricing-payments/b2b#show-content-based-on-company-or-location)Show content based on company or location

You can show content conditionally based on the current company or location of the customer.

9

1

2

3

{% if customer.current\_company.name == 'Shopify' %}

<h3>Delivery and installation included.</h3>

{% endif %}

---

## [Anchor to Show content to B2B customers only](/docs/storefronts/themes/pricing-payments/b2b#show-content-to-b2b-customers-only)Show content to B2B customers only

Dedicated B2B stores might want to show certain online store content only to verified B2B customers.

You might want to hide the following elements from customers who aren't logged in as a B2B customer:

* Product prices
* The cart icon in the header
* Add to cart buttons
* Other calls to action in the product page

  You can [adapt your theme content for your B2B customers](https://help.shopify.com//en/manual/online-store/themes/customizing-themes/store-contextualization) directly from the theme editor. Alternatively, you can use the Liquid [`customer.b2b?`](/docs/api/liquid/objects#customer-b2b?) property to render content for verified B2B customers. In this example, `customer.b2b?` is used to conditionally hide the product price:

9

1

2

3

{%- if customer.b2b? -%}

// code for price here

{%- endif -%}

Where logged out customers would usually see pricing, you can instead show a prompt to log in:

9

1

2

3

4

5

{%- if customer.b2b? -%}

// code for price here

{%- else -%}

<a href="{{ routes.account\_login\_url }}">Log in to see the price</a>

{%- endif -%}

You can also use this property to render content only for logged out customers. In this example, `customer.b2b?` is used to conditionally show an inquiry form.

9

1

2

3

{%- unless customer.b2b? -%}

// code for inquiry form here

{%- endunless -%}

Note

If you're using a theme from the Shopify Theme Store, and you want to [keep your theme eligible for automatic upgrades](https://help.shopify.com/manual/online-store/themes/managing-themes/updating-themes), then you should avoid editing your theme code to conditionally hide elements. Instead, you can hide the section or block that contains the content that you want to conditionally display, and then add a new Custom Liquid section or block that conditionally displays the element. For example, to show or hide the product price on the product page, you can copy the contents of the price block into the Custom Liquid block in your main product page section and use `customer.b2b?` as shown in the example.
Some areas, such as the cart icon in the header, might not be configured as individual sections or blocks. As a result, it might not be possible to avoid making changes to the theme code in these cases.

**Note:**

If you're using a theme from the Shopify Theme Store, and you want to [keep your theme eligible for automatic upgrades](https://help.shopify.com/manual/online-store/themes/managing-themes/updating-themes), then you should avoid editing your theme code to conditionally hide elements. Instead, you can hide the section or block that contains the content that you want to conditionally display, and then add a new Custom Liquid section or block that conditionally displays the element. For example, to show or hide the product price on the product page, you can copy the contents of the price block into the Custom Liquid block in your main product page section and use `customer.b2b?` as shown in the example.
Some areas, such as the cart icon in the header, might not be configured as individual sections or blocks. As a result, it might not be possible to avoid making changes to the theme code in these cases.

---

Was this page helpful?

YesNo