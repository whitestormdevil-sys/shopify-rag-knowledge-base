---
source: https://shopify.dev/docs/api/liquid/tags/comment
---

Prevents an expression from being rendered or output.

Any text inside `comment` tags won't be output, and any Liquid code will be parsed, but not executed.

## Syntax

9

1

2

3

{% comment %}

content

{% endcomment %}

content

The content of the comment.

[Anchor to Inline comments](/docs/api/liquid/tags/comment#comment-inline-comments)

### Inline comments

## Syntax

9

1

{% # content %}

Inline comments prevent an expression inside of a tag `{% %}` from being rendered or output.

You can use inline comment tags to annotate your code, or to temporarily prevent logic in your code from executing.

You can create multi-line inline comments. However, each line in the tag must begin with a `#`, or a syntax error will occur.

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

{% # this is a comment %}

{% # for i in (1..3) -%}

{{ i }}

{% # endfor %}

{%

###############################

# This is a comment

# across multiple lines

###############################

%}

##### Code

```liquid
{% # this is a comment %}

{% # for i in (1..3) -%}
  {{ i }}
{% # endfor %}

{%
  ###############################
  # This is a comment
  # across multiple lines
  ###############################
%}
```

## Output

9

1

##### Output

[Anchor to Inline comments inside `liquid` tags](/docs/api/liquid/tags/comment#comment-inline-comments-inside-liquid-tags)

### Inline comments inside `liquid` tags

You can use inline comment tags inside [`liquid` tags](/docs/api/liquid/tags/liquid). The tag must be used for each line that you want to comment.

9

1

2

3

4

5

{% liquid

# this is a comment

assign topic = 'Learning about comments!'

echo topic

%}

##### Code

```liquid
{% liquid
  # this is a comment
  assign topic = 'Learning about comments!'
  echo topic
%}
```

## Output

9

1

Learning about comments!

##### Output

```liquid
Learning about comments!
```

Was this page helpful?

YesNo