---
source: https://polaris.shopify.com/components/feedback-indicators/skeleton-body-text
---

# Skeleton body text

Skeleton body text is used to provide a low fidelity representation of content before it appears on the page, and improves load times perceived by merchants. Can be used for content in or outside of a card.

### Skeleton body text component examples

DefaultSingle line content

Use this component to represent a block of content being loaded. For example, you could use it to represent an entire product description card on the product page.

Edit in CodeSandbox

ReactHTML

```
import {SkeletonBodyText} from '@shopify/polaris';
import React from 'react';

function SkeletonExample() {
  return <SkeletonBodyText />;
}
```

## Props

interface SkeletonBodyTextProps

lines?number
:   Number of lines to display.

    Defaults to 3.

## Best practices

Skeleton body text component should:

* Be used with [Skeleton page](https://polaris.shopify.com/components/skeleton-page) when page content loads all at once. Together, these components give merchants an indication of what the page layout will be once loaded.
* Be used on its own, inside any content container component (like a [card](https://polaris.shopify.com/components/layout-and-structure/card)), and when content loads after the main page load.
* Try to match the number of lines to the content being loaded so it gives an accurate representation.

---

## Content guidelines

### Skeleton body text

Show static content that never changes on a page and use skeleton loading for dynamic content. Skeleton body text can sometimes be used to represent non-typographic content such as forms. Don’t use placeholder content that will change when the page fully loads.

![Image showing skeleton body text for dynamic content](/_next/image?url=%2Fimages%2Fcomponents%2Ffeedback-indicators%2Fskeleton-body-text%2Fdo-use-skeleton-body-for-dynamic-content%402x.png&w=1920&q=75)

Do

Use skeleton body text for dynamic content.

![Image showing skeleton body text for static content](/_next/image?url=%2Fimages%2Fcomponents%2Ffeedback-indicators%2Fskeleton-body-text%2Fdont-use-skeleton-body-for-static-or-placeholder-for-dynamic-text%402x.png&w=1920&q=75)

Don't

Use skeleton body text for static content or use placeholder content for dynamic content.

---

## Related components

* Use this component with [Skeleton page](https://polaris.shopify.com/components/skeleton-page) and [Skeleton display text](https://polaris.shopify.com/components/skeleton-display-text) to represent the content of a page while it’s loading.
* When giving feedback for in-context operations, use [Progress bar](https://polaris.shopify.com/components/progress-bar) or [Spinner](https://polaris.shopify.com/components/spinner) component.