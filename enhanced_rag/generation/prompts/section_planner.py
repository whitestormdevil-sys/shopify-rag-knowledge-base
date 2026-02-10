"""
Stage 2: Section Planner

Takes parsed intent + Dawn section catalog and decides:
- Which Dawn sections to KEEP as-is (header, footer, cart, etc.)
- Which Dawn sections to MODIFY (change layout, add features)
- Which sections to CREATE from scratch (custom sections)
- Template JSON configurations
"""

from .constraints import get_constraints_for_stage


# Complete Dawn section catalog with descriptions
DAWN_SECTION_CATALOG = """
<dawn_sections>
  AVAILABLE DAWN SECTIONS (already exist — can be kept or modified):

  HERO/BANNER:
  - image-banner        → Full-width image with text overlay, CTA buttons, color overlay
  - slideshow           → Multiple slides with auto-play, text + buttons per slide
  - video               → Video section (Shopify-hosted or YouTube/Vimeo)
  - image-with-text     → Split layout: image on one side, text + CTA on other

  PRODUCT:
  - main-product        → Full product page (gallery, price, variants, add-to-cart, description)
  - featured-product    → Single product showcase on any page
  - related-products    → "You may also like" grid below product

  COLLECTION:
  - main-collection-product-grid → Collection page with filters, sorting, pagination
  - main-collection-banner       → Collection header image + title
  - featured-collection          → Product grid from one collection (homepage use)
  - collection-list              → Grid of collection cards with images

  CONTENT:
  - rich-text           → Text content block (heading, body, button)
  - multicolumn         → 2-6 column grid with icon/image + text per column
  - multirow            → Alternating image + text rows
  - collapsible-content → Accordion/FAQ style expandable content
  - collage             → Creative image collage layout
  - custom.liquid       → Raw Liquid code section (escape hatch)

  MARKETING:
  - newsletter          → Email signup form
  - email-signup-banner → Full-width email signup with image background
  - announcement-bar    → Top-of-page announcement strip

  NAVIGATION:
  - header              → Site header (logo, nav, search, cart icon)
  - footer              → Site footer (menus, social, payment icons, copyright)

  CART:
  - main-cart-items     → Cart page item list
  - main-cart-footer    → Cart totals, checkout button, notes
  - cart-drawer         → Slide-out cart sidebar

  BLOG:
  - featured-blog       → Blog post cards grid
  - main-blog           → Blog listing page
  - main-article        → Single blog post

  PAGES:
  - main-page           → Generic page content
  - page                → Page content section
  - contact-form        → Contact form section
  - apps                → App block container

  UTILITY:
  - main-404            → 404 error page
  - main-search         → Search results page
  - main-login          → Customer login
  - main-account        → Customer account
  - main-addresses      → Customer addresses
  - main-order          → Order details
  - main-register       → Registration
  - main-reset-password → Password reset
  - main-password-header/footer → Password page
  - main-list-collections → All collections page
</dawn_sections>
"""


SECTION_PLANNER_SYSTEM = """You are ShopifyAI Section Planner — stage 2 of the theme generation pipeline.

Your job: Given a parsed store intent, create a precise build plan that maps to Dawn's architecture.

{constraints}

{dawn_catalog}

OUTPUT FORMAT (JSON only):
{{
  "theme_name": "descriptive theme name",
  "homepage_plan": {{
    "sections_order": [
      {{
        "key": "unique_template_key",
        "action": "keep|modify|create",
        "dawn_section": "existing section name or null for create",
        "new_section_name": "name for created sections or null",
        "description": "what this section does on the page",
        "modifications": "what to change from Dawn default (if modify)",
        "settings_override": {{}}
      }}
    ]
  }},
  "product_page_plan": {{
    "sections_order": [...]
  }},
  "collection_page_plan": {{
    "sections_order": [...]
  }},
  "other_pages": {{
    "cart": {{"action": "keep_default"}},
    "blog": {{"action": "keep_default|customize"}},
    "page.about": {{"sections_order": [...]}},
    "page.contact": {{"sections_order": [...]}},
    "page.faq": {{"sections_order": [...]}}
  }},
  "navigation": {{
    "header_style": "simple|mega_menu|drawer",
    "footer_columns": 3|4,
    "announcement_bar": true|false,
    "announcement_text": "text or null"
  }},
  "custom_sections_needed": [
    {{
      "name": "section-file-name",
      "display_name": "Section Display Name",
      "description": "detailed description of what to build",
      "blocks": ["block types needed"],
      "settings_needed": ["list of settings"],
      "needs_css": true|false,
      "needs_js": true|false,
      "similar_to": "closest Dawn section for reference"
    }}
  ],
  "snippets_needed": [
    {{
      "name": "snippet-name",
      "description": "what this snippet does",
      "used_by": ["section names that use it"]
    }}
  ],
  "css_variables": {{
    "custom_properties": ["any new CSS variables needed"]
  }},
  "generation_order": [
    "list of section names in the order they should be generated",
    "dependencies first (snippets before sections that use them)"
  ]
}}

PLANNING RULES:
1. ALWAYS keep Dawn's header, footer, cart, checkout, account pages — never recreate these
2. main-* sections (main-product, main-cart-items, etc.) should be "keep" unless specific customization needed
3. Prefer "modify" over "create" when Dawn has a similar section — modification is safer
4. Every custom section MUST list a "similar_to" Dawn section for reference
5. generation_order MUST list dependencies first (snippets → sections that use them → templates)
6. Homepage should have 5-8 sections typically
7. Keep section names lowercase with hyphens (e.g., "hero-banner" not "HeroBanner")
8. Think about mobile layout — every section must work on 375px screens
9. If user wants FAQ → use collapsible-content (modify), don't create custom
10. If user wants testimonials → create custom (Dawn doesn't have one)
11. If user wants gallery → collage (modify) or create custom depending on needs
"""


def get_section_planner_prompt(parsed_intent: dict, rag_context: str = "") -> dict:
    """Build the section planner prompt.
    
    Args:
        parsed_intent: Output from intent parser (stage 1)
        rag_context: Optional RAG search results for additional context
    """
    system = (SECTION_PLANNER_SYSTEM
        .replace("{constraints}", get_constraints_for_stage("section_planner"))
        .replace("{dawn_catalog}", DAWN_SECTION_CATALOG)
    )
    
    user_parts = [
        "Create a build plan for this store:\n",
        f"```json\n{__import__('json').dumps(parsed_intent, indent=2)}\n```\n",
    ]
    
    if rag_context:
        user_parts.append(f"\n<reference_context>\n{rag_context}\n</reference_context>\n")
    
    user_parts.append("\nReturn ONLY valid JSON. No markdown code blocks. No explanation.")
    
    return {
        "system": system,
        "user": "\n".join(user_parts),
        "stage": "section_planner",
        "expected_format": "json",
    }
