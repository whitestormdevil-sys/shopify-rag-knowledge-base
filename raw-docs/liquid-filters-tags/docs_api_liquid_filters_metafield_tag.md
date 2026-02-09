---
source: https://shopify.dev/docs/api/liquid/filters/metafield_tag
---

9

1

metafield | metafield\_tag

returns [string](/docs/api/liquid/basics#string)

Generates an HTML element to host the data from a [`metafield` object](https://shopify.dev/docs/api/liquid/objects/metafield).
The type of element that's generated differs depending on the type of metafield.

---

Note

The `metafield_tag` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

**Note:**

The `metafield_tag` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">metafield<wbr/>\_tag</span></code> filter doesn&#39;t currently support list metafields other than <code><span class="PreventFireFoxApplyingGapToWBR">list.single<wbr/>\_line<wbr/>\_text<wbr/>\_field</span></code> and <code><span class="PreventFireFoxApplyingGapToWBR">list.metaobject<wbr/>\_reference</span></code>.

---

[Anchor to Basic types](/docs/api/liquid/filters/metafield_tag#metafield_tag-basic-types)

### Basic types

Most metafield types return a simple HTML element:

| Type | Element | Attributes |
| --- | --- | --- |
| `boolean` | `<span>` | `class="metafield-boolean"` |
| `collection_reference` | `<a>` | `class="metafield-collection_reference"` |
| `color` | `<span>` | `class="metafield-color"` |
| `date` | `<time>` | `datetime="&lt;the metafield value&gt;"`  `class="metafield-date"`  Value is localized to the customer |
| `date_time` | `<time>` | `datetime="&lt;the metafield value&gt;"`  `class="metafield-date"`  Value is localized to the customer |
| `json` | `<script>` | `type="application/json"`<br><br>`class="metafield-json"` |
| `money` | `<span>` | `class="metafield-money"`  Value is formatted using the store's [HTML with currency setting](https://help.shopify.com/manual/payments/currency-formatting) |
| `multi_line_text_field` | `<span>` | `class="metafield-multi_line_text_field"` |
| `number_decimal` | `<span>` | `class="metafield-number_decimal"` |
| `number_integer` | `<span>` | `class="metafield-number_integer"` |
| `page_reference` | `<a>` | `class="metafield-page_reference"` |
| `product_reference` | `<a>` | `class="metafield-page_reference"` |
| `rating` | `<span>` | `class="metafield-rating"` |
| `single_line_text_field` | `<span>` | `class="metafield-single_line_text_field"` |
| `url` | `<a>` | `class="metafield-url"` |
| `variant_reference` | `<a>` | `class="metafield-variant_reference"` |
| `rich_text_field` | `<div>` | `class="metafield-rich_text_field"` |

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

<!-- boolean -->

{{ product.metafields.information.seasonal | metafield\_tag }}

<!-- collection\_reference -->

{{ product.metafields.information.related\_collection | metafield\_tag }}

<!-- color -->

{{ product.metafields.details.potion\_color | metafield\_tag }}

<!-- date -->

{{ product.metafields.information.expiry | metafield\_tag }}

<!-- date\_time -->

{{ product.metafields.information.brew\_date | metafield\_tag }}

<!-- json -->

{{ product.metafields.information.burn\_temperature | metafield\_tag }}

<!-- money -->

{{ product.metafields.details.price\_per\_ml | metafield\_tag }}

<!-- multi\_line\_text\_field -->

{{ product.metafields.information.shipping | metafield\_tag }}

<!-- number\_decimal -->

{{ product.metafields.information.salinity | metafield\_tag }}

<!-- number\_integer -->

{{ product.metafields.information.doses\_per\_day | metafield\_tag }}

<!-- page\_reference -->

{{ product.metafields.information.dosage | metafield\_tag }}

<!-- product\_reference -->

{{ product.metafields.information.related\_product | metafield\_tag }}

<!-- rating -->

{{ product.metafields.details.rating | metafield\_tag }}

<!-- single\_line\_text\_field -->

{{ product.metafields.information.directions | metafield\_tag }}

<!-- url -->

{{ product.metafields.information.health | metafield\_tag }}

<!-- variant\_reference -->

{{ product.metafields.information.best\_seller | metafield\_tag }}

<!-- rich\_text\_field -->

{{ product.metafields.information.rich\_description | metafield\_tag }}

##### Code

```liquid
<!-- boolean -->
{{ product.metafields.information.seasonal | metafield_tag }}

<!-- collection_reference -->
{{ product.metafields.information.related_collection | metafield_tag }}

<!-- color -->
{{ product.metafields.details.potion_color | metafield_tag }}

<!-- date -->
{{ product.metafields.information.expiry | metafield_tag }}

<!-- date_time -->
{{ product.metafields.information.brew_date | metafield_tag }}

<!-- json -->
{{ product.metafields.information.burn_temperature | metafield_tag }}

<!-- money -->
{{ product.metafields.details.price_per_ml | metafield_tag }}

<!-- multi_line_text_field -->
{{ product.metafields.information.shipping | metafield_tag }}

<!-- number_decimal -->
{{ product.metafields.information.salinity | metafield_tag }}

<!-- number_integer -->
{{ product.metafields.information.doses_per_day | metafield_tag }}

<!-- page_reference -->
{{ product.metafields.information.dosage | metafield_tag }}

<!-- product_reference -->
{{ product.metafields.information.related_product | metafield_tag }}

<!-- rating -->
{{ product.metafields.details.rating | metafield_tag }}

<!-- single_line_text_field -->
{{ product.metafields.information.directions | metafield_tag }}

<!-- url -->
{{ product.metafields.information.health | metafield_tag }}

<!-- variant_reference -->
{{ product.metafields.information.best_seller | metafield_tag }}

<!-- rich_text_field -->
{{ product.metafields.information.rich_description | metafield_tag }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
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

<!-- boolean -->

<span class="metafield-boolean">false</span>

<!-- collection\_reference -->

<a href="/collections/sale-potions" class="metafield-collection\_reference">Sale potions</a>

<!-- color -->

<span class="metafield-color">#ff0000</span>

<!-- date -->

<time datetime="2040-01-01" class="metafield-date">January 1, 2040</time>

<!-- date\_time -->

<time datetime="2022-06-22T13:00:00Z" class="metafield-date\_time">Jun 22, 2022, 1:00 pm</time>

<!-- json -->

<script type="application/json" class="metafield-json">{"temperature":"700","unit":"degrees","scale":"Fahrenheit"}</script>

<!-- money -->

<span class="metafield-money">$0.10 CAD</span>

<!-- multi\_line\_text\_field -->

<span class="metafield-multi\_line\_text\_field">All health potions are made to order, so it might take up to 2 weeks before your order can be shipped.<br />

<br />

Thanks for your patience!</span>

<!-- number\_decimal -->

<span class="metafield-number\_decimal">8.4</span>

<!-- number\_integer -->

<span class="metafield-number\_integer">3</span>

<!-- page\_reference -->

<a href="/pages/potion-dosages" class="metafield-page\_reference">Potion dosages</a>

<!-- product\_reference -->

<a href="/products/dried-chamomile" class="metafield-product\_reference">Dried chamomile</a>

<!-- rating -->

<span class="metafield-rating">4.5</span>

<!-- single\_line\_text\_field -->

<span class="metafield-single\_line\_text\_field">Take with a meal.</span>

<!-- url -->

<a href="https://www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html" class="metafield-url">www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html</a>

<!-- variant\_reference -->

<a href="/products/health-potion?variant=39897499762753" class="metafield-variant\_reference">S / Medium</a>

<!-- rich\_text\_field -->

<div class="metafield-rich\_text\_field"><h3>Are you low on health? Well we&#39;ve got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p></div>

##### Output

```liquid
<!-- boolean -->
<span class="metafield-boolean">false</span>

<!-- collection_reference -->
<a href="/collections/sale-potions" class="metafield-collection_reference">Sale potions</a>

<!-- color -->
<span class="metafield-color">#ff0000</span>

<!-- date -->
<time datetime="2040-01-01" class="metafield-date">January 1, 2040</time>

<!-- date_time -->
<time datetime="2022-06-22T13:00:00Z" class="metafield-date_time">Jun 22, 2022, 1:00 pm</time>

<!-- json -->
<script type="application/json" class="metafield-json">{"temperature":"700","unit":"degrees","scale":"Fahrenheit"}</script>

<!-- money -->
<span class="metafield-money">$0.10 CAD</span>

<!-- multi_line_text_field -->
<span class="metafield-multi_line_text_field">All health potions are made to order, so it might take up to 2 weeks before your order can be shipped.<br />
<br />
Thanks for your patience!</span>

<!-- number_decimal -->
<span class="metafield-number_decimal">8.4</span>

<!-- number_integer -->
<span class="metafield-number_integer">3</span>

<!-- page_reference -->
<a href="/pages/potion-dosages" class="metafield-page_reference">Potion dosages</a>

<!-- product_reference -->
<a href="/products/dried-chamomile" class="metafield-product_reference">Dried chamomile</a>

<!-- rating -->
<span class="metafield-rating">4.5</span>

<!-- single_line_text_field -->
<span class="metafield-single_line_text_field">Take with a meal.</span>

<!-- url -->
<a href="https://www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html" class="metafield-url">www.canada.ca/en/health-canada/services/food-nutrition/legislation-guidelines/acts-regulations/canada-food-drugs.html</a>

<!-- variant_reference -->
<a href="/products/health-potion?variant=39897499762753" class="metafield-variant_reference">S / Medium</a>

<!-- rich_text_field -->
<div class="metafield-rich_text_field"><h3>Are you low on health? Well we&#39;ve got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p></div>
```

[Anchor to Complex types](/docs/api/liquid/filters/metafield_tag#metafield_tag-complex-types)

### Complex types

The following metafield types return nested elements, or different elements depending on the metafield contents:

* [`dimension`](/docs/api/liquid/filters/metafield_tag#metafield_tag-dimension)
* [`file_reference`](/docs/api/liquid/filters/metafield_tag#metafield_tag-file_reference)
* [`list.metaobject_reference`](/docs/api/liquid/filters/metafield_tag#metafield_tag-list.metaobject_reference)
* [`list.single_line_text_field`](/docs/api/liquid/filters/metafield_tag#metafield_tag-list.single_line_text_field)
* [`metaobject_reference`](/docs/api/liquid/filters/metafield_tag#metafield_tag-metaobject_reference)
* [`volume`](/docs/api/liquid/filters/metafield_tag#metafield_tag-volume)
* [`weight`](/docs/api/liquid/filters/metafield_tag#metafield_tag-weight)

[Anchor to dimension](/docs/api/liquid/filters/metafield_tag#metafield_tag-dimension)

### dimension

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-dimension` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The dimension value.  If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-dimension_value"` |
| The dimension unit. | `<span>` | `class="metafield-dimension_unit"` |

9

1

{{ product.metafields.details.scale\_width | metafield\_tag }}

##### Code

```liquid
{{ product.metafields.details.scale_width | metafield_tag }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

<span class="metafield-dimension"><span class="metafield-dimension\_value">3 </span><span class="metafield-dimension\_unit">cm</span></span>

##### Output

```liquid
<span class="metafield-dimension"><span class="metafield-dimension_value">3 </span><span class="metafield-dimension_unit">cm</span></span>
```

[Anchor to file\_reference](/docs/api/liquid/filters/metafield_tag#metafield_tag-file_reference)

### file\_reference

The output varies depending on the type of file. There are the following categories of file type:

| File type | Description |
| --- | --- |
| Image | Images in the format of `jpg`, `png`, `gif`, `heic`, and `webp`. |
| Video | Videos in the format of `mov`, and `mp4`. |
| Other | Any other file type. |

##### Image

Outputs an `<img>` element with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The image's URL. |
| `alt` | The image's alt text. |
| `class` | `metafield-file_reference` |

##### Video

Outputs a `<video>` element with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The video's URL. |
| `poster` | The video's preview image (poster) URL. |
| `playsinline` | N/A - Indicates the video will be played "inline" within the element's playback area. |
| `preload` | `metadata` - Only metadata is pre-fetched before the video is played. |

The `<video>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The video's multimedia playlist source, for [HTTP live streaming (HLS)](https://developer.apple.com/streaming/) | `&lt;source&gt;` | `src="&lt;the video's m3u8 source URL>"`<br><br>`type="application/x-mpegURL"` |
| The video's original source | `&lt;source&gt;` | `src="&lt;the video's source URL&gt;"`<br><br>`type="&lt;the video's original source MIME type>"` |
| The video's preview (poster) image | `&lt;img&gt;` | `src="&lt;the video's preview image URL>"` |

##### Other

Outputs an `<a>` element with a link to the file and the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-file_reference` |

The `<a>` element contains an `<img>` element for the file's [preview image](/docs/api/liquid/objects/generic_file#generic_file-preview_image) with the following attributes:

| Attribute | Value |
| --- | --- |
| `src` | The file's preview image URL. |
| `loading` | `lazy` - The image isn't loaded until it's almost in view. |

9

1

2

3

4

5

6

7

8

<!-- Image -->

{{ product.metafields.information.promo\_image | metafield\_tag }}

<!-- Video -->

{{ product.metafields.information.promo\_video | metafield\_tag }}

<!-- Other -->

{{ product.metafields.information.disclaimers | metafield\_tag }}

##### Code

```liquid
<!-- Image -->
{{ product.metafields.information.promo_image | metafield_tag }}

<!-- Video -->
{{ product.metafields.information.promo_video | metafield_tag }}

<!-- Other -->
{{ product.metafields.information.disclaimers | metafield_tag }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
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

7

8

<!-- Image -->

<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393" loading="lazy" class="metafield-file\_reference">

<!-- Video -->

<video playsinline="playsinline" preload="metadata" poster="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview\_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000\_small.jpg?v=1655257099"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4733c31cd9d744f6994f61458fda85e6/4733c31cd9d744f6994f61458fda85e6.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview\_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000\_small.jpg?v=1655257099"></video>

<!-- Other -->

<a href="//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859" class="metafield-file\_reference"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview\_images/document-7f23220eb4be7eeaa6e225738b97d943f22e74367cd2d7544fc3b37fb36acd71.png?v=1653087800" loading="lazy"></a>

##### Output

```liquid
<!-- Image -->
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393" loading="lazy" class="metafield-file_reference">

<!-- Video -->
<video playsinline="playsinline" preload="metadata" poster="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000_small.jpg?v=1655257099"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4733c31cd9d744f6994f61458fda85e6/4733c31cd9d744f6994f61458fda85e6.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/4733c31cd9d744f6994f61458fda85e6.thumbnail.0000000_small.jpg?v=1655257099"></video>

<!-- Other -->
<a href="//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859" class="metafield-file_reference"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/preview_images/document-7f23220eb4be7eeaa6e225738b97d943f22e74367cd2d7544fc3b37fb36acd71.png?v=1653087800" loading="lazy"></a>
```

[Anchor to list.metaobject\_reference](/docs/api/liquid/filters/metafield_tag#metafield_tag-listmetaobject_reference)

### list.metaobject\_reference

9

1

metafield | metafield\_tag: field: string

Outputs a `<ul>` element by default with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-single_line_text_field-array` |

The `<ul>` element contains an `<li>` element for each metaobject in the list with a `class` of `metafield-single_line_text_field`. The required `field` parameter specifies which field should be rendered for each metaobject. The `field` parameter can reference only metafields of type `single_line_text_field`.

To output an `<ol>` element, pass the `list_format` parameter with a value of `ordered`.

9

1

2

3

4

5

<!-- <ul> element -->

{{ product.metafields.information.ingredients | metafield\_tag: field: 'name' }}

<!-- <ol> element -->

{{ product.metafields.information.ingredients | metafield\_tag: field: 'name', list\_format: 'ordered' }}

##### Code

```liquid
<!-- <ul> element -->
{{ product.metafields.information.ingredients | metafield_tag: field: 'name' }}

<!-- <ol> element -->
{{ product.metafields.information.ingredients | metafield_tag: field: 'name', list_format: 'ordered' }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
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

<!-- <ul> element -->

<ul class="metafield-single\_line\_text\_field-array"><li class="metafield-single\_line\_text\_field">Spinach</li><li class="metafield-single\_line\_text\_field">Kale</li><li class="metafield-single\_line\_text\_field">Mushrooms</li></ul>

<!-- <ol> element -->

<ol class="metafield-single\_line\_text\_field-array"><li class="metafield-single\_line\_text\_field">Spinach</li><li class="metafield-single\_line\_text\_field">Kale</li><li class="metafield-single\_line\_text\_field">Mushrooms</li></ol>

##### Output

```liquid
<!-- <ul> element -->
<ul class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Spinach</li><li class="metafield-single_line_text_field">Kale</li><li class="metafield-single_line_text_field">Mushrooms</li></ul>

<!-- <ol> element -->
<ol class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Spinach</li><li class="metafield-single_line_text_field">Kale</li><li class="metafield-single_line_text_field">Mushrooms</li></ol>
```

[Anchor to list.single\_line\_text\_field](/docs/api/liquid/filters/metafield_tag#metafield_tag-listsingle_line_text_field)

### list.single\_line\_text\_field

Outputs a `<ul>` element by default with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-single_line_text_field-array` |

The `<ul>` element contains an `<li>` element for each item in the list with a `class` of `metafield-single_line_text_field`.

To output an `<ol>` element, pass the `list_format` parameter with a value of `ordered`.

9

1

2

3

4

5

<!-- <ul> element -->

{{ product.metafields.information.pickup\_locations | metafield\_tag }}

<!-- <ol> element -->

{{ product.metafields.information.pickup\_locations | metafield\_tag: list\_format: 'ordered' }}

##### Code

```liquid
<!-- <ul> element -->
{{ product.metafields.information.pickup_locations | metafield_tag }}

<!-- <ol> element -->
{{ product.metafields.information.pickup_locations | metafield_tag: list_format: 'ordered' }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
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

<!-- <ul> element -->

<ul class="metafield-single\_line\_text\_field-array"><li class="metafield-single\_line\_text\_field">Ottawa</li><li class="metafield-single\_line\_text\_field">Toronto</li><li class="metafield-single\_line\_text\_field">Montreal</li><li class="metafield-single\_line\_text\_field">Vancouver</li></ul>

<!-- <ol> element -->

<ol class="metafield-single\_line\_text\_field-array"><li class="metafield-single\_line\_text\_field">Ottawa</li><li class="metafield-single\_line\_text\_field">Toronto</li><li class="metafield-single\_line\_text\_field">Montreal</li><li class="metafield-single\_line\_text\_field">Vancouver</li></ol>

##### Output

```liquid
<!-- <ul> element -->
<ul class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Ottawa</li><li class="metafield-single_line_text_field">Toronto</li><li class="metafield-single_line_text_field">Montreal</li><li class="metafield-single_line_text_field">Vancouver</li></ul>

<!-- <ol> element -->
<ol class="metafield-single_line_text_field-array"><li class="metafield-single_line_text_field">Ottawa</li><li class="metafield-single_line_text_field">Toronto</li><li class="metafield-single_line_text_field">Montreal</li><li class="metafield-single_line_text_field">Vancouver</li></ol>
```

[Anchor to metaobject\_reference](/docs/api/liquid/filters/metafield_tag#metafield_tag-metaobject_reference)

### metaobject\_reference

9

1

metafield | metafield\_tag: field: string

Outputs an HTML element for the metaobject field specified by the required `field` parameter. The `field` parameter can reference only metafields of type `single_line_text_field`.

9

1

{{ product.metafields.information.primary\_ingredient | metafield\_tag: field: 'name' }}

##### Code

```liquid
{{ product.metafields.information.primary_ingredient | metafield_tag: field: 'name' }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

<span class="metafield-single\_line\_text\_field">Spinach</span>

##### Output

```liquid
<span class="metafield-single_line_text_field">Spinach</span>
```

[Anchor to volume](/docs/api/liquid/filters/metafield_tag#metafield_tag-volume)

### volume

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-volume` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The volume value.  If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-volume_value"` |
| The volume unit. | `<span>` | `class="metafield-volume_unit"` |

9

1

{{ product.metafields.details.milk\_container\_volume | metafield\_tag }}

##### Code

```liquid
{{ product.metafields.details.milk_container_volume | metafield_tag }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

<span class="metafield-volume"><span class="metafield-volume\_value">500 </span><span class="metafield-volume\_unit">mL</span></span>

##### Output

```liquid
<span class="metafield-volume"><span class="metafield-volume_value">500 </span><span class="metafield-volume_unit">mL</span></span>
```

[Anchor to weight](/docs/api/liquid/filters/metafield_tag#metafield_tag-weight)

### weight

Outputs a `<span>` element with the following attribute:

| Attribute | Value |
| --- | --- |
| `class` | `metafield-weight` |

The `<span>` element contains the following child elements:

| Child element | HTML element | Attributes |
| --- | --- | --- |
| The weight value.  If it's a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. | `<span>` | `class="metafield-weight_value"` |
| The weight unit. | `<span>` | `class="metafield-weight_unit"` |

9

1

{{ product.metafields.details.chamomile\_base\_weight | metafield\_tag }}

##### Code

```liquid
{{ product.metafields.details.chamomile_base_weight | metafield_tag }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

<span class="metafield-weight"><span class="metafield-weight\_value">50 </span><span class="metafield-weight\_unit">g</span></span>

##### Output

```liquid
<span class="metafield-weight"><span class="metafield-weight_value">50 </span><span class="metafield-weight_unit">g</span></span>
```

Was this page helpful?

YesNo