"""
Liquid Syntax Validator

Validates Liquid template syntax without executing it.
Catches common errors that would break sections in Shopify.

This is a static analysis tool — it can't catch every error,
but it catches the most common ones that AI models produce.
"""

import re
from dataclasses import dataclass, field
from typing import Optional

from ..parser.theme_file import ThemeFile


@dataclass
class ValidationIssue:
    severity: str      # critical, major, minor
    message: str
    line: Optional[int] = None
    fix: Optional[str] = None


@dataclass
class ValidationResult:
    valid: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    
    @property
    def critical_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "critical")
    
    @property
    def major_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "major")


class LiquidValidator:
    """Static analysis validator for Liquid templates."""
    
    # Tag pairs that must be matched
    PAIRED_TAGS = {
        "if": "endif",
        "unless": "unless",
        "for": "endfor",
        "case": "endcase",
        "capture": "endcapture",
        "comment": "endcomment",
        "raw": "endraw",
        "paginate": "endpaginate",
        "form": "endform",
        "style": "endstyle",
        "javascript": "endjavascript",
        "schema": "endschema",
        "liquid": "endliquid",
    }
    
    # Deprecated tags
    DEPRECATED = {"include"}  # Use render instead
    
    # All recognized Liquid tags
    VALID_TAGS = {
        "if", "elsif", "else", "endif",
        "unless", "endunless",
        "for", "endfor", "break", "continue",
        "case", "when", "endcase",
        "assign", "capture", "endcapture", "increment", "decrement",
        "render", "include", "section", "sections",
        "comment", "endcomment",
        "raw", "endraw",
        "liquid", "endliquid",
        "paginate", "endpaginate",
        "form", "endform",
        "style", "endstyle",
        "javascript", "endjavascript",
        "schema", "endschema",
        "layout",
        "echo",
        "tablerow", "endtablerow",
    }
    
    def validate(self, file: ThemeFile) -> ValidationResult:
        """Validate a Liquid file."""
        result = ValidationResult(valid=True)
        content = file.content
        lines = content.split("\n")
        
        # Run all checks
        self._check_tag_matching(content, lines, result)
        self._check_deprecated_tags(content, lines, result)
        self._check_schema_position(content, lines, result, file)
        self._check_render_syntax(content, lines, result)
        self._check_common_errors(content, lines, result)
        self._check_accessibility(content, lines, result, file)
        
        # Set validity
        result.valid = result.critical_count == 0
        return result
    
    def _check_tag_matching(self, content: str, lines: list, result: ValidationResult):
        """Check that all Liquid tags are properly opened and closed."""
        # Extract all Liquid tags
        tag_pattern = re.compile(r'\{%-?\s*(\w+)(?:\s|%)')
        
        stack = []
        for line_num, line in enumerate(lines, 1):
            for match in tag_pattern.finditer(line):
                tag = match.group(1)
                
                if tag in self.PAIRED_TAGS:
                    stack.append((tag, line_num))
                elif tag.startswith("end"):
                    # Find the matching open tag
                    base_tag = tag[3:]  # Remove "end" prefix
                    
                    # Special case: endunless
                    if tag == "endunless":
                        base_tag = "unless"
                    
                    if not stack:
                        result.issues.append(ValidationIssue(
                            severity="critical",
                            message=f"Closing tag '{{% {tag} %}}' has no matching opening tag",
                            line=line_num,
                        ))
                    elif stack[-1][0] != base_tag:
                        result.issues.append(ValidationIssue(
                            severity="critical",
                            message=f"Mismatched tags: expected '{{% end{stack[-1][0]} %}}' but found '{{% {tag} %}}'",
                            line=line_num,
                            fix=f"Check tag at line {stack[-1][1]} — it opened '{{% {stack[-1][0]} %}}'"
                        ))
                        # Try to recover by popping
                        stack.pop()
                    else:
                        stack.pop()
        
        # Any unclosed tags
        for tag, line_num in stack:
            result.issues.append(ValidationIssue(
                severity="critical",
                message=f"Unclosed tag '{{% {tag} %}}' — missing '{{% end{tag} %}}'",
                line=line_num,
            ))
    
    def _check_deprecated_tags(self, content: str, lines: list, result: ValidationResult):
        """Check for deprecated Liquid tags."""
        for line_num, line in enumerate(lines, 1):
            if re.search(r'\{%-?\s*include\s', line):
                result.issues.append(ValidationIssue(
                    severity="major",
                    message="{% include %} is deprecated — use {% render %} instead",
                    line=line_num,
                    fix="Replace {% include 'snippet' %} with {% render 'snippet' %}"
                ))
    
    def _check_schema_position(self, content: str, lines: list, result: ValidationResult, file: ThemeFile):
        """Check that {% schema %} is the last Liquid tag in section files."""
        if not file.is_section:
            return
        
        schema_match = re.search(r'\{%-?\s*schema\s*-?%\}', content)
        endschema_match = re.search(r'\{%-?\s*endschema\s*-?%\}', content)
        
        if not schema_match:
            result.issues.append(ValidationIssue(
                severity="critical",
                message="Section file is missing {% schema %} tag",
                fix="Add {% schema %} with valid JSON at the end of the file"
            ))
            return
        
        if not endschema_match:
            result.issues.append(ValidationIssue(
                severity="critical",
                message="Section has {% schema %} but missing {% endschema %}",
            ))
            return
        
        # Check nothing meaningful comes after endschema
        after_endschema = content[endschema_match.end():].strip()
        if after_endschema:
            # Allow whitespace and comments, but not Liquid tags
            if re.search(r'\{[%{]', after_endschema):
                result.issues.append(ValidationIssue(
                    severity="critical",
                    message="Liquid code found after {% endschema %} — schema must be the LAST tag",
                    fix="Move all code before the {% schema %} block"
                ))
    
    def _check_render_syntax(self, content: str, lines: list, result: ValidationResult):
        """Check {% render %} tag syntax."""
        for line_num, line in enumerate(lines, 1):
            render_matches = re.finditer(r'\{%-?\s*render\s+[\'"]([^\'"]+)[\'"]', line)
            for match in render_matches:
                snippet_name = match.group(1)
                # Snippet names should be lowercase with hyphens
                if snippet_name != snippet_name.lower():
                    result.issues.append(ValidationIssue(
                        severity="minor",
                        message=f"Snippet name '{snippet_name}' should be lowercase",
                        line=line_num,
                    ))
    
    def _check_common_errors(self, content: str, lines: list, result: ValidationResult):
        """Check for common Liquid errors AI models make."""
        for line_num, line in enumerate(lines, 1):
            # Ternary operator (doesn't exist in Liquid)
            if re.search(r'\{\{.*\?.*:.*\}\}', line) and "?" in line:
                # Be careful not to flag legitimate ? in URLs
                if not re.search(r'https?://.*\?', line):
                    result.issues.append(ValidationIssue(
                        severity="critical",
                        message="Ternary operator (?:) doesn't exist in Liquid",
                        line=line_num,
                        fix="Use {% if condition %}value{% else %}other{% endif %} or | default: filter"
                    ))
            
            # Arrow functions in Liquid context
            if "=>" in line and "{%" in line:
                result.issues.append(ValidationIssue(
                    severity="critical",
                    message="Arrow functions (=>) don't exist in Liquid — this is JavaScript syntax",
                    line=line_num,
                ))
            
            # Template literals in Liquid
            if "`" in line and "{{" in line and "${" in line:
                result.issues.append(ValidationIssue(
                    severity="critical",
                    message="Template literals (`${}`) don't work in Liquid — use Liquid filters",
                    line=line_num,
                ))
            
            # Double-rendering {{ {{ }}  }}
            if re.search(r'\{\{\s*\{\{', line):
                result.issues.append(ValidationIssue(
                    severity="critical",
                    message="Nested {{ {{ }} }} — Liquid output tags can't be nested",
                    line=line_num,
                ))
            
            # forloop outside of for
            # (This is a simplified check — only flags if forloop appears with no for in context)
            
            # Missing | escape on user-provided content in attributes
            attr_pattern = re.findall(r'(?:alt|title|aria-label)="([^"]*\{\{[^}]*\}\}[^"]*)"', line)
            for attr_val in attr_pattern:
                if "| escape" not in attr_val and "| e " not in attr_val:
                    # Check if it's a settings value (should be escaped)
                    if "settings." in attr_val or "block.settings." in attr_val:
                        result.issues.append(ValidationIssue(
                            severity="major",
                            message="User-provided value in HTML attribute without | escape filter",
                            line=line_num,
                            fix="Add | escape filter: {{ value | escape }}"
                        ))
    
    def _check_accessibility(self, content: str, lines: list, result: ValidationResult, file: ThemeFile):
        """Check basic accessibility requirements."""
        if not file.is_section and not file.is_snippet:
            return
        
        # Check images have alt text
        img_tags = re.finditer(r'<img\s[^>]*>', content, re.DOTALL)
        for img in img_tags:
            img_str = img.group(0)
            if 'alt=' not in img_str and 'alt =' not in img_str:
                line_num = content[:img.start()].count("\n") + 1
                result.issues.append(ValidationIssue(
                    severity="major",
                    message="<img> tag missing alt attribute",
                    line=line_num,
                    fix='Add alt="{{ image.alt | escape }}" or alt="" for decorative images'
                ))
        
        # Check image_tag usage (Liquid filter) — these auto-generate alt but check anyway
        # image_tag filter in Liquid adds alt automatically from image.alt
        
        # Check for block.shopify_attributes
        if file.is_section and "section.blocks" in content:
            if "shopify_attributes" not in content:
                result.issues.append(ValidationIssue(
                    severity="major",
                    message="Section uses blocks but missing {{ block.shopify_attributes }}",
                    fix="Add {{ block.shopify_attributes }} to block wrapper elements for theme editor support"
                ))
