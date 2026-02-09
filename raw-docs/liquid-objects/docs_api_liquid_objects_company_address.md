---
source: https://shopify.dev/docs/api/liquid/objects/company_address
---

The address of a company location.

To learn about B2B in themes, refer to [Support B2B customers in your theme](/themes/pricing-payments/b2b).

## Properties

[Anchor to](/docs/api/liquid/objects/company_address#company_address-address1) 

address1**address1** [string](/docs/api/liquid/basics#string)

:   The first line of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-address2) 

address2**address2** [string](/docs/api/liquid/basics#string)

:   The second line of the address.

    If no second line is specified, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-attention) 

attention**attention** [string](/docs/api/liquid/basics#string)

:   The attention line of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-city) 

city**city** [string](/docs/api/liquid/basics#string)

:   The city of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-country) 

country**country** [country](/docs/api/liquid/objects/country)

:   The country of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-country_code) 

country\_code**country\_code** [string](/docs/api/liquid/basics#string)

:   The country of the address in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

[Anchor to](/docs/api/liquid/objects/company_address#company_address-first_name) 

first\_name**first\_name** [string](/docs/api/liquid/basics#string)

:   The first name of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-last_name) 

last\_name**last\_name** [string](/docs/api/liquid/basics#string)

:   The last name of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-province) 

province**province** [string](/docs/api/liquid/basics#string)

:   The province of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-province_code) 

province\_code**province\_code** [string](/docs/api/liquid/basics#string)

:   The province of the address in [ISO 3166-2 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

    Note

    The value doesn't include the preceding [ISO 3166-1](https://www.iso.org/glossary-for-iso-3166.html) country code.

    **Note:**

    The value doesn't include the preceding [ISO 3166-1](https://www.iso.org/glossary-for-iso-3166.html) country code.

    **Note:** The value doesn&#39;t include the preceding <a href="https://www.iso.org/glossary-for-iso-3166.html">ISO 3166-1</a> country code.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-street) 

street**street** [string](/docs/api/liquid/basics#string)

:   A combination of the first and second lines of the address.

[Anchor to](/docs/api/liquid/objects/company_address#company_address-zip) 

zip**zip** [string](/docs/api/liquid/basics#string)

:   The zip or postal code of the address.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

{

"address1": "99 Cauldron Lane",

"address2": "Unit 4B",

"attention": "Cornelius&#39; Custom Concoctions",

"city": "Edinburgh",

"country": {},

"country\_code": "GB",

"first\_name": "Cornelius",

"id": 65,

"last\_name": "Potionmaker",

"province": null,

"province\_code": null,

"street": "99 Cauldron Lane, Unit 4B",

"zip": "EH95 1AF"

}

##### Example

```liquid
{
  "address1": "99 Cauldron Lane",
  "address2": "Unit 4B",
  "attention": "Cornelius&#39; Custom Concoctions",
  "city": "Edinburgh",
  "country": {},
  "country_code": "GB",
  "first_name": "Cornelius",
  "id": 65,
  "last_name": "Potionmaker",
  "province": null,
  "province_code": null,
  "street": "99 Cauldron Lane, Unit 4B",
  "zip": "EH95 1AF"
}
```

Was this section helpful?

YesNo