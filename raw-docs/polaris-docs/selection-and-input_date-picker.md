---
source: https://polaris.shopify.com/components/selection-and-input/date-picker
---

# Date picker

Date pickers let merchants choose dates from a visual calendar that’s consistently applied wherever dates need to be selected across Shopify.

### Upgrade to Polaris Web Components

Date picker is now available as a framework-agnostic web component.

[Start using <s-date-picker>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/datepicker)

### Date picker component examples

DefaultRangedMulti-month rangedWith disabled date rangesWith specific disabled dates

Use when merchants need to select a single day close to today (today is the default starting position for the date picker).

Edit in CodeSandbox

ReactHTML

```
import {DatePicker} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function DatePickerExample() {
  const [{month, year}, setDate] = useState({month: 1, year: 2018});
  const [selectedDates, setSelectedDates] = useState({
    start: new Date('Wed Feb 07 2018 00:00:00 GMT-0500 (EST)'),
    end: new Date('Wed Feb 07 2018 00:00:00 GMT-0500 (EST)'),
  });

  const handleMonthChange = useCallback(
    (month: number, year: number) => setDate({month, year}),
    [],
  );

  return (
    <DatePicker
      month={month}
      year={year}
      onChange={setSelectedDates}
      onMonthChange={handleMonthChange}
      selected={selectedDates}
    />
  );
}
```

## Props

interface DatePickerProps

id?string
:   ID for the element.

selected?Range | Date
:   The selected date or range of dates.

monthnumber
:   The month to show, from 0 to 11. 0 is January, 1 is February ... 11 is December.

yearnumber
:   The year to show.

allowRange?boolean
:   Allow a range of dates to be selected.

disableDatesBefore?Date
:   Disable selecting dates before this.

disableDatesAfter?Date
:   Disable selecting dates after this.

disableSpecificDates?Date[]
:   Disable specific dates.

multiMonth?boolean
:   The selection can span multiple months.

weekStartsOn?number
:   First day of week, from 0 to 6. 0 is Sunday, 1 is Monday ... 6 is Saturday.

    Defaults to 0.

dayAccessibilityLabelPrefix?string
:   Visually hidden prefix text for selected days on single selection date pickers.

onChange?(date: Range) => void
:   Callback when date is selected.

onMonthChange?(month: number, year: number) => void
:   Callback when month is changed.

#### Tip

Check out the [new patterns section](https://polaris.shopify.com/patterns) to
learn how merchants prefer to select dates in different scenarios!

## Best practices

Date pickers should:

* Use smart defaults and highlight common selections
* Close after a single date is selected unless a range with a start and end date is required
* Set the start date on first click or tap and the end date on second click or tap if a range is required
* Not be used to enter a date that is many years in the future or the past
* Follow [date format guidelines](https://polaris.shopify.com/content/grammar-and-mechanics#dates--numbers--and-measurements)

---

## Accessibility

Some users might find interacting with date pickers to be challenging. When you use the date picker component, always give users the option to enter the date using a text field component as well.

If you use the date picker within a [popover component](/components/overlays/popover), then use a button to trigger the popover instead of displaying the popover when the text input gets focus. This gives users more control over their experience.

### Keyboard support

* Press the `tab` key to move forward and `shift` + `tab` to move backward through the previous button, next button, and the calendar
* When focus is in the calendar, move keyboard focus between the dates using the arrow keys
* To select a date that has focus, press the `enter`/`return` key

## Related patterns

* [Date picking](/patterns/date-picking)