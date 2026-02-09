---
source: https://shopify.dev/docs/api/liquid/objects/collection
---

A [collection](https://help.shopify.com/manual/products/collections) in a store.

## Properties

[Anchor to](/docs/api/liquid/objects/collection#collection-all_products_count) 

all\_products\_count**all\_products\_count** [number](/docs/api/liquid/basics#number)

:   The total number of products in a collection.

    This includes products that have been filtered out of the current view.

    Tip

    To display the number of products in a filtered collection, use [`collection.products_count`](/docs/api/liquid/objects/collection#collection-products_count).

    **Tip:**

    To display the number of products in a filtered collection, use [`collection.products_count`](/docs/api/liquid/objects/collection#collection-products_count).

    **Tip:** To display the number of products in a filtered collection, use <a href="/docs/api/liquid/objects/collection#collection-products\_count"><code><span class="PreventFireFoxApplyingGapToWBR">collection.products<wbr/>\_count</span></code></a>.

[Anchor to](/docs/api/liquid/objects/collection#collection-all_tags) 

all\_tags**all\_tags** array of [string](/docs/api/liquid/basics#string)

:   All of the tags applied to the products in the collection.

    This includes tags for products that have been filtered out of the current view.
    A maximum of 1,000 tags can be returned.

    Tip

    To display the tags that are currently applied, use [`collection.tags`](/docs/api/liquid/objects/collection#collection-tags).

    **Tip:**

    To display the tags that are currently applied, use [`collection.tags`](/docs/api/liquid/objects/collection#collection-tags).

    **Tip:** To display the tags that are currently applied, use <a href="/docs/api/liquid/objects/collection#collection-tags"><code>collection.tags</code></a>.

[Anchor to](/docs/api/liquid/objects/collection#collection-all_types) 

all\_types**all\_types** array of [string](/docs/api/liquid/basics#string)

:   All of the product types in a collection.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Create links to product types

    Use the [`link_to_type`](/docs/api/liquid/filters/link_to_type) filter to create links to the product types in a collection.

    9

    1

    2

    3

    {% for product\_type in collection.all\_types -%}

    {{- product\_type | link\_to\_type }}

    {%- endfor %}

    ##### Code

    ```liquid
    {% for product_type in collection.all_types -%}
      {{- product_type | link_to_type }}
    {%- endfor %}
    ```

    ##### Data

    ```liquid
    {
      "collection": {
        "all_types": [
          "Animals & Pet Supplies",
          "Baking Flavors & Extracts",
          "Cooking & Baking Ingredients",
          "Dried Flowers",
          "Fruits & Vegetables",
          "Seasonings & Spices",
          "Water"
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

    7

    <a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>

    <a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>

    <a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>

    <a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>

    <a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>

    <a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>

    <a href="/collections/types?q=Water" title="Water">Water</a>

    ##### Output

    ```liquid
    <a href="/collections/types?q=Animals%20%26%20Pet%20Supplies" title="Animals &amp; Pet Supplies">Animals & Pet Supplies</a>
    <a href="/collections/types?q=Baking%20Flavors%20%26%20Extracts" title="Baking Flavors &amp; Extracts">Baking Flavors & Extracts</a>
    <a href="/collections/types?q=Cooking%20%26%20Baking%20Ingredients" title="Cooking &amp; Baking Ingredients">Cooking & Baking Ingredients</a>
    <a href="/collections/types?q=Dried%20Flowers" title="Dried Flowers">Dried Flowers</a>
    <a href="/collections/types?q=Fruits%20%26%20Vegetables" title="Fruits &amp; Vegetables">Fruits & Vegetables</a>
    <a href="/collections/types?q=Seasonings%20%26%20Spices" title="Seasonings &amp; Spices">Seasonings & Spices</a>
    <a href="/collections/types?q=Water" title="Water">Water</a>
    ```

[Anchor to](/docs/api/liquid/objects/collection#collection-all_vendors) 

all\_vendors**all\_vendors** array of [string](/docs/api/liquid/basics#string)

:   All of the product vendors in a collection.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Create links to vendors

    Use the [`link_to_vendor`](/docs/api/liquid/filters/link_to_vendor) filter to create links to the vendors in a collection.

    9

    1

    2

    3

    {% for product\_vendor in collection.all\_vendors %}

    {{- product\_vendor | link\_to\_vendor }}

    {% endfor %}

    ##### Code

    ```liquid
    {% for product_vendor in collection.all_vendors %}
      {{- product_vendor | link_to_vendor }}
    {% endfor %}
    ```

    ##### Data

    ```liquid
    {
      "collection": {
        "all_vendors": [
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

[Anchor to](/docs/api/liquid/objects/collection#collection-current_type) 

current\_type**current\_type** [string](/docs/api/liquid/basics#string)

:   The product type on a product type collection page.

    You can query for products of a certain type at the `/collections/types` URL
    with a query parameter in the format of `?q=[type]`, where `[type]` is your desired product type.

    Tip

    The query value is case-insensitive, so `shirts` is equivalent to `Shirts` or `SHIRTS`.

    **Tip:**

    The query value is case-insensitive, so `shirts` is equivalent to `Shirts` or `SHIRTS`.

    **Tip:** The query value is case-insensitive, so <code>shirts</code> is equivalent to <code>Shirts</code> or <code><span class="PreventFireFoxApplyingGapToWBR">S<wbr/>H<wbr/>I<wbr/>R<wbr/>T<wbr/>S</span></code>.

[Anchor to](/docs/api/liquid/objects/collection#collection-current_vendor) 

current\_vendor**current\_vendor** [string](/docs/api/liquid/basics#string)

:   The vendor name on a vendor collection page.

    You can query for products from a certain vendor at the `/collections/vendors` URL
    with a query parameter in the format of `?q=[vendor]`, where `[vendor]` is your desired product vendor.

    Tip

    The query value is case-insensitive, so `apparelco` is equivalent to `ApparelCo` or `APPARELCO`.

    **Tip:**

    The query value is case-insensitive, so `apparelco` is equivalent to `ApparelCo` or `APPARELCO`.

    **Tip:** The query value is case-insensitive, so <code>apparelco</code> is equivalent to <code><span class="PreventFireFoxApplyingGapToWBR">Apparel<wbr/>Co</span></code> or <code><span class="PreventFireFoxApplyingGapToWBR">A<wbr/>P<wbr/>P<wbr/>A<wbr/>R<wbr/>E<wbr/>L<wbr/>C<wbr/>O</span></code>.

[Anchor to](/docs/api/liquid/objects/collection#collection-default_sort_by) 

default\_sort\_by**default\_sort\_by** [string](/docs/api/liquid/basics#string) from a set of values

:   The default sort order of the collection.

    This is set on the collection's page in the Shopify admin.

    | Possible values |
    | --- |
    | manual |
    | best-selling |
    | title-ascending |
    | price-ascending |
    | price-descending |
    | created-ascending |
    | created-descending |

[Anchor to](/docs/api/liquid/objects/collection#collection-description) 

description**description** [string](/docs/api/liquid/basics#string)

:   The description of the collection.

[Anchor to](/docs/api/liquid/objects/collection#collection-featured_image) 

featured\_image**featured\_image** [image](/docs/api/liquid/objects/image)

:   The featured image for the collection.

    The default is the [collection image](/docs/api/liquid/objects/collection#collection-image). If this image isn't available, then
    Shopify falls back to the featured image of the first product in the collection. If the first product in the collection
    doesn't have a featured image, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/collection#collection-filters) 

filters**filters** array of [filter](/docs/api/liquid/objects/filter)

:   The [storefront filters](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters) that
    have been set up on the collection.

    Only filters relevant to the current collection are returned. Filters will be empty for collections that contain over 5000 products.

    To learn about supporting filters in your theme, refer to [Support storefront filtering](/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

[Anchor to](/docs/api/liquid/objects/collection#collection-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the collection.

[Anchor to](/docs/api/liquid/objects/collection#collection-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the collection.

[Anchor to](/docs/api/liquid/objects/collection#collection-image) 

image**image** [image](/docs/api/liquid/objects/image)

:   The image for the collection.

    This image is added on the collection's page in the Shopify admin.

[Anchor to](/docs/api/liquid/objects/collection#collection-metafields) 

metafields**metafields** array of [metafield](/docs/api/liquid/objects/metafield)

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the collection.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/collection#collection-next_product) 

next\_product**next\_product** [product](/docs/api/liquid/objects/product)

:   The next product in the collection. Returns `nil` if there's no next product.

    This property can be used on the [product page](/themes/architecture/templates/product) to output `next` links.

[Anchor to](/docs/api/liquid/objects/collection#collection-previous_product) 

previous\_product**previous\_product** [product](/docs/api/liquid/objects/product)

:   The previous product in the collection. Returns `nil` if there's no previous product.

    This property can be used on the [product page](/themes/architecture/templates/product) to output `previous` links.

[Anchor to](/docs/api/liquid/objects/collection#collection-products) 

products**products** array of [product](/docs/api/liquid/objects/product)

:   All of the products in the collection.

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many products to show per page, up to a limit of 50.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many products to show per page, up to a limit of 50.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many products to show per page, up to a limit of 50.

[Anchor to](/docs/api/liquid/objects/collection#collection-products_count) 

products\_count**products\_count** [number](/docs/api/liquid/basics#number)

:   The total number of products in the current view of the collection.

[Anchor to](/docs/api/liquid/objects/collection#collection-published_at) 

published\_at**published\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the collection was published.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/collection#collection-sort_by) 

sort\_by**sort\_by** [string](/docs/api/liquid/basics#string)

:   The sort order applied to the collection by the `sort_by` URL parameter.

    If there's no `sort_by` URL parameter, then the value is `nil`.

[Anchor to](/docs/api/liquid/objects/collection#collection-sort_options) 

sort\_options**sort\_options** array of [sort\_option](/docs/api/liquid/objects/sort_option)

:   The available sorting options for the collection.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the sort options

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

    {%- assign sort\_by = collection.sort\_by | default: collection.default\_sort\_by -%}

    <select>

    {%- for option in collection.sort\_options %}

    <option

    value="{{ option.value }}"

    {%- if option.value == sort\_by %}

    selected="selected"

    {%- endif %}

    >

    {{ option.name }}

    </option>

    {% endfor -%}

    </select>

    ##### Code

    ```liquid
    {%- assign sort_by = collection.sort_by | default: collection.default_sort_by -%}

    <select>
    {%- for option in collection.sort_options %}
      <option
        value="{{ option.value }}"
        {%- if option.value == sort_by %}
          selected="selected"
        {%- endif %}
      >
        {{ option.name }}
      </option>
    {% endfor -%}
    </select>
    ```

    ##### Data

    ```liquid
    {
      "collection": {
        "default_sort_by": "title-ascending",
        "sort_by": "",
        "sort_options": [
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop",
          "CollectionDrop::SortOptionDrop"
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

    <select>

    <option

    value="manual"

    >

    Featured

    </option>

    <option

    value="best-selling"

    >

    Best selling

    </option>

    <option

    value="title-ascending"

    selected="selected"

    >

    Alphabetically, A-Z

    </option>

    <option

    value="title-descending"

    >

    Alphabetically, Z-A

    </option>

    <option

    value="price-ascending"

    >

    Price, low to high

    </option>

    <option

    value="price-descending"

    >

    Price, high to low

    </option>

    <option

    value="created-ascending"

    >

    Date, old to new

    </option>

    <option

    value="created-descending"

    >

    Date, new to old

    </option>

    </select>

    ##### Output

    ```liquid
    <select>
      <option
        value="manual"
      >
        Featured
      </option>

      <option
        value="best-selling"
      >
        Best selling
      </option>

      <option
        value="title-ascending"
          selected="selected"
      >
        Alphabetically, A-Z
      </option>

      <option
        value="title-descending"
      >
        Alphabetically, Z-A
      </option>

      <option
        value="price-ascending"
      >
        Price, low to high
      </option>

      <option
        value="price-descending"
      >
        Price, high to low
      </option>

      <option
        value="created-ascending"
      >
        Date, old to new
      </option>

      <option
        value="created-descending"
      >
        Date, new to old
      </option>
    </select>
    ```

[Anchor to](/docs/api/liquid/objects/collection#collection-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   The tags that are currently applied to the collection.

    This doesn't include tags for products that have been filtered out of the current view.
    Returns `nil` if no tags have been applied, or all products with tags have been filtered out of the current view.

[Anchor to](/docs/api/liquid/objects/collection#collection-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) assigned to the collection.

    The name doesn't include the `collection.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the collection, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/collection#collection-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the collection.

[Anchor to](/docs/api/liquid/objects/collection#collection-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the collection.

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

{

"all\_products\_count": 10,

"all\_tags": [

"Burning",

"dried",

"extracts",

"fresh",

"ingredients",

"plant",

"supplies"

],

"all\_types": [

"Animals & Pet Supplies",

"Baking Flavors & Extracts",

"Cooking & Baking Ingredients",

"Dried Flowers",

"Fruits & Vegetables",

"Seasonings & Spices",

"Water"

],

"all\_vendors": [

"Clover's Apothecary",

"Polina's Potent Potions",

"Ted's Apothecary Supply"

],

"current\_type": null,

"current\_vendor": null,

"default\_sort\_by": "created-ascending",

"description": "Brew your own potions at home using our fresh, ethically-sourced ingredients.",

"featured\_image": {},

"filters": {},

"handle": "ingredients",

"id": 266168401985,

"image": {},

"metafields": {},

"next\_product": null,

"previous\_product": null,

"products": {},

"products\_count": 1,

"published\_at": "2022-04-19 09:52:18 -0400",

"sort\_by": "",

"sort\_options": [],

"tags": [

"Burning"

],

"template\_suffix": "eight-products-per-page",

"title": "Ingredients",

"url": {}

}

##### Example

```liquid
{
  "all_products_count": 10,
  "all_tags": [
    "Burning",
    "dried",
    "extracts",
    "fresh",
    "ingredients",
    "plant",
    "supplies"
  ],
  "all_types": [
    "Animals & Pet Supplies",
    "Baking Flavors & Extracts",
    "Cooking & Baking Ingredients",
    "Dried Flowers",
    "Fruits & Vegetables",
    "Seasonings & Spices",
    "Water"
  ],
  "all_vendors": [
    "Clover's Apothecary",
    "Polina's Potent Potions",
    "Ted's Apothecary Supply"
  ],
  "current_type": null,
  "current_vendor": null,
  "default_sort_by": "created-ascending",
  "description": "Brew your own potions at home using our fresh, ethically-sourced ingredients.",
  "featured_image": {},
  "filters": {},
  "handle": "ingredients",
  "id": 266168401985,
  "image": {},
  "metafields": {},
  "next_product": null,
  "previous_product": null,
  "products": {},
  "products_count": 1,
  "published_at": "2022-04-19 09:52:18 -0400",
  "sort_by": "",
  "sort_options": [],
  "tags": [
    "Burning"
  ],
  "template_suffix": "eight-products-per-page",
  "title": "Ingredients",
  "url": {}
}
```

[Anchor to](/docs/api/liquid/objects/collection#template-using) 

## Templates using collection

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturecollection template

Theme architecture

collection template](/themes/architecture/templates/collection)

Was this section helpful?

YesNo