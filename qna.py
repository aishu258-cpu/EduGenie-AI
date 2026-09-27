from gemini_client import client, GEMINI_MODEL

def answer_question_with_gemini(question: str) -> str:
    try:
        if not client:
            return "⚠ GEMINI_API_KEY is not configured."

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=question
        )
        return response.text.strip()

    except Exception as e:
        return "⚠ Error in QnA: Failed to generate content. Please check API key and model availability."
