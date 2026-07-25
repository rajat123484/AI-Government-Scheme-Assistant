def get_chat_response(question: str):

    q = question.lower()

    if "document" in q:
        return "Required documents: Aadhaar Card, Income Certificate, Residence Certificate, Bank Passbook, Passport Size Photograph."

    if "apply" in q:
        return "You can apply through the official government portal or your nearest CSC center."

    if "benefit" in q:
        return "Benefits depend on the selected scheme, such as scholarships, financial assistance, insurance, or pension support."

    return "I am the backend assistant. AI chat integration will be connected in the next step."