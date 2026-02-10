"""
Output Parser for ShopifyAI Theme Generation

Parses structured AI output (<shopifyTheme> and <themeDiff>) into ThemeFile objects.
Handles edge cases: malformed XML, missing tags, streaming partial output.
"""

import re
import json
from typing import Optional
from dataclasses import dataclass, field

from .theme_file import ThemeFile


@dataclass
class ParseResult:
    """Result of parsing AI output."""
    theme_id: str = ""
    title: str = ""
    files: list[ThemeFile] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    raw_output: str = ""
    
    @property
    def success(self) -> bool:
        return len(self.files) > 0 and len(self.errors) == 0
    
    @property
    def has_files(self) -> bool:
        return len(self.files) > 0
    
    @property
    def sections(self) -> list[ThemeFile]:
        return [f for f in self.files if f.is_section]
    
    @property
    def assets(self) -> list[ThemeFile]:
        return [f for f in self.files if f.is_asset]
    
    @property
    def templates(self) -> list[ThemeFile]:
        return [f for f in self.files if f.is_template]
    
    @property
    def snippets(self) -> list[ThemeFile]:
        return [f for f in self.files if f.is_snippet]
    
    def get_file(self, path: str) -> Optional[ThemeFile]:
        """Get a file by path."""
        for f in self.files:
            if f.path == path:
                return f
        return None
    
    def to_dict(self) -> dict:
        """Convert to dict for serialization."""
        return {
            "theme_id": self.theme_id,
            "title": self.title,
            "files": [{"path": f.path, "action": f.action, "content": f.content} for f in self.files],
            "errors": self.errors,
        }


class ThemeOutputParser:
    """Parses <shopifyTheme> output from the section generator."""
    
    # Regex patterns
    THEME_TAG = re.compile(
        r'<shopifyTheme\s+(?:id="([^"]*)")?\s*(?:title="([^"]*)")?\s*>',
        re.DOTALL
    )
    THEME_CLOSE = re.compile(r'</shopifyTheme>')
    FILE_TAG = re.compile(
        r'<themeFile\s+path="([^"]+)"(?:\s+action="([^"]*)")?\s*>(.*?)</themeFile>',
        re.DOTALL
    )
    FILE_SELF_CLOSE = re.compile(
        r'<themeFile\s+path="([^"]+)"\s+action="delete"\s*/>'
    )
    
    def parse(self, raw_output: str) -> ParseResult:
        """Parse AI output into structured theme files.
        
        Handles multiple fallback strategies:
        1. Standard <shopifyTheme> tags
        2. Loose <themeFile> tags (no wrapper)
        3. Markdown code blocks with file paths
        """
        result = ParseResult(raw_output=raw_output)
        
        # Strategy 1: Standard <shopifyTheme> wrapper
        theme_match = self.THEME_TAG.search(raw_output)
        if theme_match:
            result.theme_id = theme_match.group(1) or ""
            result.title = theme_match.group(2) or ""
            
            # Extract content between theme tags
            theme_start = theme_match.end()
            theme_close = self.THEME_CLOSE.search(raw_output, theme_start)
            theme_content = raw_output[theme_start:theme_close.start() if theme_close else len(raw_output)]
            
            result.files = self._extract_files(theme_content)
            
            if result.files:
                self._validate_files(result)
                return result
        
        # Strategy 2: Loose <themeFile> tags
        files = self._extract_files(raw_output)
        if files:
            result.files = files
            result.errors.append("Warning: No <shopifyTheme> wrapper found, extracted loose <themeFile> tags")
            self._validate_files(result)
            return result
        
        # Strategy 3: Try markdown code blocks
        files = self._extract_from_markdown(raw_output)
        if files:
            result.files = files
            result.errors.append("Warning: Parsed from markdown code blocks (non-standard format)")
            self._validate_files(result)
            return result
        
        result.errors.append("Failed to parse any theme files from output")
        return result
    
    def _extract_files(self, content: str) -> list[ThemeFile]:
        """Extract ThemeFile objects from content with <themeFile> tags."""
        files = []
        
        # Self-closing delete tags
        for match in self.FILE_SELF_CLOSE.finditer(content):
            files.append(ThemeFile(
                path=match.group(1),
                content="",
                action="delete"
            ))
        
        # Regular file tags
        for match in self.FILE_TAG.finditer(content):
            path = match.group(1)
            action = match.group(2) or "create"
            file_content = match.group(3).strip()
            
            files.append(ThemeFile(
                path=path,
                content=file_content,
                action=action
            ))
        
        return files
    
    def _extract_from_markdown(self, content: str) -> list[ThemeFile]:
        """Fallback: extract files from markdown code blocks with file path hints."""
        files = []
        
        # Pattern: ```liquid\n// sections/hero-banner.liquid\n...```
        # Or: **sections/hero-banner.liquid**\n```liquid\n...```
        block_pattern = re.compile(
            r'(?:(?:\*\*|`)((?:sections|assets|snippets|templates|layout|config)/[^\s*`]+)(?:\*\*|`)[\s\n]*)?'
            r'```(?:liquid|css|javascript|js|json)?\n'
            r'(?://\s*((?:sections|assets|snippets|templates|layout|config)/[^\n]+)\n)?'
            r'(.*?)'
            r'```',
            re.DOTALL
        )
        
        for match in block_pattern.finditer(content):
            path = match.group(1) or match.group(2)
            code = match.group(3).strip()
            
            if path and code:
                files.append(ThemeFile(path=path, content=code, action="create"))
        
        return files
    
    def _validate_files(self, result: ParseResult):
        """Run basic validation on parsed files."""
        paths_seen = set()
        
        for f in result.files:
            # Check for duplicates
            if f.path in paths_seen:
                result.errors.append(f"Duplicate file path: {f.path}")
            paths_seen.add(f.path)
            
            # Validate path
            path_errors = f.validate_path()
            for err in path_errors:
                result.errors.append(f"{f.path}: {err}")
            
            # Check sections have schema
            if f.is_section and f.action != "delete":
                if "{% schema %}" not in f.content and "{%- schema -%}" not in f.content:
                    result.errors.append(f"{f.path}: Missing {{% schema %}} tag")
            
            # Check templates are valid JSON
            if f.is_template and f.extension == ".json" and f.action != "delete":
                try:
                    json.loads(f.content)
                except json.JSONDecodeError as e:
                    result.errors.append(f"{f.path}: Invalid JSON — {e}")
            
            # Check for placeholder comments
            placeholders = ["// TODO", "<!-- TODO", "// rest of", "// add more", "// ...", "/* ... */"]
            for placeholder in placeholders:
                if placeholder.lower() in f.content.lower():
                    result.errors.append(f"{f.path}: Contains placeholder '{placeholder}' — code must be complete")
            
            # Check CSS references match
            if f.is_section:
                css_refs = re.findall(r"'(section-[^']+\.css)'", f.content)
                for css_ref in css_refs:
                    css_path = f"assets/{css_ref}"
                    if not any(rf.path == css_path for rf in result.files):
                        # Could be an existing Dawn asset
                        result.errors.append(
                            f"{f.path}: References '{css_ref}' but no matching asset in output "
                            f"(OK if it's an existing Dawn asset)"
                        )


class ThemeDiffParser(ThemeOutputParser):
    """Parses <themeDiff> output from the iteration handler."""
    
    DIFF_TAG = re.compile(r'<themeDiff\s*>', re.DOTALL)
    DIFF_CLOSE = re.compile(r'</themeDiff>')
    
    def parse(self, raw_output: str) -> ParseResult:
        """Parse diff output — same file extraction, different wrapper tag."""
        result = ParseResult(raw_output=raw_output)
        
        # Try <themeDiff> wrapper
        diff_match = self.DIFF_TAG.search(raw_output)
        if diff_match:
            diff_start = diff_match.end()
            diff_close = self.DIFF_CLOSE.search(raw_output, diff_start)
            diff_content = raw_output[diff_start:diff_close.start() if diff_close else len(raw_output)]
            
            result.files = self._extract_files(diff_content)
            
            if result.files:
                self._validate_files(result)
                return result
        
        # Fall back to standard parsing
        return super().parse(raw_output)


def parse_json_response(raw_output: str) -> tuple[Optional[dict], Optional[str]]:
    """Parse a JSON response from intent parser or verifier.
    
    Returns (parsed_dict, error_message).
    """
    # Try direct parse
    try:
        return json.loads(raw_output.strip()), None
    except json.JSONDecodeError:
        pass
    
    # Try extracting from markdown code block
    json_match = re.search(r'```(?:json)?\s*\n(.*?)\n```', raw_output, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1)), None
        except json.JSONDecodeError as e:
            return None, f"JSON in code block is invalid: {e}"
    
    # Try finding JSON object in text
    json_match = re.search(r'\{[\s\S]*\}', raw_output)
    if json_match:
        try:
            return json.loads(json_match.group(0)), None
        except json.JSONDecodeError as e:
            return None, f"Found JSON-like content but it's invalid: {e}"
    
    return None, "No JSON found in response"
