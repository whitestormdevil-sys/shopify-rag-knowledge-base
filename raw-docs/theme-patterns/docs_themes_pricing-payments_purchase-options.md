---
source: https://shopify.dev/docs/themes/pricing-payments/purchase-options
---

Users are able to offer various options for purchasing goods and services at checkout through a subscription app. For example, customers can subscribe to a product delivery every month for a 10% discount, or every week for a 20% discount.

Tip

To be eligible to use Shopify subscriptions, merchants must meet the [qualifying criteria](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/setup#eligibility-requirements).

**Tip:**

To be eligible to use Shopify subscriptions, merchants must meet the [qualifying criteria](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/setup#eligibility-requirements).

---

## [Anchor to How it works](/docs/storefronts/themes/pricing-payments/subscriptions#how-it-works)How it works

To enable subscriptions, apps create [selling plan groups](/docs/api/liquid/objects/selling_plan_group), within which they create [selling plans](/docs/api/liquid/objects/selling_plan). These selling plans are linked to products and product variants. For example, a selling plan group called "Subscribe & Save" can offer selling plans that enable the customer to choose the delivery frequency and billing frequency separately. Merchants can offer multiple optional selling plans to customers, or specify a required selling plan for a product, such as "subscription-only" offers.

![](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/subscribe-and-save-eaLUKESq.png)


---

## [Anchor to Implementing subscriptions in a theme](/docs/storefronts/themes/pricing-payments/subscriptions#implementing-subscriptions-in-a-theme)Implementing subscriptions in a theme

You can use Liquid and JavaScript to integrate subscriptions into your theme. You should also review the UX guidelines for subscriptions to ensure a great user experience.

[![](/images/icons/48/tutorial.png)![](/images/icons/48/tutorial-dark.png)

Add subscriptions to your theme

Learn more about how to integrate subscriptions into your theme.

Add subscriptions to your theme

Learn more about how to integrate subscriptions into your theme.](/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme)

[Add subscriptions to your theme  
  

Learn more about how to integrate subscriptions into your theme.](/docs/storefronts/themes/pricing-payments/subscriptions/add-subscriptions-to-your-theme)

[![](/images/icons/48/themes.png)![](/images/icons/48/themes-dark.png)

Subscriptions UX guidelines

Learn how to build a subscription experience and style components in your theme.

Subscriptions UX guidelines

Learn how to build a subscription experience and style components in your theme.](/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines)

[Subscriptions UX guidelines  
  

Learn how to build a subscription experience and style components in your theme.](/docs/storefronts/themes/pricing-payments/subscriptions/subscription-ux-guidelines)

---

Was this page helpful?

YesNo