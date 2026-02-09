---
source: https://polaris.shopify.com/components/selection-and-input/text-field
---

# Text field

A text field is an input field that merchants can type into. It has a range of options and supports several text formats including numbers.

### Upgrade to Polaris Web Components

Text field is now available as a framework-agnostic web component.

[Start using <s-text-field>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/textfield)

### Text field component examples

DefaultNumberEmailMultilineWith hidden labelWith label actionWith right aligned textWith placeholder textWith help textWith prefix or suffixWith vertical contentWith connected fieldsWith validation errorWith separate validation errorDisabledWith character countWith clear buttonWith monospaced fontWith value selected on focusWith inline suggestionWith auto sizeWith auto size and dynamic suffixWith loading

Use to allow merchants to provide text input when the expected input is short. For longer input, use the auto grow or multiline options.

Edit in CodeSandbox

ReactHTML

```
import {TextField} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function TextFieldExample() {
  const [value, setValue] = useState('Jaded Pixel');

  const handleChange = useCallback(
    (newValue: string) => setValue(newValue),
    [],
  );

  return (
    <TextField
      label="Store name"
      value={value}
      onChange={handleChange}
      autoComplete="off"
    />
  );
}
```

## Props

This component defines its props in a way that our website can't automatically parse. The type definition is shown below, but it might be hard to read.

type TextFieldProps

NonMutuallyExclusiveProps & (Interactive | Readonly | Disabled) & (SelectSuggestion | SelectTextOnFocus)

## Best practices

Text fields should:

* Be clearly labeled so it’s obvious to merchants what they should enter into the field
* Be labeled as “Optional” when you need to request input that’s not required
* Only ask for information that’s really needed
* Validate input as soon as merchants have finished interacting with a field (but not before)

### Autocomplete

The autocomplete attribute in an input field controls two types of browser behavior:

1. **Browser autofill**: a feature that automatically populates form fields with previously-saved information, such as passwords, addresses, and credit card data.

   * Autofill is an important feature for our users. Google has found that ["users complete forms up to 30% faster"](https://developers.google.com/web/updates/2015/06/checkout-faster-with-autofill?hl=en) when using autofill.
   * The WHATWG has a list of supported autofill values for the autocomplete attribute. [Review the section "4.10.18.7 Autofill"](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) for all the input types and their corresponding autocomplete attribute values.
2. **Browser autocomplete** - a feature that displays previously submitted values for that field.

   * When this is on for a field, a user is presented a list with previously submitted values for the input

**Recommendation**

> Always add an autocomplete attribute and value to inputs if the type is: color, date, datetime-local, email, month, number, password, range, search, tel, text, time, url, or week.

#### Turning autofill/autocomplete off

Even if you do not want the browser to autofill a user's information, it is recommended you still have an autocomplete attribute with the value off or nope.

Unfortunately, [not all browsers support](https://caniuse.com/input-autocomplete-onoff) or respect autocomplete="off". This makes things challenging. Chrome, for example, [has a long outstanding bug](https://bugs.chromium.org/p/chromium/issues/detail?id=468153) and won't add support for off for now.

| Browser | Support for autocomplete="off" | Details |
| --- | --- | --- |
| Chrome | Partial | Intentionally ignores off value when the user uses the browser's autofill functionality. [See bug](https://bugs.chromium.org/p/chromium/issues/detail?id=468153). |
| Safari | Partial | Ignores off value for username, email and password fields. |
| Firefox | Partial | Ignores off value for login forms. [See bug](https://bugzilla.mozilla.org/show_bug.cgi?id=956906). |
| Edge | Partial | Intentionally ignores off value when the user uses the browser's autofill functionality. |

Chrome does seem to turn autocomplete off when using the value nope (or any non valid string). However, we have seen some inconsistencies even with that support.

**Recommendation (Chrome only)**

* Turning off both **autofill** and **browser autocomplete** (previously submitted values) in Chrome
  + Use autocomplete=nope and also **must have a name attribute**.
* Turning off **browser autocomplete** (previously submitted values) in Chrome
  + If you don't have name attribute and the field is not a typical autofill input (address, email, etc), use autocomplete=off.

### Virtual keyboard

![Examples of different number keyboards set with inputMode](/images/components/selection-and-input/text-field/virtual-keyboards.png)

The inputMode property should be set to select the appropriate virtual keyboard for the type of data expected to be entered by the user. Above are examples of different number keyboards set with inputMode.

---

## Content guidelines

For text field content guidelines, reference the [text fields experience](https://polaris.shopify.com/patterns/text-fields) page.

---

## Related components

* To lay out the elements in a responsive form, [use the form layout component](https://polaris.shopify.com/components/form-layout)
* To describe an invalid form input with a separate validation error, [use the inline error component](https://polaris.shopify.com/components/inline-error)
* It’s common to [use a select component](https://polaris.shopify.com/components/select) connected to the left or right of a text field.

---

## Accessibility

### Structure

Screen readers convey information about text fields automatically through native HTML.

* Use the disabled prop to add the HTML disabled attribute to the text field.
* Use the readOnly prop to add the HTML readonly attribute to the text field.
* If you use the type prop, then some assistive technologies adapt the software keyboard to the current task. This helps merchants with mobility, vision, and cognitive issues to enter information more easily.

Use the id prop to provide a unique id attribute value for the text field. If you don't provide an id, then the component generates one automatically. All text fields need to have unique id values.

### Labeling

The label prop is required to convey the purpose of the checkbox to all merchants.

If there are separate visual cues that convey the purpose of the text field to sighted merchants, then the label can be visually hidden with the labelHidden prop.

When you provide help text via the helpText prop or an inline error message via the error prop, the help or error content is conveyed to screen reader users with the aria-describedby attribute. This attribute causes the content to be read along with the label, either immediately or after a short delay.

Use the placeholder prop to provide additional instructions. However, don’t rely on placeholders alone since the content isn’t always conveyed to all merchants.

Do

* Use the label to provide instructions critical to using the text field
* Use help text and placeholder text to provide additional, non-critical instructions

Don't

Use the placeholder to provide information that’s required to use the text field.

### Keyboard support

Text fields have standard keyboard support.

* Merchants who rely on the keyboard expect to move focus to each text field using the `tab` key (or `shift` + `tab` when tabbing backwards)
* If the type is set to number, then merchants can use the up and down arrow keys to adjust the value typed into the field when hovering over or focusing the field to make the arrows appear
* Using the disabled prop will prevent the text field from receive keyboard focus or inputs
* The readOnly prop allows focus on the text field but prevents input or editing
* The inputMode prop can be used to bring up a relevant keyboard for merchants on mobile; it’s passed down to the input as an [inputmode attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode)

#### Automatically focusing

Although you can use the autoFocus prop to automatically move focus to the text field, it’s generally best to avoid focusing on fields automatically. The autoFocus prop is set to false by default and should only be used in cases where it won’t force focus to skip other controls or content of equal or greater importance.