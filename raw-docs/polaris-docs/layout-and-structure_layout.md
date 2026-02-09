---
source: https://polaris.shopify.com/components/layout-and-structure/layout
---

# Layout

The layout component is used to create the main layout on a page. Layouts sections come in three main configurations. one-column, two-column, and annotated. One and two column layouts can be combined in the same page. Annotated layouts should be used on their own and only on settings pages.

### Upgrade to Polaris Web Components

Layout is now available as a framework-agnostic web component.

[Start using <s-page>](https://shopify.dev/docs/api/app-home/polaris-web-components/structure/page)

### Layout component examples

One-columnTwo columns with primary and secondary widthsTwo columns with equal widthThree columns with equal widthAnnotatedAnnotated with sectionsAnnotated with Banner at the top

Use to have a single section on its own in a full-width container. Use for simple pages and as a container for banners and other full-width content.

Edit in CodeSandbox

ReactHTML

```
import {Page, Layout, LegacyCard} from '@shopify/polaris';
import React from 'react';

function LayoutExample() {
  return (
    <Page fullWidth>
      <Layout>
        <Layout.Section>
          <LegacyCard title="Online store dashboard" sectioned>
            <p>View a summary of your online store’s performance.</p>
          </LegacyCard>
        </Layout.Section>
      </Layout>
    </Page>
  );
}
```

## Props

interface LayoutProps

sectioned?boolean
:   Automatically adds sections to layout.

children?React.ReactNode
:   The content to display inside the layout.

## Best practices

The layout component should:

* Use sections with white backgrounds for primary content and sections with grey backgrounds for secondary content that is less important
* Center cards on the background when there is no secondary card on the page to stop the content from becoming too wide
* Group similar concepts and actions together in cards
* Separate different cards using a full-width divider
* Structure primary/secondary, two-column layouts so the primary ⅔ section is used for main information and the secondary ⅓ section is used for information that might not be used as often but remains helpful for context or secondary tasks
* Use equal-width layouts with two or more columns when each layout section has the same importance

---

## Content guidelines

The content that appears in the layout component comes from cards and annotated sections.

### Cards

Content from cards should follow the content guidelines for [cards](https://polaris.shopify.com/components/layout-and-structure/legacy-card#content-guidelines).

### Annotated section titles

Annotated section titles should follow the content guidelines for [headings and subheadings](https://polaris.shopify.com/content/actionable-language#headings-and-subheadings).

### Annotated section descriptions

Annotated section descriptions should:

* Be used if the explanation or purpose of the associated cards isn’t clear
* Provide instructions for any choices merchants need to make, or explain the purpose of the section
* Be short, no more than 1–3 sentences
* Direct merchants to more content in the Help Center with “Learn more” links
* Not repeat the section title
* Use complete sentences and regular punctuation

---

## Related components

* To visually group content in a layout section, [use the card component](https://polaris.shopify.com/components/layout-and-structure/card)
* To lay out a set of smaller components in a row, [use the vertical stack component](https://polaris.shopify.com/components/layout-and-structure/vertical-stack)
* To lay out form fields, [use the form layout component](https://polaris.shopify.com/components/form-layout)