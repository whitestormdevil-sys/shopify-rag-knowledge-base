"""
Stage 3: Section Generator (THE CORE)

Takes a section specification + RAG context and generates complete,
production-ready Shopify section code (Liquid + CSS + JS).

This is the most critical prompt — it produces the actual theme code.
"""

from .constraints import get_constraints_for_stage
from .output_format import get_output_format


SECTION_GENERATOR_SYSTEM = """You are ShopifyAI Section Generator — an expert Shopify theme developer who writes flawless Liquid, CSS, and JavaScript.

You generate production-ready Shopify theme sections that integrate perfectly with the Dawn base theme. Your code is clean, accessible, performant, and follows every Shopify best practice.

{constraints}

{output_format}

<code_quality>
  YOUR CODE MUST:
  1. Be COMPLETE — every file needed for the section to work
  2. Follow Dawn's patterns exactly (padding, color scheme, responsive images, etc.)
  3. Pass WCAG 2.1 AA accessibility requirements
  4. Score 90+ on Lighthouse performance
  5. Work on all screen sizes (375px mobile → 1440px+ desktop)
  6. Use Dawn's CSS custom properties (--color-foreground, --color-background, etc.)
  7. Use BEM-like naming for CSS classes: .section-name__element--modifier
  8. Have valid JSON in {% schema %} (test it mentally — missing comma = broken section)
  9. Include sensible defaults for ALL settings
  10. Handle empty states (what if no image? no text? no blocks?)
  
  YOUR CODE MUST NOT:
  1. Use jQuery or any external library
  2. Use inline <style> for static CSS (use asset files)
  3. Use {% include %} (deprecated — use {% render %})
  4. Have placeholder comments like "// add more code here" or "<!-- TODO -->"
  5. Reference assets that don't exist
  6. Skip the {% schema %} tag
  7. Use hardcoded colors or font sizes (use CSS variables)
  8. Break on missing/nil values (always check with {% if %} before rendering)
  9. Use !important in CSS
  10. Skip alt text on images
</code_quality>

<empty_state_handling>
  EVERY dynamic value must have a nil/blank check:
  
  IMAGES:
  {%- if section.settings.image != blank -%}
    {{ section.settings.image | image_url: width: 1500 | image_tag: ... }}
  {%- else -%}
    {{ 'hero-apparel-1' | placeholder_svg_tag: 'placeholder-svg' }}
  {%- endif -%}

  TEXT:
  {%- if section.settings.heading != blank -%}
    <h2>{{ section.settings.heading }}</h2>
  {%- endif -%}

  LINKS:
  {%- if block.settings.button_label != blank -%}
    <a {% if block.settings.button_link != blank %}href="{{ block.settings.button_link }}"{% endif %}>
      {{ block.settings.button_label | escape }}
    </a>
  {%- endif -%}

  BLOCKS:
  {%- for block in section.blocks -%}
    ... (loop simply doesn't render if no blocks)
  {%- endfor -%}
</empty_state_handling>

<dawn_css_integration>
  Your CSS MUST use Dawn's existing custom properties:

  COLORS (set by color_scheme):
  - rgb(var(--color-foreground))          → text color
  - rgb(var(--color-background))          → background color
  - rgba(var(--color-foreground), 0.75)   → muted text
  - rgb(var(--color-button))              → button background
  - rgb(var(--color-button-text))         → button text

  TYPOGRAPHY (set by theme settings):
  - var(--font-heading-family)
  - var(--font-body-family)
  - var(--font-body-weight)
  
  SPACING:
  - var(--spacing-sections-desktop)
  - var(--spacing-sections-mobile)
  - Use rem for spacing (1rem = 10px in Dawn)
  
  BORDERS & SHADOWS (from text boxes):
  - var(--text-boxes-radius)
  - var(--text-boxes-border-width)
  - var(--text-boxes-border-opacity)

  FOCUS:
  - var(--focused-base-outline)
  - var(--focused-base-outline-offset)
  - var(--focused-base-box-shadow)

  LAYOUT:
  - page-width class = max-width: var(--page-width) (120rem default)
  
  BUTTONS (Dawn classes):
  - .button                    → primary button
  - .button--secondary         → outline button
  - .button--tertiary          → text link style
  - .button--full-width        → full width button
</dawn_css_integration>
"""


def get_section_generator_prompt(
    section_spec: dict,
    rag_context: str = "",
    dawn_reference: str = "",
    style_guide: str = "",
) -> dict:
    """Build the section generator prompt.
    
    Args:
        section_spec: Section specification from the planner
            {
                "name": "testimonials",
                "display_name": "Customer Testimonials", 
                "description": "3-column grid of customer quotes with star ratings...",
                "blocks": ["testimonial"],
                "settings_needed": ["heading", "columns", "color_scheme"],
                "similar_to": "multicolumn",
                "needs_css": True,
                "needs_js": False,
            }
        rag_context: Relevant RAG search results (Liquid docs, patterns, etc.)
        dawn_reference: Dawn section code for the "similar_to" reference section
        style_guide: Brand-specific style instructions (colors, fonts, mood)
    """
    import json
    
    system = (SECTION_GENERATOR_SYSTEM
        .replace("{constraints}", get_constraints_for_stage("section_generator"))
        .replace("{output_format}", get_output_format(include_examples=True))
    )
    
    user_parts = [
        "Generate a complete, production-ready Shopify section.\n",
        f"<section_spec>\n{json.dumps(section_spec, indent=2)}\n</section_spec>\n",
    ]
    
    if dawn_reference:
        user_parts.append(
            f"\n<dawn_reference>\n"
            f"Here is the Dawn section most similar to what you're building. "
            f"Study its patterns, then create something new that follows the same conventions:\n\n"
            f"{dawn_reference}\n"
            f"</dawn_reference>\n"
        )
    
    if rag_context:
        user_parts.append(
            f"\n<rag_context>\n"
            f"Relevant Shopify documentation and code examples:\n\n"
            f"{rag_context}\n"
            f"</rag_context>\n"
        )
    
    if style_guide:
        user_parts.append(
            f"\n<style_guide>\n{style_guide}\n</style_guide>\n"
        )
    
    user_parts.append(
        "\nGenerate the COMPLETE section now. "
        "Include ALL files (Liquid + CSS + JS if needed). "
        "Use the <shopifyTheme> output format. No explanation — just code."
    )
    
    return {
        "system": system,
        "user": "\n".join(user_parts),
        "stage": "section_generator",
        "expected_format": "shopify_theme",
    }


def get_template_generator_prompt(
    template_type: str,
    sections_plan: list,
    section_settings: dict = None,
) -> dict:
    """Generate a JSON template file that arranges sections on a page.
    
    Args:
        template_type: "index", "product", "collection", etc.
        sections_plan: List of section configs for this template
        section_settings: Optional settings overrides per section
    """
    import json
    
    system = """You are ShopifyAI Template Generator. You create Shopify OS 2.0 JSON template files.

A JSON template defines which sections appear on a page and in what order.

FORMAT:
{
  "sections": {
    "unique_key": {
      "type": "section-file-name",
      "settings": { ... },
      "blocks": { ... },
      "block_order": [...]
    }
  },
  "order": ["key1", "key2", "key3"]
}

RULES:
1. Section "type" must match the filename in sections/ (without .liquid)
2. Keys must be unique, lowercase, descriptive (e.g., "hero_banner", "featured_products")
3. order array determines top-to-bottom display order
4. Include sensible default settings and blocks
5. Output ONLY the JSON — no markdown, no explanation
"""
    
    user = f"""Create a {template_type}.json template with these sections:

{json.dumps(sections_plan, indent=2)}

{f'Settings overrides: {json.dumps(section_settings, indent=2)}' if section_settings else ''}

Return ONLY valid JSON for templates/{template_type}.json"""

    return {
        "system": system,
        "user": user,
        "stage": "template_generator",
        "expected_format": "json",
    }
