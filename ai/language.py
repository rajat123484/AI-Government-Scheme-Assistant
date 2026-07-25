def detect_language(text: str) -> str:
    """
    Very simple language detector.
    Returns:
        english
        hindi
        hinglish
    """

    # Detect Devanagari characters
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return "hindi"

    # Common Hinglish words
    hinglish_words = [
        "mera",
        "meri",
        "main",
        "mujhe",
        "hai",
        "hoon",
        "karna",
        "scheme",
        "yojana",
        "paise"
    ]

    text = text.lower()

    for word in hinglish_words:
        if word in text:
            return "hinglish"

    return "english"