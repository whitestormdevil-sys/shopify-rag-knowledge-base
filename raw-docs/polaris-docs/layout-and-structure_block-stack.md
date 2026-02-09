---
source: https://polaris.shopify.com/components/layout-and-structure/block-stack
---

# Block stack

Use to display children vertically and horizontally with full width by default. Based on CSS Flexbox.

### Upgrade to Polaris Web Components

Block stack is now available as a framework-agnostic web component.

[Start using <s-stack>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/stack)

### Block stack component examples

GapAlignInline align

Control the vertical space between children using the gap prop.

Edit in CodeSandbox

ReactHTML

```
import React from 'react';
import {BlockStack} from '@shopify/polaris';


function BlockStackWithGapExample() {
  return (
    <SpacingBackground>
      <BlockStack gap="500">
        <Placeholder height="48px" />
        <Placeholder height="48px" />
        <Placeholder height="48px" />
      </BlockStack>
    </SpacingBackground>
  );
}

const SpacingBackground = ({children}: {children: React.ReactNode}) => {
  return (
    <div
      style={{
        background: 'var(--p-color-bg-surface-success)',
        height: 'auto',
      }}
    >
      {children}
    </div>
  );
};

const Placeholder = ({height = 'auto'}) => {
  return (
    <div
      style={{
        background: 'var(--p-color-text-info)',
        padding: '14px var(--p-space-200)',
        height: height,
      }}
    />
  );
};
```

## Props

interface BlockStackProps

children?React.ReactNode

as?'div' | 'span' | 'ul' | 'ol' | 'li' | 'fieldset'
:   HTML Element type.

    Defaults to 'div'.

align?'start' | 'center' | 'end' | 'space-around' | 'space-between' | 'space-evenly'
:   Vertical alignment of children.

inlineAlign?'start' | 'center' | 'end' | 'baseline' | 'stretch'
:   Horizontal alignment of children.

gap?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   The spacing between children.

id?string
:   HTML id attribute.

reverseOrder?boolean
:   Reverse the render order of child items.

    Defaults to false.

role?any
:   Aria role.

## Best practices

Stacks should:

* Not be used for complex or unique arrangements of components
* Not be used for large-scale page layout

---

## Related components

* To display elements horizontally, [use the InlineStack component](https://polaris.shopify.com/components/layout-and-structure/inline-stack)

## Related resources

* BlockStack props are named following the convention of CSS logical properties, such as align="start" vs. align="top" and inlineAlign="end" vs. verticalAlign="right". Learn more about [CSS logicial properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).