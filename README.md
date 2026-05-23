# Loupe

> Agentic RAG for webpages.  
> Paste a link. Ask questions. Get grounded answers with streaming responses.

---

## Overview

Loupe is a lightweight Agentic RAG system that:

- fetches webpage content
- extracts meaningful text
- chunks and retrieves relevant context
- queries an LLM
- streams responses in real time

Built with:

- Next.js
- FastAPI
- Groq
- React Streaming UI

---

# Features

- Streaming chat interface
- Webpage ingestion
- Retrieval-Augmented Generation (RAG)
- Markdown rendering
- Groq-powered inference
- Responsive UI
- FastAPI backend
- Deploy-ready architecture

---

# Architecture

```text
User Question
      ↓
Frontend (Next.js)
      ↓
FastAPI Backend
      ↓
Fetch Webpage
      ↓
Extract Content
      ↓
Chunk Text
      ↓
Retrieve Relevant Chunks
      ↓
Groq LLM
      ↓
Stream Response
      ↓
Frontend Chat UI
```

---

# Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 16 |
| UI | React + Tailwind |
| Backend | FastAPI |
| LLM Provider | Groq |
| Streaming | StreamingResponse |
| Markdown | react-markdown |

---

# Project Structure

```text
loupe/
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── ...
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   └── ...
│
└── README.md
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Environment Variables

## Frontend

Create:

```text
frontend/.env.local
```

Add:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## Backend

Create:

```text
backend/.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Example Usage

1. Paste webpage URL
2. Ask question
3. Loupe:
   - extracts webpage
   - retrieves relevant context
   - streams grounded answer

---

# Example Questions

```text
What is this article about?

Summarize the main points.

What technologies are mentioned?

Explain this section in simple terms.
```

---

# Deployment

## Frontend
Deploy on:
- Vercel

## Backend
Deploy on:
- Render

---

# Future Plans

- Vector database support
- Multi-page ingestion
- PDF support
- Source citations
- Agent workflows
- Local Ollama mode
- Multi-model routing
- Conversation memory

---

# Why Loupe?

Most RAG systems are:
- overengineered
- slow
- difficult to deploy

Loupe focuses on:
- simplicity
- streaming UX
- fast iteration
- clean architecture

---

# License

MIT

---

# Author

Built by Pranav Manglik.
