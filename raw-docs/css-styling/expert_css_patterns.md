---
source: expert-written
---

# Shopify Theme CSS & Styling Patterns

## CSS Architecture in Shopify Themes

### File Structure
Shopify themes store CSS in the `assets/` directory. Dawn theme uses:
- `base.css` — CSS custom properties, resets, typography, utilities
- `section-*.css` — Per-section styles loaded on demand
- `component-*.css` — Reusable component styles
- `global.css` or `theme.css` — Global styles loaded on every page

### Loading CSS in Liquid
```liquid
{%- comment -%} In layout/theme.liquid {%- endcomment -%}
{{ 'base.css' | asset_url | stylesheet_tag }}

{%- comment -%} Lazy-load section CSS {%- endcomment -%}
<link rel="stylesheet" href="{{ 'section-header.css' | asset_url }}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{{ 'section-header.css' | asset_url }}"></noscript>
```

### Using the `{% style %}` Tag
For section-specific inline CSS with Liquid variables:
```liquid
{% style %}
  .section-{{ section.id }} {
    background-color: {{ section.settings.background_color }};
    padding-top: {{ section.settings.padding_top }}px;
    padding-bottom: {{ section.settings.padding_bottom }}px;
  }
{% endstyle %}
```

## Responsive Design Patterns

### Media Queries in Shopify Themes
Dawn theme breakpoints:
```css
/* Mobile first approach */
@media screen and (min-width: 750px) {
  /* Tablet and above */
}
@media screen and (min-width: 990px) {
  /* Desktop */
}
@media screen and (min-width: 1400px) {
  /* Large desktop */
}
```

### CSS Grid for Collection Pages
```css
.collection-product-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

@media screen and (min-width: 750px) {
  .collection-product-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media screen and (min-width: 990px) {
  .collection-product-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

### Flexbox Layouts
```css
/* Product card layout */
.product-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.product-card__media {
  flex-shrink: 0;
  aspect-ratio: 1;
  overflow: hidden;
}
.product-card__info {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  padding: 1rem;
}
.product-card__price {
  margin-top: auto;
}

/* Header with flexbox */
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}
```

## Hover Effects & Animations

### Product Card Hover
```css
.product-card__media img {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.product-card:hover .product-card__media img {
  transform: scale(1.05);
}

/* Reveal second image on hover */
.product-card__media-secondary {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.product-card:hover .product-card__media-secondary {
  opacity: 1;
}
```

### Button Hover Effects
```css
.button {
  position: relative;
  overflow: hidden;
  transition: color 0.3s ease, background-color 0.3s ease;
}
.button:hover {
  background-color: var(--color-button-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
```

### Scroll Animations with CSS
```css
.reveal-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal-on-scroll.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

## Dark Mode in Shopify Themes

### CSS Custom Properties Approach
```css
:root {
  --color-background: #ffffff;
  --color-foreground: #121212;
  --color-primary: #121212;
  --color-secondary: #645f5b;
  --color-border: #e8e8e1;
}

[data-color-scheme="dark"] {
  --color-background: #1a1a2e;
  --color-foreground: #eaeaea;
  --color-primary: #ffffff;
  --color-secondary: #a0a0a0;
  --color-border: #333355;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-color-scheme="light"]) {
    --color-background: #1a1a2e;
    --color-foreground: #eaeaea;
  }
}
```

### Section-level color schemes
```liquid
{% schema %}
{
  "name": "My Section",
  "settings": [
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "default": "background-1",
      "label": "Color scheme"
    }
  ]
}
{% endschema %}

<div class="section color-{{ section.settings.color_scheme }}">
  <!-- content -->
</div>
```

## Tailwind CSS with Shopify

### Setup via CDN
```liquid
{%- comment -%} Quick Tailwind via CDN (dev only) {%- endcomment -%}
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: '{{ settings.color_primary }}',
          secondary: '{{ settings.color_secondary }}',
        }
      }
    }
  }
</script>
```

### Production Setup
For production, use Tailwind CLI with Shopify CLI:
1. `npm init` in theme root
2. `npm install tailwindcss`
3. Configure `tailwind.config.js` to scan `.liquid` files
4. Build CSS: `npx tailwindcss -i ./src/input.css -o ./assets/tailwind.css`
5. Include in theme: `{{ 'tailwind.css' | asset_url | stylesheet_tag }}`

## CSS Custom Properties (Design Tokens)

### Dawn Theme Pattern
```css
:root {
  --font-heading-family: {{ settings.type_header_font.family }}, {{ settings.type_header_font.fallback_families }};
  --font-heading-style: {{ settings.type_header_font.style }};
  --font-heading-weight: {{ settings.type_header_font.weight }};
  
  --font-body-family: {{ settings.type_body_font.family }}, {{ settings.type_body_font.fallback_families }};
  
  --page-width: {{ settings.page_width | divided_by: 10.0 }}rem;
  --grid-mobile-gap: 1rem;
  --grid-desktop-gap: 2rem;
}
```

## Sticky Header Pattern
```css
.header-wrapper {
  position: sticky;
  top: 0;
  z-index: 10;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.header-wrapper.scrolled {
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.header-wrapper.scroll-up {
  transform: translateY(0);
}

.header-wrapper.scroll-down {
  transform: translateY(-100%);
}
```

## Hamburger Menu (Mobile Navigation)
```css
.mobile-nav-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  background: none;
  border: none;
  cursor: pointer;
}

.mobile-nav-toggle__line {
  display: block;
  width: 24px;
  height: 2px;
  background: currentColor;
  transition: transform 0.3s, opacity 0.3s;
}

.mobile-nav-toggle[aria-expanded="true"] .mobile-nav-toggle__line:first-child {
  transform: translateY(7px) rotate(45deg);
}
.mobile-nav-toggle[aria-expanded="true"] .mobile-nav-toggle__line:nth-child(2) {
  opacity: 0;
}
.mobile-nav-toggle[aria-expanded="true"] .mobile-nav-toggle__line:last-child {
  transform: translateY(-7px) rotate(-45deg);
}

@media screen and (min-width: 990px) {
  .mobile-nav-toggle { display: none; }
}
```

## Masonry Grid Layout
```css
.masonry-grid {
  columns: 2;
  column-gap: 1.5rem;
}

.masonry-grid__item {
  break-inside: avoid;
  margin-bottom: 1.5rem;
}

@media screen and (min-width: 750px) {
  .masonry-grid { columns: 3; }
}

@media screen and (min-width: 990px) {
  .masonry-grid { columns: 4; }
}
```

## Form Styling in Shopify
```css
.field {
  position: relative;
  margin-bottom: 1.5rem;
}

.field__input {
  width: 100%;
  padding: 1rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background: var(--color-background);
  color: var(--color-foreground);
  font-size: 1rem;
  transition: border-color 0.2s;
}

.field__input:focus {
  border-color: var(--color-primary);
  outline: none;
  box-shadow: 0 0 0 2px rgba(var(--color-primary-rgb), 0.2);
}

/* Floating label */
.field__label {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  transition: all 0.2s ease;
  pointer-events: none;
  color: var(--color-secondary);
}

.field__input:focus + .field__label,
.field__input:not(:placeholder-shown) + .field__label {
  top: 0.25rem;
  font-size: 0.75rem;
  color: var(--color-primary);
}
```

## Performance: Deferring Non-Critical CSS
```liquid
{%- comment -%} 
  Defer non-critical CSS using media trick.
  Browser downloads but doesn't block render.
{%- endcomment -%}
<link rel="stylesheet" href="{{ 'section-footer.css' | asset_url }}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{{ 'section-footer.css' | asset_url }}"></noscript>
```

### Critical CSS Inline
```liquid
{%- comment -%} Inline critical above-the-fold CSS {%- endcomment -%}
<style>
  /* Only styles needed for initial viewport */
  .header, .hero { /* ... */ }
</style>

{%- comment -%} Load full CSS async {%- endcomment -%}
<link rel="preload" href="{{ 'base.css' | asset_url }}" as="style" onload="this.onload=null;this.rel='stylesheet'">
```
