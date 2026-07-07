from backend.rag.retriever import retrieve_context
from backend.services.gemini_service import ask_gemini
from backend.services.chat_memory import (
    add_message,
    get_history
)


def rag_answer(query: str, system_prompt: str):

    context, sources = retrieve_context(query)

    history = get_history()

    final_prompt = f"""
{system_prompt}

==================================================

Conversation History

{history}

==================================================

Company Knowledge Base

{context}

==================================================

Customer Question

{query}

==================================================

Instructions:

1. Use the conversation history if helpful.

2. Answer ONLY using the company knowledge.

3. If the answer is not present in the knowledge base, reply exactly:

"I couldn't find this information in the company's knowledge base."

4. Keep the answer concise.

5. Be professional.
"""

    answer = ask_gemini(final_prompt)

    add_message("User", query)
    add_message("Assistant", answer)

    return {
        "answer": answer,
        "sources": sources
    }