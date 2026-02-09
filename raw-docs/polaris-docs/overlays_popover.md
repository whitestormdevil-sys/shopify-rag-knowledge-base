---
source: https://polaris.shopify.com/components/overlays/popover
---

# Popover

Popovers are small overlays that open on demand. They let merchants access additional content and actions without cluttering the page.

### Upgrade to Polaris Web Components

Popover is now available as a framework-agnostic web component.

[Start using <s-popover>](https://shopify.dev/docs/api/app-home/polaris-web-components/overlays/popover)

### Popover component examples

With action listWith content and actionsWith form componentsWith lazy loaded listWith searchable listbox

Use when presenting a set of actions in a disclosable menu.

Edit in CodeSandbox

ReactHTML

```
import {Button, Popover, ActionList} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function PopoverWithActionListExample() {
  const [popoverActive, setPopoverActive] = useState(true);

  const togglePopoverActive = useCallback(
    () => setPopoverActive((popoverActive) => !popoverActive),
    [],
  );

  const activator = (
    <Button onClick={togglePopoverActive} disclosure>
      More actions
    </Button>
  );

  return (
    <div style={{height: '250px'}}>
      <Popover
        active={popoverActive}
        activator={activator}
        autofocusTarget="first-node"
        onClose={togglePopoverActive}
      >
        <ActionList
          actionRole="menuitem"
          items={[{content: 'Import'}, {content: 'Export'}]}
        />
      </Popover>
    </div>
  );
}
```

## Props

interface PopoverProps

children?React.ReactNode
:   The content to display inside the popover.

preferredPosition?'above' | 'below' | 'mostSpace' | 'cover'
:   The preferred direction to open the popover.

preferredAlignment?'left' | 'center' | 'right'
:   The preferred alignment of the popover relative to its activator.

activeboolean
:   Show or hide the Popover.

activatorReact.ReactElement
:   The element to activate the Popover.
    If using a button, use the default or tertiary variant
    which will show an active state when popover is active.

preferInputActivator?boolean
:   Use the activator's input element to calculate the Popover position.

    Defaults to true.

activatorWrapper?string
:   The element type to wrap the activator with.

    Defaults to 'div'.

zIndexOverride?number
:   Override on the default z-index of 400.

preventFocusOnClose?boolean
:   Prevents focusing the activator or the next focusable element when the popover is deactivated.

sectioned?boolean
:   Automatically add wrap content in a section.

fullWidth?boolean
:   Allow popover to stretch to the full width of its activator.

fullHeight?boolean
:   Allow popover to stretch to fit content vertically.

fluidContent?boolean
:   Allow popover content to determine the overlay width and height.

fixed?boolean
:   Remains in a fixed position.

ariaHaspopup?boolean | "false" | "true" | "menu" | "dialog" | "grid" | "listbox" | "tree"
:   Used to illustrate the type of popover element.

hideOnPrint?boolean
:   Allow the popover overlay to be hidden when printing.

onClose(source: PopoverCloseSource) => void
:   Callback when popover is closed.

autofocusTarget?'none' | 'first-node' | 'container'
:   The preferred auto focus target defaulting to the popover container.

    Defaults to 'container'.

preventCloseOnChildOverlayClick?boolean
:   Prevents closing the popover when other overlays are clicked.

captureOverscroll?boolean
:   Prevents page scrolling when the end of the scrollable Popover overlay content is reached - applied to Pane subcomponent.

    Defaults to false.

## Best practices

Popovers should:

* Always be positioned next to the button or other interface element that triggers them
* Be used for secondary or less important information and actions since they’re hidden until merchants hit the trigger
* Contain navigation or actions that share a relationships to each other
* Be triggered by a clearly labeled button
* Use a default or tertiary button as the activator

---

## Content guidelines

### Popover content

If a popover contains actions, they should:

* Be clear and predictable: merchants should be able to anticipate what will happen when they click on an action item. Never deceive merchants by mislabeling an action.

Do

* Create order
* Buy shipping label

Don't

* New order
* Buy

* Be action-led: buttons should always lead with a strong verb that encourages action. To provide enough context to merchants use the {verb}+{noun} format on buttons except in the case of common actions like Save, Close, Cancel, or OK.

Do

* Rename
* Edit HTML
* Duplicate

Don't

* HTML editing options
* File name changes
* Duplicate this order so that you can make edits, updates, or changes

* Be scannable, especially when the popover contains a list of actions or options. Avoid unnecessary words and articles such as “the”, “an”, or “a”.

Do

* Add menu item

Don't

* Add a menu item

If the popover includes a series of navigational links, each item should:

* Be concise but still give merchants enough information so they can easily find and accurately navigate to the path they want.

Do

* Online store
* Messenger
* Facebook
* Buy Button

Don't

* Sales channel

---

## Related components

* To put a list of actions in a popover, [use the action list component](https://polaris.shopify.com/components/action-list)
* To let merchants select simple options from a list, [use the select component](https://polaris.shopify.com/components/select)

---

## Accessibility

Popovers usually contain an [option list](https://polaris.shopify.com/components/option-list) or an [action list](https://polaris.shopify.com/components/action-list), but can also contain other controls or content.

To assist screen readers with sending focus to an [action list](https://polaris.shopify.com/components/action-list), pass autofocusTarget='first-node' to Popover. This will avoid known issues a screen reader may have with keyboard support once focus is moved off the activator.

Web browsers assign a default value of 'menu' to the aria-haspopup role. You can use the prop ariaHaspopup to specify a value. Screen readers may fail to send focus to the Popover content when they expect the content to be adjacent to the element with aria-haspopup in the DOM tree. In this scenario, it is recommended not to provide the ariaHaspopup prop.

### Keyboard support

* When a popover opens, focus moves to the first focusable element or to the popover container
* Once focus is in the popover, merchants can access controls in the popover using the `tab` key (and `shift` + `tab` backwards) and standard keystrokes for interacting
* Merchants can dismiss the popover by tabbing out of it, pressing the `esc` key, or clicking outside of it
* When the popover is closed, focus returns to the element that launched it