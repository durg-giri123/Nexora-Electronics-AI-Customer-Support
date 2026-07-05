from backend.rag.rag_pipeline import rag_answer

SYSTEM_PROMPT = """
You are a helpful AI Customer Support Assistant.
"""

query = "What is the warranty period?"

result = rag_answer(query, SYSTEM_PROMPT)

print("\n========================")
print("RAG ANSWER")
print("========================\n")

print(result["answer"])

print("\n========================")
print("SOURCES")
print("========================\n")

for source in result["sources"]:
    print(f"📄 {source}")