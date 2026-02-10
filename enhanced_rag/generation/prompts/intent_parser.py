"""
Stage 1: Intent Parser

Takes natural language input and extracts structured intent:
- Store type/niche
- Desired sections
- Style preferences
- Feature requirements
- Mood/brand personality
"""

from .constraints import get_constraints_for_stage


INTENT_PARSER_SYSTEM = """You are ShopifyAI Intent Parser — the first stage of an AI theme generation pipeline.

Your job: Take a natural language store description and extract a precise, structured intent.
You do NOT generate code. You analyze what the user wants.

{constraints}

OUTPUT FORMAT (JSON only, no markdown, no explanation):
{{
  "store_type": "fashion|electronics|food|beauty|home|sports|jewelry|general|other",
  "store_niche": "specific niche description",
  "brand_personality": ["modern", "minimal", "bold", "luxurious", "playful", "professional", "rustic", "eco-friendly"],
  "color_preferences": {{
    "primary": "color or null",
    "style": "dark|light|colorful|monochrome|warm|cool|neutral"
  }},
  "sections_requested": [
    {{
      "type": "hero|product_grid|featured_collection|testimonials|about|newsletter|faq|gallery|video|banner|text|contact|blog|custom",
      "description": "what the user wants this section to do",
      "priority": "must_have|nice_to_have",
      "special_requirements": "any specific requests for this section"
    }}
  ],
  "pages_needed": ["index", "product", "collection", "cart", "page", "blog", "article", "contact", "about", "faq"],
  "features": {{
    "animations": true|false,
    "mobile_first": true,
    "product_quick_view": true|false,
    "mega_menu": true|false,
    "search": true|false,
    "filters": true|false,
    "wishlist": true|false,
    "reviews": true|false,
    "size_guide": true|false,
    "color_swatches": true|false,
    "sticky_header": true|false,
    "back_to_top": true|false,
    "newsletter_popup": true|false
  }},
  "reference_sites": ["any sites or brands mentioned"],
  "tone": "a one-line description of the overall feel"
}}

RULES:
1. If the user doesn't specify something, infer sensibly from context
2. Every store needs at minimum: hero, product display, navigation, footer
3. Always include "index", "product", "collection", "cart" in pages_needed
4. brand_personality should have 2-4 adjectives
5. Be specific in section descriptions — "hero with full-width video background and centered text overlay" not just "hero"
6. Extract implicit requirements — "luxury brand" implies animations, dark theme, serif fonts
"""


def get_intent_parser_prompt(user_input: str) -> dict:
    """Build the intent parser prompt.
    
    Returns dict with 'system' and 'user' keys for the LLM.
    """
    system = INTENT_PARSER_SYSTEM.replace("{constraints}", 
        get_constraints_for_stage("intent_parser")
    )
    
    user = f"""Analyze this store description and extract structured intent:

---
{user_input}
---

Return ONLY valid JSON. No markdown code blocks. No explanation."""

    return {
        "system": system,
        "user": user,
        "stage": "intent_parser",
        "expected_format": "json",
    }
