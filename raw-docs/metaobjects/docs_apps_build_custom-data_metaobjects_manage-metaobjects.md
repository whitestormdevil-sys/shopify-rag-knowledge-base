---
source: https://shopify.dev/docs/apps/build/custom-data/metaobjects/manage-metaobjects
---

Metaobjects let you store structured data with multiple related field values. This guide shows you how to create, read, update, and delete metaobject entries using the GraphQL Admin API.

---

## [Anchor to Requirements](/docs/apps/build/metaobjects/manage-metaobjects#requirements)Requirements

* Your app can make [authenticated requests](/docs/api/usage/authentication) to the GraphQL Admin API.
* Your app has the `read_metaobjects` and `write_metaobjects` [access scopes](/docs/api/usage/access-scopes).
* You've created a [metaobject definition](/docs/apps/build/metaobjects/manage-metaobject-definitions) for your metaobject. The definition specifies the fields, validations, and permissions.

---

## [Anchor to Creating entries](/docs/apps/build/metaobjects/manage-metaobjects#creating-entries)Creating entries

Create metaobject entries to store instances of structured data based on your metaobject definitions.

### [Anchor to Create a basic entry](/docs/apps/build/metaobjects/manage-metaobjects#create-a-basic-entry)Create a basic entry

This example creates a size chart metaobject entry with basic field values. Both the field keys and `type` must match the existing metaobject definition.

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

{ key: "hip\_inches", value: "36" }

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

### [Anchor to Create an entry with capabilities](/docs/apps/build/metaobjects/manage-metaobjects#create-an-entry-with-capabilities)Create an entry with capabilities

If your metaobject definition has [capabilities](/docs/apps/build/metaobjects/use-metaobject-capabilities) enabled (such as publishable), set their initial state when creating entries. This example creates an author metaobject with publishable status set to active.

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

mutation CreatePublishableEntry {

metaobjectCreate(metaobject: {

type: "$app:author"

capabilities: {

publishable: {

status: ACTIVE

}

}

fields: [

{ key: "full\_name", value: "Jane Smith" }

{ key: "bio", value: "Award-winning author with 20 years of experience..." }

{ key: "email", value: "jane@example.com" }

]

}) {

metaobject {

id

handle

displayName

capabilities {

publishable {

status

}

}

}

userErrors {

field

message

}

}

}

### [Anchor to Create entries in batch](/docs/apps/build/metaobjects/manage-metaobjects#create-entries-in-batch)Create entries in batch

When you need to create many metaobject entries, use bulk operations for better performance. This is more efficient than making separate requests for each entry.

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

mutation CreateBulkEntries {

bulkOperationRunMutation(

mutation: """

mutation createMetaobject($input: MetaobjectCreateInput!) {

metaobjectCreate(metaobject: $input) {

metaobject { id }

userErrors { field message }

}

}

"""

stagedUploadPath: "bulk\_ops/metaobjects\_create.jsonl"

) {

bulkOperation {

id

status

}

userErrors {

field

message

}

}

}

---

## [Anchor to Reading entries](/docs/apps/build/metaobjects/manage-metaobjects#reading-entries)Reading entries

Query metaobject entries to retrieve their data using various approaches.

### [Anchor to Query entries by type](/docs/apps/build/metaobjects/manage-metaobjects#query-entries-by-type)Query entries by type

Retrieve all metaobject entries of a specific type. This is useful when you need to list all entries, such as displaying all size charts or author profiles.

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

query GetSizeCharts {

metaobjects(type: "size\_chart", first: 10) {

edges {

node {

id

handle

displayName

fields {

key

value

}

}

}

}

}

### [Anchor to Query a specific entry by handle](/docs/apps/build/metaobjects/manage-metaobjects#query-a-specific-entry-by-handle)Query a specific entry by handle

Retrieve a single metaobject using its handle. Handles are URL-friendly identifiers for referencing specific entries.

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

query GetMetaobjectByHandle {

metaobjectByHandle(handle: {

type: "size\_chart"

handle: "medium"

}) {

id

handle

displayName

fields {

key

value

}

updatedAt

}

}

### [Anchor to Query a specific entry by ID](/docs/apps/build/metaobjects/manage-metaobjects#query-a-specific-entry-by-id)Query a specific entry by ID

Retrieve a metaobject entry using its global ID. This is useful when you have the ID stored and need to fetch the entry's current state.

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

query GetMetaobjectById {

metaobject(id: "gid://shopify/Metaobject/123") {

id

handle

displayName

type

fields {

key

value

type

}

capabilities {

publishable {

status

}

}

}

}

### [Anchor to Query specific fields](/docs/apps/build/metaobjects/manage-metaobjects#query-specific-fields)Query specific fields

Optimize queries by requesting only the fields you need.

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

query GetSpecificFields {

metaobject(id: "gid://shopify/Metaobject/123") {

field(key: "full\_name") {

value

}

emailField: field(key: "email") {

value

}

}

}

### [Anchor to Query with filters](/docs/apps/build/metaobjects/manage-metaobjects#query-with-filters)Query with filters

Filter metaobject entries based on field values. This is useful for finding entries that match specific criteria, such as all size charts for "Large" sizes.

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

query GetFilteredMetaobjects {

metaobjects(

type: "size\_chart"

first: 10

query: "size:Large"

) {

edges {

node {

id

displayName

fields {

key

value

}

}

}

}

}

---

## [Anchor to Updating entries](/docs/apps/build/metaobjects/manage-metaobjects#updating-entries)Updating entries

Modify existing metaobject entries to change field values or capability states.

### [Anchor to Update field values](/docs/apps/build/metaobjects/manage-metaobjects#update-field-values)Update field values

Update one or more field values in a metaobject entry. Optimize the operation by including only the fields you want to change.

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

mutation UpdateSizeChart {

metaobjectUpdate(

id: "gid://shopify/Metaobject/123"

metaobject: {

fields: [

{ key: "chest\_inches", value: "40" }

{ key: "waist\_inches", value: "34" }

]

}

) {

metaobject {

id

fields {

key

value

}

updatedAt

}

userErrors {

field

message

}

}

}

Note

You can't change the metaobject `type` after it's created. Field keys must match those defined in the metaobject definition, and field values must match their defined types.

**Note:**

You can't change the metaobject `type` after it's created. Field keys must match those defined in the metaobject definition, and field values must match their defined types.

### [Anchor to Update published status](/docs/apps/build/metaobjects/manage-metaobjects#update-published-status)Update published status

For metaobjects with the publishable capability enabled, change their published status to control visibility on the storefront.

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

mutation PublishMetaobject {

metaobjectUpdate(

id: "gid://shopify/Metaobject/123"

metaobject: {

capabilities: {

publishable: {

status: ACTIVE

}

}

}

) {

metaobject {

id

capabilities {

publishable {

status

}

}

}

userErrors {

field

message

}

}

}

### [Anchor to Bulk update entries](/docs/apps/build/metaobjects/manage-metaobjects#bulk-update-entries)Bulk update entries

When you need to update many metaobject entries, use bulk operations for better performance.

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

mutation BulkUpdateMetaobjects {

bulkOperationRunMutation(

mutation: """

mutation updateMetaobject($id: ID!, $metaobject: MetaobjectUpdateInput!) {

metaobjectUpdate(id: $id, metaobject: $metaobject) {

metaobject { id }

userErrors { field message }

}

}

"""

stagedUploadPath: "bulk\_ops/metaobjects\_update.jsonl"

) {

bulkOperation {

id

status

}

userErrors {

field

message

}

}

}

---

## [Anchor to Deleting entries](/docs/apps/build/metaobjects/manage-metaobjects#deleting-entries)Deleting entries

Remove metaobject entries that are no longer needed using the GraphQL Admin API.

### [Anchor to Delete a single entry](/docs/apps/build/metaobjects/manage-metaobjects#delete-a-single-entry)Delete a single entry

Delete a metaobject entry using its global ID.

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

mutation DeleteMetaobject {

metaobjectDelete(

id: "gid://shopify/Metaobject/123"

) {

deletedId

userErrors {

field

message

}

}

}

### [Anchor to Bulk delete entries](/docs/apps/build/metaobjects/manage-metaobjects#bulk-delete-entries)Bulk delete entries

When you need to delete many metaobject entries, use bulk operations for better performance.

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

mutation BulkDeleteMetaobjects {

bulkOperationRunMutation(

mutation: """

mutation deleteMetaobject($id: ID!) {

metaobjectDelete(id: $id) {

deletedId

userErrors { field message }

}

}

"""

stagedUploadPath: "bulk\_ops/metaobjects\_delete.jsonl"

) {

bulkOperation {

id

status

}

userErrors {

field

message

}

}

}

---

## [Anchor to Connecting metaobjects to resources](/docs/apps/build/metaobjects/manage-metaobjects#connecting-metaobjects-to-resources)Connecting metaobjects to resources

One of the most powerful patterns with metaobjects is connecting them to Shopify resources using metafields. [Reference type metafields](/docs/apps/build/metafields/list-of-data-types#reference-types) store links to metaobject entries, enabling you to create reusable structured data that can be attached to products, orders, and other resources.

**How it works:**

1. Create definitions (metaobject + metafield) in your TOML configuration and deploy
2. Create metaobject entries (such as "Waterproof", "Eco-friendly", "Durable")
3. Attach entries to products by setting the metafield value

**Why use this pattern:**

* **Reusability**: Create a feature (such as 'Waterproof') once, reference it from 100 products
* **Maintainability**: Update the feature entry, and it updates everywhere it's referenced
* **Structure**: Features have consistent fields (title, description, icon) defined by the metaobject definition

**Reference types available:**

* `metaobject_reference` - Link to a single metaobject entry
* `list.metaobject_reference` - Link to multiple entries of the same metaobject type
* `mixed_reference` - Link to entries from different metaobject types

### [Anchor to Step 1: Create definitions](/docs/apps/build/metaobjects/manage-metaobjects#step-1-create-definitions)Step 1: Create definitions

Define the metaobject structure and the metafield that references it:

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

# Metaobject definition

[metaobjects.app.product\_feature]

name = "Product Feature"

[metaobjects.app.product\_feature.fields.title]

type = "single\_line\_text\_field"

name = "Title"

[metaobjects.app.product\_feature.fields.description]

type = "multi\_line\_text\_field"

name = "Description"

[metaobjects.app.product\_feature.fields.icon]

type = "file\_reference"

name = "Icon"

# Metafield definition that references the metaobject

[product.metafields.product\_info.features]

type = "list.metaobject\_reference<$app:product\_feature>"

name = "Product Features"

Deploy the definitions:

9

1

shopify app deploy

### [Anchor to Step 2: Create metaobject entries](/docs/apps/build/metaobjects/manage-metaobjects#step-2-create-metaobject-entries)Step 2: Create metaobject entries

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

mutation CreateWaterproofFeature {

metaobjectCreate(metaobject: {

type: "product\_feature"

fields: [

{ key: "title", value: "Waterproof" }

{ key: "description", value: "Protected against water damage" }

]

}) {

metaobject {

id # gid://shopify/Metaobject/789

handle

}

userErrors {

field

message

}

}

}

### [Anchor to Step 3: Attach metaobject entries to a product](/docs/apps/build/metaobjects/manage-metaobjects#step-3-attach-metaobject-entries-to-a-product)Step 3: Attach metaobject entries to a product

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

mutation AttachFeaturesToProduct {

productUpdate(input: {

id: "gid://shopify/Product/456"

metafields: [{

namespace: "product\_info"

key: "features"

type: "list.metaobject\_reference"

value: "[\"gid://shopify/Metaobject/789\", \"gid://shopify/Metaobject/790\"]"

}]

}) {

product {

metafield(namespace: "product\_info", key: "features") {

references(first: 10) {

nodes {

... on Metaobject {

handle

fields { key value }

}

}

}

}

}

userErrors {

field

message

}

}

}

---

## [Anchor to Handle management](/docs/apps/build/metaobjects/manage-metaobjects#handle-management)Handle management

Metaobject handles are URL-friendly identifiers used to reference entries.

### [Anchor to Auto-generated handles](/docs/apps/build/metaobjects/manage-metaobjects#auto-generated-handles)Auto-generated handles

By default, Shopify generates handles from the display name:

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

mutation CreateWithAutoHandle {

metaobjectCreate(metaobject: {

type: "size\_chart"

fields: [

{ key: "size", value: "Extra Large" }

]

}) {

metaobject {

handle # Will be "extra-large"

displayName

}

}

}

### [Anchor to Custom handles](/docs/apps/build/metaobjects/manage-metaobjects#custom-handles)Custom handles

Specify a custom handle for more control:

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

mutation CreateWithCustomHandle {

metaobjectCreate(metaobject: {

type: "size\_chart"

handle: "xl-size-chart"

fields: [

{ key: "size", value: "Extra Large" }

]

}) {

metaobject {

handle

displayName

}

userErrors {

field

message

}

}

}

---

## [Anchor to Error handling](/docs/apps/build/metaobjects/manage-metaobjects#error-handling)Error handling

Common errors when managing metaobject entries:

| Error | Cause | Solution |
| --- | --- | --- |
| `UNDEFINED_OBJECT_TYPE` | No metaobject definition exists for this type | Create the definition first or check the type identifier |
| `OBJECT_FIELD_REQUIRED` | A required field value is not provided | Include all required fields in the mutation |
| `UNDEFINED_OBJECT_FIELD` | Field key doesn't exist in the definition | Verify field keys match the definition |
| `CAPABILITY_NOT_ENABLED` | Trying to use a capability not enabled on the definition | Enable the capability on the definition first |

---

## [Anchor to Best practices](/docs/apps/build/metaobjects/manage-metaobjects#best-practices)Best practices

* Use meaningful handles: Choose handles that clearly identify the entry's purpose.
* Validate before creating: Check that all required fields are provided and values match expected types.
* Use bulk operations for scale: When creating, updating, or deleting many entries, use bulk operations for better performance.
* Query only needed fields: Optimize API usage by requesting only the fields you need.
* Handle errors gracefully: Check `userErrors` in responses and provide clear feedback.
* Consider capability states: Set appropriate published/unpublished states for publishable metaobjects.

---

## [Anchor to Troubleshooting](/docs/apps/build/metaobjects/manage-metaobjects#troubleshooting)Troubleshooting

Common issues and solutions when working with metaobject entries:

| Issue | Possible Causes | Solution |
| --- | --- | --- |
| Entry not appearing on storefront | Missing storefront access, unpublished entry, or incorrect query | Verify the definition has `storefront: PUBLIC_READ` access, check if the entry is published (for publishable metaobjects), and ensure your storefront query includes the correct type |
| Unable to update entry | Missing permissions, incorrect ID, or invalid field keys | Confirm you have write access to the metaobject type, check that the entry ID is correct and the entry still exists, and verify field keys match the definition |
| Bulk operation failing | Invalid JSONL format, missing required fields, or file size issues | Validate your JSONL file format, check that all entries have required fields, ensure file size is within limits, and review bulk operation status for specific error details |

---

## [Anchor to Next steps](/docs/apps/build/metaobjects/manage-metaobjects#next-steps)Next steps

* Learn how to [work with metaobject definitions](/docs/apps/build/metaobjects/manage-metaobject-definitions).
* Learn how to [enable advanced features](/docs/apps/build/metaobjects/use-metaobject-capabilities).
* Learn about [metaobject limits](/docs/apps/build/metaobjects/metaobject-limits).

---

Was this page helpful?

YesNo