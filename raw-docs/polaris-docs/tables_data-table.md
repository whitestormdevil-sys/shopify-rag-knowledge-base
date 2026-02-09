---
source: https://polaris.shopify.com/components/tables/data-table
---

# Data table

Data tables are used to organize and display all information from a data set. While a data visualization represents part of data set, a data table lets merchants view details from the entire set. This helps merchants compare and analyze the data.

### Upgrade to Polaris Web Components

Data table is now available as a framework-agnostic web component.

[Start using <s-table>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/table)

### Data table component examples

DefaultSortableWith footerWith custom totals headingWith totals in footerWith row heading linksWith all of its elementsWith fixed first columnsWith increased density and zebra stripingWith sticky header enabledWith pagination

Use to present small amounts of data for merchants to view statically.

Edit in CodeSandbox

ReactHTML

```
import {Page, LegacyCard, DataTable} from '@shopify/polaris';
import React from 'react';

function DataTableExample() {
  const rows = [
    ['Emerald Silk Gown', '$875.00', 124689, 140, '$122,500.00'],
    ['Mauve Cashmere Scarf', '$230.00', 124533, 83, '$19,090.00'],
    [
      'Navy Merino Wool Blazer with khaki chinos and yellow belt',
      '$445.00',
      124518,
      32,
      '$14,240.00',
    ],
  ];

  return (
    <Page title="Sales by product">
      <LegacyCard>
        <DataTable
          columnContentTypes={[
            'text',
            'numeric',
            'numeric',
            'numeric',
            'numeric',
          ]}
          headings={[
            'Product',
            'Price',
            'SKU Number',
            'Net quantity',
            'Net sales',
          ]}
          rows={rows}
          totals={['', '', '', 255, '$155,830.00']}
        />
      </LegacyCard>
    </Page>
  );
}
```

## Props

interface DataTableProps

columnContentTypes'text' | 'numeric'[]
:   List of data types, which determines content alignment for each column. Data types are "text," which aligns left, or "numeric," which aligns right.

headingsReact.ReactNode[]
:   List of column headings.

totals?any[]
:   List of numeric column totals, highlighted in the table’s header below column headings. Use empty strings as placeholders for columns with no total.

totalsName?{ singular: React.ReactNode; plural: React.ReactNode; }
:   Custom totals row heading.

showTotalsInFooter?boolean
:   Placement of totals row within table.

rowsany[][]
:   Lists of data points which map to table body rows.

hideScrollIndicator?boolean
:   Hide column visibility and navigation buttons above the header when the table horizontally collapses to be scrollable.

    Defaults to false.

truncate?boolean
:   Truncate content in first column instead of wrapping.

    Defaults to true.

verticalAlign?'top' | 'bottom' | 'middle' | 'baseline'
:   Vertical alignment of content in the cells.

    Defaults to 'top'.

footerContent?any
:   Content centered in the full width cell of the table footer row.

hoverable?boolean
:   Table row has hover state. Defaults to true.

sortable?boolean[]
:   List of booleans, which maps to whether sorting is enabled or not for each column. Defaults to false for all columns.

defaultSortDirection?'ascending' | 'descending' | 'none'
:   The direction to sort the table rows on first click or keypress of a sortable column heading. Defaults to ascending.

    Defaults to 'ascending'.

initialSortColumnIndex?number
:   The index of the heading that the table rows are initially sorted by. Defaults to the first column.

    Defaults to 0.

onSort?(headingIndex: number, direction: 'ascending' | 'descending' | 'none') => void
:   Callback fired on click or keypress of a sortable column heading.

increasedTableDensity?boolean
:   Increased density.

hasZebraStripingOnData?boolean
:   Add zebra striping to data rows.

stickyHeader?boolean
:   Header becomes sticky and pins to top of table when scrolling.

hasFixedFirstColumn?boolean
:   Deprecated

    Add a fixed first column on horizontal scroll. Use fixedFirstColumns={n} instead.

fixedFirstColumns?number
:   Add fixed columns on horizontal scroll.

firstColumnMinWidth?string
:   Specify a min width for the first column if neccessary.

pagination?Omit<PaginationProps, 'type'>
:   Properties to enable pagination at the bottom of the table.

## Best practices

Data tables should:

* Show values across multiple categories and measures.
* Allow for filtering and ordering when comparison is not a priority.
* Help merchants visualize and scan many values from an entire data set.
* Help merchants find other values in the data hierarchy through use of links.
* Minimize clutter by only including values that supports the data’s purpose.
* Include a summary row to surface the column totals.
* Not include calculations within the summary row.
* Wrap instead of truncate content. This is because if row titles start with the same word, they’ll all appear the same when truncated.
* Not to be used for an actionable list of items that link to details pages. For this functionality, use the [resource list component](https://polaris.shopify.com/components/resource-list).

### Alignment

Column content types are built into the component props so the following alignment rules are followed:

* Numerical = Right aligned
* Textual data = Left aligned
* Align headers with their related data
* Don’t center align

---

## Content guidelines

Headers should:

* Be informative and descriptive
* Concise and scannable
* Include units of measurement symbols so they aren’t repeated throughout the columns
* Use sentence case (first word capitalized, rest lowercase)

Do

Temperature °C

Don't

Temperature

Column content should:

* Be concise and scannable
* Not include units of measurement symbols (put those symbols in the headers)
* Use sentence case (first word capitalized, rest lowercase)

### Decimals

Keep decimals consistent. For example, don’t use 3 decimals in one row and 2 in others.

---

## Related components

* To create an actionable list of related items that link to details pages, such as a list of customers, use the [resource list component](https://polaris.shopify.com/components/resource-list).

---

## Accessibility

### Structure

Native HTML tables provide a large amount of structural information to screen reader users. Merchants who rely on screen readers can navigate tables and identify relationships between data cells (<td>) and headers (<th>) using keys specific to their screen reader.

Sortable tables use the aria-sort attribute to convey which columns are sortable (and in what direction). They also use aria-label on sorting buttons to convey what activating the button will do.

Do

Use tables for tabular data.

Don't

Use tables for layout. For a table-like layout that doesn’t use table HTML elements, use the [resource list component](https://polaris.shopify.com/components/resource-list).

### Keyboard support

Sorting controls for the data table component are implemented with native HTML buttons.

* Give buttons keyboard focus with the `tab` key (or `shift` + `tab` when tabbing backwards)
* Activate buttons with the `enter`/`return` and `space` keys