from fastapi import APIRouter

from fastapi.responses import (
    StreamingResponse,
)

from pydantic import BaseModel

from services.rag import run_rag


router = APIRouter()


class ChatRequest(BaseModel):

    url: str

    question: str


@router.post("/chat")
async def chat(
    request: ChatRequest,
):

    async def generator():

        async for token in run_rag(
            request.url,
            request.question,
        ):

            yield token.encode("utf-8")

    return StreamingResponse(
        generator(),
        media_type="text/plain",
    )
