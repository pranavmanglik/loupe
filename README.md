# Loupe

Agentic documentation retrieval for complex technical ecosystems.

Loupe dynamically explores documentation structures, selects relevant paths, retrieves targeted context, and generates grounded answers using adaptive retrieval workflows.

---

# Why Loupe?

Traditional RAG systems usually:

- scrape entire websites
- index everything blindly
- retrieve chunks statically

Loupe instead performs:

```text
question
 → docs graph discovery
 → semantic route planning
 → adaptive traversal
 → targeted retrieval
 → grounded response generation
```

This allows Loupe to work effectively across large documentation systems like:

- Django
- FastAPI
- React
- Python
- LangChain
- Kubernetes
- and other deeply nested docs ecosystems

---

# Features

## Agentic Retrieval

Loupe does not rely on naive full-site scraping.

It:

- builds lightweight documentation graphs
- selects semantically relevant paths
- recursively expands promising branches
- retrieves only useful context

---

## Adaptive Documentation Traversal

Instead of indexing every page upfront:

```text
root docs
 → discover structure
 → plan traversal
 → expand relevant neighborhoods
 → fetch selectively
```

This significantly improves:
- scalability
- retrieval precision
- latency
- token efficiency

---

## Streaming Responses

Responses stream in real time using:
- FastAPI
- async generators
- Groq inference

---

## Markdown-Aware Rendering

Frontend supports:
- markdown rendering
- code blocks
- streaming UI
- conversational interaction

---

# Architecture

```text
Question
    ↓
Docs Graph Builder
    ↓
Semantic Route Planner
    ↓
Recursive Graph Explorer
    ↓
Targeted Page Fetching
    ↓
Chunking
    ↓
Retrieval
    ↓
LLM Synthesis
    ↓
Streaming Response
```

---

# Tech Stack

## Frontend

- Next.js
- React
- TailwindCSS

## Backend

- FastAPI
- Python
- httpx
- BeautifulSoup

## AI

- Groq
- Llama 3.3 70B
- Retrieval-Augmented Generation

---

# Current Retrieval Workflow

## 1. Graph Construction

Loupe crawls documentation roots and builds a lightweight graph:

```python
{
    "url": {
        "title": "...",
        "links": [...]
    }
}
```

---

## 2. Semantic Planning

Relevant documentation paths are selected based on:
- URL structure
- semantic relevance
- keyword scoring
- graph relationships

---

## 3. Recursive Expansion

Loupe expands nearby graph neighborhoods dynamically:

```text
models/
 → querysets/
 → queries/
 → fields/
```

instead of crawling the entire documentation tree.

---

## 4. Retrieval

Only relevant pages are:
- fetched
- extracted
- chunked
- retrieved

This reduces:
- unnecessary crawling
- retrieval noise
- latency

---

# Example

Question:

```text
How does Django ORM work?
```

Loupe may traverse:

```text
topics/db/models/
topics/db/queries/
ref/models/querysets/
ref/models/fields/
```

instead of blindly indexing the entire Django documentation site.

---

# Project Structure

```text
backend/
├── api/
├── core/
├── models/
├── services/
│   ├── crawler.py
│   ├── docs_graph.py
│   ├── explorer.py
│   ├── planner.py
│   ├── retrieval.py
│   ├── rag.py
│   └── llm.py
└── main.py

frontend/
└── app/
```

---

# Running Locally

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\\Scripts\\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Environment Variables

## Backend

```env
GROQ_API_KEY=your_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

## Frontend

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

# Roadmap

- Vector database integration
- Embedding-based hybrid retrieval
- Reflection loops
- Confidence scoring
- Persistent graph caching
- Citation generation
- Incremental indexing
- Multi-hop retrieval planning
- Autonomous recursive exploration

---

# Vision

Loupe is moving toward:

```text
adaptive retrieval orchestration
```

rather than static chatbot-style RAG.

The long-term goal is a retrieval system capable of intelligently navigating and reasoning across massive technical documentation ecosystems.

---
