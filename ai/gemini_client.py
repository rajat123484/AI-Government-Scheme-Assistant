from google import genai
from ai.config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt):
    """
    Generate response using Gemini 2.5 Flash
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return f"Error: {e}"