from backend.rag.retriever import retrieve_context

query = "What is the warranty period?"

context = retrieve_context(query)

print("\nRetrieved Context:\n")
print(context)