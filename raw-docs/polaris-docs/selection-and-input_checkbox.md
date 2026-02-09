---
source: https://polaris.shopify.com/components/selection-and-input/checkbox
---

# Checkbox

Checkboxes are most commonly used to give merchants a way to make a range of selections (zero, one, or multiple). They may also be used as a way to have merchants indicate they agree to specific terms and services.

### Upgrade to Polaris Web Components

Checkbox is now available as a framework-agnostic web component.

[Start using <s-checkbox>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/checkbox)

### Checkbox component examples

Default

Use in forms to toggle the state of something on or off. Default checkboxes can appear as selected and disabled, or unselected.

Edit in CodeSandbox

ReactHTML

```
import {Checkbox} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function CheckboxExample() {
  const [checked, setChecked] = useState(false);
  const handleChange = useCallback(
    (newChecked: boolean) => setChecked(newChecked),
    [],
  );

  return (
    <Checkbox
      label="Basic checkbox"
      checked={checked}
      onChange={handleChange}
    />
  );
}
```

## Props

interface CheckboxProps

ariaControls?string
:   Indicates the ID of the element that is controlled by the checkbox.

ariaDescribedBy?string
:   Indicates the ID of the element that describes the checkbox.

labelReact.ReactNode
:   Label for the checkbox.

labelHidden?boolean
:   Visually hide the label.

checked?boolean | "indeterminate"
:   Checkbox is selected. `indeterminate` shows a horizontal line in the checkbox.

disabled?boolean
:   Disable input.

id?string
:   ID for form input.

name?string
:   Name for form input.

value?string
:   Value for form input.

onChange?(newChecked: boolean, id: string) => void
:   Callback when checkbox is toggled.

onFocus?() => void
:   Callback when checkbox is focused.

onBlur?() => void
:   Callback when focus is removed.

labelClassName?string
:   Added to the wrapping label.

fill?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><boolean>
:   Grow to fill the space. Equivalent to width: 100%; height: 100%.

helpText?React.ReactNode
:   Additional text to aide in use.

error?any
:   Display an error message.

tone?"magic"
:   Indicates the tone of the checkbox.

bleed?Spacing
:   Spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

bleedBlockStart?Spacing
:   Vertical start spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

bleedBlockEnd?Spacing
:   Vertical end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

bleedInlineStart?Spacing
:   Horizontal start spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

bleedInlineEnd?Spacing
:   Horizontal end spacing around children. Accepts a spacing token or an object of spacing tokens for different screen sizes.

## Best practices

Checkboxes should:

* Work independently from each other. Selecting one checkbox shouldn’t change the selection status of another checkbox in the list. The exception is when a checkbox is used to make a bulk selection of multiple items.
* Be framed positively. For example, say “Publish store” instead of “Hide store”.
* Always have a label when used to activate or deactivate a setting.
* Be listed according to a logical order, whether it’s alphabetical, numerical, time-based, or some other clear system.
* Link to more information or include a subtitle as required to provide more explanation. Don’t rely on tooltips to explain a checkbox.

---

## Content guidelines

### Lists with checkboxes

Lists that use checkboxes should:

* Start with a capital letter

Do

* Option 1
* Option 2
* Option 3

Don't

* option 1
* option 2
* option 3

* Not use commas or semicolons at the end of each line

Do

* Red
* Yellow
* Blue

Don't

* Red;
* Yellow;
* Blue.

* In the rare case where the checkbox is asking merchants to agree to terms or service, use the first person

Do

I agree to the Terms of Service.

Don't

You agree to the Terms of Service

---

## Related components

* To present a list of options where merchants can only make a single choice, [use the radio button component](https://polaris.shopify.com/components/radio-button)
* To display a list of related content, [use the choice list component](https://polaris.shopify.com/components/choice-list)
* To create an ungrouped list, [use the content list component](https://polaris.shopify.com/components/lists/list)

---

## Accessibility

Screen readers convey the state of the checkbox automatically.

* Use the disabled prop to apply the HTML disabled attribute to the checkbox <input>. This prevents merchants from being able to interact with the checkbox, and conveys its inactive state to assistive technologies.
* Use the id prop to provide a unique id attribute value for the checkbox. If an id isn’t provided, then the component generates one. All checkboxes must have unique id values to work correctly with assistive technologies.
* Setting checked="indeterminate" conveys the state of the checkbox using aria-checked="mixed".
* Setting the ariaControls prop conveys the ID of the element whose contents or presence are controlled by the checkbox to screen reader users with the aria-controls attribute.

### Labeling

* The required label prop conveys the purpose of the checkbox to all merchants
* Use the labelHidden prop to visually hide the label but make it available to assistive technologies
* When you provide help text via the helpText prop or an inline error message via the error prop, the help or error content is conveyed to screen reader users with the aria-describedby attribute

### Keyboard support

* Move focus to each checkbox using the `tab` key (or `shift` + `tab` when tabbing backwards)
* To interact with the checkbox when it has keyboard focus, press the `space` key