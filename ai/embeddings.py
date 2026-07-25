import os
import pandas as pd

from ai.langchain_core.documents import Document
from ai.langchain_community.vectorstores import FAISS
from ai.langchain_huggingface import HuggingFaceEmbeddings


def load_documents(csv_path):
    """
    Load government schemes from CSV
    and convert them into LangChain Documents.
    """

    df = pd.read_csv(csv_path)

    documents = []

    for _, row in df.iterrows():

        content = f"""
Scheme Name:
{row['Scheme Name']}

Objective:
{row['Objective']}

Description:
{row['Description']}

Eligibility:
{row['Eligibility']}

Benefits:
{row['Benefits']}

Required Documents:
{row['Required Documents']}

Income Limit:
{row['Income Limit']}

Age Criteria:
{row['Age Criteria']}

State/Central:
{row['State/Central']}

Category:
{row['Category']}

Keywords:
{row['Keywords']}

Official Link:
{row['Official Link']}
"""

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "id": row["ID"],
                    "scheme_name": row["Scheme Name"],
                    "category": row["Category"],
                    "state": row["State/Central"]
                }
            )
        )

    return documents


def create_vector_database():

    print("📄 Loading CSV Dataset...")

    documents = load_documents("data/government_schemes.csv")

    print(f"✅ Loaded {len(documents)} schemes")

    print("🧠 Loading Embedding Model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("📦 Creating FAISS Vector Database...")

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    os.makedirs("vector_db", exist_ok=True)

    vector_store.save_local("vector_db")

    print("\n🎉 Vector Database Created Successfully!")
    print("📁 Saved in vector_db/")


if __name__ == "__main__":
    create_vector_database()