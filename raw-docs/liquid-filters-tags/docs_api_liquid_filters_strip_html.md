---
source: https://shopify.dev/docs/api/liquid/filters/strip_html
---

9

1

string | strip\_html

returns [string](/docs/api/liquid/basics#string)

Strips all HTML tags from a string.

9

1

2

3

4

5

<!-- With HTML -->

{{ product.description }}

<!-- HTML stripped -->

{{ product.description | strip\_html }}

##### Code

```liquid
<!-- With HTML -->
{{ product.description }}

<!-- HTML stripped -->
{{ product.description | strip_html }}
```

##### Data

```liquid
{
  "product": {
    "description": "<h3>Are you low on health? Well we've got the potion just for you!</h3>\n<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>"
  }
}
```

## Output

9

1

2

3

4

5

6

7

<!-- With HTML -->

<h3>Are you low on health? Well we've got the potion just for you!</h3>

<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- HTML stripped -->

Are you low on health? Well we've got the potion just for you!

Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!

##### Output

```liquid
<!-- With HTML -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- HTML stripped -->
Are you low on health? Well we've got the potion just for you!
Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!
```

Was this page helpful?

YesNo