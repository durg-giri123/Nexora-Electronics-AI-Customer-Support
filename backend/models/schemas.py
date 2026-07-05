from typing import List

from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    agent: str
    response: str
    sources: List[str]