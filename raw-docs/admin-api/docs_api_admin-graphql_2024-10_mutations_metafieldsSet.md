---
source: https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/metafieldsSet
---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

Requires the same access level needed to mutate the owner resource. For instance, if you want to set
a metafield on a product, you need the same permissions as you would need to mutate a product.

Sets metafield values. Metafield values will be set regardless if they were previously created or not.

Allows a maximum of 25 metafields to be set at a time, with a maximum total request payload size of 10MB.

This operation is atomic, meaning no changes are persisted if an error is encountered.

As of `2024-07`, this operation supports compare-and-set functionality to better handle concurrent requests.
If `compareDigest` is set for any metafield, the mutation will only set that metafield if the persisted metafield value matches the digest used on `compareDigest`.
If the metafield doesn't exist yet, but you want to guarantee that the operation will run in a safe manner, set `compareDigest` to `null`.
The `compareDigest` value can be acquired by querying the metafield object and selecting `compareDigest` as a field.
If the `compareDigest` value does not match the digest for the persisted value, the mutation will return an error.
You can opt out of write guarantees by not sending `compareDigest` in the request.

* metafields ([MetafieldsSetInput!]!)

[Anchor to metafields](/docs/api/admin-graphql/latest/mutations/metafieldsSet#arguments-metafields)metafields •[[MetafieldsSetInput!]!](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput) required
:   The list of metafield values to set. Maximum of 25.

    Show input fields

---

Was this section helpful?

YesNo

## [Anchor to MetafieldsSetPayload returns](/docs/api/admin-graphql/latest/mutations/metafieldsSet#returns)MetafieldsSetPayload returns

* metafields ([Metafield!])
* userErrors ([MetafieldsSetUserError!]!)

[Anchor to metafields](/docs/api/admin-graphql/latest/mutations/metafieldsSet#returns-metafields)metafields •[[Metafield!]](/docs/api/admin-graphql/latest/objects/Metafield)
:   The list of metafields that were set.

    Show fields

[Anchor to userErrors](/docs/api/admin-graphql/latest/mutations/metafieldsSet#returns-userErrors)userErrors •[[MetafieldsSetUserError!]!](/docs/api/admin-graphql/latest/objects/MetafieldsSetUserError) non-null
:   The list of errors that occurred from executing the mutation.

    Show fields

---

Was this section helpful?

YesNo