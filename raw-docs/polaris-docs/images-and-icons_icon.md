---
source: https://polaris.shopify.com/components/images-and-icons/icon
---

# Icon

Icons are used to visually communicate core parts of the product and available actions. They can act as wayfinding tools to help merchants more easily understand where they are in the product, and common interaction patterns that are available.

### Upgrade to Polaris Web Components

Icon is now available as a framework-agnostic web component.

[Start using <s-icon>](https://shopify.dev/docs/api/app-home/polaris-web-components/media/icon)

### Icon component examples

DefaultColoredWith custom SVGWith custom SVG and color

Use to visually communicate core parts of the product and available actions.

Edit in CodeSandbox

ReactHTML

```
import {Icon} from '@shopify/polaris';
import {PlusCircleIcon} from '@shopify/polaris-icons';
import React from 'react';

function IconExample() {
  return <Icon source={PlusCircleIcon} />;
}
```

## Props

interface IconProps

sourceany
:   The SVG contents to display in the icon (icons should fit in a 20 × 20 pixel viewBox).

tone?'base' | 'inherit' | 'subdued' | 'caution' | 'warning' | 'critical' | 'interactive' | 'info' | 'success' | 'primary' | 'emphasis' | 'magic' | 'textCaution' | 'textWarning' | 'textCritical' | 'textInfo' | 'textSuccess' | 'textPrimary' | 'textMagic'
:   Set the color for the SVG fill.

accessibilityLabel?string
:   Descriptive text to be read to screenreaders.

## Accessibility

Using icons can be a great help to merchants who have difficulties with reading, language, attention, and low vision.

If the icon appears without text, then use the accessibilityLabel prop to give the icon a text alternative. This adds an aria-label that’s conveyed to screen reader users.

Do

* Pair text and icons for clarity
* Give the icon a text equivalent if its purpose isn’t conveyed in another way
* Review our [alternative text](https://polaris.shopify.com/content/alternative-text) guidelines to make sure your use of icon works for all merchants

Example

```
<Icon source={OrderIcon} />
<p>No orders yet</p>
```

Example

```
<Button icon={PlusCircleIcon}>Add a product</Button>
```

Don't

* Describe what the icon looks like
* Include “icon” in the text equivalent
* Duplicate adjacent text in the alternative text
* Duplicate information provided programmatically

Example

```
<Icon source={PlusCircleIcon} accessibilityLabel="Circle plus icon" />
```

---

## Related guidelines

* To learn about implementing Polaris icons with [Polaris React](https://github.com/Shopify/polaris-react) in your projects, see the [@shopify/polaris-icons documentation](https://www.npmjs.com/package/@shopify/polaris-icons)
* To learn about the best practices for designing and using icons in your projects, see the [icon design guidelines](https://polaris.shopify.com/design/icons)
* To learn how to name icons, see the [icon naming guidelines](https://polaris.shopify.com/content/naming#icons)