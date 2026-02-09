---
source: https://polaris.shopify.com/components/selection-and-input/select
---

# Select

Select lets merchants choose one option from an options menu. Consider select when you have 4 or more options, to avoid cluttering the interface.

### Upgrade to Polaris Web Components

Select is now available as a framework-agnostic web component.

[Start using <s-select>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/select)

### Select component examples

DefaultWith inline labelDisabledWith prefixWith validation errorWith separate validation error

Presents a classic dropdown menu or equivalent picker as determined by merchants’ browsers.

Edit in CodeSandbox

ReactHTML

```
import {Select} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function SelectExample() {
  const [selected, setSelected] = useState('today');

  const handleSelectChange = useCallback(
    (value: string) => setSelected(value),
    [],
  );

  const options = [
    {label: 'Today', value: 'today'},
    {label: 'Yesterday', value: 'yesterday'},
    {label: 'Last 7 days', value: 'lastWeek'},
  ];

  return (
    <Select
      label="Date range"
      options={options}
      onChange={handleSelectChange}
      value={selected}
    />
  );
}
```

## Props

interface SelectProps

options?((string | StrictOption) | SelectGroup)[]
:   List of options or option groups to choose from.

labelReact.ReactNode
:   Label for the select.

labelAction?Action
:   Adds an action to the label.

labelHidden?boolean
:   Visually hide the label.

labelInline?boolean
:   Show the label to the left of the value, inside the control.

disabled?boolean
:   Disable input.

helpText?React.ReactNode
:   Additional text to aide in use.

placeholder?string
:   Example text to display as placeholder.

id?string
:   ID for form input.

name?string
:   Name for form input.

value?string
:   Value for form input.

error?any
:   Display an error state.

onChange?(selected: string, id: string) => void
:   Callback when selection is changed.

onFocus?(event?: React.FocusEvent<HTMLSelectElement>) => void
:   Callback when select is focused.

onBlur?(event?: React.FocusEvent<HTMLSelectElement>) => void
:   Callback when focus is removed.

requiredIndicator?boolean
:   Visual required indicator, add an asterisk to label.

tone?"magic"
:   Indicates the tone of the select.

## Best practices

The select component should:

* Be used for selecting between 4 or more pre-defined options
* Have a default option selected whenever possible
* Use “Select” as a placeholder option only if there’s no logical default option

---

## Content guidelines

### Select label

Labels should:

* Give a short description (1–3 words) of the requested input.
* Be written in sentence case (the first word capitalized, the rest lowercase).
* Avoid punctuation and articles (“the”, “an”, “a”).
* Be independent sentences. To support [internationalization](https://polaris.shopify.com/foundations/internationalization), they should not act as the first part of a sentence that is finished by the component’s options.
* Be descriptive, not instructional. If the selection needs more explanation, use help text below the field.

Do

* Email address

Don't

* What is your email address?

Do

* Phone number

Don't

* My phone number is:

### Select options

Options should:

* Start with “Select” as a placeholder if there isn’t a default option
* Be listed alphabetically or in another logical order so merchants can easily find the option they need
* Be written in sentence case (the first word capitalized, the rest lowercase) and avoid using commas or semicolons at the end of each option
* Be clearly labelled based on what the option will do

---

## Related components

* To let merchants select one option from a list with less than 4 options, use [the choice list component](https://polaris.shopify.com/components/choice-list)
* To create a select where merchants can make multiple selections, or to allow advanced formatting of option text, use an [option list](https://polaris.shopify.com/components/option-list) inside a [popover](https://polaris.shopify.com/components/overlays/popover)