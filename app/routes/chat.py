"""
Receive Request
Validate Request
Call Service
Return Response

"""
from fastapi import APIRouter, Request
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.ai_services import get_ai_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    ai_response = get_ai_response(request.message)
    return ChatResponse(response=ai_response)