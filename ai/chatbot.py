from ai.gemini_client import generate_response


def local_answer(question, schemes):
    """
    Answer common follow-up questions locally
    without calling Gemini.
    """

    q = question.lower().strip()

    if not schemes:
        return "I couldn't find any recommended schemes."

    # =============================
    # Best Scheme
    # =============================
    if "best" in q:

        best = schemes[0]

        return f"""
🏆 Based on your profile, the best matching scheme is:

{best.metadata.get("scheme_name")}

It is ranked first because it is the most relevant match for your profile.
""".strip()

    # =============================
    # Eligible
    # =============================
    if "eligible" in q or "eligibility" in q:

        answer = "✅ Based on your profile, you may be eligible for:\n\n"

        for doc in schemes:
            answer += f"• {doc.metadata.get('scheme_name')}\n"

        return answer

    # =============================
    # Explain Scheme
    # =============================
    if "explain" in q or "about" in q:

        for doc in schemes:

            if doc.metadata["scheme_name"].lower() in q:
                return doc.page_content

        return (
            "Please mention the scheme name.\n\n"
            "Example:\n"
            "Explain PM-KISAN"
        )

    # =============================
    # Benefits
    # =============================
    if "benefit" in q:

        answer = ""

        for doc in schemes:

            text = doc.page_content

            start = text.find("Benefits")

            end = text.find("Required Documents")

            if start != -1 and end != -1:

                answer += f"\n📌 {doc.metadata['scheme_name']}\n"

                answer += text[start:end]

                answer += "\n"

        return answer

    # =============================
    # Documents
    # =============================
    if "document" in q:

        answer = ""

        for doc in schemes:

            text = doc.page_content

            start = text.find("Required Documents")

            end = text.find("Official Link")

            if start != -1 and end != -1:

                answer += f"\n📄 {doc.metadata['scheme_name']}\n"

                answer += text[start:end]

                answer += "\n"

        return answer

    # =============================
    # Eligibility Criteria
    # =============================
    if "criteria" in q or "requirement" in q:

        answer = ""

        for doc in schemes:

            text = doc.page_content

            start = text.find("Eligibility")

            end = text.find("Benefits")

            if start != -1 and end != -1:

                answer += f"\n✅ {doc.metadata['scheme_name']}\n"

                answer += text[start:end]

                answer += "\n"

        return answer

    # =============================
    # Website / Apply
    # =============================
    if (
        "website" in q
        or "link" in q
        or "apply" in q
        or "application" in q
    ):

        answer = ""

        for doc in schemes:

            text = doc.page_content

            start = text.find("Official Link")

            if start != -1:

                answer += f"\n🌐 {doc.metadata['scheme_name']}\n"

                answer += text[start:]

                answer += "\n"

        return answer

    # =============================
    # List Schemes
    # =============================
    if (
        "scheme" in q
        or "schemes" in q
        or "all schemes" in q
    ):

        answer = "Here are the schemes recommended for you:\n\n"

        for i, doc in enumerate(schemes, start=1):

            answer += f"{i}. {doc.metadata['scheme_name']}\n"

        return answer

    return None


# ==================================================
# Gemini Chat
# ==================================================

def gemini_chat(question, user_profile, schemes):
    """
    Gemini answers ONLY using the
    recommended schemes.
    """

    context = ""

    for doc in schemes:

        context += doc.page_content
        context += "\n\n--------------------------------------\n\n"

    prompt = f"""
You are an AI Government Scheme Assistant.

User Profile:

{user_profile}

Recommended Government Schemes:

{context}

User Question:

{question}

Rules:

1. Answer ONLY using the recommended schemes above.

2. Never invent any government scheme.

3. Never invent eligibility, benefits, documents or websites.

4. If the answer is unavailable, say:
"I couldn't find this information in the recommended government schemes."

5. Reply in the same language as the user's question.

6. Keep the answer short and easy to understand.

7. If the user asks to compare schemes,
compare ONLY the recommended schemes.

8. If the user asks which scheme is best,
justify using the retrieved information.
"""

    return generate_response(prompt)