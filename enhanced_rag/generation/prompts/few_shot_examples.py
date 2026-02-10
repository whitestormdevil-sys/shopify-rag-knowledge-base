"""
Few-Shot Golden Reference Sections for the Builder Prompt.

These are 2 complete, production-quality Shopify sections that demonstrate
EXACTLY the output format and code quality the Builder should produce.

Section 1: Hero Banner — fixed-layout section (no blocks)
Section 2: Features Grid — block-based section

Both use the ShopifyAI design token system (--sai-* variables) and follow
Dawn's patterns for maximum compatibility.

These get injected into the Builder's system prompt so the model learns
the pattern through examples, not just instructions.
"""

# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: HERO BANNER
# Demonstrates: images, overlay, settings, responsive, no blocks
# ═══════════════════════════════════════════════════════════════════════════

EXAMPLE_1_INPUT = """{
  "id": "hero-banner",
  "name": "Hero Banner",
  "type": "hero",
  "similar_to": "image-banner",
  "action": "create_custom",
  "special_features": ["background_image", "overlay_text", "cta_button"],
  "blocks_needed": [],
  "description": "Full-width hero with background image, overlay heading, subheading, and CTA button"
}"""

EXAMPLE_1_OUTPUT = """<shopifyTheme>
<themeFile path="sections/hero-banner.liquid">
{%- style -%}
  .section-{{ section.id }}-padding {
    padding-top: calc(var(--sai-section-vertical) * 0.75);
    padding-bottom: calc(var(--sai-section-vertical) * 0.75);
  }
  @media screen and (min-width: 750px) {
    .section-{{ section.id }}-padding {
      padding-top: var(--sai-section-vertical);
      padding-bottom: var(--sai-section-vertical);
    }
  }
{%- endstyle -%}

<div class="hero-banner hero-banner--{{ section.settings.height }}">
  {%- if section.settings.image != blank -%}
    <div class="hero-banner__media">
      {{
        section.settings.image
        | image_url: width: 1920
        | image_tag:
          loading: 'lazy',
          sizes: '100vw',
          widths: '375, 550, 750, 1100, 1500, 1920',
          class: 'hero-banner__image',
          alt: section.settings.image.alt | default: section.settings.heading
      }}
    </div>
  {%- else -%}
    <div class="hero-banner__media hero-banner__media--placeholder">
      {{ 'hero-apparel-1' | placeholder_svg_tag: 'hero-banner__placeholder' }}
    </div>
  {%- endif -%}

  <div class="hero-banner__overlay" style="--overlay-opacity: {{ section.settings.overlay_opacity | divided_by: 100.0 }};"></div>

  <div class="hero-banner__content section-{{ section.id }}-padding page-width">
    <div class="hero-banner__text hero-banner__text--{{ section.settings.text_alignment }}">
      {%- if section.settings.subheading != blank -%}
        <p class="hero-banner__subheading">
          {{- section.settings.subheading | escape -}}
        </p>
      {%- endif -%}

      {%- if section.settings.heading != blank -%}
        <h2 class="hero-banner__heading">
          {{- section.settings.heading -}}
        </h2>
      {%- endif -%}

      {%- if section.settings.description != blank -%}
        <div class="hero-banner__description">
          {{- section.settings.description -}}
        </div>
      {%- endif -%}

      {%- if section.settings.button_label != blank -%}
        <a
          href="{{ section.settings.button_link }}"
          class="hero-banner__button button"
          {% if section.settings.button_link == blank %}
            role="link" aria-disabled="true"
          {% endif %}
        >
          {{- section.settings.button_label | escape -}}
        </a>
      {%- endif -%}
    </div>
  </div>
</div>

{% schema %}
{
  "name": "Hero Banner",
  "tag": "section",
  "class": "section",
  "settings": [
    {
      "type": "image_picker",
      "id": "image",
      "label": "Background image"
    },
    {
      "type": "select",
      "id": "height",
      "label": "Section height",
      "default": "large",
      "options": [
        { "value": "small", "label": "Small" },
        { "value": "medium", "label": "Medium" },
        { "value": "large", "label": "Large" },
        { "value": "full", "label": "Full screen" }
      ]
    },
    {
      "type": "range",
      "id": "overlay_opacity",
      "label": "Overlay opacity",
      "min": 0,
      "max": 100,
      "step": 5,
      "default": 40,
      "unit": "%"
    },
    {
      "type": "text",
      "id": "subheading",
      "label": "Subheading",
      "default": "Welcome to our store"
    },
    {
      "type": "inline_richtext",
      "id": "heading",
      "label": "Heading",
      "default": "Elevate Your <em>Style</em>"
    },
    {
      "type": "richtext",
      "id": "description",
      "label": "Description",
      "default": "<p>Discover our curated collection of premium products designed for the modern lifestyle.</p>"
    },
    {
      "type": "text",
      "id": "button_label",
      "label": "Button label",
      "default": "Shop Now"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Button link"
    },
    {
      "type": "select",
      "id": "text_alignment",
      "label": "Text alignment",
      "default": "center",
      "options": [
        { "value": "left", "label": "Left" },
        { "value": "center", "label": "Center" },
        { "value": "right", "label": "Right" }
      ]
    }
  ],
  "presets": [
    {
      "name": "Hero Banner"
    }
  ]
}
{% endschema %}
</themeFile>
<themeFile path="assets/section-hero-banner.css">
/* ==========================================================================
   Hero Banner Section
   ========================================================================== */

.hero-banner {
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-banner--small { min-height: 300px; }
.hero-banner--medium { min-height: 450px; }
.hero-banner--large { min-height: 600px; }
.hero-banner--full { min-height: 100vh; }

@media screen and (max-width: 749px) {
  .hero-banner--small { min-height: 200px; }
  .hero-banner--medium { min-height: 350px; }
  .hero-banner--large { min-height: 450px; }
  .hero-banner--full { min-height: 100svh; }
}

/* ── Media ── */

.hero-banner__media {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-banner__image,
.hero-banner__placeholder {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-banner__media--placeholder {
  background-color: var(--sai-color-surface-alt);
}

.hero-banner__placeholder {
  fill: var(--sai-color-border);
}

/* ── Overlay ── */

.hero-banner__overlay {
  position: absolute;
  inset: 0;
  z-index: 1;
  background-color: rgba(0, 0, 0, var(--overlay-opacity, 0.4));
}

/* ── Content ── */

.hero-banner__content {
  position: relative;
  z-index: 2;
  width: 100%;
}

.hero-banner__text {
  max-width: 650px;
  display: flex;
  flex-direction: column;
  gap: var(--sai-element-gap);
}

.hero-banner__text--center {
  margin-inline: auto;
  text-align: center;
  align-items: center;
}

.hero-banner__text--right {
  margin-left: auto;
  text-align: right;
  align-items: flex-end;
}

/* ── Typography ── */

.hero-banner__subheading {
  font-size: var(--sai-small-size);
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sai-color-accent);
  margin: 0;
}

.hero-banner__heading {
  font-family: var(--sai-font-heading);
  font-weight: var(--sai-font-heading-weight);
  font-size: var(--sai-h1-size);
  line-height: var(--sai-line-height-heading);
  letter-spacing: var(--sai-letter-spacing-heading);
  color: #ffffff;
  margin: 0;
}

.hero-banner__description {
  font-size: var(--sai-body-size);
  line-height: var(--sai-line-height-body);
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
}

.hero-banner__description p { margin: 0; }

/* ── Button ── */

.hero-banner__button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 32px;
  font-size: var(--sai-body-size);
  font-weight: 600;
  color: var(--sai-color-accent-contrast);
  background-color: var(--sai-color-accent);
  border: none;
  border-radius: var(--sai-radius-md);
  text-decoration: none;
  cursor: pointer;
  transition: opacity var(--sai-transition-fast);
  margin-top: 8px;
}

.hero-banner__button:hover {
  opacity: 0.85;
}

.hero-banner__button[aria-disabled="true"] {
  pointer-events: none;
  opacity: 0.6;
}
</themeFile>
</shopifyTheme>"""


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: FEATURES GRID (Block-based)
# Demonstrates: blocks, grid layout, forloop, shopify_attributes
# ═══════════════════════════════════════════════════════════════════════════

EXAMPLE_2_INPUT = """{
  "id": "features-grid",
  "name": "Features Grid",
  "type": "features",
  "similar_to": "multicolumn",
  "action": "create_custom",
  "special_features": ["icon_blocks", "responsive_grid", "hover_animation"],
  "blocks_needed": [
    { "type": "feature", "settings": ["icon", "heading", "text", "link"] }
  ],
  "description": "Grid of feature cards with icons, headings, text, and optional links"
}"""

EXAMPLE_2_OUTPUT = """<shopifyTheme>
<themeFile path="sections/features-grid.liquid">
{{ 'section-features-grid.css' | asset_url | stylesheet_tag }}

{%- style -%}
  .section-{{ section.id }}-padding {
    padding-top: calc(var(--sai-section-vertical) * 0.75);
    padding-bottom: calc(var(--sai-section-vertical) * 0.75);
  }
  @media screen and (min-width: 750px) {
    .section-{{ section.id }}-padding {
      padding-top: var(--sai-section-vertical);
      padding-bottom: var(--sai-section-vertical);
    }
  }
{%- endstyle -%}

<div class="features-grid section-{{ section.id }}-padding">
  <div class="page-width">
    {%- if section.settings.heading != blank -%}
      <div class="features-grid__header">
        <h2 class="features-grid__heading">
          {{- section.settings.heading -}}
        </h2>
        {%- if section.settings.description != blank -%}
          <div class="features-grid__description">
            {{- section.settings.description -}}
          </div>
        {%- endif -%}
      </div>
    {%- endif -%}

    {%- if section.blocks.size > 0 -%}
      <div
        class="features-grid__grid"
        style="--grid-columns: {{ section.settings.columns }};"
      >
        {%- for block in section.blocks -%}
          <div
            class="features-grid__card"
            {{ block.shopify_attributes }}
            style="--animation-order: {{ forloop.index }};"
          >
            {%- if block.settings.icon != 'none' -%}
              <div class="features-grid__icon-wrapper">
                {% render 'icon', icon: block.settings.icon %}
              </div>
            {%- elsif block.settings.custom_image != blank -%}
              <div class="features-grid__icon-wrapper">
                {{
                  block.settings.custom_image
                  | image_url: width: 96
                  | image_tag:
                    loading: 'lazy',
                    width: 48,
                    height: 48,
                    class: 'features-grid__custom-icon',
                    alt: block.settings.heading
                }}
              </div>
            {%- endif -%}

            {%- if block.settings.heading != blank -%}
              <h3 class="features-grid__card-heading">
                {{- block.settings.heading | escape -}}
              </h3>
            {%- endif -%}

            {%- if block.settings.text != blank -%}
              <p class="features-grid__card-text">
                {{- block.settings.text | escape -}}
              </p>
            {%- endif -%}

            {%- if block.settings.link_label != blank -%}
              <a
                href="{{ block.settings.link_url }}"
                class="features-grid__card-link"
              >
                {{- block.settings.link_label | escape -}}
                <span aria-hidden="true">&rarr;</span>
              </a>
            {%- endif -%}
          </div>
        {%- endfor -%}
      </div>
    {%- else -%}
      {%- if request.design_mode -%}
        <p class="features-grid__empty">Add feature blocks in the theme editor.</p>
      {%- endif -%}
    {%- endif -%}
  </div>
</div>

{% schema %}
{
  "name": "Features Grid",
  "tag": "section",
  "class": "section",
  "settings": [
    {
      "type": "inline_richtext",
      "id": "heading",
      "label": "Heading",
      "default": "Why Choose <em>Us</em>"
    },
    {
      "type": "richtext",
      "id": "description",
      "label": "Description",
      "default": "<p>Everything you need, nothing you don't.</p>"
    },
    {
      "type": "range",
      "id": "columns",
      "label": "Columns on desktop",
      "min": 2,
      "max": 4,
      "step": 1,
      "default": 3
    }
  ],
  "blocks": [
    {
      "type": "feature",
      "name": "Feature",
      "limit": 8,
      "settings": [
        {
          "type": "select",
          "id": "icon",
          "label": "Icon",
          "default": "star",
          "options": [
            { "value": "none", "label": "None" },
            { "value": "star", "label": "Star" },
            { "value": "shield", "label": "Shield" },
            { "value": "truck", "label": "Shipping" },
            { "value": "heart", "label": "Heart" },
            { "value": "clock", "label": "Clock" },
            { "value": "refresh", "label": "Refresh" },
            { "value": "chat", "label": "Chat" },
            { "value": "check", "label": "Checkmark" }
          ]
        },
        {
          "type": "image_picker",
          "id": "custom_image",
          "label": "Custom icon image",
          "info": "Used when Icon is set to None. 96×96px recommended."
        },
        {
          "type": "text",
          "id": "heading",
          "label": "Heading",
          "default": "Feature heading"
        },
        {
          "type": "textarea",
          "id": "text",
          "label": "Description",
          "default": "Pair text with an icon to focus on your chosen product, collection, or blog post."
        },
        {
          "type": "text",
          "id": "link_label",
          "label": "Link label"
        },
        {
          "type": "url",
          "id": "link_url",
          "label": "Link URL"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Features Grid",
      "blocks": [
        { "type": "feature", "settings": { "icon": "truck", "heading": "Free Shipping", "text": "On all orders over $50. Fast, reliable delivery to your door." } },
        { "type": "feature", "settings": { "icon": "shield", "heading": "Secure Payment", "text": "Your transactions are protected with industry-standard encryption." } },
        { "type": "feature", "settings": { "icon": "refresh", "heading": "Easy Returns", "text": "30-day hassle-free return policy. No questions asked." } }
      ]
    }
  ]
}
{% endschema %}
</themeFile>
<themeFile path="assets/section-features-grid.css">
/* ==========================================================================
   Features Grid Section
   ========================================================================== */

.features-grid__header {
  text-align: center;
  max-width: 650px;
  margin-inline: auto;
  margin-bottom: calc(var(--sai-inner-padding) * 2);
}

.features-grid__heading {
  font-family: var(--sai-font-heading);
  font-weight: var(--sai-font-heading-weight);
  font-size: var(--sai-h2-size);
  line-height: var(--sai-line-height-heading);
  letter-spacing: var(--sai-letter-spacing-heading);
  color: rgb(var(--color-foreground));
  margin: 0 0 var(--sai-element-gap);
}

.features-grid__description {
  font-size: var(--sai-body-size);
  line-height: var(--sai-line-height-body);
  color: rgba(var(--color-foreground), 0.7);
}

.features-grid__description p { margin: 0; }

/* ── Grid ── */

.features-grid__grid {
  display: grid;
  grid-template-columns: repeat(var(--grid-columns, 3), 1fr);
  gap: var(--sai-grid-gap);
}

@media screen and (max-width: 989px) and (min-width: 750px) {
  .features-grid__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 749px) {
  .features-grid__grid {
    grid-template-columns: 1fr;
  }
}

/* ── Cards ── */

.features-grid__card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: var(--sai-inner-padding);
  background-color: var(--sai-color-surface);
  border: var(--sai-border-width) solid var(--sai-color-border);
  border-radius: var(--sai-radius-md);
  transition: box-shadow var(--sai-transition-normal), transform var(--sai-transition-normal);
}

.features-grid__card:hover {
  box-shadow: var(--sai-shadow-md);
  transform: translateY(-2px);
}

/* ── Icon ── */

.features-grid__icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  margin-bottom: var(--sai-element-gap);
  color: var(--sai-color-accent);
}

.features-grid__icon-wrapper svg {
  width: 28px;
  height: 28px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.features-grid__custom-icon {
  width: 48px;
  height: 48px;
  object-fit: contain;
}

/* ── Text ── */

.features-grid__card-heading {
  font-family: var(--sai-font-heading);
  font-weight: var(--sai-font-heading-weight);
  font-size: var(--sai-h3-size);
  line-height: var(--sai-line-height-heading);
  color: rgb(var(--color-foreground));
  margin: 0 0 8px;
}

.features-grid__card-text {
  font-size: var(--sai-body-size);
  line-height: var(--sai-line-height-body);
  color: rgba(var(--color-foreground), 0.7);
  margin: 0;
  flex-grow: 1;
}

.features-grid__card-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: var(--sai-element-gap);
  font-size: var(--sai-small-size);
  font-weight: 600;
  color: var(--sai-color-accent);
  text-decoration: none;
  transition: gap var(--sai-transition-fast);
}

.features-grid__card-link:hover {
  gap: 8px;
}

/* ── Empty state ── */

.features-grid__empty {
  text-align: center;
  color: rgba(var(--color-foreground), 0.5);
  font-style: italic;
  padding: var(--sai-inner-padding);
}
</themeFile>
</shopifyTheme>"""


# ═══════════════════════════════════════════════════════════════════════════
# Prompt builder
# ═══════════════════════════════════════════════════════════════════════════

def get_few_shot_prompt() -> str:
    """Return the full few-shot examples block for the Builder system prompt.

    This is injected AFTER the main rules and BEFORE the output format reminder.
    Two examples cover the two most important patterns:
      1. Fixed-layout section (hero) — images, overlay, no blocks
      2. Block-based section (features) — blocks, grid, forloop, shopify_attributes
    """
    return f"""
<few_shot_examples>
Study these examples carefully. They show EXACTLY the output quality and patterns you must follow.

<example_1>
<input>
{EXAMPLE_1_INPUT}
</input>
<output>
{EXAMPLE_1_OUTPUT}
</output>
</example_1>

<example_2>
<input>
{EXAMPLE_2_INPUT}
</input>
<output>
{EXAMPLE_2_OUTPUT}
</output>
</example_2>

KEY PATTERNS FROM THESE EXAMPLES:
1. Section padding uses the standard pattern with section-{{ section.id }}-padding class
2. CSS loads via {{ 'section-name.css' | asset_url | stylesheet_tag }}
3. All CSS uses var(--sai-*) design tokens — NEVER hardcoded values
4. Block wrappers include {{ block.shopify_attributes }} for theme editor
5. Nil checks everywhere: {{% if section.settings.heading != blank %}}
6. BEM naming: .section-name__element--modifier
7. Schema has name, tag, class, settings, (blocks if needed), and presets
8. Responsive: @media max-width: 749px for mobile, 989px for tablet
9. Placeholder SVG for empty images: {{ 'placeholder-name' | placeholder_svg_tag }}
10. Links check blank: aria-disabled="true" when no URL
</few_shot_examples>
"""
