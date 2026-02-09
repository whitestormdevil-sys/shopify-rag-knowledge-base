---
source: https://shopify.dev/docs/api/liquid/filters/newline_to_br
---

9

1

string | newline\_to\_br

returns [string](/docs/api/liquid/basics#string)

Converts newlines (`\n`) in a string to HTML line breaks (`<br>`).

9

1

{{ product.description | newline\_to\_br }}

##### Code

```liquid
{{ product.description | newline_to_br }}
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

<h3>Are you low on health? Well we've got the potion just for you!</h3><br />

<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>

##### Output

```liquid
<h3>Are you low on health? Well we've got the potion just for you!</h3><br />
<p>Just need a top up? Almost dead? In between? No need to worry because we have a range of sizes and strengths!</p>
```

Was this page helpful?

YesNo