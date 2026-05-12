from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.fetcher import fetch_url
from services.extractor import extract_content
from services.chunker import chunk_text
from services.retrieval import Retriever

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


@app.get("/")
async def root():
    return {
        "message": "Loupe backend running"
    }


@app.post("/chat")
async def chat(req: ChatRequest):

    html = await fetch_url(req.url)

    content = extract_content(html)

    chunks = chunk_text(content)

    retriever = Retriever(chunks)

    results = retriever.search(
        req.question
    )

    return {
        "chunks": results
    }
