---
source: https://polaris.shopify.com/components/actions/button
---

# Button

Buttons are used primarily for actions, such as "Add", "Close", "Cancel", or "Save". Plain buttons, which look similar to links, are used for less important or less commonly used actions, such as "view shipping settings".

### Upgrade to Polaris Web Components

Button is now available as a framework-agnostic web component.

[Start using <s-button>](https://shopify.dev/docs/api/app-home/polaris-web-components/button)

### Button component examples

DefaultPlainTertiaryPlain criticalPrimaryPrimary criticalLargeFull-widthText-alignedPressedPlain disclosureRight-aligned disclosureSelect disclosureSplitDisabled stateLoading stateWith iconIcon only

Used most in the interface. Only use another style if a button requires more or less visual weight.

Edit in CodeSandbox

ReactHTML

```
import {Button} from '@shopify/polaris';
import React from 'react';

function ButtonExample() {
  return <Button>Add product</Button>;
}
```

## Props

interface ButtonProps

children?string | string[]
:   The content to display inside the button.

size?"medium" | "large" | "micro" | "slim"
:   Changes the size of the button, giving it more or less padding.

    Defaults to 'medium'.

textAlign?"start" | "center" | "end" | "left" | "right"
:   Changes the inner text alignment of the button.

fullWidth?boolean
:   Allows the button to grow to the width of its container.

disclosure?boolean | "up" | "down" | "select"
:   Displays the button with a disclosure icon. Defaults to `down` when set to true.

removeUnderline?boolean
:   Removes underline from button text (including on interaction).

    Deprecated

    Use a variant instead.

icon?any
:   Icon to display to the left of the button content.

dataPrimaryLink?boolean
:   Indicates whether or not the button is the primary navigation link when rendered inside of an `IndexTable.Row`.

tone?"success" | "critical"
:   Sets the color treatment of the Button.

variant?"plain" | "primary" | "secondary" | "tertiary" | "monochromePlain"
:   Changes the visual appearance of the Button.

id?string
:   A unique identifier for the button.

url?string
:   A destination to link to, rendered in the href attribute of a link.

external?boolean
:   Forces url to open in a new tab.

target?Target
:   Where to display the url.

download?string | boolean
:   Tells the browser to download the url instead of opening it. Provides a hint for the downloaded filename if it is a string value.

submit?boolean
:   Allows the button to submit a form.

disabled?boolean
:   Disables the button, disallowing merchant interaction.

loading?boolean
:   Replaces button text with a spinner while a background action is being performed.

pressed?boolean
:   Sets the button in a pressed state.

accessibilityLabel?string
:   Visually hidden text for screen readers.

role?string
:   A valid WAI-ARIA role to define the semantic value of this element.

ariaControls?string
:   Id of the element the button controls.

ariaExpanded?boolean
:   Tells screen reader the controlled element is expanded.

ariaDescribedBy?string
:   Indicates the ID of the element that describes the button.

ariaChecked?"false" | "true"
:   Indicates the current checked state of the button when acting as a toggle or switch.

onClick?() => unknown
:   Callback when clicked.

onFocus?() => void
:   Callback when button becomes focused.

onBlur?() => void
:   Callback when focus leaves button.

onKeyPress?(event: React.KeyboardEvent<HTMLButtonElement>) => void
:   Callback when a keypress event is registered on the button.

onKeyUp?(event: React.KeyboardEvent<HTMLButtonElement>) => void
:   Callback when a keyup event is registered on the button.

onKeyDown?(event: React.KeyboardEvent<HTMLButtonElement>) => void
:   Callback when a keydown event is registered on the button.

onMouseEnter?() => void
:   Callback when mouse enter.

onTouchStart?() => void
:   Callback when element is touched.

onPointerDown?(event: React.PointerEvent<HTMLButtonElement>) => void
:   Callback when pointerdown event is being triggered.

## Best practices

Buttons should:

* Be clearly and accurately labeled.
* Lead with a strong, actionable verb.
* Use established button colors appropriately. For example, only use a red button for an action that’s difficult or impossible to undo.
* Prioritize the most important actions. Too many calls to action can cause confusion and make merchants unsure of what to do next.
* Be positioned in consistent locations in the interface.

### Buttons versus links

Buttons are used primarily for actions, such as “Add”, “Close”, “Cancel”, or “Save”. Plain buttons, which look similar to links, are used for less important or less commonly used actions, such as “view shipping settings”.

Links are used primarily for navigation, and usually appear within or directly following a sentence.

The HTML that renders for the Button and Link components carries meaning. Using these components intentionally and consistently results in:

* a more inclusive experience for assistive technology users
* a more cohesive visual experience for sighted users
* products that are easier to maintain at scale

---

## Content guidelines

Buttons need to be clear and predictable. Merchants should be able to anticipate what will happen when they select a button. Never mislead someone by mislabeling a button.

* Use universally understood iconography instead of words wherever you can
* Buttons can include an icon or text, or both
* Verbs like “View” or “Go” or “Read” are often unnecessary since the button itself already conveys these actions
* Sentence case
* No articles (“a” “an” “the”)
* No punctuation

Do

* Save
* Edit
* Add tags

Don't

* Save product
* Edit collection
* Add tag(s)

Always write button text in sentence case, which means the first word is capitalized and the rest are lowercase (unless a term is a proper noun).

Do

* Buy new domain

Don't

* Buy New Domain

Avoid unnecessary words and articles such as “the,” “an,” or “a.”

Do

Add menu item

Don't

Add a menu item

---

## Related components

* To combine or lay out multiple buttons, [use the button group component](https://polaris.shopify.com/components/actions/button-group)
* For navigational actions that appear within or directly following a sentence, use the [link component](https://polaris.shopify.com/components/link)

---

## Accessibility

Buttons can have different states that are visually and programmatically conveyed to merchants.

* Use the ariaControls prop to add an aria-controls attribute to the button. Use the attribute to point to the unique id of the content that the button manages.
* If a button expands or collapses adjacent content, then use the ariaExpanded prop to add the aria-expanded attribute to the button. Set the value to convey the current expanded (true) or collapsed (false) state of the content.
* Use the disabled prop to set the disabled state of the button. This prevents merchants from being able to interact with the button, and conveys its inactive state to assistive technologies.
* Use the pressed prop to add an aria-pressed attribute to the button.

#### Navigation

Merchants generally expect buttons to submit data or take action, and for links to navigate. If navigation is required for the button component, use the url prop. The control will output an anchor styled as a button, instead of a button in HTML, to help convey this difference.

For more information on making accessible links, see the [link component](https://polaris.shopify.com/components/link).

### Labeling

The accessibilityLabel prop adds an aria-label attribute to the button, which can be accessed by assistive technologies like screen readers. Typically, this label text replaces the visible text on the button for merchants who use assistive technology.

Use accessibilityLabel for a button if:

* The button’s visible text doesn’t adequately convey the purpose of the button to non-visual merchants
* The button has no text and relies on an icon alone to convey its purpose

To help support merchants who use speech activation software as well as sighted screen reader users, make sure that the aria-label text includes any button text that’s visible. Mismatches between visible and programmatic labeling can cause confusion, and might prevent voice recognition commands from working.

When possible, give the button visible text that clearly conveys its purpose without the use of accessibilityLabel. When no additional content is needed, duplicating the button text with accessibilityLabel isn’t necessary.

Do

Example

```
<Button>Edit shipping address</Button>
```

Example

```
<Heading>Shipping address</Heading>
<Button accessibilityLabel="Edit shipping address">Edit</Button>
```

Don't

Example

```
<Button accessibilityLabel="Change your shipping address">Edit</Button>
```

Example

```
<Button accessibilityLabel="Edit">Edit</Button>
```

#### External links

When you use the button component to create a link to an external resource:

* Use the external prop to make the link open in a new tab (or window, depending on the merchant’s browser settings)
* Use the icon prop to add the external icon to the button
* Use the accessibilityLabel prop to include the warning about opening a new tab in the button text for non-visual screen reader users

For more information on making accessible links, see the [link component](https://polaris.shopify.com/components/link).

Do

Example

```
<Button
  accessibilityLabel="Terms and conditions (opens a new window)"
  icon={ExternalIcon}
  url="http://example.com"
  external
>
  Terms and conditions
</Button>
```

Don't

Example

```
<Button url="http://example.com" external>Terms and conditions</Button>
<Button url="http://example.com" external>
  Terms and conditions
</Button>
```

### Keyboard support

Buttons use browser defaults for keyboard interactions.

* Give buttons keyboard focus with the `tab` key (or `shift` + `tab` when tabbing backwards)
* Activate buttons with the `enter`/`return` key or the `space` key

#### Custom key events

Use the onKeyDown, onKeyPress, and onKeyUp props to create custom events for buttons. With these props, you can use buttons to create complex, custom interactions like drag-and-drop interfaces.

Since these props introduce non-standard features to buttons, make sure to include accessible instructions so that merchants can understand how to use these features.