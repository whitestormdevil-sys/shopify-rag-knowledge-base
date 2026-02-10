"""
Shopify Theme Development Constraints & Knowledge Base

This is THE comprehensive reference that gets injected into every generation prompt.
Derived from 48,130 indexed chunks, Dawn source analysis, and Shopify official docs.

Every rule here prevents a real bug. Nothing is theoretical.
"""

# =============================================================================
# LIQUID SYNTAX RULES
# =============================================================================

LIQUID_SYNTAX = """
<liquid_syntax>
  Shopify uses Liquid, a template language. Three tag types:
  
  OUTPUT:     {{ variable }}              → renders value
  LOGIC:      {% if condition %}...{% endif %}  → control flow
  WHITESPACE: {%- tag -%}                → strips whitespace (use liberally)

  COMMON OBJECTS (available in sections):
  - section          → current section (section.id, section.settings, section.blocks)
  - block            → current block inside {% for block in section.blocks %}
  - settings         → global theme settings from settings_schema.json
  - shop             → store info (shop.name, shop.url, shop.currency)
  - product          → on product pages (product.title, .price, .images, .variants)
  - collection       → on collection pages (collection.title, .products, .products_count)
  - cart             → cart object (cart.items, cart.total_price, cart.item_count)
  - customer         → logged-in customer (customer.first_name, customer.email)
  - request          → request info (request.locale, request.page_type)
  - routes           → URL routes (routes.cart_url, routes.account_url)
  - content_for_header → REQUIRED in layout, loads Shopify scripts
  - content_for_layout → REQUIRED in layout, renders page content
  - page_title       → current page title
  - canonical_url    → canonical URL for SEO

  COMMON FILTERS:
  - | money                → format as currency ($10.00)
  - | money_with_currency  → format with code ($10.00 USD)
  - | image_url: width: N  → responsive image URL
  - | image_tag            → generate <img> tag with srcset
  - | asset_url            → URL to theme asset
  - | stylesheet_tag       → wrap in <link rel="stylesheet">
  - | script_tag           → wrap in <script>
  - | t                    → translation lookup
  - | escape               → HTML escape
  - | url_encode           → URL encode
  - | default: value       → fallback value
  - | append: str          → append string
  - | prepend: str         → prepend string
  - | replace: old, new    → string replace
  - | strip_html           → remove HTML tags
  - | truncate: N          → truncate to N chars
  - | split: ','           → split string to array
  - | first / last         → array first/last
  - | size                 → array/string length
  - | sort                 → sort array
  - | where: 'key', 'val'  → filter array
  - | map: 'key'           → extract property from array
  - | times: N             → multiply
  - | divided_by: N        → divide
  - | round: N             → round to N decimals
  - | at_least: N          → minimum value
  - | at_most: N           → maximum value
  - | json                 → JSON encode (for JS interop)
  - | handle               → convert to handle format
  - | handleize            → same as handle

  CONTROL FLOW:
  - {% if %} / {% elsif %} / {% else %} / {% endif %}
  - {% unless condition %} / {% endunless %}  (inverse if)
  - {% case variable %} {% when value %} {% endcase %}
  - {% for item in array %} / {% endfor %}
    - forloop.index (1-based), forloop.index0 (0-based)
    - forloop.first, forloop.last, forloop.length
    - {% for item in array limit:4 offset:2 %}
    - {% break %}, {% continue %}
  - {% assign var = value %}
  - {% capture var %}...{% endcapture %}
  - {% liquid
      assign x = 1
      if x == 1
        echo 'one'
      endif
    %}  (multi-line liquid tag, NO braces inside)

  SECTION/SNIPPET RENDERING:
  - {% render 'snippet-name' %}                     → render snippet (isolated scope)
  - {% render 'snippet-name', product: product %}    → pass variables explicitly
  - {% render 'snippet-name' for array as item %}    → render for each item
  - {% section 'section-name' %}                     → render static section (in layouts only)
  - {% sections 'section-group-name' %}              → render section group (header/footer)
  - NEVER use {% include %} — it's deprecated

  CRITICAL RULES:
  - {% schema %} MUST be the last Liquid tag in a section file
  - Variables from {% render %} are isolated — must pass them explicitly
  - Liquid is NOT JavaScript — no ternary, no arrow functions, no template literals
  - Use {% liquid %} tag for complex logic (cleaner than many {% %} tags)
  - String comparison is case-sensitive
  - nil/null checks: {% if variable %} (falsy: nil, false, empty string, empty array)
  - blank check: {% if variable == blank %} (catches nil AND empty)
</liquid_syntax>
"""

# =============================================================================
# SECTION SCHEMA SPECIFICATION
# =============================================================================

SCHEMA_SPECIFICATION = """
<schema_specification>
  Every section MUST end with a {% schema %} tag containing valid JSON.
  One syntax error in schema JSON breaks the ENTIRE section.

  FULL SCHEMA STRUCTURE:
  {
    "name": "Section Display Name",          // REQUIRED - shown in theme editor
    "tag": "section",                         // HTML tag wrapper (section, div, aside, etc.)
    "class": "css-class-name",               // CSS class on wrapper element
    "limit": 1,                               // Max instances per page (optional)
    "disabled_on": {                          // Where section CAN'T be added
      "groups": ["header", "footer"]          // Options: header, footer, aside, custom.overlay
    },
    "enabled_on": {                           // Where section CAN be added (use one or the other)
      "templates": ["product", "collection"], // Specific templates
      "groups": ["header"]                    // Or groups
    },
    "settings": [                             // Section-level settings
      // ... setting objects
    ],
    "blocks": [                               // Repeatable content blocks
      {
        "type": "block_type_handle",          // Unique within section
        "name": "Block Display Name",
        "limit": 3,                           // Max instances of this block type
        "settings": [
          // ... setting objects
        ]
      }
    ],
    "max_blocks": 16,                         // Total max blocks across all types
    "presets": [                              // REQUIRED for "Add section" in editor
      {
        "name": "Preset Display Name",
        "settings": {},                       // Default setting values
        "blocks": [                           // Default blocks
          { "type": "block_type_handle" }
        ]
      }
    ]
  }

  SETTING TYPES (all require id, type, label):
  
  Input types:
  - text          → single line text input
  - textarea      → multi-line text input  
  - richtext      → rich text editor (returns HTML)
  - inline_richtext → inline rich text (bold/italic only, no block elements)
  - number        → number input
  - range         → slider (requires min, max, step, unit)
  - checkbox      → boolean toggle
  - select        → dropdown (requires options: [{value, label}])
  - radio         → radio buttons (requires options: [{value, label}])

  Resource pickers:
  - image_picker  → image upload/selection
  - video         → Shopify-hosted video
  - video_url     → YouTube/Vimeo URL (accepts: ["youtube", "vimeo"])
  - url           → URL picker
  - link_list     → navigation menu picker
  - page          → page picker
  - blog          → blog picker
  - collection    → collection picker
  - product       → product picker
  - product_list  → multiple product picker
  - collection_list → multiple collection picker

  Design types:
  - color          → color picker (hex)
  - color_scheme   → color scheme selector (scheme-1, scheme-2, etc.)
  - color_background → gradient-capable color picker
  - font_picker    → font selector

  Informational (no value, just labels):
  - header         → section divider in editor (uses "content" not "label")
  - paragraph      → help text in editor (uses "content" not "label")
  - liquid         → custom Liquid in editor

  SETTING OBJECT FORMAT:
  {
    "type": "text",
    "id": "unique_setting_id",        // MUST be unique within section/block
    "label": "Human Readable Label",  // Or "t:key" for translations
    "default": "default value",       // Optional but recommended
    "info": "Help text shown below",  // Optional
    "placeholder": "Placeholder..."   // For text inputs
  }

  RANGE SPECIFIC:
  {
    "type": "range",
    "id": "columns",
    "min": 1,
    "max": 6,
    "step": 1,
    "unit": "col",
    "label": "Number of columns",
    "default": 3
  }

  SELECT SPECIFIC:
  {
    "type": "select",
    "id": "layout",
    "options": [
      { "value": "grid", "label": "Grid" },
      { "value": "list", "label": "List" }
    ],
    "default": "grid",
    "label": "Layout style"
  }
</schema_specification>
"""

# =============================================================================
# OS 2.0 ARCHITECTURE
# =============================================================================

OS2_ARCHITECTURE = """
<os2_architecture>
  Shopify OS 2.0 uses JSON templates that reference sections.

  FILE STRUCTURE:
  layout/
    theme.liquid              → Master layout (ONE per theme, wraps everything)
  templates/
    index.json                → Homepage
    product.json              → Product pages
    collection.json           → Collection pages
    cart.json                 → Cart page
    page.json                 → Generic pages
    page.contact.json         → Contact page (alternate template)
    blog.json                 → Blog listing
    article.json              → Blog post
    search.json               → Search results
    404.json                  → Not found
    list-collections.json     → All collections
    customers/account.json    → Customer account
    customers/login.json      → Login page
    password.json             → Password page
  sections/
    *.liquid                  → Section files (reusable UI blocks)
  snippets/
    *.liquid                  → Code fragments (rendered via {% render %})
  assets/
    *.css, *.js, *.svg        → Static assets
  config/
    settings_schema.json      → Theme-level settings definition
    settings_data.json        → Saved setting values
  locales/
    en.default.json           → Translations

  JSON TEMPLATE FORMAT:
  {
    "sections": {
      "unique_key": {                    // Unique key for this instance
        "type": "section-file-name",     // Maps to sections/section-file-name.liquid
        "settings": {                    // Override default settings
          "setting_id": "value"
        },
        "blocks": {                      // Block instances
          "block_key": {
            "type": "block_type",
            "settings": { ... }
          }
        },
        "block_order": ["block_key"]     // Block display order
      }
    },
    "order": ["unique_key_1", "unique_key_2"]   // Section display order
  }

  KEY RULES:
  - Section keys in JSON must be unique per template
  - Section "type" must match a file in sections/ (without .liquid)
  - Block "type" must match a block type defined in the section's schema
  - block_order array controls block rendering order
  - order array controls section rendering order on the page
  - Sections with presets can be added/removed by merchants in theme editor
  - Sections without presets are "static" (only usable when hardcoded in templates)
  - main-* sections (main-product, main-cart-items) are typically unique per template
</os2_architecture>
"""

# =============================================================================
# DAWN THEME PATTERNS
# =============================================================================

DAWN_PATTERNS = """
<dawn_patterns>
  Generated sections MUST follow Dawn's established patterns to ensure compatibility.

  CSS LOADING (top of section file):
    {{ 'section-name.css' | asset_url | stylesheet_tag }}
    {{ 'component-card.css' | asset_url | stylesheet_tag }}

  SECTION PADDING (standard pattern used in ALL Dawn sections):
    {%- style -%}
      .section-{{ section.id }}-padding {
        padding-top: {{ section.settings.padding_top | times: 0.75 | round: 0 }}px;
        padding-bottom: {{ section.settings.padding_bottom | times: 0.75 | round: 0 }}px;
      }
      @media screen and (min-width: 750px) {
        .section-{{ section.id }}-padding {
          padding-top: {{ section.settings.padding_top }}px;
          padding-bottom: {{ section.settings.padding_bottom }}px;
        }
      }
    {%- endstyle -%}

  ALWAYS include padding_top and padding_bottom settings:
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_top",
      "default": 36
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_bottom",
      "default": 36
    }

  COLOR SCHEME:
    HTML: <div class="color-{{ section.settings.color_scheme }} gradient">
    Setting: { "type": "color_scheme", "id": "color_scheme", "default": "scheme-1" }

  PAGE WIDTH:
    Full width:  <div class="page-width">
    Break out:   <div class="page-width page-width--full-width">

  RESPONSIVE IMAGES:
    {{ image | image_url: width: 1500 | image_tag:
      loading: 'lazy',
      sizes: sizes_value,
      widths: '375, 550, 750, 1100, 1500',
      class: 'image-class'
    }}
    - First visible image: loading: 'eager', fetchpriority: 'high'
    - Below fold images: loading: 'lazy' (DEFAULT)
    - Always provide widths and sizes for srcset

  HEADING SIZES (Dawn's scale):
    Classes: h0 (largest), h1, h2, h3 (smallest in headings)
    Setting: { "type": "select", "id": "heading_size", 
               "options": [{"value":"h2","label":"Small"},{"value":"h1","label":"Medium"},{"value":"h0","label":"Large"}],
               "default": "h1" }

  BLOCK ITERATION:
    {%- for block in section.blocks -%}
      {%- case block.type -%}
        {%- when 'heading' -%}
          <h2 class="{{ block.settings.heading_size }}" {{ block.shopify_attributes }}>
            {{ block.settings.heading }}
          </h2>
        {%- when 'text' -%}
          <div class="rte">{{ block.settings.text }}</div>
        {%- when 'button' -%}
          {%- if block.settings.button_label != blank -%}
            <a href="{{ block.settings.button_link }}" class="button">
              {{ block.settings.button_label | escape }}
            </a>
          {%- endif -%}
      {%- endcase -%}
    {%- endfor -%}

  IMPORTANT: Always add {{ block.shopify_attributes }} to block wrappers.
  This enables theme editor selection/highlighting.

  ANIMATION SUPPORT:
    {% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}

  SECTION ID SCOPING:
    Always scope dynamic styles with section.id:
    #Section-{{ section.id }} { ... }
    .section-{{ section.id }}-padding { ... }

  ACCESSIBILITY:
    - All images need alt text: alt="{{ image.alt | escape }}"
    - Interactive elements need aria-labels
    - Use <h2> not <div> for headings
    - Focus states: :focus-visible with --focused-base-outline
    - Screen reader text: <span class="visually-hidden">{{ text }}</span>
    - Skip links for keyboard navigation
    - Use semantic HTML (nav, main, article, aside, footer)

  DAWN BREAKPOINTS:
    - Mobile: < 750px
    - Tablet: 750px - 989px  
    - Desktop: >= 990px
    - Wide: >= 1400px
    Mobile-first: base styles are mobile, use min-width media queries

  DAWN SECTION CATEGORIES:
    Hero/Banner:    image-banner, slideshow, video, image-with-text
    Product:        main-product, featured-product, related-products
    Collection:     main-collection-product-grid, featured-collection, collection-list
    Content:        rich-text, multicolumn, multirow, collapsible-content, collage
    Marketing:      newsletter, email-signup-banner, announcement-bar
    Navigation:     header, footer
    Cart:           main-cart-items, main-cart-footer, cart-drawer
    Blog:           featured-blog, main-blog, main-article
    Utility:        custom.liquid, apps, contact-form, page
</dawn_patterns>
"""

# =============================================================================
# PERFORMANCE RULES
# =============================================================================

PERFORMANCE_RULES = """
<performance_rules>
  Shopify measures Core Web Vitals. Generated themes must be fast.

  CRITICAL:
  - NO inline <style> blocks for static CSS — use asset files
  - {%- style -%} is OK for dynamic CSS (uses section.id, settings values)
  - Defer all JavaScript: <script src="{{ 'file.js' | asset_url }}" defer></script>
  - Lazy load all below-fold images: loading="lazy"
  - First visible image (hero): loading="eager", fetchpriority="high"
  - Use responsive images with srcset (widths + sizes attributes)
  - Minimize DOM depth — avoid unnecessary wrapper divs
  - Use CSS for animations, NOT JavaScript
  - NO jQuery — vanilla JS custom elements only
  - NO external CDN resources (Google Fonts via font_picker setting instead)
  - Keep JavaScript minimal — most Shopify themes need very little JS
  - Avoid document.querySelectorAll in loops — cache references
  - Use IntersectionObserver for scroll-triggered behavior

  CSS BEST PRACTICES:
  - Use CSS custom properties (variables) for theming
  - Use CSS Grid and Flexbox for layout — no floats
  - Use logical properties (margin-inline, padding-block) where possible
  - Minimize specificity — avoid !important
  - Use content-visibility: auto for off-screen sections

  JS PATTERN (Dawn custom elements):
  class MySection extends HTMLElement {
    constructor() {
      super();
      // Setup
    }
    connectedCallback() {
      // When element enters DOM
    }
    disconnectedCallback() {
      // Cleanup
    }
  }
  customElements.define('my-section', MySection);

  ASSET SIZE TARGETS:
  - Section CSS: < 10KB per file
  - Section JS: < 5KB per file (most sections need zero JS)
  - Total theme CSS: < 100KB
  - Total theme JS: < 50KB
</performance_rules>
"""

# =============================================================================
# ACCESSIBILITY RULES
# =============================================================================

ACCESSIBILITY_RULES = """
<accessibility_rules>
  Shopify Theme Store REQUIRES WCAG 2.1 AA compliance.

  MANDATORY:
  - All images: alt="{{ image.alt | escape }}" (always escape user content)
  - Decorative images: alt="" (empty alt, NOT missing alt)
  - All form inputs: associated <label> elements
  - All buttons: visible text or aria-label
  - All links: descriptive text (never "click here")
  - Color contrast: 4.5:1 for text, 3:1 for large text
  - Focus indicators: visible on all interactive elements
  - Keyboard navigable: all interactive elements reachable via Tab
  - Skip to content link: first focusable element
  - Heading hierarchy: h1 → h2 → h3 (no skipping levels per section)
  - Language attribute: <html lang="{{ request.locale.iso_code }}">
  - ARIA landmarks: nav, main, footer, aside
  - Live regions: aria-live="polite" for dynamic content updates (cart count, etc.)

  FOCUS STYLE (Dawn pattern):
  :focus-visible {
    outline: var(--focused-base-outline);
    outline-offset: var(--focused-base-outline-offset);
    box-shadow: var(--focused-base-box-shadow);
  }

  SCREEN READER:
  <span class="visually-hidden">{{ descriptive_text }}</span>
  .visually-hidden {
    position: absolute !important;
    width: 1px; height: 1px;
    padding: 0; margin: -1px;
    overflow: hidden; clip: rect(0,0,0,0);
    white-space: nowrap; border: 0;
  }

  MOTION:
  @media (prefers-reduced-motion: reduce) {
    * { animation-duration: 0s !important; transition-duration: 0s !important; }
  }
</accessibility_rules>
"""

# =============================================================================
# ASSET HANDLING
# =============================================================================

ASSET_HANDLING = """
<asset_handling>
  LOADING CSS IN SECTIONS:
    {{ 'section-name.css' | asset_url | stylesheet_tag }}
    {{ 'component-card.css' | asset_url | stylesheet_tag }}
  
  LOADING JS IN SECTIONS:
    <script src="{{ 'section-name.js' | asset_url }}" defer="defer"></script>

  DYNAMIC CSS (using Liquid values — OK to inline):
    {%- style -%}
      .section-{{ section.id }}-padding { padding-top: {{ section.settings.padding_top }}px; }
    {%- endstyle -%}

  IMAGES:
    Responsive: {{ image | image_url: width: 1500 | image_tag: loading: 'lazy', sizes: sizes }}
    Direct URL: {{ image | image_url: width: 800 }}
    SVG icons:  {% render 'icon-name' %}

  FILE NAMING:
    CSS: section-{name}.css or component-{name}.css
    JS:  {name}.js
    Sections: {name}.liquid (lowercase, hyphens)
    Snippets: {name}.liquid (lowercase, hyphens)
  
  GENERATED ASSETS:
    When creating a new section called "hero-banner":
    → sections/hero-banner.liquid    (Liquid template)
    → assets/section-hero-banner.css (CSS, if needed)
    → assets/hero-banner.js          (JS, only if interactive)
</asset_handling>
"""

# =============================================================================
# COMBINED CONSTRAINTS
# =============================================================================

def get_all_constraints() -> str:
    """Return ALL Shopify constraints as a single string for prompt injection."""
    return "\n".join([
        LIQUID_SYNTAX,
        SCHEMA_SPECIFICATION,
        OS2_ARCHITECTURE,
        DAWN_PATTERNS,
        PERFORMANCE_RULES,
        ACCESSIBILITY_RULES,
        ASSET_HANDLING,
    ])


def get_constraints_for_stage(stage: str) -> str:
    """Return stage-specific constraints to reduce token usage.
    
    Stages: intent_parser, section_planner, section_generator, 
            section_verifier, iteration_handler
    """
    if stage == "intent_parser":
        # Intent parser just needs to know what's possible
        return OS2_ARCHITECTURE + DAWN_PATTERNS
    
    elif stage == "section_planner":
        # Planner needs architecture + Dawn catalog
        return OS2_ARCHITECTURE + DAWN_PATTERNS
    
    elif stage == "section_generator":
        # Generator needs EVERYTHING
        return get_all_constraints()
    
    elif stage == "section_verifier":
        # Verifier needs syntax rules + schema spec
        return LIQUID_SYNTAX + SCHEMA_SPECIFICATION + PERFORMANCE_RULES + ACCESSIBILITY_RULES
    
    elif stage == "iteration_handler":
        # Iteration needs patterns + syntax for targeted edits
        return LIQUID_SYNTAX + DAWN_PATTERNS + ASSET_HANDLING
    
    else:
        return get_all_constraints()
