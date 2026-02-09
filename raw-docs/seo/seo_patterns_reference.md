---
source: compiled-expert-knowledge
---

# Shopify SEO Patterns & Best Practices

## 1. Meta Tags

```liquid
<!-- layout/theme.liquid -->
<head>
  <title>
    {%- if template.name == 'index' -%}
      {{ shop.name }} — {{ shop.description }}
    {%- elsif template.name == 'product' -%}
      {{ product.title }} | {{ shop.name }}
    {%- elsif template.name == 'collection' -%}
      {{ collection.title }} | {{ shop.name }}
    {%- elsif template.name == 'blog' -%}
      {{ blog.title }} | {{ shop.name }}
    {%- elsif template.name == 'article' -%}
      {{ article.title }} | {{ blog.title }} | {{ shop.name }}
    {%- elsif template.name == 'page' -%}
      {{ page.title }} | {{ shop.name }}
    {%- else -%}
      {{ page_title }} | {{ shop.name }}
    {%- endif -%}
  </title>
  
  {%- if page_description -%}
    <meta name="description" content="{{ page_description | escape }}">
  {%- endif -%}
  
  <link rel="canonical" href="{{ canonical_url }}">
  
  {%- if template.name == 'collection' and current_tags -%}
    <meta name="robots" content="noindex, follow">
  {%- endif -%}
  
  <!-- Open Graph -->
  <meta property="og:site_name" content="{{ shop.name }}">
  <meta property="og:url" content="{{ canonical_url }}">
  <meta property="og:title" content="{{ page_title }}">
  <meta property="og:type" content="{% if template.name == 'product' %}product{% elsif template.name == 'article' %}article{% else %}website{% endif %}">
  {%- if page_description -%}
    <meta property="og:description" content="{{ page_description | escape }}">
  {%- endif -%}
  {%- if page_image -%}
    <meta property="og:image" content="https:{{ page_image | image_url: width: 1200 }}">
    <meta property="og:image:width" content="1200">
  {%- endif -%}
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
</head>
```

## 2. Canonical URLs

- Always use `{{ canonical_url }}` — never hardcode
- Paginated pages: `?page=2` gets canonical back to page 1 by default
- **Gotcha:** Filtered collections (`/collections/all/tag`) should have `noindex` to avoid duplicate content
- Variant URLs: `?variant=123456` should canonical to the main product URL

## 3. Schema.org Structured Data

### Product
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "image": [
    {%- for image in product.images limit: 5 -%}
      {{ image | image_url: width: 1024 | prepend: 'https:' | json }}{% unless forloop.last %},{% endunless %}
    {%- endfor -%}
  ],
  "description": {{ product.description | strip_html | truncate: 5000 | json }},
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "brand": {
    "@type": "Brand",
    "name": {{ product.vendor | json }}
  },
  "offers": [
    {%- for variant in product.variants -%}
    {
      "@type": "Offer",
      "url": "{{ shop.url }}{{ variant.url }}",
      "priceCurrency": {{ cart.currency.iso_code | json }},
      "price": {{ variant.price | money_without_currency | json }},
      "availability": "https://schema.org/{% if variant.available %}InStock{% else %}OutOfStock{% endif %}",
      "sku": {{ variant.sku | json }},
      "name": {{ variant.title | json }}
    }{% unless forloop.last %},{% endunless %}
    {%- endfor -%}
  ]
  {%- if product.metafields.reviews.rating -%}
  ,"aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": {{ product.metafields.reviews.rating.value | json }},
    "reviewCount": {{ product.metafields.reviews.rating_count.value | json }}
  }
  {%- endif -%}
}
</script>
```

### BreadcrumbList
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": {{ 'general.breadcrumbs.home' | t | json }},
      "item": "{{ shop.url }}"
    }
    {%- if template.name == 'product' -%}
      {%- if collection -%}
      ,{
        "@type": "ListItem",
        "position": 2,
        "name": {{ collection.title | json }},
        "item": "{{ shop.url }}{{ collection.url }}"
      }
      ,{
        "@type": "ListItem",
        "position": 3,
        "name": {{ product.title | json }}
      }
      {%- else -%}
      ,{
        "@type": "ListItem",
        "position": 2,
        "name": {{ product.title | json }}
      }
      {%- endif -%}
    {%- elsif template.name == 'collection' -%}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": {{ collection.title | json }}
    }
    {%- endif -%}
  ]
}
</script>
```

### Organization
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": {{ shop.name | json }},
  "url": {{ shop.url | json }},
  "logo": {{ shop.brand.logo | image_url: width: 600 | prepend: 'https:' | json }},
  "sameAs": [
    {{ settings.social_facebook_link | json }},
    {{ settings.social_instagram_link | json }},
    {{ settings.social_twitter_link | json }}
  ]
}
</script>
```

## 4. Image SEO
- Always set `alt` text on images
- Use descriptive filenames before uploading
- Use `loading="lazy"` on below-fold images
- Use `fetchpriority="high"` on hero/LCP images
- Shopify CDN auto-converts to WebP when supported

## 5. URL Structure
- Keep URLs clean: `/products/product-name`, `/collections/collection-name`
- Use redirects for changed URLs: Admin > Online Store > Navigation > URL Redirects
- Avoid deep nesting: `/collections/category/products/product` is bad
- `{{ routes }}` object for safe URL references

## 6. Sitemap
- Shopify auto-generates sitemap.xml at `/sitemap.xml`
- Includes products, collections, pages, blogs
- **Cannot customize** — all published resources are included
- Submit to Google Search Console

## 7. Page Speed (SEO Factor)
- Minimize render-blocking JS/CSS
- Use `<link rel="preconnect" href="https://cdn.shopify.com">`
- Inline critical CSS for above-fold content
- Defer non-essential scripts
- Use `content_for_header` placement wisely (required but adds bloat)
