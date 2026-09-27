import traceback
from gemini_client import client, GEMINI_MODEL

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.

Suggest a structured and adaptive learning path including:
1. Beginner, intermediate, and advanced levels.
2. Key topics at each level.
3. The recommended order of learning.
4. Useful resources such as videos, articles, books, or documentation.
5. A short estimated timeline for each level.

Keep the plan practical and easy to follow.
"""

    try:
        if not client:
            return "⚠ GEMINI_API_KEY is not configured."

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        print("Gemini request completed successfully.")

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "❌ Could not extract content from Gemini response."

    except Exception as e:
        traceback.print_exc()
        return "❌ Error occurred while fetching recommendations."
