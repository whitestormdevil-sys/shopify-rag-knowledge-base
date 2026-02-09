---
source: https://shopify.dev/docs/api/liquid/filters/customer_login_link
---

9

1

string | customer\_login\_link

returns [string](/docs/api/liquid/basics#string)

Generates an HTML link to the customer login page.

9

1

{{ 'Log in' | customer\_login\_link }}

##### Code

```liquid
{{ 'Log in' | customer_login_link }}
```

## Output

9

1

<a href="/account/login" id="customer\_login\_link">Log in</a>

##### Output

```liquid
<a href="/account/login" id="customer_login_link">Log in</a>
```

Was this page helpful?

YesNo