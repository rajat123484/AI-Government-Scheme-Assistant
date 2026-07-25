from ai.retriever import retrieve_documents
from ai.gemini_client import generate_response
from ai.formatter import format_response

from ai.prompts import (
    SYSTEM_PROMPT,
    RECOMMENDATION_PROMPT
)


# ==========================================================
# Build Search Query
# ==========================================================

def build_search_query(user_profile):
    """
    Convert the user profile into a natural language query
    for better semantic retrieval.
    """

    query = f"""
Find the most suitable Indian Government Schemes for the following person.

Age: {user_profile.get('age')}

Gender: {user_profile.get('gender')}

Occupation: {user_profile.get('occupation')}

State: {user_profile.get('state')}

Annual Family Income: ₹{user_profile.get('income')}

Category: {user_profile.get('category')}

Disability: {user_profile.get('disability')}

Prioritize schemes related to:

• Scholarships
• Education
• Employment
• Skill Development
• Entrepreneurship
• Financial Assistance
• Insurance
• Social Welfare

Only retrieve schemes genuinely relevant to this profile.
"""

    return query.strip()


# ==========================================================
# RAG PIPELINE
# ==========================================================

def rag_pipeline(user_profile):

    query = build_search_query(user_profile)

    print("\n================ SEARCH QUERY ================\n")
    print(query)

    # ======================================================
    # FORCE ENGLISH RESPONSE
    # ======================================================

    language = "English"

    # ======================================================
    # RETRIEVE RELEVANT SCHEMES
    # ======================================================

    retrieved_docs = retrieve_documents(
        query=query,
        k=8
    )

    # ======================================================
    # NO RESULTS
    # ======================================================

    if not retrieved_docs:

        return (
            "Sorry! I couldn't find any matching government scheme."
        ), []

    # ======================================================
    # BUILD CONTEXT FOR GEMINI
    # ======================================================

    context = ""

    for i, doc in enumerate(retrieved_docs, 1):

        text = doc.page_content

        context += f"""
==============================

SCHEME {i}

{text}

==============================
"""

    print("\n============= CONTEXT SENT TO GEMINI =============\n")
    print(context)
    print("\n===================================================\n")

    # ======================================================
    # GENERATE RECOMMENDATION PROMPT
    # ======================================================

    prompt = f"""
{SYSTEM_PROMPT}

IMPORTANT LANGUAGE INSTRUCTION:

The final response MUST be written entirely in English.

Do NOT use:
- Hindi
- Hinglish
- Hindi words written in English letters
- Mixed Hindi-English sentences

Use clear, professional, simple English only.

{RECOMMENDATION_PROMPT.format(
    profile=user_profile,
    context=context,
    language=language
)}

FINAL LANGUAGE REQUIREMENT:

Return the recommendation completely in English.
Do not translate or mix languages.
"""

    # ======================================================
    # GENERATE GEMINI RESPONSE
    # ======================================================

    response = generate_response(prompt)

    # ======================================================
    # FORMAT RESPONSE
    # ======================================================

    response = format_response(response)

    line = "=" * 70

    final_response = f"""
{line}
🇮🇳 AI Government Scheme Recommendation
{line}

{response}
"""

    return final_response.strip(), retrieved_docs