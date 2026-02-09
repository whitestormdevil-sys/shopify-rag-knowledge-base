---
source: https://shopify.dev/docs/api/liquid/filters/customer_register_link
---

9

1

string | customer\_register\_link

returns [string](/docs/api/liquid/basics#string)

Generates an HTML link to the customer registration page.

9

1

{{ 'Create an account' | customer\_register\_link }}

##### Code

```liquid
{{ 'Create an account' | customer_register_link }}
```

## Output

9

1

<a href="/account/register" id="customer\_register\_link">Create an account</a>

##### Output

```liquid
<a href="/account/register" id="customer_register_link">Create an account</a>
```

Was this page helpful?

YesNo