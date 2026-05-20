from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from models.chat import ChatRequest

from services.rag import run_rag

router = APIRouter()


@router.post("/chat")
async def chat(
    req: ChatRequest
):

    async def generator():

        async for token in run_rag(
            req.url,
            req.question,
        ):

            yield token

    return StreamingResponse(
        generator(),
        media_type="text/plain",
    )
