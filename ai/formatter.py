def format_response(response: str) -> str:
    """
    Clean the AI response and return it.
    No extra headings or footers.
    """

    response = response.strip()

    # Remove unwanted duplicate headings if Gemini generates them
    unwanted = [
        "🇮🇳 AI Government Scheme Recommendation",
        "Thank you for using AI Government Scheme Assistant",
        "Hope this helps!",
        "Thank you!"
    ]

    for text in unwanted:
        response = response.replace(text, "")

    # Remove extra blank lines
    while "\n\n\n" in response:
        response = response.replace("\n\n\n", "\n\n")

    return response.strip()