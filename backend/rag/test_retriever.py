from backend.rag.retriever import retrieve_context

query = "My laptop is overheating."

context, sources = retrieve_context(query)

print("\nRetrieved Context:\n")
print(context)

print("\nRetrieved Sources:\n")
for source in sources:
    print(f"📄 {source}")