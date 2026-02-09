---
source: https://shopify.dev/docs/apps/build/custom-data
---

Shopify includes built-in data models like products, customers, and orders. Metafields extend these models by letting you add custom data to any [Shopify resource](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).

You can use metafields to add warranty information to products, track customer lifetime value, store fulfillment notes on orders, link related products, trigger Shopify Flow automations, or power backend processes. This flexibility lets you extend Shopify's data model for specialized features and business logic.

Info

Metafields add individual custom fields to specific Shopify resources.

* Need to create standalone objects with multiple related fields? Use [metaobjects](/docs/apps/build/metaobjects) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

**Info:**

Metafields add individual custom fields to specific Shopify resources.

* Need to create standalone objects with multiple related fields? Use [metaobjects](/docs/apps/build/metaobjects) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

  

Want to skip ahead? Choose a path based on what you're building:

* **Building an app**: Use [app-owned metafields](#app-owned-metafields) with TOML configuration.
* **Extending existing store data**: Use [merchant-owned metafields](#merchant-owned-metafields) with GraphQL.

---

## [Anchor to What are metafields?](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#what-are-metafields)What are metafields?

Metafields are key-value pairs with the following components:

* **Identifier**: A combination of namespace and key (for example, `custom.warranty_info`). Namespaces are logical containers that not only provide organization and prevent naming conflicts, they establish [ownership](#metafield-ownership).
* **Value**: The data being stored.
* **Type**: Defines the kind of value (such as text, number, date, or reference) and how the value is interpreted. [See available types](/docs/apps/build/metafields/list-of-data-types).

### [Anchor to Metafield definitions](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#metafield-definitions)Metafield definitions

Before creating a metafield, you will create a metafield definition. Metafield definitions establish data schemas that enable type validation, Shopify admin integration, query filtering, access control, and performance optimization.

Note

Shopify provides pre-built "standard" definitions for common use cases like ISBN numbers, product ingredients, and care instructions. Using standard definitions helps ensure interoperability across the Shopify ecosystem and saves you from defining schemas for well-known data types. Explore [standard metafield definitions](/docs/apps/build/metafields/list-of-standard-definitions).

**Note:**

Shopify provides pre-built "standard" definitions for common use cases like ISBN numbers, product ingredients, and care instructions. Using standard definitions helps ensure interoperability across the Shopify ecosystem and saves you from defining schemas for well-known data types. Explore [standard metafield definitions](/docs/apps/build/metafields/list-of-standard-definitions).

### [Anchor to Metafield ownership](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#metafield-ownership)Metafield ownership

Ownership determines access and control. When creating metafields, you choose between two ownership models:

| **Ownership Type** | **Purpose** | **Namespace** |
| --- | --- | --- |
| App-owned | App-managed data for internal logic, configuration, and workflows | Use reserved namespace `$app` (GraphQL) or `app` (TOML) |
| Merchant-owned | Merchant-managed data shared across all apps | Use any non-reserved namespace, such as `custom` |

**Additional ownership types:**

* **Shopify-reserved**: Metafields with Shopify-controlled namespaces and structures, including those typically prefixed with reserved namespace `shopify--` and [standard definitions](/docs/apps/build/metafields/list-of-standard-definitions). Shopify controls the structure, but the metafields are typically [merchant-owned](#merchant-owned-metafields).
* **App-data**: A special type of app-owned metafield tied to your app installation (not to products, customers, or orders) and completely hidden from the Shopify admin. See [App-data metafields](#app-data-metafields) for details.

---

## [Anchor to App-owned metafields](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#app-owned-metafields)App-owned metafields

App-owned metafields are custom data entries controlled by your app. Your app manages both the structure and values, which are view only in the Shopify admin (by default).

App-ownership is defined using the `app` reserved namespace.

Info

App-owned data is viewable by default in the Shopify admin. If you need to store data that is not visible, consider [App-data metafields](#app-data-metafields).

**Info:**

App-owned data is viewable by default in the Shopify admin. If you need to store data that is not visible, consider [App-data metafields](#app-data-metafields).

### [Anchor to Example](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#example)Example

You want to track internal SKU codes for products. Because your app manages inventory tracking, you create an app-owned metafield.

#### [Anchor to Step 1: Create the metafield definition](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-1-create-the-metafield-definition)Step 1: Create the metafield definition

Create the metafield definition using your app's `shopify.app.toml` file. The following creates the definition with app-owned namespace `app` and key `internal_sku`:

9

1

2

3

4

[product.metafields.app.internal\_sku]

name = "Internal SKU"

description = "Internal inventory tracking code"

type = "single\_line\_text\_field"

Deploy it with your app:

9

1

shopify app deploy

#### [Anchor to Step 2: Create the metafield](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-2-create-the-metafield)Step 2: Create the metafield

After you create the metafield definition, add the metafield (value) using the GraphQL Admin API. Use the same namespace, key, and type from the definition:

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

mutation AddInternalSKU {

productUpdate(

input: {

id: "gid://shopify/Product/123456789"

metafields: [

{

namespace: "$app"

key: "internal\_sku"

value: "INV-2024-COTTON-001"

type: "single\_line\_text\_field"

}

]

}

) {

product {

id

metafield(namespace: "$app", key: "internal\_sku") {

id

value

}

}

userErrors {

field

message

}

}

}

Note

Get a product ID by querying `products(first: 1)` in GraphiQL, or find it in the Shopify admin URL when viewing a product: `/admin/products/123456789`.

**Note:**

Get a product ID by querying `products(first: 1)` in GraphiQL, or find it in the Shopify admin URL when viewing a product: `/admin/products/123456789`.

---

## [Anchor to Merchant-owned metafields](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#merchant-owned-metafields)Merchant-owned metafields

Merchant-owned metafields are custom data entries that merchants and all installed apps can modify. Both the structure and values are editable, making them ideal for shared data across multiple apps.

Create merchant-owned metafields using any [non-reserved namespace](#metafield-ownership) (such as `custom`, `specs`, or `inventory`).

Info

Merchant-owned definitions can't be created in `shopify.app.toml`.

**Info:**

Merchant-owned definitions can't be created in `shopify.app.toml`.

### [Anchor to Example](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#example)Example

You want to add warranty information to products. Because this type of field should be managed in the Shopify admin, you use a merchant-owned metafield.

#### [Anchor to Step 1: Create the metafield definition](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-1-create-the-metafield-definition)Step 1: Create the metafield definition

First, create the metafield definition using the GraphQL Admin API. The following example doesn't use namespace `$app`, so the definition will be merchant-owned:

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

mutation {

metafieldDefinitionCreate(definition: {

name: "Warranty Information",

namespace: "custom",

key: "warranty\_info",

description: "Product warranty details and coverage information",

type: "multi\_line\_text\_field",

ownerType: PRODUCT,

access: {

storefront: PUBLIC\_READ,

},

}) {

createdDefinition {

name

namespace

key

type

access

}

}

}

#### [Anchor to Step 2: Create the metafield](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-2-create-the-metafield)Step 2: Create the metafield

After you create the metafield definition, add the metafield (value). Use the same namespace, key, and type from the definition:

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

mutation AddWarrantyInfo {

productUpdate(

input: {

id: "gid://shopify/Product/123456789"

metafields: [

{

namespace: "custom"

key: "warranty\_info"

value: "2-year manufacturer warranty. Covers defects in materials and workmanship."

type: "multi\_line\_text\_field"

}

]

}

) {

product {

id

metafield(namespace: "custom", key: "warranty\_info") {

id

value

}

}

userErrors {

field

message

}

}

}

---

## [Anchor to App-data metafields](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#app-data-metafields)App-data metafields

App-data metafields are tied to a specific app installation and are completely hidden from the Shopify admin. They're stored on the `AppInstallation` resource and can only be accessed by the owning app via GraphQL or through the [`app` object in Liquid](/docs/api/liquid/objects/app). They can't be created using `shopify.app.toml`.

Unlike [app-owned metafields](#app-owned-metafields) on shared resources, the `$app` reserved namespace isn't required because the `AppInstallation` owner provides isolation — only your app can access its own installation's metafields.

Caution

Generally, private app data should be stored in an app-specific, secure database. App-data metafields can be used for per-installation configuration values, but sensitive credentials should be stored in environment variables or a dedicated secret management system.

**Caution:**

Generally, private app data should be stored in an app-specific, secure database. App-data metafields can be used for per-installation configuration values, but sensitive credentials should be stored in environment variables or a dedicated secret management system.

### [Anchor to Example](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#example)Example

You want to store a feature tier configuration for each app installation. Because this data should be completely hidden from merchants and specific to each installation, you use app-data metafields.

#### [Anchor to Step 1: Retrieve the app installation ID](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-1-retrieve-the-app-installation-id)Step 1: Retrieve the app installation ID

Get the app installation ID using the [`currentAppInstallation`](/docs/api/admin-graphql/latest/queries/currentAppInstallation) query:

9

1

2

3

4

5

query {

currentAppInstallation {

id

}

}

9

1

2

3

4

5

6

7

{

"data": {

"currentAppInstallation": {

"id": "gid://shopify/AppInstallation/123456"

}

}

}

#### [Anchor to Step 2: Create the app-data metafield](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#step-2-create-the-app-data-metafield)Step 2: Create the app-data metafield

Create the app-data metafield using the [`metafieldsSet`](/docs/api/admin-graphql/current/mutations/metafieldsSet) mutation:

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

mutation CreateAppDataMetafield($metafieldsSetInput: [MetafieldsSetInput!]!) {

metafieldsSet(metafields: $metafieldsSetInput) {

metafields {

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

{

"metafieldsSetInput": [

{

"namespace": "app\_config",

"key": "feature\_tier",

"type": "single\_line\_text\_field",

"value": "premium",

"ownerId": "gid://shopify/AppInstallation/123456"

}

]

}

---

## [Anchor to Permissions](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#permissions)Permissions

Configure who can read and write your metafields using the `access` settings on your definition.

### [Anchor to Shopify admin permissions](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#shopify-admin-permissions)Shopify admin permissions

`admin` controls permissions for both the Shopify admin and the GraphQL Admin API.

**For app-owned metafields:**

9

1

2

3

4

5

# Merchants can view but not edit (default)

access.admin = "merchant\_read"

# Merchants can view and edit

access.admin = "merchant\_read\_write"

9

1

2

3

4

5

6

7

access: {

admin: MERCHANT\_READ # view only (default)

}

access: {

admin: MERCHANT\_READ\_WRITE # view and edit

}

##### TOML

```liquid
# Merchants can view but not edit (default)
access.admin = "merchant_read"

# Merchants can view and edit
access.admin = "merchant_read_write"
```

##### GraphQL

```liquid
access: {
  admin: MERCHANT_READ  # view only (default)
}

access: {
  admin: MERCHANT_READ_WRITE  # view and edit
}
```

**For merchant-owned metafields:**

* Always full access - readable and writable by merchants and all apps with appropriate scopes. No configuration needed.

### [Anchor to Storefront permissions](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#storefront-permissions)Storefront permissions

`storefront` controls permissions for the Storefront API (used by headless and custom storefronts). This setting doesn't affect Liquid templates - metafields are always accessible in Liquid regardless of this setting.

**Available settings:**

9

1

2

3

4

5

# Hidden from Storefront API (default)

access.storefront = "none"

# Accessible in Storefront API

access.storefront = "public\_read"

9

1

2

3

4

5

6

7

access: {

storefront: NONE # hidden (default)

}

access: {

storefront: PUBLIC\_READ # accessible

}

##### TOML

```liquid
# Hidden from Storefront API (default)
access.storefront = "none"

# Accessible in Storefront API
access.storefront = "public_read"
```

##### GraphQL

```liquid
access: {
  storefront: NONE  # hidden (default)
}

access: {
  storefront: PUBLIC_READ  # accessible
}
```

Note

Metafield access depends on its owning resource.

**Note:**

Metafield access depends on its owning resource.

### [Anchor to Customer accounts permissions](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#customer-accounts-permissions)Customer accounts permissions

`customer_accounts` controls permissions for the Customer Accounts API.

**Available settings:**

9

1

2

3

4

5

6

7

8

# Hidden from Customer Accounts API (default)

access.customer\_account = "none"

# Readable in Customer Accounts API

access.customer\_account = "read"

# Readable and writable in Customer Accounts API

access.customer\_account = "read\_write"

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

access: {

customerAccount: NONE # hidden (default)

}

access: {

customerAccount: READ # readable

}

access: {

customerAccount: READ\_WRITE # readable and writable

}

##### TOML

```liquid
# Hidden from Customer Accounts API (default)
access.customer_account = "none"

# Readable in Customer Accounts API
access.customer_account = "read"

# Readable and writable in Customer Accounts API
access.customer_account = "read_write"
```

##### GraphQL

```liquid
access: {
  customerAccount: NONE  # hidden (default)
}

access: {
  customerAccount: READ  # readable
}

access: {
  customerAccount: READ_WRITE  # readable and writable
}
```

Note

Customer Account API access levels can only be adjusted via GraphQL Admin API mutation for app-owned metafields (namespace `app--`). For merchant-owned metafields, Customer Account API access can only be configured through the Shopify admin.

**Note:**

Customer Account API access levels can only be adjusted via GraphQL Admin API mutation for app-owned metafields (namespace `app--`). For merchant-owned metafields, Customer Account API access can only be configured through the Shopify admin.

---

## [Anchor to Next steps](/docs/apps/build/metafields?utm_campaign=social_care&utm_medium=community&utm_source=social#next-steps)Next steps

* Learn how to [model your data structure](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).
* Learn how to [work with metafield definitions](/docs/apps/build/metafields/definitions).
* Learn how to [work with metafield values](/docs/apps/build/metafields/manage-metafields).
* Learn how to use metafields to [query resources](/docs/apps/build/metafields/query-using-metafields).
* Learn how to [enable filtering and other advanced features](/docs/apps/build/metafields/use-metafield-capabilities).

---

Was this page helpful?

YesNo