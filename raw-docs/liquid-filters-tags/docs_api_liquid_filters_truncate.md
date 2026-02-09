---
source: https://shopify.dev/docs/api/liquid/filters/truncate
---

9

1

string | truncate: number

returns [string](/docs/api/liquid/basics#string)

Truncates a string down to a given number of characters.

If the specified number of characters is less than the length of the string, then an ellipsis (`...`) is appended to
the truncated string. The ellipsis is included in the character count of the truncated string.

9

1

{{ article.title | truncate: 15 }}

##### Code

```liquid
{{ article.title | truncate: 15 }}
```

##### Data

```liquid
{
  "article": {
    "title": "How to tell if you're out of invisibility potion"
  }
}
```

## Output

9

1

How to tell ...

##### Output

```liquid
How to tell ...
```

[Anchor to Specify a custom ellipsis](/docs/api/liquid/filters/truncate#truncate-specify-a-custom-ellipsis)

### Specify a custom ellipsis

9

1

string | truncate: number, string

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

9

1

2

{{ article.title | truncate: 15, '--' }}

{{ article.title | truncate: 15, '' }}

##### Code

```liquid
{{ article.title | truncate: 15, '--' }}
{{ article.title | truncate: 15, '' }}
```

##### Data

```liquid
{
  "article": {
    "title": "How to tell if you're out of invisibility potion"
  }
}
```

## Output

9

1

2

How to tell i--

How to tell if

##### Output

```liquid
How to tell i--
How to tell if
```

Was this page helpful?

YesNo