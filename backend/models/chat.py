from pydantic import BaseModel


class ChatRequest(BaseModel):
    url: str
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
