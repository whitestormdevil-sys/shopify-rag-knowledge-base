---
source: compiled-expert-knowledge
---

# Shopify Performance Optimization Patterns

## 1. Critical Rendering Path

### Preconnect to Critical Origins
```liquid
<!-- layout/theme.liquid <head> -->
<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>
<link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>
<link rel="dns-prefetch" href="https://productreviews.shopifycdn.com">
```

### Inline Critical CSS
```liquid
{% style %}
  /* Inline only above-fold critical styles */
  :root { --color-primary: {{ settings.color_primary }}; }
  .header { /* ... */ }
  .hero { /* ... */ }
{% endstyle %}

<!-- Defer non-critical CSS -->
<link rel="stylesheet" href="{{ 'theme.css' | asset_url }}" media="print" onload="this.media='all'">
```

## 2. Image Optimization

### Responsive Images with srcset
```liquid
{{ image | image_url: width: 1500 | image_tag:
   widths: '165, 360, 535, 750, 1000, 1500',
   sizes: '(min-width: 1200px) calc((1200px - 10rem) / 4), (min-width: 750px) calc((100vw - 10rem) / 2), calc(100vw - 3rem)',
   loading: 'lazy',
   decoding: 'async',
   fetchpriority: 'auto' }}
```

### LCP Image — No Lazy Load!
```liquid
{%- if forloop.first -%}
  {{ image | image_url: width: 1500 | image_tag:
     loading: 'eager',
     fetchpriority: 'high',
     decoding: 'sync',
     widths: '750, 1000, 1500' }}
{%- else -%}
  {{ image | image_url: width: 1500 | image_tag:
     loading: 'lazy',
     decoding: 'async' }}
{%- endif -%}
```

### Preload Hero Image
```liquid
{%- if section.settings.image -%}
  <link rel="preload" as="image" 
        href="{{ section.settings.image | image_url: width: 1500 }}"
        imagesrcset="{{ section.settings.image | image_url: width: 750 }} 750w, {{ section.settings.image | image_url: width: 1500 }} 1500w"
        imagesizes="100vw">
{%- endif -%}
```

## 3. JavaScript Optimization

### Defer All Non-Critical JS
```liquid
<script src="{{ 'theme.js' | asset_url }}" defer></script>
```

### Use Web Components
```javascript
// Lazy-initialize components only when needed
class ProductForm extends HTMLElement {
  connectedCallback() {
    // Only runs when element is in DOM
    this.form = this.querySelector('form');
    this.form.addEventListener('submit', this.onSubmit.bind(this));
  }
}
customElements.define('product-form', ProductForm);
```

### Intersection Observer for Lazy Components
```javascript
// Don't load carousel JS until it's visible
const lazyComponents = document.querySelectorAll('[data-lazy-component]');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const script = document.createElement('script');
      script.src = entry.target.dataset.lazyComponent;
      document.body.appendChild(script);
      observer.unobserve(entry.target);
    }
  });
});
lazyComponents.forEach(el => observer.observe(el));
```

## 4. Font Optimization

### Preload Critical Fonts
```liquid
{%- if settings.type_header_font != blank -%}
  <link rel="preload" as="font" type="font/woff2" 
        href="{{ settings.type_header_font | font_url }}" crossorigin>
{%- endif -%}
```

### Use font-display: swap
```liquid
{% style %}
  {{ settings.type_body_font | font_face: font_display: 'swap' }}
  {{ settings.type_header_font | font_face: font_display: 'swap' }}
{% endstyle %}
```

### Limit Font Variants
- Load only weights you use (e.g., 400, 700)
- Avoid loading italic if not used
- System font stack fallback: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`

## 5. Reduce Third-Party Impact

### Load Third-Party Scripts After Interaction
```javascript
// Only load chat widget / analytics after user interacts
let thirdPartyLoaded = false;
['mouseover', 'touchstart', 'scroll', 'keydown'].forEach(event => {
  window.addEventListener(event, () => {
    if (thirdPartyLoaded) return;
    thirdPartyLoaded = true;
    // Load chat widget, extra analytics, etc.
    loadScript('https://widget.example.com/chat.js');
  }, { once: true });
});
```

## 6. Section Rendering API for Dynamic Content

```javascript
// Instead of full page reloads for cart/filter updates
async function refreshSection(sectionId) {
  const url = `${window.location.pathname}?sections=${sectionId}`;
  const response = await fetch(url);
  const data = await response.json();
  
  const tempDoc = new DOMParser().parseFromString(data[sectionId], 'text/html');
  const newContent = tempDoc.querySelector(`#shopify-section-${sectionId}`);
  document.querySelector(`#shopify-section-${sectionId}`).replaceWith(newContent);
}
```

## 7. Shopify-Specific Performance Rules

1. **Never use `| asset_url` on `'all'`** — loads every asset
2. **Minimize Liquid loops** — O(n²) nested loops kill TTFB
3. **Use `{% render %}` not `{% include %}`** — render is faster (isolated scope)
4. **Avoid `{% for product in collections.all.products %}`** — fetches everything
5. **Limit `{{ content_for_header }}` impact** — it's required but adds 10-30KB
6. **Use `{% cache %}` blocks** where available (OS 2.0+)
7. **Paginate collections** — max 50 per page, use less for faster TTFB

## 8. Core Web Vitals Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| INP | ≤ 200ms | ≤ 500ms | > 500ms |
| CLS | ≤ 0.1 | ≤ 0.25 | > 0.25 |

### Common Shopify CLS Causes:
- Images without explicit width/height
- Dynamically injected banners/bars
- Font swap causing layout shift
- Late-loading app blocks

### Common Shopify LCP Issues:
- Hero image not preloaded
- Lazy-loading above-fold images
- Render-blocking CSS (large theme.css)
- Slow TTFB from complex Liquid
