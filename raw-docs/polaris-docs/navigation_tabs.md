---
source: https://polaris.shopify.com/components/navigation/tabs
---

# Tabs

Use to alternate among related views within the same context.

### Tabs component examples

DefaultInside of a CardFittedWith actionsWith badge contentWith custom disclosure

Use for most cases, especially when the number of tabs may be more than three.

Edit in CodeSandbox

ReactHTML

```
import {LegacyCard, Tabs} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function TabsDefaultExample() {
  const [selected, setSelected] = useState(0);

  const handleTabChange = useCallback(
    (selectedTabIndex: number) => setSelected(selectedTabIndex),
    [],
  );

  const tabs = [
    {
      id: 'all-customers-1',
      content: 'All',
      accessibilityLabel: 'All customers',
      panelID: 'all-customers-content-1',
    },
    {
      id: 'accepts-marketing-1',
      content: 'Accepts marketing',
      panelID: 'accepts-marketing-content-1',
    },
    {
      id: 'repeat-customers-1',
      content: 'Repeat customers',
      panelID: 'repeat-customers-content-1',
    },
    {
      id: 'prospects-1',
      content: 'Prospects',
      panelID: 'prospects-content-1',
    },
  ];

  return (
    <Tabs tabs={tabs} selected={selected} onSelect={handleTabChange}>
      <LegacyCard.Section title={tabs[selected].content}>
        <p>Tab {selected} selected</p>
      </LegacyCard.Section>
    </Tabs>
  );
}
```

## Props

interface TabsProps

tabsTabProps[]
:   The items that map to each Tab.

children?React.ReactNode
:   Content to display in tabs.

selectednumber
:   The index of the currently selected Tab.

disabled?boolean
:   Whether the Tabs are disabled or not.

canCreateNewView?boolean
:   Whether to show the add new view Tab.

newViewAccessibilityLabel?string
:   Label for the new view Tab. Will override the default of "Create new view".

fitted?boolean
:   Fit tabs to container.

disclosureText?string
:   Text to replace disclosures horizontal dots.

disclosureZIndexOverride?number
:   Override z-index of popovers and tooltips.

onSelect?(selectedTabIndex: number) => void
:   Optional callback invoked when a Tab becomes selected.

onCreateNewView?(value: string) => Promise<boolean>
:   Optional callback invoked when a merchant saves a new view from the Modal.

## Best practices

Tabs should:

* Represent the same kind of content, such as a list-view with different filters applied. Don’t use tabs to group content that is dissimilar.
* Only be active one at a time.
* Not force merchants to jump back and forth to do a single task. Merchants should be able to complete their work and find what they need under each tab.
* Not be used for primary navigation.

---

## Content guidelines

### Tabs

Tabs should:

* Be clearly labeled to help differentiate the different sections beneath them.
* Have short and scannable labels, generally kept to single word.
* Relate to the section of Shopify they’re on. Imagine the page section title is an invisible noun after the tab. For example, the tabs for the orders section are:

  + All
  + Open
  + Unfulfilled
  + Unpaid

The tabs for the gift cards section are:

* All
* New
* Partially used
* Used
* Disabled

And for the customers section, the tabs are:

* All
* New
* Returning
* Abandoned checkouts
* Email subscribers

Where possible, follow this pattern when writing tabs.