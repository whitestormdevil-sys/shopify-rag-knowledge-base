---
source: https://shopify.dev/docs/api/liquid/filters/slice
---

9

1

string | slice

returns [string](/docs/api/liquid/basics#string)

Returns a substring or series of array items, starting at a given 0-based index.

By default, the substring has a length of one character, and the array series has one array item. However, you can
provide a second parameter to specify the number of characters or array items.

9

1

2

3

4

{{ collection.title | slice: 0 }}

{{ collection.title | slice: 0, 5 }}

{{ collection.all\_tags | slice: 1, 2 | join: ', ' }}

##### Code

```liquid
{{ collection.title | slice: 0 }}
{{ collection.title | slice: 0, 5 }}

{{ collection.all_tags | slice: 1, 2 | join: ', ' }}
```

##### Data

```liquid
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ],
    "title": "Products"
  }
}
```

## Output

9

1

2

3

4

P

Produ

dried, extra-potent

##### Output

```liquid
P
Produ

dried, extra-potent
```

[Anchor to Negative index](/docs/api/liquid/filters/slice#slice-negative-index)

### Negative index

You can supply a negative index which will count from the end of the string.

9

1

{{ collection.title | slice: -3, 3 }}

##### Code

```liquid
{{ collection.title | slice: -3, 3 }}
```

##### Data

```liquid
{
  "collection": {
    "title": "Products"
  }
}
```

## Output

9

1

cts

##### Output

```liquid
cts
```

Was this page helpful?

YesNo