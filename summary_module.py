from gemini_client import client, GEMINI_MODEL

def summarize_text(text: str) -> str:
    try:
        if not client:
            return "⚠ GEMINI_API_KEY is not configured."

        prompt = f"""Summarize the following text in simple language:

{text}
"""

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        return "⚠ Error in Summary: API request failed. Please check your model availability."
