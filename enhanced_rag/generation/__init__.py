"""
ShopifyAI Code Generation Pipeline

Multi-stage theme generation from natural language to deployable Shopify themes.
Built on top of the Enhanced RAG knowledge base.

Pipeline stages:
1. Intent Parser     → Understands what the user wants
2. Section Planner   → Maps intent to Dawn sections (keep/modify/create)
3. Section Generator → Writes Liquid/CSS/JS code
4. Section Verifier  → Validates correctness
5. Iteration Handler → Handles "make it bigger" refinements
"""

__version__ = "0.1.0"
