"""
Stage 5: Iteration Handler

Handles user feedback and modification requests:
- "Make the hero bigger"
- "Change the color to blue"  
- "Add a video background"
- "Remove the newsletter section"
- "Swap the order of testimonials and FAQ"

Produces targeted diffs, not full regenerations.
"""

from .constraints import get_constraints_for_stage
from .output_format import get_diff_format


ITERATION_HANDLER_SYSTEM = """You are ShopifyAI Iteration Handler — you make precise, targeted modifications to existing Shopify theme sections.

Your job: Take existing section code + a modification request and produce the minimum changes needed.

{constraints}

{diff_format}

MODIFICATION PRINCIPLES:
1. MINIMAL CHANGES — only touch what needs to change
2. PRESERVE EVERYTHING ELSE — don't reformat, rename, or "improve" unrelated code
3. COMPLETE FILES — when you modify a file, output the ENTIRE updated file (not patches)
4. SCHEMA CONSISTENCY — if you add a new setting, add it to the schema too
5. CSS UPDATES — if you change HTML structure, update CSS to match
6. BLOCK CHANGES — if you add/remove block types, update presets too

COMMON MODIFICATIONS:
- Size changes → CSS updates (padding, font-size, min-height, max-width)
- Color changes → Update color_scheme setting default, or add custom color settings
- Layout changes → CSS grid/flex modifications + possibly Liquid structure
- Content changes → Update default text in schema, possibly block structure
- Add feature → New settings + Liquid logic + CSS + possibly JS
- Remove element → Remove Liquid code + related settings + CSS + blocks
- Reorder → Template JSON order change (no section code changes)

IMPORTANT:
- If the change only affects the template JSON (reordering sections), only output the template file
- If the change requires new functionality, include ALL files (Liquid + CSS + JS)
- Test your changes mentally — will the old settings still work? Will existing blocks break?
"""


def get_iteration_handler_prompt(
    current_code: dict,
    modification_request: str,
    section_spec: dict = None,
    conversation_history: list = None,
) -> dict:
    """Build the iteration handler prompt.
    
    Args:
        current_code: Dict of file_path → file_content for current section files
        modification_request: User's modification request in natural language
        section_spec: Original section specification
        conversation_history: Previous modification requests for context
    """
    import json
    
    system = (ITERATION_HANDLER_SYSTEM
        .replace("{constraints}", get_constraints_for_stage("iteration_handler"))
        .replace("{diff_format}", get_diff_format())
    )
    
    user_parts = ["Modify this section based on the user's request.\n"]
    
    user_parts.append("CURRENT CODE:\n")
    for path, content in current_code.items():
        user_parts.append(f"--- {path} ---\n{content}\n")
    
    if conversation_history:
        user_parts.append("\nPREVIOUS MODIFICATIONS:\n")
        for i, mod in enumerate(conversation_history[-5:], 1):  # Last 5
            user_parts.append(f"{i}. {mod}\n")
    
    user_parts.append(f"\nMODIFICATION REQUEST: {modification_request}\n")
    
    user_parts.append(
        "\nApply the change using <themeDiff> format. "
        "Include only files that change. "
        "Provide COMPLETE file content for each changed file. "
        "No explanation — just the diff output."
    )
    
    return {
        "system": system,
        "user": "\n".join(user_parts),
        "stage": "iteration_handler",
        "expected_format": "theme_diff",
    }
