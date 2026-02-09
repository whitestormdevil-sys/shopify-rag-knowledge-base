---
source: https://polaris.shopify.com/components/layout-and-structure/inline-stack
---

# Inline stack

Use to display children horizontally in a row. Based on CSS Flexbox.

### Upgrade to Polaris Web Components

Inline stack is now available as a framework-agnostic web component.

[Start using <s-stack>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/stack)

### Inline stack component examples

Non-wrappingGapBlock alignAlignDirection

The default wrapping behavior of children can be overridden using the wrap prop.

Edit in CodeSandbox

ReactHTML

```
import React from 'react';
import {InlineStack} from '@shopify/polaris';


function InlineWithNonWrappingExample() {
  return (
    <InlineStack wrap={false}>
      <Placeholder width="106px" height="36px" />
      <Placeholder width="106px" height="20px" showBorder />
      <Placeholder width="106px" height="20px" showBorder />
      <Placeholder width="106px" height="20px" showBorder />
      <Placeholder width="106px" height="20px" showBorder />
      <Placeholder width="106px" height="20px" showBorder />
    </InlineStack>
  );
}

const Placeholder = ({height = 'auto', width = 'auto', showBorder = false}) => {
  return (
    <div
      style={{
        background: 'var(--p-color-text-info)',
        height: height,
        width: width,
        borderInlineStart: showBorder
          ? '1px dashed var(--p-color-bg-surface-success)'
          : 'none',
      }}
    />
  );
};
```

## Props

interface InlineStackProps

children?React.ReactNode

as?'div' | 'span' | 'li' | 'ol' | 'ul'
:   HTML Element type.

    Defaults to 'div'.

align?'start' | 'center' | 'end' | 'space-around' | 'space-between' | 'space-evenly'
:   Horizontal alignment of children.

direction?"row" | "row-reverse"
:   Horizontal direction in which children are laid out.

blockAlign?'start' | 'center' | 'end' | 'baseline' | 'stretch'
:   Vertical alignment of children.

gap?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   The spacing between elements. Accepts a spacing token or an object of spacing tokens for different screen sizes.

wrap?boolean
:   Wrap stack elements to additional rows as needed on small screens.

    Defaults to true.

## Related components

* To create the large-scale structure of pages, [use the InlineGrid component](https://polaris.shopify.com/components/layout-and-structure/inline-grid)
* To display elements vertically, [use the BlockStack component](https://polaris.shopify.com/components/layout-and-structure/block-stack)

## Related resources

* InlineStack props are named following the convention of CSS logical properties, such as align="start" vs. align="left" and blockAlign="end" vs. verticalAlign="bottom". Learn more about [CSS logicial properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).