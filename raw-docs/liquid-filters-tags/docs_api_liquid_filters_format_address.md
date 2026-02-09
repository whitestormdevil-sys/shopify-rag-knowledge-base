---
source: https://shopify.dev/docs/api/liquid/filters/format_address
---

9

1

address | format\_address

returns [string](/docs/api/liquid/basics#string)

Generates an HTML address display, with each address component ordered according to the address's locale.

9

1

{{ shop.address | format\_address }}

##### Code

```liquid
{{ shop.address | format_address }}
```

##### Data

```liquid
{
  "shop": {
    "address": {}
  }
}
```

## Output

9

1

<p>Polina&#39;s Potions, LLC<br>150 Elgin Street<br>8th floor<br>Ottawa ON K2P 1L4<br>Canada</p>

##### Output

```liquid
<p>Polina&#39;s Potions, LLC<br>150 Elgin Street<br>8th floor<br>Ottawa ON K2P 1L4<br>Canada</p>
```

9

1

{{ customer.default\_address | format\_address }}

##### Code

```liquid
{{ customer.default_address | format_address }}
```

##### Data

```liquid
{
  "customer": {
    "default_address": {}
  }
}
```

## Output

9

1

<p>Cornelius Potionmaker<br>12 Phoenix Feather Alley<br>1<br>Calgary AB T1X 0L4<br>Canada</p>

##### Output

```liquid
<p>Cornelius Potionmaker<br>12 Phoenix Feather Alley<br>1<br>Calgary AB T1X 0L4<br>Canada</p>
```

Was this page helpful?

YesNo