# ShopifyAI RAG Knowledge Base

Comprehensive Shopify knowledge base with vector embeddings for RAG (Retrieval-Augmented Generation).

## Stats
- **2,320 files** processed across 46 categories
- **41,303 vector chunks** indexed in Qdrant
- **208MB** vector database
- **Embedding Model:** BAAI/bge-small-en-v1.5 (384 dimensions)
- **Vector DB:** Qdrant (local storage mode)
- **Framework:** LangChain

## Categories Covered

### Core Liquid
- Liquid objects (product, collection, cart, shop, customer, etc.)
- Liquid filters & tags (complete reference)
- Liquid basics (types, operators, whitespace)

### APIs
- Admin REST API (products, orders, customers, inventory, etc.)
- Admin GraphQL API (queries, mutations, objects)
- Storefront API (queries, mutations, objects)
- Ajax API (cart.js, section rendering, predictive search)

### Theme Development
- Dawn theme source code
- Theme architecture (layouts, templates, sections, blocks)
- JSON schemas (section schema, settings schema)
- Best practices & performance

### App Development
- Functions (discounts, shipping, payment customization)
- Checkout extensions & components
- App Bridge
- Theme app extensions
- Admin extensions
- Authentication & OAuth

### Specialized
- Metafields & Metaobjects
- Customer Events & Web Pixels
- Bulk Operations
- Shopify Markets (multi-currency, multi-language)
- Shopify Flow
- B2B features
- Subscriptions & Selling Plans
- Discounts

### Reference
- Polaris design system (42 components)
- Shopify CLI
- Hydrogen (headless framework)
- Stack Overflow top Q&A (200+ questions)
- Changelog & versioning
- Performance patterns
- SEO patterns
- Common theme patterns (cart drawer, swatches, galleries, etc.)
- Gotchas & edge cases

### Source Code
- Shopify/dawn (reference theme)
- Shopify/hydrogen (headless framework)
- Shopify/theme-liquid-docs (machine-readable Liquid docs)
- Shopify/theme-check (linter rules)
- Shopify app templates (Node, Remix)

## Project Structure
```
rag-knowledge-base/
├── raw-docs/           # Source documents (47MB)
│   ├── liquid-docs/
│   ├── liquid-objects/
│   ├── liquid-filters-tags/
│   ├── admin-api/
│   ├── storefront-api/
│   ├── ajax-api/
│   ├── dawn-theme/
│   ├── shopify-repos/
│   ├── ... (46 categories)
├── qdrant_data/        # Vector database (208MB)
├── scripts/            # Scraping & indexing scripts
│   ├── scrape_liquid_docs.py
│   ├── scrape_phase2.py
│   ├── scrape_phase4_all.py
│   ├── scrape_community.py
│   └── index_efficient.py
├── index_stats.json    # Indexing statistics
└── .venv/              # Python virtual environment (not tracked)
```

## Usage

### Setup
```bash
cd rag-knowledge-base
python3.13 -m venv .venv
source .venv/bin/activate
pip install langchain langchain-community qdrant-client[fastembed] beautifulsoup4 markdownify tqdm
```

### Query the Knowledge Base
```python
from qdrant_client import QdrantClient
from fastembed import TextEmbedding

client = QdrantClient(path="./qdrant_data")
embed_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

query = "How do I create a cart drawer in Shopify?"
query_vector = list(embed_model.embed([query]))[0].tolist()

results = client.search(
    collection_name="shopify_knowledge",
    query_vector=query_vector,
    limit=5,
)

for result in results:
    print(f"Score: {result.score:.3f}")
    print(f"File: {result.payload['file_path']}")
    print(f"Text: {result.payload['text'][:200]}...")
    print()
```

## Re-indexing
```bash
# Re-scrape docs
python scripts/scrape_liquid_docs.py
python scripts/scrape_phase2.py
python scripts/scrape_phase4_all.py
python scripts/scrape_community.py

# Re-index
python scripts/index_efficient.py
```
