---
source: https://shopify.dev/docs/api/liquid/tags/include
---

Renders a [snippet](/themes/architecture/snippets).

Inside the snippet, you can access and alter variables that are [created](/docs/api/liquid/tags/variable-tags) outside of the
snippet.

Deprecated

Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain.

The `include` tag has been replaced by [`render`](/docs/api/liquid/tags/render).

**Deprecated:**

Deprecated because the way that variables are handled reduces performance and makes code harder to both read and maintain.

The `include` tag has been replaced by [`render`](/docs/api/liquid/tags/render).

## Syntax

9

1

{% include 'filename' %}

filename

The name of the snippet to render, without the `.liquid` extension.

Was this page helpful?

YesNo