---
source: https://shopify.dev/docs/themes/product-merchandising/variants
---

Products can be broken up into a maximum of three options, and a single combination of those options is a variant. For example, if a t-shirt comes in sizes `S`, `M`, and `L`, and colors `Black`, `White`, and `Red`, then `S/Black` would be a variant of that product.

In this tutorial, you'll learn how to support product variants in your theme.

---

## [Anchor to Resources](/docs/storefronts/themes/product-merchandising/variants#resources)Resources

To support product variants, you'll use the following:

* The [`product` object](/docs/api/liquid/objects/product)
* The [`variant` object](/docs/api/liquid/objects/variant)

---

## [Anchor to Implementing product variants](/docs/storefronts/themes/product-merchandising/variants#implementing-product-variants)Implementing product variants

To support variants in your theme, you need to implement the following components:

* [Variant deep link handling](#variant-deep-link-handling): A variant can be linked to directly, so you should ensure that the product information is updated for the "selected" variant when a variant is referenced in a product link.
* [Variant selectors](#variant-selectors): You should build a variant selector to allow customers to easily browse the available variants of a product. Selecting a variant should update the page with variant-specific information.

  You might want to add these components to a section that can be included in a JSON product template, or a Liquid product template.

---

## [Anchor to Variant deep link handling](/docs/storefronts/themes/product-merchandising/variants#variant-deep-link-handling)Variant deep link handling

Variant deep links are product links that contain a `?variant=[variant-id]` query parameter, where `[variant-id]` is the [ID](/docs/api/liquid/objects/variant#variant-id) of the associated variant. This allows you to link directly to a variant. You can add this functionality to a section that can be included in a JSON product template, or a Liquid product template.

When variants are deep-linked, you can access which variant is linked through the `selected_variant` attribute of the [`product` object](/docs/api/liquid/objects/product#product-selected_variant). However, a product link won't always contain a deep-linked variant. In these cases, you can default to the selected, first available, or first variant through the `selected_or_first_available_variant` attribute.

You can also deep link using the format `?option_values=[option-value-id-1],...,[option-value-id-N]` where `[option-value-id]` is the [ID](/docs/api/liquid/objects/product_option_value#product_option_value-id) of the associated option value. One option value ID must be provided per product option and the order must match the option order. If the option value combination maps to a variant that is not present, the requested option values will be selected but the product fields [`selected_variant`](/docs/api/liquid/objects/product#product-selected_variant) and [`selected_or_first_available_variant`](/docs/api/liquid/objects/product#product-selected_or_first_available_variant) will return null.

After you identify the variant that you want to display, you need to ensure that the following product elements reflect it:

* Product media
* Product price
* Variant selector

### [Anchor to Example](/docs/storefronts/themes/product-merchandising/variants#example)Example

The following example assigns a default variant using `product.selected_or_first_available_variant`, populates a basic media and price display based on that variant, and selects that variant in a basic variant selector.

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

{% assign current\_variant = product.selected\_or\_first\_available\_variant %}

<!-- Product media -->

{% assign featured\_media = current\_variant.featured\_media %}

{% case featured\_media.media\_type %}

{% when 'image' %}

<div className="product-single\_\_media"

style={{paddingTop: '{{ 1 | divided\_by'}}

data-media-id="{{ featured\_media.id }}"

>

{{ featured\_media | image\_url: width: 2048 | image\_tag }}

</div>

{% when 'external\_video' %}

<div className="product-single\_\_media"

style={{paddingTop: '{{ 1 | divided\_by'}}

data-media-id="{{ featured\_media.id }}"

>

{{ featured\_media | external\_video\_tag }}

</div>

{% when 'video' %}

<div className="product-single\_\_media" data-media-id="{{ featured\_media.id }}">

{{ featured\_media | video\_tag: controls: true }}

</div>

{% when 'model' %}

<div className="product-single\_\_media"

style={{paddingTop: '100%'}}

data-media-id="{{ featured\_media.id }}"

>

{{ featured\_media | model\_viewer\_tag }}

</div>

{% else %}

<div className="product-single\_\_media"

style={{paddingTop: '100%'}}

data-media-id="{{ featured\_media.id }}"

>

{{ featured\_media | media\_tag }}

</div>

{% endcase %}

<!-- Product price -->

<div className="price">

<span className="price-reg">{{ current\_variant.price | money }}</span>

{% if current\_variant.compare\_at\_price > current\_variant.price %}

<span className="price-sale"><s>{{ current\_variant.compare\_at\_price | money }}</s></span>

{% endif %}

</div>

<!-- Variant selector -->

<select name="id">

{% for variant in product.variants %}

<option value="{{ variant.id }}"

{% if variant == current\_variant %}selected="selected"{% endif %}

>

{{ variant.title }} - {{ variant.price | money }}

</option>

{% endfor %}

</select>

---

## [Anchor to Variant selectors](/docs/storefronts/themes/product-merchandising/variants#variant-selectors)Variant selectors

You can use a single variant selector where each option represents a variant. However, products may have more than one option. For a better buyer experience and to avoid future compatibility issues, we recommend that you present each of these options separately in the UI. To achieve this, you can use the [`product.options_with_values` object](/docs/api/liquid/objects/product#product-options_with_values) to generate a selector for each option. You can then use JavaScript to update the state when a new option value is selected.

Note

Regardless of the approach you use for variant selection, you need to ensure that when a new variant is selected, the product media and price are updated to reflect the selected variant.

**Note:**

Regardless of the approach you use for variant selection, you need to ensure that when a new variant is selected, the product media and price are updated to reflect the selected variant.

Variant selectors should be added to a section that can be included in a JSON product template, or a Liquid product template. They can also be included in product grid or product quick view snippets to allow customers to view variants on other pages, like collections.

Tip

Refer to the following files in Dawn for an example implementation:

* [`product-variant-picker.liquid` section](https://github.com/Shopify/dawn/blob/main/snippets/product-variant-picker.liquid)
* [`global.js` asset](https://github.com/Shopify/dawn/blob/main/assets/global.js)

**Tip:**

Refer to the following files in Dawn for an example implementation:

* [`product-variant-picker.liquid` section](https://github.com/Shopify/dawn/blob/main/snippets/product-variant-picker.liquid)
* [`global.js` asset](https://github.com/Shopify/dawn/blob/main/assets/global.js)

---

Was this page helpful?

YesNo