import sys
from pathlib import Path

# -----------------------------
# Add AI folder to Python Path
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]
ROOT_DIR = BASE_DIR.parent
sys.path.append(str(ROOT_DIR))

from ai.rag import rag_pipeline


def get_recommendations(profile):

    user_profile = {
        "age": profile.age,
        "gender": profile.gender,
        "state": profile.state,
        "income": profile.income,
        "category": profile.category,
        "occupation": profile.occupation,
        "disability": "No"
    }

    response, retrieved_docs = rag_pipeline(user_profile)

    schemes = []

    for doc in retrieved_docs:
        schemes.append(doc.page_content)

    return {
        "response": response,
        "retrieved_schemes": schemes
    }