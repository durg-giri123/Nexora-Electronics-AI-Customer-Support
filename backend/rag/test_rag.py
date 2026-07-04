from backend.rag.rag_pipeline import rag_answer

query = "What is the warranty period?"

answer = rag_answer(query)

print("\n========================")
print("RAG ANSWER")
print("========================\n")

print(answer)