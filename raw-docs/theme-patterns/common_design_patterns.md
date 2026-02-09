---
source: compiled-expert-knowledge
---

# Shopify Theme Design Patterns — Comprehensive Reference

## 1. Cart Drawer (Ajax Cart / Side Cart)

The most common modern cart pattern. Cart opens as a slide-out drawer without page navigation.

### Implementation Pattern:
```liquid
<!-- snippets/cart-drawer.liquid -->
<div id="cart-drawer" class="cart-drawer" aria-hidden="true" role="dialog">
  <div class="cart-drawer__overlay" data-cart-drawer-close></div>
  <div class="cart-drawer__content">
    <header class="cart-drawer__header">
      <h2>{{ 'cart.general.title' | t }} ({{ cart.item_count }})</h2>
      <button data-cart-drawer-close aria-label="{{ 'accessibility.close' | t }}">×</button>
    </header>
    
    <div class="cart-drawer__items">
      {% for item in cart.items %}
        {% render 'cart-drawer-item', item: item %}
      {% endfor %}
    </div>
    
    <footer class="cart-drawer__footer">
      <div class="cart-drawer__subtotal">
        <span>{{ 'cart.general.subtotal' | t }}</span>
        <span>{{ cart.total_price | money }}</span>
      </div>
      <a href="{{ routes.cart_url }}" class="button button--secondary">{{ 'cart.general.view_cart' | t }}</a>
      <button type="submit" name="checkout" class="button button--primary">{{ 'cart.general.checkout' | t }}</button>
    </footer>
  </div>
</div>
```

### JavaScript Pattern:
```javascript
// Use Section Rendering API for dynamic updates
async function updateCartDrawer() {
  const response = await fetch('/?sections=cart-drawer');
  const data = await response.json();
  document.getElementById('cart-drawer').innerHTML = 
    new DOMParser().parseFromString(data['cart-drawer'], 'text/html')
      .querySelector('#cart-drawer').innerHTML;
}

// Add to cart via Ajax
async function addToCart(formData) {
  await fetch('/cart/add.js', { method: 'POST', body: formData });
  await updateCartDrawer();
  openCartDrawer();
}
```

### Key Gotcha:
- Always use Section Rendering API (`/?sections=section-id`) for updates, NOT innerHTML from `/cart` page
- Cart item count badge should update globally (header + drawer)
- Handle empty cart state gracefully


## 2. Quick Add / Quick Buy

Add to cart directly from collection pages without visiting PDP.

### Pattern:
```liquid
<!-- snippets/quick-add-button.liquid -->
{% if product.variants.size == 1 and product.available %}
  <form action="/cart/add" method="post">
    <input type="hidden" name="id" value="{{ product.variants.first.id }}">
    <button type="submit" class="quick-add-btn">
      {{ 'products.product.add_to_cart' | t }}
    </button>
  </form>
{% elsif product.available %}
  <button class="quick-add-btn" data-quick-add="{{ product.handle }}">
    {{ 'products.product.choose_options' | t }}
  </button>
{% else %}
  <button class="quick-add-btn" disabled>
    {{ 'products.product.sold_out' | t }}
  </button>
{% endif %}
```

### For multi-variant products — use a modal:
```javascript
// Fetch product form via Section Rendering API
async function openQuickAdd(handle) {
  const response = await fetch(`/products/${handle}?sections=quick-add-modal`);
  const html = await response.json()['quick-add-modal'];
  showModal(html);
}
```


## 3. Color/Variant Swatches

Visual option selectors instead of dropdowns.

### Pattern:
```liquid
<!-- snippets/variant-swatches.liquid -->
{% for option in product.options_with_values %}
  <fieldset class="swatch-group" data-option-index="{{ forloop.index0 }}">
    <legend>{{ option.name }}</legend>
    {% for value in option.values %}
      {% assign variant_for_value = product.variants | where: option.name, value | first %}
      <label class="swatch{% if option.selected_value == value %} swatch--active{% endif %}{% unless variant_for_value.available %} swatch--unavailable{% endunless %}">
        <input type="radio" 
               name="{{ option.name }}" 
               value="{{ value }}"
               {% if option.selected_value == value %}checked{% endif %}>
        
        {% if option.name == 'Color' or option.name == 'Colour' %}
          {%- assign color_handle = value | handleize -%}
          <span class="swatch__color" 
                style="background-color: {{ value | downcase }};"
                title="{{ value }}">
          </span>
        {% else %}
          <span class="swatch__label">{{ value }}</span>
        {% endif %}
      </label>
    {% endfor %}
  </fieldset>
{% endfor %}
```

### Key considerations:
- Handle color names that aren't CSS colors (use metafields for hex codes)
- Cross out unavailable variants (strikethrough on swatch)
- Update product image when color swatch changes
- Consider using `option_selection.js` or custom variant picker


## 4. Product Image Gallery

Thumbnail navigation + zoom + swipe on mobile.

### Pattern:
```liquid
<!-- sections/product-gallery.liquid -->
<div class="product-gallery" data-product-gallery>
  <div class="product-gallery__main">
    {% for media in product.media %}
      <div class="product-gallery__slide" 
           data-media-id="{{ media.id }}"
           data-media-type="{{ media.media_type }}">
        {% case media.media_type %}
          {% when 'image' %}
            {{ media | image_url: width: 1200 | image_tag: 
               loading: 'lazy',
               widths: '300,600,900,1200',
               sizes: '(min-width: 750px) 50vw, 100vw' }}
          {% when 'video' %}
            {{ media | video_tag: autoplay: false, controls: true }}
          {% when 'external_video' %}
            {{ media | external_video_tag }}
          {% when 'model' %}
            {{ media | model_viewer_tag }}
        {% endcase %}
      </div>
    {% endfor %}
  </div>
  
  <div class="product-gallery__thumbs">
    {% for media in product.media %}
      <button class="product-gallery__thumb" 
              data-target="{{ media.id }}"
              aria-label="{{ media.alt | escape }}">
        {{ media.preview_image | image_url: width: 100 | image_tag }}
      </button>
    {% endfor %}
  </div>
</div>
```


## 5. Infinite Scroll / Load More

For collection pages.

### Pattern:
```javascript
// Intersection Observer for infinite scroll
const sentinel = document.querySelector('.collection-sentinel');
const observer = new IntersectionObserver(async (entries) => {
  if (entries[0].isIntersecting && hasNextPage) {
    const nextUrl = document.querySelector('.pagination__next')?.href;
    if (!nextUrl) return;
    
    const response = await fetch(nextUrl);
    const html = await response.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const newProducts = doc.querySelectorAll('.product-card');
    
    const grid = document.querySelector('.collection-grid');
    newProducts.forEach(card => grid.appendChild(card));
    
    // Update pagination link
    const newNext = doc.querySelector('.pagination__next');
    if (!newNext) hasNextPage = false;
    else document.querySelector('.pagination__next').href = newNext.href;
  }
});
observer.observe(sentinel);
```


## 6. Predictive Search

Live search with results dropdown.

### Pattern:
```liquid
<!-- snippets/predictive-search.liquid -->
<div class="predictive-search" data-predictive-search>
  <form action="{{ routes.search_url }}" method="get" role="search">
    <input type="search" 
           name="q" 
           autocomplete="off"
           aria-label="{{ 'general.search.placeholder' | t }}"
           data-search-input>
    <div class="predictive-search__results" aria-live="polite" hidden>
      <!-- Results injected via JS -->
    </div>
  </form>
</div>
```

```javascript
// Debounced predictive search
let searchTimeout;
searchInput.addEventListener('input', (e) => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(async () => {
    if (e.target.value.length < 2) return;
    
    const response = await fetch(
      `/search/suggest.json?q=${encodeURIComponent(e.target.value)}&resources[type]=product,collection,article,page&resources[limit]=4`
    );
    const data = await response.json();
    renderPredictiveResults(data.resources.results);
  }, 300);
});
```


## 7. Sticky Add to Cart

Fixed add-to-cart bar when scrolling past the main CTA.

### Pattern:
```javascript
const addToCartBtn = document.querySelector('.product-form__submit');
const stickyBar = document.querySelector('.sticky-add-to-cart');

const observer = new IntersectionObserver(([entry]) => {
  stickyBar.classList.toggle('is-visible', !entry.isIntersecting);
}, { threshold: 0 });

observer.observe(addToCartBtn);
```


## 8. Size Chart Modal

Common for apparel stores.

### Pattern:
```liquid
{% if product.type contains 'shirt' or product.type contains 'pants' %}
  <button data-size-chart-open class="size-chart-link">
    {{ 'products.product.size_chart' | t }}
  </button>
  
  <div id="size-chart-modal" class="modal" aria-hidden="true">
    <div class="modal__content">
      {{ pages['size-chart'].content }}
    </div>
  </div>
{% endif %}
```


## 9. Recently Viewed Products

Track viewed products in localStorage.

### Pattern:
```javascript
// Track
function trackRecentlyViewed(productId) {
  let viewed = JSON.parse(localStorage.getItem('recently-viewed') || '[]');
  viewed = viewed.filter(id => id !== productId);
  viewed.unshift(productId);
  viewed = viewed.slice(0, 10);
  localStorage.setItem('recently-viewed', JSON.stringify(viewed));
}

// Display via Section Rendering API
async function loadRecentlyViewed() {
  const viewed = JSON.parse(localStorage.getItem('recently-viewed') || '[]');
  if (!viewed.length) return;
  
  const response = await fetch(
    `/recommendations/products?product_id=${viewed[0]}&limit=4&intent=related§ion_id=recently-viewed`
  );
  // Or use product handles to fetch individually
}
```


## 10. Announcement Bar with Auto-Rotate

```liquid
<!-- sections/announcement-bar.liquid -->
{% if section.blocks.size > 0 %}
  <div class="announcement-bar" 
       data-announcement-bar
       role="region" 
       aria-label="{{ 'sections.announcement.label' | t }}">
    {% for block in section.blocks %}
      <div class="announcement-bar__message{% unless forloop.first %} hidden{% endunless %}" 
           {{ block.shopify_attributes }}>
        {% if block.settings.link != blank %}
          <a href="{{ block.settings.link }}">{{ block.settings.text }}</a>
        {% else %}
          <p>{{ block.settings.text }}</p>
        {% endif %}
      </div>
    {% endfor %}
  </div>
{% endif %}
```


## 11. Responsive Image Pattern (Best Practice)

```liquid
{%- assign image = section.settings.image -%}
{{ image | image_url: width: 1500 | image_tag:
   loading: 'lazy',
   decoding: 'async',
   widths: '375, 550, 750, 1100, 1500',
   sizes: '(min-width: 1200px) 1100px, (min-width: 750px) calc(100vw - 10rem), 100vw',
   alt: image.alt | escape,
   class: 'responsive-image' }}
```


## 12. Schema.org Structured Data

```liquid
<!-- snippets/structured-data-product.liquid -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "image": {{ product.featured_image | image_url: width: 1024 | prepend: 'https:' | json }},
  "description": {{ product.description | strip_html | truncate: 500 | json }},
  "brand": {
    "@type": "Brand",
    "name": {{ product.vendor | json }}
  },
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": {{ cart.currency.iso_code | json }},
    "lowPrice": {{ product.price_min | money_without_currency | json }},
    "highPrice": {{ product.price_max | money_without_currency | json }},
    "offerCount": {{ product.variants.size | json }},
    "availability": "https://schema.org/{% if product.available %}InStock{% else %}OutOfStock{% endif %}"
  }
}
</script>
```
