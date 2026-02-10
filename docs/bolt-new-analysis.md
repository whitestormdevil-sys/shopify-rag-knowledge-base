# 🔬 bolt.new Deep Architecture Analysis

> Complete dissection of every component, system prompt, tool, and pattern.
> Analyzed for ShopifyAI adaptation potential.

**Repo:** `github.com/stackblitz/bolt.new` (16,199 ⭐)
**Stack:** Remix + Cloudflare Workers + WebContainer + Claude API
**Total:** ~7,300 lines of TypeScript across 87 files
**Analysis Date:** 2026-02-10

---

## Table of Contents
1. [Architecture Overview](#1-architecture-overview)
2. [System Prompt Analysis](#2-system-prompt-analysis)
3. [LLM Layer](#3-llm-layer)
4. [Runtime Engine](#4-runtime-engine)
5. [State Management](#5-state-management)
6. [API Routes](#6-api-routes)
7. [Frontend Components](#7-frontend-components)
8. [Utilities](#8-utilities)
9. [Component Scorecard](#9-component-scorecard)
10. [Lessons for ShopifyAI](#10-lessons-for-shopifyai)

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND (Remix)                  │
│  ┌─────────┐  ┌───────────┐  ┌──────────────────┐  │
│  │ Chat UI │  │  Editor   │  │  Preview (iframe) │  │
│  │ (React) │  │(CodeMirror)│  │  (WebContainer)  │  │
│  └────┬────┘  └─────┬─────┘  └────────┬─────────┘  │
│       │             │                  │             │
│  ┌────▼─────────────▼──────────────────▼──────────┐ │
│  │              Stores (nanostores)                │ │
│  │  chatStore │ workbenchStore │ filesStore │ etc  │ │
│  └────────────────────┬───────────────────────────┘ │
│                       │                              │
│  ┌────────────────────▼───────────────────────────┐ │
│  │          StreamingMessageParser                 │ │
│  │   Extracts <boltArtifact> + <boltAction>       │ │
│  │   from streaming AI response in real-time      │ │
│  └────────────────────┬───────────────────────────┘ │
│                       │ callbacks                    │
│  ┌────────────────────▼───────────────────────────┐ │
│  │              ActionRunner                       │ │
│  │   Executes file writes + shell commands         │ │
│  │   in WebContainer                               │ │
│  └────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────┘
                       │ POST /api/chat
┌──────────────────────▼──────────────────────────────┐
│                  SERVER (Cloudflare)                  │
│  ┌─────────────────────────────────────────────────┐ │
│  │ stream-text.ts → Claude API (Anthropic SDK)     │ │
│  │ System prompt + conversation → streaming tokens │ │
│  │ SwitchableStream for auto-continue on max_tokens│ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

**Key Insight:** bolt.new is deceptively simple. The entire AI backend is ~6 files. The magic is in the **system prompt** and the **streaming parser**.

---

## 2. System Prompt Analysis

**File:** `app/lib/.server/llm/prompts.ts` (284 lines)
**Total prompt size:** ~8,500 chars (~2,125 tokens)

### Structure Breakdown

| Section | Lines | Purpose | Score |
|---------|-------|---------|-------|
| Identity | 2 | "You are Bolt, an expert AI..." | ⭐⭐⭐ |
| `<system_constraints>` | 25 | WebContainer limitations (no native bins, no pip, no g++) | ⭐⭐⭐⭐⭐ |
| `<code_formatting_info>` | 1 | "Use 2 spaces" | ⭐⭐ |
| `<message_formatting_info>` | 1 | Allowed HTML elements (dynamic) | ⭐⭐⭐ |
| `<diff_spec>` | 25 | How file modifications are sent to the model | ⭐⭐⭐⭐⭐ |
| `<artifact_info>` | 60 | Output format spec with 14 rules | ⭐⭐⭐⭐⭐ |
| Behavioral rules | 8 | "Don't be verbose", "Think first", never say "artifact" | ⭐⭐⭐⭐ |
| Examples | 80 | 3 few-shot examples (factorial, snake, bouncing ball) | ⭐⭐⭐⭐ |

### What Makes It Brilliant

1. **Negative constraints are explicit** — "There is NO pip", "Git is NOT available", "CANNOT run native binaries" — repeated 3 different ways. AI models need to hear "no" multiple times.

2. **14 artifact rules are numbered and ordered by priority** — Not a wall of text. Structured rules the model can reference by number.

3. **Rule #11 is THE critical rule:** "ALWAYS provide the FULL, updated content... NEVER use placeholders" — This single rule prevents 90% of bad code generation. Without it, models love to write `// rest of code stays the same...`

4. **Few-shot examples are escalating complexity:** Simple function → Game → Physics animation. Teaches the pattern through progressive examples.

5. **Diff spec is genius for iterations:** When user edits code in the editor, bolt computes a unified diff and prepends it to the next message. The model sees exactly what changed. Saves tokens vs sending full files.

### What's Weak

1. **No domain-specific constraints** — bolt is generic. No framework best practices, no accessibility rules, no performance targets. This is where ShopifyAI adds massive value.

2. **No validation instructions** — No mention of "check your JSON is valid" or "verify imports exist." The model can produce broken code with no self-check.

3. **No multi-model strategy** — Single model, single prompt. No specialization.

4. **No RAG integration** — Pure model knowledge only. No external reference injection.

5. **CONTINUE_PROMPT is naive:** Just "Continue your prior response" — no context about what was being generated, no checksums, easy to lose track.

### Score: 8.5/10
Excellent for a generic builder. The structured constraint approach is best-in-class. Weak on domain knowledge and verification.

---

## 3. LLM Layer

### 3.1 Model Selection (`model.ts`) — 7 lines

```typescript
return anthropic('claude-3-5-sonnet-20240620');
```

**Verdict:** Hardcoded single model. No model routing, no fallbacks, no multi-model.
**Score: 3/10** — Functional but inflexible.

### 3.2 Stream Text (`stream-text.ts`) — 37 lines

Key patterns:
- Uses Vercel AI SDK (`streamText` from `ai` package)
- Passes `anthropic-beta: max-tokens-3-5-sonnet-2024-07-15` header (extended token limit)
- `toolChoice: 'none'` — explicitly disables function calling
- `maxTokens: 8192` — hard cap per response

**Score: 7/10** — Clean, uses industry-standard SDK. No retry logic, no error recovery.

### 3.3 SwitchableStream (`switchable-stream.ts`) — 60 lines

**This is clever.** When Claude hits `max_tokens` (8192) mid-generation:
1. The `onFinish` callback detects `finishReason === 'length'`
2. Appends the partial response as assistant message
3. Appends `CONTINUE_PROMPT` as user message
4. Starts a NEW stream and switches the readable source
5. Client sees one continuous stream — no interruption
6. Max 2 continuations (`MAX_RESPONSE_SEGMENTS = 2`)

**Score: 9/10** — Elegant solution to token limits. The client never knows a switch happened. Critical for large code generation.

### 3.4 API Key (`api-key.ts`) — 6 lines

Simple env var lookup. Supports both Cloudflare Workers env and Node.js process.env.

**Score: 6/10** — Works, but no validation, no key rotation, no rate limit handling.

### 3.5 Constants (`constants.ts`) — 2 lines

```typescript
MAX_TOKENS = 8192
MAX_RESPONSE_SEGMENTS = 2
```

Effective max output: 8192 × 3 = ~24,576 tokens per response.

---

## 4. Runtime Engine

### 4.1 StreamingMessageParser (`message-parser.ts`) — 285 lines

**THE most important file in the entire codebase.**

This is a **streaming XML parser** that processes AI output character-by-character as it streams in. It:

1. Scans for `<boltArtifact>` opening tags
2. Extracts `id` and `title` attributes
3. Fires `onArtifactOpen` callback → shows workbench
4. Scans for `<boltAction type="file|shell">` tags inside the artifact
5. Extracts `type` and `filePath` attributes
6. Fires `onActionOpen` callback → shows file in editor
7. Accumulates content between action open/close tags
8. Fires `onActionClose` callback → writes file / runs command

**Critical design decisions:**
- File actions fire `onActionOpen` immediately (show in editor while generating)
- Shell actions wait for `onActionClose` (need complete command before executing)
- Uses character-level scanning, NOT regex — handles partial/streaming input
- Maintains per-message state (position, inside artifact/action, current action)
- Strips trailing whitespace, adds newline to file content

**Why it's character-level:**
Regex can't handle incomplete XML tags. When streaming, you might receive `<boltAc` in one chunk and `tion type="file">` in the next. The character scanner handles this by tracking position and breaking when it can't find a complete tag yet.

**Score: 9.5/10** — Masterful streaming parser. The callback architecture is clean and extensible. Only weakness: no error recovery if AI produces malformed tags.

### 4.2 ActionRunner (`action-runner.ts`) — 186 lines

Executes parsed actions in a WebContainer:

**File actions:**
1. `mkdir -p` for parent directories
2. `fs.writeFile` with full content
3. That's it. Simple file write.

**Shell actions:**
1. Spawns `jsh -c <command>` in WebContainer
2. Pipes output to console
3. Supports abort via AbortController
4. Tracks status: pending → running → complete|failed|aborted

**Execution model:**
- Actions execute SEQUENTIALLY via promise chaining (`#currentExecutionPromise`)
- This ensures `npm install` finishes before `npm run dev`
- Each action is independent (own abort controller)
- Status tracked in a nanostores MapStore for reactive UI updates

**Score: 8/10** — Clean sequential execution. Wish it had retry logic and better error messages. The abort mechanism is well-designed.

---

## 5. State Management

Uses **nanostores** — a minimal (334 bytes) reactive store library.

### Stores:

| Store | Purpose | Complexity |
|-------|---------|-----------|
| `chatStore` | Chat state (started, aborted, showChat) | Simple map |
| `workbenchStore` | THE big one — files, editor, terminal, previews, artifacts, actions | Complex class |
| `filesStore` | File system state, file modifications tracking | Medium |
| `editorStore` | Current document, scroll positions, selections | Medium |
| `previewsStore` | Preview iframe ports/URLs | Simple |
| `terminalStore` | Terminal instance, show/hide | Simple |
| `settingsStore` | User preferences | Simple |

**WorkbenchStore is the hub.** It orchestrates:
- File modifications → diff computation → prepend to next message
- Artifact lifecycle → action runner → file writes → editor updates
- Unsaved file tracking → save before send

**Score: 8/10** — Clean separation of concerns. nanostores is a great choice for streaming-heavy UIs (more performant than Redux/Zustand for fine-grained updates).

---

## 6. API Routes

### 6.1 `/api/chat` (`api.chat.ts`) — 55 lines

The main endpoint. Handles:
1. Receives message history from client
2. Calls `streamText()` with system prompt
3. Returns streaming response
4. **Auto-continue:** When `finishReason === 'length'`:
   - Appends partial response + CONTINUE_PROMPT
   - Creates new stream via `SwitchableStream`
   - Client sees uninterrupted flow

**Score: 8/10** — The auto-continue is the killer feature. No error handling for rate limits or API failures though.

### 6.2 `/api/enhancer` (`api.enhancer.ts`) — 45 lines

Prompt enhancement endpoint:
1. Takes user's raw prompt
2. Wraps in `<original_prompt>` tags
3. Asks Claude to improve it
4. Streams improved prompt back to input field

**The enhance prompt:**
```
I want you to improve the user prompt that is wrapped in `<original_prompt>` tags.
IMPORTANT: Only respond with the improved prompt and nothing else!
```

**Score: 7/10** — Smart UX feature. The prompt is too simple — could be more specific about what "improve" means (add technical details? clarify architecture? specify framework?).

---

## 7. Frontend Components

### Key Components:

| Component | Lines | Purpose | Score |
|-----------|-------|---------|-------|
| `Chat.client.tsx` | 234 | Chat container, message handling, file diff injection | ⭐⭐⭐⭐ |
| `BaseChat.tsx` | 213 | Chat UI layout, input area, send button | ⭐⭐⭐ |
| `CodeMirrorEditor.tsx` | 461 | Full code editor with syntax highlighting | ⭐⭐⭐⭐ |
| `FileTree.tsx` | 409 | File explorer with expand/collapse | ⭐⭐⭐⭐ |
| `Workbench.client.tsx` | 187 | Split view: editor + preview | ⭐⭐⭐ |
| `Preview.tsx` | 124 | iframe preview with port detection | ⭐⭐⭐ |
| `Terminal.tsx` | 86 | xterm.js terminal integration | ⭐⭐⭐ |
| `Artifact.tsx` | 213 | Artifact display (collapsible action list) | ⭐⭐⭐⭐ |
| `Menu.client.tsx` | 172 | Sidebar with chat history | ⭐⭐⭐ |

### Chat Flow (Chat.client.tsx):

```
User types message
  → Save all unsaved files
  → Compute file modifications (diffs)
  → Prepend diffs to user message: `${diff}\n\n${input}`
  → Send to /api/chat
  → Stream response through StreamingMessageParser
  → Parser fires callbacks → workbench updates in real-time
  → Files appear in editor AS they stream
  → Shell commands execute AFTER they complete
```

**The diff injection is key:** Every message after the first includes file modifications the user made in the editor. This means Claude always has the latest state.

---

## 8. Utilities

| Utility | Purpose | Score | ShopifyAI Use? |
|---------|---------|-------|---------------|
| `diff.ts` | Computes unified diffs, converts to HTML for prompt injection | ⭐⭐⭐⭐⭐ | YES — for iteration diffs |
| `markdown.ts` | Configures remark/rehype with allowed HTML + sanitization | ⭐⭐⭐ | Maybe — for chat formatting |
| `stripIndent.ts` | Template literal indentation stripping | ⭐⭐⭐ | YES — for clean prompts |
| `logger.ts` | Scoped logging with levels | ⭐⭐⭐ | YES |
| `shell.ts` | Shell command utilities | ⭐⭐ | No (we use Python) |
| `buffer.ts` | Buffer utilities | ⭐⭐ | No |
| `constants.ts` | WORK_DIR, MODIFICATIONS_TAG_NAME | ⭐⭐⭐ | YES — define our own |

### diff.ts Deep Dive:

The diff system is sophisticated:
1. Uses `diff` npm package to compute GNU unified diffs
2. Compares original file content vs current editor content
3. **Smart choice:** If diff > new content size → send full file; else → send diff
4. Wraps in `<bolt_file_modifications>` tag with `<diff>` or `<file>` children
5. Prepended to user message so Claude sees all changes

This is the secret to bolt's iteration quality. Claude doesn't guess what changed — it sees exact diffs.

---

## 9. Component Scorecard

| Component | Quality | Complexity | Reusability | ShopifyAI Relevance |
|-----------|---------|-----------|-------------|-------------------|
| **System Prompt** | 8.5/10 | Medium | High (adapt constraints) | ⭐⭐⭐⭐⭐ |
| **StreamingMessageParser** | 9.5/10 | High | High (change tag names) | ⭐⭐⭐⭐⭐ |
| **SwitchableStream** | 9/10 | Medium | Direct reuse | ⭐⭐⭐⭐ |
| **ActionRunner** | 8/10 | Medium | Adapt (Shopify API vs WebContainer) | ⭐⭐⭐⭐ |
| **Diff System** | 9/10 | Medium | Direct reuse | ⭐⭐⭐⭐⭐ |
| **Auto-Continue** | 8/10 | Low | Direct reuse | ⭐⭐⭐⭐ |
| **Prompt Enhancer** | 7/10 | Low | Adapt for Shopify prompts | ⭐⭐⭐ |
| **Chat Component** | 7/10 | High | Reference only (we use Telegram) | ⭐⭐ |
| **WorkbenchStore** | 8/10 | High | Reference pattern | ⭐⭐⭐ |
| **Model Layer** | 3/10 | Low | Rewrite (multi-model) | ⭐ |

### Overall Architecture Score: **8.2/10**

**Strengths:** Streaming parser, diff system, prompt engineering, auto-continue, clean separation
**Weaknesses:** Single model, no validation, no RAG, no error recovery, no retry logic

---

## 10. Lessons for ShopifyAI

### 🟢 STEAL (Direct adaptation)

1. **Streaming XML parser pattern** — Change `<boltArtifact>` → `<shopifyTheme>` and `<boltAction>` → `<themeFile>`. The character-level parsing approach is perfect for streaming code generation.

2. **Auto-continue via SwitchableStream** — Our section generator prompt is ~32K chars. With a 6-section theme, we could hit token limits. Auto-continue ensures complete sections.

3. **Diff injection for iterations** — When user says "make hero bigger", compute diff of current theme files and inject into the iteration prompt. Claude sees exactly what the current state is.

4. **"FULL content, NEVER placeholders" rule** — Rule #11 in their prompt. We already have this. It's THE most important code generation rule. Keep it.

5. **Numbered, structured rules in prompts** — Not prose paragraphs. Numbered lists that the model can reference. We already do this.

6. **Negative constraints repeated multiple ways** — "NO pip", "CANNOT run native binaries", "NOT available" — Claude needs to hear "no" 3 times. Apply to Shopify: "NEVER use {% include %}", "CANNOT skip {% schema %}", "NO inline styles for static CSS".

### 🟡 ADAPT (Modify for our use case)

7. **ActionRunner → ThemeAssembler** — Their runner writes files to WebContainer. Ours writes to `/tmp/themes/{user_id}/` and pushes via Shopify Asset API. Same pattern, different target.

8. **Single artifact → Multi-section generation** — bolt creates ONE artifact per response. We generate MULTIPLE sections, each as a separate `<themeFile>`. Our parser already handles this.

9. **Prompt enhancer → Requirements clarifier** — Their enhancer is generic ("improve this prompt"). Our Client Agent (Sonnet 4.5 + Thinking) does this better with Shopify-specific follow-up questions.

10. **WebContainer preview → Shopify preview URL** — They preview in iframe via WebContainer. We preview via Shopify's theme preview URL (`store.myshopify.com/?preview_theme_id=XXX`).

### 🔴 DON'T COPY (Their weaknesses, our strengths)

11. **Single model** — Their biggest limitation. We have 4 specialized agents with model escalation.

12. **No validation** — They trust the model output blindly. We have LiquidValidator + SchemaValidator + AI Reviewer (Opus 4.6). Three layers of verification.

13. **No RAG** — They rely purely on Claude's training data. We have 48,130 indexed chunks with Dawn source code, Liquid reference, and Shopify best practices.

14. **No domain constraints** — Their prompt is generic. Ours has 20,000 chars of Shopify-specific rules covering Liquid, schemas, OS 2.0, Dawn patterns, performance, and accessibility.

15. **No retry logic** — If generation fails, the user has to rephrase. Our pipeline retries with Opus 4.6 fallback and specific fix instructions from the reviewer.

---

## Summary

bolt.new proved that a relatively simple architecture (streaming parser + structured prompt + action runner) can build a massively successful AI code generator. Their code is clean, focused, and well-engineered.

**What they got right:** The streaming parser and prompt engineering are world-class.
**What they left on the table:** Domain specialization, multi-model, validation, RAG.

**That table is where ShopifyAI lives.** We take their proven patterns and add everything they're missing: domain expertise, quality gates, knowledge retrieval, and intelligent model routing.

**bolt.new is a general-purpose hammer. ShopifyAI is a precision instrument for Shopify themes.**
