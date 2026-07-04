from backend.rag.retriever import retrieve_context
from backend.services.gemini_service import ask_gemini


def rag_answer(query: str, system_prompt: str):

    context = retrieve_context(query)

    final_prompt = f"""
{system_prompt}

===================================================

Company Knowledge Base

{context}

===================================================

Customer Question

{query}

===================================================

Instructions:

1. Answer ONLY using the company knowledge.
2. If the answer is not present in the knowledge base, reply exactly:
   "I couldn't find this information in the company's knowledge base."
3. Keep the answer concise.
4. Be professional.
"""

    return ask_gemini(final_prompt)