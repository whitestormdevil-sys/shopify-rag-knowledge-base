---
source: https://polaris.shopify.com/components/layout-and-structure/bleed
---

# Bleed

Applies negative margin to allow content to bleed out into the surrounding layout.

### Bleed component examples

HorizontalVerticalSpecific direction

Content will bleed horizontally into the surrounding layout using the marginInline prop.

Edit in CodeSandbox

ReactHTML

```
import React from 'react';
import {Bleed, Card, Text, InlineStack} from '@shopify/polaris';


function BleedHorizontalExample() {
  return (
    <Card>
      <Text as="h2" variant="bodyMd">
        Content inside a card
      </Text>
      <Bleed marginInline="400">
        <Placeholder label="marginInline" />
      </Bleed>
    </Card>
  );
}

const Placeholder = ({label = '', height = 'auto', width = 'auto'}) => {
  return (
    <div
      style={{
        background: 'var(--p-color-text-info)',
        padding: '14px var(--p-space-200)',
        height: height,
        width: width,
      }}
    >
      <InlineStack gap="400" align="center">
        <div
          style={{
            color: 'var(--p-color-text-info-on-bg-fill)',
          }}
        >
          <Text
            as="h2"
            variant="bodyMd"
            fontWeight="regular"
            tone="text-inverse"
          >
            {label}
          </Text>
        </div>
      </InlineStack>
    </div>
  );
};
```

## Props

interface BleedProps

children?React.ReactNode

marginInline?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative horizontal space around children.

marginBlock?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative vertical space around children.

marginBlockStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative top space around children.

marginBlockEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative bottom space around children.

marginInlineStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative left space around children.

marginInlineEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Negative right space around children.

## Bleed values

Content should never go beyond the edges of the parent container. Choose a bleed value that works within the containing layout.

## Related resources

* Bleed props are named following the convention of CSS logical properties, such as 'margin-inline-start' and 'margin-block-start'. Learn more about [CSS logicial properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).