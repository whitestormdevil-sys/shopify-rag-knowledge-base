---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/ProductVariant
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `unauthenticated_read_product_listings` access scope.

A product variant represents a different version of a product, such as differing sizes or differing colors.

## [Anchor to Fields](/docs/api/storefront/latest/objects/ProductVariant#fields)Fields

* availableForSale (Boolean!)
* barcode (String)
* compareAtPrice (MoneyV2)
* components (ProductVariantComponentConnection!)
* currentlyNotInStock (Boolean!)
* groupedBy (ProductVariantConnection!)
* id (ID!)
* image (Image)
* metafield (Metafield)
* metafields ([Metafield]!)
* price (MoneyV2!)
* product (Product!)
* quantityAvailable (Int)
* quantityPriceBreaks (QuantityPriceBreakConnection!)
* quantityRule (QuantityRule!)
* requiresComponents (Boolean!)
* requiresShipping (Boolean!)
* selectedOptions ([SelectedOption!]!)
* sellingPlanAllocations (SellingPlanAllocationConnection!)
* shopPayInstallmentsPricing (ShopPayInstallmentsProductVariantPricing)
* sku (String)
* storeAvailability (StoreAvailabilityConnection!)
* taxable (Boolean!)
* title (String!)
* unitPrice (MoneyV2)
* unitPriceMeasurement (UnitPriceMeasurement)
* weight (Float)
* weightUnit (WeightUnit!)

[Anchor to availableForSale](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.availableForSale)availableForSale •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Indicates if the product variant is available for sale.

[Anchor to barcode](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.barcode)barcode •[String](/docs/api/storefront/latest/scalars/String)
:   The barcode (for example, ISBN, UPC, or GTIN) associated with the variant.

[Anchor to compareAtPrice](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.compareAtPrice)compareAtPrice •[MoneyV2](/docs/api/storefront/latest/objects/MoneyV2)
:   The compare at price of the variant. This can be used to mark a variant as on sale, when `compareAtPrice` is higher than `price`.

    Show fields

[Anchor to components](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.components)components •[ProductVariantComponentConnection!](/docs/api/storefront/latest/connections/ProductVariantComponentConnection) non-null
:   List of bundles components included in the variant considering only fixed bundles.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.components.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.components.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.components.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.components.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    ---

[Anchor to currentlyNotInStock](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.currentlyNotInStock)currentlyNotInStock •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Whether a product is out of stock but still available for purchase (used for backorders).

[Anchor to groupedBy](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.groupedBy)groupedBy •[ProductVariantConnection!](/docs/api/storefront/latest/connections/ProductVariantConnection) non-null
:   List of bundles that include this variant considering only fixed bundles.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.groupedBy.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.groupedBy.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.groupedBy.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.groupedBy.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    ---

[Anchor to id](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to image](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.image)image •[Image](/docs/api/storefront/latest/objects/Image)
:   Image associated with the product variant. This field falls back to the product image if no image is available.

    Show fields

[Anchor to metafield](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to price](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.price)price •[MoneyV2!](/docs/api/storefront/latest/objects/MoneyV2) non-null
:   The product variant’s price.

    Show fields

[Anchor to product](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.product)product •[Product!](/docs/api/storefront/latest/objects/Product) non-null
:   The product object that the product variant belongs to.

    Show fields

[Anchor to quantityAvailable](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityAvailable)quantityAvailable •[Int](/docs/api/storefront/latest/scalars/Int) Token access required
:   The total sellable quantity of the variant for online sales channels.

[Anchor to quantityPriceBreaks](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityPriceBreaks)quantityPriceBreaks •[QuantityPriceBreakConnection!](/docs/api/storefront/latest/connections/QuantityPriceBreakConnection) non-null
:   A list of quantity breaks for the product variant.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityPriceBreaks.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityPriceBreaks.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityPriceBreaks.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityPriceBreaks.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    ---

[Anchor to quantityRule](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.quantityRule)quantityRule •[QuantityRule!](/docs/api/storefront/latest/objects/QuantityRule) non-null
:   The quantity rule for the product variant in a given context.

    Show fields

[Anchor to requiresComponents](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.requiresComponents)requiresComponents •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Whether a product variant requires components. The default value is `false`.
    If `true`, then the product variant can only be purchased as a parent bundle with components.

[Anchor to requiresShipping](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.requiresShipping)requiresShipping •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Whether a customer needs to provide a shipping address when placing an order for the product variant.

[Anchor to selectedOptions](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.selectedOptions)selectedOptions •[[SelectedOption!]!](/docs/api/storefront/latest/objects/SelectedOption) non-null
:   List of product options applied to the variant.

    Show fields

[Anchor to sellingPlanAllocations](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations)sellingPlanAllocations •[SellingPlanAllocationConnection!](/docs/api/storefront/latest/connections/SellingPlanAllocationConnection) non-null
:   Represents an association between a variant and a selling plan. Selling plan allocations describe which selling plans are available for each variant, and what their impact is on pricing.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sellingPlanAllocations.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to shopPayInstallmentsPricing](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.shopPayInstallmentsPricing)shopPayInstallmentsPricing •[ShopPayInstallmentsProductVariantPricing](/docs/api/storefront/latest/objects/ShopPayInstallmentsProductVariantPricing) Token access required
:   The Shop Pay Installments pricing information for the product variant.

    Show fields

[Anchor to sku](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.sku)sku •[String](/docs/api/storefront/latest/scalars/String)
:   The SKU (stock keeping unit) associated with the variant.

[Anchor to storeAvailability](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability)storeAvailability •[StoreAvailabilityConnection!](/docs/api/storefront/latest/connections/StoreAvailabilityConnection) non-null
:   The in-store pickup availability of this variant by location.

    Show fields

    ### Arguments

    [Anchor to near](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.near)near •[GeoCoordinateInput](/docs/api/storefront/latest/input-objects/GeoCoordinateInput)
    :   Used to sort results based on proximity to the provided location.

        Show input fields

    [Anchor to first](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.storeAvailability.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to taxable](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.taxable)taxable •[Boolean!](/docs/api/storefront/latest/scalars/Boolean) non-null
:   Whether tax is charged when the product variant is sold.

[Anchor to title](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.title)title •[String!](/docs/api/storefront/latest/scalars/String) non-null
:   The product variant’s title.

[Anchor to unitPrice](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.unitPrice)unitPrice •[MoneyV2](/docs/api/storefront/latest/objects/MoneyV2)
:   The unit price value for the variant based on the variant's measurement.

    Show fields

[Anchor to unitPriceMeasurement](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.unitPriceMeasurement)unitPriceMeasurement •[UnitPriceMeasurement](/docs/api/storefront/latest/objects/UnitPriceMeasurement)
:   The unit price measurement for the variant.

    Show fields

[Anchor to weight](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.weight)weight •[Float](/docs/api/storefront/latest/scalars/Float)
:   The weight of the product variant in the unit system specified with `weight_unit`.

[Anchor to weightUnit](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.weightUnit)weightUnit •[WeightUnit!](/docs/api/storefront/latest/enums/WeightUnit) non-null
:   Unit of measurement for weight.

    Show enum values

### Deprecated fields

* compareAtPriceV2 (MoneyV2): deprecated
* priceV2 (MoneyV2!): deprecated

[Anchor to compareAtPriceV2](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.compareAtPriceV2)compareAtPriceV2 •[MoneyV2](/docs/api/storefront/latest/objects/MoneyV2) Deprecated
:   Show fields

[Anchor to priceV2](/docs/api/storefront/latest/objects/ProductVariant#field-ProductVariant.fields.priceV2)priceV2 •[MoneyV2!](/docs/api/storefront/latest/objects/MoneyV2) non-nullDeprecated
:   Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/ProductVariant#interfaces)Interfaces

* HasMetafields
* Node

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/ProductVariant#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/storefront/latest/objects/ProductVariant#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo