---
source: https://polaris.shopify.com/components/navigation/pagination
---

# Pagination

Use pagination to let merchants move through an ordered collection of items that has been split into pages. On the web, pagination uses buttons to move back and forth between pages. On iOS and Android, pagination uses infinite scrolling.

### Pagination component examples

DefaultWith keyboard navigationWith labelWith table type

Use for pagination of resources.

Edit in CodeSandbox

ReactHTML

```
import {Pagination} from '@shopify/polaris';
import React from 'react';

function PaginationExample() {
  return (
    <Pagination
      hasPrevious
      onPrevious={() => {
        console.log('Previous');
      }}
      hasNext
      onNext={() => {
        console.log('Next');
      }}
    />
  );
}
```

## Props

interface PaginationProps

nextKeys?Key[]
:   Keyboard shortcuts for the next button.

previousKeys?Key[]
:   Keyboard shortcuts for the previous button.

nextTooltip?string
:   Tooltip for the next button.

previousTooltip?string
:   Tooltip for the previous button.

nextURL?string
:   The URL of the next page.

previousURL?string
:   The URL of the previous page.

hasNext?boolean
:   Whether there is a next page to show.

hasPrevious?boolean
:   Whether there is a previous page to show.

accessibilityLabel?string
:   Accessible label for the pagination.

accessibilityLabels?AccessibilityLabels
:   Accessible labels for the buttons and UnstyledLinks.

onNext?() => void
:   Callback when next button is clicked.

onPrevious?() => void
:   Callback when previous button is clicked.

label?React.ReactNode
:   Text to provide more context in between the arrow buttons.

type?"table" | "page"
:   Layout structure of the component.

## Best practices

On all platforms, pagination should:

* Only be used for lists with more than 25 items

Web pagination should:

* Be placed at the bottom of a long list that has been split up into pages
* Pagination should navigate to the previous and next set of items in the paged list
* Hint when merchants are at the first or the last page by disabling the corresponding button

iOS and Android pagination should:

* Start loading items when merchants are close to the bottom, roughly 5 items from the end
* Show [a spinner](https://polaris.shopify.com/components/spinner) below the list to indicate that items have been requested

---

## Related components

* To see how pagination is used on a page, see the [page component](https://polaris.shopify.com/components/layout-and-structure/page)
* To add primary and secondary calls to action at the bottom of a page, see the [page actions component](https://polaris.shopify.com/components/actions/page-actions)
* The [resource list component](https://polaris.shopify.com/components/resource-list) is often combined with pagination to handle long lists of resources such as orders or customers
* To create stand-alone navigational links or calls to action, use the [button component](https://polaris.shopify.com/components/actions/button)
* To embed actions or pathways to more information within a sentence, use the [link component](https://polaris.shopify.com/components/link)