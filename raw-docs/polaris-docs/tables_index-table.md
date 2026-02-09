---
source: https://polaris.shopify.com/components/tables/index-table
---

# Index table

An index table displays a collection of objects of the same type, like orders or products. The main job of an index table is to help merchants get an at-a-glance of the objects to perform actions or navigate to a full-page representation of it.

### Upgrade to Polaris Web Components

Index table is now available as a composition pattern using web components.

[Explore Index table](https://shopify.dev/docs/api/app-home/patterns/compositions/index-table)

### Index table component examples

DefaultWith saved views, search, filtering, and sortingWith edit columns buttonWith disabled rowsSmall screenSmall screen with saved views, search, filtering, and sortingWith empty stateWith bulk actionsWith multiple promoted bulk actionsWith bulk actions and selection across pagesWith selection and no bulk actionsWith loading stateWith filteringWith sticky last columnWith row navigation linkWithout checkboxesWith subheadersWith paginationWith nested rowsWith sticky scroll barWith pagination and bulk actions

An index table with simple items and no bulk actions, sorting, or filtering.

Edit in CodeSandbox

ReactHTML

```
import {
  IndexTable,
  LegacyCard,
  useIndexResourceState,
  Text,
  Badge,
} from '@shopify/polaris';
import React from 'react';

function SimpleIndexTableExample() {
  const orders = [
    {
      id: '1020',
      order: '#1020',
      date: 'Jul 20 at 4:34pm',
      customer: 'Jaydon Stanton',
      total: '$969.44',
      paymentStatus: <Badge progress="complete">Paid</Badge>,
      fulfillmentStatus: <Badge progress="incomplete">Unfulfilled</Badge>,
    },
    {
      id: '1019',
      order: '#1019',
      date: 'Jul 20 at 3:46pm',
      customer: 'Ruben Westerfelt',
      total: '$701.19',
      paymentStatus: <Badge progress="partiallyComplete">Partially paid</Badge>,
      fulfillmentStatus: <Badge progress="incomplete">Unfulfilled</Badge>,
    },
    {
      id: '1018',
      order: '#1018',
      date: 'Jul 20 at 3.44pm',
      customer: 'Leo Carder',
      total: '$798.24',
      paymentStatus: <Badge progress="complete">Paid</Badge>,
      fulfillmentStatus: <Badge progress="incomplete">Unfulfilled</Badge>,
    },
  ];
  const resourceName = {
    singular: 'order',
    plural: 'orders',
  };

  const {selectedResources, allResourcesSelected, handleSelectionChange} =
    useIndexResourceState(orders);

  const rowMarkup = orders.map(
    (
      {id, order, date, customer, total, paymentStatus, fulfillmentStatus},
      index,
    ) => (
      <IndexTable.Row
        id={id}
        key={id}
        selected={selectedResources.includes(id)}
        position={index}
      >
        <IndexTable.Cell>
          <Text variant="bodyMd" fontWeight="bold" as="span">
            {order}
          </Text>
        </IndexTable.Cell>
        <IndexTable.Cell>{date}</IndexTable.Cell>
        <IndexTable.Cell>{customer}</IndexTable.Cell>
        <IndexTable.Cell>
          <Text as="span" alignment="end" numeric>
            {total}
          </Text>
        </IndexTable.Cell>
        <IndexTable.Cell>{paymentStatus}</IndexTable.Cell>
        <IndexTable.Cell>{fulfillmentStatus}</IndexTable.Cell>
      </IndexTable.Row>
    ),
  );

  return (
    <LegacyCard>
      <IndexTable
        resourceName={resourceName}
        itemCount={orders.length}
        selectedItemsCount={
          allResourcesSelected ? 'All' : selectedResources.length
        }
        onSelectionChange={handleSelectionChange}
        headings={[
          {title: 'Order'},
          {title: 'Date'},
          {title: 'Customer'},
          {title: 'Total', alignment: 'end'},
          {title: 'Payment status'},
          {title: 'Fulfillment status'},
        ]}
      >
        {rowMarkup}
      </IndexTable>
    </LegacyCard>
  );
}
```

## Props

interface IndexTableProps

headings[T, ...T[]]<IndexTableHeadingTitleString | IndexTableHeadingTitleNode>

promotedBulkActions?(MenuGroupDescriptor | BulkAction)[]

bulkActions?(ActionListSection | BulkAction)[]

children?React.ReactNode

emptyState?React.ReactNode

sort?React.ReactNode

paginatedSelectAllActionText?string

paginatedSelectAllText?string

lastColumnSticky?boolean

selectable?boolean

sortable?boolean[]
:   List of booleans, which maps to whether sorting is enabled or not for each column. Defaults to false for all columns.

defaultSortDirection?'ascending' | 'descending'
:   The direction to sort the table rows on first click or keypress of a sortable column heading. Defaults to descending.

    Defaults to 'descending'.

sortDirection?'ascending' | 'descending'
:   The current sorting direction.

sortColumnIndex?number
:   The index of the heading that the table rows are sorted by.

onSort?(headingIndex: number, direction: 'ascending' | 'descending') => void
:   Callback fired on click or keypress of a sortable column heading.

sortToggleLabels?IndexTableSortToggleLabels
:   Optional dictionary of sort toggle labels for each sortable column, with ascending and descending label,
    with the key as the index of the column.

hasZebraStriping?boolean
:   Add zebra striping to table rows.

pagination?Omit<PaginationProps, 'type'>
:   Properties to enable pagination at the bottom of the table.

itemCountnumber

selectedItemsCount?number | "All"

resourceName?{ singular: string; plural: string; }

loading?boolean

hasMoreItems?boolean

condensed?boolean

onSelectionChange?(selectionType: SelectionType, toggleType: boolean, selection?: string | Range, position?: number) => void

Index tables can also:

* Support [customized index rows and columns](https://polaris.shopify.com/components/resource-item)
* Include bulk actions so merchants can act on multiple objects at once
* Support sorting and [filtering](https://polaris.shopify.com/components/filters) of long lists
* Be paired with pagination to make long lists digestible

---

## Build

Using an index table in a project involves combining the following components and subcomponents:

* IndexTable
* [IndexTable.Row](#index-table-row)
* [IndexTable.Cell](#index-table-cell)
* [Filters](/components/selection-and-input/filters) (optional)
* [IndexFilters](/components/selection-and-input/index-filters) (optional)
* [Pagination](/components/navigation/pagination) (optional)

The index table component provides the UI elements for list selection, sorting, filtering, and pagination, but doesn’t provide the logic for these operations. When a sort option is changed, filter added, or second page requested, you’ll need to handle that event (including any network requests) and then update the component with new props.

---

## Purpose

Shopify is organized around objects that represent merchants' businesses, like customers, products, and orders. Each individual order, for example, is given a dedicated page that can be linked to. In Shopify, we call these types of objects *resources*, and we call the object’s dedicated page its *details page*.

### Problem

Take orders as an example. Merchants may have a lot of them. They need a way to scan their orders, view the different attributes on each order, and find out which ones need action first. In other words, they need a way find an individual order, call up more information about it, and take action on it.

### Solution

Index tables function as:

* A content format, presenting a set of individual resources with multiple columns of information for each
* A system for taking action on one or more individual resources
* A way to navigate to an individual resource’s details page

Because a details page displays all the content and actions for an individual resource, you can think of a resource list as a summary of these details pages. In this way resource lists bridge a middle level in Shopify’s navigation hierarchy.

---

## Best practices

Index tables should:

* Have items that perform an action when clicked. The action should navigate to the resource’s details page or otherwise provide more detail about the item.
* [Customize the content and layout](https://polaris.shopify.com/components/resource-item) of their items rows to surface information to support merchants’ needs.
* Support sorting if the list can be long, and especially if different merchant tasks benefit from different sort orders.
* Support [filtering](https://polaris.shopify.com/components/filters) if the list can be long.
* Paginate when the current list contains more than 50 items.
* Use the [skeleton page](https://polaris.shopify.com/components/skeleton-page) component on initial page load for the rest of the page if the loading prop is true and items are processing.
* Numeric cells and titles should be right aligned with the [Text](https://polaris.shopify.com/components/text) component
* Numeric cells should use the numeric style with the [Text](https://polaris.shopify.com/components/text) component

Index tables can optionally:

* Provide bulk actions for tasks that are often applied to many list items at once. For example, merchants may want to add the same tag to a large number of products.
* Hide bulk actions on small screens using the condensed prop. We only recommend hiding bulk actions on screens smaller than 490px using our breakpoints-sm value: condensed={useBreakpoints().smDown}.
  + Hiding bulk actions means a merchant can’t select multiple items at once, so it should only be used when the bulk actions are not essential to the merchant’s workflow.

---

## Content guidelines

Index tables should:

* Identify the type of resource, usually with a heading

Do

* Products
* Showing 50 products

Don't

* *No heading*

* Indicate when not all members of a resource are being shown. For a card summarizing and linking to recently purchased products:

Do

* Popular products this week

Don't

* Products

* Follow the verb + noun formula for bulk actions
* Follow the [content guidelines for filter options and applied filters](https://polaris.shopify.com/components/filters#content-guidelines)

---

## IndexTable.Row

An IndexTable.Row is used to render a row representing an item within an IndexTable

### IndexTable.Row properties

| Prop | Type | Description |
| --- | --- | --- |
| children | ReactNode | Table header or data cells |
| id | string | A unique identifier for the row |
| selected? | boolean | "indeterminate" | A boolean property indicating whether the row or it's related rows are selected |
| position | number | The zero-indexed position of the row. Used for Shift key multi-selection as well as selection of a range of rows when a selectionRange is set. |
| tone? | "subdued" | "success" | "warning" | "critical" | Whether the row should visually indicate its status with a background color |
| disabled? | boolean | Whether the row should be disabled |
| selectionRange? | [number, number] | A tuple array with the first and last index of the range of other rows that the row describes. All non-disabled rows in the range are selected when the row with a selection range set is selected. |
| rowType? | "data" | "subheader" | "child" | Indicates the relationship or role of the row's contents. A rowType of "subheader" looks and behaves the same as the table header. Rows of type "child" are indented. Defaults to "data". |
| accessibilityLabel? | string | Label set on the row's checkbox. Defaults to "Select {resourceName}" |
| onClick? | () => void | Callback fired when the row is clicked. Overrides the default click behaviour. |
| onNavigation? | (id: string) => void | Callback fired when the row is clicked and contains an anchor element with the data-primary-link property set |

## IndexTable.Cell

An IndexTable.Cell is used to render a single cell within an IndexTable.Row

### IndexTable.Cell properties

| Prop | Type | Description |
| --- | --- | --- |
| as? | 'th' | 'td' | The table cell element to render. Render the cell as a th if it serves as a subheading. Defaults to td. |
| id? | string | The unique ID to set on the cell element |
| children? | ReactNode | The cell contents |
| className? | string | Adds a class to the cell. Use to set a custom cell width. |
| flush? | boolean | Whether the cell padding should be removed. Defaults to false. |
| colSpan? | [HTMLTableCellElement['colSpan']](https://www.w3schools.com/tags/att_colspan.asp) | For subheader cells -- The number of the columns that the cell element should extend to within the row. |
| scope? | [HTMLTableCellElement['scope']](https://www.w3schools.com/tags/att_scope.asp) | For subheader cells -- Indicates the cells that the th element relates to |
| headers? | [HTMLTableCellElement['headers']](https://www.w3schools.com/tags/att_headers.asp) | A space-separated list of the th cell IDs that describe or apply to it. Use for cells within a row that relate to a subheader cell in addition to their column header. |

---

## Related components

* To create an actionable list of related items that link to details pages, such as a list of customers, use the [resource list component](https://polaris.shopify.com/components/lists/resource-list)
* To present structured data for comparison and analysis, like when helping merchants to gain insights or review analytics, use the [data table component](https://polaris.shopify.com/components/tables/data-table)
* To display a simple list of related content, [use the list component](https://polaris.shopify.com/components/lists/list)

---

## Accessibility

### Structure

The IndexTable is an actionable, filterable, and sortable table widget that supports row selection with [subheaders](https://www.w3.org/WAI/tutorials/tables/multi-level/). To ensure that the power of this table is accessible to all merchants when implementing IndexTable.Row subheaders, set the following props on IndexTable.Cell that are appropriate for the enhancement you are implementing.

Merchants can select a group of rows at once by clicking or `Space` keypressing a subheader row's checkbox. To indicate that an IndexTable.Row serves as a subheader for 1 or more rows below it, set the:

* Zero-indexed table position of the first and last IndexTable.Row described by the subheader IndexTable.Row as a tuple array on its selectionRange prop
* Unique id on the IndexTable.Cell that contains the subheader content
* Element tag to "th" on the as prop of the subheader IndexTable.Cell
* Subheader IndexTable.Cell scope prop to "colgroup"

To associate the subheader IndexTable.Row with each IndexTable.Cell that it describes, set the:

* Unique id provided to the subheader IndexTable.Cell on the headers prop of each related IndexTable.Cell (contained by an IndexTable.Row that's position is within the selectionRange) as well as the unique id of its corresponding column heading that you provided to the IndexTable headings prop

### Keyboard support

IndexTable also supports multi-selection of a range of rows by keypressing the `Shift` key. To select a range, press and hold the `Shift` key while you click or keypress the `Space` key on a row checkbox and then do the same on another row's checkbox. All selectable rows between the selected checkboxes will also be selected.