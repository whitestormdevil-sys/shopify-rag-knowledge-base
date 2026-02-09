---
source: https://polaris.shopify.com/components/layout-and-structure/box
---

# Box

Box is the most primitive layout component. It’s a way to access Polaris design tokens.

### Upgrade to Polaris Web Components

Box is now available as a framework-agnostic web component.

[Start using <s-box>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/box)

### Box component examples

ColorBorder widthBorder radiusPaddingShadow

Background color of box and text color inside a box can be adjusted using the [Color tokens](https://polaris.shopify.com/tokens/color).

Edit in CodeSandbox

ReactHTML

```
import React from 'react';
import {Box, Text} from '@shopify/polaris';


function BoxWithColorExample() {
  return (
    <Box background="bg-fill-info">
      <Placeholder label="Content inside a box" />
    </Box>
  );
}

const Placeholder = ({label = '', height = 'auto', width = 'auto'}) => {
  return (
    <div
      style={{
        background: 'var(--p-color-border-interactive-subdued)',
        height: height,
        width: width,
        borderRadius: 'inherit',
      }}
    >
      <div
        style={{
          color: 'var(--p-color-text)',
        }}
      >
        <Text as="p" variant="bodyMd">
          {label}
        </Text>
      </div>
    </div>
  );
};
```

## Props

interface BoxProps

children?React.ReactNode

as?'div' | 'span' | 'section' | 'legend' | 'ul' | 'li'
:   HTML Element type.

    Defaults to 'div'.

background?ColorBackgroundAlias
:   Background color.

borderColor?ColorBorderAlias | "transparent"
:   Border color.

borderStyle?'solid' | 'dashed'
:   Border style.

borderRadius?BorderRadiusAliasOrScale
:   Border radius.

borderEndStartRadius?BorderRadiusAliasOrScale
:   Vertical end horizontal start border radius.

borderEndEndRadius?BorderRadiusAliasOrScale
:   Vertical end horizontal end border radius.

borderStartStartRadius?BorderRadiusAliasOrScale
:   Vertical start horizontal start border radius.

borderStartEndRadius?BorderRadiusAliasOrScale
:   Vertical start horizontal end border radius.

borderWidth?BorderWidthScale
:   Border width.

borderBlockStartWidth?BorderWidthScale
:   Vertical start border width.

borderBlockEndWidth?BorderWidthScale
:   Vertical end border width.

borderInlineStartWidth?BorderWidthScale
:   Horizontal start border width.

borderInlineEndWidth?BorderWidthScale
:   Horizontal end border width.

color?ColorTextAlias
:   Color of children.

id?string
:   HTML id attribute.

minHeight?string
:   Minimum height of container.

minWidth?string
:   Minimum width of container.

maxWidth?string
:   Maximum width of container.

overflowX?'hidden' | 'scroll' | 'clip'
:   Clip horizontal content of children.

overflowY?'hidden' | 'scroll' | 'clip'
:   Clip vertical content of children.

padding?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingBlock?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Vertical start and end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingBlockStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Vertical start spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingBlockEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Vertical end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingInline?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Horizontal start and end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingInlineStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Horizontal start spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

paddingInlineEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Horizontal end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

role?any
:   Aria role.

shadow?ShadowAliasOrScale
:   Shadow on box.

tabIndex?any
:   Set tab order.

width?string
:   Width of container.

position?'relative' | 'absolute' | 'fixed' | 'sticky'
:   Position of box.

insetBlockStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Top position of box.

insetBlockEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Bottom position of box.

insetInlineStart?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Left position of box.

insetInlineEnd?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><SpaceScale>
:   Right position of box.

opacity?string
:   Opacity of box.

outlineColor?ColorBorderAlias
:   Outline color.

outlineStyle?'solid' | 'dashed'
:   Outline style.

outlineWidth?BorderWidthScale
:   Outline width.

printHidden?boolean
:   Visually hide the contents during print.

visuallyHidden?boolean
:   Visually hide the contents (still announced by screenreader).

zIndex?string
:   z-index of box.

## Related components

* For more specific use cases, [use the Card component](https://polaris.shopify.com/components/layout-and-structure/card)

## Related resources

* Box props are named following the convention of CSS logical properties, such as 'padding-inline-start' and 'padding-block-start'. Learn more about [CSS logicial properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).