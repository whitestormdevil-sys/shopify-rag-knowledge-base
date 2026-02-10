"""
Schema JSON Validator

Validates the {% schema %} JSON in Shopify section files.
Ensures all settings are properly formed and follow Shopify conventions.
"""

import re
import json
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class SchemaIssue:
    severity: str      # critical, major, minor
    path: str          # JSON path like "settings[2].options"
    message: str
    fix: Optional[str] = None


@dataclass 
class SchemaResult:
    valid: bool
    schema_data: Optional[dict] = None
    issues: list[SchemaIssue] = field(default_factory=list)
    
    @property
    def critical_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "critical")


# All valid Shopify setting types
VALID_SETTING_TYPES = {
    # Input
    "text", "textarea", "richtext", "inline_richtext", "number", "range",
    "checkbox", "select", "radio",
    # Resource pickers
    "image_picker", "video", "video_url", "url", "link_list",
    "page", "blog", "collection", "product", "product_list", "collection_list",
    # Design
    "color", "color_scheme", "color_background", "font_picker",
    # Info (no value)
    "header", "paragraph", "liquid",
}

# Setting types that DON'T use "label" (use "content" instead)
CONTENT_TYPES = {"header", "paragraph"}

# Setting types that require additional fields
EXTRA_REQUIRED = {
    "range": {"min", "max", "step"},
    "select": {"options"},
    "radio": {"options"},
    "video_url": {"accept"},
}


class SchemaValidator:
    """Validates section schema JSON."""
    
    def validate_section(self, liquid_content: str) -> SchemaResult:
        """Extract and validate schema from a Liquid section file."""
        result = SchemaResult(valid=True)
        
        # Extract schema JSON
        schema_match = re.search(
            r'\{%-?\s*schema\s*-?%\}\s*(.*?)\s*\{%-?\s*endschema\s*-?%\}',
            liquid_content,
            re.DOTALL
        )
        
        if not schema_match:
            result.valid = False
            result.issues.append(SchemaIssue(
                severity="critical",
                path="",
                message="No {% schema %} block found"
            ))
            return result
        
        raw_json = schema_match.group(1).strip()
        
        # Parse JSON
        try:
            schema = json.loads(raw_json)
        except json.JSONDecodeError as e:
            result.valid = False
            result.issues.append(SchemaIssue(
                severity="critical",
                path="",
                message=f"Invalid JSON in schema: {e}",
                fix="Check for missing commas, unclosed brackets, or trailing commas"
            ))
            return result
        
        result.schema_data = schema
        
        # Validate structure
        self._validate_root(schema, result)
        self._validate_settings(schema.get("settings", []), "settings", result)
        self._validate_blocks(schema.get("blocks", []), result)
        self._validate_presets(schema.get("presets", []), schema, result)
        self._check_id_uniqueness(schema, result)
        
        result.valid = result.critical_count == 0
        return result
    
    def _validate_root(self, schema: dict, result: SchemaResult):
        """Validate root schema properties."""
        # Name is required
        if "name" not in schema:
            result.issues.append(SchemaIssue(
                severity="critical",
                path="name",
                message='Schema missing required "name" field',
                fix='Add "name": "Section Name"'
            ))
        elif not isinstance(schema["name"], str):
            result.issues.append(SchemaIssue(
                severity="critical",
                path="name",
                message='"name" must be a string'
            ))
        
        # Optional but recommended fields
        if "tag" in schema and schema["tag"] not in {"section", "div", "aside", "article", "nav", "footer", "header"}:
            result.issues.append(SchemaIssue(
                severity="minor",
                path="tag",
                message=f'Unusual tag value "{schema["tag"]}" — common values: section, div, aside'
            ))
        
        # disabled_on / enabled_on
        if "disabled_on" in schema:
            groups = schema["disabled_on"].get("groups", [])
            valid_groups = {"header", "footer", "aside", "custom.overlay"}
            for g in groups:
                if g not in valid_groups:
                    result.issues.append(SchemaIssue(
                        severity="minor",
                        path=f"disabled_on.groups",
                        message=f'Unknown group "{g}". Valid: {valid_groups}'
                    ))
        
        if "disabled_on" in schema and "enabled_on" in schema:
            result.issues.append(SchemaIssue(
                severity="critical",
                path="",
                message="Cannot have both disabled_on and enabled_on — use only one"
            ))
    
    def _validate_settings(self, settings: list, path_prefix: str, result: SchemaResult):
        """Validate an array of settings."""
        if not isinstance(settings, list):
            result.issues.append(SchemaIssue(
                severity="critical",
                path=path_prefix,
                message=f'"{path_prefix}" must be an array'
            ))
            return
        
        for i, setting in enumerate(settings):
            path = f"{path_prefix}[{i}]"
            
            if not isinstance(setting, dict):
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=path,
                    message="Setting must be an object"
                ))
                continue
            
            # Type is required
            setting_type = setting.get("type")
            if not setting_type:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}.type",
                    message="Setting missing required 'type' field"
                ))
                continue
            
            if setting_type not in VALID_SETTING_TYPES:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}.type",
                    message=f'Unknown setting type "{setting_type}". Valid types: {sorted(VALID_SETTING_TYPES)}',
                ))
                continue
            
            # ID is required for non-info types
            if setting_type not in CONTENT_TYPES:
                if "id" not in setting:
                    result.issues.append(SchemaIssue(
                        severity="critical",
                        path=f"{path}.id",
                        message=f"Setting of type '{setting_type}' missing required 'id' field"
                    ))
                if "label" not in setting:
                    result.issues.append(SchemaIssue(
                        severity="major",
                        path=f"{path}.label",
                        message=f"Setting '{setting.get('id', '?')}' missing 'label' field"
                    ))
            else:
                # header/paragraph use "content" not "label"
                if "content" not in setting:
                    result.issues.append(SchemaIssue(
                        severity="major",
                        path=f"{path}.content",
                        message=f"'{setting_type}' setting missing 'content' field (uses 'content' not 'label')"
                    ))
            
            # Type-specific validation
            if setting_type in EXTRA_REQUIRED:
                for req_field in EXTRA_REQUIRED[setting_type]:
                    if req_field not in setting:
                        result.issues.append(SchemaIssue(
                            severity="critical",
                            path=f"{path}.{req_field}",
                            message=f"'{setting_type}' setting requires '{req_field}' field",
                            fix=self._get_field_hint(setting_type, req_field)
                        ))
            
            # Validate select/radio options
            if setting_type in ("select", "radio") and "options" in setting:
                self._validate_options(setting["options"], f"{path}.options", result)
            
            # Validate range bounds
            if setting_type == "range":
                self._validate_range(setting, path, result)
    
    def _validate_options(self, options: list, path: str, result: SchemaResult):
        """Validate select/radio options array."""
        if not isinstance(options, list):
            result.issues.append(SchemaIssue(
                severity="critical",
                path=path,
                message="Options must be an array"
            ))
            return
        
        if len(options) < 2:
            result.issues.append(SchemaIssue(
                severity="minor",
                path=path,
                message="Select/radio should have at least 2 options"
            ))
        
        values_seen = set()
        for i, opt in enumerate(options):
            if not isinstance(opt, dict):
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}[{i}]",
                    message="Option must be an object with 'value' and 'label'"
                ))
                continue
            
            if "value" not in opt:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}[{i}].value",
                    message="Option missing 'value' field"
                ))
            elif opt["value"] in values_seen:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}[{i}].value",
                    message=f"Duplicate option value '{opt['value']}'"
                ))
            else:
                values_seen.add(opt["value"])
            
            if "label" not in opt:
                result.issues.append(SchemaIssue(
                    severity="major",
                    path=f"{path}[{i}].label",
                    message="Option missing 'label' field"
                ))
    
    def _validate_range(self, setting: dict, path: str, result: SchemaResult):
        """Validate range setting bounds."""
        min_val = setting.get("min")
        max_val = setting.get("max")
        step = setting.get("step")
        default = setting.get("default")
        
        if min_val is not None and max_val is not None:
            if min_val >= max_val:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=path,
                    message=f"Range min ({min_val}) must be less than max ({max_val})"
                ))
            
            if default is not None:
                if default < min_val or default > max_val:
                    result.issues.append(SchemaIssue(
                        severity="critical",
                        path=f"{path}.default",
                        message=f"Default value ({default}) is outside range [{min_val}, {max_val}]"
                    ))
    
    def _validate_blocks(self, blocks: list, result: SchemaResult):
        """Validate blocks array."""
        if not isinstance(blocks, list):
            result.issues.append(SchemaIssue(
                severity="critical",
                path="blocks",
                message="'blocks' must be an array"
            ))
            return
        
        block_types = set()
        for i, block in enumerate(blocks):
            path = f"blocks[{i}]"
            
            if "type" not in block:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}.type",
                    message="Block missing required 'type' field"
                ))
            else:
                if block["type"] in block_types:
                    result.issues.append(SchemaIssue(
                        severity="critical",
                        path=f"{path}.type",
                        message=f"Duplicate block type '{block['type']}'"
                    ))
                block_types.add(block["type"])
            
            if "name" not in block:
                result.issues.append(SchemaIssue(
                    severity="major",
                    path=f"{path}.name",
                    message="Block missing 'name' field"
                ))
            
            # Validate block settings
            if "settings" in block:
                self._validate_settings(block["settings"], f"{path}.settings", result)
    
    def _validate_presets(self, presets: list, schema: dict, result: SchemaResult):
        """Validate presets array."""
        if not presets:
            result.issues.append(SchemaIssue(
                severity="major",
                path="presets",
                message="No presets defined — section won't appear in 'Add section' menu",
                fix='Add "presets": [{"name": "Section Name"}]'
            ))
            return
        
        for i, preset in enumerate(presets):
            path = f"presets[{i}]"
            if "name" not in preset:
                result.issues.append(SchemaIssue(
                    severity="critical",
                    path=f"{path}.name",
                    message="Preset missing required 'name' field"
                ))
            
            # Validate preset blocks reference valid block types
            if "blocks" in preset:
                schema_block_types = {b["type"] for b in schema.get("blocks", []) if "type" in b}
                for j, block in enumerate(preset["blocks"]):
                    if isinstance(block, dict) and "type" in block:
                        if block["type"] not in schema_block_types:
                            result.issues.append(SchemaIssue(
                                severity="critical",
                                path=f"{path}.blocks[{j}].type",
                                message=f"Preset references block type '{block['type']}' not defined in blocks array"
                            ))
    
    def _check_id_uniqueness(self, schema: dict, result: SchemaResult):
        """Check that all setting IDs are unique within their scope."""
        # Section-level settings
        section_ids = set()
        for i, s in enumerate(schema.get("settings", [])):
            sid = s.get("id")
            if sid:
                if sid in section_ids:
                    result.issues.append(SchemaIssue(
                        severity="critical",
                        path=f"settings[{i}].id",
                        message=f"Duplicate setting ID '{sid}' in section settings"
                    ))
                section_ids.add(sid)
        
        # Block-level settings (per block type)
        for bi, block in enumerate(schema.get("blocks", [])):
            block_ids = set()
            for si, s in enumerate(block.get("settings", [])):
                sid = s.get("id")
                if sid:
                    if sid in block_ids:
                        result.issues.append(SchemaIssue(
                            severity="critical",
                            path=f"blocks[{bi}].settings[{si}].id",
                            message=f"Duplicate setting ID '{sid}' in block '{block.get('type', '?')}'"
                        ))
                    block_ids.add(sid)
    
    def _get_field_hint(self, setting_type: str, field: str) -> str:
        """Get a hint for a required field."""
        hints = {
            ("range", "min"): 'Add "min": 0',
            ("range", "max"): 'Add "max": 100',
            ("range", "step"): 'Add "step": 1',
            ("select", "options"): 'Add "options": [{"value": "opt1", "label": "Option 1"}]',
            ("radio", "options"): 'Add "options": [{"value": "opt1", "label": "Option 1"}]',
            ("video_url", "accept"): 'Add "accept": ["youtube", "vimeo"]',
        }
        return hints.get((setting_type, field), "")
