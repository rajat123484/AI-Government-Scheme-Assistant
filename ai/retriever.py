from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# =====================================================
# Load Embedding Model
# =====================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =====================================================
# Load FAISS Vector Database
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

VECTOR_DB_PATH = BASE_DIR / "vector_db"

vector_store = FAISS.load_local(
    folder_path=str(VECTOR_DB_PATH),
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)


# =====================================================
# Retrieve Relevant Schemes
# =====================================================

def retrieve_documents(query, k=10):
    """
    Retrieves diverse and relevant schemes using
    Max Marginal Relevance (MMR).
    """

    docs = vector_store.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=20
    )

    # Remove duplicate schemes
    unique_docs = []
    seen = set()

    for doc in docs:

        name = doc.metadata.get(
            "scheme_name",
            doc.page_content[:50]
        )

        if name not in seen:
            seen.add(name)
            unique_docs.append(doc)

    return unique_docs


# =====================================================
# Debug
# =====================================================

if __name__ == "__main__":

    query = """
    21 year old male student
    from Uttar Pradesh
    annual income 150000
    """

    docs = retrieve_documents(query)

    print("=" * 80)

    for i, doc in enumerate(docs, 1):

        print(f"\nResult {i}")

        print("-" * 80)

        print(
            doc.metadata.get(
                "scheme_name",
                "Unknown Scheme"
            )
        )

        print()

        print(doc.page_content[:500])

        print("=" * 80)