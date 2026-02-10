"""
Design Token System for ShopifyAI Theme Generation.

Converts the Architect's design specification into concrete CSS custom properties
and a builder-friendly reference guide. Ensures ALL generated sections share
the same visual language.

Architecture:
  - Dawn's native variables (--color-foreground, --font-heading-family, etc.)
    are used for theme-editor-controlled properties.
  - ShopifyAI tokens (--sai-*) extend Dawn's system with section-specific
    design decisions (accent colors, shadows, radii, spacing, transitions).
  - A global CSS file (assets/sai-design-tokens.css) defines all --sai-* vars.
  - Every Builder call receives the token reference so all sections stay consistent.

Usage:
  tokens = DesignTokenProcessor()
  result = tokens.process(architect_requirements)
  # result.css_content   → inject as ThemeFile("assets/sai-design-tokens.css")
  # result.builder_guide → inject into every Builder user message
  # result.token_map     → raw dict for programmatic access
"""

import json
from dataclasses import dataclass, field
from typing import Optional


# ── Defaults ────────────────────────────────────────────────────────────────
# Used when Architect doesn't provide concrete values.

DEFAULT_TOKENS = {
    "colors": {
        "accent": "#e94560",
        "accent_contrast": "#ffffff",
        "surface": "#f8f9fa",
        "surface_alt": "#edf2f7",
        "border": "#e2e8f0",
        "border_strong": "#cbd5e0",
        "success": "#38a169",
        "error": "#e53e3e",
        "warning": "#d69e2e",
        "overlay": "rgba(0, 0, 0, 0.45)",
    },
    "typography": {
        "heading_font": "var(--font-heading-family)",
        "body_font": "var(--font-body-family)",
        "heading_weight": "var(--font-heading-weight)",
        "body_weight": "var(--font-body-weight)",
        "h1_size": "clamp(2.25rem, 5vw, 3.5rem)",
        "h2_size": "clamp(1.75rem, 4vw, 2.75rem)",
        "h3_size": "clamp(1.25rem, 3vw, 1.75rem)",
        "body_size": "1rem",
        "small_size": "0.875rem",
        "line_height_heading": "1.2",
        "line_height_body": "1.6",
        "letter_spacing_heading": "-0.02em",
    },
    "spacing": {
        "section_vertical": "60px",
        "section_vertical_mobile": "36px",
        "inner_padding": "24px",
        "inner_padding_mobile": "16px",
        "grid_gap": "16px",
        "element_gap": "12px",
        "container_max": "var(--page-width)",
    },
    "borders": {
        "radius_sm": "4px",
        "radius_md": "8px",
        "radius_lg": "16px",
        "radius_pill": "999px",
        "width": "1px",
    },
    "shadows": {
        "sm": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
        "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
        "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)",
        "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
    },
    "transitions": {
        "fast": "150ms ease",
        "normal": "300ms ease",
        "slow": "500ms cubic-bezier(0.4, 0, 0.2, 1)",
    },
    "breakpoints": {
        "mobile": "749px",
        "tablet": "989px",
        "desktop": "1200px",
    },
}


@dataclass
class DesignTokenResult:
    """Output of the design token processor."""
    css_content: str           # Full CSS file content for assets/sai-design-tokens.css
    builder_guide: str         # Concise reference for Builder prompt injection
    token_map: dict            # Raw token dict for programmatic access
    liquid_snippet: str        # Optional Liquid snippet for theme.liquid inclusion


class DesignTokenProcessor:
    """Processes Architect output into a concrete design token system."""

    def process(self, architect_output: dict) -> DesignTokenResult:
        """Convert Architect requirements into design tokens.

        The Architect may provide:
          - design_tokens: dict   (concrete values — ideal)
          - design_system: dict   (mood words — we map to defaults)
          - Nothing               (we use full defaults)
        """
        # Try to get concrete tokens from Architect
        raw_tokens = architect_output.get("design_tokens", {})

        if not raw_tokens:
            # Fall back to interpreting the mood-based design_system
            design_system = architect_output.get("design_system", {})
            raw_tokens = self._mood_to_tokens(design_system)

        # Merge with defaults (Architect's values override defaults)
        tokens = self._merge_with_defaults(raw_tokens)

        # Generate outputs
        css_content = self._generate_css(tokens)
        builder_guide = self._generate_builder_guide(tokens)
        liquid_snippet = self._generate_liquid_snippet()

        return DesignTokenResult(
            css_content=css_content,
            builder_guide=builder_guide,
            token_map=tokens,
            liquid_snippet=liquid_snippet,
        )

    def _merge_with_defaults(self, raw: dict) -> dict:
        """Deep merge raw tokens with defaults. Raw values win."""
        merged = {}
        for category, defaults in DEFAULT_TOKENS.items():
            raw_cat = raw.get(category, {})
            if isinstance(defaults, dict) and isinstance(raw_cat, dict):
                merged[category] = {**defaults, **raw_cat}
            else:
                merged[category] = raw_cat if raw_cat else defaults
        return merged

    def _mood_to_tokens(self, design_system: dict) -> dict:
        """Map mood-based design_system to concrete token overrides."""
        tokens = {}
        color_mood = design_system.get("color_mood", "balanced")

        # Color palettes by mood
        color_palettes = {
            "warm": {"accent": "#e07c24", "surface": "#fdf6ec", "border": "#e8d5b7"},
            "cool": {"accent": "#3b82f6", "surface": "#eff6ff", "border": "#bfdbfe"},
            "bold": {"accent": "#dc2626", "surface": "#fef2f2", "border": "#fecaca"},
            "dark": {"accent": "#8b5cf6", "surface": "#1a1a2e", "border": "#374151"},
            "earthy": {"accent": "#92400e", "surface": "#fef3c7", "border": "#d6ceb5"},
            "minimal": {"accent": "#111827", "surface": "#fafafa", "border": "#e5e7eb"},
            "luxury": {"accent": "#b8860b", "surface": "#faf5ef", "border": "#d4c5a9"},
            "playful": {"accent": "#ec4899", "surface": "#fdf2f8", "border": "#fbcfe8"},
        }
        if color_mood in color_palettes:
            tokens["colors"] = color_palettes[color_mood]

        # Typography mood
        typo_mood = design_system.get("typography_mood", "modern-sans")
        typo_map = {
            "modern-sans": {},  # Uses Dawn defaults (Inter-like)
            "elegant-serif": {
                "heading_font": "'Playfair Display', serif",
                "letter_spacing_heading": "0",
            },
            "bold-impact": {
                "heading_weight": "800",
                "letter_spacing_heading": "-0.03em",
            },
            "mono-tech": {
                "heading_font": "'JetBrains Mono', monospace",
                "letter_spacing_heading": "-0.01em",
            },
        }
        if typo_mood in typo_map:
            tokens["typography"] = typo_map[typo_mood]

        # Animation level
        anim_level = design_system.get("animation_level", "subtle")
        if anim_level == "none":
            tokens["transitions"] = {"fast": "0ms", "normal": "0ms", "slow": "0ms"}
        elif anim_level == "dramatic":
            tokens["transitions"] = {
                "fast": "200ms cubic-bezier(0.4, 0, 0.2, 1)",
                "normal": "400ms cubic-bezier(0.4, 0, 0.2, 1)",
                "slow": "700ms cubic-bezier(0.4, 0, 0.2, 1)",
            }

        # Border radius
        layout = design_system.get("layout_density", "balanced")
        if layout == "spacious":
            tokens["spacing"] = {"section_vertical": "80px", "section_vertical_mobile": "48px"}
            tokens["borders"] = {"radius_sm": "8px", "radius_md": "12px", "radius_lg": "24px"}
        elif layout == "compact":
            tokens["spacing"] = {"section_vertical": "40px", "section_vertical_mobile": "24px"}
            tokens["borders"] = {"radius_sm": "2px", "radius_md": "4px", "radius_lg": "8px"}

        return tokens

    def _generate_css(self, tokens: dict) -> str:
        """Generate the CSS custom properties file."""
        colors = tokens.get("colors", {})
        typo = tokens.get("typography", {})
        spacing = tokens.get("spacing", {})
        borders = tokens.get("borders", {})
        shadows = tokens.get("shadows", {})
        transitions = tokens.get("transitions", {})

        return f"""/* ==========================================================================
   ShopifyAI Design Tokens
   Generated by the Architect — DO NOT EDIT MANUALLY
   These extend Dawn's native CSS variable system.
   
   Usage in sections:
     color: var(--sai-color-accent);
     border-radius: var(--sai-radius-md);
     box-shadow: var(--sai-shadow-md);
   ========================================================================== */

:root {{
  /* ── Colors ── */
  --sai-color-accent: {colors.get('accent', '#e94560')};
  --sai-color-accent-contrast: {colors.get('accent_contrast', '#ffffff')};
  --sai-color-surface: {colors.get('surface', '#f8f9fa')};
  --sai-color-surface-alt: {colors.get('surface_alt', '#edf2f7')};
  --sai-color-border: {colors.get('border', '#e2e8f0')};
  --sai-color-border-strong: {colors.get('border_strong', '#cbd5e0')};
  --sai-color-success: {colors.get('success', '#38a169')};
  --sai-color-error: {colors.get('error', '#e53e3e')};
  --sai-color-warning: {colors.get('warning', '#d69e2e')};
  --sai-color-overlay: {colors.get('overlay', 'rgba(0, 0, 0, 0.45)')};

  /* ── Typography ── */
  --sai-font-heading: {typo.get('heading_font', 'var(--font-heading-family)')};
  --sai-font-body: {typo.get('body_font', 'var(--font-body-family)')};
  --sai-font-heading-weight: {typo.get('heading_weight', 'var(--font-heading-weight)')};
  --sai-font-body-weight: {typo.get('body_weight', 'var(--font-body-weight)')};
  --sai-h1-size: {typo.get('h1_size', 'clamp(2.25rem, 5vw, 3.5rem)')};
  --sai-h2-size: {typo.get('h2_size', 'clamp(1.75rem, 4vw, 2.75rem)')};
  --sai-h3-size: {typo.get('h3_size', 'clamp(1.25rem, 3vw, 1.75rem)')};
  --sai-body-size: {typo.get('body_size', '1rem')};
  --sai-small-size: {typo.get('small_size', '0.875rem')};
  --sai-line-height-heading: {typo.get('line_height_heading', '1.2')};
  --sai-line-height-body: {typo.get('line_height_body', '1.6')};
  --sai-letter-spacing-heading: {typo.get('letter_spacing_heading', '-0.02em')};

  /* ── Spacing ── */
  --sai-section-vertical: {spacing.get('section_vertical', '60px')};
  --sai-section-vertical-mobile: {spacing.get('section_vertical_mobile', '36px')};
  --sai-inner-padding: {spacing.get('inner_padding', '24px')};
  --sai-inner-padding-mobile: {spacing.get('inner_padding_mobile', '16px')};
  --sai-grid-gap: {spacing.get('grid_gap', '16px')};
  --sai-element-gap: {spacing.get('element_gap', '12px')};

  /* ── Borders ── */
  --sai-radius-sm: {borders.get('radius_sm', '4px')};
  --sai-radius-md: {borders.get('radius_md', '8px')};
  --sai-radius-lg: {borders.get('radius_lg', '16px')};
  --sai-radius-pill: {borders.get('radius_pill', '999px')};
  --sai-border-width: {borders.get('width', '1px')};

  /* ── Shadows ── */
  --sai-shadow-sm: {shadows.get('sm', '0 1px 3px 0 rgba(0,0,0,0.1)')};
  --sai-shadow-md: {shadows.get('md', '0 4px 6px -1px rgba(0,0,0,0.1)')};
  --sai-shadow-lg: {shadows.get('lg', '0 10px 15px -3px rgba(0,0,0,0.1)')};
  --sai-shadow-xl: {shadows.get('xl', '0 20px 25px -5px rgba(0,0,0,0.1)')};

  /* ── Transitions ── */
  --sai-transition-fast: {transitions.get('fast', '150ms ease')};
  --sai-transition-normal: {transitions.get('normal', '300ms ease')};
  --sai-transition-slow: {transitions.get('slow', '500ms cubic-bezier(0.4, 0, 0.2, 1)')};
}}

/* ── Responsive overrides ── */
@media screen and (max-width: 749px) {{
  :root {{
    --sai-section-vertical: var(--sai-section-vertical-mobile);
    --sai-inner-padding: var(--sai-inner-padding-mobile);
  }}
}}
"""

    def _generate_builder_guide(self, tokens: dict) -> str:
        """Generate a concise reference for the Builder prompt."""
        colors = tokens.get("colors", {})
        borders = tokens.get("borders", {})

        return f"""<design_tokens>
DESIGN TOKEN REFERENCE — Use these exact variables in ALL generated CSS.

COLORS (use these, NOT hardcoded hex values):
  --sai-color-accent: {colors.get('accent', '#e94560')}     → Primary brand/action color
  --sai-color-accent-contrast: {colors.get('accent_contrast', '#fff')}  → Text ON accent backgrounds
  --sai-color-surface: {colors.get('surface', '#f8f9fa')}    → Card/elevated surface background
  --sai-color-surface-alt: {colors.get('surface_alt', '#edf2f7')} → Alternate surface (stripes)
  --sai-color-border: {colors.get('border', '#e2e8f0')}     → Default borders
  --sai-color-overlay: {colors.get('overlay', 'rgba(0,0,0,0.45)')}  → Image overlays

  For text/background, USE Dawn's native variables:
    rgb(var(--color-foreground))   → Main text
    rgb(var(--color-background))   → Main background
    var(--font-heading-family)     → Heading font
    var(--font-body-family)        → Body font

SPACING:
  --sai-section-vertical     → Section top/bottom padding (responsive)
  --sai-inner-padding        → Content inner padding (responsive)
  --sai-grid-gap             → Grid/flex gap between items
  --sai-element-gap          → Gap between small elements (icon + text)

BORDERS:
  --sai-radius-sm: {borders.get('radius_sm', '4px')}   → Small elements (tags, badges)
  --sai-radius-md: {borders.get('radius_md', '8px')}   → Cards, inputs
  --sai-radius-lg: {borders.get('radius_lg', '16px')}  → Large cards, modals
  --sai-radius-pill: 999px  → Pill buttons
  --sai-border-width: {borders.get('width', '1px')}

SHADOWS:
  --sai-shadow-sm  → Subtle lift (cards)
  --sai-shadow-md  → Medium elevation (dropdowns)
  --sai-shadow-lg  → High elevation (modals)

TRANSITIONS:
  --sai-transition-fast   → Hover states (150ms)
  --sai-transition-normal → Reveals, slides (300ms)
  --sai-transition-slow   → Page transitions (500ms)

SECTION PADDING PATTERN (use for EVERY section):
  {{%- style -%}}
    .section-{{{{ section.id }}}}-padding {{
      padding-top: calc(var(--sai-section-vertical) * 0.75);
      padding-bottom: calc(var(--sai-section-vertical) * 0.75);
    }}
    @media screen and (min-width: 750px) {{
      .section-{{{{ section.id }}}}-padding {{
        padding-top: var(--sai-section-vertical);
        padding-bottom: var(--sai-section-vertical);
      }}
    }}
  {{%- endstyle -%}}

CSS CLASS NAMING: Use BEM convention with section name prefix:
  .hero-banner            → block
  .hero-banner__title     → element
  .hero-banner--centered  → modifier

RULES:
  - NEVER hardcode colors — always use var(--sai-*) or Dawn variables
  - NEVER hardcode font families — use var(--sai-font-*) or Dawn variables
  - ALWAYS include mobile breakpoint (@media max-width: 749px)
  - ALWAYS use var(--sai-radius-*) for border-radius
  - ALWAYS use var(--sai-transition-*) for transitions
  - ALWAYS use var(--sai-shadow-*) for box-shadow
</design_tokens>"""

    def _generate_liquid_snippet(self) -> str:
        """Generate Liquid snippet to load the design tokens CSS."""
        return "{{ 'sai-design-tokens.css' | asset_url | stylesheet_tag }}\n"
