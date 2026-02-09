#!/usr/bin/env python3
"""Smart Chunker — Code-aware, hierarchical, metadata-rich chunking for Shopify docs.

Produces parent chunks (large context) and child chunks (precise retrieval).
Keeps code blocks intact. Tags every chunk with rich metadata.
"""

import re
import hashlib
import json
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Chunk:
    id: str
    text: str
    parent_id: Optional[str]  # None for parent chunks
    chunk_type: str  # "parent" | "child"
    content_type: str  # "documentation" | "code_example" | "liquid_reference" | "api_reference" | "pattern" | "troubleshooting"
    file_path: str
    file_name: str
    file_type: str
    category: str
    collection: str  # Which Qdrant collection this goes into
    source_url: str
    topics: list = field(default_factory=list)
    related_objects: list = field(default_factory=list)
    related_filters: list = field(default_factory=list)
    complexity: str = "basic"  # basic | intermediate | advanced
    chunk_index: int = 0
    char_count: int = 0


# ============ SHOPIFY ENTITY DETECTION ============

LIQUID_OBJECTS = {
    "product", "collection", "cart", "shop", "customer", "order", "variant",
    "image", "metafield", "page", "blog", "article", "comment", "link",
    "linklist", "section", "block", "settings", "template", "theme",
    "request", "content_for_header", "content_for_layout", "form",
    "paginate", "search", "tablerow", "forloop", "address", "company",
    "discount", "fulfillment", "gift_card", "line_item", "money",
    "policy", "shipping_method", "store_availability", "tax_line",
    "transaction", "video", "media", "model", "predictive_search",
    "recommendations", "color", "font", "filter", "filter_value",
    "country", "currency", "locale", "market", "selling_plan",
    "selling_plan_allocation", "selling_plan_group", "quantity_rule",
    "company_location", "company_address", "discount_allocation",
    "discount_application", "unit_price_measurement", "video_source",
    "model_source", "localization",
}

LIQUID_FILTERS = {
    "asset_url", "image_url", "image_tag", "stylesheet_tag", "script_tag",
    "money", "money_with_currency", "money_without_trailing_zeros",
    "money_without_currency", "link_to", "link_to_type", "link_to_vendor",
    "url_for_type", "url_for_vendor", "within", "pluralize",
    "customer_login_link", "customer_logout_link", "customer_register_link",
    "img_url", "asset_img_url", "file_url", "file_img_url",
    "shopify_asset_url", "global_asset_url", "payment_type_img_url",
    "t", "weight_with_unit", "format_address", "highlight",
    "metafield_tag", "metafield_text", "external_video_tag",
    "external_video_url", "model_viewer_tag", "video_tag", "media_tag",
    "color_to_rgb", "color_to_hsl", "color_to_hex", "color_extract",
    "color_brightness", "color_modify", "color_lighten", "color_darken",
    "color_saturate", "color_desaturate", "color_mix",
    "font_modify", "font_face", "font_url",
    "json", "date", "default", "escape", "strip_html", "newline_to_br",
    "abs", "append", "at_least", "at_most", "capitalize", "ceil",
    "compact", "concat", "divided_by", "downcase", "first", "floor",
    "join", "last", "lstrip", "map", "minus", "modulo", "plus",
    "prepend", "remove", "remove_first", "replace", "replace_first",
    "reverse", "round", "rstrip", "size", "slice", "sort",
    "sort_natural", "split", "strip", "strip_newlines", "times",
    "truncate", "truncatewords", "uniq", "upcase", "url_decode",
    "url_encode", "where", "escape_once",
}

LIQUID_TAGS = {
    "if", "elsif", "else", "unless", "case", "when", "for", "break",
    "continue", "cycle", "tablerow", "assign", "capture", "increment",
    "decrement", "echo", "liquid", "raw", "render", "include",
    "section", "sections", "layout", "comment", "form", "paginate",
    "style", "javascript", "schema",
}

SHOPIFY_APIS = {
    "admin_rest", "admin_graphql", "storefront", "ajax_api",
    "section_rendering", "cart_api", "product_api", "predictive_search",
    "webhooks", "functions", "checkout_extensions", "app_bridge",
    "web_pixels", "customer_events", "bulk_operations", "multipass",
}


def detect_entities(text: str) -> dict:
    """Detect Shopify-specific entities in text."""
    text_lower = text.lower()
    
    found_objects = [obj for obj in LIQUID_OBJECTS if obj in text_lower or obj.replace("_", ".") in text_lower]
    found_filters = [f for f in LIQUID_FILTERS if f" {f}" in text_lower or f"|{f}" in text_lower or f"| {f}" in text_lower]
    found_tags = [t for t in LIQUID_TAGS if f"{{% {t}" in text_lower or f"{{%- {t}" in text_lower]
    
    topics = list(set(found_objects + found_filters + found_tags))
    
    return {
        "objects": found_objects[:10],
        "filters": found_filters[:10],
        "tags": found_tags[:5],
        "topics": topics[:15],
    }


def detect_complexity(text: str) -> str:
    """Estimate complexity of content."""
    indicators = {
        "advanced": ["graphql", "mutation", "bulk operation", "webhook", "function", "metaobject",
                     "selling_plan", "checkout extension", "app bridge", "multipass"],
        "intermediate": ["ajax", "section rendering", "schema", "metafield", "paginate",
                        "customer account", "predictive search", "variant picker"],
    }
    text_lower = text.lower()
    for level, keywords in indicators.items():
        if any(kw in text_lower for kw in keywords):
            return level
    return "basic"


# ============ COLLECTION ROUTING ============

COLLECTION_RULES = {
    "liquid_reference": {
        "categories": ["liquid-docs", "liquid-objects", "liquid-filters-tags"],
        "path_patterns": [r"liquid"],
    },
    "code_examples": {
        "categories": ["dawn-theme", "shopify-repos"],
        "file_types": [".liquid", ".js", ".css", ".scss"],
    },
    "theme_patterns": {
        "categories": ["theme-patterns", "patterns-best-practices", "json-schemas", 
                       "accessibility", "performance", "seo"],
    },
    "api_reference": {
        "categories": ["admin-api", "storefront-api", "ajax-api", "webhooks",
                       "functions-docs", "checkout-docs", "app-bridge-docs",
                       "cli-docs", "hydrogen-docs", "bulk-operations",
                       "customer-events", "multipass", "auth",
                       "ajax-cart-api", "auth-oauth", "subscriptions-docs",
                       "pixels-analytics", "editor-api"],
    },
    "troubleshooting": {
        "categories": ["gotchas", "community"],
    },
    "best_practices": {
        "categories": ["review-checklists", "changelog", "tutorials",
                       "polaris-docs", "theme-app-extensions", "admin-extensions",
                       "markets", "b2b", "payments", "flow", "subscriptions",
                       "discounts", "fulfillment", "pos", "migrations",
                       "email-templates", "metaobjects", "app-proxy",
                       "cdn-images", "perf-best-practices", "flow-docs",
                       "markets-i18n"],
    },
    "theme_patterns": {
        "categories": ["theme-patterns", "patterns-best-practices", "json-schemas",
                       "accessibility", "performance", "seo",
                       "os2-sections", "theme-app-ext", "css-styling"],
    },
}


def route_to_collection(category: str, file_type: str, file_path: str) -> str:
    """Determine which Qdrant collection a chunk belongs to."""
    for collection, rules in COLLECTION_RULES.items():
        if "categories" in rules and category in rules["categories"]:
            return collection
        if "file_types" in rules and file_type in rules["file_types"]:
            return collection
        if "path_patterns" in rules:
            for pattern in rules["path_patterns"]:
                if re.search(pattern, file_path, re.IGNORECASE):
                    return collection
    return "best_practices"  # default


def detect_content_type(text: str, file_type: str, category: str) -> str:
    """Classify content type of a chunk."""
    code_indicators = text.count("{%") + text.count("{{") + text.count("```")
    
    if file_type in (".liquid", ".js", ".css", ".scss", ".ts", ".tsx", ".rb"):
        return "code_example"
    if category in ("liquid-docs", "liquid-objects", "liquid-filters-tags"):
        return "liquid_reference"
    if category in ("admin-api", "storefront-api", "ajax-api", "webhooks", "functions-docs",
                     "ajax-cart-api", "auth-oauth", "subscriptions-docs", "pixels-analytics", "editor-api"):
        return "api_reference"
    if category in ("gotchas", "community"):
        return "troubleshooting"
    if category in ("theme-patterns", "patterns-best-practices", "seo", "performance",
                     "os2-sections", "theme-app-ext", "css-styling"):
        return "pattern"
    if code_indicators > 5:
        return "code_example"
    return "documentation"


# ============ SMART CHUNKING ============

def extract_code_blocks(text: str) -> list:
    """Extract code blocks with surrounding context."""
    blocks = []
    # Markdown fenced code blocks
    pattern = r'((?:.*\n){0,3})(```[\w]*\n.*?```)((?:\n.*){0,3})'
    for match in re.finditer(pattern, text, re.DOTALL):
        context_before = match.group(1).strip()
        code = match.group(2).strip()
        context_after = match.group(3).strip()
        full_block = f"{context_before}\n{code}\n{context_after}".strip()
        blocks.append(full_block)
    
    # Liquid blocks ({% schema %}...{% endschema %}, etc.)
    liquid_blocks = re.findall(
        r'(\{%-?\s*(?:schema|javascript|style)\s*-?%\}.*?\{%-?\s*end(?:schema|javascript|style)\s*-?%\})',
        text, re.DOTALL
    )
    blocks.extend(liquid_blocks)
    
    return blocks


def extract_source_url(content: str) -> str:
    """Extract source URL from frontmatter."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            for line in content[3:end].split("\n"):
                if line.strip().startswith("source:"):
                    return line.split("source:", 1)[1].strip()
    return ""


def smart_chunk_text(text: str, parent_size: int = 2000, child_size: int = 500, 
                     overlap: int = 100) -> list:
    """
    Hierarchical chunking:
    - Parent chunks: 2000 chars (large context)
    - Child chunks: 500 chars (precise retrieval)
    - Code blocks stay intact
    """
    chunks = []
    
    # Split by major sections (## headers or double newlines)
    sections = re.split(r'\n(?=## |\n\n)', text)
    
    current_parent = ""
    parent_idx = 0
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        # If adding this section exceeds parent size, flush
        if len(current_parent) + len(section) > parent_size and current_parent:
            # Create parent chunk
            parent_id = hashlib.md5(f"parent:{parent_idx}:{current_parent[:100]}".encode()).hexdigest()
            chunks.append({
                "text": current_parent,
                "chunk_type": "parent",
                "parent_id": None,
                "parent_ref": parent_id,
                "chunk_index": parent_idx,
            })
            
            # Create child chunks from this parent
            child_texts = _split_into_children(current_parent, child_size, overlap)
            for ci, child_text in enumerate(child_texts):
                chunks.append({
                    "text": child_text,
                    "chunk_type": "child",
                    "parent_id": parent_id,
                    "parent_ref": None,
                    "chunk_index": ci,
                })
            
            current_parent = section
            parent_idx += 1
        else:
            current_parent += "\n\n" + section if current_parent else section
    
    # Flush remaining
    if current_parent.strip():
        parent_id = hashlib.md5(f"parent:{parent_idx}:{current_parent[:100]}".encode()).hexdigest()
        chunks.append({
            "text": current_parent,
            "chunk_type": "parent",
            "parent_id": None,
            "parent_ref": parent_id,
            "chunk_index": parent_idx,
        })
        child_texts = _split_into_children(current_parent, child_size, overlap)
        for ci, child_text in enumerate(child_texts):
            chunks.append({
                "text": child_text,
                "chunk_type": "child",
                "parent_id": parent_id,
                "parent_ref": None,
                "chunk_index": ci,
            })
    
    return chunks


def _split_into_children(text: str, max_size: int, overlap: int) -> list:
    """Split text into child chunks, respecting code blocks and paragraphs."""
    if len(text) <= max_size:
        return [text]
    
    children = []
    # Try to split on paragraph boundaries
    paragraphs = re.split(r'\n\n+', text)
    
    current = ""
    for para in paragraphs:
        # If this paragraph contains a code block, keep it intact
        if "```" in para or "{%" in para:
            if current:
                if len(current) + len(para) <= max_size * 1.5:  # Allow some overflow for code
                    current += "\n\n" + para
                    continue
                else:
                    children.append(current.strip())
                    current = para
                    continue
        
        if len(current) + len(para) > max_size and current:
            children.append(current.strip())
            # Overlap: keep last bit
            lines = current.split("\n")
            overlap_text = "\n".join(lines[-2:]) if len(lines) > 2 else ""
            current = overlap_text + "\n\n" + para if overlap_text else para
        else:
            current += "\n\n" + para if current else para
    
    if current.strip():
        children.append(current.strip())
    
    # Filter out tiny chunks
    children = [c for c in children if len(c.strip()) >= 30]
    
    return children


def smart_chunk_code_file(text: str, file_type: str) -> list:
    """Chunk source code files intelligently."""
    chunks = []
    
    if file_type == ".liquid":
        # Split by Liquid sections/blocks
        parts = re.split(r'(\{%-?\s*(?:schema|javascript|style|section|comment)\s*-?%\})', text)
        current = ""
        idx = 0
        for part in parts:
            if len(current) + len(part) > 1500 and current:
                chunk_id = hashlib.md5(f"code:{idx}:{current[:100]}".encode()).hexdigest()
                chunks.append({
                    "text": current.strip(),
                    "chunk_type": "child",
                    "parent_id": None,
                    "parent_ref": None,
                    "chunk_index": idx,
                })
                current = part
                idx += 1
            else:
                current += part
        if current.strip():
            chunks.append({
                "text": current.strip(),
                "chunk_type": "child",
                "parent_id": None,
                "parent_ref": None,
                "chunk_index": idx,
            })
    else:
        # For JS/CSS/etc, split by function/class boundaries
        boundaries = re.split(r'\n(?=(?:function |class |const |export |module\.))', text)
        idx = 0
        for block in boundaries:
            if len(block.strip()) < 30:
                continue
            # Further split if too large
            if len(block) > 1500:
                sub_chunks = _split_into_children(block, 800, 100)
                for sc in sub_chunks:
                    chunks.append({
                        "text": sc,
                        "chunk_type": "child",
                        "parent_id": None,
                        "parent_ref": None,
                        "chunk_index": idx,
                    })
                    idx += 1
            else:
                chunks.append({
                    "text": block.strip(),
                    "chunk_type": "child",
                    "parent_id": None,
                    "parent_ref": None,
                    "chunk_index": idx,
                })
                idx += 1
    
    return chunks


# ============ MAIN PROCESSING ============

def process_file(filepath: Path, base_dir: Path) -> list:
    """Process a single file into smart chunks with rich metadata."""
    # Read file
    content = None
    for enc in ["utf-8", "latin-1", "cp1252"]:
        try:
            content = filepath.read_text(encoding=enc)
            break
        except (UnicodeDecodeError, ValueError):
            continue
    
    if not content or len(content.strip()) < 30:
        return []
    
    # File metadata
    relative = filepath.relative_to(base_dir)
    category = relative.parts[0] if len(relative.parts) > 0 else "uncategorized"
    file_type = filepath.suffix.lower()
    source_url = extract_source_url(content)
    
    # Route to collection
    collection = route_to_collection(category, file_type, str(relative))
    content_type = detect_content_type(content, file_type, category)
    
    # Choose chunking strategy
    if file_type in (".liquid", ".js", ".ts", ".tsx", ".css", ".scss", ".rb"):
        raw_chunks = smart_chunk_code_file(content, file_type)
    else:
        raw_chunks = smart_chunk_text(content)
    
    # Enrich each chunk with metadata
    result = []
    for raw in raw_chunks:
        text = raw["text"]
        if len(text.strip()) < 30:
            continue
        
        entities = detect_entities(text)
        complexity = detect_complexity(text)
        
        chunk_id = hashlib.md5(
            f"{filepath}:{raw['chunk_index']}:{text[:100]}".encode()
        ).hexdigest()
        
        chunk = Chunk(
            id=chunk_id,
            text=text,
            parent_id=raw.get("parent_id"),
            chunk_type=raw["chunk_type"],
            content_type=content_type,
            file_path=str(relative),
            file_name=filepath.name,
            file_type=file_type,
            category=category,
            collection=collection,
            source_url=source_url,
            topics=entities["topics"],
            related_objects=entities["objects"],
            related_filters=entities["filters"],
            complexity=complexity,
            chunk_index=raw["chunk_index"],
            char_count=len(text),
        )
        result.append(chunk)
    
    return result
