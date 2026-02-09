---
source: https://polaris.shopify.com/components/navigation/navigation
---

# Navigation

The navigation component is used to display the primary navigation in the sidebar of the [frame](https://polaris.shopify.com/components/deprecated/frame) of an application. Navigation includes a list of links that merchants use to move between sections of the application.

## Deprecated

This component is no longer supported. Please use the [App Bridge Navigation
Menu
API](https://shopify.dev/docs/api/app-bridge-library/reference/navigation-menu)
instead.

### Navigation component examples

DefaultWith multiple secondary navigationsWith an active root item with secondary navigation itemsWith a secondary action for a section and a section titleWith a secondary action for an itemWith multiple secondary actionsWith section rollupWith section separatorWith various states and secondary elementsWith truncation active for various statesWith aria-labelledbyUsing Major icons

Use to present a navigation menu in the [frame](https://polaris.shopify.com/components/deprecated/frame).

Edit in CodeSandbox

ReactHTML

```
import {Frame, Navigation} from '@shopify/polaris';
import {HomeIcon, OrderIcon, ProductIcon} from '@shopify/polaris-icons';
import React from 'react';

function NavigationExample() {
  return (
    <Frame>
      <Navigation location="/">
        <Navigation.Section
          items={[
            {
              url: '#',
              label: 'Home',
              icon: HomeIcon,
            },
            {
              url: '#',
              excludePaths: ['#'],
              label: 'Orders',
              icon: OrderIcon,
              badge: '15',
            },
            {
              url: '#',
              excludePaths: ['#'],
              label: 'Products',
              icon: ProductIcon,
            },
          ]}
        />
      </Navigation>
    </Frame>
  );
}
```

## Required components

The navigation component must be passed to the [frame](https://polaris.shopify.com/components/deprecated/frame) component. The mobile version of the navigation component appears in the [top bar](https://polaris.shopify.com/components/deprecated/top-bar) component.

---

## Best practices

The navigation component should:

* Contain primary navigation items that perform an action when clicked. Each action should navigate to a URL or trigger another action like a modal overlay.
* Only use secondary actions for supplementary actions to the primary actions.
* Provide a non-primary link or action as a secondary action to a section or an item.
* Group navigation items into sections based on related categories.
* Use a section title to clarify the category of a section.
* Use a major icon for item actions.
* Use a minor icon for secondary actions.
* Use the provided navigation section component to group navigation items.
* Not add additional components, like [badge](/components/feedback-indicators/badge), in navigation items. Example: Don‘t add the [New badge](/patterns-legacy/new-badge).

---

## Content guidelines

Navigation should:

* Use sentence case for primary and secondary navigation items

Do

* Online store

Don't

* Online Store

* Use as few words as possible to describe each item label

Do

* Products

Don't

* Products in your store

* Use all caps for section labels

Do

* SALES CHANNELS

Don't

* Sales channels

---

## Navigation section

A navigation section groups together related navigation items. Navigation sections can be clarified by a heading. Merchants can use a section to easily find navigation items within a specific category.

### Section properties

| Prop | Type | Description |
| --- | --- | --- |
| items | [Item[]](#type-item) | A collection of navigation items to be rendered inside the section |
| icon | IconProps['source'] | An icon to be displayed next to the section title |
| title | string | A string property providing a title for the navigation section |
| fill | boolean | A boolean property indicating whether the section should take up all vertical space available |
| rollup | [Rollup](#type-rollup) | An object determining the collapsing behavior of the navigation section |
| action | [Action](#type-action) | Renders an icon-only action as a supplementary action next to the section title |
| separator | boolean | A boolean property indicating whether the section should have a visual separator |

### Navigation section item

The content of the navigation component consists of navigation items. Each item is a link or action a merchant can take.

#### Item properties

| Prop | Type | Description |
| --- | --- | --- |
| url | string | A location for the navigation item to navigate to when clicked |
| matches | boolean | A boolean property indicating whether the navigation item should respond to a closely matching location property |
| exactMatch | boolean | A boolean property indicating whether the navigation item should respond to an exactly matching location property |
| matchPaths | string[] | A string property providing a collection of additional paths for the navigation item to respond to |
| excludePaths | string[] | A string property providing an explicit collection of paths the navigation item should not respond to |
| icon | IconProps['source'] | An icon to be displayed next to the navigation. Please prefer minor icons here. If a major icon has to be used, set the shouldResizeIcon prop to true |
| badge | string | null | A string property allowing content to be displayed in a badge next to the navigation item |
| label | string | A string property allowing content to be displayed as link text in the navigation item |
| disabled | boolean | A boolean property indicating whether the navigation item is disabled |
| new | boolean | Indicate whether the navigation item is new by adding an indicator dot to the parent and badge to the item (overwritten by the badge prop) |
| accessibilityLabel | string | A visually hidden label for screen readers to understand the content of a navigation item |
| selected | boolean | A boolean property indicating whether the navigation item is the currently-selected item |
| shouldResizeIcon | boolean | Will allow for major icons to be displayed at the same size as minor icons |
| subNavigationItems | [SubNavigationItem[]](#sub-navigation-item) | A collection of navigation items rendered as nested secondary navigation items |
| secondaryAction | [SecondaryAction](#secondary-action) | Renders an icon-only action as a supplementary action next to a navigation item |
| secondaryActions | [SecondaryAction[]](#secondary-action) | Renders one or two icon-only actions as supplementary actions next to a navigation item |
| onClick() | function | A callback function to handle clicking on a navigation item |
| truncateText | boolean | A boolean property to allow text that exceeds the width of the navigation item to be truncated with ellipsis |
| displayActionsOnHover | boolean | A boolean to only display secondary actions when being the nabigation item is hovered (Only on desktop) |

### SubNavigationItem

#### Properties

| Prop | Type | Description |
| --- | --- | --- |
| url | string | A location for the navigation item to navigate to when clicked |
| matches | boolean | A boolean property indicating whether the navigation item should respond to a closely matching location property |
| exactMatch | boolean | A boolean property indicating whether the navigation item should respond to an exactly matching location property |
| matchPaths | string[] | A string property providing a collection of additional paths for the navigation item to respond to |
| excludePaths | string[] | A string property providing an explicit collection of paths the navigation item should not respond to |
| external | boolean | Indicates whether this is an external link. If it is, an external link icon will be shown next to the label |
| label | string | A string property allowing content to be displayed as link text in the navigation item |
| disabled | boolean | A boolean property indicating whether the navigation item is disabled |
| new | boolean | Indicate whether the navigation item is new by adding an indicator dot to the parent and badge to the item (overwritten by the badge prop) |
| onClick() | function | A callback function to handle clicking on a navigation item |

### SecondaryAction

#### Properties

| Prop | Type | Description |
| --- | --- | --- |
| url | string | A location for the navigation item to navigate to when clicked |
| accessibilityLabel | string | A visually hidden label for screen readers to understand the content of a navigation item |
| icon | IconProps['source'] | An icon to be displayed next to the navigation. Please prefer minor icons here. If a major icon has to be used, set the shouldResizeIcon prop to true |
| onClick() | function | A callback function to handle clicking on a navigation item |
| tooltip | [TooltipProps](https://polaris.shopify.com/components/tooltip#navigation) | Options for displaying a tooltip when you hover over the action button |

### Navigation section rollup

Rollup allows items in a navigation section to roll up and be revealed when they are of use to the merchant.

#### Rollup properties

| Prop | Type | Description |
| --- | --- | --- |
| after | number | A number of items after which the navigation section should be collapsed |
| view | string | A string property providing content for the section view action |
| hide | string | A string property providing content for the section hide action |
| activePath | string | A string property representing the current URL of your application |

### Navigation section action

Action allows a complementary icon-only action to render next to the section title.

#### Action properties

| Prop | Type | Description |
| --- | --- | --- |
| icon | IconProps['source'] | An icon to be displayed as the content of the action |
| accessibilityLabel | string | A visually hidden label for screen readers to understand the content of the action |
| onClick() | function | A callback function to handle clicking on the action |
| tooltip | [TooltipProps](https://polaris.shopify.com/components/tooltip#navigation) | Options for displaying a tooltip when you hover over the action button |

---

## Related components

* To provide the structure for the navigation component, including the left sidebar and the top bar use the [frame](https://polaris.shopify.com/components/deprecated/frame) component.
* To display the navigation component on small screens, to provide search and a user menu, or to theme the [frame](https://polaris.shopify.com/components/deprecated/frame) component to reflect an application’s brand, use the [top bar](https://polaris.shopify.com/components/deprecated/top-bar) component.
* To tell merchants their options once they have made changes to a form on the page use the [contextual save bar](https://polaris.shopify.com/components/deprecated/contextual-save-bar) component.
* To provide quick, at-a-glance feedback on the outcome of an action, use the [toast](https://polaris.shopify.com/components/deprecated/toast) component.
* To indicate to merchants that a page is loading or an upload is processing use the [loading](https://polaris.shopify.com/components/deprecated/loading) component.
* To alternate among related views within the same context, use the [tabs](https://polaris.shopify.com/components/tabs) component.
* To embed a single action or link within a larger span of text, use the [link](https://polaris.shopify.com/components/link) component.