---
source: https://polaris.shopify.com/components/layout-and-structure/divider
---

# Divider

Use to separate or group content.

### Upgrade to Polaris Web Components

Divider is now available as a framework-agnostic web component.

[Start using <s-divider>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/divider)

### Divider component examples

Color

Divider border color can be adjusted using the [Color tokens](https://polaris.shopify.com/tokens/color).

Edit in CodeSandbox

ReactHTML

```
import React from 'react';

import {Card, Divider, Text, BlockStack} from '@shopify/polaris';


function DividerWithBorderColorExample() {
  return (
    <Card>
      <BlockStack gap="500">
        <Text as="h1" variant="headingSm">
          Default
        </Text>
        <Divider />
        <Text as="h1" variant="headingSm">
          Border
        </Text>
        <Divider borderColor="border" />
        <Text as="h1" variant="headingSm">
          Border inverse
        </Text>
        <Divider borderColor="border-inverse" />
        <Text as="h1" variant="headingSm">
          Transparent
        </Text>
        <Divider borderColor="transparent" />
      </BlockStack>
    </Card>
  );
}
```

## Props

interface DividerProps

borderColor?ColorBorderAlias | "transparent"
:   Divider border color.

    Defaults to 'border-secondary'.

borderWidth?BorderWidthScale
:   Divider border width.

    Defaults to '025'.