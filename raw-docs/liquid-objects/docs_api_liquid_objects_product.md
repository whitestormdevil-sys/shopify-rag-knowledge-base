---
source: https://shopify.dev/docs/api/liquid/objects/product
---

A [product](https://help.shopify.com/manual/products) in the store.

## Properties

[Anchor to](/docs/api/liquid/objects/product#product-available) 

available**available** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if at least one of the variants of the product is available. Returns `false` if not.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.
    * The variant has an associated [delivery profile](/docs/apps/selling-strategies/purchase-options/deferred/shipping-delivery/delivery-profiles) with a valid shipping rate.

[Anchor to](/docs/api/liquid/objects/product#product-category) 

category**category** [taxonomy\_category](/docs/api/liquid/objects/taxonomy_category)

:   The taxonomy category for the product

[Anchor to](/docs/api/liquid/objects/product#product-collections) 

collections**collections** array of [collection](/docs/api/liquid/objects/collection)

:   The collections that the product belongs to.

    Note

    Collections that aren't [available](https://help.shopify.com/manual/products/collections/make-collections-available) on
    the Online Store sales channel aren't included.

    **Note:**

    Collections that aren't [available](https://help.shopify.com/manual/products/collections/make-collections-available) on
    the Online Store sales channel aren't included.

    **Note:** Collections that aren&#39;t <a href="https://help.shopify.com/manual/products/collections/make-collections-available">available</a> on
    the Online Store sales channel aren&#39;t included.

[Anchor to](/docs/api/liquid/objects/product#product-compare_at_price) 

compare\_at\_price**compare\_at\_price** [number](/docs/api/liquid/basics#number)

:   The lowest **compare at** price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-compare_at_price_max) 

compare\_at\_price\_max**compare\_at\_price\_max** [number](/docs/api/liquid/basics#number)

:   The highest **compare at** price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-compare_at_price_min) 

compare\_at\_price\_min**compare\_at\_price\_min** [number](/docs/api/liquid/basics#number)

:   The lowest **compare at** price of any variants of the product in the currency's subunit. This is the same as
    `product.compare_at_price`.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-compare_at_price_varies) 

compare\_at\_price\_varies**compare\_at\_price\_varies** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the variant **compare at** prices of the product vary. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/product#product-content) 

content**content** [string](/docs/api/liquid/basics#string)

:   The description of the product.

    Note

    This is the same value as [`product.description`](/docs/api/liquid/objects/product#product-description).

    **Note:**

    This is the same value as [`product.description`](/docs/api/liquid/objects/product#product-description).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/product#product-description"><code>product.description</code></a>.

[Anchor to](/docs/api/liquid/objects/product#product-created_at) 

created\_at**created\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the product was created.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/product#product-description) 

description**description** [string](/docs/api/liquid/basics#string)

:   The description of the product.

    Note

    This is the same value as [`product.content`](/docs/api/liquid/objects/product#product-content).

    **Note:**

    This is the same value as [`product.content`](/docs/api/liquid/objects/product#product-content).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/product#product-content"><code>product.content</code></a>.

[Anchor to](/docs/api/liquid/objects/product#product-featured_image) 

featured\_image**featured\_image** [image](/docs/api/liquid/objects/image)

:   The first (featured) image attached to the product.

[Anchor to](/docs/api/liquid/objects/product#product-featured_media) 

featured\_media**featured\_media** [media](/docs/api/liquid/objects/media)

:   The first (featured) media attached to the product.

    Note

    In search results or a filtered collection, the [media](/docs/api/liquid/objects/media) of the most relevant variant is returned. Relevancy is based on search terms and applied filters.

    **Note:**

    In search results or a filtered collection, the [media](/docs/api/liquid/objects/media) of the most relevant variant is returned. Relevancy is based on search terms and applied filters.

    **Note:** In search results or a filtered collection, the <a href="/docs/api/liquid/objects/media">media</a> of the most relevant variant is returned. Relevancy is based on search terms and applied filters.

    Tip

    You can use [media filters](/docs/api/liquid/filters/media-filters) to output media URLs and displays. To learn about how
    to include media in your theme, refer to [Support product media](/themes/product-merchandising/media/support-media).

    **Tip:**

    You can use [media filters](/docs/api/liquid/filters/media-filters) to output media URLs and displays. To learn about how
    to include media in your theme, refer to [Support product media](/themes/product-merchandising/media/support-media).

    **Tip:** You can use <a href="/docs/api/liquid/filters/media-filters">media filters</a> to output media URLs and displays. To learn about how
    to include media in your theme, refer to <a href="/themes/product-merchandising/media/support-media">Support product media</a>.

[Anchor to](/docs/api/liquid/objects/product#product-first_available_variant) 

first\_available\_variant**first\_available\_variant** [variant](/docs/api/liquid/objects/variant)

:   The first available variant of the product.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.

[Anchor to](/docs/api/liquid/objects/product#product-gift_card?) 

gift\_card?**gift\_card?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the product is a gift card. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/product#product-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the product.

[Anchor to](/docs/api/liquid/objects/product#product-has_only_default_variant) 

has\_only\_default\_variant**has\_only\_default\_variant** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the product doesn't have any options. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/product#product-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the product.

[Anchor to](/docs/api/liquid/objects/product#product-images) 

images**images** array of [image](/docs/api/liquid/objects/image)

:   The images attached to the product.

[Anchor to](/docs/api/liquid/objects/product#product-media) 

media**media** array of [media](/docs/api/liquid/objects/media)

:   The media attached to the product, sorted by the date it was added to the product.

    Tip

    You can use [media filters](/docs/api/liquid/filters/media-filters) to output media URLs and displays. To learn about how
    to include media in your theme, refer to [Support product media](/themes/product-merchandising/media/support-media).

    **Tip:**

    You can use [media filters](/docs/api/liquid/filters/media-filters) to output media URLs and displays. To learn about how
    to include media in your theme, refer to [Support product media](/themes/product-merchandising/media/support-media).

    **Tip:** You can use <a href="/docs/api/liquid/filters/media-filters">media filters</a> to output media URLs and displays. To learn about how
    to include media in your theme, refer to <a href="/themes/product-merchandising/media/support-media">Support product media</a>.

[Anchor to](/docs/api/liquid/objects/product#product-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the product.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/product#product-options) 

options**options** array of [string](/docs/api/liquid/basics#string)

:   The option names of the product.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the options

    You can use the [`size` filter](/docs/api/liquid/filters/size) with dot notation to determine how many options a product has.

    9

    1

    2

    3

    4

    5

    {% if product.options.size > 0 -%}

    {% for option in product.options -%}

    - {{ option }}

    {%- endfor %}

    {%- endif %}

    ##### Code

    ```liquid
    {% if product.options.size > 0 -%}
      {% for option in product.options -%}
        - {{ option }}
      {%- endfor %}
    {%- endif %}
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "options": [
          "Size",
          "Strength"
        ]
      }
    }
    ```

    ## Output

    9

    1

    2

    - Size

    - Strength

    ##### Output

    ```liquid
    - Size
    - Strength
    ```

[Anchor to](/docs/api/liquid/objects/product#product-options_by_name) 

options\_by\_name**options\_by\_name**

:   Allows you to access a specific [product option](/docs/api/liquid/objects/product_option) by its name.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Output the values for a specific option

    When accessing a specific option, the name is case-insensitive.

    9

    1

    2

    3

    4

    5

    6

    7

    8

    <label>

    Strength

    <select>

    {%- for value in product.options\_by\_name['strength'].values %}

    <option>{{ value }}</option>

    {%- endfor %}

    </select>

    </label>

    ##### Code

    ```liquid
    <label>
      Strength
      <select>
        {%- for value in product.options_by_name['strength'].values %}
        <option>{{ value }}</option>
        {%- endfor %}
      </select>
    </label>
    ```

    ##### Data

    ```liquid
    {
      "product": {
        "options_by_name": {}
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

    <label>

    Strength

    <select>

    <option>Low</option>

    <option>Medium</option>

    <option>High</option>

    </select>

    </label>

    ##### Output

    ```liquid
    <label>
      Strength
      <select>
        <option>Low</option>
        <option>Medium</option>
        <option>High</option>
      </select>
    </label>
    ```

[Anchor to](/docs/api/liquid/objects/product#product-options_with_values) 

options\_with\_values**options\_with\_values** array of [product\_option](/docs/api/liquid/objects/product_option)

:   The options on the product.

[Anchor to](/docs/api/liquid/objects/product#product-price) 

price**price** [number](/docs/api/liquid/basics#number)

:   The lowest price of any variants of the product in the currency's subunit.

    Note

    This is the same value as [`product.price_min`](/docs/api/liquid/objects/product#product-price_min).

    **Note:**

    This is the same value as [`product.price_min`](/docs/api/liquid/objects/product#product-price_min).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/product#product-price\_min"><code><span class="PreventFireFoxApplyingGapToWBR">product.price<wbr/>\_min</span></code></a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-price_max) 

price\_max**price\_max** [number](/docs/api/liquid/basics#number)

:   The highest price of any variants of the product in the currency's subunit.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-price_min) 

price\_min**price\_min** [number](/docs/api/liquid/basics#number)

:   The lowest price of any variants of the product in the currency's subunit.

    Note

    This is the same value as [`product.price`](/docs/api/liquid/objects/product#product-price).

    **Note:**

    This is the same value as [`product.price`](/docs/api/liquid/objects/product#product-price).

    **Note:** This is the same value as <a href="/docs/api/liquid/objects/product#product-price"><code>product.price</code></a>.

    The value is output in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    Tip

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:**

    Use [money filters](/docs/api/liquid/filters/money-filters) to output a formatted price.

    **Tip:** Use <a href="/docs/api/liquid/filters/money-filters">money filters</a> to output a formatted price.

[Anchor to](/docs/api/liquid/objects/product#product-price_varies) 

price\_varies**price\_varies** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the product's variant prices vary. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/product#product-published_at) 

published\_at**published\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the product was published.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/product#product-quantity_price_breaks_configured?) 

quantity\_price\_breaks\_configured?**quantity\_price\_breaks\_configured?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the product has at least one variant with quantity price breaks in the current customer context.
    Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/product#product-requires_selling_plan) 

requires\_selling\_plan**requires\_selling\_plan** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if all of the variants of the product require a selling plan. Returns `false` if not.

    Note

    A variant requires a selling plan if [`variant.requires_selling_plan`](/docs/api/liquid/objects/variant#variant-requires_selling_plan)
    is `true`.

    **Note:**

    A variant requires a selling plan if [`variant.requires_selling_plan`](/docs/api/liquid/objects/variant#variant-requires_selling_plan)
    is `true`.

    **Note:** A variant requires a selling plan if <a href="/docs/api/liquid/objects/variant#variant-requires\_selling\_plan"><code><span class="PreventFireFoxApplyingGapToWBR">variant.requires<wbr/>\_selling<wbr/>\_plan</span></code></a>
    is <code>true</code>.

[Anchor to](/docs/api/liquid/objects/product#product-selected_or_first_available_selling_plan_allocation) 

selected\_or\_first\_available\_selling\_plan\_allocation**selected\_or\_first\_available\_selling\_plan\_allocation** [selling\_plan\_allocation](/docs/api/liquid/objects/selling_plan_allocation)

:   The currently selected, or first available, selling plan allocation.

    The following logic is used to determine which selling plan allocation is returned:

    | Selling plan allocation | Return criteria |
    | --- | --- |
    | The currently selected allocation | Returned if a variant and selling plan are selected.  The selected variant is determined by the `variant` URL parameter, and the selected selling plan is determined by the `selling_plan` URL parameter. |
    | The first allocation on the first available variant | Returned if no allocation is currently selected. |
    | The first allocation on the first variant | Returned if no allocation is currently selected, and there are no available variants. |

    If the product doesn't have any selling plans, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/product#product-selected_or_first_available_variant) 

selected\_or\_first\_available\_variant**selected\_or\_first\_available\_variant** [variant](/docs/api/liquid/objects/variant)

:   The currently selected or first available variant of the product.

    If a variant is selected, it will be returned, regardless of its availability. Otherwise, the first available variant is returned. If no available variant exists, the first variant is returned.

    A selected variant is determined by the following criteria:

    * On product pages, it is based on the variant ID set in the `variant` URL parameter.
    * In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

    For a variant to be available, it needs to meet one of the following criteria:

    * The `variant.inventory_quantity` is greater than 0.
    * The `variant.inventory_policy` is set to `continue`.
    * The `variant.inventory_management` is `nil`.

[Anchor to](/docs/api/liquid/objects/product#product-selected_selling_plan) 

selected\_selling\_plan**selected\_selling\_plan** [selling\_plan](/docs/api/liquid/objects/selling_plan)

:   The currently selected selling plan.

    If no selling plan is selected, then `nil` is returned.

    Note

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:**

    The selected selling plan is determined by the `selling_plan` URL parameter.

    **Note:** The selected selling plan is determined by the <code><span class="PreventFireFoxApplyingGapToWBR">selling<wbr/>\_plan</span></code> URL parameter.

[Anchor to](/docs/api/liquid/objects/product#product-selected_selling_plan_allocation) 

selected\_selling\_plan\_allocation**selected\_selling\_plan\_allocation** [selling\_plan\_allocation](/docs/api/liquid/objects/selling_plan_allocation)

:   The currently selected selling plan allocation for the currently selected variant.

    If no variant and selling plan are selected, then `nil` is returned.

    Note

    The selected variant is determined by the `variant` URL parameter, and the selected selling plan is determined by the
    `selling_plan` URL parameter.

    **Note:**

    The selected variant is determined by the `variant` URL parameter, and the selected selling plan is determined by the
    `selling_plan` URL parameter.

    **Note:** The selected variant is determined by the <code>variant</code> URL parameter, and the selected selling plan is determined by the
    <code><span class="PreventFireFoxApplyingGapToWBR">selling<wbr/>\_plan</span></code> URL parameter.

[Anchor to](/docs/api/liquid/objects/product#product-selected_variant) 

selected\_variant**selected\_variant** [variant](/docs/api/liquid/objects/variant)

:   The currently selected variant of the product.

    If no variant is currently selected, then `nil` is returned.

    Note

    On product pages, it is based on the variant ID set in the `variant` URL parameter.
    In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

    **Note:**

    On product pages, it is based on the variant ID set in the `variant` URL parameter.
    In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

    **Note:** On product pages, it is based on the variant ID set in the <code>variant</code> URL parameter.
    In search results and filtered collections, it is the most relevant variant based on search terms and applied filters.

[Anchor to](/docs/api/liquid/objects/product#product-selling_plan_groups) 

selling\_plan\_groups**selling\_plan\_groups** array of [selling\_plan\_group](/docs/api/liquid/objects/selling_plan_group)

:   The selling plan groups that the variants of the product are included in.

[Anchor to](/docs/api/liquid/objects/product#product-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   The [tags](https://help.shopify.com/manual/shopify-admin/productivity-tools/using-tags) of the product.

    Note

    The tags are returned in alphabetical order.

    **Note:**

    The tags are returned in alphabetical order.

    **Note:** The tags are returned in alphabetical order.

[Anchor to](/docs/api/liquid/objects/product#product-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) of the product.

    The name doesn't include the `product.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the product, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/product#product-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the product.

[Anchor to](/docs/api/liquid/objects/product#product-type) 

type**type** [string](/docs/api/liquid/basics#string)

:   The type of the product.

[Anchor to](/docs/api/liquid/objects/product#product-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the product.

    If a product is rendered in search results or a filtered collection, then the URL contains the `variant` parameter of the most relevant variant.

    9

    1

    /products/gorgeous-wooden-computer?variant=1234567890

    ```liquid
    /products/gorgeous-wooden-computer?variant=1234567890
    ```

    If a product is rendered as a [product recommendation](/docs/themes/product-merchandising/recommendations), then the URL contains tracking parameters:

    9

    1

    /products/gorgeous-wooden-computer?pr\_choice=default&pr\_prod\_strat=description&pr\_rec\_pid=13&pr\_ref\_pid=17&pr\_seq=alternating

    ```liquid
    /products/gorgeous-wooden-computer?pr_choice=default&pr_prod_strat=description&pr_rec_pid=13&pr_ref_pid=17&pr_seq=alternating
    ```

[Anchor to](/docs/api/liquid/objects/product#product-variants) 

variants**variants** array of [variant](/docs/api/liquid/objects/variant)

:   The variants of the product.

    Note

    Returns a maximum of 250 variants when unpaginated.
    Tip:
    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many variants to show per page, up to a limit of 50.

    **Note:**

    Returns a maximum of 250 variants when unpaginated.
    Tip:
    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many variants to show per page, up to a limit of 50.

    **Note:** Returns a maximum of 250 variants when unpaginated.
    Tip:
    Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many variants to show per page, up to a limit of 50.

[Anchor to](/docs/api/liquid/objects/product#product-variants_count) 

variants\_count**variants\_count** [number](/docs/api/liquid/basics#number)

:   The total number of variants for the product.

[Anchor to](/docs/api/liquid/objects/product#product-vendor) 

vendor**vendor** [string](/docs/api/liquid/basics#string)

:   The vendor of the product.

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

{

"available": true,

"category": {},

"collections": [],

"compare\_at\_price": "25.00",

"compare\_at\_price\_max": "25.00",

"compare\_at\_price\_min": "25.00",

"compare\_at\_price\_varies": false,

"content": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",

"created\_at": "2022-04-13 14:46:16 -0400",

"description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",

"featured\_image": {},

"featured\_media": {},

"first\_available\_variant": {},

"gift\_card?": false,

"handle": "health-potion",

"has\_only\_default\_variant": false,

"id": 6786188247105,

"images": [],

"media": [],

"metafields": {},

"options": [

"Size",

"Strength"

],

"options\_by\_name": {},

"options\_with\_values": [],

"price": "10.00",

"price\_max": "22.00",

"price\_min": "10.00",

"price\_varies": true,

"published\_at": "2022-04-13 14:53:34 -0400",

"quantity\_price\_breaks\_configured?": false,

"requires\_selling\_plan": false,

"selected\_or\_first\_available\_selling\_plan\_allocation": {},

"selected\_or\_first\_available\_variant": {},

"selected\_selling\_plan": null,

"selected\_selling\_plan\_allocation": null,

"selected\_variant": null,

"selling\_plan\_groups": [],

"tags": [

"healing"

],

"template\_suffix": "",

"title": "Health potion",

"type": {},

"url": {},

"variants": [],

"variants\_count": 9,

"vendor": "Polina's Potent Potions"

}

##### Example

```liquid
{
  "available": true,
  "category": {},
  "collections": [],
  "compare_at_price": "25.00",
  "compare_at_price_max": "25.00",
  "compare_at_price_min": "25.00",
  "compare_at_price_varies": false,
  "content": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",
  "created_at": "2022-04-13 14:46:16 -0400",
  "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>",
  "featured_image": {},
  "featured_media": {},
  "first_available_variant": {},
  "gift_card?": false,
  "handle": "health-potion",
  "has_only_default_variant": false,
  "id": 6786188247105,
  "images": [],
  "media": [],
  "metafields": {},
  "options": [
    "Size",
    "Strength"
  ],
  "options_by_name": {},
  "options_with_values": [],
  "price": "10.00",
  "price_max": "22.00",
  "price_min": "10.00",
  "price_varies": true,
  "published_at": "2022-04-13 14:53:34 -0400",
  "quantity_price_breaks_configured?": false,
  "requires_selling_plan": false,
  "selected_or_first_available_selling_plan_allocation": {},
  "selected_or_first_available_variant": {},
  "selected_selling_plan": null,
  "selected_selling_plan_allocation": null,
  "selected_variant": null,
  "selling_plan_groups": [],
  "tags": [
    "healing"
  ],
  "template_suffix": "",
  "title": "Health potion",
  "type": {},
  "url": {},
  "variants": [],
  "variants_count": 9,
  "vendor": "Polina's Potent Potions"
}
```

[Anchor to](/docs/api/liquid/objects/product#template-using) 

## Templates using product

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architectureproduct template

Theme architecture

product template](/themes/architecture/templates/product)

Was this section helpful?

YesNo