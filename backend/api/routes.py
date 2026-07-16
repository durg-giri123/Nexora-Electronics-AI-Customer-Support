from fastapi import APIRouter
import traceback

from backend.models.schemas import ChatRequest, ChatResponse
from backend.agents.router import route_query

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "THIS IS THE NEW BACKEND"
    }


@router.get("/health")
def health():
    return {
        "status": "Running"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    print("\n" + "=" * 80)
    print("REQUEST RECEIVED")
    print(f"Query: {request.query}")
    print("=" * 80)

    try:

        result = route_query(request.query)

        print("\n" + "=" * 80)
        print("ROUTER RESULT")
        print(result)
        print("=" * 80)

        response = ChatResponse(
            agent=result["agent"],
            response=result["response"],
            sources=result["sources"]
        )

        print("\n" + "=" * 80)
        print("RESPONSE SENT")
        print(response)
        print("=" * 80)

        return response

    except Exception:

        print("\n" + "=" * 80)
        print("EXCEPTION OCCURRED")
        traceback.print_exc()
        print("=" * 80)

        raise