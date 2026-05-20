from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import asyncio

router = APIRouter()


@router.post("/chat")
async def chat():

    async def fake_stream():

        for word in [
            "Hello ",
            "from ",
            "Loupe ",
            "streaming!"
        ]:

            await asyncio.sleep(1)

            print("YIELDING:", word)

            yield word

    return StreamingResponse(
        fake_stream(),
        media_type="text/plain",
    )
