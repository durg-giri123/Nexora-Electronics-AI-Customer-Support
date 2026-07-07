from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = None
vectorstore = None


def load_vectorstore():
    global embedding_model, vectorstore

    if embedding_model is None:
        print("Loading embedding model...")
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding model loaded.")

    if vectorstore is None:
        print("Loading FAISS index...")
        vectorstore = FAISS.load_local(
            "backend/vectorstore/faiss_index",
            embedding_model,
            allow_dangerous_deserialization=True
        )
        print("FAISS index loaded.")

    return vectorstore


def retrieve_context(query: str, k: int = 5):

    store = load_vectorstore()

    docs = store.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=10
    )

    context = ""
    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source", "Unknown")
        source = source.replace("\\", "/").split("/")[-1]

        if source not in sources:
            sources.append(source)

    return context, sources