---
source: https://shopify.dev/docs/api/liquid/tags/liquid
---

Allows you to have a block of Liquid without delimeters on each tag.

Because the tags don't have delimeters, each tag needs to be on its own line.

---

Tip

Use the [`echo` tag](/docs/api/liquid/tags/echo) to output an expression inside `liquid` tags.

**Tip:**

Use the [`echo` tag](/docs/api/liquid/tags/echo) to output an expression inside `liquid` tags.

**Tip:** Use the <a href="/docs/api/liquid/tags/echo"><code>echo</code> tag</a> to output an expression inside <code>liquid</code> tags.

---

## Syntax

9

1

2

3

{% liquid

expression

%}

expression

The expression to be rendered inside the `liquid` tag.

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

{% liquid

# Show a message that's customized to the product type

assign product\_type = product.type | downcase

assign message = ''

case product\_type

when 'health'

assign message = 'This is a health potion!'

when 'love'

assign message = 'This is a love potion!'

else

assign message = 'This is a potion!'

endcase

echo message

%}

##### Code

```liquid
{% liquid
  # Show a message that's customized to the product type

  assign product_type = product.type | downcase
  assign message = ''

  case product_type
    when 'health'
      assign message = 'This is a health potion!'
    when 'love'
      assign message = 'This is a love potion!'
    else
      assign message = 'This is a potion!'
  endcase

  echo message
%}
```

##### Data

```liquid
{
  "product": {
    "type": null
  }
}
```

## Output

9

1

This is a health potion!

##### Output

```liquid
This is a health potion!
```

Was this page helpful?

YesNo