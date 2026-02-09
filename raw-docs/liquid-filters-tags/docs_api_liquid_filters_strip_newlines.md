---
source: https://shopify.dev/docs/api/liquid/filters/strip_newlines
---

9

1

string | strip\_newlines

returns [string](/docs/api/liquid/basics#string)

Strips all newline characters (line breaks) from a string.

9

1

2

3

4

5

<!-- With newlines -->

{{ product.description }}

<!-- Newlines stripped -->

{{ product.description | strip\_newlines }}

##### Code

```liquid
<!-- With newlines -->
{{ product.description }}

<!-- Newlines stripped -->
{{ product.description | strip_newlines }}
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

<!-- With newlines -->

<h3>Are you low on health? Well we've got the potion just for you!</h3>

<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- Newlines stripped -->

<h3>Are you low on health? Well we've got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

##### Output

```liquid
<!-- With newlines -->
<h3>Are you low on health? Well we've got the potion just for you!</h3>
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

<!-- Newlines stripped -->
<h3>Are you low on health? Well we've got the potion just for you!</h3><p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```

Was this page helpful?

YesNo