from fastapi import APIRouter
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

    result = route_query(request.query)

    return ChatResponse(
        agent=result["agent"],
        response=result["response"]
    )