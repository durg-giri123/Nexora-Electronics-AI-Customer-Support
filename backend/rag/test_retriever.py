from backend.rag.retriever import retrieve_context

queries = [
    "What is the warranty period?",
    "How many days does a refund take?",
    "How long does shipping take?",
    "When is technical support available?",
    "Do I need an invoice for warranty?",
    "What products does Nexora manufacture?",
    "How can I claim my warranty?"
]

for query in queries:

    print("=" * 80)
    print(f"Query: {query}")
    print("=" * 80)

    context, sources = retrieve_context(query)

    print("\nRetrieved Sources:")

    for source in sources:
        print(f"📄 {source}")

    print("\n")