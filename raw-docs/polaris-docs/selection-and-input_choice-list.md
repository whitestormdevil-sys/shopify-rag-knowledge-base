---
source: https://polaris.shopify.com/components/selection-and-input/choice-list
---

# Choice list

A choice list lets you create a list of grouped radio buttons or checkboxes. Use this component if you need to group together a related list of interactive choices.

### Upgrade to Polaris Web Components

Choice list is now available as a framework-agnostic web component.

[Start using <s-choice-list>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/choicelist)

### Choice list component examples

DefaultWith errorWith multi-choiceWith children contentWith dynamic children content

Allows merchants to select one option from a list. Make sure all options are an either/or choice.

Edit in CodeSandbox

ReactHTML

```
import {ChoiceList} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function SingleChoiceListExample() {
  const [selected, setSelected] = useState<string[]>(['hidden']);

  const handleChange = useCallback((value: string[]) => setSelected(value), []);

  return (
    <ChoiceList
      title="Company name"
      choices={[
        {label: 'Hidden', value: 'hidden'},
        {label: 'Optional', value: 'optional'},
        {label: 'Required', value: 'required'},
      ]}
      selected={selected}
      onChange={handleChange}
    />
  );
}
```

## Props

interface ChoiceListProps

titleReact.ReactNode
:   Label for list of choices.

choicesChoice[]
:   Collection of choices.

selectedstring[]
:   Collection of selected choices.

name?string
:   Name for form input.

allowMultiple?boolean
:   Allow merchants to select multiple options at once.

titleHidden?boolean
:   Toggles display of the title.

error?any
:   Display an error message.

disabled?boolean
:   Disable all choices \*.

onChange?(selected: string[], name: string) => void
:   Callback when the selected choices change.

tone?"magic"
:   Indicates the tone of the choice list.

## Best practices

Choice lists should:

* Include a title that tells merchants what to do or explains the available options
* Label options clearly based on what the option will do
* Avoid mutually exclusive options when allowing multiple selection

---

## Content guidelines

### List titles

List titles should:

* Help merchants understand how the items in the list are grouped together, or should explain what kind of choice merchants are making

Do

Pick a shipping method

Don't

Pick one

### Be concise and scannable

* Use simple, clear language that can be read at a glance
* Keep list titles to a single sentence
* It the title introduces the list, it should end with a colon
* Should be written in sentence case

Do

Shipping options

Don't

Shipping Options

### Not use colons

Do

If the customer abandons their checkout, send them an email reminder to complete their order:

* Option a
* Option b

Don't

If the customer abandons their checkout, send them an email reminder to complete their order

* Option a
* Option b

### List choices

Every item in a choice list should:

* Start with a capital letter
* Not use commas or semicolons at the end of each line
* Be written in sentence case (the first word capitalized, the rest lowercase)

Do

* Option 1
* Yellow
* Item three

Don't

* option 1
* Yellow;
* Item Three

### Helper text and descriptions

If your list contains helper text, only the description below the list item should contain punctuation.

---

## Related components

* To present a long list of radio buttons or when space is constrained, [use the select component](https://polaris.shopify.com/components/select)
* To build a group of radio buttons or checkboxes with a custom layout, use the [radio button component](https://polaris.shopify.com/components/radio-button) or [checkbox component](https://polaris.shopify.com/components/checkbox)
* To display a simple, non-interactive list of related content, [use the list component](https://polaris.shopify.com/components/lists/list)

---

## Accessibility

The choice list component uses the accessibility features of the [checkbox](https://polaris.shopify.com/components/checkbox) and [radio button](https://polaris.shopify.com/components/radio-button) components.