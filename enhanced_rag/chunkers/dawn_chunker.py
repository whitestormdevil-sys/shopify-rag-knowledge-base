#!/usr/bin/env python3
"""Deep Dawn theme chunker — creates rich, purpose-built chunks for every
Dawn file so code generation agents have perfect knowledge of the reference theme.

Creates chunks in multiple categories:
1. SECTION_FULL — complete section with schema analysis + dependency map
2. SECTION_SCHEMA — extracted schema definition with settings breakdown
3. SECTION_RENDER — the render/output portion (Liquid + HTML)
4. SNIPPET_FULL — complete snippet with usage context
5. TEMPLATE_JSON — template structure showing section arrangement
6. LAYOUT — layout files with content injection points
7. ASSET_CSS — CSS files with component/variable analysis
8. ASSET_JS — JS files with custom element/class analysis
9. CONFIG — theme settings schema + data
10. DAWN_ARCHITECTURE — high-level architecture docs (generated)
"""

import re
import json
from pathlib import Path
from typing import Optional


DAWN_PATH = Path(__file__).parent.parent.parent / "raw-docs" / "dawn-theme"


# ============ HELPERS ============

def extract_schema(liquid_content: str) -> Optional[dict]:
    """Extract {% schema %} JSON from a section file."""
    match = re.search(r'\{%[-\s]*schema\s*[-]?%\}(.*?)\{%[-\s]*endschema\s*[-]?%\}', 
                       liquid_content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            return None
    return None


def extract_render_calls(content: str) -> list[str]:
    """Find all {% render 'snippet-name' %} calls."""
    return re.findall(r"\{%[-\s]*render\s+['\"]([^'\"]+)['\"]", content)


def extract_section_calls(content: str) -> list[str]:
    """Find all {% section 'name' %} calls."""
    return re.findall(r"\{%[-\s]*section\s+['\"]([^'\"]+)['\"]", content)


def extract_stylesheet_tags(content: str) -> list[str]:
    """Find all {{ 'file.css' | asset_url | stylesheet_tag }}."""
    return re.findall(r"['\"]([^'\"]+\.css)['\"].*?(?:stylesheet_tag|asset_url)", content)


def extract_script_tags(content: str) -> list[str]:
    """Find all script/JS references."""
    return re.findall(r"['\"]([^'\"]+\.js)['\"].*?(?:script_tag|asset_url)", content)


def extract_liquid_objects(content: str) -> list[str]:
    """Find Shopify Liquid objects used (product, collection, cart, etc.)."""
    objects = set()
    # {{ object.property }}
    for m in re.findall(r'\{\{[-\s]*(\w+)\.', content):
        if m not in ('section', 'block', 'forloop', 'tablerow', 'paginate'):
            objects.add(m)
    # {% for item in object %}
    for m in re.findall(r'\{%[-\s]*for\s+\w+\s+in\s+(\w+)', content):
        if m not in ('section', 'block'):
            objects.add(m)
    # Direct assignments
    for m in re.findall(r'\{%[-\s]*assign\s+\w+\s*=\s*(\w+)\.', content):
        objects.add(m)
    return sorted(objects)


def extract_css_variables(content: str) -> list[str]:
    """Extract CSS custom properties defined."""
    return list(set(re.findall(r'(--\w[\w-]+)\s*:', content)))


def extract_css_classes(content: str) -> list[str]:
    """Extract CSS class names defined."""
    return list(set(re.findall(r'\.([a-zA-Z][\w-]+)\s*[\{,:]', content)))[:50]


def extract_js_classes(content: str) -> list[str]:
    """Extract JS class names and custom elements."""
    classes = re.findall(r'class\s+(\w+)', content)
    custom_elements = re.findall(r"customElements\.define\(['\"]([^'\"]+)['\"]", content)
    return classes + custom_elements


def analyze_schema_settings(schema: dict) -> dict:
    """Deep analysis of a section schema."""
    info = {
        "name": schema.get("name", "Unknown"),
        "tag": schema.get("tag", None),
        "class": schema.get("class", None),
        "limit": schema.get("limit", None),
        "max_blocks": schema.get("max_blocks", None),
        "settings_count": len(schema.get("settings", [])),
        "settings_types": [],
        "blocks": [],
        "presets": [],
        "enabled_on": schema.get("enabled_on", None),
        "disabled_on": schema.get("disabled_on", None),
    }
    
    # Analyze settings
    setting_types = {}
    for s in schema.get("settings", []):
        stype = s.get("type", "unknown")
        setting_types[stype] = setting_types.get(stype, 0) + 1
    info["settings_types"] = setting_types
    
    # Analyze blocks
    for block in schema.get("blocks", []):
        block_info = {
            "type": block.get("type", "unknown"),
            "name": block.get("name", "unknown"),
            "settings_count": len(block.get("settings", [])),
        }
        info["blocks"].append(block_info)
    
    # Presets
    for preset in schema.get("presets", []):
        info["presets"].append(preset.get("name", "unknown"))
    
    return info


def get_section_category(filename: str, schema: dict = None) -> str:
    """Categorize a section by its purpose."""
    name = filename.replace(".liquid", "").replace(".json", "")
    
    if name.startswith("main-"):
        page = name.replace("main-", "")
        if page in ("product", "featured-product"):
            return "product"
        elif page in ("collection-product-grid", "collection-banner", "list-collections"):
            return "collection"
        elif "cart" in page:
            return "cart"
        elif page in ("search",):
            return "search"
        elif page in ("blog", "article"):
            return "blog"
        elif page in ("account", "login", "register", "activate-account", "addresses", "order", "reset-password"):
            return "account"
        elif page in ("page",):
            return "page"
        elif page in ("404",):
            return "utility"
        elif "password" in page:
            return "utility"
        else:
            return "page"
    elif name in ("header", "header-group"):
        return "navigation"
    elif name in ("footer", "footer-group"):
        return "navigation"
    elif name in ("announcement-bar",):
        return "navigation"
    elif name in ("slideshow", "image-banner", "image-with-text", "video"):
        return "hero"
    elif name in ("featured-collection", "collection-list"):
        return "collection"
    elif name in ("featured-blog",):
        return "blog"
    elif name in ("rich-text", "multicolumn", "multirow", "collage", "custom-liquid"):
        return "content"
    elif name in ("collapsible-content",):
        return "faq"
    elif name in ("email-signup-banner", "newsletter"):
        return "marketing"
    elif name in ("contact-form",):
        return "form"
    elif name in ("related-products", "pickup-availability", "featured-product"):
        return "product"
    elif name in ("predictive-search",):
        return "search"
    elif "cart" in name:
        return "cart"
    elif name in ("apps", "page"):
        return "utility"
    else:
        return "general"


# ============ CHUNK GENERATORS ============

def chunk_section(filepath: Path) -> list[dict]:
    """Create multiple rich chunks for a section file."""
    chunks = []
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    section_name = filename.replace(".liquid", "").replace(".json", "")
    is_json = filepath.suffix == ".json"
    
    if is_json:
        # Section group JSON files (header-group.json, footer-group.json)
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = {}
        
        chunks.append({
            "text": f"# Dawn Section Group: {section_name}\n\n"
                    f"Type: Section Group (JSON)\n"
                    f"File: sections/{filename}\n\n"
                    f"```json\n{content}\n```\n\n"
                    f"Section groups define the order and type of sections "
                    f"that appear in a specific area (header/footer). They use "
                    f"the `type` and `order` fields to arrange sections.",
            "metadata": {
                "source": f"dawn-theme/sections/{filename}",
                "type": "section_group",
                "category": "dawn_theme",
                "subcategory": get_section_category(filename),
                "section_name": section_name,
                "file_type": "json",
            },
            "collection": "theme_patterns",
        })
        return chunks
    
    # Liquid section file
    schema = extract_schema(content)
    renders = extract_render_calls(content)
    stylesheets = extract_stylesheet_tags(content)
    scripts = extract_script_tags(content)
    liquid_objects = extract_liquid_objects(content)
    category = get_section_category(filename, schema)
    
    schema_info = analyze_schema_settings(schema) if schema else {}
    
    # --- CHUNK 1: Full Section Overview ---
    dep_text = ""
    if renders:
        dep_text += f"\n**Snippets used:** {', '.join(renders)}"
    if stylesheets:
        dep_text += f"\n**CSS files:** {', '.join(stylesheets)}"
    if scripts:
        dep_text += f"\n**JS files:** {', '.join(scripts)}"
    if liquid_objects:
        dep_text += f"\n**Liquid objects:** {', '.join(liquid_objects)}"
    
    schema_summary = ""
    if schema_info:
        schema_summary = (
            f"\n**Schema:** {schema_info.get('settings_count', 0)} settings, "
            f"{len(schema_info.get('blocks', []))} block types"
        )
        if schema_info.get("presets"):
            schema_summary += f"\n**Presets:** {', '.join(schema_info['presets'])}"
        if schema_info.get("settings_types"):
            schema_summary += f"\n**Setting types:** {', '.join(f'{k}({v})' for k,v in schema_info['settings_types'].items())}"
        if schema_info.get("blocks"):
            block_strs = [f"{b['type']}({b['settings_count']} settings)" for b in schema_info['blocks']]
            schema_summary += f"\n**Blocks:** {', '.join(block_strs)}"
        if schema_info.get("enabled_on"):
            schema_summary += f"\n**Enabled on:** {json.dumps(schema_info['enabled_on'])}"
        if schema_info.get("disabled_on"):
            schema_summary += f"\n**Disabled on:** {json.dumps(schema_info['disabled_on'])}"
    
    lines = content.count('\n') + 1
    
    overview = (
        f"# Dawn Section: {section_name}\n\n"
        f"**File:** `sections/{filename}` ({lines} lines)\n"
        f"**Category:** {category}\n"
        f"**Purpose:** {schema_info.get('name', section_name)} — Dawn's implementation of this section type\n"
        f"{schema_summary}\n{dep_text}\n\n"
        f"## Full Source Code\n\n"
        f"```liquid\n{content}\n```"
    )
    
    chunks.append({
        "text": overview,
        "metadata": {
            "source": f"dawn-theme/sections/{filename}",
            "type": "dawn_section_full",
            "category": "dawn_theme",
            "subcategory": category,
            "section_name": section_name,
            "file_type": "liquid",
            "line_count": lines,
            "dependencies": {
                "snippets": renders,
                "css": stylesheets,
                "js": scripts,
            },
            "liquid_objects": liquid_objects,
            "schema_settings_count": schema_info.get("settings_count", 0),
            "block_types": [b["type"] for b in schema_info.get("blocks", [])],
        },
        "collection": "code_examples",
    })
    
    # --- CHUNK 2: Schema Only (for agents that need to understand settings) ---
    if schema:
        schema_text = (
            f"# Dawn Section Schema: {section_name}\n\n"
            f"**Section:** `sections/{filename}`\n"
            f"**Name:** {schema.get('name', 'N/A')}\n\n"
            f"## Schema JSON\n\n"
            f"```json\n{json.dumps(schema, indent=2)}\n```\n\n"
            f"## Analysis\n"
            f"- **Settings:** {schema_info.get('settings_count', 0)} total\n"
            f"- **Setting types:** {json.dumps(schema_info.get('settings_types', {}))}\n"
            f"- **Blocks:** {len(schema_info.get('blocks', []))} types\n"
        )
        
        if schema_info.get("blocks"):
            schema_text += "\n### Block Types\n"
            for b in schema_info["blocks"]:
                schema_text += f"- `{b['type']}` — {b['name']} ({b['settings_count']} settings)\n"
        
        chunks.append({
            "text": schema_text,
            "metadata": {
                "source": f"dawn-theme/sections/{filename}",
                "type": "dawn_section_schema",
                "category": "dawn_theme",
                "subcategory": category,
                "section_name": section_name,
            },
            "collection": "theme_patterns",
        })
    
    # --- CHUNK 3: Large sections get split render portion ---
    if lines > 200:
        # Extract the render portion (everything before {% schema %})
        render_part = re.split(r'\{%[-\s]*schema', content)[0].strip()
        if len(render_part) > 500:
            chunks.append({
                "text": (
                    f"# Dawn Section Render: {section_name}\n\n"
                    f"**File:** `sections/{filename}` — Liquid/HTML rendering portion\n"
                    f"**Category:** {category}\n\n"
                    f"```liquid\n{render_part}\n```"
                ),
                "metadata": {
                    "source": f"dawn-theme/sections/{filename}",
                    "type": "dawn_section_render",
                    "category": "dawn_theme",
                    "subcategory": category,
                    "section_name": section_name,
                    "liquid_objects": liquid_objects,
                },
                "collection": "code_examples",
            })
    
    return chunks


def chunk_snippet(filepath: Path) -> list[dict]:
    """Create chunks for a snippet file."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    snippet_name = filename.replace(".liquid", "")
    
    # Find which sections use this snippet
    sections_dir = filepath.parent.parent / "sections"
    used_by = []
    for section_file in sections_dir.glob("*.liquid"):
        sec_content = section_file.read_text(encoding="utf-8", errors="replace")
        if f"'{snippet_name}'" in sec_content or f'"{snippet_name}"' in sec_content:
            used_by.append(section_file.stem)
    
    renders = extract_render_calls(content)
    liquid_objects = extract_liquid_objects(content)
    lines = content.count('\n') + 1
    
    usage_text = f"\n**Used by sections:** {', '.join(used_by)}" if used_by else ""
    sub_renders = f"\n**Sub-snippets:** {', '.join(renders)}" if renders else ""
    
    return [{
        "text": (
            f"# Dawn Snippet: {snippet_name}\n\n"
            f"**File:** `snippets/{filename}` ({lines} lines)\n"
            f"**Purpose:** Reusable component used across Dawn sections"
            f"{usage_text}{sub_renders}\n"
            f"**Liquid objects:** {', '.join(liquid_objects) if liquid_objects else 'none'}\n\n"
            f"## Full Source Code\n\n"
            f"```liquid\n{content}\n```"
        ),
        "metadata": {
            "source": f"dawn-theme/snippets/{filename}",
            "type": "dawn_snippet",
            "category": "dawn_theme",
            "subcategory": "snippet",
            "snippet_name": snippet_name,
            "used_by": used_by,
            "liquid_objects": liquid_objects,
            "line_count": lines,
        },
        "collection": "code_examples",
    }]


def chunk_template(filepath: Path) -> list[dict]:
    """Create chunks for template JSON files."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    template_name = filename.replace(".json", "").replace(".liquid", "")
    
    if filepath.suffix == ".json":
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = {}
        
        # Extract section references
        sections_used = []
        if "sections" in data:
            for key, sec in data["sections"].items():
                sections_used.append(f"{key}: {sec.get('type', 'unknown')}")
        
        order = data.get("order", [])
        
        return [{
            "text": (
                f"# Dawn Template: {template_name}\n\n"
                f"**File:** `templates/{filename}`\n"
                f"**Layout:** {data.get('layout', 'theme')}\n"
                f"**Section order:** {', '.join(order)}\n\n"
                f"## Sections\n"
                + "\n".join(f"- `{s}`" for s in sections_used) + "\n\n"
                f"## Full JSON\n\n"
                f"```json\n{content}\n```\n\n"
                f"This template defines which sections appear on the "
                f"`{template_name}` page and their order. In OS2.0, "
                f"templates are JSON files that reference sections."
            ),
            "metadata": {
                "source": f"dawn-theme/templates/{filename}",
                "type": "dawn_template",
                "category": "dawn_theme",
                "subcategory": "template",
                "template_name": template_name,
                "sections_used": [s.split(": ")[-1] for s in sections_used],
                "section_order": order,
            },
            "collection": "theme_patterns",
        }]
    else:
        # .liquid template (gift_card.liquid)
        return [{
            "text": (
                f"# Dawn Template: {template_name}\n\n"
                f"**File:** `templates/{filename}`\n"
                f"**Type:** Liquid template (not JSON)\n\n"
                f"```liquid\n{content}\n```"
            ),
            "metadata": {
                "source": f"dawn-theme/templates/{filename}",
                "type": "dawn_template_liquid",
                "category": "dawn_theme",
                "subcategory": "template",
            },
            "collection": "code_examples",
        }]


def chunk_customer_template(filepath: Path) -> list[dict]:
    """Chunk customer account templates."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    
    return [{
        "text": (
            f"# Dawn Customer Template: {filename}\n\n"
            f"**File:** `templates/customers/{filename}`\n\n"
            f"```json\n{content}\n```"
        ),
        "metadata": {
            "source": f"dawn-theme/templates/customers/{filename}",
            "type": "dawn_template",
            "category": "dawn_theme",
            "subcategory": "account",
        },
        "collection": "theme_patterns",
    }]


def chunk_layout(filepath: Path) -> list[dict]:
    """Create chunks for layout files."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    layout_name = filename.replace(".liquid", "")
    
    # Find content injection points
    content_tags = re.findall(r'\{\{[-\s]*(content_for_\w+)[-\s]*\}\}', content)
    section_calls = extract_section_calls(content)
    renders = extract_render_calls(content)
    
    return [{
        "text": (
            f"# Dawn Layout: {layout_name}\n\n"
            f"**File:** `layout/{filename}`\n"
            f"**Content injection points:** {', '.join(content_tags)}\n"
            f"**Section calls:** {', '.join(section_calls) if section_calls else 'none'}\n"
            f"**Snippets used:** {', '.join(renders) if renders else 'none'}\n\n"
            f"## Full Source Code\n\n"
            f"```liquid\n{content}\n```\n\n"
            f"The layout file is the outermost wrapper. `content_for_header` "
            f"injects Shopify's required scripts/analytics. `content_for_layout` "
            f"injects the template content (sections)."
        ),
        "metadata": {
            "source": f"dawn-theme/layout/{filename}",
            "type": "dawn_layout",
            "category": "dawn_theme",
            "subcategory": "layout",
            "content_tags": content_tags,
        },
        "collection": "theme_patterns",
    }]


def chunk_asset_css(filepath: Path) -> list[dict]:
    """Create chunks for CSS asset files."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    lines = content.count('\n') + 1
    
    variables = extract_css_variables(content)
    classes = extract_css_classes(content)
    
    # Determine what section/component this CSS belongs to
    related_to = filename.replace(".css", "").replace("section-", "").replace("component-", "")
    
    return [{
        "text": (
            f"# Dawn CSS: {filename}\n\n"
            f"**File:** `assets/{filename}` ({lines} lines)\n"
            f"**Related to:** {related_to}\n"
            f"**CSS variables defined:** {len(variables)}\n"
            f"**Classes defined:** {len(classes)}\n\n"
            + (f"**Key variables:** {', '.join(variables[:20])}\n\n" if variables else "")
            + (f"**Key classes:** {', '.join(classes[:30])}\n\n" if classes else "")
            + f"## Full CSS\n\n"
            f"```css\n{content}\n```"
        ),
        "metadata": {
            "source": f"dawn-theme/assets/{filename}",
            "type": "dawn_css",
            "category": "dawn_theme",
            "subcategory": "css",
            "related_to": related_to,
            "css_variables": variables[:20],
            "css_classes": classes[:30],
            "line_count": lines,
        },
        "collection": "code_examples",
    }]


def chunk_asset_js(filepath: Path) -> list[dict]:
    """Create chunks for JS asset files."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    lines = content.count('\n') + 1
    
    classes = extract_js_classes(content)
    
    return [{
        "text": (
            f"# Dawn JavaScript: {filename}\n\n"
            f"**File:** `assets/{filename}` ({lines} lines)\n"
            f"**Classes/Custom Elements:** {', '.join(classes) if classes else 'none'}\n\n"
            f"## Full Source Code\n\n"
            f"```javascript\n{content}\n```"
        ),
        "metadata": {
            "source": f"dawn-theme/assets/{filename}",
            "type": "dawn_js",
            "category": "dawn_theme",
            "subcategory": "javascript",
            "js_classes": classes,
            "line_count": lines,
        },
        "collection": "code_examples",
    }]


def chunk_config(filepath: Path) -> list[dict]:
    """Create chunks for config files."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {}
    
    if filename == "settings_schema.json":
        # Theme settings schema — defines what appears in Theme Editor > Theme Settings
        sections_summary = []
        for section in data if isinstance(data, list) else []:
            if isinstance(section, dict) and "name" in section:
                settings_count = len(section.get("settings", []))
                sections_summary.append(f"{section['name']} ({settings_count} settings)")
        
        return [{
            "text": (
                f"# Dawn Config: settings_schema.json\n\n"
                f"**File:** `config/settings_schema.json`\n"
                f"**Purpose:** Defines global theme settings in Theme Editor\n\n"
                f"## Setting Groups\n"
                + "\n".join(f"- {s}" for s in sections_summary) + "\n\n"
                f"## Full JSON\n\n"
                f"```json\n{content}\n```\n\n"
                f"This file defines the global settings available under "
                f"Theme Settings in the Shopify Theme Editor. Each group "
                f"appears as a section with its own settings."
            ),
            "metadata": {
                "source": f"dawn-theme/config/{filename}",
                "type": "dawn_config_schema",
                "category": "dawn_theme",
                "subcategory": "config",
            },
            "collection": "theme_patterns",
        }]
    else:
        # settings_data.json — actual values
        return [{
            "text": (
                f"# Dawn Config: settings_data.json\n\n"
                f"**File:** `config/settings_data.json`\n"
                f"**Purpose:** Default theme setting values\n\n"
                f"```json\n{content[:5000]}\n```\n\n"
                f"This file stores the actual values for theme settings. "
                f"When a merchant customizes their theme, changes are written here."
            ),
            "metadata": {
                "source": f"dawn-theme/config/{filename}",
                "type": "dawn_config_data",
                "category": "dawn_theme",
                "subcategory": "config",
            },
            "collection": "theme_patterns",
        }]


def generate_architecture_chunks() -> list[dict]:
    """Generate high-level Dawn architecture documentation chunks."""
    dawn = DAWN_PATH
    
    # Count files
    sections = list((dawn / "sections").glob("*.liquid"))
    section_groups = list((dawn / "sections").glob("*.json"))
    snippets = list((dawn / "snippets").glob("*.liquid"))
    templates_json = list((dawn / "templates").glob("*.json"))
    templates_liquid = list((dawn / "templates").glob("*.liquid"))
    customer_templates = list((dawn / "templates" / "customers").glob("*"))
    css_files = list((dawn / "assets").glob("*.css"))
    js_files = list((dawn / "assets").glob("*.js"))
    
    # Build dependency map
    section_deps = {}
    for sf in sections:
        content = sf.read_text(encoding="utf-8", errors="replace")
        renders = extract_render_calls(content)
        css = extract_stylesheet_tags(content)
        js = extract_script_tags(content)
        if renders or css or js:
            section_deps[sf.stem] = {"snippets": renders, "css": css, "js": js}
    
    # Template → section mapping
    template_sections = {}
    for tf in templates_json:
        try:
            data = json.loads(tf.read_text(encoding="utf-8", errors="replace"))
            secs = [s.get("type", "unknown") for s in data.get("sections", {}).values()]
            template_sections[tf.stem] = secs
        except (json.JSONDecodeError, AttributeError):
            pass
    
    chunks = []
    
    # Architecture overview
    arch_text = f"""# Dawn Theme Architecture Overview

**Dawn** is Shopify's official reference theme (OS 2.0). It demonstrates all best practices for Shopify theme development.

## File Statistics
- **Sections:** {len(sections)} Liquid + {len(section_groups)} JSON groups
- **Snippets:** {len(snippets)} reusable components
- **Templates:** {len(templates_json)} JSON + {len(templates_liquid)} Liquid + {len(customer_templates)} customer
- **CSS:** {len(css_files)} stylesheets
- **JS:** {len(js_files)} scripts
- **Layouts:** 2 (theme.liquid, password.liquid)
- **Config:** settings_schema.json + settings_data.json

## Template → Section Mapping
"""
    for tmpl, secs in sorted(template_sections.items()):
        arch_text += f"- **{tmpl}**: {', '.join(secs)}\n"
    
    arch_text += f"""
## Section Dependency Map
"""
    for sec, deps in sorted(section_deps.items()):
        dep_parts = []
        if deps["snippets"]:
            dep_parts.append(f"snippets: {', '.join(deps['snippets'])}")
        if deps["css"]:
            dep_parts.append(f"css: {', '.join(deps['css'])}")
        if deps["js"]:
            dep_parts.append(f"js: {', '.join(deps['js'])}")
        arch_text += f"- **{sec}**: {' | '.join(dep_parts)}\n"
    
    arch_text += """
## Key Patterns in Dawn
1. **OS2.0 JSON Templates** — All page templates are JSON, referencing sections
2. **Section Groups** — Header and footer use section groups (JSON) for modularity
3. **Scoped CSS** — Each section/component has its own CSS file, loaded conditionally
4. **Custom Elements** — JS uses Web Components (customElements.define) for interactivity
5. **Responsive Design** — Mobile-first CSS with media queries
6. **Accessibility** — ARIA attributes, semantic HTML, keyboard navigation
7. **Performance** — Lazy loading, deferred scripts, minimal JS
8. **Schema-driven** — Every section has a {% schema %} with typed settings
"""
    
    chunks.append({
        "text": arch_text,
        "metadata": {
            "source": "dawn-theme/ARCHITECTURE.md",
            "type": "dawn_architecture",
            "category": "dawn_theme",
            "subcategory": "architecture",
        },
        "collection": "theme_patterns",
    })
    
    # Section categories overview
    categories = {}
    for sf in sections:
        cat = get_section_category(sf.name)
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(sf.stem)
    
    cat_text = "# Dawn Sections by Category\n\n"
    for cat, secs in sorted(categories.items()):
        cat_text += f"## {cat.title()}\n"
        for s in sorted(secs):
            cat_text += f"- `sections/{s}.liquid`\n"
        cat_text += "\n"
    
    cat_text += """
## How to Use This for Code Generation
When generating a new section:
1. Look at Dawn's implementation of the same category
2. Follow the same schema patterns (setting types, blocks)
3. Use the same snippet dependencies where applicable
4. Follow Dawn's CSS naming conventions
5. Use the same custom element patterns for JS
"""
    
    chunks.append({
        "text": cat_text,
        "metadata": {
            "source": "dawn-theme/SECTION_CATEGORIES.md",
            "type": "dawn_section_categories",
            "category": "dawn_theme",
            "subcategory": "architecture",
        },
        "collection": "theme_patterns",
    })
    
    return chunks


# ============ MAIN CHUNKING FUNCTION ============

def chunk_dawn_theme(dawn_path: str = None) -> list[dict]:
    """Chunk the entire Dawn theme into rich, purpose-built chunks."""
    dawn = Path(dawn_path) if dawn_path else DAWN_PATH
    
    if not dawn.exists():
        raise FileNotFoundError(f"Dawn theme not found at {dawn}")
    
    all_chunks = []
    
    print(f"📁 Chunking Dawn theme from {dawn}")
    
    # 1. Architecture docs (generated)
    print("  📐 Generating architecture docs...")
    all_chunks.extend(generate_architecture_chunks())
    
    # 2. Sections
    print("  📦 Chunking sections...")
    for f in sorted((dawn / "sections").glob("*")):
        if f.suffix in (".liquid", ".json"):
            all_chunks.extend(chunk_section(f))
    
    # 3. Snippets
    print("  🧩 Chunking snippets...")
    for f in sorted((dawn / "snippets").glob("*.liquid")):
        all_chunks.extend(chunk_snippet(f))
    
    # 4. Templates
    print("  📄 Chunking templates...")
    for f in sorted((dawn / "templates").glob("*")):
        if f.is_file():
            all_chunks.extend(chunk_template(f))
    if (dawn / "templates" / "customers").exists():
        for f in sorted((dawn / "templates" / "customers").glob("*")):
            all_chunks.extend(chunk_customer_template(f))
    
    # 5. Layouts
    print("  🏗️ Chunking layouts...")
    for f in sorted((dawn / "layout").glob("*.liquid")):
        all_chunks.extend(chunk_layout(f))
    
    # 6. CSS assets
    print("  🎨 Chunking CSS assets...")
    for f in sorted((dawn / "assets").glob("*.css")):
        all_chunks.extend(chunk_asset_css(f))
    
    # 7. JS assets
    print("  ⚡ Chunking JS assets...")
    for f in sorted((dawn / "assets").glob("*.js")):
        all_chunks.extend(chunk_asset_js(f))
    
    # 8. Config
    print("  ⚙️ Chunking config...")
    for f in sorted((dawn / "config").glob("*.json")):
        all_chunks.extend(chunk_config(f))
    
    # Stats
    collections = {}
    for c in all_chunks:
        col = c.get("collection", "unknown")
        collections[col] = collections.get(col, 0) + 1
    
    print(f"\n✅ Total Dawn chunks: {len(all_chunks)}")
    for col, count in sorted(collections.items()):
        print(f"  → {col}: {count}")
    
    return all_chunks


if __name__ == "__main__":
    chunks = chunk_dawn_theme()
    
    # Save to JSON for inspection
    output = Path(__file__).parent.parent.parent / "dawn_chunks.json"
    import json
    with open(output, "w") as f:
        json.dump(chunks, f, indent=2, default=str)
    print(f"\n💾 Saved to {output}")
