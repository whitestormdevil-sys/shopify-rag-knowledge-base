---
source: https://polaris.shopify.com/components/actions/button-group
---

# Button group

Button group displays multiple related actions stacked or in a horizontal row to help with arrangement and spacing.

### Upgrade to Polaris Web Components

Button group is now available as a framework-agnostic web component.

[Start using <s-button-group>](https://shopify.dev/docs/api/app-home/polaris-web-components/actions/buttongroup)

### Button group component examples

DefaultWith segmented buttonsPressed with segmented buttons

Use when you have multiple buttons to space them out evenly.

Edit in CodeSandbox

ReactHTML

```
import {ButtonGroup, Button} from '@shopify/polaris';
import React from 'react';

function ButtonGroupDefaultExample() {
  return (
    <ButtonGroup>
      <Button>Cancel</Button>
      <Button variant="primary">Save</Button>
    </ButtonGroup>
  );
}
```

## Props

interface ButtonGroupProps

gap?'extraTight' | 'tight' | 'loose'
:   Determines the space between button group items.

variant?"segmented"
:   Styling variant for group.

fullWidth?boolean
:   Buttons will stretch/shrink to occupy the full width.

connectedTop?boolean
:   Remove top left and right border radius.

noWrap?boolean
:   Prevent buttons in button group from wrapping to next line.

children?React.ReactNode
:   Button components.

## Best practices

Button groups should:

* Only use buttons that follow the
  [best practices outlined in the button component](https://polaris.shopify.com/components/actions/button#best-practices)
* Group together calls to action that have a relationship
* Be used with consideration that too many calls to action can cause merchants to be unsure of what to do next
* Be thoughtful about how multiple buttons will look and work on small screens
* Only be used in groups of up to six buttons if the buttons contain an icon with no text

---

## Content guidelines

Button groups should follow the [content guidelines](https://polaris.shopify.com/components/actions/button#content-guidelines) for buttons.

---

## Related components

* To learn how to use individual buttons, [use the button component](https://polaris.shopify.com/components/actions/button)
* To embed an action or navigation into a line of text, [use the link component](https://polaris.shopify.com/components/link)