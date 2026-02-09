---
source: https://shopify.dev/docs/api/usage/bulk-operations/imports
---

Importing large volumes of data using traditional and synchronous APIs is slow, complex to run, and difficult to manage. Instead of manually running a GraphQL mutation multiple times and managing a client-side throttle, you can run a bulk mutation operation.

Using the GraphQL Admin API, you can bulk import large volumes of data asynchronously. When the operation is complete, the results are delivered in a [JSON Lines (JSONL)](https://jsonlines.org/) file that Shopify makes available at a URL.

This guide introduces the [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) and shows you how to use it to bulk import data into Shopify.

In API versions `2026-01` and higher, you can run up to five bulk mutation operations at a time per shop. In API versions prior to `2026-01`, you can run only one bulk mutation operation at a time per shop. When the operation is complete, the results are delivered in a [JSON Lines (JSONL)](https://jsonlines.org/) file that Shopify makes available at a URL.

---

## [Anchor to Requirements](/docs/api/usage/bulk-operations/imports#requirements)Requirements

* You're familiar with creating [products](/docs/api/admin-graphql/latest/mutations/productcreate), [product variants](/docs/api/admin-graphql/latest/mutations/productvariantcreate), and [collections](/docs/api/admin-graphql/latest/mutations/collectioncreate) in your development store.
* You're familiar with [performing bulk operations](/docs/api/usage/bulk-operations/queries) using the GraphQL Admin API.

---

## [Anchor to Limitations](/docs/api/usage/bulk-operations/imports#limitations)Limitations

* In API versions `2026-01` and higher, you can run up to five bulk mutation operations at a time per shop. In API versions prior to `2026-01`, you can run only one bulk operation of each type ([`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) or [`bulkOperationRunQuery`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunquery)) at a time per shop.
* The bulk mutation operation has to complete within 24 hours. After that it will be stopped and marked as `failed`. When your import runs into this limit, consider reducing the input size.
* You can supply any GraphQL Admin API mutation to the `bulkOperationRunMutation`, except for `bulkOperationRunMutation` and `bulkOperationRunQuery` themselves (to prevent recursion).
* The mutation that's passed into `bulkOperationRunMutation` is limited to one connection field, which is defined by the GraphQL Admin API schema.
* The size of the JSONL file can't exceed 100MB.

---

## [Anchor to How bulk importing data works](/docs/api/usage/bulk-operations/imports#how-bulk-importing-data-works)How bulk importing data works

You initiate a bulk operation by supplying a mutation string in the [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunMutation). Shopify then executes that mutation string asynchronously as a bulk operation.

Most GraphQL Admin API requests that you make are subject to [rate limits](/docs/api/usage/limits#rate-limits), but the `bulkOperationRunMutation` request isn't. Because you're only making low-cost requests for creating operations, polling their status, or canceling them, bulk mutation operations are an efficient way to create data compared to standard GraphQL API requests.

### [Anchor to Listing and filtering bulk operations](/docs/api/usage/bulk-operations/imports#listing-and-filtering-bulk-operations)Listing and filtering bulk operations

In API versions `2026-01` and higher, you can use the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) query to list, filter, and paginate your bulk operations. `bulkOperations` replaces the deprecated [`currentBulkOperation`](/docs/api/admin-graphql/latest/queries/currentBulkOperation) query.

The `bulkOperations` query provides the following features:

* Filtering by [status](/docs/api/admin-graphql/2026-01/queries/bulkOperations#argument-query-filter-status), such as `completed`, `running`, or `failed`.
* Filtering by operation type, such as query or mutation.
* [Sorting](/docs/api/admin-graphql/2026-01/queries/bulkOperations#arguments-sortKey) by values such as creation date, completion date, status, or ID.
* [Pagination](/docs/api/usage/pagination-graphql) with cursor-based navigation.
* The [`bulkOperation`](/docs/api/admin-graphql/2026-01/queries/bulkOperation) query replaces the deprecated [`currentBulkOperation`](/docs/api/admin-graphql/latest/queries/currentBulkOperation) query by allowing a direct lookup of a specific operation by ID using `bulkOperation(id:)`.

For complete details, refer to the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) and [`bulkOperation`](/docs/api/admin-graphql/2026-01/queries/bulkOperation) query reference.

The following diagram shows the steps involved in bulk importing data into Shopify:

![Workflow for bulk importing data](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/api/tutorials/bulk-import-data-CVIWHlpb.png)

1. **Create a JSONL file and include GraphQL variables**: Include the variables for the mutation in a JSONL file format. Each line in the JSONL file represents one input unit. The mutation runs once on each line of the input file.
2. **Upload the file to Shopify**: Before you upload the file, you must reserve a link by running the [`stagedUploadsCreate`](/docs/api/admin-graphql/latest/mutations/stageduploadscreate) mutation. After the space has been reserved, you can upload the file by making a request using the information returned from the [`stagedUploadsCreate`](/docs/api/admin-graphql/latest/mutations/stageduploadscreate) response.
3. **Create a bulk mutation operation**: After the file has been uploaded, you can run [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) to create a bulk mutation operation. The [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) imports data in bulk by running the supplied GraphQL API mutation with the file of variables uploaded in the last step.
4. **Wait for the operation to finish**: To determine when the bulk mutation has finished, you can either:

   * **Subscribe to a webhook topic**: You can use the [`webhookSubscriptionCreate`](/docs/api/admin-graphql/latest/mutations/webhooksubscriptioncreate) mutation to subscribe to the `bulk_operations/finish` webhook topic in order to receive a webhook when any operation finishes - in other words, it has completed, failed, or been cancelled.
   * **Poll the status of the operation**: While the operation is running, you can poll to see its progress by querying the specific bulk operation using its ID (returned from the `bulkOperationRunQuery` mutation). In API version `2026-01` and higher, use the `bulkOperation(id:)` query. In API versions prior to 2026-01, use the `currentBulkOperation` query. The `objectCount` field increments to indicate the operation's progress, and the `status` field returns whether the operation is completed.
5. **Retrieve the results**: When a bulk mutation operation is completed, a JSONL output file is available for download at the URL specified in the `url` field.

---

## [Anchor to Create a JSONL file and include GraphQL variables](/docs/api/usage/bulk-operations/imports#create-a-jsonl-file-and-include-graphql-variables)Create a JSONL file and include GraphQL variables

When adding GraphQL variables to a new JSONL file, you need to format the variables so that they are accepted by the corresponding bulk operation GraphQL API. The format of the input variables need to match the GraphQL Admin API schema.

For example, you might want to import a large quantity of products. Each attribute of a product must be mapped to existing fields defined in the GraphQL input object [`ProductInput`](/docs/api/admin-graphql/latest/input-objects/productinput). In the JSONL file, each line represents one product input. The GraphQL Admin API runs once on each line of the input file. One input should take up one line only, no matter how complex the input object structure is.

The following example shows a sample JSONL file that is used to create 10 products in bulk:

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

{ "input": { "title": "Sweet new snowboard 1", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 2", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 3", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 4", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 5", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 6", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 7", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 8", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 9", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 10", "productType": "Snowboard", "vendor": "JadedPixel" } }

Note

The GraphQL Admin API doesn't serially process the contents of the JSONL file. Avoid relying on a particular sequence of lines and object order to achieve a desired result.

**Note:**

The GraphQL Admin API doesn't serially process the contents of the JSONL file. Avoid relying on a particular sequence of lines and object order to achieve a desired result.

---

## [Anchor to Upload the file to Shopify](/docs/api/usage/bulk-operations/imports#upload-the-file-to-shopify)Upload the file to Shopify

After you've created the JSONL file, and included the GraphQL variables, you can upload the file to Shopify. Before uploading the file, you need to first generate the upload URL and parameters.

### [Anchor to Generate the uploaded URL and parameters](/docs/api/usage/bulk-operations/imports#generate-the-uploaded-url-and-parameters)Generate the uploaded URL and parameters

You can use the [`stagedUploadsCreate`](/docs/api/admin-graphql/latest/mutations/stageduploadscreate) mutation to generate the values that you need to authenticate the upload. The mutation returns an array of [`stagedMediaUploadTarget`](/docs/api/admin-graphql/latest/objects/stagedmediauploadtarget) instances.

An instance of [`stagedMediaUploadTarget`](/docs/api/admin-graphql/latest/objects/stagedmediauploadtarget) has the following key properties:

* `parameters`: The parameters that you use to authenticate an upload request.
* `url`: The signed URL where you can upload the JSONL file that includes GraphQL variables.

The mutation accepts an input of type [`stagedUploadInput`](/docs/api/admin-graphql/latest/input-objects/stageduploadinput), which has the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `resource` | [enum](/docs/api/admin-graphql/latest/enums/stageduploadtargetgenerateuploadresource) | Specifies the resource type to upload. To use `bulkOperationRunMutation`, the resource type must be `BULK_MUTATION_VARIABLES`. |
| `filename` | [string](/docs/api/admin-graphql/latest/scalars/String) | The name of the file to upload. |
| `mimeType` | [string](/docs/api/admin-graphql/latest/scalars/String) | The [media type](https://en.wikipedia.org/wiki/Media_type) of the file to upload. To use `bulkOperationRunMutation`, the `mimeType` must be `"text/jsonl"`. |
| `httpMethod` | [enum](/docs/api/admin-graphql/latest/enums/stageduploadhttpmethodtype) | The HTTP method to be used by the staged upload. To use `bulkOperationRunMutation`, the `httpMethod` must be `POST`. |

#### [Anchor to Example](/docs/api/usage/bulk-operations/imports#example)Example

The following example uses the [`stagedUploadsCreate`](/docs/api/admin-graphql/latest/mutations/stageduploadscreate) mutation to generate the values required to upload a JSONL file and be consumed by the [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation). You must first run the `stagedUploadsCreate` mutation with no variables, and then separately send a POST request to the staged upload URL with the JSONL data:

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

stagedUploadsCreate(input:[{

resource: BULK\_MUTATION\_VARIABLES,

filename: "bulk\_op\_vars",

mimeType: "text/jsonl",

httpMethod: POST

}]){

userErrors{

field,

message

},

stagedTargets{

url,

resourceUrl,

parameters {

name,

value

}

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

52

53

54

55

56

57

{

"data": {

"stagedUploadsCreate": {

"userErrors": [],

"stagedTargets": [

{

"url": "https://shopify-staged-uploads.storage.googleapis.com",

"resourceUrl": null,

"parameters": [

{

"name": "key",

"value": "tmp/21759409/bulk/2d278b12-d153-4667-a05c-a5d8181623de/bulk\_op\_vars"

},

{

"name": "Content-Type",

"value": "text/jsonl"

},

{

"name": "success\_action\_status",

"value": "201"

},

{

"name": "acl",

"value": "private"

},

{

"name": "policy",

"value": "zyJjb25kaXRpb25zIjpbeyJDb250ZW50LVR5cGUiOiJ0ZXh0XC9qc29ubCJ9LHsic3VjY2Vzc19hY3Rpb25fc3RhdHVzIjoiMjAxIn0seyJhY2wiOiJwcml2YXRlIn0sWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMSwyMDk3MTUyMF0seyJidWNrZXQiOiJzaG9waWZ5LXN0YWdlZC11cGxvYWRzIn0seyJrZXkiOiJ0bXBcL2djc1wvMTQzMjMyMjEwNFwvYnVsa1wvM2QyNzhiMTItZDE1My00NjY3LWEwNWMtYTVkODE4MTYyM2RlXC9idWxrX29wX3ZhcnMifSx7IngtZ29vZy1kYXRlIjoiMjAyMjA4MzBUMDI1MTI3WiJ9LHsieC1nb29nLWNyZWRlbnRpYWwiOiJtZXJjaGFudC1hc3NldHNAc2hvcGlmeS10aWVycy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbVwvMjAyMjA4MzBcL2F1dG9cL3N0b3JhZ2VcL2dvb2c0X3JlcXVlc3QifSx7IngtZ29vZy1hbGdvcml0aG0iOiJHT09HNC1SU0EtU0hBMjU2In1dLCJleHBpcmF0aW9uIjoiMjAyMi0wOC0zMVQwMjo1MToyN1oifQ=="

},

{

"name": "x-goog-credential",

"value": "merchant-assets@shopify-tiers.iam.gserviceaccount.com/20220830/auto/storage/goog4\_request"

},

{

"name": "x-goog-algorithm",

"value": "GOOG4-RSA-SHA256"

},

{

"name": "x-goog-date",

"value": "20220830T025127Z"

},

{

"name": "x-goog-signature",

"value": "4c0f6920cd67cbdf1faae75c112a98d49f9751e4e0c9f525c850f15f40629afa13584ab9937ec9f5292065ca8fd357ba87e98d6ab0e383e15a6e444c7e9bae06fb95dc422ad673fe77aefcb68e9d1a6d55deb478e6976b61769e20863992fffd4036898f76c7a50e92f18aa4d9e3e04aa8d04086386dc0e488f2ccb0ebcc30c17da2ba5a4d6a9cd57553b41ef6698dbefc78a9b3fe1af167ea539b70e83e5fb015f061399e952270202b769ae8f4e7e50e97dbe6679c3281ec3fc886c3a67becc7b3cee1d0e6a2d0777d09f6d7b083499c58f9c566eeb5374afd67e26c7ab2a91cfe5c5deb83a507d7e3c3ea44bb9f401afd3f2e6b09742baff2b30bc3def78a"

}

]

}

]

}

},

"extensions": {

"cost": {

"requestedQueryCost": 11,

"actualQueryCost": 11

}

}

}

### [Anchor to Upload the JSONL file](/docs/api/usage/bulk-operations/imports#upload-the-jsonl-file)Upload the JSONL file

After you generate the parameters and URL for an upload, you can upload the JSONL file using a POST request. You must use a multipart form, and include all parameters as form inputs in the request body.

To generate the parameters for the multipart form, start with the parameters returned from the `stagedUploadsCreate` mutation. Then, add the file attachment.

Note

The `file` parameter must be the last parameter in the list. If you add the `file` parameter somewhere else, then you'll receive an error.

**Note:**

The `file` parameter must be the last parameter in the list. If you add the `file` parameter somewhere else, then you'll receive an error.

Caution

After uploading your JSONL file, don't modify or replace the file at the staged upload URL while the bulk operation is running. The system validates the file's integrity using checksums, and any modifications will cause the operation to fail with an `INTERNAL_SERVER_ERROR`.

**Caution:**

After uploading your JSONL file, don't modify or replace the file at the staged upload URL while the bulk operation is running. The system validates the file's integrity using checksums, and any modifications will cause the operation to fail with an `INTERNAL_SERVER_ERROR`.

**POST request**

$

$

$

$

$

$

$

$

$

$

$

$

curl --location --request POST 'https://shopify-staged-uploads.storage.googleapis.com/' \

--form 'key="tmp/21759409/bulk/2d278b12-d153-4667-a05c-a5d8181623de/bulk\_op\_vars"' \

--form 'x-goog-credential="merchant-assets@shopify-tiers.iam.gserviceaccount.com/20220830/auto/storage/goog4\_request"' \

--form 'x-goog-algorithm="GOOG4-RSA-SHA256"' \

--form 'x-goog-date="20220830T025127Z"' \

--form 'x-goog-signature="4c0f6920cd67cbdf1faae75c112a98d49f9751e4e0c9f525c850f15f40629afa13584ab9937ec9f5292065ca8fd357ba87e98d6ab0e383e15a6e444c7e9bae06fb95dc422ad673fe77aefcb68e9d1a6d55deb478e6976b61769e20863992fffd4036898f76c7a50e92f18aa4d9e3e04aa8d04086386dc0e488f2ccb0ebcc30c17da2ba5a4d6a9cd57553b41ef6698dbefc78a9b3fe1af167ea539b70e83e5fb015f061399e952270202b769ae8f4e7e50e97dbe6679c3281ec3fc886c3a67becc7b3cee1d0e6a2d0777d09f6d7b083499c58f9c566eeb5374afd67e26c7ab2a91cfe5c5deb83a507d7e3c3ea44bb9f401afd3f2e6b09742baff2b30bc3def78a"' \

--form 'policy="zyJjb25kaXRpb25zIjpbeyJDb250ZW50LVR5cGUiOiJ0ZXh0XC9qc29ubCJ9LHsic3VjY2Vzc19hY3Rpb25fc3RhdHVzIjoiMjAxIn0seyJhY2wiOiJwcml2YXRlIn0sWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMSwyMDk3MTUyMF0seyJidWNrZXQiOiJzaG9waWZ5LXN0YWdlZC11cGxvYWRzIn0seyJrZXkiOiJ0bXBcL2djc1wvMTQzMjMyMjEwNFwvYnVsa1wvM2QyNzhiMTItZDE1My00NjY3LWEwNWMtYTVkODE4MTYyM2RlXC9idWxrX29wX3ZhcnMifSx7IngtZ29vZy1kYXRlIjoiMjAyMjA4MzBUMDI1MTI3WiJ9LHsieC1nb29nLWNyZWRlbnRpYWwiOiJtZXJjaGFudC1hc3NldHNAc2hvcGlmeS10aWVycy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbVwvMjAyMjA4MzBcL2F1dG9cL3N0b3JhZ2VcL2dvb2c0X3JlcXVlc3QifSx7IngtZ29vZy1hbGdvcml0aG0iOiJHT09HNC1SU0EtU0hBMjU2In1dLCJleHBpcmF0aW9uIjoiMjAyMi0wOC0zMVQwMjo1MToyN1oifQ=="' \

--form 'acl="private"' \

--form 'Content-Type="text/jsonl"' \

--form 'success\_action\_status="201"' \

--form 'file=@"/Users/username/Documents/bulk\_mutation\_tests/products\_long.jsonl"'

**GraphQL variables in JSONL file**

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

{ "input": { "title": "Sweet new snowboard 1", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 2", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 3", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 4", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 5", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 6", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 7", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 8", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 9", "productType": "Snowboard", "vendor": "JadedPixel" } }

{ "input": { "title": "Sweet new snowboard 10", "productType": "Snowboard", "vendor": "JadedPixel" } }

---

## [Anchor to Create a bulk mutation operation](/docs/api/usage/bulk-operations/imports#create-a-bulk-mutation-operation)Create a bulk mutation operation

After you upload the file, you can run [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) to import data in bulk. You must supply the corresponding mutation and the URL that you obtained in the [previous step](#generate-the-uploaded-url-and-parameters).

The [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) mutation takes the following arguments:

| Field | Type | Description |
| --- | --- | --- |
| `mutation` | [string](/docs/api/admin-graphql/latest/scalars/String) | Specifies the GraphQL API mutation that you want to run in bulk. Valid values: [`productCreate`](/docs/api/admin-graphql/latest/mutations/productcreate), [`collectionCreate`](/docs/api/admin-graphql/latest/mutations/collectioncreate), [`productUpdate`](/docs/api/admin-graphql/latest/mutations/productupdate), [`productUpdateMedia`](/docs/api/admin-graphql/latest/mutations/productupdatemedia) |
| `stagedUploadPath` | [string](/docs/api/admin-graphql/latest/scalars/String) | The path to the file of inputs in JSONL format to be consumed by [`stagedUploadsCreate`](/docs/api/admin-graphql/latest/mutations/stageduploadscreate) |

### [Anchor to Example](/docs/api/usage/bulk-operations/imports#example)Example

In the following example, you want to run the following [`productCreate`](/docs/api/admin-graphql/latest/mutations/productcreate) mutation in bulk:

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

mutation call($input: ProductInput!) {

productCreate(input: $input) {

product {

id

title

variants(first: 10) {

edges {

node {

id

title

inventoryQuantity

}

}

}

}

userErrors {

message

field

}

}

}

To run the `productCreate` mutation in bulk, pass the mutation as a string into [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunMutation):

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

mutation {

bulkOperationRunMutation(

mutation: "mutation call($input: ProductInput!) { productCreate(input: $input) { product {id title variants(first: 10) {edges {node {id title inventoryQuantity }}}} userErrors { message field } } }",

stagedUploadPath: "tmp/21759409/bulk/89e620e1-0252-43b0-8f3b-3b7075ba4a23/bulk\_op\_vars") {

bulkOperation {

id

url

status

}

userErrors {

message

field

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

{

"data": {

"bulkOperationRunMutation": {

"bulkOperation": {

"id": "gid://shopify/BulkOperation/206005076024",

"url": null,

"status": "CREATED"

},

"userErrors": []

}

},

"extensions": {

"cost": {

"requestedQueryCost": 10,

"actualQueryCost": 10

}

}

}

---

## [Anchor to Wait for the operation to finish](/docs/api/usage/bulk-operations/imports#wait-for-the-operation-to-finish)Wait for the operation to finish

Tip

Subscribing to the webhook topic is recommended over polling as it limits the number of redundant API calls.

**Tip:**

Subscribing to the webhook topic is recommended over polling as it limits the number of redundant API calls.

### [Anchor to Option A. Subscribe to the ,[object Object], webhook topic](/docs/api/usage/bulk-operations/imports#option-a-subscribe-to-the-bulk_operations-finish-webhook-topic)Option A. Subscribe to the `bulk_operations/finish` webhook topic

You can use the [`webhookSubscriptionCreate`](/docs/api/admin-graphql/latest/mutations/webhooksubscriptioncreate) mutation to subscribe to the `bulk_operations/finish` webhook topic in order to receive a webhook when any operation finishes - in other words, it has completed, failed, or been cancelled.

For full setup instructions, refer to [Configuring webhooks](/docs/apps/build/webhooks/subscribe).

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

mutation {

webhookSubscriptionCreate(

topic: BULK\_OPERATIONS\_FINISH

webhookSubscription: {

format: JSON,

uri: "https://12345.ngrok.io/"}

) {

userErrors {

field

message

}

webhookSubscription {

id

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

{

"data": {

"webhookSubscriptionCreate": {

"userErrors": [],

"webhookSubscription": {

"id": "gid://shopify/WebhookSubscription/4567"

}

}

},

"extensions": {

"cost": {

"requestedQueryCost": 10,

"actualQueryCost": 10,

"throttleStatus": {

"maximumAvailable": 1000,

"currentlyAvailable": 990,

"restoreRate": 50

}

}

}

}

After you've subscribed to the webhook topic, Shopify sends a POST request to the specified URL any time a bulk operation on the store (both mutations and [queries](/docs/api/usage/bulk-operations/queries)) finishes.

**Example webhook response**

9

1

2

3

4

5

6

7

8

{

"admin\_graphql\_api\_id": "gid://shopify/BulkOperation/206005076024",

"completed\_at": "2024-01-28T19:11:09Z",

"created\_at": "2024-01-28T19:10:59Z",

"error\_code": null,

"status": "completed",

"type": "mutation",

}

You now must retrieve the bulk operation's data URL by using the `node` field and passing the `admin_graphql_api_id` value from the webhook payload as its `id`:

9

1

2

3

4

5

6

7

8

query {

node(id: "gid://shopify/BulkOperation/206005076024") {

... on BulkOperation {

url

partialDataUrl

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

"data": {

"node": {

"url": "https://storage.googleapis.com/shopify/dyfkl3g72empyyoenvmtidlm9o4g?<params />",

"partialDataUrl": null

}

},

"extensions": {

"cost": {

"requestedQueryCost": 1,

"actualQueryCost": 1,

"throttleStatus": {

"maximumAvailable": 1000,

"currentlyAvailable": 999,

"restoreRate": 50

}

}

}

}

For more information on how webhooks work, refer to [Webhooks](/docs/apps/build/webhooks).

Note

Webhook delivery isn't always guaranteed, so you might still need to poll for the operation's status to check when it's finished.

**Note:**

Webhook delivery isn't always guaranteed, so you might still need to poll for the operation's status to check when it's finished.

### [Anchor to Option B. Poll the status of the operation](/docs/api/usage/bulk-operations/imports#option-b-poll-the-status-of-the-operation)Option B. Poll the status of the operation

While the operation is running, you can poll to see its progress by querying the specific bulk operation using its ID, which is returned from the [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunMutation) mutation.

In API versions `2026-01` and higher, use the `bulkOperation(id:)` query. In API versions prior to `2026-01`, use the `currentBulkOperation` query. The `objectCount` field increments to indicate the operation's progress, and the `status` field returns whether the operation is completed.

You can adjust your polling intervals based on the amount of data that you import. To learn about other possible operation statuses, refer to the [`BulkOperationStatus`](/docs/api/admin-graphql/latest/enums/bulkoperationstatus) reference documentation.

**In API versions `2026-01` and higher:**

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

query {

bulkOperation(id: "gid://shopify/BulkOperation/206005076024") {

id

status

errorCode

createdAt

completedAt

objectCount

fileSize

url

partialDataUrl

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

{

"data": {

"bulkOperation": {

"id": "gid://shopify/BulkOperation/206005076024",

"status": "COMPLETED",

"errorCode": null,

"createdAt": "2024-01-28T19:10:59Z",

"completedAt": "2024-01-28T19:11:09Z",

"objectCount": "16",

"fileSize": "6155",

"url": "https://storage.googleapis.com/shopify-tiers-assets-prod-us-east1/iqtpj52yuoa7prkbpzp9gwn27kw3?GoogleAccessId=assets-us-prod%40shopify-tiers.iam.gserviceaccount.com&Expires=1612465869&Signature=KOhlcYhLve3NLr6rfVbAeY02crFAM3rMrDNfTSlgT%2FScI%2B8o%2B%2FdO99F3UseC837uWA6FzfrNhxdRNqhBN%2F8ekBTW7IyPRD6ho5phfE8MTaev4ltQrJygJTDbjXfX5KLJOuY8siH%2FDrc4gctZsMsNaf2%2FYp%2FaDzBzjfxJge8i8he69t0uZ39FBXrMxCeMVd6lU8%2FbgMuO80rTHjgI%2BlC8g2%2FWiHyq5rSTDLIxxGWRCddMfPcaivdWVdMubMa0wOt9W9R2mfjuTAgUBexUkJwhvrkdof%2Bg00gU1g4dIBWlUSO5D9tdrv9bmIy7FceopNufrpwnD1NXU8Narsx2yEQ6aA%3D%3D&response-content-disposition=attachment%3B+filename%3D%22bulk-206005076024.jsonl%22%3B+filename%2A%3DUTF-8%27%27bulk-206005076024.jsonl&response-content-type=application%2Fjsonl",

"partialDataUrl": null

}

},

"extensions": {

"cost": {

"requestedQueryCost": 1,

"actualQueryCost": 1

}

}

}

**In API versions prior to `2026-01` (using the deprecated [`currentBulkOperation`](/docs/api/admin-graphql/latest/queries/currentBulkOperation) query):**

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

query {

currentBulkOperation(type: MUTATION) {

id

status

errorCode

createdAt

completedAt

objectCount

fileSize

url

partialDataUrl

}

}

---

## [Anchor to Retrieve the results](/docs/api/usage/bulk-operations/imports#retrieve-the-results)Retrieve the results

When a bulk mutation operation is finished, you can download a result data file.

If an operation successfully completes, then the `url` field contains a URL where you can download the data file. If an operation fails, but some data was retrieved before the failure occurred, then a partially complete data file is available at the URL specified in the `partialDataUrl` field.

In either case, the returned URLs are authenticated and expire after one week.

After you've downloaded the data, you can parse it according to the JSONL format. Since both input and response files are in JSONL, each line in the final asset file represents the response of running the mutation on the corresponding line in the input file.

### [Anchor to Operation success](/docs/api/usage/bulk-operations/imports#operation-success)Operation success

The following example shows the response for a product that was successfully created:

9

1

{"data":{"productCreate":{"product":{"id":"gid:\/\/shopify\/Product\/5602345320504","title":"Monday morning snowboard 1","variants":{"edges":[{"node":{"id":"gid:\/\/shopify\/ProductVariant\/35645836853304","title":"First","inventoryQuantity":0}},{"node":{"id":"gid:\/\/shopify\/ProductVariant\/35645836886072","title":"Second","inventoryQuantity":0}}]}},"userErrors":[]}},"\_\_lineNumber":0}

### [Anchor to Operation failures](/docs/api/usage/bulk-operations/imports#operation-failures)Operation failures

Bulk operations provide detailed per-line error handling. Each mutation in your JSONL file is validated and executed independently, with errors reported in the output file alongside successful results.

#### [Anchor to Error handling behavior](/docs/api/usage/bulk-operations/imports#error-handling-behavior)Error handling behavior

Errors are handled at the line level and reported in the output file:

* **JSON parse errors**: Invalid JSON format in a JSONL line appears as an error for that specific line in the output.
* **Validation errors**: GraphQL query validation failures, such as invalid fields or missing required arguments, display as errors for the affected line.
* **Execution errors**: Mutation failures during execution, such as business logic errors or permission issues, display in the output with detailed error messages.
* **Access denied errors**: Missing access scopes are reported for each line in the output file with details about which fields caused the issue.

The bulk operation only fails entirely (with `status: FAILED`) for critical system errors:

* `INTERNAL_SERVER_ERROR`: Something went wrong on Shopify's server and we've been notified of the error. These errors might be intermittent, so you can try making your request again.

To learn about the other possible operation error codes, refer to the [`BulkOperationErrorCode`](/docs/api/admin-graphql/2026-01/enums/BulkOperationErrorCode) reference documentation.

#### [Anchor to Best practices](/docs/api/usage/bulk-operations/imports#best-practices)Best practices

* Review the output JSONL file to identify which specific mutations failed and why.
* Each error includes the line number from your input file, making it easy to identify failing mutations.
* Test individual mutations first to validate your access scopes and mutation structure before running bulk operations.

Note

When using the `bulk_operations/finish` webhook, the `error_code` and `status` fields in the webhook payload will be lowercase. For example, `failed` instead of `FAILED`.

**Note:**

When using the `bulk_operations/finish` webhook, the `error_code` and `status` fields in the webhook payload will be lowercase. For example, `failed` instead of `FAILED`.

#### [Anchor to Error examples in output files](/docs/api/usage/bulk-operations/imports#error-examples-in-output-files)Error examples in output files

When a mutation fails, the error appears in the output JSONL file for that specific line. Here are common error formats:

##### [Anchor to Validation error](/docs/api/usage/bulk-operations/imports#validation-error)Validation error

If the input has the correct format, but one or more values failed validation, then the line in the output file looks like the following:

9

1

{"data"=>{"productCreate"=>{"userErrors"=>[{"message"=>"Some error message", "field"=>["some field"]}]}}}

##### [Anchor to Unrecognizable field error](/docs/api/usage/bulk-operations/imports#unrecognizable-field-error)Unrecognizable field error

If the input has an unrecognizable field, then the line in the output file looks like the following:

9

1

{"errors"=>[{"message"=>"Variable input of type ProductInput! was provided invalid value for myfavoriteaddress (Field is not defined on ProductInput)", "locations"=>[{"line"=>1, "column"=>13}], "extensions"=>{"value"=>{"myfavoriteaddress"=>"test1"}, "problems"=>[{"path"=>["myfavoriteaddress"], "explanation"=>"Field is not defined on ProductInput"}]}}]}

Note

This check is executed by comparing the input against the [`productInput`](/docs/api/admin-graphql/latest/input-objects/productinput) object, which is specified as part of the mutation argument.

**Note:**

This check is executed by comparing the input against the [`productInput`](/docs/api/admin-graphql/latest/input-objects/productinput) object, which is specified as part of the mutation argument.

---

## [Anchor to Manage concurrent operations](/docs/api/usage/bulk-operations/imports#manage-concurrent-operations)Manage concurrent operations

In API versions `2026-01` and higher, you can run up to 5 bulk mutation operations concurrently per shop. This enables you to import multiple datasets simultaneously without waiting for each operation to complete.

### [Anchor to Run concurrent operations](/docs/api/usage/bulk-operations/imports#run-concurrent-operations)Run concurrent operations

To start a new bulk operation while others are running, call [`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunMutation) again with a different staged upload URL and mutation:

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

mutation {

bulkOperationRunMutation(

mutation: "mutation call($input: ProductInput!) { productCreate(input: $input) { product { id } userErrors { message field } } }",

stagedUploadPath: "tmp/uploads/another-bulk-op.jsonl"

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

Each operation runs independently and returns its own ID. You can track each operation separately using [`bulkOperation(id:)`](/docs/api/admin-graphql/2026-01/queries/bulkOperation) or view all operations together using the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) query.

### [Anchor to View all running operations](/docs/api/usage/bulk-operations/imports#view-all-running-operations)View all running operations

Use the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) query to see all your bulk operations, including those currently running:

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

query {

bulkOperations(first: 10, query: "status:RUNNING type:MUTATION") {

edges {

node {

id

status

createdAt

objectCount

}

}

}

}

This query returns all currently running bulk mutation operations, allowing you to monitor progress across multiple concurrent operations.

For complete details on filtering and pagination, refer to the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) query reference.

---

## [Anchor to Cancel an operation](/docs/api/usage/bulk-operations/imports#cancel-an-operation)Cancel an operation

To cancel an in-progress bulk operation, run the [`bulkOperationCancel`](/docs/api/admin-graphql/latest/mutations/bulkoperationcancel) mutation and supply the operation ID as an input variable:

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

mutation {

bulkOperationCancel(id: "gid://shopify/BulkOperation/1") {

bulkOperation {

status

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

{

"data": {

"bulkOperationCancel": {

"id": "gid://shopify/BulkOperation/1",

"bulkOperation": {

"status": "COMPLETED"

}

}

},

"extensions": {

"cost": {

"requestedQueryCost": 1,

"actualQueryCost": 1

}

}

}

---

## [Anchor to Next steps](/docs/api/usage/bulk-operations/imports#next-steps)Next steps

* Consult our [reference documentation](/docs/api/admin-graphql/latest/objects/BulkOperation) to learn more about creating and managing bulk operations.
* Learn how to use bulk operations to [asynchronously fetch data in bulk](/docs/api/usage/bulk-operations/queries).

---

Was this page helpful?

YesNo