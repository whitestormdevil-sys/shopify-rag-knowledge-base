---
source: https://polaris.shopify.com/components/feedback-indicators/badge
---

# Badge

Badges are used to inform merchants of the tone of an object or of an action that’s been taken.

### Upgrade to Polaris Web Components

Badge is now available as a framework-agnostic web component.

[Start using <s-badge>](https://shopify.dev/docs/api/app-home/polaris-web-components/titles-and-text/badge)

### Badge component examples

DefaultSmallInformationalSuccessAttentionWarningCriticalIncompletePartially completeCompleteWith toneAndProgressLabelOverride

Use to give a non-critical tone update on a piece of information or action.

Edit in CodeSandbox

ReactHTML

```
import {Badge, Card} from '@shopify/polaris';
import React from 'react';

function BadgeExample() {
  return (
    <Card>
      <Badge>Fulfilled</Badge>
    </Card>
  );
}
```

## Props

This component defines its props in a way that our website can't automatically parse. The type definition is shown below, but it might be hard to read.

type BadgeProps

NonMutuallyExclusiveProps & (
| {progress?: ('incomplete' | 'partiallyComplete' | 'complete'); icon?: undefined}
| {icon?: (React.FunctionComponent<React.SVGProps<SVGSVGElement>> | 'placeholder' | string); progress?: undefined}
)

## Best practices

Badges benefit merchants by:

* Using established color patterns so that merchants can quickly identify their tone or importance level
* Being clearly labeled with short, scannable text
* Being positioned to clearly identify the object they’re informing or labelling

---

## Content guidelines

### Badge label

Badge labels should:

* Use a single word to describe the tone of an object.
* Only use two words if you need to describe a complex state. For example, “Partially refunded” and “Partially fulfilled”.
* Always describe the tone in the past tense. For example, refunded not refund.

The available badges for financial tone are:

* Authorized
* Pending
* Paid
* Unpaid
* Pending
* Voided
* Partially paid
* Partially refunded
* Refunded

The available badges for fulfillment tone are:

* Fulfilled
* Complete
* Partial
* Unfulfilled
* Restocked

Don't

Don’t use alternatives to existing badge options. Only create a new badge option if there aren’t any existing options to communicate the tone you need.

---

## Related components

* To represent an interactive list of categories provided by merchants, [use tags](https://polaris.shopify.com/components/tag)

---

## Accessibility

Badges that convey information with icons or color include text provided by the [visually hidden component](https://polaris.shopify.com/components/visually-hidden#navigation). This text is read out by assistive technologies like screen readers so that merchants with vision issues can access the meaning of the badge in context.