"""
Structured Output Format for ShopifyAI Theme Generation

Defines the XML-based output format that AI models must produce,
ensuring parseable, structured theme files every time.

Inspired by bolt.new's <boltArtifact> pattern, adapted for Shopify themes.
"""

# =============================================================================
# THEME OUTPUT FORMAT
# =============================================================================

THEME_OUTPUT_FORMAT = """
<output_format>
  You MUST output theme files using this EXACT structured format.
  Every file goes in a <themeFile> tag. No prose, no explanation around the code.

  FORMAT:
  <shopifyTheme id="unique-theme-id" title="Short Description">

    <themeFile path="sections/section-name.liquid">
      ... complete Liquid code including {% schema %} ...
    </themeFile>

    <themeFile path="assets/section-section-name.css">
      ... complete CSS ...
    </themeFile>

    <themeFile path="assets/section-name.js">
      ... complete JavaScript (only if section needs interactivity) ...
    </themeFile>

    <themeFile path="snippets/snippet-name.liquid">
      ... complete snippet code ...
    </themeFile>

    <themeFile path="templates/page-type.json">
      ... complete JSON template ...
    </themeFile>

  </shopifyTheme>

  CRITICAL RULES:
  1. ALWAYS provide the COMPLETE file content — NEVER use placeholders like "// rest of code..."
  2. NEVER truncate or summarize code
  3. File paths MUST be relative to theme root (sections/, assets/, templates/, snippets/)
  4. Every section MUST include its {% schema %} tag as the last element
  5. CSS files go in assets/ with prefix "section-" (e.g., assets/section-hero-banner.css)
  6. JS files go in assets/ (e.g., assets/hero-banner.js)
  7. Only include JS files when the section genuinely needs client-side interactivity
  8. Template JSON files MUST be valid JSON
  9. Include ALL files needed for the section to work (Liquid + CSS + JS + snippets)
  10. Do NOT include files that already exist in Dawn unchanged
</output_format>
"""

# =============================================================================
# DIFF OUTPUT FORMAT (for iterations)
# =============================================================================

DIFF_OUTPUT_FORMAT = """
<diff_format>
  For modifications to existing sections, use this format:

  <themeDiff>
    <themeFile path="sections/hero-banner.liquid" action="replace">
      ... complete updated file content ...
    </themeFile>

    <themeFile path="assets/section-hero-banner.css" action="replace">
      ... complete updated CSS ...
    </themeFile>

    <themeFile path="sections/old-section.liquid" action="delete" />

    <themeFile path="snippets/new-helper.liquid" action="create">
      ... new snippet content ...
    </themeFile>
  </themeDiff>

  ACTIONS:
  - replace  → overwrite existing file with new content (ALWAYS provide full content)
  - create   → new file that doesn't exist yet
  - delete   → remove file from theme
  
  RULES:
  1. For "replace": ALWAYS provide the COMPLETE updated file, not a diff/patch
  2. For "delete": self-closing tag, no content needed
  3. Only include files that actually changed — don't repeat unchanged files
  4. If modifying a section's CSS, include both the .liquid and .css files
</diff_format>
"""

# =============================================================================
# FEW-SHOT EXAMPLES
# =============================================================================

SECTION_EXAMPLE = '''
<example_output>
  Here's an example of a correctly formatted section output:

  <shopifyTheme id="testimonials-section" title="Customer Testimonials Grid">

    <themeFile path="sections/testimonials.liquid">
{{ 'section-testimonials.css' | asset_url | stylesheet_tag }}

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

<div class="color-{{ section.settings.color_scheme }} gradient">
  <div class="page-width section-{{ section.id }}-padding">
    {%- if section.settings.heading != blank -%}
      <h2 class="testimonials__heading {{ section.settings.heading_size }} center{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}">
        {{ section.settings.heading }}
      </h2>
    {%- endif -%}

    <div class="testimonials__grid testimonials__grid--{{ section.settings.columns }}">
      {%- for block in section.blocks -%}
        <div class="testimonials__item" {{ block.shopify_attributes }}>
          {%- if block.settings.rating > 0 -%}
            <div class="testimonials__stars" role="img" aria-label="{{ block.settings.rating }} out of 5 stars">
              {%- for i in (1..5) -%}
                <span class="testimonials__star{% if i <= block.settings.rating %} testimonials__star--filled{% endif %}">★</span>
              {%- endfor -%}
            </div>
          {%- endif -%}

          {%- if block.settings.quote != blank -%}
            <blockquote class="testimonials__quote">
              {{ block.settings.quote }}
            </blockquote>
          {%- endif -%}

          <div class="testimonials__author">
            {%- if block.settings.author_image != blank -%}
              <div class="testimonials__avatar">
                {{ block.settings.author_image | image_url: width: 100 | image_tag:
                  loading: 'lazy',
                  widths: '50, 100',
                  class: 'testimonials__avatar-img',
                  alt: block.settings.author_name
                }}
              </div>
            {%- endif -%}
            <div class="testimonials__author-info">
              {%- if block.settings.author_name != blank -%}
                <p class="testimonials__author-name">{{ block.settings.author_name | escape }}</p>
              {%- endif -%}
              {%- if block.settings.author_title != blank -%}
                <p class="testimonials__author-title">{{ block.settings.author_title | escape }}</p>
              {%- endif -%}
            </div>
          </div>
        </div>
      {%- endfor -%}
    </div>
  </div>
</div>

{% schema %}
{
  "name": "Testimonials",
  "tag": "section",
  "class": "section",
  "disabled_on": {
    "groups": ["header", "footer"]
  },
  "settings": [
    {
      "type": "inline_richtext",
      "id": "heading",
      "label": "Heading",
      "default": "What Our Customers Say"
    },
    {
      "type": "select",
      "id": "heading_size",
      "options": [
        { "value": "h2", "label": "Small" },
        { "value": "h1", "label": "Medium" },
        { "value": "h0", "label": "Large" }
      ],
      "default": "h1",
      "label": "Heading size"
    },
    {
      "type": "select",
      "id": "columns",
      "options": [
        { "value": "2", "label": "2 columns" },
        { "value": "3", "label": "3 columns" }
      ],
      "default": "3",
      "label": "Desktop columns"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "Color scheme",
      "default": "scheme-1"
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "Top padding",
      "default": 36
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "Bottom padding",
      "default": 36
    }
  ],
  "blocks": [
    {
      "type": "testimonial",
      "name": "Testimonial",
      "settings": [
        {
          "type": "range",
          "id": "rating",
          "min": 0,
          "max": 5,
          "step": 1,
          "label": "Star rating",
          "default": 5
        },
        {
          "type": "richtext",
          "id": "quote",
          "label": "Quote",
          "default": "<p>This product changed my life! Absolutely love it.</p>"
        },
        {
          "type": "image_picker",
          "id": "author_image",
          "label": "Author photo"
        },
        {
          "type": "text",
          "id": "author_name",
          "label": "Author name",
          "default": "Jane Doe"
        },
        {
          "type": "text",
          "id": "author_title",
          "label": "Author title",
          "default": "Verified Buyer"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Testimonials",
      "blocks": [
        { "type": "testimonial" },
        { "type": "testimonial" },
        { "type": "testimonial" }
      ]
    }
  ]
}
{% endschema %}
    </themeFile>

    <themeFile path="assets/section-testimonials.css">
.testimonials__heading {
  margin-bottom: 3rem;
}

.testimonials__grid {
  display: grid;
  gap: 2rem;
}

.testimonials__grid--2 {
  grid-template-columns: repeat(2, 1fr);
}

.testimonials__grid--3 {
  grid-template-columns: repeat(3, 1fr);
}

@media screen and (max-width: 749px) {
  .testimonials__grid--2,
  .testimonials__grid--3 {
    grid-template-columns: 1fr;
  }
}

@media screen and (min-width: 750px) and (max-width: 989px) {
  .testimonials__grid--3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

.testimonials__item {
  padding: 2rem;
  border-radius: var(--text-boxes-radius);
  border: var(--text-boxes-border-width) solid rgba(var(--color-foreground), var(--text-boxes-border-opacity));
}

.testimonials__stars {
  margin-bottom: 1rem;
  font-size: 1.4rem;
}

.testimonials__star {
  color: rgba(var(--color-foreground), 0.2);
}

.testimonials__star--filled {
  color: rgb(var(--color-foreground));
}

.testimonials__quote {
  font-style: italic;
  margin: 0 0 1.5rem;
  line-height: 1.6;
}

.testimonials__author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.testimonials__avatar {
  width: 5rem;
  height: 5rem;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.testimonials__avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.testimonials__author-name {
  font-weight: bold;
  margin: 0;
}

.testimonials__author-title {
  margin: 0;
  opacity: 0.7;
  font-size: 0.9em;
}
    </themeFile>

  </shopifyTheme>
</example_output>
'''


def get_output_format(include_examples: bool = True) -> str:
    """Return the output format specification, optionally with examples."""
    parts = [THEME_OUTPUT_FORMAT]
    if include_examples:
        parts.append(SECTION_EXAMPLE)
    return "\n".join(parts)


def get_diff_format() -> str:
    """Return the diff output format for iteration prompts."""
    return DIFF_OUTPUT_FORMAT
