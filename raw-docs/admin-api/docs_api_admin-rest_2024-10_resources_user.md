---
source: https://shopify.dev/docs/api/admin-rest/2024-10/resources/user
---

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the [GraphQL Admin API](/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](/docs/apps/build/graphql/migrate).

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04 

2026-01latest

# User

Ask assistant

Requires `users` access scope.

**Requires `users` access scope.:**

#### Shopify Plus

The User resource is available for [private apps](/concepts/apps#private-apps) and [custom apps](/concepts/apps#custom-apps) installed on **[Shopify Plus](https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/shopify-plus)** stores.
You need to contact Shopify Plus Support to request the `read_users` [access scope](/api/usage/access-scopes) for your app.

The User resource lets you retrieve information about staff on a Shopify shop, including
[staff permissions](https://help.shopify.com/manual/your-account/staff-accounts/staff-permissions).

Permissions determine the level of access that staff have to a merchant's store. From the Shopify admin, merchants can give each staff
individual permissions that control access to a part of Shopify. The API only lets you retrieve information about staff.

Was this section helpful?

YesNo

#

## Endpoints

* [get

  /admin/api/latest/users.json](/docs/api/admin-rest/latest/resources/user#get-users)

  Retrieves a list of all users

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-all-users)
* [get

  /admin/api/latest/users/{user\_id}.json](/docs/api/admin-rest/latest/resources/user#get-users-user-id)

  Retrieves a single user

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  staffMember](/docs/api/admin-graphql/latest/queries/staffMember?example=retrieves-a-single-user)
* [get

  /admin/api/latest/users/current.json](/docs/api/admin-rest/latest/resources/user#get-users-current)

  Retrieves the currently logged-in user

  [![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

  staffMember](/docs/api/admin-graphql/latest/queries/staffMember?example=retrieves-the-currently-logged-in-user)

---

[Anchor to](/docs/api/admin-rest/latest/resources/user#resource-object) 

## The User resource

[Anchor to](/docs/api/admin-rest/latest/resources/user#resource-object-properties) 

### Properties

---

account\_owner

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

isShopOwner](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.isShopOwner)

Whether the user is the owner of the Shopify account.

---

bio

deprecated**deprecated**

The description the user has written for themselves.

---

email

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

email](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.email)

The user's email address.

---

first\_name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

firstName](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.firstName)

The user's first name.

---

id

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

id](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.id)

The ID of the user's staff.

---

im

deprecated**deprecated**

This property is deprecated.

---

last\_name

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

lastName](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.lastName)

The user's last name.

---

permissions

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

permissions](/docs/api/admin-graphql/latest/objects/StaffMemberPrivateData#field-StaffMemberPrivateData.fields.permissions)

The permissions granted to the user's staff account. Valid values:

Show permissions properties

* **applications**: The user can authorize the installation of applications.
* **billing\_application\_charges**: The user can approve application charges.
* **billing\_charges**: The user can view and export billing charges.
* **billing\_invoices\_view**: The user can view billing invoices.
* **billing\_payment\_methods\_view**: The user can view billing payment methods.
* **customers**: The user can view, create, edit, and delete customers, and respond to customer messages in Shopify Ping.
* **dashboard**: The user can view the **Home** page, which includes sales information and other store data.
* **domains**: The user can view, buy, and manage domains.
* **draft\_orders**: The user can create, update, and delete draft orders.
* **edit\_orders**: The user can edit orders.
* **edit\_private\_apps**: The user can give permission to private apps to read, write, and make changes to the store.
* **export\_customers**: The user can export customers.
* **export\_draft\_orders**: The user can export draft orders.
* **export\_products**: The user can export products and inventory.
* **export\_orders**: The user can export orders.
* **gift\_cards**: The user can view, create, issue, and export gift cards to a CSV file.
* **links**: The user can view and modify links and navigation menus.
* **locations**: The user can create, update, and delete locations where you stock or manage inventory.
* **marketing**: The user can view and create discount codes and automatic discounts, and export discounts to a CSV file.
* **marketing\_section**: The user can view, create, and automate marketing campaigns.
* **orders**: The user can view, create, update, delete, and cancel orders, and receive order notifications.
* **overviews**: The user can view the **Overview** and **Live view** pages,
  which include sales information, and other store and sales channels data.
* **pages**: The user can view, create, update, publish, and delete blog posts and pages.
* **preferences**: The user can view the preferences and configuration of a shop.
* **products**: The user can view, create, import, and update products, collections, and inventory.
* **reports**: The user can view and create all reports, which includes sales information and other store data.
* **shopify\_payments\_accounts**: The user can view Shopify Payments account details.
* **shopify\_payments\_transfers**: The user can view Shopify Payments payouts.
* **staff\_audit\_log\_view**: The user can view Shopify admin browser sessions.
* **staff\_management\_activation**: The user can activate or deactivate staff in the store.
* **staff\_management\_create**: The user can add staff to the store.
* **staff\_management\_delete**: The user can delete staff from the store.
* **staff\_management\_update**: The user can update staff in the store.
* **themes**: The user can view, update, and publish themes.
* **view\_private\_apps**: The user can view private apps installed on the store.

---

phone

->[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

phone](/docs/api/admin-graphql/latest/objects/StaffMember#field-StaffMember.fields.phone)

The user's phone number.

---

receive\_announcements

deprecated**deprecated**

Whether this account will receive email announcements from Shopify. Valid values: `0`, `1`

---

screen\_name

deprecated**deprecated**

This property is deprecated.

---

url

deprecated**deprecated**

The user's homepage or other web address.

---

Show 2 hidden fields

Was this section helpful?

YesNo

{}

## The User resource

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

20

{

"account\_owner": false,

"bio": "A person on a mission",

"email": "joe@example.com",

"first\_name": "Joe",

"id": 1234567890,

"im": "joe-chat@example.com",

"last\_name": "Smith",

"permissions": [

"customers",

"dashboard",

"reports"

],

"phone": "(555) 555-5555",

"receive\_announcements": 0,

"screen\_name": "joesmith",

"url": "http://example.com",

"locale": "en",

"user\_type": "regular"

}

---

## [Anchor to GET request, Retrieves a list of all users](/docs/api/admin-rest/latest/resources/user#get-users) get Retrieves a list of all users

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-all-users)

Retrieves a list of all users. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

### [Anchor to Parameters of Retrieves a list of all users](/docs/api/admin-rest/latest/resources/user#get-users-parameters)Parameters

---

api\_version

string**string**

required**required**

---

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show on a page.

---

page\_info

A unique ID used to access a certain page of results.

---

Was this section helpful?

YesNo

### [Anchor to get-users-examples](/docs/api/admin-rest/latest/resources/user#get-users-examples)Examples

Retrieve a list of all users

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

999

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

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

HTTP/1.1 200 OK

{

"users": [

{

"id": 548380009,

"first\_name": "John",

"email": "j.smith@example.com",

"url": "www.example.com",

"im": null,

"screen\_name": null,

"phone": null,

"last\_name": "Smith",

"account\_owner": true,

"receive\_announcements": 1,

"bio": null,

"permissions": [

"applications",

"beacons",

"billing\_application\_charges",

"bulk\_data\_export",

"bulk\_data\_import",

"channels",

"content",

"content\_entries\_delete",

"content\_entries\_edit",

"content\_entries\_view",

"content\_models\_delete",

"content\_models\_edit",

"content\_models\_view",

"create\_store\_credit\_account\_transactions",

"create\_and\_edit\_files",

"create\_and\_update\_marketing\_integrated\_campaigns",

"create\_files",

"custom\_pixels\_management",

"custom\_pixels\_view",

"customers",

### examples

* #### Retrieve a list of all users

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.User.all({
    session: session,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::User.all(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.User.all({
    session: session,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"users":[{"id":548380009,"first_name":"John","email":"j.smith@example.com","url":"www.example.com","im":null,"screen_name":null,"phone":null,"last_name":"Smith","account_owner":true,"receive_announcements":1,"bio":null,"permissions":["applications","beacons","billing_application_charges","bulk_data_export","bulk_data_import","channels","content","content_entries_delete","content_entries_edit","content_entries_view","content_models_delete","content_models_edit","content_models_view","create_store_credit_account_transactions","create_and_edit_files","create_and_update_marketing_integrated_campaigns","create_files","custom_pixels_management","custom_pixels_view","customers","create_and_edit_customers","delete_customers","export_customers","merge_customers","dashboard","delete_products","delete_files","delete_marketing_integrated_campaigns","domains","draft_orders","create_and_edit_draft_orders","apply_discounts_to_draft_orders","mark_draft_orders_as_paid","set_payment_terms_for_draft_orders","delete_draft_orders","pay_draft_orders_by_vaulted_card","edit_files","edit_orders","edit_private_apps","edit_product_cost","edit_product_price","edit_theme_code","gift_cards","create_and_edit_gift_cards","deactivate_gift_cards","export_gift_cards","links","locations","manage_delivery_settings","manage_inventory","view_inventory_transfers","create_and_edit_inventory_transfers","manage_inventory_shipments","manage_policies","manage_product_tags","manage_products","manage_store_credit_settings","manage_taxes_settings","marketing","marketing_section","metaobjects_delete","metaobjects_edit","metaobjects_view","metaobject_definitions_delete","metaobject_definitions_edit","metaobject_definitions_view","orders","over_refund_to_original_payment","overviews","pages","pay_draft_orders_by_credit_card","pay_orders_by_credit_card","pay_orders_by_vaulted_card","preferences","products","refund_orders","refund_to_store_credit","reports","translations","themes","view_all_shopify_credit_transactions","view_balance_bank_accounts","view_files","view_marketing_integrated_campaigns","view_private_apps","view_product_costs","view_store_credit_account_transactions","apply_discounts_to_orders","fulfill_and_ship_orders","buy_shipping_labels","return_orders","manage_abandoned_checkouts","cancel_orders","delete_orders","manage_orders_information","set_payment_terms_for_orders","mark_orders_as_paid","capture_payments_for_orders","view_companies","create_and_edit_companies","delete_companies","manage_company_location_assignments","third_party_money_movement","export_draft_orders","export_orders","export_products","manage_checkout_customer_accounts_editor","manage_checkout_settings","view_price_lists","delete_price_lists","create_and_edit_price_lists","view_catalogs","create_and_edit_catalogs","delete_catalogs","view_markets","create_and_edit_markets","delete_markets","manage_customer_identity_providers","select_existing_legal_entity","sidekick","view_rollouts","create_and_edit_rollouts","delete_rollouts","view_company_store_credit_account_transactions","create_company_store_credit_account_transactions","manage_terms_of_service","quick_sale","shopify_payments_accounts","shopify_payments_transfers","staff_audit_log_view","staff_management_update","applications_billing","attestation_authority","authentication_management","balance_bank_accounts_management","billing_charges","billing_invoices_pay","billing_invoices_view","billing_payment_methods_manage","billing_payment_methods_view","billing_settings","billing_subscriptions","capital","customer_private_data","erase_customer_data","request_customer_data","domains_management","domains_transfer_out","enable_private_apps","experiments_management","manage_all_shopify_credit_cards","manage_tap_to_pay","payment_settings","upgrade_to_plus_plan","shopify_payments","sqlite_bulk_data_transfer","staff_api_permission_management","staff_management","staff_management_activation","staff_management_create","staff_management_delete","support_methods","third_party_gateways","collaborator_request_management","collaborator_request_settings","enable_retail_terms_of_service"],"locale":"en","user_type":"regular","admin_graphql_api_id":"gid://shopify/AdminUserSerializer/548380009","tfa_enabled?":false},{"id":930143300,"first_name":"John","email":"j.limited@example.com","url":"www.example.com","im":null,"screen_name":null,"phone":null,"last_name":"Limited","account_owner":false,"receive_announcements":1,"bio":null,"permissions":[],"locale":"en","user_type":"regular","admin_graphql_api_id":"gid://shopify/AdminUserSerializer/930143300","tfa_enabled?":false}]}
  ```

---

## [Anchor to GET request, Retrieves a single user](/docs/api/admin-rest/latest/resources/user#get-users-user-id) get Retrieves a single user

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

staffMember](/docs/api/admin-graphql/latest/queries/staffMember?example=retrieves-a-single-user)

Retrieves a single user

### [Anchor to Parameters of Retrieves a single user](/docs/api/admin-rest/latest/resources/user#get-users-user-id-parameters)Parameters

---

api\_version

string**string**

required**required**

---

user\_id

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-users-user-id-examples](/docs/api/admin-rest/latest/resources/user#get-users-user-id-examples)Examples

Retrieve a single user

Path parameters

user\_id=548380009

string**string**

required**required**

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users/548380009.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

999

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

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

HTTP/1.1 200 OK

{

"user": {

"id": 548380009,

"first\_name": "John",

"email": "j.smith@example.com",

"url": "www.example.com",

"im": null,

"screen\_name": null,

"phone": null,

"last\_name": "Smith",

"account\_owner": true,

"receive\_announcements": 1,

"bio": null,

"permissions": [

"applications",

"beacons",

"billing\_application\_charges",

"bulk\_data\_export",

"bulk\_data\_import",

"channels",

"content",

"content\_entries\_delete",

"content\_entries\_edit",

"content\_entries\_view",

"content\_models\_delete",

"content\_models\_edit",

"content\_models\_view",

"create\_store\_credit\_account\_transactions",

"create\_and\_edit\_files",

"create\_and\_update\_marketing\_integrated\_campaigns",

"create\_files",

"custom\_pixels\_management",

"custom\_pixels\_view",

"customers",

"create\_and\_edit\_customers",

### examples

* #### Retrieve a single user

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users/548380009.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.User.find({
    session: session,
    id: 548380009,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::User.find(
    session: test_session,
    id: 548380009,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.User.find({
    session: session,
    id: 548380009,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"user":{"id":548380009,"first_name":"John","email":"j.smith@example.com","url":"www.example.com","im":null,"screen_name":null,"phone":null,"last_name":"Smith","account_owner":true,"receive_announcements":1,"bio":null,"permissions":["applications","beacons","billing_application_charges","bulk_data_export","bulk_data_import","channels","content","content_entries_delete","content_entries_edit","content_entries_view","content_models_delete","content_models_edit","content_models_view","create_store_credit_account_transactions","create_and_edit_files","create_and_update_marketing_integrated_campaigns","create_files","custom_pixels_management","custom_pixels_view","customers","create_and_edit_customers","delete_customers","export_customers","merge_customers","dashboard","delete_products","delete_files","delete_marketing_integrated_campaigns","domains","draft_orders","create_and_edit_draft_orders","apply_discounts_to_draft_orders","mark_draft_orders_as_paid","set_payment_terms_for_draft_orders","delete_draft_orders","pay_draft_orders_by_vaulted_card","edit_files","edit_orders","edit_private_apps","edit_product_cost","edit_product_price","edit_theme_code","gift_cards","create_and_edit_gift_cards","deactivate_gift_cards","export_gift_cards","links","locations","manage_delivery_settings","manage_inventory","view_inventory_transfers","create_and_edit_inventory_transfers","manage_inventory_shipments","manage_policies","manage_product_tags","manage_products","manage_store_credit_settings","manage_taxes_settings","marketing","marketing_section","metaobjects_delete","metaobjects_edit","metaobjects_view","metaobject_definitions_delete","metaobject_definitions_edit","metaobject_definitions_view","orders","over_refund_to_original_payment","overviews","pages","pay_draft_orders_by_credit_card","pay_orders_by_credit_card","pay_orders_by_vaulted_card","preferences","products","refund_orders","refund_to_store_credit","reports","translations","themes","view_all_shopify_credit_transactions","view_balance_bank_accounts","view_files","view_marketing_integrated_campaigns","view_private_apps","view_product_costs","view_store_credit_account_transactions","apply_discounts_to_orders","fulfill_and_ship_orders","buy_shipping_labels","return_orders","manage_abandoned_checkouts","cancel_orders","delete_orders","manage_orders_information","set_payment_terms_for_orders","mark_orders_as_paid","capture_payments_for_orders","view_companies","create_and_edit_companies","delete_companies","manage_company_location_assignments","third_party_money_movement","export_draft_orders","export_orders","export_products","manage_checkout_customer_accounts_editor","manage_checkout_settings","view_price_lists","delete_price_lists","create_and_edit_price_lists","view_catalogs","create_and_edit_catalogs","delete_catalogs","view_markets","create_and_edit_markets","delete_markets","manage_customer_identity_providers","select_existing_legal_entity","sidekick","view_rollouts","create_and_edit_rollouts","delete_rollouts","view_company_store_credit_account_transactions","create_company_store_credit_account_transactions","manage_terms_of_service","quick_sale","shopify_payments_accounts","shopify_payments_transfers","staff_audit_log_view","staff_management_update","applications_billing","attestation_authority","authentication_management","balance_bank_accounts_management","billing_charges","billing_invoices_pay","billing_invoices_view","billing_payment_methods_manage","billing_payment_methods_view","billing_settings","billing_subscriptions","capital","customer_private_data","erase_customer_data","request_customer_data","domains_management","domains_transfer_out","enable_private_apps","experiments_management","manage_all_shopify_credit_cards","manage_tap_to_pay","payment_settings","upgrade_to_plus_plan","shopify_payments","sqlite_bulk_data_transfer","staff_api_permission_management","staff_management","staff_management_activation","staff_management_create","staff_management_delete","support_methods","third_party_gateways","collaborator_request_management","collaborator_request_settings","enable_retail_terms_of_service"],"locale":"en","user_type":"regular","admin_graphql_api_id":"gid://shopify/AdminUserSerializer/548380009","tfa_enabled?":false}}
  ```

---

## [Anchor to GET request, Retrieves the currently logged-in user](/docs/api/admin-rest/latest/resources/user#get-users-current) get Retrieves the currently logged-in user

[![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-CQ7q9aDJ.svg)![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/logos/GraphQL-dark-CtivyDg_.svg)

staffMember](/docs/api/admin-graphql/latest/queries/staffMember?example=retrieves-the-currently-logged-in-user)

Retrieves information about the user account associated with the access token used to make this API request. This request works only when the access token was created for a specific user of the shop.

### [Anchor to Parameters of Retrieves the currently logged-in user](/docs/api/admin-rest/latest/resources/user#get-users-current-parameters)Parameters

---

api\_version

string**string**

required**required**

---

Was this section helpful?

YesNo

### [Anchor to get-users-current-examples](/docs/api/admin-rest/latest/resources/user#get-users-current-examples)Examples

Retrieve the the currently logged-in user

Was this section helpful?

YesNo

9

1

2

3

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users/current.json" \

-H "X-Shopify-Access-Token: {access\_token}"

{}

## Response

JSON

999

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

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

HTTP/1.1 200 OK

{

"user": {

"id": 548380009,

"first\_name": "John",

"email": "j.smith@example.com",

"url": "www.example.com",

"im": null,

"screen\_name": null,

"phone": null,

"last\_name": "Smith",

"account\_owner": true,

"receive\_announcements": 1,

"bio": null,

"permissions": [

"applications",

"beacons",

"billing\_application\_charges",

"bulk\_data\_export",

"bulk\_data\_import",

"channels",

"content",

"content\_entries\_delete",

"content\_entries\_edit",

"content\_entries\_view",

"content\_models\_delete",

"content\_models\_edit",

"content\_models\_view",

"create\_store\_credit\_account\_transactions",

"create\_and\_edit\_files",

"create\_and\_update\_marketing\_integrated\_campaigns",

"create\_files",

"custom\_pixels\_management",

"custom\_pixels\_view",

"customers",

"create\_and\_edit\_customers",

### examples

* #### Retrieve the the currently logged-in user

  ##### 

  ```liquid
  curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/users/current.json" \
  -H "X-Shopify-Access-Token: {access_token}"
  ```

  ##### 

  ```liquid
  await admin.rest.resources.User.current({
    session: session,
  });
  ```

  ##### 

  ```liquid
  # Session is activated via Authentication
  test_session = ShopifyAPI::Context.active_session

  ShopifyAPI::User.current(
    session: test_session,
  )
  ```

  ##### 

  ```liquid
  // Session is built by the OAuth process

  await shopify.rest.User.current({
    session: session,
  });
  ```

  #### response

  ```liquid
  HTTP/1.1 200 OK{"user":{"id":548380009,"first_name":"John","email":"j.smith@example.com","url":"www.example.com","im":null,"screen_name":null,"phone":null,"last_name":"Smith","account_owner":true,"receive_announcements":1,"bio":null,"permissions":["applications","beacons","billing_application_charges","bulk_data_export","bulk_data_import","channels","content","content_entries_delete","content_entries_edit","content_entries_view","content_models_delete","content_models_edit","content_models_view","create_store_credit_account_transactions","create_and_edit_files","create_and_update_marketing_integrated_campaigns","create_files","custom_pixels_management","custom_pixels_view","customers","create_and_edit_customers","delete_customers","export_customers","merge_customers","dashboard","delete_products","delete_files","delete_marketing_integrated_campaigns","domains","draft_orders","create_and_edit_draft_orders","apply_discounts_to_draft_orders","mark_draft_orders_as_paid","set_payment_terms_for_draft_orders","delete_draft_orders","pay_draft_orders_by_vaulted_card","edit_files","edit_orders","edit_private_apps","edit_product_cost","edit_product_price","edit_theme_code","gift_cards","create_and_edit_gift_cards","deactivate_gift_cards","export_gift_cards","links","locations","manage_delivery_settings","manage_inventory","view_inventory_transfers","create_and_edit_inventory_transfers","manage_inventory_shipments","manage_policies","manage_product_tags","manage_products","manage_store_credit_settings","manage_taxes_settings","marketing","marketing_section","metaobjects_delete","metaobjects_edit","metaobjects_view","metaobject_definitions_delete","metaobject_definitions_edit","metaobject_definitions_view","orders","over_refund_to_original_payment","overviews","pages","pay_draft_orders_by_credit_card","pay_orders_by_credit_card","pay_orders_by_vaulted_card","preferences","products","refund_orders","refund_to_store_credit","reports","translations","themes","view_all_shopify_credit_transactions","view_balance_bank_accounts","view_files","view_marketing_integrated_campaigns","view_private_apps","view_product_costs","view_store_credit_account_transactions","apply_discounts_to_orders","fulfill_and_ship_orders","buy_shipping_labels","return_orders","manage_abandoned_checkouts","cancel_orders","delete_orders","manage_orders_information","set_payment_terms_for_orders","mark_orders_as_paid","capture_payments_for_orders","view_companies","create_and_edit_companies","delete_companies","manage_company_location_assignments","third_party_money_movement","export_draft_orders","export_orders","export_products","manage_checkout_customer_accounts_editor","manage_checkout_settings","view_price_lists","delete_price_lists","create_and_edit_price_lists","view_catalogs","create_and_edit_catalogs","delete_catalogs","view_markets","create_and_edit_markets","delete_markets","manage_customer_identity_providers","select_existing_legal_entity","sidekick","view_rollouts","create_and_edit_rollouts","delete_rollouts","view_company_store_credit_account_transactions","create_company_store_credit_account_transactions","manage_terms_of_service","quick_sale","shopify_payments_accounts","shopify_payments_transfers","staff_audit_log_view","staff_management_update","applications_billing","attestation_authority","authentication_management","balance_bank_accounts_management","billing_charges","billing_invoices_pay","billing_invoices_view","billing_payment_methods_manage","billing_payment_methods_view","billing_settings","billing_subscriptions","capital","customer_private_data","erase_customer_data","request_customer_data","domains_management","domains_transfer_out","enable_private_apps","experiments_management","manage_all_shopify_credit_cards","manage_tap_to_pay","payment_settings","upgrade_to_plus_plan","shopify_payments","sqlite_bulk_data_transfer","staff_api_permission_management","staff_management","staff_management_activation","staff_management_create","staff_management_delete","support_methods","third_party_gateways","collaborator_request_management","collaborator_request_settings","enable_retail_terms_of_service"],"locale":"en","user_type":"regular","admin_graphql_api_id":"gid://shopify/AdminUserSerializer/548380009","tfa_enabled?":false}}
  ```