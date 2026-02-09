---
source: https://shopify.dev/docs/api/liquid/filters/metafield_text
---

9

1

metafield | metafield\_text

returns [string](/docs/api/liquid/basics#string)

Generates a text version of the data from a [`metafield` object](https://shopify.dev/docs/api/liquid/objects/metafield).

---

Note

The `metafield_text` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

**Note:**

The `metafield_text` filter doesn't currently support list metafields other than `list.single_line_text_field` and `list.metaobject_reference`.

**Note:** The <code><span class="PreventFireFoxApplyingGapToWBR">metafield<wbr/>\_text</span></code> filter doesn&#39;t currently support list metafields other than <code><span class="PreventFireFoxApplyingGapToWBR">list.single<wbr/>\_line<wbr/>\_text<wbr/>\_field</span></code> and <code><span class="PreventFireFoxApplyingGapToWBR">list.metaobject<wbr/>\_reference</span></code>.

---

[Anchor to Basic types](/docs/api/liquid/filters/metafield_text#metafield_text-basic-types)

### Basic types

The following outlines the output for each metafield type:

| Metafield type | Output |
| --- | --- |
| `single_line_text_field` | The metafield text. |
| `multi_line_text_field` | The metafield text. |
| `page_reference` | The page title. |
| `product_reference` | The product title. |
| `collection_reference` | The collection title. |
| `variant_reference` | The variant title. |
| `file_reference` | The file URL. |
| `number_integer` | The number. |
| `number_decimal` | The number. |
| `date` | The date. |
| `date-time` | The date and time. |
| `url` | The URL. |
| `json` | The JSON. |
| `boolean` | The boolean value. |
| `color` | The color value. |
| `weight` | The weight value and unit.  If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `volume` | The volume value and unit.  If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `dimension` | The dimension value and unit.  If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `rating` | The rating value. |
| `list.single_line_text_field` | The metafield values in sentence format.  For example, if you had the values `Toronto`, `Ottawa`, and `Vancouver`, then the output would be:  `Toronto, Ottawa, and Vancouver` |
| `money` | The money value, formatted using the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting). |
| `rich_text_field` | The rich text value as simple text. |

9

1

{{ product.metafields.information.dosage | metafield\_text }}

##### Code

```liquid
{{ product.metafields.information.dosage | metafield_text }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

Potion dosages

##### Output

```liquid
Potion dosages
```

[Anchor to Complex types](/docs/api/liquid/filters/metafield_text#metafield_text-complex-types)

### Complex types

The following metafield types produce different output depending on the provided `field` parameter:

* [`list.metaobject_reference`](/docs/api/liquid/filters/metafield_text#metafield_text-list.metaobject_reference)
* [`metaobject_reference`](/docs/api/liquid/filters/metafield_text#metafield_text-metaobject_reference)

[Anchor to list.metaobject\_reference](/docs/api/liquid/filters/metafield_text#metafield_text-listmetaobject_reference)

### list.metaobject\_reference

9

1

metafield | metafield\_text: field: string

Outputs the list of metaobjects in sentence format. The required `field` parameter specifies which field should be rendered for each metaobject. The `field` parameter can reference only metafields of type `single_line_text_field`.

9

1

{{ product.metafields.information.ingredients | metafield\_text: field: 'name' }}

##### Code

```liquid
{{ product.metafields.information.ingredients | metafield_text: field: 'name' }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

Spinach, Kale, and Mushrooms

##### Output

```liquid
Spinach, Kale, and Mushrooms
```

[Anchor to metaobject\_reference](/docs/api/liquid/filters/metafield_text#metafield_text-metaobject_reference)

### metaobject\_reference

9

1

metafield | metafield\_text: field: string

Outputs the metafield text for the metaobject field specified by the required `field` parameter. The `field` parameter can reference only metafields of type `single_line_text_field`.

9

1

{{ product.metafields.information.primary\_ingredient | metafield\_tag: field: 'name' }}

##### Code

```liquid
{{ product.metafields.information.primary_ingredient | metafield_tag: field: 'name' }}
```

##### Data

```liquid
{
  "product": {
    "metafields": {}
  }
}
```

## Output

9

1

<span class="metafield-single\_line\_text\_field">Spinach</span>

##### Output

```liquid
<span class="metafield-single_line_text_field">Spinach</span>
```

Was this page helpful?

YesNo