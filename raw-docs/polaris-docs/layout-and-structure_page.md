---
source: https://polaris.shopify.com/components/layout-and-structure/page
---

# Page

Use to build the outer wrapper of a page, including the page title and associated actions.

### Upgrade to Polaris Web Components

Page is now available as a framework-agnostic web component.

[Start using <s-page>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/page)

### Page component examples

DefaultWith custom primary actionWithout primary action in headerWith destructive secondary actionWith custom secondary actionWith tooltip actionWith subtitleWith external linkWithout paginationFull-widthNarrow widthWith action groupsWith content after title

Use for detail pages, which should have pagination and breadcrumbs, and also often have several actions.

Edit in CodeSandbox

ReactHTML

```
import {Page, Badge, LegacyCard} from '@shopify/polaris';
import React from 'react';

function PageExample() {
  return (
    <Page
      backAction={{content: 'Products', url: '#'}}
      title="3/4 inch Leather pet collar"
      titleMetadata={<Badge tone="success">Paid</Badge>}
      subtitle="Perfect for any pet"
      compactTitle
      primaryAction={{content: 'Save', disabled: true}}
      secondaryActions={[
        {
          content: 'Duplicate',
          accessibilityLabel: 'Secondary action label',
          onAction: () => alert('Duplicate action'),
        },
        {
          content: 'View on your store',
          onAction: () => alert('View on your store action'),
        },
      ]}
      actionGroups={[
        {
          title: 'Promote',
          actions: [
            {
              content: 'Share on Facebook',
              accessibilityLabel: 'Individual action label',
              onAction: () => alert('Share on Facebook action'),
            },
          ],
        },
      ]}
      pagination={{
        hasPrevious: true,
        hasNext: true,
      }}
    >
      <LegacyCard title="Credit card" sectioned>
        <p>Credit card information</p>
      </LegacyCard>
    </Page>
  );
}
```

## Props

interface PageProps

children?React.ReactNode
:   The contents of the page.

fullWidth?boolean
:   Remove the normal max-width on the page.

narrowWidth?boolean
:   Decreases the maximum layout width. Intended for single-column layouts.

titleHidden?boolean
:   Visually hide the title.

pageReadyAccessibilityLabel?string
:   A label to use for the page when the page is ready, used by screen readers. Will override the title prop if present.

filterActions?boolean
:   Enables filtering action list items.

primaryAction?any
:   Primary page-level action.

pagination?PaginationProps
:   Page-level pagination.

backAction?LinkAction | CallbackAction
:   Deprecated

    A back action link
    Use `breadcrumbs` prop instead as documented [here](https://shopify.dev/docs/api/app-bridge/previous-versions/actions/titlebar#using-titlebar-with-polaris).

secondaryActions?any
:   Collection of secondary page-level actions.

actionGroups?MenuGroupDescriptor[]
:   Collection of page-level groups of secondary actions.

additionalMetadata?any

onActionRollup?(hasRolledUp: boolean) => void
:   Callback that returns true when secondary actions are rolled up into action groups, and false when not.

title?string
:   Deprecated

    Page title, in large type
    Use `breadcrumbs` prop instead as documented [here](https://shopify.dev/docs/api/app-bridge/previous-versions/actions/titlebar#using-titlebar-with-polaris).

subtitle?string
:   Page subtitle, in regular type.

titleMetadata?React.ReactNode
:   Important status information shown immediately after the title.

compactTitle?boolean
:   Removes spacing between title and subtitle.

hasSubtitleMaxWidth?boolean
:   Whether or not to add a max-width to the subtitle. Gets calculated by
    the presence of either the secondaryActions or actionGroups props on the
    Header that consumes this component.

#### Tip

Check out the [new patterns section](https://polaris.shopify.com/patterns) to
learn how merchants prefer to select dates in different scenarios!

## Best practices

The page component should:

* Always provide a title for the page header.
* Always provide breadcrumbs when a page has a parent page.
* Be organized around a primary activity. If that primary activity is a single action, provide it as a primary button in the page header.
* Provide other page-level actions as secondary actions in the page header.
* When the page represents an object of a certain type, provide pagination links to the previous and next object of the same type.

---

## Content guidelines

### Title

Titles should:

* Describe the page in as few words as possible.
* Be the name of the object type (pluralized) when the page is a list of objects. For a list of orders, the page title should be “Orders”.
* Not be truncated.

### App icon

App icons should:

* Provide their app icon
* Only be provided for pages that are part of a Shopify app

### Breadcrumbs

The content of each breadcrumb link should be the title of the page to which it links.

### Page header actions

Page header action labels should be:

* Clear and predictable: merchants should be able to anticipate what will happen when they click a page action. Never deceive merchants by mislabeling an action.
* Action-led: they should always lead with a strong verb that encourages action. To provide enough context to merchants, use the {verb}+{noun} format.

Do

* Create order
* View in Postmates

Don't

* Create
* Postmates deliveries

* Short: for secondary actions, when the noun represents the same object as the page itself, a verb alone may be used. If there is ambiguity (such as with the verb “Cancel”), always use the {verb}+{noun} format.

  In the context of the orders list page:

Do

* Import
* Export

Don't

* Import orders
* Export orders

* Scannable: avoid unnecessary words and articles such as the, an, or a.

Do

Add menu item

Don't

Add a menu item

---

## Related components

* To lay out the content within a page, use the [layout component](https://polaris.shopify.com/components/layout-and-structure/layout)
* To add pagination within the context of a list or other page content, use the [pagination component](https://polaris.shopify.com/components/navigation/pagination)
* To add primary and secondary calls to action at the bottom of a page, see the [page actions component](https://polaris.shopify.com/components/actions/page-actions)

## Related patterns

* [App settings layout](/patterns/app-settings-layout)
* [Resource details layout](/patterns/resource-details-layout)