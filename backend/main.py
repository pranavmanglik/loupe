from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.fetcher import fetch_url
from services.extractor import extract_content
from services.chunker import chunk_text
from services.retrieval import Retriever
from services.llm import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    url: str
    question: str


@app.post("/chat")
async def chat(req: ChatRequest):

    html = await fetch_url(req.url)

    content = extract_content(html)

    chunks = chunk_text(content)

    retriever = Retriever(chunks)

    relevant_chunks = retriever.search(
        req.question,
        n=5
    )

    answer = await generate_answer(
        req.question,
        relevant_chunks
    )

    return {
        "answer": answer,
        "sources": relevant_chunks
    }
