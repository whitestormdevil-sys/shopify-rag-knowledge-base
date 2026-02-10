"""
Section Context Accumulator for Builder-to-Builder consistency.

Tracks what previous Builder calls generated (CSS classes, custom properties,
snippets, JS components) and produces a concise context string for the next
Builder call. This ensures:

  - Consistent CSS class naming (BEM prefix carries forward)
  - No duplicate snippet creation (reuse what exists)
  - CSS custom properties are shared (no --color-primary vs --primary-color)
  - Layout patterns stay consistent (all grid or all flexbox)
  - JS custom elements don't collide

The context is kept CONCISE (~20-40 lines) to avoid burning Builder tokens
on context that isn't directly actionable.
"""

import re
from dataclasses import dataclass, field
from typing import Optional

# Avoid circular import — use string type hint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .parser.theme_file import ThemeFile


@dataclass
class SectionRecord:
    """Record of a generated section."""
    name: str
    liquid_path: str
    css_path: Optional[str] = None
    js_path: Optional[str] = None
    snippet_paths: list = field(default_factory=list)


class SectionContextAccumulator:
    """Tracks cross-section context for Builder consistency.
    
    Usage:
        acc = SectionContextAccumulator()
        
        # After each Builder call:
        acc.add_section("hero-banner", generated_files)
        
        # Before next Builder call:
        context = acc.get_context_for_builder()
        # → inject as <previous_sections> in user message
    """

    def __init__(self):
        self.sections: list[SectionRecord] = []
        self.css_classes: list[str] = []          # Ordered, not set — preserves first-seen
        self.css_custom_properties: list[str] = []
        self.snippets: list[str] = []
        self.js_custom_elements: list[str] = []
        self.layout_patterns: list[str] = []      # "grid", "flexbox", "float"
        self._seen_classes: set = set()
        self._seen_props: set = set()

    def add_section(self, section_name: str, files: list) -> None:
        """Register a generated section's files.
        
        Args:
            section_name: The section identifier (e.g., "hero-banner")
            files: List of ThemeFile objects from the Builder
        """
        record = SectionRecord(name=section_name, liquid_path="")

        for f in files:
            path = f.path if hasattr(f, 'path') else str(f)
            content = f.content if hasattr(f, 'content') else ""

            if path.endswith('.liquid') and path.startswith('sections/'):
                record.liquid_path = path
            elif path.endswith('.css'):
                record.css_path = path
                self._extract_css_info(content)
            elif path.endswith('.js'):
                record.js_path = path
                self._extract_js_info(content)
            elif path.startswith('snippets/'):
                record.snippet_paths.append(path)
                self.snippets.append(path)

        self.sections.append(record)

    def _extract_css_info(self, css: str) -> None:
        """Extract CSS classes, custom properties, and layout patterns."""
        if not css:
            return

        # Extract CSS class names from selectors
        # Match .class-name in selectors (before { or ,)
        for match in re.finditer(r'\.([\w][\w-]*)', css):
            cls = match.group(1)
            # Skip common utility/Dawn classes
            if cls in ('page-width', 'section', 'button', 'hidden', 'visually-hidden'):
                continue
            if cls not in self._seen_classes:
                self._seen_classes.add(cls)
                self.css_classes.append(cls)

        # Extract custom properties DEFINED (not just used)
        # Match --property-name: value
        for match in re.finditer(r'(--[\w-]+)\s*:', css):
            prop = match.group(1)
            # Skip our design tokens (they're global, not section-specific)
            if prop.startswith('--sai-') or prop.startswith('--overlay'):
                continue
            if prop not in self._seen_props:
                self._seen_props.add(prop)
                self.css_custom_properties.append(prop)

        # Detect layout patterns
        if 'display: grid' in css or 'grid-template' in css:
            if 'grid' not in self.layout_patterns:
                self.layout_patterns.append('grid')
        if 'display: flex' in css:
            if 'flexbox' not in self.layout_patterns:
                self.layout_patterns.append('flexbox')

    def _extract_js_info(self, js: str) -> None:
        """Extract custom element registrations."""
        if not js:
            return

        for match in re.finditer(r"customElements\.define\(['\"]([^'\"]+)['\"]", js):
            element_name = match.group(1)
            if element_name not in self.js_custom_elements:
                self.js_custom_elements.append(element_name)

    def get_context_for_builder(self) -> str:
        """Generate a concise context string for the next Builder call.
        
        Returns empty string if no sections have been generated yet.
        This is injected as <previous_sections> in the Builder's user message.
        """
        if not self.sections:
            return ""

        parts = []

        # Section list
        section_names = [s.name for s in self.sections]
        parts.append(f"Sections already generated: {', '.join(section_names)}")

        # CSS naming convention — show pattern by example
        if self.css_classes:
            # Group by prefix to show the BEM convention
            prefixes = {}
            for cls in self.css_classes:
                prefix = cls.split('__')[0].split('--')[0]
                if prefix not in prefixes:
                    prefixes[prefix] = []
                if len(prefixes[prefix]) < 3:
                    prefixes[prefix].append(f'.{cls}')

            convention_examples = []
            for prefix, examples in list(prefixes.items())[:4]:
                convention_examples.extend(examples[:2])

            parts.append(
                f"CSS naming convention (follow this BEM pattern): "
                f"{', '.join(convention_examples[:8])}"
            )

        # Section-specific custom properties
        if self.css_custom_properties:
            parts.append(
                f"Section-specific CSS properties defined: "
                f"{', '.join(self.css_custom_properties[:10])}"
            )

        # Available snippets
        if self.snippets:
            parts.append(
                f"Available snippets (REUSE, don't recreate): "
                f"{', '.join(self.snippets)}"
            )

        # JS custom elements
        if self.js_custom_elements:
            parts.append(
                f"Registered JS custom elements: "
                f"{', '.join(self.js_custom_elements)}"
            )

        # Layout pattern
        if self.layout_patterns:
            parts.append(
                f"Layout pattern used: {', '.join(self.layout_patterns)} "
                f"(be consistent — use the same approach)"
            )

        if not parts:
            return ""

        header = "CONSISTENCY RULES — Previous sections used these patterns. Follow them:"
        return f"<previous_sections>\n{header}\n\n" + "\n".join(f"• {p}" for p in parts) + "\n</previous_sections>"

    def get_snippets_list(self) -> list[str]:
        """Return list of snippet paths created so far."""
        return list(self.snippets)

    def get_section_count(self) -> int:
        """Return number of sections generated so far."""
        return len(self.sections)
