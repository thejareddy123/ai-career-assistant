from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.services.ai_services import (chat)

router = APIRouter()


@router.post("/chat")
def chat_endpoint(
    request: ChatRequest
):

    response = chat(
        request.session_id,
        request.message
    )

    return {
        "response": response
    }