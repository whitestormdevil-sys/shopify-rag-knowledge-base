---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/Cart
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

A cart represents the merchandise that a buyer intends to purchase,
and the estimated cost associated with the cart. Learn how to
[interact with a cart](https://shopify.dev/custom-storefronts/internationalization/international-pricing)
during a customer's session.

## [Anchor to Fields](/docs/api/storefront/latest/objects/Cart#fields)Fields

* appliedGiftCards ([AppliedGiftCard!]!)
* attribute (Attribute)
* attributes ([Attribute!]!)
* buyerIdentity (CartBuyerIdentity!)
* checkoutUrl (URL!)
* cost (CartCost!)
* createdAt (DateTime!)
* delivery (CartDelivery!)
* deliveryGroups (CartDeliveryGroupConnection!)
* discountAllocations ([CartDiscountAllocation!]!)
* discountCodes ([CartDiscountCode!]!)
* id (ID!)
* lines (BaseCartLineConnection!)
* metafield (Metafield)
* metafields ([Metafield]!)
* note (String)
* totalQuantity (Int!)
* updatedAt (DateTime!)
* estimatedCost (CartEstimatedCost!): deprecated

[Anchor to appliedGiftCards](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.appliedGiftCards)appliedGiftCards •[[AppliedGiftCard!]!](/docs/api/storefront/latest/objects/AppliedGiftCard) non-null
:   The gift cards that have been applied to the cart.

    Show fields

[Anchor to attribute](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.attribute)attribute •[Attribute](/docs/api/storefront/latest/objects/Attribute)
:   An attribute associated with the cart.

    Show fields

    ### Arguments

    [Anchor to key](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.attribute.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The key of the attribute.

    ---

[Anchor to attributes](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.attributes)attributes •[[Attribute!]!](/docs/api/storefront/latest/objects/Attribute) non-null
:   The attributes associated with the cart. Attributes are represented as key-value pairs.

    Show fields

[Anchor to buyerIdentity](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.buyerIdentity)buyerIdentity •[CartBuyerIdentity!](/docs/api/storefront/latest/objects/CartBuyerIdentity) non-null
:   Information about the buyer that's interacting with the cart.

    Show fields

[Anchor to checkoutUrl](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.checkoutUrl)checkoutUrl •[URL!](/docs/api/storefront/latest/scalars/URL) non-null
:   The URL of the checkout for the cart.

[Anchor to cost](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.cost)cost •[CartCost!](/docs/api/storefront/latest/objects/CartCost) non-null
:   The estimated costs that the buyer will pay at checkout. The costs are subject to change and changes will be reflected at checkout. The `cost` field uses the `buyerIdentity` field to determine [international pricing](https://shopify.dev/custom-storefronts/internationalization/international-pricing).

    Show fields

[Anchor to createdAt](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.createdAt)createdAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null
:   The date and time when the cart was created.

[Anchor to delivery](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.delivery)delivery •[CartDelivery!](/docs/api/storefront/latest/objects/CartDelivery) non-null
:   The delivery properties of the cart.

    Show fields

[Anchor to deliveryGroups](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups)deliveryGroups •[CartDeliveryGroupConnection!](/docs/api/storefront/latest/connections/CartDeliveryGroupConnection) non-null
:   The delivery groups available for the cart, based on the buyer identity default
    delivery address preference or the default address of the logged-in customer.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    [Anchor to withCarrierRates](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.deliveryGroups.arguments.withCarrierRates)withCarrierRates •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Whether to include [carrier-calculated delivery rates](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers) in the response.

        By default, only static shipping rates are returned. This argument requires mandatory usage of the [`@defer` directive](https://shopify.dev/docs/api/storefront#directives).

        For more information, refer to [fetching carrier-calculated rates for the cart using `@defer`](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/defer#fetching-carrier-calculated-rates-for-the-cart-using-defer).

    ---

[Anchor to discountAllocations](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.discountAllocations)discountAllocations •[[CartDiscountAllocation!]!](/docs/api/storefront/latest/interfaces/CartDiscountAllocation) non-null
:   The discounts that have been applied to the entire cart.

    Show fields

[Anchor to discountCodes](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.discountCodes)discountCodes •[[CartDiscountCode!]!](/docs/api/storefront/latest/objects/CartDiscountCode) non-null
:   The case-insensitive discount codes that the customer added at checkout.

    Show fields

[Anchor to id](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to lines](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines)lines •[BaseCartLineConnection!](/docs/api/storefront/latest/connections/BaseCartLineConnection) non-null
:   A list of lines containing information about the items the customer intends to purchase.

    Show fields

    ### Arguments

    [Anchor to first](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines.arguments.first)first •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the first `n` elements from the list.

    [Anchor to after](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines.arguments.after)after •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come after the specified cursor.

    [Anchor to last](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines.arguments.last)last •[Int](/docs/api/storefront/latest/scalars/Int)
    :   Returns up to the last `n` elements from the list.

    [Anchor to before](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines.arguments.before)before •[String](/docs/api/storefront/latest/scalars/String)
    :   Returns the elements that come before the specified cursor.

    [Anchor to reverse](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.lines.arguments.reverse)reverse •[Boolean](/docs/api/storefront/latest/scalars/Boolean) Default:false
    :   Reverse the order of the underlying list.

    ---

[Anchor to metafield](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.metafield)metafield •[Metafield](/docs/api/storefront/latest/objects/Metafield) Token access required
:   A [custom field](https://shopify.dev/docs/apps/build/custom-data), including its `namespace` and `key`, that's associated with a Shopify resource for the purposes of adding and storing additional information.

    Show fields

    ### Arguments

    [Anchor to namespace](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.metafield.arguments.namespace)namespace •[String](/docs/api/storefront/latest/scalars/String)
    :   The container the metafield belongs to. If omitted, the app-reserved namespace will be used.

    [Anchor to key](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.metafield.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The identifier for the metafield.

    ---

[Anchor to metafields](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.metafields)metafields •[[Metafield]!](/docs/api/storefront/latest/objects/Metafield) non-null Token access required
:   A list of [custom fields](/docs/apps/build/custom-data) that a merchant associates with a Shopify resource.

    Show fields

    ### Arguments

    [Anchor to identifiers](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.metafields.arguments.identifiers)identifiers •[[HasMetafieldsIdentifier!]!](/docs/api/storefront/latest/input-objects/HasMetafieldsIdentifier) required
    :   The list of metafields to retrieve by namespace and key.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to note](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.note)note •[String](/docs/api/storefront/latest/scalars/String)
:   A note that's associated with the cart. For example, the note can be a personalized message to the buyer.

[Anchor to totalQuantity](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.totalQuantity)totalQuantity •[Int!](/docs/api/storefront/latest/scalars/Int) non-null
:   The total number of items in the cart.

[Anchor to updatedAt](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.updatedAt)updatedAt •[DateTime!](/docs/api/storefront/latest/scalars/DateTime) non-null
:   The date and time when the cart was updated.

[Anchor to estimatedCost](/docs/api/storefront/latest/objects/Cart#field-Cart.fields.estimatedCost)estimatedCost •[CartEstimatedCost!](/docs/api/storefront/latest/objects/CartEstimatedCost) non-nullDeprecated
:   Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Queries](/docs/api/storefront/latest/objects/Cart#queries)Queries

* cart (Cart)

[Anchor to cart](/docs/api/storefront/latest/objects/Cart#query-cart)[cart](/docs/api/storefront/latest/queries/cart) •query
:   Retrieve a cart by its ID. For more information, refer to
    [Manage a cart with the Storefront API](https://shopify.dev/custom-storefronts/cart/manage).

    Show fields

    ### Arguments

    [Anchor to id](/docs/api/storefront/latest/objects/Cart#query-cart.arguments.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Mutations](/docs/api/storefront/latest/objects/Cart#mutations)Mutations

* cartAttributesUpdate (CartAttributesUpdatePayload)
* cartBuyerIdentityUpdate (CartBuyerIdentityUpdatePayload)
* cartCreate (CartCreatePayload)
* cartDeliveryAddressesAdd (CartDeliveryAddressesAddPayload)
* cartDeliveryAddressesRemove (CartDeliveryAddressesRemovePayload)
* cartDeliveryAddressesReplace (CartDeliveryAddressesReplacePayload)
* cartDeliveryAddressesUpdate (CartDeliveryAddressesUpdatePayload)
* cartDiscountCodesUpdate (CartDiscountCodesUpdatePayload)
* cartGiftCardCodesAdd (CartGiftCardCodesAddPayload)
* cartGiftCardCodesRemove (CartGiftCardCodesRemovePayload)
* cartGiftCardCodesUpdate (CartGiftCardCodesUpdatePayload)
* cartLinesAdd (CartLinesAddPayload)
* cartLinesRemove (CartLinesRemovePayload)
* cartLinesUpdate (CartLinesUpdatePayload)
* cartNoteUpdate (CartNoteUpdatePayload)
* cartSelectedDeliveryOptionsUpdate (CartSelectedDeliveryOptionsUpdatePayload)

[Anchor to cartAttributesUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartAttributesUpdate)[cartAttributesUpdate](/docs/api/storefront/latest/mutations/cartAttributesUpdate) •mutation
:   Updates the attributes on a cart.

    Show payload

    ### Arguments

    [Anchor to attributes](/docs/api/storefront/latest/objects/Cart#mutation-cartAttributesUpdate.arguments.attributes)attributes •[[AttributeInput!]!](/docs/api/storefront/latest/input-objects/AttributeInput) required
    :   An array of key-value pairs that contains additional information about the cart.

        The input must not contain more than `250` values.

        Show input fields

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartAttributesUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    ---

[Anchor to cartBuyerIdentityUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartBuyerIdentityUpdate)[cartBuyerIdentityUpdate](/docs/api/storefront/latest/mutations/cartBuyerIdentityUpdate) •mutation
:   Updates customer information associated with a cart.
    Buyer identity is used to determine
    [international pricing](https://shopify.dev/custom-storefronts/internationalization/international-pricing)
    and should match the customer's shipping address.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartBuyerIdentityUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to buyerIdentity](/docs/api/storefront/latest/objects/Cart#mutation-cartBuyerIdentityUpdate.arguments.buyerIdentity)buyerIdentity •[CartBuyerIdentityInput!](/docs/api/storefront/latest/input-objects/CartBuyerIdentityInput) required
    :   The customer associated with the cart. Used to determine
        [international pricing](https://shopify.dev/custom-storefronts/internationalization/international-pricing).
        Buyer identity should match the customer's shipping address.

        Show input fields

    ---

[Anchor to cartCreate](/docs/api/storefront/latest/objects/Cart#mutation-cartCreate)[cartCreate](/docs/api/storefront/latest/mutations/cartCreate) •mutation
:   Creates a new cart.

    Show payload

    ### Arguments

    [Anchor to input](/docs/api/storefront/latest/objects/Cart#mutation-cartCreate.arguments.input)input •[CartInput](/docs/api/storefront/latest/input-objects/CartInput)
    :   The fields used to create a cart.

        Show input fields

    ---

[Anchor to cartDeliveryAddressesAdd](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesAdd)[cartDeliveryAddressesAdd](/docs/api/storefront/latest/mutations/cartDeliveryAddressesAdd) •mutation
:   Adds delivery addresses to the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesAdd.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to addresses](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesAdd.arguments.addresses)addresses •[[CartSelectableAddressInput!]!](/docs/api/storefront/latest/input-objects/CartSelectableAddressInput) required
    :   A list of delivery addresses to add to the cart.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to cartDeliveryAddressesRemove](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesRemove)[cartDeliveryAddressesRemove](/docs/api/storefront/latest/mutations/cartDeliveryAddressesRemove) •mutation
:   Removes delivery addresses from the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesRemove.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to addressIds](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesRemove.arguments.addressIds)addressIds •[[ID!]!](/docs/api/storefront/latest/scalars/ID) required
    :   A list of delivery addresses by handle to remove from the cart.

        The input must not contain more than `250` values.

    ---

[Anchor to cartDeliveryAddressesReplace](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesReplace)[cartDeliveryAddressesReplace](/docs/api/storefront/latest/mutations/cartDeliveryAddressesReplace) •mutation
:   Replaces delivery addresses on the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesReplace.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to addresses](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesReplace.arguments.addresses)addresses •[[CartSelectableAddressInput!]!](/docs/api/storefront/latest/input-objects/CartSelectableAddressInput) required
    :   A list of delivery addresses to replace on the cart.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to cartDeliveryAddressesUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesUpdate)[cartDeliveryAddressesUpdate](/docs/api/storefront/latest/mutations/cartDeliveryAddressesUpdate) •mutation
:   Updates one or more delivery addresses on a cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to addresses](/docs/api/storefront/latest/objects/Cart#mutation-cartDeliveryAddressesUpdate.arguments.addresses)addresses •[[CartSelectableAddressUpdateInput!]!](/docs/api/storefront/latest/input-objects/CartSelectableAddressUpdateInput) required
    :   The delivery addresses to update.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to cartDiscountCodesUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartDiscountCodesUpdate)[cartDiscountCodesUpdate](/docs/api/storefront/latest/mutations/cartDiscountCodesUpdate) •mutation
:   Updates the discount codes applied to the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartDiscountCodesUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to discountCodes](/docs/api/storefront/latest/objects/Cart#mutation-cartDiscountCodesUpdate.arguments.discountCodes)discountCodes •[[String!]!](/docs/api/storefront/latest/scalars/String) required
    :   The case-insensitive discount codes that the customer added at checkout.

        The input must not contain more than `250` values.

    ---

[Anchor to cartGiftCardCodesAdd](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesAdd)[cartGiftCardCodesAdd](/docs/api/storefront/latest/mutations/cartGiftCardCodesAdd) •mutation
:   Adds gift card codes to the cart without replacing existing ones.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesAdd.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to giftCardCodes](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesAdd.arguments.giftCardCodes)giftCardCodes •[[String!]!](/docs/api/storefront/latest/scalars/String) required
    :   The case-insensitive gift card codes to add.

        The input must not contain more than `250` values.

    ---

[Anchor to cartGiftCardCodesRemove](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesRemove)[cartGiftCardCodesRemove](/docs/api/storefront/latest/mutations/cartGiftCardCodesRemove) •mutation
:   Removes the gift card codes applied to the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesRemove.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to appliedGiftCardIds](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesRemove.arguments.appliedGiftCardIds)appliedGiftCardIds •[[ID!]!](/docs/api/storefront/latest/scalars/ID) required
    :   The gift cards to remove.

        The input must not contain more than `250` values.

    ---

[Anchor to cartGiftCardCodesUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesUpdate)[cartGiftCardCodesUpdate](/docs/api/storefront/latest/mutations/cartGiftCardCodesUpdate) •mutation
:   Updates the gift card codes applied to the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to giftCardCodes](/docs/api/storefront/latest/objects/Cart#mutation-cartGiftCardCodesUpdate.arguments.giftCardCodes)giftCardCodes •[[String!]!](/docs/api/storefront/latest/scalars/String) required
    :   The case-insensitive gift card codes.

        The input must not contain more than `250` values.

    ---

[Anchor to cartLinesAdd](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesAdd)[cartLinesAdd](/docs/api/storefront/latest/mutations/cartLinesAdd) •mutation
:   Adds a merchandise line to the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesAdd.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to lines](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesAdd.arguments.lines)lines •[[CartLineInput!]!](/docs/api/storefront/latest/input-objects/CartLineInput) required
    :   A list of merchandise lines to add to the cart.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to cartLinesRemove](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesRemove)[cartLinesRemove](/docs/api/storefront/latest/mutations/cartLinesRemove) •mutation
:   Removes one or more merchandise lines from the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesRemove.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to lineIds](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesRemove.arguments.lineIds)lineIds •[[ID!]!](/docs/api/storefront/latest/scalars/ID) required
    :   The merchandise line IDs to remove.

        The input must not contain more than `250` values.

    ---

[Anchor to cartLinesUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesUpdate)[cartLinesUpdate](/docs/api/storefront/latest/mutations/cartLinesUpdate) •mutation
:   Updates one or more merchandise lines on a cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to lines](/docs/api/storefront/latest/objects/Cart#mutation-cartLinesUpdate.arguments.lines)lines •[[CartLineUpdateInput!]!](/docs/api/storefront/latest/input-objects/CartLineUpdateInput) required
    :   The merchandise lines to update.

        The input must not contain more than `250` values.

        Show input fields

    ---

[Anchor to cartNoteUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartNoteUpdate)[cartNoteUpdate](/docs/api/storefront/latest/mutations/cartNoteUpdate) •mutation
:   Updates the note on the cart.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartNoteUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to note](/docs/api/storefront/latest/objects/Cart#mutation-cartNoteUpdate.arguments.note)note •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The note on the cart.

    ---

[Anchor to cartSelectedDeliveryOptionsUpdate](/docs/api/storefront/latest/objects/Cart#mutation-cartSelectedDeliveryOptionsUpdate)[cartSelectedDeliveryOptionsUpdate](/docs/api/storefront/latest/mutations/cartSelectedDeliveryOptionsUpdate) •mutation
:   Update the selected delivery options for a delivery group.

    Show payload

    ### Arguments

    [Anchor to cartId](/docs/api/storefront/latest/objects/Cart#mutation-cartSelectedDeliveryOptionsUpdate.arguments.cartId)cartId •[ID!](/docs/api/storefront/latest/scalars/ID) required
    :   The ID of the cart.

    [Anchor to selectedDeliveryOptions](/docs/api/storefront/latest/objects/Cart#mutation-cartSelectedDeliveryOptionsUpdate.arguments.selectedDeliveryOptions)selectedDeliveryOptions •[[CartSelectedDeliveryOptionInput!]!](/docs/api/storefront/latest/input-objects/CartSelectedDeliveryOptionInput) required
    :   The selected delivery options.

        The input must not contain more than `250` values.

        Show input fields

    ---

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/Cart#interfaces)Interfaces

* HasMetafields
* Node

[Anchor to HasMetafields](/docs/api/storefront/latest/objects/Cart#interface-HasMetafields)[HasMetafields](/docs/api/storefront/latest/interfaces/HasMetafields) •interface

[Anchor to Node](/docs/api/storefront/latest/objects/Cart#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo