import os
import re

KNOWLEDGE_FOLDER = "knowledge_base"

documents = []

print("Loading Knowledge Base...")

for filename in os.listdir(KNOWLEDGE_FOLDER):

    if filename.endswith(".txt"):

        filepath = os.path.join(KNOWLEDGE_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as f:

            text = f.read()

            paragraphs = re.split(r"\n\s*\n", text)

            for para in paragraphs:

                para = para.strip()

                if para:

                    documents.append({
                        "text": para,
                        "source": filename
                    })

print(f"Loaded {len(documents)} knowledge chunks.")


def score(query, text):

    # Normalize text
    query = re.sub(r"[^\w\s]", " ", query.lower())
    text = re.sub(r"[^\w\s]", " ", text.lower())

    query_words = set(query.split())
    text_words = set(text.split())

    return len(query_words & text_words)


def retrieve_context(query: str, k: int = 5):

    ranked = sorted(
        documents,
        key=lambda x: score(query, x["text"]),
        reverse=True
    )

    print("\n" + "=" * 80)
    print("QUERY:", query)
    print("=" * 80)

    for i, doc in enumerate(ranked[:10], start=1):
        print(f"\nRank {i}")
        print("Score :", score(query, doc["text"]))
        print("Source:", doc["source"])
        print(doc["text"][:250])
        print("-" * 80)

    top_docs = ranked[:k]

    context = ""
    sources = []

    for doc in top_docs:
        context += doc["text"] + "\n\n"

        if doc["source"] not in sources:
            sources.append(doc["source"])

    print("\n" + "=" * 80)
    print("FINAL CONTEXT")
    print("=" * 80)
    print(context)
    print("=" * 80)
    print("SOURCES:", sources)
    print("=" * 80)

    return context, sources