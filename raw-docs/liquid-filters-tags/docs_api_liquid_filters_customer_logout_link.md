---
source: https://shopify.dev/docs/api/liquid/filters/customer_logout_link
---

9

1

string | customer\_logout\_link

returns [string](/docs/api/liquid/basics#string)

Generates an HTML link to log the customer out of their account and redirect to the homepage.

9

1

{{ 'Log out' | customer\_logout\_link }}

##### Code

```liquid
{{ 'Log out' | customer_logout_link }}
```

## Output

9

1

<a href="/account/logout" id="customer\_logout\_link">Log out</a>

##### Output

```liquid
<a href="/account/logout" id="customer_logout_link">Log out</a>
```

Was this page helpful?

YesNo