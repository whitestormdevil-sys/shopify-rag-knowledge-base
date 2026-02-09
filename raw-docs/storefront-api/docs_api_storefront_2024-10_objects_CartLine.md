---
source: https://shopify.dev/docs/api/storefront/2024-10/objects/CartLine
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Represents information about the merchandise in the cart.

## [Anchor to Fields](/docs/api/storefront/latest/objects/CartLine#fields)Fields

* attribute (Attribute)
* attributes ([Attribute!]!)
* cost (CartLineCost!)
* discountAllocations ([CartDiscountAllocation!]!)
* id (ID!)
* instructions (CartLineInstructions!)
* merchandise (Merchandise!)
* parentRelationship (CartLineParentRelationship)
* quantity (Int!)
* sellingPlanAllocation (SellingPlanAllocation)
* estimatedCost (CartLineEstimatedCost!): deprecated

[Anchor to attribute](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.attribute)attribute •[Attribute](/docs/api/storefront/latest/objects/Attribute)
:   An attribute associated with the cart line.

    Show fields

    ### Arguments

    [Anchor to key](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.attribute.arguments.key)key •[String!](/docs/api/storefront/latest/scalars/String) required
    :   The key of the attribute.

    ---

[Anchor to attributes](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.attributes)attributes •[[Attribute!]!](/docs/api/storefront/latest/objects/Attribute) non-null
:   The attributes associated with the cart line. Attributes are represented as key-value pairs.

    Show fields

[Anchor to cost](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.cost)cost •[CartLineCost!](/docs/api/storefront/latest/objects/CartLineCost) non-null
:   The cost of the merchandise that the buyer will pay for at checkout. The costs are subject to change and changes will be reflected at checkout.

    Show fields

[Anchor to discountAllocations](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.discountAllocations)discountAllocations •[[CartDiscountAllocation!]!](/docs/api/storefront/latest/interfaces/CartDiscountAllocation) non-null
:   The discounts that have been applied to the cart line.

    Show fields

[Anchor to id](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.id)id •[ID!](/docs/api/storefront/latest/scalars/ID) non-null
:   A globally-unique ID.

[Anchor to instructions](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.instructions)instructions •[CartLineInstructions!](/docs/api/storefront/latest/objects/CartLineInstructions) non-null
:   The instructions for the line item.

    Show fields

[Anchor to merchandise](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.merchandise)merchandise •[Merchandise!](/docs/api/storefront/latest/unions/Merchandise) non-null
:   The merchandise that the buyer intends to purchase.

    Show union types

[Anchor to parentRelationship](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.parentRelationship)parentRelationship •[CartLineParentRelationship](/docs/api/storefront/latest/objects/CartLineParentRelationship)
:   The parent of the line item.

    Show fields

[Anchor to quantity](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.quantity)quantity •[Int!](/docs/api/storefront/latest/scalars/Int) non-null
:   The quantity of the merchandise that the customer intends to purchase.

[Anchor to sellingPlanAllocation](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.sellingPlanAllocation)sellingPlanAllocation •[SellingPlanAllocation](/docs/api/storefront/latest/objects/SellingPlanAllocation)
:   The selling plan associated with the cart line and the effect that each selling plan has on variants when they're purchased.

    Show fields

[Anchor to estimatedCost](/docs/api/storefront/latest/objects/CartLine#field-CartLine.fields.estimatedCost)estimatedCost •[CartLineEstimatedCost!](/docs/api/storefront/latest/objects/CartLineEstimatedCost) non-nullDeprecated
:   Show fields

---

Was this section helpful?

YesNo

---

## [Anchor to Interfaces](/docs/api/storefront/latest/objects/CartLine#interfaces)Interfaces

* BaseCartLine
* Node

[Anchor to BaseCartLine](/docs/api/storefront/latest/objects/CartLine#interface-BaseCartLine)[BaseCartLine](/docs/api/storefront/latest/interfaces/BaseCartLine) •interface

[Anchor to Node](/docs/api/storefront/latest/objects/CartLine#interface-Node)[Node](/docs/api/storefront/latest/interfaces/Node) •interface

---

Was this section helpful?

YesNo