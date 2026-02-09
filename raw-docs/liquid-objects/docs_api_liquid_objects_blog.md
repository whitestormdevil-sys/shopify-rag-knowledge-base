---
source: https://shopify.dev/docs/api/liquid/objects/blog
---

Information about a specific [blog](https://help.shopify.com/manual/online-store/blogs/adding-a-blog) in the store.

## Properties

[Anchor to](/docs/api/liquid/objects/blog#blog-all_tags) 

all\_tags**all\_tags** array of [string](/docs/api/liquid/basics#string)

:   All of the tags on the articles in the blog.

    This includes tags of articles that aren't in the current pagination view.

[Anchor to](/docs/api/liquid/objects/blog#blog-articles) 

articles**articles** array of [article](/docs/api/liquid/objects/article)

:   The articles in the blog.

    Tip

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many articles to show per page, up to a limit of 50.

    **Tip:**

    Use the [paginate](/docs/api/liquid/tags/paginate) tag to choose how many articles to show per page, up to a limit of 50.

    **Tip:** Use the <a href="/docs/api/liquid/tags/paginate">paginate</a> tag to choose how many articles to show per page, up to a limit of 50.

[Anchor to](/docs/api/liquid/objects/blog#blog-articles_count) 

articles\_count**articles\_count** [number](/docs/api/liquid/basics#number)

:   The total number of articles in the blog. This total doesn't include hidden articles.

[Anchor to](/docs/api/liquid/objects/blog#blog-comments_enabled?) 

comments\_enabled?**comments\_enabled?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if comments are enabled for the blog. Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/blog#blog-handle) 

handle**handle** [string](/docs/api/liquid/basics#string)

:   The [handle](/docs/api/liquid/basics#handles) of the blog.

[Anchor to](/docs/api/liquid/objects/blog#blog-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the blog.

[Anchor to](/docs/api/liquid/objects/blog#blog-metafields) 

metafields**metafields** array of [metafield](/docs/api/liquid/objects/metafield)

:   The [metafields](/docs/api/liquid/objects/metafield) applied to the blog.

    Tip

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:**

    To learn about how to create metafields, refer to [Create and manage metafields](/apps/metafields/manage) or visit
    the [Shopify Help Center](https://help.shopify.com/manual/metafields).

    **Tip:** To learn about how to create metafields, refer to <a href="/apps/metafields/manage">Create and manage metafields</a> or visit
    the <a href="https://help.shopify.com/manual/metafields">Shopify Help Center</a>.

[Anchor to](/docs/api/liquid/objects/blog#blog-moderated?) 

moderated?**moderated?** [boolean](/docs/api/liquid/basics#boolean)

:   Returns `true` if the blog is set to
    [moderate comments](https://help.shopify.com/manual/online-store/blogs/managing-comments). Returns `false` if not.

[Anchor to](/docs/api/liquid/objects/blog#blog-next_article) 

next\_article**next\_article** [article](/docs/api/liquid/objects/article)

:   The next (older) article in the blog.

    Returns `nil` if there is no next article.

    This property can be used on the [article page](/themes/architecture/templates/article) to output `next` links.

[Anchor to](/docs/api/liquid/objects/blog#blog-previous_article) 

previous\_article**previous\_article** [article](/docs/api/liquid/objects/article)

:   The previous (newer) article in the blog.

    Returns `nil` if there is no previous article.

    This property can be used on the [article page](/themes/architecture/templates/article) to output `previous` links.

[Anchor to](/docs/api/liquid/objects/blog#blog-tags) 

tags**tags** array of [string](/docs/api/liquid/basics#string)

:   A list of all of the tags on all of the articles in the blog.

    Unlike [`blog.all_tags`](/docs/api/liquid/objects/blog#blog-all_tags), this property only returns tags of articles that are in the
    filtered view.

[Anchor to](/docs/api/liquid/objects/blog#blog-template_suffix) 

template\_suffix**template\_suffix** [string](/docs/api/liquid/basics#string)

:   The name of the [custom template](/themes/architecture/templates#alternate-templates) assigned to the blog.

    The name doesn't include the `blog.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the blog, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/blog#blog-title) 

title**title** [string](/docs/api/liquid/basics#string)

:   The title of the blog.

[Anchor to](/docs/api/liquid/objects/blog#blog-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL of the blog.

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

"all\_tags": [],

"articles": [],

"articles\_count": 3,

"comments\_enabled?": true,

"handle": "potion-notions",

"id": 78580613185,

"metafields": {},

"moderated?": true,

"next\_article": {},

"previous\_article": {},

"tags": [],

"template\_suffix": "",

"title": "Potion Notions",

"url": "/blogs/potion-notions"

}

##### Example

```liquid
{
  "all_tags": [],
  "articles": [],
  "articles_count": 3,
  "comments_enabled?": true,
  "handle": "potion-notions",
  "id": 78580613185,
  "metafields": {},
  "moderated?": true,
  "next_article": {},
  "previous_article": {},
  "tags": [],
  "template_suffix": "",
  "title": "Potion Notions",
  "url": "/blogs/potion-notions"
}
```

[Anchor to](/docs/api/liquid/objects/blog#template-using) 

## Templates using blog

[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architectureblog template

Theme architecture

blog template](/themes/architecture/templates/blog)[![](/images/icons/32/themes.png)![](/images/icons/32/themes-dark.png)

Theme architecturearticle template

Theme architecture

article template](/themes/architecture/templates/article)

Was this section helpful?

YesNo