---
source: https://polaris.shopify.com/components/overlays/tooltip
---

# Tooltip

Tooltips are floating labels that briefly explain the function of a user interface element. They can be triggered when merchants hover, focus, tap, or click.

### Upgrade to Polaris Web Components

Tooltip is now available as a framework-agnostic web component.

[Start using <s-tooltip>](https://shopify.dev/docs/api/app-home/polaris-web-components/overlays/tooltip)

### Tooltip component examples

DefaultVisible only with child interactionWith persistence on clickWith suffixWith underline

Use only when necessary to provide an explanation for an interface element.

Edit in CodeSandbox

ReactHTML

```
import {Tooltip, Text} from '@shopify/polaris';
import React from 'react';

function TooltipExample() {
  return (
    <div style={{padding: '75px 0'}}>
      <Tooltip active content="This order has shipping labels.">
        <Text fontWeight="bold" as="span">
          Order #1001
        </Text>
      </Tooltip>
    </div>
  );
}
```

### Tooltip component examples

DefaultVisible only with child interactionWith persistence on clickWith suffixWith underline

Use only when necessary to provide an explanation for an interface element.

Edit in CodeSandbox

ReactHTML

```
import {Tooltip, Text} from '@shopify/polaris';
import React from 'react';

function TooltipExample() {
  return (
    <div style={{padding: '75px 0'}}>
      <Tooltip active content="This order has shipping labels.">
        <Text fontWeight="bold" as="span">
          Order #1001
        </Text>
      </Tooltip>
    </div>
  );
}
```

## Props

interface TooltipProps

children?React.ReactNode
:   The element that will activate to tooltip.

contentReact.ReactNode
:   The content to display within the tooltip.

active?boolean
:   Toggle whether the tooltip is visible.

hoverDelay?number
:   Delay in milliseconds while hovering over an element before the tooltip is visible.

dismissOnMouseOut?boolean
:   Dismiss tooltip when not interacting with its children.

preferredPosition?'above' | 'below' | 'mostSpace' | 'cover'
:   The direction the tooltip tries to display.

    Defaults to 'above'.

activatorWrapper?string
:   The element type to wrap the activator in.

    Defaults to 'span'.

accessibilityLabel?string
:   Visually hidden text for screen readers.

width?'default' | 'wide'
:   Width of content.

    Defaults to 'default'.

padding?'default' | Extract<SpaceScale, '400'>
:   Padding of content.

    Defaults to 'default'.

borderRadius?"100" | "200"
:   Border radius of the tooltip.

    Defaults to '200'.

zIndexOverride?number
:   Override on the default z-index of 400.

hasUnderline?boolean
:   Whether to render a dotted underline underneath the tooltip's activator.

persistOnClick?boolean
:   Whether the tooltip's content remains open after clicking the activator.

onOpen?() => void

onClose?() => void

## Best practices

Tooltips should:

* Provide useful, additional information or clarification.
* Succinctly describe or expand on the element they point to.
* Be provided for icon-only buttons or a button with an associated keyboard shortcut.
* Not be used to communicate critical information, including errors in forms or other interaction feedback.
* Not contain any links or buttons.
* Be used sparingly. If you’re building something that requires a lot of tooltips, work on clarifying the design and the language in the experience.

---

## Content guidelines

### Basic tooltips

Tooltips should:

* Be written in sentence case
* Be concise and scannable
* Not be used to communicate error messages or important account information

Do

Post reach is the number of people who have seen your post in their News Feed.

Don't

To continue using Shopify, this amount must be paid immediately.

---

## Related components

* To make helpful content more visible to merchants, use the help text portions of form components such as [text fields](https://polaris.shopify.com/components/selection-and-input/text-field), [footer help](https://polaris.shopify.com/components/navigation/footer-help), or [an inline link to help](https://polaris.shopify.com/components/link)