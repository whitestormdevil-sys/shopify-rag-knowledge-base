---
source: https://polaris.shopify.com/components/selection-and-input/radio-button
---

# Radio button

Use radio buttons to present each item in a list of options where merchants must make a single selection.

### Upgrade to Polaris Web Components

Radio button is now available as a framework-agnostic web component.

[Start using <s-choice-list>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/choicelist)

### Radio button component examples

Default

Use radio buttons where merchants must make a single selection.

Edit in CodeSandbox

ReactHTML

```
import {LegacyStack, RadioButton} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function RadioButtonExample() {
  const [value, setValue] = useState('disabled');

  const handleChange = useCallback(
    (_: boolean, newValue: string) => setValue(newValue),
    [],
  );

  return (
    <LegacyStack vertical>
      <RadioButton
        label="Accounts are disabled"
        helpText="Customers will only be able to check out as guests."
        checked={value === 'disabled'}
        id="disabled"
        name="accounts"
        onChange={handleChange}
      />
      <RadioButton
        label="Accounts are optional"
        helpText="Customers will be able to check out with a customer account or as a guest."
        id="optional"
        name="accounts"
        checked={value === 'optional'}
        onChange={handleChange}
      />
    </LegacyStack>
  );
}
```

## Props

interface RadioButtonProps

ariaDescribedBy?string
:   Indicates the ID of the element that describes the radio button.

labelReact.ReactNode
:   Label for the radio button.

labelHidden?boolean
:   Visually hide the label.

checked?boolean
:   Radio button is selected.

disabled?boolean
:   Disable input.

id?string
:   ID for form input.

name?string
:   Name for form input.

value?string
:   Value for form input.

onChange?(newValue: boolean, id: string) => void
:   Callback when the radio button is toggled.

onFocus?() => void
:   Callback when radio button is focused.

onBlur?() => void
:   Callback when focus is removed.

fill?T | ({ [Breakpoint in BreakpointsAlias]?: T; })<T><boolean>
:   Grow to fill the space. Equivalent to width: 100%; height: 100%.

helpText?React.ReactNode
:   Additional text to aide in use.

tone?"magic"
:   Indicates the tone of the text field.

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

Radio buttons should:

* Always be used with an associated label component.
* Be part of a list of radio buttons that:
  + Include at least two or more choices.
  + Are used to have merchants select only one option.
  + Include mutually exclusive options—this means that each option must be
    independent from every other option in the list. For example: Red, blue, and
    yellow are mutually exclusive. Red, blue, yellow, red/blue are not mutually
    exclusive.
  + List options in a rational order that makes logical sense.
  + Have a default option selected whenever possible.

---

## Content guidelines

### Radio button labels

Radio button labels should:

* Be introduced with a colon or a heading
* Start with a capital letter

Do

* Option 1

Don't

* option 1

* Not end in punctuation if it’s a single sentence, word, or a fragment

Do

* Red

Don't

* Red;

### Toggle (Android and iOS only)

Toggle labels should:

* Be clear what merchants are enabling or disabling
* Start with a capital letter

Toggle values should:

* Never be labeled

---

## Related components

* To make simple lists of radio buttons easier to build, [use the choice list component](https://polaris.shopify.com/components/choice-list)
* For long lists of options, [consider the select component](https://polaris.shopify.com/components/select) to avoid overwhelming merchants
* To present merchants with a list of checkboxes, [use the choice list component](https://polaris.shopify.com/components/choice-list) with the “allow multiple” option
* To display non-interactive list of related content, [use the content list component](https://polaris.shopify.com/components/lists/list)

---

## Accessibility

Screen readers convey the state of the radio button automatically.

* Use the disabled prop to apply the HTML disabled attribute to the radio button <input>. This prevents merchants from being able to interact with the radio button, and conveys its inactive state to assistive technologies.
* Use the id prop to provide a unique id attribute value for the radio button. If an id isn’t provided, then the component generates one. All radio buttons must have unique id values to work correctly with assistive technologies.

### Labeling

* The required label prop conveys the purpose of the radio button to all merchants
* Use the labelHidden prop to visually hide the label but make it available to assistive technologies
* When you provide help text via the helpText prop or an inline error message via the error prop, the help or error content is conveyed to screen reader users with the aria-describedby attribute

### Keyboard support

* Move focus to the radio button group using the `tab` key (or `shift` + `tab` when tabbing backwards)
* Use the up and down arrow keys to change which radio button is selected