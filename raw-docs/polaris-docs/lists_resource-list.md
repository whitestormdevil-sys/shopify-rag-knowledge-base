---
source: https://polaris.shopify.com/components/lists/resource-list
---

# Resource list

A resource list displays a collection of objects of the same type, like products or customers. The main job of a resource list is to help merchants find an object and navigate to a full-page representation of it.

### Resource list component examples

DefaultWith empty stateWith selection and no bulk actionsWith bulk actionsWith loading stateWith total countWith sortingWith alternate toolWith filteringWith a custom empty search result stateWith item shortcut actionsWith persistent item shortcut actionsWith multiselectWith all of its elementsWith paginationWith bulk actions and many itemsWith bulk actions and pagination

A resource list with simple items and no bulk actions, sorting, or filtering.

Edit in CodeSandbox

ReactHTML

```
import {
  LegacyCard,
  ResourceList,
  Avatar,
  ResourceItem,
  Text,
} from '@shopify/polaris';
import React from 'react';

function ResourceListExample() {
  return (
    <LegacyCard>
      <ResourceList
        resourceName={{singular: 'customer', plural: 'customers'}}
        items={[
          {
            id: '100',
            url: '#',
            name: 'Mae Jemison',
            location: 'Decatur, USA',
          },
          {
            id: '200',
            url: '#',
            name: 'Ellen Ochoa',
            location: 'Los Angeles, USA',
          },
        ]}
        renderItem={(item) => {
          const {id, url, name, location} = item;
          const media = <Avatar customer size="md" name={name} />;

          return (
            <ResourceItem
              id={id}
              url={url}
              media={media}
              accessibilityLabel={`View details for ${name}`}
            >
              <Text variant="bodyMd" fontWeight="bold" as="h3">
                {name}
              </Text>
              <div>{location}</div>
            </ResourceItem>
          );
        }}
      />
    </LegacyCard>
  );
}
```

## Props

interface ResourceListProps

itemsTItemType[]
:   Item data; each item is passed to renderItem.

filterControl?React.ReactNode

flushFilters?boolean
:   Whether to remove all padding around the filter controls. Should be true if using Filters, and false if using LegacyFilters.

emptyState?React.ReactNode
:   The markup to display when no resources exist yet. Renders when set and items is empty.

emptySearchState?React.ReactNode
:   The markup to display when no results are returned on search or filter of the list. Renders when `filterControl` is set, items are empty, and `emptyState` is not set.

    Defaults to EmptySearchResult.

resourceName?{ singular: string; plural: string; }
:   Name of the resource, such as customers or products.

promotedBulkActions?(MenuGroupDescriptor | BulkAction)[]
:   Up to 2 bulk actions that will be given more prominence.

bulkActions?(ActionListSection | BulkAction)[]
:   Actions available on the currently selected items.

selectedItems?string[] | 'All'
:   Collection of IDs for the currently selected items.

isFiltered?boolean
:   Whether or not the list has filter(s) applied.

selectable?boolean
:   Renders a Select All button at the top of the list and checkboxes in front of each list item. For use when bulkActions aren't provided. \*.

hasMoreItems?boolean
:   Whether or not there are more items than currently set on the items prop. Determines whether or not to set the paginatedSelectAllAction and paginatedSelectAllText props on the BulkActions component.

loading?boolean
:   Overlays item list with a spinner while a background action is being performed.

showHeader?boolean
:   Boolean to show or hide the header.

totalItemsCount?number
:   Total number of resources.

sortValue?string
:   Current value of the sort control.

sortOptions?string | StrictOption[]
:   Collection of sort options to choose from.

alternateTool?React.ReactNode
:   ReactNode to display instead of the sort control.

headerContent?string
:   Custom header text displayed above the list instead of the resource count.

onSortChange?(selected: string, id: string) => void
:   Callback when sort option is changed.

onSelectionChange?(selectedItems: string[] | 'All') => void
:   Callback when selection is changed.

renderItem(item: TItemType, id: string, index: number) => React.ReactNode
:   Function to render each list item, must return a ResourceItem component.

idForItem?(item: TItemType, index: number) => string
:   Function to customize the unique ID for each item.

resolveItemId?(item: TItemType) => string
:   Function to resolve the ids of items.

pagination?Omit<PaginationProps, 'type'>
:   Properties to enable pagination at the bottom of the list.

Resource lists can also:

* Support [customized list items](https://polaris.shopify.com/components/resource-item)
* Include bulk actions so merchants can act on multiple objects at once
* Support sorting and [filtering](https://polaris.shopify.com/components/filters) of long lists
* Be paired with pagination to make long lists digestible

---

## Build

Using a resource list in a project involves combining the following components and subcomponents:

* ResourceList
* [ResourceItem](https://polaris.shopify.com/components/resource-item) or a customized list item
* [Filters](https://polaris.shopify.com/components/filters) (optional)
* Pagination component (optional)

The resource list component provides the UI elements for list sorting, filtering, and pagination, but doesn’t provide the logic for these operations. When a sort option is changed, filter added, or second page requested, you’ll need to handle that event (including any network requests) and then update the component with new props.

---

## Purpose

Shopify is organized around objects that represent merchants businesses, like customers, products, and orders. Each individual order, for example, is given a dedicated page that can be linked to. In Shopify, we call these types of objects *resources*, and we call the object’s dedicated page its *details page*.

### Problem

Take orders as an example. Merchants may have a lot of them. They need a way to scan their orders, see what state they’re in and find out which ones need action first. In other words, they need a way find an individual order, call up more information about it, and take action on it.

### Solution

Resource lists function as:

* A content format, presenting a set of individual resources in a compact form
* A system for taking action on one or more individual resources
* A way to navigate to an individual resource’s details page

Because a details page displays all the content and actions for an individual resource, you can think of a resource list as a summary of these details pages. In this way resource lists bridge a middle level in Shopify’s navigation hierarchy.

#### A resource list isn’t a data table

On wide screens, a resource list often looks like a table, especially if some content is aligned in columns. Despite this, resource lists and data tables have different purposes.

A data table is a form of data visualization. It works best to present highly structured data for comparison and analysis.

If your use case is more about visualizing or analyzing data, use the [data table component](https://polaris.shopify.com/components/data-table). If your use case is more about finding and taking action on objects, use a resource list.

---

## Best practices

Resource lists can live in many places in Shopify. You could include a short resource list in a card summarizing recent marketing activities. You could also dedicate an entire page to a resource list like Shopify’s main products list.

Resource lists should:

* Have items that perform an action when clicked. The action should navigate to the resource’s details page or otherwise provide more detail about the item.
* [Customize the content and layout](https://polaris.shopify.com/components/resource-item) of their list items to support merchants’ needs.
* Support sorting if the list can be long, and especially if different merchant tasks benefit from different sort orders.
* Support [filtering](https://polaris.shopify.com/components/filters) if the list can be long.
* Paginate when the current list contains more than 50 items.
* Use the [skeleton page](https://polaris.shopify.com/components/skeleton-page) component on initial page load for the rest of the page if the loading prop is true and items are processing.

Resource lists can optionally:

* Provide bulk actions for tasks that are often applied to many list items at once. For example, merchants may want to add the same tag to a large number of products.

---

## Content guidelines

Resource lists should:

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

## Related components

* To present structured data for comparison and analysis, like when helping merchants to gain insights or review analytics, use the [data table component](https://polaris.shopify.com/components/tables/data-table)
* To display a simple list of related content, [use the list component](https://polaris.shopify.com/components/lists/list)