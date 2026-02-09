---
source: https://shopify.dev/docs/api/liquid/filters/join
---

9

1

array | join

returns [string](/docs/api/liquid/basics#string)

Combines all of the items in an array into a single string, separated by a space.

9

1

{{ collection.all\_tags | join }}

##### Code

```liquid
{{ collection.all_tags | join }}
```

##### Data

```liquid
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

## Output

9

1

extra-potent fresh healing ingredients

##### Output

```liquid
extra-potent fresh healing ingredients
```

[Anchor to Custom separator](/docs/api/liquid/filters/join#join-custom-separator)

### Custom separator

9

1

array | join: string

You can specify a custom separator for the joined items.

9

1

{{ collection.all\_tags | join: ', ' }}

##### Code

```liquid
{{ collection.all_tags | join: ', ' }}
```

##### Data

```liquid
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

## Output

9

1

extra-potent, fresh, healing, ingredients

##### Output

```liquid
extra-potent, fresh, healing, ingredients
```

Was this page helpful?

YesNo