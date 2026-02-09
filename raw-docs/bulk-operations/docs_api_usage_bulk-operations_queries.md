---
source: https://shopify.dev/docs/api/usage/bulk-operations/queries
---

With the GraphQL Admin API, you can use bulk operations to asynchronously fetch data in bulk. The API is designed to reduce complexity when dealing with pagination of large volumes of data. You can bulk query any connection field that's defined by the GraphQL Admin API schema.

Instead of manually paginating results and managing a client-side throttle, you can instead run a bulk query operation. Shopify's infrastructure does the hard work of executing your query, and then provides you with a URL where you can download all of the data.

The GraphQL Admin API supports querying a single top-level field, and then selecting the fields that you want returned. You can also nest connections, such as variants on products.

In API versions `2026-01` and higher apps can run up to five bulk query operations at a time per shop. In API versions prior to `2026-01`, apps are limited to running a single bulk operation at a time per shop. When the operation is complete, the results are delivered in the form of a [JSONL file](http://jsonlines.org/) that Shopify makes available at a URL.

---

## [Anchor to Limitations](/docs/api/usage/bulk-operations/queries#limitations)Limitations

* In API versions `2026-01` and higher, you can run up to five bulk query operations at a time per shop. In API versions prior to `2026-01`, you can run only one bulk operation of each type ([`bulkOperationRunMutation`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunmutation) or [`bulkOperationRunQuery`](/docs/api/admin-graphql/latest/mutations/bulkoperationrunquery)) at a time per shop.
* The bulk query operation has to complete within 10 days. After that it will be stopped and marked as `failed`. When your query runs into this limit, consider reducing the query complexity and depth.
* Bulk operations are only available through the [GraphQL Admin API](/docs/api/admin-graphql). You can't perform bulk operations with the Storefront API.

---

## [Anchor to Access token considerations](/docs/api/usage/bulk-operations/queries#access-token-considerations)Access token considerations

Because bulk query operations can take several days to complete, you should use [offline access tokens](/docs/apps/build/authentication-authorization/access-tokens/offline-access-tokens) when initiating bulk operations. [Online access tokens](/docs/apps/build/authentication-authorization/access-tokens/online-access-tokens) expire after 24 hours, which means they'll expire before long-running bulk operations can complete. Using offline access tokens ensures that your app maintains access to retrieve the results when the operation finishes.

If you're using Admin UI extensions, [Direct API access](/docs/api/admin-extensions#direct-api-access) doesn't support bulk operations. Instead, [connect your extension to your app backend](/docs/apps/build/admin/actions-blocks/connect-app-backend) to initiate and manage bulk operations.

---

## [Anchor to Bulk query overview](/docs/api/usage/bulk-operations/queries#bulk-query-overview)Bulk query overview

The complete flow for running bulk queries is covered [later](#bulk-query-workflow), but below are some small code snippets that you can use to get started quickly.

### [Anchor to Step 1. Submit a query](/docs/api/usage/bulk-operations/queries#step-1-submit-a-query)Step 1. Submit a query

Run a [`bulkOperationRunQuery`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunQuery) mutation and specify what information you want from Shopify.

The following mutation queries the `products` connection and returns each product's ID and title.

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

mutation {

bulkOperationRunQuery(

query: """

{

products {

edges {

node {

id

title

}

}

}

}

"""

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

{

"data": {

"bulkOperationRunQuery": {

"bulkOperation": {

"id": "gid:\/\/shopify\/BulkOperation\/720918",

"status": "CREATED"

},

"userErrors": []

}

},

...

}

### [Anchor to Step 2. Wait for the operation to finish](/docs/api/usage/bulk-operations/queries#step-2-wait-for-the-operation-to-finish)Step 2. Wait for the operation to finish

To retrieve data, you need to wait for the operation to finish. You can determine when a bulk operation has finished by using a webhook or by polling the operation's status.

Tip

Subscribing to the webhook topic is recommended over polling as it limits the number of redundant API calls.

**Tip:**

Subscribing to the webhook topic is recommended over polling as it limits the number of redundant API calls.

#### [Anchor to Option A. Subscribe to the ,[object Object], webhook topic](/docs/api/usage/bulk-operations/queries#option-a-subscribe-to-the-bulk_operations-finish-webhook-topic)Option A. Subscribe to the `bulk_operations/finish` webhook topic

You can use the [webhookSubscriptionCreate](/docs/api/admin-graphql/latest/mutations/webhooksubscriptioncreate) mutation to subscribe to the `bulk_operations/finish` webhook topic in order to receive a webhook when any operation finishes - in other words, it has completed, failed, or been cancelled.

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

After you've subscribed to the webhook topic, Shopify sends a POST request to the specified URL any time a bulk operation on the store (both queries and [mutations](/docs/api/usage/bulk-operations/imports)) finishes.

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

"admin\_graphql\_api\_id": "gid://shopify/BulkOperation/720918",

"completed\_at": "2024-08-29T17:23:25Z",

"created\_at": "2024-08-29T17:16:35Z",

"error\_code": null,

"status": "completed",

"type": "query"

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

node(id: "gid://shopify/BulkOperation/720918") {

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

"url": "https:\/\/storage.googleapis.com\/shopify\/dyfkl3g72empyyoenvmtidlm9o4g?<params />",

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

#### [Anchor to Option B. Poll your operation's status](/docs/api/usage/bulk-operations/queries#option-b-poll-your-operations-status)Option B. Poll your operation's status

While the operation is running, you can poll to see its progress by querying the specific bulk operation using its ID (returned from the `bulkOperationRunQuery` mutation). In API version `2026-01` and higher, use the `bulkOperation(id:)` query. In API versions prior to `2026-01`, use the `currentBulkOperation` query. The `objectCount` field increments to indicate the operation's progress, and the `status` field returns whether the operation is completed.

**API version `2026-01` and higher:**

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

bulkOperation(id: "gid://shopify/BulkOperation/720918") {

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

{

"data": {

"bulkOperation": {

"id": "gid:\/\/shopify\/BulkOperation\/720918",

"status": "COMPLETED",

"errorCode": null,

"createdAt": "2024-08-29T17:16:35Z",

"completedAt": "2024-08-29T17:23:25Z",

"objectCount": "57",

"fileSize": "358",

"url": "https:\/\/storage.googleapis.com\/shopify\/dyfkl3g72empyyoenvmtidlm9o4g?<params />",

"partialDataUrl": null

}

},

...

}

**API versions prior to `2026-01` (using deprecated `currentBulkOperation`):**

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

currentBulkOperation {

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

### [Anchor to Step 3. Retrieve your data](/docs/api/usage/bulk-operations/queries#step-3-retrieve-your-data)Step 3. Retrieve your data

When an operation is completed, a JSONL output file is available for download at the URL specified in the `url` field.
If the query produced no results, then the `url` field will return `null`.

See [Download result data](#download-result-data) for more details on the files we return and [JSONL file format](#the-jsonl-data-format) for how to parse them.

---

## [Anchor to Bulk query workflow](/docs/api/usage/bulk-operations/queries#bulk-query-workflow)Bulk query workflow

Below is the high-level workflow for creating a bulk query:

1. [Identify a potential bulk operation](#identify-a-potential-bulk-query).

   You can use a new or existing query, but it should potentially return a lot of data. Connection-based queries work best.
2. Test the query by using the [Shopify GraphiQL app](https://shopify-graphiql-app.shopifycloud.com).
3. [Write a new mutation document](#write-a-bulk-operation) for `bulkOperationRunQuery`.
4. Include the query as the value for the `query` argument in the mutation.
5. Run the mutation.
6. [Wait for the bulk operation to finish](#wait-for-the-bulk-operation-to-finish) by either:

   1. [Subscribing to a webhook topic](#option-a-use-the-bulk_operations-finish-webhook-topic) that sends a webhook payload when the operation is finished.
   2. [Polling the bulk operation](#option-b-poll-a-running-bulk-operation) until the `status` field shows that the operation is no longer running.

   You can [check the operation's progress](#check-an-operations-progress) using the `objectCount` field in `bulkOperation(id:)` (API version `2026-01` and higher) or `currentBulkOperation` (API versions prior to `2026-01`).
7. Download the JSONL file at the URL provided in the `url` field.

### [Anchor to Identify a potential bulk query](/docs/api/usage/bulk-operations/queries#identify-a-potential-bulk-query)Identify a potential bulk query

Identify a new or existing query that could return a lot of data and would benefit from being a bulk operation. Queries that use pagination to get all pages of results are the most common candidates.

The example query below retrieves some basic information from a store's first 50 products that were created on or after January 1, 2024.

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

{

products(query: "created\_at:>=2024-01-01 AND created\_at:<2024-05-01", first: 50) {

edges {

cursor

node {

id

createdAt

updatedAt

title

handle

descriptionHtml

productType

options {

name

position

values

}

priceRange {

minVariantPrice {

amount

currencyCode

}

maxVariantPrice {

amount

currencyCode

}

}

}

}

pageInfo {

hasNextPage

}

}

}

Tip

Use the [Shopify GraphiQL app](https://shopify-graphiql-app.shopifycloud.com) to run this query against your development store.
The query used in a bulk operation requires the same permissions as it would when run as a normal query, so it's important to run the query first and ensure it succeeds without any access denied errors.

**Tip:**

Use the [Shopify GraphiQL app](https://shopify-graphiql-app.shopifycloud.com) to run this query against your development store.
The query used in a bulk operation requires the same permissions as it would when run as a normal query, so it's important to run the query first and ensure it succeeds without any access denied errors.

### [Anchor to Write a bulk operation](/docs/api/usage/bulk-operations/queries#write-a-bulk-operation)Write a bulk operation

To turn the query above into a bulk query, use the [`bulkOperationRunQuery`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunQuery) mutation. It's easiest to begin with a skeleton mutation without the `query` value:

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

bulkOperationRunQuery(

query:"""

"""

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

* The triple quotes (""") define a multi-line string in GraphQL.
* The bulk operation's ID is returned so you can poll the operation.
* The `userErrors` field is returned to retrieve any error messages.

Paste the original sample query into the mutation, and then make a couple of minor optional changes:

* The `first` argument is optional and ignored if present, so it can be removed.
* The `cursor` and `pageInfo` fields are also optional and ignored if present, so they can be removed.

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

mutation {

bulkOperationRunQuery(

query:"""

{

products(query: "created\_at:>=2024-01-01 AND created\_at:<2024-05-01") {

edges {

node {

id

createdAt

updatedAt

title

handle

descriptionHtml

productType

options {

name

position

values

}

priceRange {

minVariantPrice {

amount

currencyCode

}

maxVariantPrice {

amount

currencyCode

}

}

}

}

}

}

"""

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

If the mutation is successful, then the response looks similar to the example below:

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

{

"data": {

"bulkOperationRunQuery": {

"bulkOperation": {

"id": "gid:\/\/shopify\/BulkOperation\/1",

"status": "CREATED"

},

"userErrors": []

}

},

...

}

### [Anchor to Wait for the bulk operation to finish](/docs/api/usage/bulk-operations/queries#wait-for-the-bulk-operation-to-finish)Wait for the bulk operation to finish

To retrieve data, you need to wait for the operation to finish. You can determine when a bulk operation has finished by using a webhook or by polling the operation's status.

#### [Anchor to Option A. Use the ,[object Object], webhook topic](/docs/api/usage/bulk-operations/queries#option-a-use-the-bulk_operations-finish-webhook-topic)Option A. Use the `bulk_operations/finish` webhook topic

Use the [webhookSubscriptionCreate](/docs/api/admin-graphql/latest/mutations/webhooksubscriptioncreate) mutation to subscribe to the [`bulk_operations/finish`](/docs/api/admin-graphql/latest/enums/webhooksubscriptiontopic) webhook topic. For full setup instructions, refer to [Configuring webhooks](/docs/apps/build/webhooks/subscribe).

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

After you've subscribed, you'll receive a webhook any time a bulk operation on the store (both queries and [mutations](/docs/api/usage/bulk-operations/imports)) finishes (for example, completes, fails, or is cancelled). Refer to the [GraphQL Admin API reference](/docs/api/webhooks?reference=graphql) for details on the webhook payload.

Once you receive the webhook, you must retrieve the bulk operation's data URL by querying the `node` field and passing in the ID given by `admin_graphql_api_id` in the webhook payload:

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

node(id: "gid://shopify/BulkOperation/1") {

... on BulkOperation {

url

partialDataUrl

}

}

}

#### [Anchor to Option B. Poll a running bulk operation](/docs/api/usage/bulk-operations/queries#option-b-poll-a-running-bulk-operation)Option B. Poll a running bulk operation

You can also determine when the bulk operation has finished by querying the specific bulk operation by ID using the `bulkOperation` field:

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

{

bulkOperation(id: "gid://shopify/BulkOperation/1") {

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

You can adjust your polling intervals based on the amount of data that you expect. For example, if you're currently making pagination queries manually and it takes one hour to fetch all product data, then that can serve as a rough estimate for the bulk operation time. In this situation, a polling interval of one minute would probably be better than every 10 seconds.

To learn about the other possible operation statuses, refer to the [`BulkOperationStatus` reference](/docs/api/admin-graphql/latest/enums/bulkoperationstatus).

### [Anchor to Check an operation's progress](/docs/api/usage/bulk-operations/queries#check-an-operations-progress)Check an operation's progress

Although polling is useful for checking whether an operation is complete, you can also use it to check the operation's progress by using the `objectCount` field. This field provides you with a running total of all the objects processed by your bulk operation. You can use the object count to validate your assumptions about how much data should be returned.

9

1

2

3

4

5

6

7

{

bulkOperation(id: "gid://shopify/BulkOperation/1") {

status

objectCount

url

}

}

For example, if you're trying to query all products created in a single month and the object count exceeds your expected number, then it might be a sign that your query conditions are wrong. In that case, you might want to [cancel](#canceling-an-operation) your current operation and run a new one with a different query.

---

## [Anchor to Download result data](/docs/api/usage/bulk-operations/queries#download-result-data)Download result data

Only once an operation is finished running will there be result data available.

If an operation successfully completes, the `url` field will contain a URL where you can download the data. If an operation fails but some data was retrieved before the failure occurred, then a partially complete output file is available at the URL specified in the `partialDataUrl` field.
In either case, the URLs return will be signed (authenticated) and will expire after one week.

Now that you've downloaded the data, it's time to parse it according to the JSONL format.

---

## [Anchor to The JSONL data format](/docs/api/usage/bulk-operations/queries#the-jsonl-data-format)The JSONL data format

Normal (non-bulk) GraphQL responses are JSON. The response structure mirrors the query structure, which results in a single JSON object with many nested objects. Most standard JSON parsers require the entire string or file to be read into memory, which can cause issues when the responses are large.

Since bulk operations are specifically designed to fetch large datasets, we've chosen the [JSON Lines](http://jsonlines.org/) (JSONL) format for the response data so that clients have more flexibility in how they consume the data. JSONL is similar to JSON, but each line is its own valid JSON object. To avoid issues with memory consumption, the file can be parsed one line at a time by using file streaming functionality, which most languages have.

Each line in the file is a node object returned in a connection. If a node has a nested connection, then each child node is extracted into its own object on the next line. For example, a bulk operation might use the following query to retrieve a list of products and their nested variants:

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

{

products {

edges {

node {

id

variants {

edges {

node {

id

title

}

}

}

}

}

}

}

In the JSONL results, each product object is followed by each of its variant objects on a new line. The order of each connection type is preserved and all nested connections appear after their parents in the file. Because connections are no longer nested in the response data structure, the bulk operation result automatically includes the `__parentId` field, which is a reference to an object's parent. This field doesn't exist in the API schema, so you can't explicitly query it.

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

{"id":"gid://shopify/Product/1921569226808"}

{"id":"gid://shopify/ProductVariant/19435458986123","title":"52","\_\_parentId":"gid://shopify/Product/1921569226808"}

{"id":"gid://shopify/ProductVariant/19435458986040","title":"70","\_\_parentId":"gid://shopify/Product/1921569226808"}

{"id":"gid://shopify/Product/1921569259576"}

{"id":"gid://shopify/ProductVariant/19435459018808","title":"34","\_\_parentId":"gid://shopify/Product/1921569259576"}

{"id":"gid://shopify/Product/1921569292344"}

{"id":"gid://shopify/ProductVariant/19435459051576","title":"Default Title","\_\_parentId":"gid://shopify/Product/1921569292344"}

{"id":"gid://shopify/Product/1921569325112"}

{"id":"gid://shopify/ProductVariant/19435459084344","title":"36","\_\_parentId":"gid://shopify/Product/1921569325112"}

{"id":"gid://shopify/Product/1921569357880"}

{"id":"gid://shopify/ProductVariant/19435459117112","title":"47","\_\_parentId":"gid://shopify/Product/1921569357880"}

### [Anchor to Example](/docs/api/usage/bulk-operations/queries#example)Example

Most programming languages have the ability to read a file one line at a time to avoid reading the entire file into memory. This feature should be taken advantage of when dealing with the JSONL data files.

Here's a simple example in Ruby to demonstrate the proper way of loading and parsing a JSONL file:

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

# Efficient: reads the file a single line at a time

File.open(file) do |f|

f.each do |line|

JSON.parse(line)

end

end

# Inefficient: reads the entire file into memory

jsonl = File.read(file)

jsonl.each\_line do |line|

JSON.parse(line)

end

To demonstrate the difference using a 100MB JSONL file, the "good" version would consume only 2.5MB of memory while the "bad" version would consume 100MB (equal to the file size).

Other languages:

* NodeJS: [`readline`](https://nodejs.org/api/readline.html#readline_example_read_file_stream_line_by_line)
* Python: [built-in iterator](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)
* PHP: [`fgets`](https://www.php.net/manual/en/function.fgets.php)

---

## [Anchor to Operation failures](/docs/api/usage/bulk-operations/queries#operation-failures)Operation failures

Bulk operations can fail for any of the reasons that a regular GraphQL query would fail, such as not having permission to query a field. For this reason, we encourage you to run the query normally first to make sure that it works. You'll get much better error feedback than when a query fails within a bulk operation.

When a bulk operation fails, [some data might be available to download](#download-result-data), the `status` field returns `FAILED`, and the `errorCode` field includes one of the following codes:

* `ACCESS_DENIED`: there are missing access scopes. Run the query normally (outside of a bulk operation) to get more details on which field is causing the issue.
* `INTERNAL_SERVER_ERROR`: something went wrong on our server and we've been notified of the error. These errors might be intermittent, so you can try [submitting the query again](#step-1-submit-a-query).
* `TIMEOUT`: one or more query timeouts occurred during execution. Try removing some fields from your query so that it can run successfully. These timeouts might be intermittent, so you can try [submitting the query again](#step-1-submit-a-query).

Tip

Querying resources using a [range search](/docs/api/usage/search-syntax#search-query-syntax) might timeout or return an error if the collection of resources is sufficiently large, and the search field is different from the specified (or default) sort key for the connection you are querying. If your query is slow or returns an error, then try specifying a sort key that matches the field used in the search. For example, `query: "created_at:>2024-05-01", sortKey: CREATED_AT`.

**Tip:**

Querying resources using a [range search](/docs/api/usage/search-syntax#search-query-syntax) might timeout or return an error if the collection of resources is sufficiently large, and the search field is different from the specified (or default) sort key for the connection you are querying. If your query is slow or returns an error, then try specifying a sort key that matches the field used in the search. For example, `query: "created_at:>2024-05-01", sortKey: CREATED_AT`.

To learn about the other possible operation error codes, refer to the [`BulkOperationErrorCode`](/docs/api/admin-graphql/latest/enums/BulkOperationErrorCode) reference.

### [Anchor to Canceled operations](/docs/api/usage/bulk-operations/queries#canceled-operations)Canceled operations

If bulk operations have stalled, then they might be canceled by Shopify. After bulk operations are canceled, a `status` of `CANCELED` is returned. You can retry canceled bulk operations by [submitting the query again](#step-1-submit-a-query).

Note

When using the `bulk_operations/finish` webhook, the `error_code` and `status` fields in the webhook payload will be lowercase. For example, `failed` instead of `FAILED`.

**Note:**

When using the `bulk_operations/finish` webhook, the `error_code` and `status` fields in the webhook payload will be lowercase. For example, `failed` instead of `FAILED`.

---

## [Anchor to Canceling an operation](/docs/api/usage/bulk-operations/queries#canceling-an-operation)Canceling an operation

To cancel an in-progress bulk operation, use the [`bulkOperationCancel`](/docs/api/admin-graphql/latest/mutations/bulkOperationCancel) mutation with the operation ID.

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

---

## [Anchor to Rate limits](/docs/api/usage/bulk-operations/queries#rate-limits)Rate limits

You can run only one bulk operation of each type (`bulkOperationRunMutation` or `bulkOperationRunQuery`) at a time per shop. This limit is in place because operations are asynchronous and long-running. To run a subsequent bulk operation for a shop, you need to either cancel the running operation or wait for it to finish.

### [Anchor to How bulk operations fit within the Admin API rate limits](/docs/api/usage/bulk-operations/queries#how-bulk-operations-fit-within-the-admin-api-rate-limits)How bulk operations fit within the Admin API rate limits

Bulk operations are initiated by you, the API consumer, by supplying a `query` string within the `bulkOperationRunQuery` mutation. Shopify then executes that `query` string asynchronously as a bulk operation.

This distinction between the `bulkOperationRunQuery` mutation and the bulk query string itself determines how rate limits apply as well: any GraphQL requests made by you count as normal API requests and are subject to [rate limits](/docs/api/usage/limits#rate-limits#graphql-admin-api-rate-limits), while the bulk operation query execution is not.

In the following example, you would be charged the cost of the mutation request (as with any other mutation), but not for the `query` for product titles that you want Shopify to run as a bulk operation:

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

mutation {

bulkOperationRunQuery(

query: """

{

products {

edges {

node {

title

}

}

}

}

"""

) {

bulkOperation {

id

}

}

}

Since you're only making low-cost requests for creating operations, polling their status, or canceling them, bulk operations are a very efficient way to query data compared to standard pagination queries.

### [Anchor to Manage concurrent operations](/docs/api/usage/bulk-operations/queries#manage-concurrent-operations)Manage concurrent operations

In API versions `2026-01` and higher, you can run up to five bulk query operations concurrently per shop. This enables you to process multiple large datasets simultaneously without waiting for each operation to complete.

#### [Anchor to Run concurrent operations](/docs/api/usage/bulk-operations/queries#run-concurrent-operations)Run concurrent operations

To start a new bulk operation while others are running, call [`bulkOperationRunQuery`](/docs/api/admin-graphql/latest/mutations/bulkOperationRunQuery) again with a different query:

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

mutation {

bulkOperationRunQuery(

query: """

{

products {

edges {

node {

id

title

variants {

edges {

node {

id

sku

}

}

}

}

}

}

}

"""

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

#### [Anchor to View all running operations](/docs/api/usage/bulk-operations/queries#view-all-running-operations)View all running operations

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

bulkOperations(first: 10, query: "status:RUNNING type:QUERY") {

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

This query returns all currently running bulk query operations, allowing you to monitor progress across multiple concurrent operations.

### [Anchor to Listing and filtering bulk operations](/docs/api/usage/bulk-operations/queries#listing-and-filtering-bulk-operations)Listing and filtering bulk operations

In API version `2026-01` and higher, you can use the `bulkOperations` query to list, filter, and paginate your bulk operations. This replaces the deprecated `currentBulkOperation` query.

The new query provides:

* **Filtering** by status (completed, running, failed, etc.) and operation type (query or mutation)
* **Sorting** by creation date, completion date, status, or ID
* **Pagination** with cursor-based navigation
* **Direct lookup** of specific operations by ID using `bulkOperation(id:)`

For complete details, refer to the [`bulkOperations`](/docs/api/admin-graphql/2026-01/queries/bulkOperations) query reference.

---

## [Anchor to Operation restrictions](/docs/api/usage/bulk-operations/queries#operation-restrictions)Operation restrictions

A bulk operation query needs to include a connection. If your query doesn't use a connection, then it should be executed as a normal synchronous GraphQL query.

Bulk operations have some additional restrictions:

* Maximum of five total connections in the query.
* Connections must implement the [`Node`](/docs/api/storefront/latest/interfaces/Node) interface
* The top-level `node` and `nodes` fields can't be used.
* Maximum of two levels deep for nested connections. For example, the following is invalid because there are three levels of nested connections:

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

{

products {

edges {

node {

id

variants { # nested level 1

edges {

node {

id

images { # nested level 2

edges {

node {

id

metafields { # nested level 3 (invalid)

edges {

node {

value

}

}

}

}

}

}

}

}

}

}

}

}

}

The `bulkOperationRunQuery` mutation will validate the supplied queries and provide errors by using the `userErrors` field.

It's hard to provide exhaustive examples of what's allowed and what isn't given the flexibility of GraphQL queries, so try some and see what works and what doesn't. If you find useful queries which aren't yet supported, then let us know on the [.dev Community](https://community.shopify.dev/) so we can collect common use cases.

---

## [Anchor to Next steps](/docs/api/usage/bulk-operations/queries#next-steps)Next steps

* Consult our [reference documentation](/docs/api/admin-graphql/latest/objects/BulkOperation) to learn more about creating and managing bulk operations.
* Learn how [bulk import large volumes of data asynchronously](/docs/api/usage/bulk-operations/imports).

---

Was this page helpful?

YesNo