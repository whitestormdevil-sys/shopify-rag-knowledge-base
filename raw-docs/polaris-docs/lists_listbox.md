---
source: https://polaris.shopify.com/components/lists/listbox
---

# Listbox

A Listbox is a vertical list of interactive options, with room for icons, descriptions, and other elements.

### Listbox component examples

DefaultWith LoadingWith ActionWith custom elementWith search

Basic implementation of a control element used to let merchants select options

Edit in CodeSandbox

ReactHTML

```
import {Listbox} from '@shopify/polaris';
import React from 'react';

function BaseListboxExample() {
  return (
    <Listbox accessibilityLabel="Basic Listbox example">
      <Listbox.Option value="UniqueValue-1">Item 1</Listbox.Option>
      <Listbox.Option value="UniqueValue-2">Item 2</Listbox.Option>
      <Listbox.Option value="UniqueValue-3">Item 3</Listbox.Option>
    </Listbox>
  );
}
```

## Props

interface ListboxProps

childrenReactNode
:   Inner content of the listbox.

autoSelection?AutoSelection
:   Indicates the default active option in the list. Patterns that support option creation should default the active option to the first option.

    Defaults to AutoSelection.FirstSelected.

enableKeyboardControl?boolean
:   Explicitly enable keyboard control.

accessibilityLabel?string
:   Visually hidden text for screen readers.

customListId?string
:   Provide a custom ID for the list element.

onSelect?(value: string) => void
:   Callback fired when an option is selected.

onActiveOptionChange?(value: string, domId: string) => void
:   Callback fired when an option becomes active.

## Anatomy

![A diagram of the Listbox component showing the smaller primitive components it can be composed of.](/images/components/lists/listbox/listbox-anatomy@2x.png)

A listbox can be composed of:

1. **Options:** The individual options inside the Listbox that merchants can select or deselect.
2. **Dividers:** Placed between items and are useful in complex lists when there’s a lot of information for the merchant to parse.
3. **Section headers:** Used at the begining of a section when it’s necessary to call out the content being displayed. In most cases, the surrounding context should be enough for the merchant to understand the information in the list.

---

## Best practices

Listboxes should:

* Be clearly labeled so it’s noticeable to the merchant what type of options will be available
* Limit the number of options displayed at once
* Indicate a loading state to the merchant while option data is being populated

---

## Content guidelines

### Option lists

Each item in a Listbox should be clear and descriptive.

Do

* Traffic referrer source

Don't

* Source

## Patterns that use Listbox

Location picker

---

## Related components

* For a text field and popover container, [use the combobox component](https://polaris.shopify.com/components/combobox)
* [Autocomplete](https://polaris.shopify.com/components/autocomplete) can be used as a convenience wrapper in lieu of Combobox and Listbox.

---

## Accessibility

### Structure

The Listbox component is based on the [Aria 1.2 Listbox pattern](https://www.w3.org/TR/wai-aria-practices-1.2/#Listbox).

It is important to not present interactive elements inside of list box options as they can interfere with navigation for assistive technology users.

Do

* Use labels

Don't

* Use interactive elements inside the list

### Keyboard support

* Access the list of options with the up and down arrow keys
* Select an option that has focus with the `enter`/`return` key