from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

print("Step 1: Loading embedding model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("✅ Embedding model loaded")

print("Step 2: Loading FAISS index...")

vectorstore = FAISS.load_local(
    "backend/vectorstore/faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

print("✅ FAISS loaded")


def retrieve_context(query: str, k: int = 3):

    docs = vectorstore.similarity_search(query, k=k)

    context = ""
    sources = []

    for doc in docs:
        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source", "Unknown")

        source = source.replace("\\", "/").split("/")[-1]

        if source not in sources:
            sources.append(source)

    return context, sources