#!/usr/bin/env python3
"""Telegram bot for ShopifyAI Enhanced RAG — query the knowledge base via chat."""

import os
import sys
import logging
import html
from pathlib import Path

from telegram import Update, BotCommand
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    filters, ContextTypes,
)
from telegram.constants import ParseMode

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "REDACTED")

# Lazy-load search engine (heavy init)
_engine = None

def get_engine():
    global _engine
    if _engine is None:
        logger.info("Loading search engine...")
        from search.engine import EnhancedSearchEngine
        _engine = EnhancedSearchEngine(lazy_load=True)
        logger.info("Search engine ready")
    return _engine


def escape(text: str) -> str:
    """Escape HTML special chars."""
    return html.escape(text)


# ─── Handlers ───

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛍️ <b>ShopifyAI RAG Bot</b>\n\n"
        "Ask me anything about Shopify theme development!\n\n"
        "<b>Commands:</b>\n"
        "/search &lt;query&gt; — Search the knowledge base\n"
        "/quick &lt;query&gt; — Quick 3-result search\n"
        "/stats — Collection stats\n"
        "/help — Show this message\n\n"
        "Or just send a message and I'll search for it.",
        parse_mode=ParseMode.HTML,
    )


async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, ctx)


async def cmd_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    engine = get_engine()
    client = engine._get_client()
    
    lines = ["📊 <b>RAG Knowledge Base Stats</b>\n"]
    total = 0
    for col in ["liquid_reference", "code_examples", "theme_patterns",
                 "api_reference", "troubleshooting", "best_practices"]:
        try:
            info = client.get_collection(col)
            count = info.points_count
            total += count
            lines.append(f"  • <code>{col}</code>: <b>{count:,}</b> points")
        except:
            lines.append(f"  • <code>{col}</code>: ❌ error")
    
    lines.append(f"\n<b>Total: {total:,} indexed chunks</b>")
    lines.append(f"Model: <code>BAAI/bge-small-en-v1.5</code> (384d)")
    lines.append(f"Search: Dense + BM25 hybrid with RRF fusion")
    
    await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)


async def do_search(update: Update, query: str, top_k: int = 5):
    """Core search and respond."""
    if not query.strip():
        await update.message.reply_text("❌ Please provide a search query.")
        return
    
    # Send typing indicator
    await update.message.chat.send_action("typing")
    
    engine = get_engine()
    
    # Analyze
    from search.engine import analyze_query
    analyzed = analyze_query(query)
    
    # Search
    results = engine.search(query, top_k=top_k, use_reranker=True, expand_parents=True)
    
    if not results:
        await update.message.reply_text(
            f"🔍 <b>No results for:</b> <i>{escape(query)}</i>\n"
            f"Intent: {analyzed.intent} | Collections: {', '.join(analyzed.target_collections)}",
            parse_mode=ParseMode.HTML,
        )
        return
    
    # Build response
    header = (
        f"🔍 <b>{escape(query)}</b>\n"
        f"📊 Intent: <code>{analyzed.intent}</code> | "
        f"🎯 {', '.join(analyzed.target_collections)}\n"
        f"📝 <b>{len(results)} results</b>\n"
        f"{'─' * 30}\n"
    )
    
    messages = [header]
    current_msg = header
    
    for i, r in enumerate(results, 1):
        # Truncate text for Telegram
        text_preview = r.text[:600].strip()
        if len(r.text) > 600:
            text_preview += "..."
        
        # Format result
        result_block = (
            f"\n<b>#{i}</b> | Score: <code>{r.score:.4f}</code> | "
            f"<code>{r.collection}</code>\n"
        )
        
        if r.metadata.get("file_path"):
            fname = r.metadata["file_path"]
            if len(fname) > 50:
                fname = "..." + fname[-47:]
            result_block += f"📁 <code>{escape(fname)}</code>\n"
        
        meta_parts = []
        if r.metadata.get("content_type"):
            meta_parts.append(r.metadata["content_type"])
        if r.metadata.get("complexity"):
            meta_parts.append(r.metadata["complexity"])
        if meta_parts:
            result_block += f"🏷️ {' · '.join(meta_parts)}\n"
        
        if r.metadata.get("topics"):
            topics = r.metadata["topics"][:5]
            result_block += f"🔖 {', '.join(topics)}\n"
        
        if r.metadata.get("source_url"):
            result_block += f"🔗 {r.metadata['source_url']}\n"
        
        result_block += f"\n<pre>{escape(text_preview)}</pre>\n"
        
        if r.parent_text and r.parent_text != r.text:
            result_block += f"📎 <i>Parent context: {len(r.parent_text):,} chars available</i>\n"
        
        # Check Telegram message length limit (4096)
        if len(current_msg) + len(result_block) > 3800:
            messages.append(current_msg)
            current_msg = result_block
        else:
            current_msg += result_block
    
    if current_msg and current_msg != messages[-1]:
        messages.append(current_msg)
    
    # Send all message parts
    for msg in messages:
        if msg.strip():
            try:
                await update.message.reply_text(msg, parse_mode=ParseMode.HTML)
            except Exception as e:
                # Fallback without HTML if parsing fails
                await update.message.reply_text(
                    msg.replace("<b>", "").replace("</b>", "")
                    .replace("<i>", "").replace("</i>", "")
                    .replace("<code>", "").replace("</code>", "")
                    .replace("<pre>", "").replace("</pre>", "")
                )


async def cmd_search(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = " ".join(ctx.args) if ctx.args else ""
    await do_search(update, query, top_k=5)


async def cmd_quick(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = " ".join(ctx.args) if ctx.args else ""
    await do_search(update, query, top_k=3)


async def handle_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Handle plain text messages as search queries."""
    if not update.message or not update.message.text:
        return
    query = update.message.text.strip()
    if query.startswith("/"):
        return  # Skip unknown commands
    await do_search(update, query, top_k=5)


async def post_init(app: Application):
    """Set bot commands after startup."""
    await app.bot.set_my_commands([
        BotCommand("search", "Search the knowledge base"),
        BotCommand("quick", "Quick 3-result search"),
        BotCommand("stats", "Show collection stats"),
        BotCommand("help", "Show help"),
    ])
    logger.info("Bot commands set")
    
    # Pre-load engine
    get_engine()
    logger.info("🚀 Bot is ready!")


def main():
    logger.info("Starting ShopifyAI RAG Telegram Bot...")
    
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("search", cmd_search))
    app.add_handler(CommandHandler("quick", cmd_quick))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Polling for updates...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
