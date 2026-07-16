from fastapi import APIRouter
import traceback

from backend.models.schemas import ChatRequest, ChatResponse
from backend.agents.router import route_query

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to Nexora Electronics AI Customer Support!"
    }


@router.get("/health")
def health():
    return {
        "status": "Running"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        result = route_query(request.query)

        response = ChatResponse(
            agent=result["agent"],
            response=result["response"],
            sources=result["sources"]
        )

        return response

    except Exception:

        traceback.print_exc()
        raise