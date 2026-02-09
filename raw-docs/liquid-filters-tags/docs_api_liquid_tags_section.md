---
source: https://shopify.dev/docs/api/liquid/tags/section
---

Renders a [section](/themes/architecture/sections).

Rendering a section with the `section` tag renders a section statically. To learn more about sections and how to use
them in your theme, refer to [Render a section](/themes/architecture/sections#render-a-section).

## Syntax

9

1

{% section 'name' %}

name

The name of the section file you want to render.

9

1

{% section 'header' %}

##### Code

```liquid
{% section 'header' %}
```

##### Data

```liquid
{
  "cart": {
    "item_count": 2
  },
  "request": {
    "origin": "https://polinas-potent-potions.myshopify.com",
    "page_type": "index"
  },
  "routes": {
    "account_url": "/account",
    "cart_url": "/cart",
    "root_url": "/",
    "search_url": "/search"
  },
  "settings": {
    "accent_icons": "text",
    "cart_type": "notification",
    "inputs_shadow_vertical_offset": 4,
    "predictive_search_enabled": true,
    "social_facebook_link": "",
    "social_instagram_link": "",
    "social_pinterest_link": "",
    "social_snapchat_link": "",
    "social_tiktok_link": "",
    "social_tumblr_link": "",
    "social_twitter_link": "",
    "social_vimeo_link": "",
    "social_youtube_link": ""
  },
  "shop": {
    "customer_accounts_enabled": true,
    "name": "Polina&#39;s Potent Potions"
  }
}
```

## Output

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

<div id="shopify-section-header" class="shopify-section section-header"><link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-list-menu.css?v=151968516119678728991663872413" media="print" onload="this.media='all'">

<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-search.css?v=96455689198851321781663872411" media="print" onload="this.media='all'">

<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-menu-drawer.css?v=182311192829367774911663872416" media="print" onload="this.media='all'">

<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-notification.css?v=183358051719344305851663872409" media="print" onload="this.media='all'">

<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-items.css?v=23917223812499722491663872408" media="print" onload="this.media='all'"><link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-price.css?v=65402837579211014041663872409" media="print" onload="this.media='all'">

<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-loading-overlay.css?v=167310470843593579841663872415" media="print" onload="this.media='all'"><noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-list-menu.css?v=151968516119678728991663872413" rel="stylesheet" type="text/css" media="all" /></noscript>

<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-search.css?v=96455689198851321781663872411" rel="stylesheet" type="text/css" media="all" /></noscript>

<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-menu-drawer.css?v=182311192829367774911663872416" rel="stylesheet" type="text/css" media="all" /></noscript>

<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-notification.css?v=183358051719344305851663872409" rel="stylesheet" type="text/css" media="all" /></noscript>

<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-items.css?v=23917223812499722491663872408" rel="stylesheet" type="text/css" media="all" /></noscript>

<style>

header-drawer {

justify-self: start;

margin-left: -1.2rem;

}

.header\_\_heading-logo {

max-width: 90px;

}

@media screen and (min-width: 990px) {

header-drawer {

display: none;

}

}

.menu-drawer-container {

display: flex;

}

.list-menu {

list-style: none;

padding: 0;

margin: 0;

}

##### Output

```liquid
<div id="shopify-section-header" class="shopify-section section-header"><link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-list-menu.css?v=151968516119678728991663872413" media="print" onload="this.media='all'">
<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-search.css?v=96455689198851321781663872411" media="print" onload="this.media='all'">
<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-menu-drawer.css?v=182311192829367774911663872416" media="print" onload="this.media='all'">
<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-notification.css?v=183358051719344305851663872409" media="print" onload="this.media='all'">
<link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-items.css?v=23917223812499722491663872408" media="print" onload="this.media='all'"><link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-price.css?v=65402837579211014041663872409" media="print" onload="this.media='all'">
  <link rel="stylesheet" href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-loading-overlay.css?v=167310470843593579841663872415" media="print" onload="this.media='all'"><noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-list-menu.css?v=151968516119678728991663872413" rel="stylesheet" type="text/css" media="all" /></noscript>
<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-search.css?v=96455689198851321781663872411" rel="stylesheet" type="text/css" media="all" /></noscript>
<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-menu-drawer.css?v=182311192829367774911663872416" rel="stylesheet" type="text/css" media="all" /></noscript>
<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-notification.css?v=183358051719344305851663872409" rel="stylesheet" type="text/css" media="all" /></noscript>
<noscript><link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/component-cart-items.css?v=23917223812499722491663872408" rel="stylesheet" type="text/css" media="all" /></noscript>

<style>
  header-drawer {
    justify-self: start;
    margin-left: -1.2rem;
  }

  .header__heading-logo {
    max-width: 90px;
  }

  @media screen and (min-width: 990px) {
    header-drawer {
      display: none;
    }
  }

  .menu-drawer-container {
    display: flex;
  }

  .list-menu {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .list-menu--inline {
    display: inline-flex;
    flex-wrap: wrap;
  }

  summary.list-menu__item {
    padding-right: 2.7rem;
  }

  .list-menu__item {
    display: flex;
    align-items: center;
    line-height: calc(1 + 0.3 / var(--font-body-scale));
  }

  .list-menu__item--link {
    text-decoration: none;
    padding-bottom: 1rem;
    padding-top: 1rem;
    line-height: calc(1 + 0.8 / var(--font-body-scale));
  }

  @media screen and (min-width: 750px) {
    .list-menu__item--link {
      padding-bottom: 0.5rem;
      padding-top: 0.5rem;
    }
  }
</style><style data-shopify>.header {
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .section-header {
    margin-bottom: 0px;
  }

  @media screen and (min-width: 750px) {
    .section-header {
      margin-bottom: 0px;
    }
  }

  @media screen and (min-width: 990px) {
    .header {
      padding-top: 20px;
      padding-bottom: 20px;
    }
  }</style><script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/details-disclosure.js?v=153497636716254413831663872415" defer="defer"></script>
<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/details-modal.js?v=4511761896672669691663872416" defer="defer"></script>
<script src="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart-notification.js?v=160453272920806432391663872410" defer="defer"></script><svg xmlns="http://www.w3.org/2000/svg" class="hidden">
  <symbol id="icon-search" viewbox="0 0 18 19" fill="none">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M11.03 11.68A5.784 5.784 0 112.85 3.5a5.784 5.784 0 018.18 8.18zm.26 1.12a6.78 6.78 0 11.72-.7l5.4 5.4a.5.5 0 11-.71.7l-5.41-5.4z" fill="currentColor"/>
  </symbol>

  <symbol id="icon-close" class="icon icon-close" fill="none" viewBox="0 0 18 17">
    <path d="M.865 15.978a.5.5 0 00.707.707l7.433-7.431 7.579 7.282a.501.501 0 00.846-.37.5.5 0 00-.153-.351L9.712 8.546l7.417-7.416a.5.5 0 10-.707-.708L8.991 7.853 1.413.573a.5.5 0 10-.693.72l7.563 7.268-7.418 7.417z" fill="currentColor">
  </symbol>
</svg>
<sticky-header class="header-wrapper color-background-1 gradient header-wrapper--border-bottom">
  <header class="header header--middle-left header--mobile-center page-width header--has-menu"><header-drawer data-breakpoint="tablet">
        <details id="Details-menu-drawer-container" class="menu-drawer-container">
          <summary class="header__icon header__icon--menu header__icon--summary link focus-inset" aria-label="Menu">
            <span>
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" role="presentation" class="icon icon-hamburger" fill="none" viewBox="0 0 18 16">
  <path d="M1 .5a.5.5 0 100 1h15.71a.5.5 0 000-1H1zM.5 8a.5.5 0 01.5-.5h15.71a.5.5 0 010 1H1A.5.5 0 01.5 8zm0 7a.5.5 0 01.5-.5h15.71a.5.5 0 010 1H1a.5.5 0 01-.5-.5z" fill="currentColor">
</svg>

              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" role="presentation" class="icon icon-close" fill="none" viewBox="0 0 18 17">
  <path d="M.865 15.978a.5.5 0 00.707.707l7.433-7.431 7.579 7.282a.501.501 0 00.846-.37.5.5 0 00-.153-.351L9.712 8.546l7.417-7.416a.5.5 0 10-.707-.708L8.991 7.853 1.413.573a.5.5 0 10-.693.72l7.563 7.268-7.418 7.417z" fill="currentColor">
</svg>

            </span>
          </summary>
          <div id="menu-drawer" class="gradient menu-drawer motion-reduce" tabindex="-1">
            <div class="menu-drawer__inner-container">
              <div class="menu-drawer__navigation-container">
                <nav class="menu-drawer__navigation">
                  <ul class="menu-drawer__menu has-submenu list-menu" role="list"><li><a href="/" class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                            Home
                          </a></li><li><details id="Details-menu-drawer-menu-item-2">
                            <summary class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                              Catalog
                              <svg viewBox="0 0 14 10" fill="none" aria-hidden="true" focusable="false" role="presentation" class="icon icon-arrow" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.537.808a.5.5 0 01.817-.162l4 4a.5.5 0 010 .708l-4 4a.5.5 0 11-.708-.708L11.793 5.5H1a.5.5 0 010-1h10.793L8.646 1.354a.5.5 0 01-.109-.546z" fill="currentColor">
</svg>

                              <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-caret" viewBox="0 0 10 6">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">
</svg>

                            </summary>
                            <div id="link-catalog" class="menu-drawer__submenu has-submenu gradient motion-reduce" tabindex="-1">
                              <div class="menu-drawer__inner-submenu">
                                <button class="menu-drawer__close-button link link--text focus-inset" aria-expanded="true">
                                  <svg viewBox="0 0 14 10" fill="none" aria-hidden="true" focusable="false" role="presentation" class="icon icon-arrow" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.537.808a.5.5 0 01.817-.162l4 4a.5.5 0 010 .708l-4 4a.5.5 0 11-.708-.708L11.793 5.5H1a.5.5 0 010-1h10.793L8.646 1.354a.5.5 0 01-.109-.546z" fill="currentColor">
</svg>

                                  Catalog
                                </button>
                                <ul class="menu-drawer__menu list-menu" role="list" tabindex="-1"><li><a href="/collections/potions" class="menu-drawer__menu-item link link--text list-menu__item focus-inset">
                                          Potions
                                        </a></li><li><a href="/collections/ingredients" class="menu-drawer__menu-item link link--text list-menu__item focus-inset">
                                          Ingredients
                                        </a></li></ul>
                              </div>
                            </div>
                          </details></li><li><a href="/pages/contact" class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                            Contact
                          </a></li></ul>
                </nav>
                <div class="menu-drawer__utility-links"><a href="/account" class="menu-drawer__account link focus-inset h5">
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" role="presentation" class="icon icon-account" fill="none" viewBox="0 0 18 19">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M6 4.5a3 3 0 116 0 3 3 0 01-6 0zm3-4a4 4 0 100 8 4 4 0 000-8zm5.58 12.15c1.12.82 1.83 2.24 1.91 4.85H1.51c.08-2.6.79-4.03 1.9-4.85C4.66 11.75 6.5 11.5 9 11.5s4.35.26 5.58 1.15zM9 10.5c-2.5 0-4.65.24-6.17 1.35C1.27 12.98.5 14.93.5 18v.5h17V18c0-3.07-.77-5.02-2.33-6.15-1.52-1.1-3.67-1.35-6.17-1.35z" fill="currentColor">
</svg>

Account</a><ul class="list list-social list-unstyled" role="list"></ul>
                </div>
              </div>
            </div>
          </div>
        </details>
      </header-drawer><h1 class="header__heading"><a href="/" class="header__heading-link link link--text focus-inset"><span class="h2">Polina&#39;s Potent Potions</span></a></h1><nav class="header__inline-menu">
          <ul class="list-menu list-menu--inline" role="list"><li><a href="/" class="header__menu-item list-menu__item link link--text focus-inset">
                    <span>Home</span>
                  </a></li><li><header-menu>
                    <details id="Details-HeaderMenu-2">
                      <summary class="header__menu-item list-menu__item link focus-inset">
                        <span>Catalog</span>
                        <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-caret" viewBox="0 0 10 6">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M9.354.646a.5.5 0 00-.708 0L5 4.293 1.354.646a.5.5 0 00-.708.708l4 4a.5.5 0 00.708 0l4-4a.5.5 0 000-.708z" fill="currentColor">
</svg>

                      </summary>
                      <ul id="HeaderMenu-MenuList-2" class="header__submenu list-menu list-menu--disclosure gradient caption-large motion-reduce global-settings-popup" role="list" tabindex="-1"><li><a href="/collections/potions" class="header__menu-item list-menu__item link link--text focus-inset caption-large">
                                Potions
                              </a></li><li><a href="/collections/ingredients" class="header__menu-item list-menu__item link link--text focus-inset caption-large">
                                Ingredients
                              </a></li></ul>
                    </details>
                  </header-menu></li><li><a href="/pages/contact" class="header__menu-item list-menu__item link link--text focus-inset">
                    <span>Contact</span>
                  </a></li></ul>
        </nav><div class="header__icons">
      <details-modal class="header__search">
        <details>
          <summary class="header__icon header__icon--search header__icon--summary link focus-inset modal__toggle" aria-haspopup="dialog" aria-label="Search">
            <span>
              <svg class="modal__toggle-open icon icon-search" aria-hidden="true" focusable="false" role="presentation">
                <use href="#icon-search">
              </svg>
              <svg class="modal__toggle-close icon icon-close" aria-hidden="true" focusable="false" role="presentation">
                <use href="#icon-close">
              </svg>
            </span>
          </summary>
          <div class="search-modal modal__content gradient" role="dialog" aria-modal="true" aria-label="Search">
            <div class="modal-overlay"></div>
            <div class="search-modal__content search-modal__content-bottom" tabindex="-1"><predictive-search class="search-modal__form" data-loading-text="Loading..."><form action="/search" method="get" role="search" class="search search-modal__form">
                  <div class="field">
                    <input class="search__input field__input"
                      id="Search-In-Modal"
                      type="search"
                      name="q"
                      value=""
                      placeholder="Search"role="combobox"
                        aria-expanded="false"
                        aria-owns="predictive-search-results-list"
                        aria-controls="predictive-search-results-list"
                        aria-haspopup="listbox"
                        aria-autocomplete="list"
                        autocorrect="off"
                        autocomplete="off"
                        autocapitalize="off"
                        spellcheck="false">
                    <label class="field__label" for="Search-In-Modal">Search</label>
                    <input type="hidden" name="options[prefix]" value="last">
                    <button class="search__button field__button" aria-label="Search">
                      <svg class="icon icon-search" aria-hidden="true" focusable="false" role="presentation">
                        <use href="#icon-search">
                      </svg>
                    </button>
                  </div><div class="predictive-search predictive-search--header" tabindex="-1" data-predictive-search>
                      <div class="predictive-search__loading-state">
                        <svg aria-hidden="true" focusable="false" role="presentation" class="spinner" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg">
                          <circle class="path" fill="none" stroke-width="6" cx="33" cy="33" r="30"></circle>
                        </svg>
                      </div>
                    </div>

                    <span class="predictive-search-status visually-hidden" role="status" aria-hidden="true"></span></form></predictive-search><button type="button" class="search-modal__close-button modal__close-button link link--text focus-inset" aria-label="Close">
                <svg class="icon icon-close" aria-hidden="true" focusable="false" role="presentation">
                  <use href="#icon-close">
                </svg>
              </button>
            </div>
          </div>
        </details>
      </details-modal><a href="/account" class="header__icon header__icon--account link focus-inset small-hide">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" role="presentation" class="icon icon-account" fill="none" viewBox="0 0 18 19">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M6 4.5a3 3 0 116 0 3 3 0 01-6 0zm3-4a4 4 0 100 8 4 4 0 000-8zm5.58 12.15c1.12.82 1.83 2.24 1.91 4.85H1.51c.08-2.6.79-4.03 1.9-4.85C4.66 11.75 6.5 11.5 9 11.5s4.35.26 5.58 1.15zM9 10.5c-2.5 0-4.65.24-6.17 1.35C1.27 12.98.5 14.93.5 18v.5h17V18c0-3.07-.77-5.02-2.33-6.15-1.52-1.1-3.67-1.35-6.17-1.35z" fill="currentColor">
</svg>

          <span class="visually-hidden">Account</span>
        </a><a href="/cart" class="header__icon header__icon--cart link focus-inset" id="cart-icon-bubble"><svg class="icon icon-cart" aria-hidden="true" focusable="false" role="presentation" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" fill="none">
  <path fill="currentColor" fill-rule="evenodd" d="M20.5 6.5a4.75 4.75 0 00-4.75 4.75v.56h-3.16l-.77 11.6a5 5 0 004.99 5.34h7.38a5 5 0 004.99-5.33l-.77-11.6h-3.16v-.57A4.75 4.75 0 0020.5 6.5zm3.75 5.31v-.56a3.75 3.75 0 10-7.5 0v.56h7.5zm-7.5 1h7.5v.56a3.75 3.75 0 11-7.5 0v-.56zm-1 0v.56a4.75 4.75 0 109.5 0v-.56h2.22l.71 10.67a4 4 0 01-3.99 4.27h-7.38a4 4 0 01-4-4.27l.72-10.67h2.22z"/>
</svg>
<span class="visually-hidden">Cart</span><div class="cart-count-bubble"><span aria-hidden="true">2</span><span class="visually-hidden">2 items</span>
          </div></a>
    </div>
  </header>
</sticky-header>

<cart-notification>
  <div class="cart-notification-wrapper page-width">
    <div id="cart-notification" class="cart-notification focus-inset color-background-1 gradient" aria-modal="true" aria-label="Item added to your cart" role="dialog" tabindex="-1">
      <div class="cart-notification__header">
        <h2 class="cart-notification__heading caption-large text-body"><svg class="icon icon-checkmark color-foreground-text" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 9" fill="none">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M11.35.643a.5.5 0 01.006.707l-6.77 6.886a.5.5 0 01-.719-.006L.638 4.845a.5.5 0 11.724-.69l2.872 3.011 6.41-6.517a.5.5 0 01.707-.006h-.001z" fill="currentColor"/>
</svg>
Item added to your cart</h2>
        <button type="button" class="cart-notification__close modal__close-button link link--text focus-inset" aria-label="Close">
          <svg class="icon icon-close" aria-hidden="true" focusable="false"><use href="#icon-close"></svg>
        </button>
      </div>
      <div id="cart-notification-product" class="cart-notification-product"></div>
      <div class="cart-notification__links">
        <a href="/cart" id="cart-notification-button" class="button button--secondary button--full-width"></a>
        <form action="/cart" method="post" id="cart-notification-form">
          <button class="button button--primary button--full-width" name="checkout">Check out</button>
        </form>
        <button type="button" class="link button-label">Continue shopping</button>
      </div>
    </div>
  </div>
</cart-notification>
<style data-shopify>
  .cart-notification {
     display: none;
  }
</style>


<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "Polina\u0026#39;s Potent Potions",
    
    "sameAs": [
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
    ],
    "url": "https:\/\/polinas-potent-potions.myshopify.com"
  }
</script>
  <script type="application/ld+json">
    {
      "@context": "http://schema.org",
      "@type": "WebSite",
      "name": "Polina\u0026#39;s Potent Potions",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https:\/\/polinas-potent-potions.myshopify.com\/search?q={search_term_string}",
        "query-input": "required name=search_term_string"
      },
      "url": "https:\/\/polinas-potent-potions.myshopify.com"
    }
  </script>
</div>
```

Was this page helpful?

YesNo