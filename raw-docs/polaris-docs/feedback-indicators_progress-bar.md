---
source: https://polaris.shopify.com/components/feedback-indicators/progress-bar
---

# Progress bar

The progress bar component is used to visually represent the completion of a task or operation. It shows how much of the task has been completed and how much is still left.

### Progress bar component examples

DefaultSmallColoredNon-animated

Use this component to visually represent the completion of a task or operation.

Edit in CodeSandbox

ReactHTML

```
import {ProgressBar} from '@shopify/polaris';
import React from 'react';

function ProgressBarExample() {
  return (
    <div style={{width: 225}}>
      <ProgressBar progress={75} />
    </div>
  );
}
```

## Props

interface ProgressBarProps

progress?number
:   The progression of certain tasks.

    Defaults to 0.

size?'small' | 'medium' | 'large'
:   Size of progressbar.

    Defaults to 'medium'.

animated?boolean
:   Whether the fill animation is triggered.

    Defaults to 'true'.

ariaLabelledBy?string
:   Id (ids) of element (elements) that describes progressbar.

tone?'highlight' | 'primary' | 'success' | 'critical'
:   Color of progressbar.

    Defaults to 'highlight'.

## Best practices

Progress bar components should:

* Give merchants an indication of how much of the task has completed and how much is left.
* Not be used for entire page loads. In this case, use the [Skeleton page](https://polaris.shopify.com/components/skeleton-page) component.

---

## Related components

* For tasks with a short load time, use the [Spinner](https://polaris.shopify.com/components/spinner) component
* For full page loads, use the [Skeleton page](https://polaris.shopify.com/components/skeleton-page) component