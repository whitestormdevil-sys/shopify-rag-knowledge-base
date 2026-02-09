---
source: https://polaris.shopify.com/components/lists/list
---

# List

Lists display a set of related text-only content. Each list item begins with a bullet or a number.

### Upgrade to Polaris Web Components

List is now available as a framework-agnostic web component.

[Start using <s-unordered-list>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/unorderedlist)

### List component examples

BulletedNumberedExtra Tight

Use for a text-only list of related items that don’t need to be in a specific order and don’t require an icon or other indicator.

Edit in CodeSandbox

ReactHTML

```
import {List} from '@shopify/polaris';
import React from 'react';

function ListExample() {
  return (
    <List type="bullet">
      <List.Item>Yellow shirt</List.Item>
      <List.Item>Red shirt</List.Item>
      <List.Item>Green shirt</List.Item>
    </List>
  );
}
```

## Props

interface ListProps

gap?'extraTight' | 'loose'
:   Determines the space between list items.

    Defaults to 'loose'.

type?'bullet' | 'number'
:   Type of list to display.

    Defaults to 'bullet'.

children?React.ReactNode
:   List item elements.

## Best practices

Lists should:

* Break up chunks of related content to make the information easier for merchants to scan
* Be phrased consistently (try to start each item with a noun or a verb and be consistent with each item)
* Not be used for lists where the entire item represents an action

---

## Content guidelines

### List items

Every item in a list should:

* Start with a capital letter
* Not use commas or semicolons at the end of each line

Do

* Red
* Yellow
* Blue

Don't

* Red;
* Yellow;
* Blue.

* Be written in sentence case

Do

* Item one
* Item two
* Item three

Don't

* Item One
* Item Two
* Item Three

---

## Related components

* To create a list of checkboxes or radio buttons, [use the choice list component](https://polaris.shopify.com/components/choice-list)
* To present a collection of objects of the same type such as customers, products, or orders, [use the resource list component](https://polaris.shopify.com/components/resource-list)
* When text labels for each item are useful for describing the content, [use the Description List component](https://polaris.shopify.com/components/description-list)

---

## Accessibility

The list component outputs list items (<li>) inside a list wrapper (<ul> for bullet lists or <ol> for numbered lists). By default, list items are conveyed as a group of related elements to assistive technology users.

To group items for layout only, consider using the [vertical stack component](https://polaris.shopify.com/components/layout-and-structure/vertical-stack).