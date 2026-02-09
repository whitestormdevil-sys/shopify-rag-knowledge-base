---
source: https://polaris.shopify.com/components/selection-and-input/filters
---

# Filters

Filters is a composite component that filters the items of a list or table.

### Filters component examples

With a resource listWith a data tableWith children contentWith children content and unsaved changesDisabledWith some disabledWith query field hiddenWith query field disabled

Edit in CodeSandbox

ReactHTML

```
import {
  ChoiceList,
  TextField,
  RangeSlider,
  LegacyCard,
  ResourceList,
  Filters,
  Avatar,
  Text,
} from '@shopify/polaris';
import {useState, useCallback} from 'react';

function FiltersWithAResourceListExample() {
  const [accountStatus, setAccountStatus] = useState<string[] | undefined>(
    undefined,
  );
  const [moneySpent, setMoneySpent] = useState<[number, number] | undefined>(
    undefined,
  );
  const [taggedWith, setTaggedWith] = useState<string | undefined>(undefined);
  const [queryValue, setQueryValue] = useState<string | undefined>(undefined);

  const handleAccountStatusChange = useCallback(
    (value: string[]) => setAccountStatus(value),
    [],
  );
  const handleMoneySpentChange = useCallback(
    (value: [number, number]) => setMoneySpent(value),
    [],
  );
  const handleTaggedWithChange = useCallback(
    (value: string) => setTaggedWith(value),
    [],
  );
  const handleFiltersQueryChange = useCallback(
    (value: string) => setQueryValue(value),
    [],
  );
  const handleAccountStatusRemove = useCallback(
    () => setAccountStatus(undefined),
    [],
  );
  const handleMoneySpentRemove = useCallback(
    () => setMoneySpent(undefined),
    [],
  );
  const handleTaggedWithRemove = useCallback(
    () => setTaggedWith(undefined),
    [],
  );
  const handleQueryValueRemove = useCallback(
    () => setQueryValue(undefined),
    [],
  );
  const handleFiltersClearAll = useCallback(() => {
    handleAccountStatusRemove();
    handleMoneySpentRemove();
    handleTaggedWithRemove();
    handleQueryValueRemove();
  }, [
    handleAccountStatusRemove,
    handleMoneySpentRemove,
    handleQueryValueRemove,
    handleTaggedWithRemove,
  ]);

  const filters = [
    {
      key: 'accountStatus',
      label: 'Account status',
      filter: (
        <ChoiceList
          title="Account status"
          titleHidden
          choices={[
            {label: 'Enabled', value: 'enabled'},
            {label: 'Not invited', value: 'not invited'},
            {label: 'Invited', value: 'invited'},
            {label: 'Declined', value: 'declined'},
          ]}
          selected={accountStatus || []}
          onChange={handleAccountStatusChange}
          allowMultiple
        />
      ),
      shortcut: true,
    },
    {
      key: 'taggedWith',
      label: 'Tagged with',
      filter: (
        <TextField
          label="Tagged with"
          value={taggedWith}
          onChange={handleTaggedWithChange}
          autoComplete="off"
          labelHidden
        />
      ),
      shortcut: true,
    },
    {
      key: 'moneySpent',
      label: 'Money spent',
      filter: (
        <RangeSlider
          label="Money spent is between"
          labelHidden
          value={moneySpent || [0, 500]}
          prefix="$"
          output
          min={0}
          max={2000}
          step={1}
          onChange={handleMoneySpentChange}
        />
      ),
    },
  ];

  const appliedFilters = [];
  if (!isEmpty(accountStatus)) {
    const key = 'accountStatus';
    appliedFilters.push({
      key,
      label: disambiguateLabel(key, accountStatus),
      onRemove: handleAccountStatusRemove,
    });
  }
  if (!isEmpty(moneySpent)) {
    const key = 'moneySpent';
    appliedFilters.push({
      key,
      label: disambiguateLabel(key, moneySpent),
      onRemove: handleMoneySpentRemove,
    });
  }
  if (!isEmpty(taggedWith)) {
    const key = 'taggedWith';
    appliedFilters.push({
      key,
      label: disambiguateLabel(key, taggedWith),
      onRemove: handleTaggedWithRemove,
    });
  }

  return (
    <div style={{height: '568px'}}>
      <LegacyCard>
        <ResourceList
          resourceName={{singular: 'customer', plural: 'customers'}}
          filterControl={
            <Filters
              queryValue={queryValue}
              filters={filters}
              appliedFilters={appliedFilters}
              onQueryChange={handleFiltersQueryChange}
              onQueryClear={handleQueryValueRemove}
              onClearAll={handleFiltersClearAll}
            />
          }
          flushFilters
          items={[
            {
              id: '341',
              url: '#',
              name: 'Mae Jemison',
              location: 'Decatur, USA',
            },
            {
              id: '256',
              url: '#',
              name: 'Ellen Ochoa',
              location: 'Los Angeles, USA',
            },
          ]}
          renderItem={(item) => {
            const {id, url, name, location} = item;
            const media = <Avatar customer size="md" name={name} />;

            return (
              <ResourceList.Item
                id={id}
                url={url}
                media={media}
                accessibilityLabel={`View details for ${name}`}
              >
                <Text as="h3" variant="bodyMd" fontWeight="bold">
                  {name}
                </Text>
                <div>{location}</div>
              </ResourceList.Item>
            );
          }}
        />
      </LegacyCard>
    </div>
  );

  function disambiguateLabel(key: string, value: any) {
    switch (key) {
      case 'moneySpent':
        return `Money spent is between $${value[0]} and $${value[1]}`;
      case 'taggedWith':
        return `Tagged with ${value}`;
      case 'accountStatus':
        return value?.map((val: string) => `Customer ${val}`).join(', ');
      default:
        return value;
    }
  }

  function isEmpty(
    value: string | string[] | [number, number] | undefined,
  ): boolean {
    if (Array.isArray(value)) {
      return value.length === 0;
    } else {
      return value === '' || value == null;
    }
  }
}
```

## Props

interface FiltersProps

queryValue?string
:   Currently entered text in the query field.

queryPlaceholder?string
:   Placeholder text for the query field.

focused?boolean
:   Whether the query field is focused.

filtersFilterInterface[]
:   Available filters added to the filter bar. Shortcut filters are pinned to the front of the bar.

appliedFilters?AppliedFilterInterface[]
:   Applied filters which are rendered as filter pills. The remove callback is called with the respective key.

onQueryChange(queryValue: string) => void
:   Callback when the query field is changed.

onQueryClear() => void
:   Callback when the clear button is triggered.

onClearAll() => void
:   Callback when the reset all button is pressed.

onQueryBlur?() => void
:   Callback when the query field is blurred.

onQueryFocus?() => void
:   Callback when the query field is focused.

children?ReactNode
:   The content to display inline with the controls.

disabled?boolean
:   Disable all filters.

hideFilters?boolean
:   Hide filter bar for applied filters.

hideQueryField?boolean
:   Hide the query field.

disableQueryField?boolean
:   Disable the query field.

disableFilters?boolean
:   Disable the filters.

borderlessQueryField?boolean
:   Whether the text field should be borderless. Should be true when used as part of the IndexFilters component.

loading?boolean
:   Whether an asyncronous task is currently being run.

mountedState?TransitionStatus

onAddFilterClick?() => void
:   Callback when the add filter button is clicked.

closeOnChildOverlayClick?boolean
:   Whether the filter should close when clicking inside another Popover.

selectedViewName?string
:   Deprecated

    The name of the currently selected view.

Merchants use filters to:

* view different subsets of items in a list or table
* filter by typing into a text field
* filter by selecting filters or promoted filters

The way that merchants interact with filters depends on the components that you decide to incorporate. In its simplest form, filters includes a text field and a set of filters, which can be displayed in different ways. What the filters are and how they’re exposed to merchants is flexible.

---

## Accessibility

The filters component relies on the accessibility features of multiple other components:

* [Text field](https://polaris.shopify.com/components/selection-and-input/text-field)
* [Button](https://polaris.shopify.com/components/actions/button)
* [Popover](https://polaris.shopify.com/components/overlays/popover)

### Maintain accessibility with custom features

Since custom HTML can be passed to the component for additional actions, ensure that the filtering system you build is accessible as a whole.

All merchants must:

* be able to identify and understand labels for all controls
* be notified of state changes
* be able to complete all actions with the keyboard

---

## Best practices

The filters component should:

* help reduce merchant effort by promoting the filtering categories that are most commonly used
* include no more than 2 or 3 promoted filters
* consider small screen sizes when designing the interface for each filter and the total number filters to include
* use children only for content that’s related or relevant to filtering

---

## Content guidelines

### Text field

The text field should be clearly labeled so it’s obvious to merchants what they should enter into the field.

Do

* Filter orders

Don't

* Enter text here

### Filter badges

Use the name of the filter if the purpose of the name is clear on its own. For example, when you see a filter badge that reads **Fulfilled**, it’s intuitive that it falls under the Fulfillment status category.

Do

* Fulfilled, Unfulfilled

Don't

* Fulfillment: Fulfilled, Unfulfilled

If the filter name is ambiguous on its own, add a descriptive word related to the status. For example, **Low** doesn’t make sense out of context. Add the word “risk” so that merchants know it’s from the Risk category.

Do

* High risk, Low risk

Don't

* High, Low

Group tags from the same category together.

Do

* (Unfulfilled, Fulfilled)

Don't

* (Unfulfilled) (fulfilled)

If all tag pills selected: truncate in the middle

Do

* Paid, par… unpaid

Don't

* All payment status filters selected, Paid, unpa…