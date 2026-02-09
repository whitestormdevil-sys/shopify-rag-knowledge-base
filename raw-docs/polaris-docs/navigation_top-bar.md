---
source: https://polaris.shopify.com/components/navigation/top-bar
---

# Top bar

The top bar is a header component that allows merchants to search, access menus, and navigate by clicking on the logo. It’s always visible at the top of interfaces like Shopify or Shopify Plus. Third-party apps that use the top bar can customize the color to match their brand using the [app provider](https://polaris.shopify.com/components/app-provider) component and are required to use their own logo.

## Deprecated

This component is no longer supported.

### Top bar component examples

Default

Use to provide structure for the top of an application. Style the top bar component using the app provider component with a theme. Providing just the background key for the top bar component theme will result in intelligent defaults being set for complementary colors with contrasting text.

Edit in CodeSandbox

ReactHTML

```
import {TopBar, ActionList, Icon, Frame, Text} from '@shopify/polaris';
import {ArrowLeftIcon, QuestionCircleIcon} from '@shopify/polaris-icons';
import {useState, useCallback} from 'react';

function TopBarExample() {
  const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);
  const [isSecondaryMenuOpen, setIsSecondaryMenuOpen] = useState(false);
  const [isSearchActive, setIsSearchActive] = useState(false);
  const [searchValue, setSearchValue] = useState('');

  const toggleIsUserMenuOpen = useCallback(
    () => setIsUserMenuOpen((isUserMenuOpen) => !isUserMenuOpen),
    [],
  );

  const toggleIsSecondaryMenuOpen = useCallback(
    () => setIsSecondaryMenuOpen((isSecondaryMenuOpen) => !isSecondaryMenuOpen),
    [],
  );

  const handleSearchResultsDismiss = useCallback(() => {
    setIsSearchActive(false);
    setSearchValue('');
  }, []);

  const handleSearchChange = useCallback((value: string) => {
    setSearchValue(value);
    setIsSearchActive(value.length > 0);
  }, []);

  const handleNavigationToggle = useCallback(() => {
    console.log('toggle navigation visibility');
  }, []);
  const logo = {
    topBarSource:
      'https://cdn.shopify.com/s/files/1/2376/3301/files/Shopify_Secondary_Inverted.png',
    width: 86,
    url: '#',
    accessibilityLabel: 'Shopify',
  };

  const userMenuMarkup = (
    <TopBar.UserMenu
      actions={[
        {
          items: [{content: 'Back to Shopify', icon: ArrowLeftIcon}],
        },
        {
          items: [{content: 'Community forums'}],
        },
      ]}
      name="Dharma"
      detail="Jaded Pixel"
      initials="D"
      open={isUserMenuOpen}
      onToggle={toggleIsUserMenuOpen}
    />
  );

  const searchResultsMarkup = (
    <ActionList
      items={[{content: 'Shopify help center'}, {content: 'Community forums'}]}
    />
  );

  const searchFieldMarkup = (
    <TopBar.SearchField
      onChange={handleSearchChange}
      value={searchValue}
      placeholder="Search"
      showFocusBorder
    />
  );

  const secondaryMenuMarkup = (
    <TopBar.Menu
      activatorContent={
        <span>
          <Icon source={QuestionCircleIcon} />
          <Text as="span" visuallyHidden>
            Secondary menu
          </Text>
        </span>
      }
      open={isSecondaryMenuOpen}
      onOpen={toggleIsSecondaryMenuOpen}
      onClose={toggleIsSecondaryMenuOpen}
      actions={[
        {
          items: [{content: 'Community forums'}],
        },
      ]}
    />
  );

  const topBarMarkup = (
    <TopBar
      showNavigationToggle
      userMenu={userMenuMarkup}
      secondaryMenu={secondaryMenuMarkup}
      searchResultsVisible={isSearchActive}
      searchField={searchFieldMarkup}
      searchResults={searchResultsMarkup}
      onSearchResultsDismiss={handleSearchResultsDismiss}
      onNavigationToggle={handleNavigationToggle}
    />
  );

  return (
    <div style={{height: '250px'}}>
      <Frame topBar={topBarMarkup} logo={logo} />
    </div>
  );
}
```

## Required components

The top bar component must be passed to the [frame](https://polaris.shopify.com/components/deprecated/frame) component.

---

## Best practices

The top bar component should:

* Not provide global navigation for an application
  + Use the [navigation component](https://polaris.shopify.com/components/deprecated/navigation) instead
* Include search to help merchants find resources and navigate an application
* Include a user menu component to indicate the logged-in merchant and provide them with global actions
* Provide a color through the [app provider](https://polaris.shopify.com/components/app-provider) component to style the background
* The global menu text should contrast with the rest of the top bar and pass the minimum contrast ratio of the WCAG 2.0 guidelines
* Use an SVG file for the logo
* Use a logo that passes the minimum contrast ratio of the WCAG 2.0 guidelines when compared to the top bar background color
* Show the navigation toggle so it appears on small screen

---

## Content guidelines

### Placeholder content

The placeholder content for the search field should:

* Always say "Search"
* Never include an ellipsis

Do

* Search

Don't

* search...

---

## Top bar menu

A component that composes together an activator and a popover containing an action list to create a dropdown menu.

### Menu properties

| Prop | Type | Description |
| --- | --- | --- |
| activatorContent | React.ReactNode | Accepts an activator component that renders inside of a button that opens the menu |
| actions | ActionListProps['sections'] | An array of action objects that are rendered inside of a popover triggered by this menu |
| message | [MessageProps](#type-message) | Accepts a message that facilitates direct, urgent communication with the merchant through the menu |
| open | boolean | A boolean property indicating whether the menu is currently open |
| onOpen() | function | A callback function to handle opening the menu popover |
| onClose() | function | A callback function to handle closing the menu popover |

## Top bar user menu

A specialized menu component that is activated by a user avatar.

### Menu properties

| Prop | Type | Description |
| --- | --- | --- |
| actions | {items: IconableAction[]}[] | An array of action objects that are rendered inside of a popover triggered by this menu |
| message | [MessageProps](#type-message) | Accepts a message that facilitates direct, urgent communication with the merchant through the user menu |
| name | string | A string detailing the merchant’s full name to be displayed in the user menu |
| detail | string | A string allowing further details on the merchant’s name displayed in the user menu |
| initials | AvatarProps['initials'] | The merchant’s initials, rendered in place of an avatar image when not provided |
| avatar | AvatarProps['source'] | An avatar image representing the merchant |
| open | boolean | A boolean property indicating whether the user menu is currently open |
| onToggle() | function | A callback function to handle opening and closing the user menu |

### Top bar menu message

#### Message properties

| Prop | Type | Description |
| --- | --- | --- |
| title | string | A title for the message |
| description | string | A description for the message |
| action | {onClick(): void; content: string} | An action to render near the message |
| link | {to: string; content: string} | A link to view the content of the message |
| badge | {content: string; status: BadgeProps['status']} | A badge to render near the message |

---

## Top bar search field

A text field component that is tailor-made for a search use-case.

### Search field properties

| Prop | Type | Description |
| --- | --- | --- |
| value | string | Initial value for the input |
| placeholder | string | Hint text to display |
| focused | boolean | Force the focus state on the input |
| active | boolean | Force a state where search is active but the text field component is not focused |
| onChange(value: string) | function | Callback when value is changed |
| onFocus() | function | Callback when input is focused |
| onBlur() | function | Callback when focus is removed |

---

## Related components

* To provide the structure for the top bar component, as well as the primary navigation use the [frame](https://polaris.shopify.com/components/deprecated/frame) component.
* To display the primary navigation within the frame of an application, use the [navigation](https://polaris.shopify.com/components/deprecated/navigation) component.
* To tell merchants their options once they have made changes to a form on the page use the [contextual save bar](https://polaris.shopify.com/components/deprecated/contextual-save-bar) component.
* To provide quick, at-a-glance feedback on the outcome of an action, use the [toast](https://polaris.shopify.com/components/deprecated/toast) component.
* To indicate to merchants that a page is loading or an upload is processing use the [loading](https://polaris.shopify.com/components/deprecated/loading) component.