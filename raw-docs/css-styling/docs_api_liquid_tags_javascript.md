---
source: https://shopify.dev/docs/api/liquid/tags/javascript
---

JavaScript code included in [section](/storefronts/themes/architecture/sections), [block](/storefronts/themes/architecture/blocks) and [snippet](/storefronts/themes/architecture/snippets) files.

Each section, block or snippet can have only one `{% javascript %}` tag.

To learn more about how JavaScript that's defined between the `javascript` tags is loaded and run, refer to the documentation for [javascript tags](/storefronts/themes/best-practices/javascript-and-stylesheet-tags#javascript).

---

Caution

Liquid isn't rendered inside of `{% javascript %}` tags. Including Liquid code can cause syntax errors.

**Caution:**

Liquid isn't rendered inside of `{% javascript %}` tags. Including Liquid code can cause syntax errors.

**Caution:** Liquid isn&#39;t rendered inside of <code>{% javascript %}</code> tags. Including Liquid code can cause syntax errors.

---

## Syntax

9

1

2

3

{% javascript %}

javascript\_code

{% endjavascript %}

javascript\_code

The JavaScript code for the section, block or snippet.

Was this page helpful?

YesNo