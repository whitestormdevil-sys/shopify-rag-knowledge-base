---
source: https://polaris.shopify.com/components/layout-and-structure/card
---

# Card

Cards are used to group similar concepts and tasks together for merchants to scan, read, and get things done. It displays content in a familiar and recognizable style.

### Upgrade to Polaris Web Components

Card is now available as a framework-agnostic web component.

[Start using <s-section>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/section)

### Card component examples

DefaultWith subdued backgroundWith varying paddingWith responsive border radiusWith sectionWith subdued sectionWith multiple sectionsWith multiple titled sectionsWith subsectionWith flushed sectionWith sections and actionsWith sections and critical actionWith separate headerWith header actionsWith header icon actionsWith footer actionsWith multiple footer actionsWith custom footer actionsWith critical footer actionWith custom React Node titleWith all elements

By default, cards have an 8px border radius and uses --p-color-bg-surface as the background and --p-shadow-300 as the shadow. There is padding of space-400 (16px) around children.

Edit in CodeSandbox

ReactHTML

```
import {Card, Text} from '@shopify/polaris';
import React from 'react';

function CardDefault() {
  return (
    <Card>
      <Text as="h2" variant="bodyMd">
        Content inside a card
      </Text>
    </Card>
  );
}
```

## Props

interface CardProps

children?React.ReactNode

background?ColorBackgroundAlias
:   Background color.

    Defaults to 'bg-surface'.

padding?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   The spacing around the card.

    Defaults to {xs: '400', sm: '500'}.

roundedAbove?"xs" | "sm" | "md" | "lg" | "xl"
:   Border radius value above a set breakpoint.

    Defaults to 'sm'.

## Best practices

Cards should:

* Group related information
* Display information in a way that prioritizes what the merchant needs to know most first
* Use headings that set clear expectations about the card’s purpose
* Stick to single user flows or break more complicated flows into multiple sections
* Avoid too many call-to-action buttons or links and only one primary call to action per card
* Use calls to action on the bottom of the card for next steps and use the space in the upper right corner of the card for persistent, optional actions (such as Edit)

---

## Related components

* For more flexibility on styling, [use the Box component](https://polaris.shopify.com/components/layout-and-structure/box)