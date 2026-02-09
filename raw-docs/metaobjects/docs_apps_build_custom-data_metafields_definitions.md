---
source: https://shopify.dev/docs/apps/build/custom-data/metafields/definitions
---

Metafield definitions are schemas that specify the structure, type, and rules for metafields. Without definitions, metafields are untyped strings that can't be edited in the Shopify admin or validated.

This guide shows you how to create, read, update, and delete metafield definitions using TOML configuration or the GraphQL Admin API.

Note

Not sure how to structure your data? See [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects) for a translation guide from SQL concepts to Shopify's architecture.

**Note:**

Not sure how to structure your data? See [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects) for a translation guide from SQL concepts to Shopify's architecture.

---

## [Anchor to Requirements](/docs/apps/build/metafields/definitions#requirements)Requirements

* Your app can make [authenticated requests](/docs/api/usage/authentication) to the GraphQL Admin API.
* Your app has the appropriate access scopes for the [owner type](/docs/api/admin-graphql/latest/enums/MetafieldOwnerType) that you want to associate with the metafield definition. For example, `write_products` for product metafields, or `write_customers` for customer metafields.

---

## [Anchor to Creating definitions](/docs/apps/build/metafields/definitions#creating-definitions)Creating definitions

There are two ways to create metafield definitions:

* **TOML**: TOML configurations in `shopify.app.toml` create app-owned definitions. Your app maintains control over the schema while optionally allowing metafield (value) edits in the Shopify admin.
* **GraphQL**: The GraphQL Admin API provides programmatic control for creating merchant-owned definitions (editable in the Shopify admin by merchants and all installed apps) and dynamically generating definitions based on user configuration.

Tip

Creating merchant-owned metafields for common use cases (like ISBN or ingredients)? Use Shopify's pre-defined [standard definitions](#standard-definitions) instead.

**Tip:**

Creating merchant-owned metafields for common use cases (like ISBN or ingredients)? Use Shopify's pre-defined [standard definitions](#standard-definitions) instead.

### [Anchor to TOML (app-owned) example](/docs/apps/build/metafields/definitions#toml-app-owned-example)TOML (app-owned) example

This example creates an app-owned definition that tracks when products were last synchronized. The definition grants merchants write access to metafield values through `access.admin = "merchant_read_write"`, while the definition schema remains app-controlled.

9

1

2

3

4

5

[product.metafields.app.last\_synced]

name = "Last Synced"

description = "When this product was last synchronized with external system"

type = "date\_time"

access.admin = "merchant\_read\_write"

Once you've updated the file, deploy the changes with your app:

9

1

shopify app deploy

**Benefits of TOML:**

* Definitions are version-controlled as part of your app.
* Automatic creation and updates on deploy.
* Works with `shopify app dev` to safely test out changes.
* Consistent across all shops - when you update your app's data structure, it deploys to every installation automatically.
* The app maintains ownership.

### [Anchor to GraphQL Admin API example](/docs/apps/build/metafields/definitions#graphql-admin-api-example)GraphQL Admin API example

These examples show how to create metafield definitions using GraphQL. The first creates a merchant-owned definition that all apps can access. The second creates an app-owned definition that only your app controls.

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

# POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

# Headers: X-Shopify-Access-Token: {merchant\_token}

mutation CreateMerchantOwnedDefinition {

metafieldDefinitionCreate(

definition: {

namespace: "product\_details"

key: "warranty\_info"

name: "Warranty Information"

description: "Product warranty details and coverage"

type: "multi\_line\_text\_field"

ownerType: PRODUCT

access: {

storefront: PUBLIC\_READ

}

}

) {

createdDefinition {

id

namespace

key

}

userErrors {

field

message

}

}

}

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

# POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

# Headers: X-Shopify-Access-Token: {app\_token}

mutation CreateAppOwnedDefinition {

metafieldDefinitionCreate(

definition: {

namespace: "$app" # app-reserved namespace

key: "warranty\_info"

name: "Warranty Information"

description: "Product warranty details and coverage"

type: "multi\_line\_text\_field"

ownerType: PRODUCT

access: {

admin: MERCHANT\_READ\_WRITE

storefront: PUBLIC\_READ

}

}

) {

createdDefinition {

id

namespace

key

}

userErrors {

field

message

}

}

}

##### Merchant-owned (editable in Shopify admin)

```liquid
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json
# Headers: X-Shopify-Access-Token: {merchant_token}

mutation CreateMerchantOwnedDefinition {
  metafieldDefinitionCreate(
    definition: {
      namespace: "product_details"
      key: "warranty_info"
      name: "Warranty Information"
      description: "Product warranty details and coverage"
      type: "multi_line_text_field"
      ownerType: PRODUCT
      access: {
        storefront: PUBLIC_READ
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

##### App-owned (app controlled)

```liquid
# POST https://{shop}.myshopify.com/api/{api_version}/graphql.json
# Headers: X-Shopify-Access-Token: {app_token}

mutation CreateAppOwnedDefinition {
  metafieldDefinitionCreate(
    definition: {
      namespace: "$app" # app-reserved namespace
      key: "warranty_info"
      name: "Warranty Information"
      description: "Product warranty details and coverage"
      type: "multi_line_text_field"
      ownerType: PRODUCT
      access: {
        admin: MERCHANT_READ_WRITE
        storefront: PUBLIC_READ
      }
    }
  ) {
    createdDefinition {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

Key differences:

* **Merchant-owned**: Use any non-reserved namespace (like `product_details`). This provides full control in the Shopify admin—no `access.admin` needed. Only `access.storefront` is used to control customer visibility.
* **App-owned**: Use the reserved `$app` namespace. The app controls the definition. Use `access.admin` to grant merchant write permissions.

### [Anchor to When to use GraphQL vs TOML](/docs/apps/build/metafields/definitions#when-to-use-graphql-vs-toml)When to use GraphQL vs TOML

**Use TOML when:**

* Your app needs fixed, known fields (for example, tracking numbers, warranty dates).
* The structure is consistent across all installations.
* Fields are core to your app's functionality.
* You want a version-controlled, declarative configuration.

**Use GraphQL when:**

* Merchants define their own custom fields through your app's UI.
* Field structure varies per merchant or changes frequently.
* Building form builders, CMS-like tools, or field managers.
* You're creating merchant-owned fields that other apps can access.

### [Anchor to Dynamic definition creation example](/docs/apps/build/metafields/definitions#dynamic-definition-creation-example)Dynamic definition creation example

This example shows how to programmatically create definitions based on user input, such as in a field manager app where custom fields are configured through your app's UI.

Your app would collect field configuration (via a form or UI), validate the input, construct the variables object, and then execute the mutation. This enables the creation of custom fields through your app's interface without editing code or configuration files.

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

mutation CreateDynamicField($input: MetafieldDefinitionInput!) {

metafieldDefinitionCreate(definition: $input) {

createdDefinition {

id

name

namespace

key

type { name }

}

userErrors {

field

message

code

}

}

}

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

{

"input": {

"name": "Return Policy",

"namespace": "custom",

"key": "return\_policy",

"description": "Store's return policy for this product",

"type": "multi\_line\_text\_field",

"ownerType": "PRODUCT",

"validations": [

{

"name": "max\_length",

"value": "1000"

}

],

"access": {

"storefront": "PUBLIC\_READ"

}

}

}

---

## [Anchor to Reading definitions](/docs/apps/build/metafields/definitions#reading-definitions)Reading definitions

Use GraphQL to find existing definitions and check their capabilities.

Query all definitions by resource type:

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

query {

metafieldDefinitions(first: 100, ownerType: PRODUCT) {

edges {

node {

id

namespace

key

name

type { name }

access { admin storefront }

}

}

}

}

Search definitions by name or namespace:

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

query {

metafieldDefinitions(

first: 20

ownerType: PRODUCT

query: "warranty"

) {

edges {

node {

id

name

namespace

key

type { name }

}

}

}

}

Find a specific definition by namespace and key:

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

query {

metafieldDefinitions(

first: 1

ownerType: PRODUCT

namespace: "product\_details"

key: "warranty\_info"

) {

edges {

node {

id

name

namespace

key

type { name }

access { admin storefront }

}

}

}

}

Tip

Query the [`metafieldDefinitionTypes`](/docs/api/admin-graphql/latest/queries/metafieldDefinitionTypes) field to see which validations each type supports, or check the [`supportedValidations`](/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-supportedvalidations) field when querying existing definitions.

**Tip:**

Query the [`metafieldDefinitionTypes`](/docs/api/admin-graphql/latest/queries/metafieldDefinitionTypes) field to see which validations each type supports, or check the [`supportedValidations`](/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-supportedvalidations) field when querying existing definitions.

---

## [Anchor to Updating definitions](/docs/apps/build/metafields/definitions#updating-definitions)Updating definitions

Only specific fields can be updated after creation:

| Field | Can update | Method |
| --- | --- | --- |
| Name and description | Yes | TOML or GraphQL |
| Validations | Yes (with limits) | TOML or GraphQL |
| Access permissions | Yes | TOML or GraphQL |
| Type | No | Can't change |
| Namespace/key | No | Immutable |
| Owner type | No | Can't migrate |

The following example shows how to update a definition's name, description, and access permissions using the [`metafieldDefinitionUpdate`](/docs/api/admin-graphql/latest/mutations/metafieldDefinitionUpdate) mutation:

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

mutation {

metafieldDefinitionUpdate(

definition: {

id: "gid://shopify/MetafieldDefinition/1234567890"

name: "Updated Name"

description: "Updated description"

access: { storefront: PUBLIC\_READ }

}

) {

updatedDefinition { id name }

userErrors { field message }

}

}

Caution

Tightening validations may fail if existing metafields violate the new constraint.

**Caution:**

Tightening validations may fail if existing metafields violate the new constraint.

To change a namespace/key:

1. Create a new definition with the desired namespace/key.
2. Copy the existing metafield values to the new namespace/key.
3. Update your app code, extensions, and integrations to reference the new namespace/key.
4. Test thoroughly with both definitions active to ensure everything works.
5. Delete the old definition once migration is complete.

This approach enables safe, zero-downtime migration by allowing you to test with both the old and new metafields active before removing the old one.

---

## [Anchor to Deleting definitions](/docs/apps/build/metafields/definitions#deleting-definitions)Deleting definitions

For TOML definitions:

1. Remove the definition from your `shopify.app.toml` file.
2. Deploy the change:

9

1

shopify app deploy

For GraphQL definitions, use the [`metafieldDefinitionDelete`](/docs/api/admin-graphql/latest/mutations/metafieldDefinitionDelete) mutation:

9

1

2

3

4

5

6

7

8

9

mutation {

metafieldDefinitionDelete(

id: "gid://shopify/MetafieldDefinition/1234567890"

deleteAllAssociatedMetafields: true

) {

deletedDefinitionId

userErrors { field message }

}

}

Set `deleteAllAssociatedMetafields` to `true` to delete all metafield values along with the definition, or `false` to only delete the definition while preserving existing values.

---

## [Anchor to Access control](/docs/apps/build/metafields/definitions#access-control)Access control

Control who can read and write metafield values using settings on your definition. For comprehensive details, see [Permissions](/docs/apps/build/metafields#permissions).

**For app-owned metafields (using the `app` namespace):**

* Merchants can always read all metafields and definitions in their store.
* Only the app can make changes to the definition.
* Use `access.admin = "merchant_read_write"` to allow value edits in the Shopify admin.

**For merchant-owned metafields:**

* Merchants always have full control of both the definition and the values.
* The `access.storefront` setting controls customer visibility.

---

## [Anchor to Standard definitions](/docs/apps/build/metafields/definitions#standard-definitions)Standard definitions

Shopify provides pre-defined standard metafield definitions for common use cases like product descriptions, ISBN numbers, and care instructions. These definitions use reserved namespace/key combinations (such as `descriptors.subtitle` or `facts.isbn`) that ensure interoperability across themes, apps, and the Shopify ecosystem.

Standard definitions are Shopify-owned with predefined access controls that vary by definition. Values are readable and writable across apps and in the Shopify admin.

Query available standard definitions using the [`standardMetafieldDefinitionTemplates`](/docs/api/admin-graphql/latest/queries/standardMetafieldDefinitionTemplates) query:

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

query {

standardMetafieldDefinitionTemplates(first: 50) {

edges {

node {

id

name

namespace

key

type { name }

ownerTypes

}

}

}

}

Enable standard definitions using TOML configuration or the [`standardMetafieldDefinitionEnable`](/docs/api/admin-graphql/latest/mutations/standardMetafieldDefinitionEnable) mutation. This example enables the subtitle and ISBN standard definitions for products:

9

1

2

3

4

5

[product.metafields]

standard\_metafields = ["descriptors.subtitle", "facts.isbn"]

[product\_variant.metafields]

standard\_metafields = ["descriptors.subtitle"]

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

# Enable subtitle standard metafield on product

mutation {

standardMetafieldDefinitionEnable(

id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",

ownerType: PRODUCT

) {

createdDefinition {

name

key

namespace

description

}

}

}

# Enable ISBN standard metafield on product

mutation {

standardMetafieldDefinitionEnable(

id: "gid://shopify/StandardMetafieldDefinitionTemplate/3",

ownerType: PRODUCT

) {

createdDefinition {

name

key

namespace

description

}

}

}

# Enable subtitle standard metafield on product variant

mutation {

standardMetafieldDefinitionEnable(

id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",

ownerType: PRODUCTVARIANT

) {

createdDefinition {

name

key

namespace

description

}

}

}

##### TOML

```liquid
[product.metafields]
standard_metafields = ["descriptors.subtitle", "facts.isbn"]

[product_variant.metafields]
standard_metafields = ["descriptors.subtitle"]
```

##### GraphQL

```liquid
# Enable subtitle standard metafield on product
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",
    ownerType: PRODUCT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}

# Enable ISBN standard metafield on product
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/3",
    ownerType: PRODUCT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}

# Enable subtitle standard metafield on product variant
mutation {
  standardMetafieldDefinitionEnable(
    id: "gid://shopify/StandardMetafieldDefinitionTemplate/1",
    ownerType: PRODUCTVARIANT
  ) {
    createdDefinition {
      name
      key
      namespace
      description
    }
  }
}
```

Note

Standard definitions auto-enable when your app [creates metafield values](/docs/apps/build/metafields/manage-metafields#using-standard-definitions) for them. Manually enable them to make the definition available in the Shopify admin for populating values.

**Note:**

Standard definitions auto-enable when your app [creates metafield values](/docs/apps/build/metafields/manage-metafields#using-standard-definitions) for them. Manually enable them to make the definition available in the Shopify admin for populating values.

For more about standard definitions, see the [standard definitions list](/docs/apps/build/metafields/list-of-standard-definitions).

---

## [Anchor to Error handling](/docs/apps/build/metafields/definitions#error-handling)Error handling

Understanding common errors helps you implement proper error handling and provide better user experiences. Most errors occur during definition creation or updates when validations, permissions, or naming conflicts arise.

| Error | Cause | Solution |
| --- | --- | --- |
| `TAKEN` | Namespace/key is already in use | Query existing definitions first or use a different namespace/key |
| "Type <invalid\_type> is not a valid type" | Invalid type name | Check [available types](/docs/apps/build/metafields/list-of-data-types) |
| "Validation <validation\_name> is not supported for type <type\_name>" | Wrong validation for type | Query [`supportedValidations`](/docs/api/admin-graphql/latest/objects/MetafieldDefinition#field-supportedvalidations) or check [validations guide](/docs/apps/build/metafields/list-of-validation-options) |
| "App does not have permission to modify this definition" | Not app-owned | Only app-owned definitions can be modified by apps |

---

## [Anchor to Best practices](/docs/apps/build/metafields/definitions#best-practices)Best practices

Following these practices helps ensure maintainable, scalable metafield implementations that work well across development, staging, and production environments. Good naming and planning prevent migration headaches and help make your metafields easier for teams to understand and use.

* Use descriptive namespaces: `shipping_settings` rather than `custom`.
* Organize with sub-namespaces: For app-owned metafields, use sub-namespaces to group related fields. In TOML, `[product.metafields.analytics.lifetime_value]` creates namespace `app--{id}--analytics`. In GraphQL, use `namespace: "$app:analytics"`.
* Add validations gradually: Start loose, tighten as needed.
* Test in development first: Verify before production.
* Document for your team: Maintain a schema reference.
* Cache definition IDs: Avoid repeated queries.
* Batch related operations: Create multiple definitions together.

---

## [Anchor to TOML reference](/docs/apps/build/metafields/definitions#toml-reference)TOML reference

Metafields are declared in `shopify.app.toml` using the format `[<owner_type>.metafields.app.<key>]`. For example, `[product.metafields.app.page_count]` declares a product metafield with namespace `$app` and key `page_count`.

Metafields can be defined on many different resource types. For a full list, see [MetafieldOwnerType](/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).

| Property | Description |
| --- | --- |
| `type` | Data type for the metafield. See [metafield data types](/docs/apps/build/metafields/list-of-data-types). |
| `name` | Human-readable name displayed in the Shopify admin. |
| `description` | Descriptive text that explains the purpose of the metafield. |
| `access.admin` | Admin UI access control: `merchant_read` or `merchant_read_write`. |
| `access.storefront` | Storefront access control: `public_read` or `none`. |
| `access.customer_account` | Customer API access control: `read`, `read_write`, or `none`. |
| `capabilities.admin_filterable` | When `true`, enables filtering by this metafield in the Shopify admin UI and Admin API. |
| `capabilities.unique_values` | When `true`, enforces uniqueness on metafield values. |
| `capabilities.cart_to_order_copyable` | When `true`, automatically copies the cart metafield value to the corresponding order metafield when an order is created. Only available for order metafield definitions. |
| `validations` | Rules to validate field values (for example, min/max values, regex patterns). See [validation options](/docs/apps/build/metafields/list-of-validation-options). |

---

## [Anchor to TOML limitations](/docs/apps/build/metafields/definitions#toml-limitations)TOML limitations

When using TOML-based declarative definitions, be aware of these constraints:

### [Anchor to App-reserved namespace](/docs/apps/build/metafields/definitions#app-reserved-namespace)App-reserved namespace

You can only declare metafield definitions in the app-reserved namespace (`$app`) to ensure that only the owning app can make changes to definitions. This constraint allows Shopify to guarantee a consistent state between all shops your app is installed on.

### [Anchor to App-scoped limits](/docs/apps/build/metafields/definitions#app-scoped-limits)App-scoped limits

| Limit | Value |
| --- | --- |
| Metafield definitions per owner type | 128 |
| Changes per deploy | 25 |

To ensure Shopify can quickly and reliably distribute definitions across shops, you can't make more than 25 metafield changes (creation, update, or deletion) in a single deploy. If you need to make more than 25 changes, do so over multiple deploys.

### [Anchor to Read-only through Admin API](/docs/apps/build/metafields/definitions#read-only-through-admin-api)Read-only through Admin API

Declarative definitions are read-only through the Admin API, and can only be updated or deleted through the TOML configuration file. You can query declarative definitions through the Admin API, but mutations will return an error.

### [Anchor to Capability support](/docs/apps/build/metafields/definitions#capability-support)Capability support

| Capability | Supported in TOML |
| --- | --- |
| [Smart collections](/docs/apps/build/metafields/use-metafield-capabilities#smart-collection) | ❌ |
| [Admin filterable](/docs/apps/build/metafields/use-metafield-capabilities#admin-filterable) | ✅ |
| [Unique values](/docs/apps/build/metafields/use-metafield-capabilities#unique-values) | ✅ |
| [Cart to order copyable](/docs/apps/build/metafields/use-metafield-capabilities#cart-to-order-copyable) | ✅ |
| [Pinning](https://help.shopify.com/en/manual/custom-data/metafields/pinning-metafield-definitions) | ❌ |

---

## [Anchor to Next steps](/docs/apps/build/metafields/definitions#next-steps)Next steps

* Learn how to [work with metafield values](/docs/apps/build/metafields/manage-metafields).
* Learn about [validation options](/docs/apps/build/metafields/list-of-validation-options).
* Learn how to [enable filtering and other advanced features](/docs/apps/build/metafields/use-metafield-capabilities).

---

Was this page helpful?

YesNo