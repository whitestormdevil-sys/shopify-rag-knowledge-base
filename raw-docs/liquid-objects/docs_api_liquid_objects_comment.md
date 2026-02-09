---
source: https://shopify.dev/docs/api/liquid/objects/comment
---

An article comment.

## Properties

[Anchor to](/docs/api/liquid/objects/comment#comment-author) 

author**author** [string](/docs/api/liquid/basics#string)

:   The full name of the author of the comment.

[Anchor to](/docs/api/liquid/objects/comment#comment-content) 

content**content** [string](/docs/api/liquid/basics#string)

:   The content of the comment.

[Anchor to](/docs/api/liquid/objects/comment#comment-created_at) 

created\_at**created\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the comment was created.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/comment#comment-email) 

email**email** [string](/docs/api/liquid/basics#string)

:   The email of he author of the comment.

[Anchor to](/docs/api/liquid/objects/comment#comment-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the comment.

[Anchor to](/docs/api/liquid/objects/comment#comment-status) 

status**status** [string](/docs/api/liquid/basics#string)

:   The status of the comment. Always returns `published`.

    Outside of the Liquid context, the status of a comment can vary based on spam detection and whether blog comments are
    moderated. However, only comments with a status of `published` are included in the [`article.comments` array](/docs/api/liquid/objects/article#article-comments).

    Tip

    To learn more about blog comments, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/blogs/managing-comments).

    **Tip:**

    To learn more about blog comments, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/blogs/managing-comments).

    **Tip:** To learn more about blog comments, visit the <a href="https://help.shopify.com/manual/online-store/blogs/managing-comments">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/comment#comment-updated_at) 

updated\_at**updated\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the status of the comment was last updated.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/comment#comment-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the article that the comment is associated with, with [`comment.id`](/docs/api/liquid/objects/comment#comment-id)
    appended.

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

{

"author": "Cornelius",

"content": "Wow, this is going to save me a fortune in invisibility potion!",

"created\_at": "2022-06-05 19:33:57 -0400",

"email": "cornelius.potionmaker@gmail.com",

"id": 129089273921,

"status": "published",

"updated\_at": "2022-06-05 19:33:57 -0400",

"url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion#129089273921"

}

##### Example

```liquid
{
  "author": "Cornelius",
  "content": "Wow, this is going to save me a fortune in invisibility potion!",
  "created_at": "2022-06-05 19:33:57 -0400",
  "email": "cornelius.potionmaker@gmail.com",
  "id": 129089273921,
  "status": "published",
  "updated_at": "2022-06-05 19:33:57 -0400",
  "url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion#129089273921"
}
```

Was this section helpful?

YesNo