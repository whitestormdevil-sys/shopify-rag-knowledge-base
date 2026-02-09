---
source: https://shopify.dev/docs/api/liquid/basics/whitespace
---

# Basics

The following are basic concepts that you need to effectively interact with Liquid tags, filters, and objects.

Ask assistant

## [Anchor to Object handles](/docs/api/liquid/basics#object-handles)Object handles

Objects that represent store resources, such as products, collections, articles, and blogs, have handles for identifying an individual resource. The handle is used to build the URL for the resource, or to return properties for the resource.

Other objects like `linklists`, `links`, and `settings` also have handles.

### [Anchor to Creating and modifying handles](/docs/api/liquid/basics#creating-and-modifying-handles)Creating and modifying handles

Handles are automatically generated based on the resource title. They follow a set of rules:

* Handles are always lowercase
* Whitespace and special characters are replaced with a hyphen `-`.
* If there are multiple consecutive whitespace or special characters, then they're replaced with a single hyphen.
* Whitespace or special characters at the beginning are removed.

Handles need to be unique, so if a duplicate title is used, then the handle is auto-incremented by one. For example, if you had two products called `Potion`, then their handles would be `potion` and `potion-1`.

After a resource has been created, changing the resource title doesn't update the handle.

You can modify a resource's handle within the Shopify admin. This can be done either in the Handle or the Edit website SEO sections, depending on the resource. If you reference resources by their handle, then be sure to update those references when modifying handles.

---

Note

Individual links from `linklists` have handles based on their titles. These handles can't be modified directly. Individual settings, from `settings_schema.json`, sections, or blocks, get their handle from their `id` property.

**Note:**

Individual links from `linklists` have handles based on their titles. These handles can't be modified directly. Individual settings, from `settings_schema.json`, sections, or blocks, get their handle from their `id` property.

---

### [Anchor to Referencing handles](/docs/api/liquid/basics#referencing-handles)Referencing handles

All objects that have a handle have a `handle` property.
For example, you can output a product's handle with `product.handle`.
You can reference an object, from within its parent object, by its handle in two ways:

* Square bracket notation `[ ]`: Accepts a handle wrapped in quotes `'`, a Liquid variable, or an object reference.
* Dot notation `.`: Accepts a handle without quotes.

---

Note

Referencing an object by its handle is similar to [referencing array elements by their index](/docs/api/liquid/basics#array).

**Note:**

Referencing an object by its handle is similar to [referencing array elements by their index](/docs/api/liquid/basics#array).

---

---

## [Anchor to Logical and comparison operators](/docs/api/liquid/basics#logical-and-comparison-operators)Logical and comparison operators

Liquid supports basic logical and comparison operators for use with conditional tags: [`case`](/docs/api/liquid/tags/case), [`else`](/docs/api/liquid/tags/conditional-else), [`if`](/docs/api/liquid/tags/if) and [`unless`](/docs/api/liquid/tags/unless).

#### [Anchor to contains](/docs/api/liquid/basics#contains)contains

You can use `contains` to check for the presence of a string within an array, or another string. You can’t use `contains` to check for an object in an array of objects.

### [Anchor to Order of operations](/docs/api/liquid/basics#order-of-operations)Order of operations

When using more than one operator in a tag, the operators are evaluated from right to left, and you can’t change this order.

---

Caution

Parentheses `()` aren’t valid characters within Liquid tags. If you try to include them to group operators, then your tag won’t be rendered.

**Caution:**

Parentheses `()` aren’t valid characters within Liquid tags. If you try to include them to group operators, then your tag won’t be rendered.

---

---

## [Anchor to Types](/docs/api/liquid/basics#types)Types

Liquid output can be one of six data types.

### [Anchor to [object Object]](/docs/api/liquid/basics#string)string

Any series of characters, wrapped in single or double quotes.

---

Info

You can check whether a string is empty with the `blank` object.

**Info:**

You can check whether a string is empty with the `blank` object.

---

### [Anchor to [object Object]](/docs/api/liquid/basics#number)number

Numeric values, including floats and integers.

### [Anchor to [object Object]](/docs/api/liquid/basics#boolean)boolean

A binary value, either `true` or `false`.

### [Anchor to [object Object]](/docs/api/liquid/basics#nil)nil

An undefined value.

Tags or outputs that return `nil` don't print anything to the page. They are also treated as `false`.

---

Note

A string with the characters “nil” is not treated the same as `nil`.

**Note:**

A string with the characters “nil” is not treated the same as `nil`.

---

### [Anchor to [object Object]](/docs/api/liquid/basics#array)array

A list of variables of any type.

To access all of the items in an array, you can loop through each item in the array using a [`for`](/docs/api/liquid/tags/for) or [`tablerow`](/docs/api/liquid/tags/tablerow) tag.

You can use square bracket `[ ]` notation to access a specific item in an array. Array indexing starts at zero.

You can’t initialize arrays using only Liquid. You can, however, use the split filter to break a single string into an array of substrings.

### [Anchor to [object Object]](/docs/api/liquid/basics#empty)empty

An `empty` object is returned if you try to access an object that is defined, but has no value. For example a page or product that’s been deleted, or a setting with no value.

You can compare an object with `empty` to check whether an object exists before you access any of its attributes.

---

## [Anchor to Truthy and falsy](/docs/api/liquid/basics#truthy-and-falsy)Truthy and falsy

All data types must return either `true` or `false`. Those which return `true` by default are called truthy. Those that return `false` by default are called falsy.

### [Anchor to Example](/docs/api/liquid/basics#example)Example

Because `nil` and `false` are the only falsy values, you need to be careful how you check values in Liquid. A value might not be in the format you expect, but still be truthy.

For example, empty strings are truthy, so you need to check whether they’re empty with `blank`. `EmptyDrop` objects are also truthy, so you need to check whether the object you’re referencing is `empty`.

---

## [Anchor to Whitespace control](/docs/api/liquid/basics#whitespace-control)Whitespace control

Even if it doesn't output text, any line of Liquid outputs a line in your rendered content. By including hyphens in your Liquid tag, you can strip any whitespace that your Liquid generates when rendered.

If you want to remove whitespace on only one side of the Liquid tag, then you can include the hyphen on either the opening or closing tag.

---

Was this page helpful?

YesNo