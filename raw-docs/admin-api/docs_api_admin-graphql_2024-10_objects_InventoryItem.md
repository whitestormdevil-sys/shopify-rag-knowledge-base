---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/objects/InventoryItem
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires `read_inventory` access scope or `read_products` access scope.

A [product variant's](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) inventory information across all locations. The inventory item connects the product variant to its [inventory levels](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryLevel) at different locations, tracking stock keeping unit (SKU), whether quantities are tracked, shipping requirements, and customs information for the product.

Learn more about [inventory object relationships](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#inventory-object-relationships).

## [Anchor to Fields](/docs/api/admin-graphql/latest/objects/InventoryItem#fields)Fields

* countryCodeOfOrigin (CountryCode)
* countryHarmonizedSystemCodes (CountryHarmonizedSystemCodeConnection!)
* createdAt (DateTime!)
* duplicateSkuCount (Int!)
* harmonizedSystemCode (String)
* id (ID!)
* inventoryHistoryUrl (URL)
* inventoryLevel (InventoryLevel)
* inventoryLevels (InventoryLevelConnection!)
* legacyResourceId (UnsignedInt64!)
* locationsCount (Count)
* measurement (InventoryItemMeasurement!)
* provinceCodeOfOrigin (String)
* requiresShipping (Boolean!)
* sku (String)
* tracked (Boolean!)
* trackedEditable (EditableProperty!)
* unitCost (MoneyV2)
* updatedAt (DateTime!)
* variants (ProductVariantConnection)
* variant (ProductVariant!): deprecated

[Anchor to countryCodeOfOrigin](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryCodeOfOrigin)countryCodeOfOrigin •[CountryCode](/docs/api/admin-graphql/latest/enums/CountryCode)
:   The ISO 3166-1 alpha-2 country code of where the item originated from.

    Show enum values

[Anchor to countryHarmonizedSystemCodes](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes)countryHarmonizedSystemCodes •[CountryHarmonizedSystemCodeConnection!](/docs/api/admin-graphql/latest/connections/CountryHarmonizedSystemCodeConnection) non-null
:   A list of country specific harmonized system codes.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.countryHarmonizedSystemCodes.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to createdAt](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.createdAt)createdAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the inventory item was created.

[Anchor to duplicateSkuCount](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.duplicateSkuCount)duplicateSkuCount •[Int!](/docs/api/admin-graphql/latest/scalars/Int) non-null
:   The number of inventory items that share the same SKU with this item.

[Anchor to harmonizedSystemCode](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.harmonizedSystemCode)harmonizedSystemCode •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The harmonized system code of the item. This must be a number between 6 and 13 digits.

[Anchor to id](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to inventoryHistoryUrl](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryHistoryUrl)inventoryHistoryUrl •[URL](/docs/api/admin-graphql/latest/scalars/URL)
:   The URL that points to the inventory history for the item.

[Anchor to inventoryLevel](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevel)inventoryLevel •[InventoryLevel](/docs/api/admin-graphql/latest/objects/InventoryLevel)
:   The inventory item's quantities at the specified location.

    Show fields

    ### Arguments

    [Anchor to locationId](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevel.arguments.locationId)locationId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   ID of the location for which the inventory level is requested.

    ---

[Anchor to inventoryLevels](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels)inventoryLevels •[InventoryLevelConnection!](/docs/api/admin-graphql/latest/connections/InventoryLevelConnection) non-null
:   A list of the inventory item's quantities for each location that the inventory item can be stocked at.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to query](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.inventoryLevels.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-inventory_group_id) inventory\_group\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-inventory_item_id) inventory\_item\_id •id

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-updated_at) updated\_at •time

    ---

[Anchor to legacyResourceId](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.legacyResourceId)legacyResourceId •[UnsignedInt64!](/docs/api/admin-graphql/latest/scalars/UnsignedInt64) non-null
:   The ID of the corresponding resource in the REST Admin API.

[Anchor to locationsCount](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.locationsCount)locationsCount •[Count](/docs/api/admin-graphql/latest/objects/Count)
:   The number of locations where this inventory item is stocked.

    Show fields

[Anchor to measurement](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.measurement)measurement •[InventoryItemMeasurement!](/docs/api/admin-graphql/latest/objects/InventoryItemMeasurement) non-null
:   The packaging dimensions of the inventory item.

    Show fields

[Anchor to provinceCodeOfOrigin](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.provinceCodeOfOrigin)provinceCodeOfOrigin •[String](/docs/api/admin-graphql/latest/scalars/String)
:   The ISO 3166-2 alpha-2 province code of where the item originated from.

[Anchor to requiresShipping](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.requiresShipping)requiresShipping •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether the inventory item requires shipping.

[Anchor to sku](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.sku)sku •[String](/docs/api/admin-graphql/latest/scalars/String)
:   Inventory item SKU. Case-sensitive string.

[Anchor to tracked](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.tracked)tracked •[Boolean!](/docs/api/admin-graphql/latest/scalars/Boolean) non-null
:   Whether inventory levels are tracked for the item.

[Anchor to trackedEditable](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.trackedEditable)trackedEditable •[EditableProperty!](/docs/api/admin-graphql/latest/objects/EditableProperty) non-null
:   Whether the value of the `tracked` field for the inventory item can be changed.

    Show fields

[Anchor to unitCost](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.unitCost)unitCost •[MoneyV2](/docs/api/admin-graphql/latest/objects/MoneyV2)
:   Unit cost associated with the inventory item. Note: the user must have "View product costs" permission granted in order to access this field once product granular permissions are enabled.

    Show fields

[Anchor to updatedAt](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.updatedAt)updatedAt •[DateTime!](/docs/api/admin-graphql/latest/scalars/DateTime) non-null
:   The date and time when the inventory item was updated.

[Anchor to variants](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variants)variants •[ProductVariantConnection](/docs/api/admin-graphql/latest/connections/ProductVariantConnection)
:   A paginated list of the variants that reference this inventory item.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variants.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variants.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variants.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variants.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    ---

[Anchor to variant](/docs/api/admin-graphql/latest/objects/InventoryItem#field-InventoryItem.fields.variant)variant •[ProductVariant!](/docs/api/admin-graphql/latest/objects/ProductVariant) non-nullDeprecated
:   Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/admin-graphql/latest/objects/InventoryItem#queries)Queries

* inventoryItem (InventoryItem)
* inventoryItems (InventoryItemConnection!)

[Anchor to inventoryItem](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItem)[inventoryItem](/docs/api/admin-graphql/latest/queries/inventoryItem) •query
:   Returns an
    [InventoryItem](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem)
    object by ID.

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItem.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the `InventoryItem` to return.

    ---

[Anchor to inventoryItems](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems)[inventoryItems](/docs/api/admin-graphql/latest/queries/inventoryItems) •query
:   Returns a list of inventory items.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.first)first •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The first `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to after](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.after)after •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come after the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to last](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.last)last •[Int](/docs/api/admin-graphql/latest/scalars/Int)
    :   The last `n` elements from the [paginated list](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to before](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.before)before •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   The elements that come before the specified [cursor](https://shopify.dev/api/usage/pagination-graphql).

    [Anchor to reverse](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.reverse)reverse •[Boolean](/docs/api/admin-graphql/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to query](/docs/api/admin-graphql/latest/objects/InventoryItem#query-inventoryItems.arguments.query)query •[String](/docs/api/admin-graphql/latest/scalars/String)
    :   A filter made up of terms, connectives, modifiers, and comparators.
        You can apply one or more filters to a query. Learn more about [Shopify API search syntax](https://shopify.dev/api/usage/search-syntax).

        Show filters

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-created_at) created\_at •time

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-id) id •id
        :   Filter by `id` range.

        Example:

        * `id:1234`
        * `id:>=1234`
        * `id:<=1234`

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-sku) sku •string
        :   Filter by the inventory item [`sku`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem#field-sku) field. [Learn more about SKUs](https://help.shopify.com/manual/products/details/sku).

        Example:

        * `sku:XYZ-12345`

        [Anchor to](/docs/api/admin-graphql/latest/objects/InventoryItem#argument-query-filter-updated_at) updated\_at •time

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/admin-graphql/latest/objects/InventoryItem#mutations)Mutations

* inventoryBulkToggleActivation (InventoryBulkToggleActivationPayload)
* inventoryItemUpdate (InventoryItemUpdatePayload)

[Anchor to inventoryBulkToggleActivation](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryBulkToggleActivation)[inventoryBulkToggleActivation](/docs/api/admin-graphql/latest/mutations/inventoryBulkToggleActivation) •mutation
:   Activates or deactivates an inventory item at multiple locations. When you activate an [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem) at a [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location), that location can stock and track quantities for that item. When you deactivate an inventory item at a location, the inventory item is no longer stocked at that location.

    The mutation accepts an inventory item ID and a list of location-specific activation settings. It returns the updated inventory item and any activated [`InventoryLevel`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryLevel) objects.

    Learn more about [managing inventory quantities and states](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps/manage-quantities-states#inventory-object-relationships).

    Show payload

    ### Arguments

    [Anchor to inventoryItemId](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryBulkToggleActivation.arguments.inventoryItemId)inventoryItemId •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the inventory item to modify the activation status locations for.

    [Anchor to inventoryItemUpdates](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryBulkToggleActivation.arguments.inventoryItemUpdates)inventoryItemUpdates •[[InventoryBulkToggleActivationInput!]!](/docs/api/admin-graphql/latest/input-objects/InventoryBulkToggleActivationInput) required
    :   A list of pairs of locations and activate status to update for the specified inventory item.

        Show input fields

    ---

[Anchor to inventoryItemUpdate](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryItemUpdate)[inventoryItemUpdate](/docs/api/admin-graphql/latest/mutations/inventoryItemUpdate) •mutation
:   Updates an [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem)'s properties including whether inventory is tracked, cost, SKU, and whether shipping is required. Inventory items represent the goods available to be shipped to customers.

    Show payload

    ### Arguments

    [Anchor to id](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryItemUpdate.arguments.id)id •[ID!](/docs/api/admin-graphql/latest/scalars/ID) required
    :   The ID of the inventory item to update.

    [Anchor to input](/docs/api/admin-graphql/latest/objects/InventoryItem#mutation-inventoryItemUpdate.arguments.input)input •[InventoryItemInput!](/docs/api/admin-graphql/latest/input-objects/InventoryItemInput) required
    :   The input fields that update an
        [`inventoryItem`](https://shopify.dev/api/admin-graphql/latest/queries/inventoryitem).

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/admin-graphql/latest/objects/InventoryItem#interfaces)Interfaces

* LegacyInteroperability
* Node

[Anchor to LegacyInteroperability](/docs/api/admin-graphql/latest/objects/InventoryItem#interface-LegacyInteroperability)[LegacyInteroperability](/docs/api/admin-graphql/latest/interfaces/LegacyInteroperability) •interface

[Anchor to Node](/docs/api/admin-graphql/latest/objects/InventoryItem#interface-Node)[Node](/docs/api/admin-graphql/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo