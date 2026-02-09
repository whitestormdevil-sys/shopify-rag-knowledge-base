---
source: https://shopify.dev/docs/api/liquid/filters/date
---

9

1

string | date: string

returns [string](/docs/api/liquid/basics#string)

Converts a timestamp into another date format.

The `date` filter accepts the same parameters as Ruby's strftime method for formatting the date. For a list of shorthand
formats, refer to the [Ruby documentation](https://ruby-doc.org/core-3.1.1/Time.html#method-i-strftime) or
[strftime reference and sandbox](http://www.strfti.me/).

9

1

{{ article.created\_at | date: '%B %d, %Y' }}

##### Code

```liquid
{{ article.created_at | date: '%B %d, %Y' }}
```

##### Data

```liquid
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

## Output

9

1

April 14, 2022

##### Output

```liquid
April 14, 2022
```

[Anchor to The current date](/docs/api/liquid/filters/date#date-the-current-date)

### The current date

You can apply the `date` filter to the keywords `'now'` and `'today'` to output the current timestamp.

---

Note

The timestamp will reflect the time that the Liquid was last rendered. Because of this, the timestamp might not be updated for every page view, depending on the context and caching.

**Note:**

The timestamp will reflect the time that the Liquid was last rendered. Because of this, the timestamp might not be updated for every page view, depending on the context and caching.

**Note:** The timestamp will reflect the time that the Liquid was last rendered. Because of this, the timestamp might not be updated for every page view, depending on the context and caching.

---

9

1

{{ 'now' | date: '%B %d, %Y' }}

##### Code

```liquid
{{ 'now' | date: '%B %d, %Y' }}
```

##### Data

## Output

9

1

##### Output

[Anchor to format](/docs/api/liquid/filters/date#date-format)

### format

9

1

string | date: format: string

Specify a locale-aware date format. You can use the following formats:

* `abbreviated_date`
* `basic`
* `date`
* `date_at_time`
* `default`
* `on_date`
* `short` (deprecated)
* `long` (deprecated)

---

Note

You can also [define custom formats](/docs/api/liquid/filters/date-setting-format-options-in-locale-files) in your theme's locale files.

**Note:**

You can also [define custom formats](/docs/api/liquid/filters/date-setting-format-options-in-locale-files) in your theme's locale files.

**Note:** You can also <a href="/docs/api/liquid/filters/date-setting-format-options-in-locale-files">define custom formats</a> in your theme&#39;s locale files.

---

9

1

{{ article.created\_at | date: format: 'abbreviated\_date' }}

##### Code

```liquid
{{ article.created_at | date: format: 'abbreviated_date' }}
```

##### Data

```liquid
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

## Output

9

1

Apr 14, 2022

##### Output

```liquid
Apr 14, 2022
```

[Anchor to Setting format options in locale files](/docs/api/liquid/filters/date#date-setting-format-options-in-locale-files)

### Setting format options in locale files

You can define custom date formats in your [theme's storefront locale files](/themes/architecture/locales/storefront-locale-files). These custom formats should be included in a `date_formats` category:

9

1

2

3

"date\_formats": {

"month\_day\_year": "%B %d, %Y"

}

```liquid
"date_formats": {
  "month_day_year": "%B %d, %Y"
}
```

9

1

{{ article.created\_at | date: format: 'month\_day\_year' }}

##### Code

```liquid
{{ article.created_at | date: format: 'month_day_year' }}
```

##### Data

```liquid
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

## Output

9

1

April 14, 2022

##### Output

```liquid
April 14, 2022
```

Was this page helpful?

YesNo