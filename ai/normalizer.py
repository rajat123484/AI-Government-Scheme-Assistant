def normalize_value(value):
    """
    Converts Hindi/Hinglish values into standard English values.
    """

    mapping = {

        # Occupation
        "student": "student",
        "students": "student",
        "छात्र": "student",
        "विद्यार्थी": "student",

        "farmer": "farmer",
        "किसान": "farmer",

        # Gender
        "male": "male",
        "पुरुष": "male",
        "ladka": "male",

        "female": "female",
        "महिला": "female",
        "लड़की": "female",
        "ladki": "female",

        # Disability
        "yes": "yes",
        "haan": "yes",
        "हाँ": "yes",

        "no": "no",
        "nahi": "no",
        "नहीं": "no",

        # States
        "uttar pradesh": "uttar pradesh",
        "up": "uttar pradesh",
        "उत्तर प्रदेश": "uttar pradesh",

        # Categories
        "general": "general",
        "obc": "obc",
        "sc": "sc",
        "st": "st"
    }

    value = str(value).strip().lower()

    return mapping.get(value, value)