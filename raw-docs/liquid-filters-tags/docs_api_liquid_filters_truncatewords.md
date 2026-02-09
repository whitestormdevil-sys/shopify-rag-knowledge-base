---
source: https://shopify.dev/docs/api/liquid/filters/truncatewords
---

9

1

string | truncatewords: number

returns [string](/docs/api/liquid/basics#string)

Truncates a string down to a given number of words.

If the specified number of words is less than the number of words in the string, then an ellipsis (`...`) is appended to
the truncated string.

---

Caution

HTML tags are treated as words, so you should strip any HTML from truncated content. If you don't strip HTML, then
closing HTML tags can be removed, which can result in unexpected behavior.

**Caution:**

HTML tags are treated as words, so you should strip any HTML from truncated content. If you don't strip HTML, then
closing HTML tags can be removed, which can result in unexpected behavior.

**Caution:** HTML tags are treated as words, so you should strip any HTML from truncated content. If you don&#39;t strip HTML, then
closing HTML tags can be removed, which can result in unexpected behavior.

---

9

1

{{ article.content | strip\_html | truncatewords: 15 }}

##### Code

```liquid
{{ article.content | strip_html | truncatewords: 15 }}
```

##### Data

```liquid
{
  "article": {
    "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>"
  }
}
```

## Output

9

1

We've all had this problem before: we peek into the potions vault to determine which...

##### Output

```liquid
We've all had this problem before: we peek into the potions vault to determine which...
```

[Anchor to Specify a custom ellipsis](/docs/api/liquid/filters/truncatewords#truncatewords-specify-a-custom-ellipsis)

### Specify a custom ellipsis

9

1

string | truncatewords: number, string

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

9

1

2

3

{{ article.content | strip\_html | truncatewords: 15, '--' }}

{{ article.content | strip\_html | truncatewords: 15, '' }}

##### Code

```liquid
{{ article.content | strip_html | truncatewords: 15, '--' }}

{{ article.content | strip_html | truncatewords: 15, '' }}
```

##### Data

```liquid
{
  "article": {
    "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>"
  }
}
```

## Output

9

1

2

3

We've all had this problem before: we peek into the potions vault to determine which--

We've all had this problem before: we peek into the potions vault to determine which

##### Output

```liquid
We've all had this problem before: we peek into the potions vault to determine which--

We've all had this problem before: we peek into the potions vault to determine which
```

Was this page helpful?

YesNo