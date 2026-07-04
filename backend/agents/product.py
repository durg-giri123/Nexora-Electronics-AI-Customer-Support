from backend.rag.rag_pipeline import rag_answer

SYSTEM_PROMPT = """
You are a Product Recommendation Specialist at Nexora Electronics.

Responsibilities:
- Recommend suitable products
- Compare products
- Explain product features
- Help customers choose the best option

Recommend only using the company knowledge base.
"""


def product_agent(query: str):
    return rag_answer(query, SYSTEM_PROMPT)