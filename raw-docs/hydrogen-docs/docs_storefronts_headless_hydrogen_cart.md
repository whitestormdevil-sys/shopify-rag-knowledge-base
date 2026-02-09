---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/cart
---

Managing the shopping cart is one of the fundamentals of digital commerce. Carts can be difficult to implement properly, requiring both complex state management and subtle UI interactions.

Hydrogen includes a suite of cart components built to work with Shopify APIs. These components aim to make it easier to build carts that behave predictably and consistently, while still being performant and customizable.

In this set of guides, you'll learn how to assemble these components to build a server-side cart that's fast, responsive, and reliable.

---

## [Anchor to Server-side first](/docs/storefronts/headless/hydrogen/cart#server-side-first)Server-side first

Hydrogen's cart is server-rendered by default, built on top of traditional [`<form>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) and [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP). This method has several benefits:

* It improves performance by reducing the total amount of JavaScript sent to the browser.
* Form actions are available as soon as the page loads, reducing time-to-interactive.
* It's more resilient and still works when JavaScript fails or is unavailable.
* Managing state on the server allows cart instances to be shared across app contexts.
* Carts can be progressively enhanced with more complex client-rendered UI behaviors.

---

## [Anchor to Progressive enhancement](/docs/storefronts/headless/hydrogen/cart#progressive-enhancement)Progressive enhancement

Customers expect a fast, modern user experience, which typically means eliminating full-page reloads. Hydrogen is built on React Router, which includes robust methods for [progressively enhancing](https://reactrouter.com/explanation/progressive-enhancement) standard web forms. So Hydrogen's cart components also include interactive client-side features like optimistic UI updates, loading indicators, and validation feedback.

---

## [Anchor to Cart customizations](/docs/storefronts/headless/hydrogen/cart#cart-customizations)Cart customizations

Hydrogen's built-in cart includes components and utilities that cover a range of common use cases, including adding, updating, and removing products, selecting variants, managing metafields, applying discount codes, and more. The handler is also extensible, allowing you to add custom cart features, or even override built-in functionality.

---

## [Anchor to Next steps](/docs/storefronts/headless/hydrogen/cart#next-steps)Next steps

* Learn how to [set up the Hydrogen cart handler](/docs/storefronts/headless/hydrogen/cart/setup) in Hydrogen.

---

Was this page helpful?

YesNo