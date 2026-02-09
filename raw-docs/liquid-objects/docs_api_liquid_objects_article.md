---
source: https://shopify.dev/docs/api/liquid/objects/article
---

An article, or [blog post](https://help.shopify.com/manual/online-store/blogs/writing-blogs), in a blog.

## Properties

[Anchor to](/docs/api/liquid/objects/article#article-author) 

author**author** [string](/docs/api/liquid/basics#string)

:   The full name of the author of the article.

[Anchor to](/docs/api/liquid/objects/article#article-comment_post_url) 

comment\_post\_url**comment\_post\_url** [string](/docs/api/liquid/basics#string)

:   The relative URL where POST requests are sent when creating new comments.

[Anchor to](/docs/api/liquid/objects/article#article-comments) 

comments**comments** array of [comment](/docs/api/liquid/objects/comment)

:   The published comments for the article.

    Returns an empty array if comments are disabled.

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many comments to show at once, up to a limit of 50.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many comments to show at once, up to a limit of 50.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many comments to show at once, up to a limit of 50.

[Anchor to](/docs/api/liquid/objects/article#article-comments_count) 

comments\_count**comments\_count** [number](/docs/api/liquid/basics#number)

:   The number of published comments for the article.

[Anchor to](/docs/api/liquid/objects/article#article-comments_enabled?) 

comments\_enabled?**comments\_enabled?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if comments are enabled. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/article#article-content) 

content**content** [string](/docs/api/liquid/basics#string)

:   The content of the article.

[Anchor to](/docs/api/liquid/objects/article#article-created_at) 

created\_at**created\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the article was created.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/article#article-excerpt) 

excerpt**excerpt** [string](/docs/api/liquid/basics#string)

:   The excerpt of the article.

[Anchor to](/docs/api/liquid/objects/article#article-excerpt_or_content) 

excerpt\_or\_content**excerpt\_or\_content** [string](/docs/api/liquid/basics#string)

:   Returns the article [excerpt](/docs/api/liquid/objects/article#article-excerpt) if it exists. Returns the article
    [content](/docs/api/liquid/objects/article#article-content) if no excerpt exists.

[Anchor to](/docs/api/liquid/objects/article#article-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the article.

[Anchor to](/docs/api/liquid/objects/article#article-id) 

id**id** [string](/docs/api/liquid/basics#string)

:   The ID of the article.

[Anchor to](/docs/api/liquid/objects/article#article-image) 

image**image** [image](/docs/api/liquid/objects/image)

:   The featured image for the article.

[Anchor to](/docs/api/liquid/objects/article#article-metafields) 

metafields**metafields**

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the article.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/article#article-moderated?) 

moderated?**moderated?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the blog that the article belongs to is set to [moderate comments](https://help.shopify.com/manual/online-store/blogs/managing-comments).
    Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/article#article-published_at) 

published\_at**published\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the article was published.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/article#article-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   The tags applied to the article.

    ![](/images/icons/32/lightbulbscroll.png)![](/images/icons/32/lightbulbscroll-dark.png)

    Example

    Show the total tag count

    When looping through `article.tags`, you can print how many times a tag is used with `tag.total_count`. This number shows visitors how many blog posts have been tagged with a particular tag.

    9

    1

    2

    3

    {% for tag in article.tags -%}

    {{ tag }} ({{ tag.total\_count }})

    {%- endfor %}

    ##### Code

    ```liquid
    {% for tag in article.tags -%}
      {{ tag }} ({{ tag.total_count }})
    {%- endfor %}
    ```

    ##### Data

    ```liquid
    {
      "article": {
        "tags": [
          "clear potions",
          "potion troubleshooting",
          "tips"
        ]
      }
    }
    ```

    ## Output

    9

    1

    clear potions (1)potion troubleshooting (2)tips (2)

    ##### Output

    ```liquid
    clear potions (1)potion troubleshooting (2)tips (2)
    ```

[Anchor to](/docs/api/liquid/objects/article#article-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) assigned to the article.

    The name doesn't include the `article.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the article, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/article#article-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the article.

[Anchor to](/docs/api/liquid/objects/article#article-updated_at) 

updated\_at**updated\_at** [string](/docs/api/liquid/basics#string)

:   A timestamp for when the article was updated.

    Tip

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:**

    Use the [`date` filter](/docs/api/liquid/filters/date) to format the timestamp.

    **Tip:** Use the <a href="/docs/api/liquid/filters/date"><code>date</code> filter</a> to format the timestamp.

[Anchor to](/docs/api/liquid/objects/article#article-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the article.

[Anchor to](/docs/api/liquid/objects/article#article-user) 

user**user** [user](/docs/api/liquid/objects/user)

:   The user associated with the author of the article.

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

{

"author": "Polina Waters",

"comment\_post\_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments",

"comments": [],

"comments\_count": 1,

"comments\_enabled?": true,

"content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",

"created\_at": "2022-04-14 16:56:02 -0400",

"excerpt": "And where to buy <strong>more</strong>!",

"excerpt\_or\_content": "And where to buy <strong>more</strong>!",

"handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion",

"id": 556510085185,

"image": {},

"metafields": {},

"moderated?": true,

"published\_at": "2022-04-14 16:56:02 -0400",

"tags": [],

"template\_suffix": "",

"title": "How to tell if you're out of invisibility potion",

"updated\_at": "2022-06-04 19:27:33 -0400",

"url": {},

"user": {}

}

##### Example

```liquid
{
  "author": "Polina Waters",
  "comment_post_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments",
  "comments": [],
  "comments_count": 1,
  "comments_enabled?": true,
  "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",
  "created_at": "2022-04-14 16:56:02 -0400",
  "excerpt": "And where to buy <strong>more</strong>!",
  "excerpt_or_content": "And where to buy <strong>more</strong>!",
  "handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion",
  "id": 556510085185,
  "image": {},
  "metafields": {},
  "moderated?": true,
  "published_at": "2022-04-14 16:56:02 -0400",
  "tags": [],
  "template_suffix": "",
  "title": "How to tell if you're out of invisibility potion",
  "updated_at": "2022-06-04 19:27:33 -0400",
  "url": {},
  "user": {}
}
```

[Anchor to](/docs/api/liquid/objects/article#template-using) 

## Templates using article

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturearticle template

Theme architecture

article template](/themes/architecture/templates/article)

Was this section helpful?

YesNo