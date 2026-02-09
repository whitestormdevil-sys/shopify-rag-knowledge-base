---
source: https://shopify.dev/docs/apps/build/custom-data/metaobjects
---

Metaobjects enable you to define custom data structures with multiple related fields. While metafields add individual custom fields to existing Shopify resources, metaobjects let you create entirely new types of structured data that can be referenced and reused across your store.

You can use metaobjects to, for example, create product size charts with multiple measurements, author profiles with biographical information and contact details, ingredient lists with nutritional data, or warranty information with terms and conditions. This flexibility allows you to model complex data relationships and create rich content structures.

Info

Metaobjects create complex data structures with multiple related fields.

* Need to add a single custom field to an existing Shopify resource? Use [metafields](/docs/apps/build/metafields) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

**Info:**

Metaobjects create complex data structures with multiple related fields.

* Need to add a single custom field to an existing Shopify resource? Use [metafields](/docs/apps/build/metafields) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).

  

Want to skip ahead? Choose a path based on what you're building:

* **Building an app**: Use [app-owned metaobjects](#app-owned-metaobjects) with TOML configuration.
* **Extending store content**: Use [merchant-owned metaobjects](#merchant-owned-metaobjects) with GraphQL.

---

## [Anchor to What is a metaobject?](/docs/apps/build/metaobjects#what-is-a-metaobject)What is a metaobject?

A metaobject is an instance of structured data with multiple related field values. Unlike [metafields](/docs/apps/build/metafields) that attach single values to existing resources, metaobjects are standalone entities that can be referenced from multiple resources.

Each metaobject contains:

* **ID**: Unique identifier assigned by Shopify.
* **Handle**: URL-friendly identifier (auto-generated from display name, or custom).
* **Display name**: Human-readable name (auto-generated from a specified field).
* **Field values**: Data defined by its metaobject definition.
* **Capability states**: Optional states like published/unpublished (if enabled).

For example, an author metaobject might include a name, biography, email, and profile photo - all stored together as a single reusable entity.

### [Anchor to Metaobject definitions](/docs/apps/build/metaobjects#metaobject-definitions)Metaobject definitions

Before creating metaobjects, you create a metaobject definition. Metaobject definitions are schemas that specify the structure, fields, and rules for a metaobject type.

A definition establishes:

* **Type identifier**: The category name for your custom object (for example, `$app:author` or `size_chart`). This identifies what kind of metaobject entries you'll create.
* **Fields**: What data the metaobject stores (name, key, data type, validation rules).
* **Access permissions**: Who can edit and where entries can be accessed (Shopify admin, storefront).
* **Capabilities**: Optional features like publishable or renderable.
* **Display configuration**: How entries appear (field order, display name field).

The relationship is: one definition can have many metaobject instances (entries). For example, one "author" definition can have metaobjects for Jane Smith, John Doe, and other individual authors.

### [Anchor to Metaobject ownership](/docs/apps/build/metaobjects#metaobject-ownership)Metaobject ownership

Ownership determines access and control. When creating metaobjects, you choose between two ownership models:

| **Ownership Type** | **Purpose** | **Type prefix** |
| --- | --- | --- |
| App-owned | App-managed entries for features, configurations, and content | Use reserved prefix `$app` (GraphQL) or `app` (TOML) |
| Merchant-owned | Merchant-managed content shared across all apps | Use any non-reserved prefix, such as `custom` |

**Additional ownership types:**

* **Shopify-reserved**: Standard metaobject definitions for platform features. Shopify controls the structure, but merchants typically own and manage the entries. Developers don't create these but can enable [standard definitions](/docs/apps/build/metaobjects/list-of-standard-definitions) for certain use cases like product reviews.

---

## [Anchor to App-owned metaobjects](/docs/apps/build/metaobjects#app-owned-metaobjects)App-owned metaobjects

App-owned metaobjects are custom data structures that are managed by your app. These metaobject entries are used for features requiring multiple related fields, such as configuration panels, content templates, or complex product attributes.

App-ownership is defined using the `app` reserved type prefix and can be created using your app's `shopify.app.toml` file.

Info

App-owned metaobject entries are viewable by default in the Shopify admin. Edit access can be configured using the [`access.admin`](#shopify-admin-permissions) setting.

**Info:**

App-owned metaobject entries are viewable by default in the Shopify admin. Edit access can be configured using the [`access.admin`](#shopify-admin-permissions) setting.

### [Anchor to Example](/docs/apps/build/metaobjects#example)Example

You want to create author profiles with biographical information that can be referenced from blog posts. Because you want your app to own and control the structure, you create an app-owned metaobject.

#### [Anchor to Step 1: Create a metaobject definition](/docs/apps/build/metaobjects#step-1-create-a-metaobject-definition)Step 1: Create a metaobject definition

Create the metaobject definition using your app's `shopify.app.toml` file. The following creates the definition with app-owned prefix `app` and type identifier `author`:

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

[metaobjects.app.author]

name = "Author"

access.admin = "merchant\_read\_write"

access.storefront = "public\_read"

[metaobjects.app.author.fields.full\_name]

name = "Full Name"

type = "single\_line\_text\_field"

[metaobjects.app.author.fields.bio]

name = "Biography"

type = "multi\_line\_text\_field"

[metaobjects.app.author.fields.email]

name = "Email"

type = "single\_line\_text\_field"

[metaobjects.app.author.fields.photo]

name = "Profile Photo"

type = "file\_reference"

Deploy it with your app:

9

1

shopify app deploy

#### [Anchor to Step 2: Create the metaobjects](/docs/apps/build/metaobjects#step-2-create-the-metaobjects)Step 2: Create the metaobjects

After you create the metaobject definition, create metaobjects (entries) using the GraphQL Admin API. Use the same type identifier and field keys as your definition:

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

mutation CreateAuthor {

metaobjectCreate(metaobject: {

type: "$app:author"

fields: [

{ key: "full\_name", value: "Jane Smith" }

{ key: "bio", value: "Award-winning author with 20 years of experience..." }

{ key: "email", value: "jane@example.com" }

{ key: "photo", value: "gid://shopify/MediaImage/123" }

]

}) {

metaobject {

id

handle

displayName

fields {

key

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

## [Anchor to Merchant-owned metaobjects](/docs/apps/build/metaobjects#merchant-owned-metaobjects)Merchant-owned metaobjects

Merchant-owned metaobjects are custom data structures that can be managed in the Shopify admin or through any installed app. These metaobject entries are ideal for content that should be accessible and editable through the admin interface or multiple apps.

Merchant-ownership is defined by using any [non-reserved type](#metaobject-ownership) and can be created using the GraphQL Admin API.

Info

Merchant-owned metaobjects must be created using GraphQL. TOML configuration only creates app-owned metaobjects.

**Info:**

Merchant-owned metaobjects must be created using GraphQL. TOML configuration only creates app-owned metaobjects.

### [Anchor to Example](/docs/apps/build/metaobjects#example)Example

You want to add size chart information to products. Because this type of structured data should be managed in the Shopify admin and accessible to all apps, you use a merchant-owned metaobject.

#### [Anchor to Step 1: Create the metaobject definition](/docs/apps/build/metaobjects#step-1-create-the-metaobject-definition)Step 1: Create the metaobject definition

Create the metaobject definition using GraphQL. The following creates the definition with type identifier `size_chart` (no prefix makes it merchant-owned):

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

mutation CreateSizeChartDefinition {

metaobjectDefinitionCreate(definition: {

type: "size\_chart"

name: "Size Chart"

description: "Product sizing information"

access: {

storefront: PUBLIC\_READ

}

fieldDefinitions: [

{

key: "size"

name: "Size"

type: "single\_line\_text\_field"

}

{

key: "chest\_inches"

name: "Chest (inches)"

type: "number\_decimal"

}

{

key: "waist\_inches"

name: "Waist (inches)"

type: "number\_decimal"

}

{

key: "length\_inches"

name: "Length (inches)"

type: "number\_decimal"

}

]

}) {

metaobjectDefinition {

id

type

name

fieldDefinitions {

key

name

type { name }

}

}

userErrors {

field

message

}

}

}

#### [Anchor to Step 2: Create the metaobjects](/docs/apps/build/metaobjects#step-2-create-the-metaobjects)Step 2: Create the metaobjects

Create metaobjects (entries) for specific size charts:

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

mutation CreateSizeChartEntry {

metaobjectCreate(metaobject: {

type: "size\_chart"

fields: [

{ key: "size", value: "Medium" }

{ key: "chest\_inches", value: "38" }

{ key: "waist\_inches", value: "32" }

{ key: "length\_inches", value: "29" }

]

}) {

metaobject {

id

handle

displayName

fields {

key

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

## [Anchor to Permissions](/docs/apps/build/metaobjects#permissions)Permissions

Configure who can read and write your metaobjects using the `access` settings on your definition.

### [Anchor to Shopify admin permissions](/docs/apps/build/metaobjects#shopify-admin-permissions)Shopify admin permissions

`admin` controls permissions for both the Shopify admin and the GraphQL Admin API.

**For app-owned metaobjects:**

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

**For merchant-owned metaobjects:**

* Always full access - readable and writable by merchants and all apps with appropriate scopes. No configuration needed.

### [Anchor to Storefront permissions](/docs/apps/build/metaobjects#storefront-permissions)Storefront permissions

`storefront` controls permissions for the Storefront API (used by headless and custom storefronts).

**Available settings:**

9

1

2

3

4

5

# Not accessible on storefront (default)

access.storefront = "none"

# Accessible via Storefront API

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

storefront: NONE # not accessible (default)

}

access: {

storefront: PUBLIC\_READ # accessible via Storefront API

}

##### TOML

```liquid
# Not accessible on storefront (default)
access.storefront = "none"

# Accessible via Storefront API
access.storefront = "public_read"
```

##### GraphQL

```liquid
access: {
  storefront: NONE  # not accessible (default)
}

access: {
  storefront: PUBLIC_READ  # accessible via Storefront API
}
```

---

## [Anchor to Next steps](/docs/apps/build/metaobjects#next-steps)Next steps

* Learn how to [model your data structure](/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).
* Learn how to [work with metaobject definitions](/docs/apps/build/metaobjects/manage-metaobject-definitions).
* Learn how to [work with metaobject entries](/docs/apps/build/metaobjects/manage-metaobjects).
* Learn how to use metaobjects to [query entries](/docs/apps/build/metaobjects/query-metaobjects).
* Learn how to [enable advanced features](/docs/apps/build/metaobjects/use-metaobject-capabilities).

---

Was this page helpful?

YesNo