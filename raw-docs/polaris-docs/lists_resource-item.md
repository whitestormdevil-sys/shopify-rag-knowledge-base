---
source: https://polaris.shopify.com/components/lists/resource-item
---

# Resource item

Resource items represent specific objects within a collection, such as products or orders. They provide contextual information on the resource type and link to the object’s detail page.

### Resource item component examples

DefaultWith mediaWith shortcut actionsWith vertical alignment

A basic resource item with its details filled in at the point of use.

Edit in CodeSandbox

ReactHTML

```
import {LegacyCard, ResourceList, ResourceItem, Text} from '@shopify/polaris';
import type {ResourceListProps} from '@shopify/polaris';
import {useState} from 'react';

const items = [
  {
    id: '6',
    url: 'posts/6',
    title: 'How To Get Value From Wireframes',
    author: 'Jonathan Mangrove',
  },
];

function ResourceItemExample() {
  const [selectedItems, setSelectedItems] = useState<
    ResourceListProps['selectedItems']
  >([]);

  return (
    <LegacyCard>
      <ResourceList
        resourceName={{singular: 'blog post', plural: 'blog posts'}}
        items={items}
        selectedItems={selectedItems}
        onSelectionChange={setSelectedItems}
        selectable
        renderItem={(item) => {
          const {id, url, title, author} = item;
          const authorMarkup = author ? <div>by {author}</div> : null;
          return (
            <ResourceItem
              id={id}
              url={url}
              accessibilityLabel={`View details for ${title}`}
              name={title}
            >
              <Text variant="bodyMd" fontWeight="bold" as="h3">
                {title}
              </Text>
              {authorMarkup}
            </ResourceItem>
          );
        }}
      />
    </LegacyCard>
  );
}
```

## Props

This component defines its props in a way that our website can't automatically parse. The type definition is shown below, but it might be hard to read.

type ResourceItemProps

PropsWithUrl | PropsWithClick

## Required components

The resource item component must be wrapped in the [resource list](https://polaris.shopify.com/components/resource-list) component.

---

## Accessibility

Resource items function as links to the full-page representations of the items. Each item should have a unique name prop. For each ResourceItem, the accessibilityLabel prop should be used to give the link a unique aria-label value. The aria-label value should convey the link’s purpose, using the name value. Merchants who use screen readers or other text to speech tools should be able to easily distinguish each link from the others.

When adding custom content to resource items, ensure that all text is available to all users and that all custom controls have a unique accessible name to help users understand what will happen when the control is activated.

### Keyboard

Links can be activated with the `enter`/`return` key by default.

If you add custom controls to resource items, then make sure that the controls:

* Can be used with the keyboard
* Receive keyboard focus in a logical order
* Display a visible focus indicator

---

## Best practices

Resource items should:

* Be tailored to the specific type of context being displayed.
* Perform an action when clicked. The action should navigate to the resource’s details page or provide more detail about the item.

Resource items can optionally:

* Provide [shortcut actions](https://polaris.shopify.com/components/resource-list#study-custom-item-shortcut-actions) for quick access to frequent actions from the resource’s details page.

---

## Content guidelines

Resource items should:

* Present the information that merchants need to find the items that they’re looking for.
* Support merchant tasks for the particular type of resource.
* Avoid colons.
* [Shortcut actions](https://polaris.shopify.com/components/resource-list#study-custom-item-shortcut-actions) don’t need to follow the full verb + noun formula for buttons.

---

## Related components

To display a simple list of related content, [use the list component](https://polaris.shopify.com/components/lists/list).