"""
ThemeFile dataclass — represents a single file in a Shopify theme.
"""

from dataclasses import dataclass, field
from typing import Optional
from pathlib import PurePosixPath


@dataclass
class ThemeFile:
    """A single file in a Shopify theme."""
    
    path: str                          # e.g., "sections/hero-banner.liquid"
    content: str                       # Full file content
    action: str = "create"             # create | replace | delete
    
    @property
    def directory(self) -> str:
        """Theme directory (sections, assets, templates, snippets, etc.)."""
        return PurePosixPath(self.path).parts[0] if "/" in self.path else ""
    
    @property
    def filename(self) -> str:
        """Filename without directory."""
        return PurePosixPath(self.path).name
    
    @property
    def name(self) -> str:
        """Filename without extension."""
        return PurePosixPath(self.path).stem
    
    @property
    def extension(self) -> str:
        """File extension (e.g., '.liquid', '.css', '.js')."""
        return PurePosixPath(self.path).suffix
    
    @property
    def is_section(self) -> bool:
        return self.directory == "sections"
    
    @property
    def is_snippet(self) -> bool:
        return self.directory == "snippets"
    
    @property
    def is_asset(self) -> bool:
        return self.directory == "assets"
    
    @property
    def is_template(self) -> bool:
        return self.directory == "templates"
    
    @property
    def is_layout(self) -> bool:
        return self.directory == "layout"
    
    @property
    def is_config(self) -> bool:
        return self.directory == "config"
    
    @property
    def shopify_asset_key(self) -> str:
        """The key used by Shopify Asset API (e.g., 'sections/hero.liquid')."""
        return self.path
    
    def validate_path(self) -> list[str]:
        """Validate the file path follows Shopify conventions."""
        errors = []
        valid_dirs = {"sections", "snippets", "assets", "templates", "layout", "config", "locales"}
        
        if self.directory not in valid_dirs:
            errors.append(f"Invalid directory '{self.directory}'. Must be one of: {valid_dirs}")
        
        if self.is_section and self.extension != ".liquid":
            errors.append(f"Section files must be .liquid, got '{self.extension}'")
        
        if self.is_snippet and self.extension != ".liquid":
            errors.append(f"Snippet files must be .liquid, got '{self.extension}'")
        
        if self.is_template and self.extension not in (".json", ".liquid"):
            errors.append(f"Template files must be .json or .liquid, got '{self.extension}'")
        
        if self.is_asset and self.extension not in (".css", ".js", ".svg", ".json"):
            errors.append(f"Unexpected asset extension '{self.extension}'")
        
        # Check naming conventions
        if self.filename != self.filename.lower():
            errors.append(f"Filename should be lowercase: '{self.filename}'")
        
        if " " in self.filename:
            errors.append(f"Filename should not contain spaces: '{self.filename}'")
        
        return errors
    
    def __repr__(self) -> str:
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"ThemeFile(path='{self.path}', action='{self.action}', content='{content_preview}')"
