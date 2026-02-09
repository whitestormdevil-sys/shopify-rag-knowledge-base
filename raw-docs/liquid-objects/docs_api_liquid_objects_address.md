---
source: https://shopify.dev/docs/api/liquid/objects/address
---

An address, such as a customer address or order shipping address.

---

Tip

Use the [`format_address` filter](/docs/api/liquid/filters/format_address) to output an address according to its locale.

**Tip:**

Use the [`format_address` filter](/docs/api/liquid/filters/format_address) to output an address according to its locale.

**Tip:** Use the <a href="/docs/api/liquid/filters/format\_address"><code><span class="PreventFireFoxApplyingGapToWBR">format<wbr/>\_address</span></code> filter</a> to output an address according to its locale.

---

## Properties

[Anchor to](/docs/api/liquid/objects/address#address-address1) 

address1**address1** [string](/docs/api/liquid/basics#string)

:   The first line of the address.

[Anchor to](/docs/api/liquid/objects/address#address-address2) 

address2**address2** [string](/docs/api/liquid/basics#string)

:   The second line of the address.

    If no second line is specified, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/address#address-city) 

city**city** [string](/docs/api/liquid/basics#string)

:   The city of the address.

[Anchor to](/docs/api/liquid/objects/address#address-company) 

company**company** [string](/docs/api/liquid/basics#string)

:   The company of the address.

    If no company is specified, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/address#address-country) 

country**country** [country](/docs/api/liquid/objects/country)

:   The country of the address.

[Anchor to](/docs/api/liquid/objects/address#address-country_code) 

country\_code**country\_code** [string](/docs/api/liquid/basics#string)

:   The country of the address in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

[Anchor to](/docs/api/liquid/objects/address#address-first_name) 

first\_name**first\_name** [string](/docs/api/liquid/basics#string)

:   The first name of the address.

[Anchor to](/docs/api/liquid/objects/address#address-id) 

id**id** [number](/docs/api/liquid/basics#number)

:   The ID of the address.

[Anchor to](/docs/api/liquid/objects/address#address-last_name) 

last\_name**last\_name** [string](/docs/api/liquid/basics#string)

:   The last name of the address.

[Anchor to](/docs/api/liquid/objects/address#address-name) 

name**name** [string](/docs/api/liquid/basics#string)

:   A combination of the first and last names of the address.

[Anchor to](/docs/api/liquid/objects/address#address-phone) 

phone**phone** [string](/docs/api/liquid/basics#string)

:   The phone number of the address.

    If no phone number is specified, then `nil` is returned.

[Anchor to](/docs/api/liquid/objects/address#address-province) 

province**province** [string](/docs/api/liquid/basics#string)

:   The province of the address.

[Anchor to](/docs/api/liquid/objects/address#address-province_code) 

province\_code**province\_code** [string](/docs/api/liquid/basics#string)

:   The province of the address in [ISO 3166-2 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

    Note

    The value doesn't include the preceding [ISO 3166-1](https://www.iso.org/glossary-for-iso-3166.html) country code.

    **Note:**

    The value doesn't include the preceding [ISO 3166-1](https://www.iso.org/glossary-for-iso-3166.html) country code.

    **Note:** The value doesn&#39;t include the preceding <a href="https://www.iso.org/glossary-for-iso-3166.html">ISO 3166-1</a> country code.

[Anchor to](/docs/api/liquid/objects/address#address-street) 

street**street** [string](/docs/api/liquid/basics#string)

:   A combination of the first and second lines of the address.

[Anchor to](/docs/api/liquid/objects/address#address-summary) 

summary**summary** [string](/docs/api/liquid/basics#string)

:   A summary of the address, including the following properties:

    * First and last name
    * First and second lines
    * City
    * Province
    * Country

[Anchor to](/docs/api/liquid/objects/address#address-url) 

url**url** [string](/docs/api/liquid/basics#string)

:   The relative URL for the address.

    Note

    This only applies to customer addresses.

    **Note:**

    This only applies to customer addresses.

    **Note:** This only applies to customer addresses.

[Anchor to](/docs/api/liquid/objects/address#address-zip) 

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

16

17

18

19

{

"address1": "150 Elgin Street",

"address2": "8th floor",

"city": "Ottawa",

"company": "Polina&#39;s Potions, LLC",

"country": {},

"country\_code": "CA",

"first\_name": null,

"id": 56174706753,

"last\_name": null,

"name": "",

"phone": "416-123-1234",

"province": "Ontario",

"province\_code": "ON",

"street": "150 Elgin Street, 8th floor",

"summary": "150 Elgin Street, 8th floor, Ottawa, Ontario, Canada",

"url": "/account/addresses/56174706753",

"zip": "K2P 1L4"

}

##### Example

```liquid
{
  "address1": "150 Elgin Street",
  "address2": "8th floor",
  "city": "Ottawa",
  "company": "Polina&#39;s Potions, LLC",
  "country": {},
  "country_code": "CA",
  "first_name": null,
  "id": 56174706753,
  "last_name": null,
  "name": "",
  "phone": "416-123-1234",
  "province": "Ontario",
  "province_code": "ON",
  "street": "150 Elgin Street, 8th floor",
  "summary": "150 Elgin Street, 8th floor, Ottawa, Ontario, Canada",
  "url": "/account/addresses/56174706753",
  "zip": "K2P 1L4"
}
```

Was this section helpful?

YesNo