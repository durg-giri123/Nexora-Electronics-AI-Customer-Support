from backend.rag.retriever import retrieve_context
from backend.services.gemini_service import ask_gemini
from backend.services.chat_memory import (
    add_message,
    get_history
)


def rag_answer(query: str, system_prompt: str):

    # Retrieve relevant knowledge
    context, sources = retrieve_context(query)

    print("=" * 80)
    print("RETRIEVED SOURCES")
    print(sources)
    print("=" * 80)

    print("=" * 80)
    print("RETRIEVED CONTEXT")
    print(context)
    print("=" * 80)

    history = get_history()

    final_prompt = f"""
You are Nexora Electronics Customer Support.

{system_prompt}

==================================================

Conversation History

{history}

==================================================

Knowledge Base

{context}

==================================================

Customer Question

{query}

==================================================

Instructions

1. Answer ONLY using the Knowledge Base above.

2. If the Knowledge Base contains information related to the question,
answer naturally in complete sentences.

3. Do NOT ignore partially relevant information.

4. Do NOT invent any information.

5. Reply in a friendly professional tone.

6. ONLY say:

"I couldn't find this information in the company's knowledge base."

when the Knowledge Base section is completely empty or unrelated.
"""

    print("=" * 80)
    print("PROMPT SENT TO GEMINI")
    print(final_prompt)
    print("=" * 80)

    answer = ask_gemini(final_prompt)

    print("=" * 80)
    print("GEMINI ANSWER")
    print(answer)
    print("=" * 80)

    add_message("User", query)
    add_message("Assistant", answer)

    return {
        "answer": answer,
        "sources": sources
    }