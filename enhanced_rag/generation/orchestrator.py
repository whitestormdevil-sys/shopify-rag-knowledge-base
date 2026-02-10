"""
ShopifyAI Pipeline Orchestrator — Wires RAG, prompts, models, and validators together.

The FULL pipeline:
  User → Router → Architect → RAG → Builder×N → Validators → Critic → Assembler → Output

Each stage uses the correct model, injects RAG context where needed, and tracks costs.
"""

import json
import logging
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field

# Internal imports
from .llm_client import LLMClient, LLMResponse
from .parser.output_parser import ThemeOutputParser, ThemeDiffParser
from .parser.theme_file import ThemeFile
from .validator.liquid_validator import LiquidValidator
from .validator.schema_validator import SchemaValidator

# RAG search engine
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from search.engine import EnhancedSearchEngine

logger = logging.getLogger(__name__)


# ── Model configs (from model_architecture.py — kept private) ───────────────

MODELS = {
    "router":    {"model_id": "anthropic.claude-haiku-4-5-20251001-v1:0",    "max_tokens": 4096,  "thinking": False, "budget": 0,     "temp": 0.3},
    "architect": {"model_id": "anthropic.claude-sonnet-4-5-20250929-v1:0",   "max_tokens": 16384, "thinking": True,  "budget": 10000, "temp": 1.0},
    "builder":   {"model_id": "anthropic.claude-sonnet-4-5-20250929-v1:0",   "max_tokens": 16384, "thinking": False, "budget": 0,     "temp": 0.4},
    "critic":    {"model_id": "anthropic.claude-opus-4-6-v1",                "max_tokens": 8192,  "thinking": True,  "budget": 16000, "temp": 1.0},
    "assembler": {"model_id": "anthropic.claude-haiku-4-5-20251001-v1:0",    "max_tokens": 4096,  "thinking": False, "budget": 0,     "temp": 0.3},
    "iterator":  {"model_id": "anthropic.claude-sonnet-4-5-20250929-v1:0",   "max_tokens": 16384, "thinking": True,  "budget": 10000, "temp": 1.0},
}


# ── System prompts loaded from private repo (or inline fallback) ────────────

def _load_prompt(role: str) -> str:
    """Load system prompt. Tries private repo first, falls back to inline prompts."""
    private_repo = Path.home() / "Documents/ShopifyAI/shopifyai-prompts/prompts/model_architecture.py"
    if private_repo.exists():
        # Import from private repo
        import importlib.util
        spec = importlib.util.spec_from_file_location("model_arch", str(private_repo))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.get_system_prompt(role)
    else:
        # Fallback: use the stage prompts from public repo
        from .prompts.intent_parser import INTENT_PARSER_SYSTEM
        from .prompts.section_planner import SECTION_PLANNER_SYSTEM
        from .prompts.section_generator import SECTION_GENERATOR_SYSTEM
        from .prompts.section_verifier import SECTION_VERIFIER_SYSTEM
        from .prompts.iteration_handler import ITERATION_HANDLER_SYSTEM
        fallbacks = {
            "router": INTENT_PARSER_SYSTEM,
            "architect": SECTION_PLANNER_SYSTEM,
            "builder": SECTION_GENERATOR_SYSTEM,
            "critic": SECTION_VERIFIER_SYSTEM,
            "assembler": "Generate Shopify OS 2.0 JSON template files. Output ONLY valid JSON.",
            "iterator": ITERATION_HANDLER_SYSTEM,
        }
        return fallbacks.get(role, "")


# ── RAG Context Builder ─────────────────────────────────────────────────────

class RAGContextBuilder:
    """Builds targeted RAG context for each pipeline stage."""
    
    def __init__(self, search_engine: EnhancedSearchEngine):
        self.engine = search_engine
    
    def for_section(self, section_spec: dict, max_chunks: int = 8) -> str:
        """Get RAG context for generating a specific section.
        
        Searches for:
        1. Dawn reference code for the similar_to section
        2. Liquid patterns matching the section type
        3. Relevant CSS/JS examples
        """
        queries = []
        
        # Query 1: Dawn reference section
        similar = section_spec.get("similar_to") or section_spec.get("dawn_equivalent")
        if similar:
            queries.append(f"Dawn {similar} section Liquid code schema")
        
        # Query 2: Section type patterns
        section_type = section_spec.get("type", section_spec.get("name", ""))
        queries.append(f"Shopify {section_type} section Liquid template with schema")
        
        # Query 3: Specific features
        features = section_spec.get("special_features", [])
        if features:
            queries.append(f"Shopify Liquid {' '.join(features[:3])} implementation")
        
        # Query 4: Block types if specified
        blocks = section_spec.get("blocks_needed", section_spec.get("blocks", []))
        if blocks:
            block_types = [b.get("type", b) if isinstance(b, dict) else str(b) for b in blocks[:3]]
            queries.append(f"Shopify section blocks {' '.join(block_types)} schema")
        
        # Run searches and deduplicate
        all_results = []
        seen_texts = set()
        
        for query in queries:
            try:
                results = self.engine.search(query, top_k=max_chunks // len(queries) + 1)
                for r in results:
                    text_key = r.text[:200]  # Deduplicate by first 200 chars
                    if text_key not in seen_texts:
                        seen_texts.add(text_key)
                        all_results.append(r)
            except Exception as e:
                logger.warning(f"RAG search failed for '{query}': {e}")
        
        # Sort by score and take top N
        all_results.sort(key=lambda r: r.score, reverse=True)
        top_results = all_results[:max_chunks]
        
        if not top_results:
            return ""
        
        # Format as context string
        context_parts = []
        for i, r in enumerate(top_results, 1):
            source = r.metadata.get("file_path", r.metadata.get("source_url", "unknown"))
            collection = r.collection
            # Use parent text if available (more context)
            text = r.parent_text if r.parent_text and len(r.parent_text) > len(r.text) else r.text
            context_parts.append(
                f"--- Reference {i} [{collection}] ({source}) ---\n{text}\n"
            )
        
        return "\n".join(context_parts)
    
    def for_dawn_reference(self, section_name: str) -> str:
        """Get the full Dawn source code for a specific section."""
        query = f"Dawn {section_name} section complete Liquid code"
        results = self.engine.search(query, top_k=3)
        
        # Look for full section source
        for r in results:
            if (r.metadata.get("content_type") in ("section_full", "section_render", "SECTION_FULL") and
                section_name.lower() in r.metadata.get("file_path", "").lower()):
                return r.parent_text or r.text
        
        # Fall back to best match
        if results:
            return results[0].parent_text or results[0].text
        return ""
    
    def for_review(self, section_names: list) -> str:
        """Get Dawn patterns context for the Critic to verify against."""
        queries = [
            "Dawn section required patterns color_scheme padding responsive",
            "Shopify Liquid accessibility WCAG requirements alt text aria",
            "Dawn CSS custom properties variables color-foreground font-heading",
        ]
        
        all_results = []
        seen = set()
        for q in queries:
            for r in self.engine.search(q, top_k=3):
                key = r.text[:200]
                if key not in seen:
                    seen.add(key)
                    all_results.append(r)
        
        parts = [f"--- {r.collection}: {r.metadata.get('file_path', '')} ---\n{r.text[:800]}\n"
                 for r in all_results[:6]]
        return "\n".join(parts)


# ── Pipeline Orchestrator ───────────────────────────────────────────────────

@dataclass
class PipelineResult:
    """Result from the full generation pipeline."""
    success: bool
    theme_files: list[ThemeFile] = field(default_factory=list)
    template_jsons: dict = field(default_factory=dict)  # {"index.json": {...}}
    requirements: dict = field(default_factory=dict)
    section_plan: dict = field(default_factory=dict)
    review_result: dict = field(default_factory=dict)
    validation_errors: list = field(default_factory=list)
    cost_summary: dict = field(default_factory=dict)
    error: Optional[str] = None


class PipelineOrchestrator:
    """Orchestrates the full ShopifyAI generation pipeline.
    
    Pipeline:
      1. ROUTER (Haiku)      → Classify intent
      2. ARCHITECT (Sonnet+T) → Extract requirements / plan
      3. RAG SEARCH (free)    → Retrieve relevant context per section
      4. BUILDER×N (Sonnet)   → Generate section code with RAG context
      5. VALIDATORS (free)    → Static Liquid + Schema validation
      6. CRITIC (Opus+T)      → Deep code review
      7. ASSEMBLER (Haiku)    → Generate template JSONs
    """
    
    def __init__(self, rag_engine: Optional[EnhancedSearchEngine] = None, region: str = "us-east-1"):
        self.llm = LLMClient(region=region)
        self.rag = RAGContextBuilder(rag_engine) if rag_engine else None
        self.output_parser = ThemeOutputParser()
        self.diff_parser = ThemeDiffParser()
        self.liquid_validator = LiquidValidator()
        self.schema_validator = SchemaValidator()
        
        # Load system prompts
        self._prompts = {}
        for role in MODELS:
            self._prompts[role] = _load_prompt(role)
    
    def _call_model(self, role: str, user_message: str, system_override: str = None) -> LLMResponse:
        """Call a model by role with correct config."""
        config = MODELS[role]
        return self.llm.call(
            role=role,
            system_prompt=system_override or self._prompts[role],
            user_message=user_message,
            model_id=config["model_id"],
            max_tokens=config["max_tokens"],
            temperature=config["temp"],
            extended_thinking=config["thinking"],
            thinking_budget=config["budget"],
            cache_system=True,
        )
    
    # ── Stage 1: Route ──────────────────────────────────────────────────────
    
    def route(self, user_input: str) -> dict:
        """Classify user intent. Returns parsed JSON."""
        resp = self._call_model("router", user_input)
        try:
            return json.loads(resp.content)
        except json.JSONDecodeError:
            # Try to extract JSON from response
            import re
            match = re.search(r'\{.*\}', resp.content, re.DOTALL)
            if match:
                return json.loads(match.group())
            return {"intent": "unclear", "confidence": 0.0, "summary": resp.content[:200]}
    
    # ── Stage 2: Architect ──────────────────────────────────────────────────
    
    def extract_requirements(self, user_input: str) -> dict:
        """Extract structured requirements from user description."""
        resp = self._call_model("architect", 
            f"MODE 1: REQUIREMENTS EXTRACTION\n\nUser description:\n{user_input}\n\n"
            f"Return the full requirements JSON."
        )
        try:
            return json.loads(resp.content)
        except json.JSONDecodeError:
            import re
            match = re.search(r'\{.*\}', resp.content, re.DOTALL)
            if match:
                return json.loads(match.group())
            raise ValueError(f"Architect returned non-JSON: {resp.content[:500]}")
    
    def plan_iteration(self, current_files: dict, modification: str) -> dict:
        """Plan an iteration (what needs to change)."""
        files_context = "\n".join(f"--- {p} ---\n{c[:500]}..." for p, c in current_files.items())
        resp = self._call_model("architect",
            f"MODE 2: ITERATION PLANNING\n\n"
            f"CURRENT FILES:\n{files_context}\n\n"
            f"MODIFICATION REQUEST: {modification}\n\n"
            f"Return the iteration plan JSON."
        )
        try:
            return json.loads(resp.content)
        except json.JSONDecodeError:
            import re
            match = re.search(r'\{.*\}', resp.content, re.DOTALL)
            if match:
                return json.loads(match.group())
            raise ValueError(f"Architect returned non-JSON: {resp.content[:500]}")
    
    # ── Stage 3+4: RAG + Build Section ──────────────────────────────────────
    
    def build_section(self, section_spec: dict, style_guide: str = "") -> tuple[list[ThemeFile], list]:
        """Generate a single section with RAG context.
        
        Returns (theme_files, validation_errors).
        """
        # ── Get RAG context ──
        rag_context = ""
        dawn_reference = ""
        
        if self.rag:
            rag_context = self.rag.for_section(section_spec, max_chunks=8)
            similar = section_spec.get("similar_to") or section_spec.get("dawn_equivalent")
            if similar:
                dawn_reference = self.rag.for_dawn_reference(similar)
        
        # ── Build user message ──
        user_parts = [
            f"Generate a complete, production-ready Shopify section.\n",
            f"<section_spec>\n{json.dumps(section_spec, indent=2)}\n</section_spec>\n",
        ]
        
        if dawn_reference:
            user_parts.append(
                f"\n<dawn_reference>\n"
                f"Dawn section most similar to what you're building — follow its patterns:\n\n"
                f"{dawn_reference[:4000]}\n"
                f"</dawn_reference>\n"
            )
        
        if rag_context:
            user_parts.append(
                f"\n<rag_context>\n"
                f"Relevant Shopify documentation and code examples:\n\n"
                f"{rag_context[:6000]}\n"
                f"</rag_context>\n"
            )
        
        if style_guide:
            user_parts.append(f"\n<style_guide>\n{style_guide}\n</style_guide>\n")
        
        user_parts.append(
            "\nGenerate the COMPLETE section now. "
            "Include ALL files (Liquid + CSS + JS if needed). "
            "Use the <shopifyTheme> output format. No explanation — just code."
        )
        
        # ── Call Builder ──
        resp = self._call_model("builder", "\n".join(user_parts))
        
        # ── Parse output ──
        theme_files = self.output_parser.parse(resp.content)
        
        # ── Validate ──
        errors = self._validate_files(theme_files)
        
        return theme_files, errors
    
    # ── Stage 5: Static Validation ──────────────────────────────────────────
    
    def _validate_files(self, files: list[ThemeFile]) -> list:
        """Run static validators on generated files."""
        all_errors = []
        
        for f in files:
            if f.path.endswith(".liquid"):
                liquid_errors = self.liquid_validator.validate(f.content)
                for err in liquid_errors:
                    all_errors.append({
                        "file": f.path,
                        "validator": "liquid",
                        "severity": err.get("severity", "warning"),
                        "message": err.get("message", str(err)),
                    })
                
                # Schema validation for sections
                if f.path.startswith("sections/"):
                    schema_errors = self.schema_validator.validate(f.content)
                    for err in schema_errors:
                        all_errors.append({
                            "file": f.path,
                            "validator": "schema",
                            "severity": err.get("severity", "warning"),
                            "message": err.get("message", str(err)),
                        })
        
        return all_errors
    
    # ── Stage 6: Critic Review ──────────────────────────────────────────────
    
    def review(self, theme_files: list[ThemeFile], validation_errors: list = None) -> dict:
        """Send all generated code to the Critic for review."""
        # Build review context
        user_parts = ["Review these generated Shopify theme files:\n"]
        
        for f in theme_files:
            user_parts.append(f"--- {f.path} ---\n{f.content}\n")
        
        if validation_errors:
            user_parts.append(
                f"\nStatic validation already caught these issues (already fixed or flagged):\n"
                f"{json.dumps(validation_errors[:10], indent=2)}\n"
                f"Focus on what static analysis CANNOT catch.\n"
            )
        
        # Add RAG context for Dawn patterns
        if self.rag:
            section_names = [f.path.split("/")[-1].replace(".liquid", "") 
                           for f in theme_files if f.path.startswith("sections/")]
            review_context = self.rag.for_review(section_names)
            if review_context:
                user_parts.append(
                    f"\n<dawn_patterns>\n"
                    f"Reference Dawn patterns to verify against:\n{review_context}\n"
                    f"</dawn_patterns>\n"
                )
        
        user_parts.append("\nReturn ONLY valid JSON with your verdict.")
        
        # Call Critic
        resp = self._call_model("critic", "\n".join(user_parts))
        
        try:
            return json.loads(resp.content)
        except json.JSONDecodeError:
            import re
            match = re.search(r'\{.*\}', resp.content, re.DOTALL)
            if match:
                return json.loads(match.group())
            return {"verdict": "REVISE", "overall_score": 0, "summary": f"Failed to parse: {resp.content[:300]}"}
    
    # ── Stage 7: Assemble Templates ─────────────────────────────────────────
    
    def assemble_templates(self, requirements: dict, section_files: list[ThemeFile]) -> dict:
        """Generate template JSONs for each page."""
        # Extract section names from generated files
        section_names = []
        for f in section_files:
            if f.path.startswith("sections/") and f.path.endswith(".liquid"):
                name = f.path.replace("sections/", "").replace(".liquid", "")
                section_names.append(name)
        
        pages = requirements.get("pages", {"index": {"sections": section_names}})
        
        user_message = (
            f"Generate Shopify OS 2.0 JSON templates for these pages:\n\n"
            f"Pages config: {json.dumps(pages, indent=2)}\n\n"
            f"Available custom sections: {json.dumps(section_names)}\n\n"
            f"Standard Dawn sections available: header, footer, main-product, "
            f"main-collection-product-grid, main-cart-items, main-cart-footer, "
            f"main-blog, main-article, main-search, main-404\n\n"
            f"Generate ONE JSON per page. Output format:\n"
            f'{{"templates": {{"index.json": {{...}}, "product.json": {{...}}, ...}}}}'
        )
        
        resp = self._call_model("assembler", user_message)
        
        try:
            result = json.loads(resp.content)
            return result.get("templates", result)
        except json.JSONDecodeError:
            import re
            match = re.search(r'\{.*\}', resp.content, re.DOTALL)
            if match:
                result = json.loads(match.group())
                return result.get("templates", result)
            raise ValueError(f"Assembler returned non-JSON: {resp.content[:500]}")
    
    # ── FULL PIPELINE ───────────────────────────────────────────────────────
    
    def generate_theme(self, user_input: str, max_revisions: int = 2) -> PipelineResult:
        """Run the FULL generation pipeline end-to-end.
        
        Args:
            user_input: Natural language store description
            max_revisions: Max revision rounds with Critic
            
        Returns:
            PipelineResult with all generated files, costs, etc.
        """
        result = PipelineResult(success=False)
        
        try:
            # ── 1. Route ──
            logger.info("=== Stage 1: ROUTING ===")
            route_result = self.route(user_input)
            logger.info(f"Intent: {route_result.get('intent')}, confidence: {route_result.get('confidence')}")
            
            if route_result.get("intent") != "new_theme":
                result.error = f"Expected new_theme intent, got: {route_result.get('intent')}"
                return result
            
            # ── 2. Architect ──
            logger.info("=== Stage 2: ARCHITECTURE ===")
            requirements = self.extract_requirements(user_input)
            result.requirements = requirements
            logger.info(f"Sections to generate: {requirements.get('generation_plan', {}).get('total_custom_sections', '?')}")
            
            # ── 3+4. RAG + Build each section ──
            logger.info("=== Stage 3+4: RAG + BUILD ===")
            all_files = []
            all_errors = []
            
            # Get sections that need generation
            sections_to_build = [
                s for s in requirements.get("sections", [])
                if s.get("action") in ("create_custom", "modify_dawn")
            ]
            
            # Build style guide from design system
            design = requirements.get("design_system", {})
            style_guide = (
                f"Color mood: {design.get('color_mood', 'balanced')}\n"
                f"Typography: {design.get('typography_mood', 'modern-sans')}\n"
                f"Layout: {design.get('layout_density', 'balanced')}\n"
                f"Animations: {design.get('animation_level', 'subtle')}\n"
                f"Overall feel: {design.get('overall_feel', 'modern and clean')}"
            )
            
            for section_spec in sections_to_build:
                section_name = section_spec.get("id", section_spec.get("name", "unknown"))
                logger.info(f"  Building: {section_name}")
                
                files, errors = self.build_section(section_spec, style_guide=style_guide)
                all_files.extend(files)
                all_errors.extend(errors)
                
                logger.info(f"    → {len(files)} files, {len(errors)} validation errors")
            
            result.theme_files = all_files
            result.validation_errors = all_errors
            
            # ── 5. Validators already ran in build_section ──
            critical_errors = [e for e in all_errors if e.get("severity") == "critical"]
            if critical_errors:
                logger.warning(f"  {len(critical_errors)} CRITICAL validation errors found")
            
            # ── 6. Critic review ──
            logger.info("=== Stage 6: CRITIC REVIEW ===")
            for revision in range(max_revisions + 1):
                review = self.review(all_files, all_errors)
                result.review_result = review
                
                verdict = review.get("verdict", "REJECT")
                score = review.get("overall_score", 0)
                logger.info(f"  Verdict: {verdict}, Score: {score}")
                
                if verdict == "APPROVE":
                    logger.info("  ✅ APPROVED")
                    break
                elif verdict == "REVISE" and revision < max_revisions:
                    logger.info(f"  🔄 REVISION {revision + 1}/{max_revisions}")
                    # Apply fix instructions and rebuild affected sections
                    all_files, all_errors = self._apply_fixes(all_files, review, style_guide)
                    result.theme_files = all_files
                    result.validation_errors = all_errors
                else:
                    logger.warning(f"  ❌ {'REJECTED' if verdict == 'REJECT' else 'Max revisions reached'}")
                    if verdict == "REJECT":
                        result.error = f"Critic rejected with score {score}: {review.get('summary', '')}"
                        # Don't return — still return what we have
                    break
            
            # ── 7. Assemble templates ──
            logger.info("=== Stage 7: ASSEMBLY ===")
            templates = self.assemble_templates(requirements, all_files)
            result.template_jsons = templates
            logger.info(f"  Generated {len(templates)} template(s)")
            
            # ── Done ──
            result.success = True
            result.cost_summary = self.llm.get_cost_summary()
            
            logger.info(f"=== PIPELINE COMPLETE ===")
            logger.info(f"  Files: {len(result.theme_files)}")
            logger.info(f"  Templates: {len(result.template_jsons)}")
            logger.info(f"  Total cost: ${result.cost_summary['total']:.4f}")
            logger.info(f"  Total calls: {result.cost_summary['calls']}")
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            result.error = str(e)
            result.cost_summary = self.llm.get_cost_summary()
        
        return result
    
    def _apply_fixes(self, files: list[ThemeFile], review: dict, style_guide: str) -> tuple:
        """Apply Critic's fix instructions by re-calling Builder."""
        # Collect fix instructions per section
        fixes_by_section = {}
        for section_review in review.get("section_reviews", []):
            if section_review.get("status") == "needs_fixes":
                section_name = section_review["section"]
                fixes = [issue["fix_instruction"] for issue in section_review.get("issues", [])
                        if issue.get("severity") in ("critical", "major")]
                if fixes:
                    fixes_by_section[section_name] = fixes
        
        if not fixes_by_section:
            return files, []
        
        # Rebuild affected sections with fix instructions
        new_files = [f for f in files]  # Copy
        all_errors = []
        
        for section_name, fixes in fixes_by_section.items():
            # Find current files for this section
            section_files = {f.path: f.content for f in files 
                          if section_name in f.path}
            
            if not section_files:
                continue
            
            fix_instructions = "\n".join(f"- {fix}" for fix in fixes)
            
            user_message = (
                f"Fix these issues in the {section_name} section:\n\n"
                f"CURRENT CODE:\n"
                + "\n".join(f"--- {p} ---\n{c}\n" for p, c in section_files.items())
                + f"\n\nFIX INSTRUCTIONS:\n{fix_instructions}\n\n"
                f"<style_guide>\n{style_guide}\n</style_guide>\n\n"
                f"Output the COMPLETE fixed files using <shopifyTheme> format."
            )
            
            resp = self._call_model("builder", user_message)
            fixed_files = self.output_parser.parse(resp.content)
            
            # Replace files
            for fixed in fixed_files:
                errors = self._validate_files([fixed])
                all_errors.extend(errors)
                # Replace in list
                replaced = False
                for i, f in enumerate(new_files):
                    if f.path == fixed.path:
                        new_files[i] = fixed
                        replaced = True
                        break
                if not replaced:
                    new_files.append(fixed)
        
        return new_files, all_errors
    
    # ── Iteration Pipeline ──────────────────────────────────────────────────
    
    def iterate_theme(self, current_files: dict, modification: str) -> PipelineResult:
        """Handle user modification request on existing theme.
        
        Args:
            current_files: dict of {path: content} for current theme files
            modification: User's modification request
        """
        result = PipelineResult(success=False)
        
        try:
            # Route
            route = self.route(modification)
            
            # Plan
            plan = self.plan_iteration(current_files, modification)
            
            # Apply changes via Iterator
            files_context = "\n".join(f"--- {p} ---\n{c}\n" for p, c in current_files.items())
            
            user_message = (
                f"CURRENT THEME FILES:\n{files_context}\n\n"
                f"MODIFICATION REQUEST: {modification}\n\n"
                f"ARCHITECT'S PLAN:\n{json.dumps(plan, indent=2)}\n\n"
                f"Apply the changes using <themeDiff> format."
            )
            
            resp = self._call_model("iterator", user_message)
            
            # Parse diff
            changed_files = self.diff_parser.parse(resp.content)
            result.theme_files = changed_files
            
            # Validate
            result.validation_errors = self._validate_files(changed_files)
            
            # Quick review (Critic)
            review = self.review(changed_files, result.validation_errors)
            result.review_result = review
            
            result.success = review.get("verdict") in ("APPROVE", "REVISE")
            result.cost_summary = self.llm.get_cost_summary()
            
        except Exception as e:
            logger.error(f"Iteration failed: {e}", exc_info=True)
            result.error = str(e)
            result.cost_summary = self.llm.get_cost_summary()
        
        return result
