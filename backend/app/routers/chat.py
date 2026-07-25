from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.services.chat_service import get_chat_response

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(data: ChatRequest):

    answer = get_chat_response(data.question)

    return {
        "question": data.question,
        "answer": answer
    }