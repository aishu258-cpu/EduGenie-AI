import json
import re
from gemini_client import client, GEMINI_MODEL

def clean_json_block(text: str) -> str:
    """Remove Markdown JSON fences if Gemini returns them."""
    return re.sub(
        r"```(?:json)?\n(.*?)```",
        r"\1",
        text,
        flags=re.DOTALL
    ).strip()


def generate_quiz(text: str) -> list:
    try:
        if not client:
            return [{"error": "GEMINI_API_KEY is not configured."}]

        prompt = f"""
You are a quiz generator.

From the following passage, create exactly 3 multiple-choice questions.
Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that exactly matches one of the options.

Format your output as valid JSON, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Do not add any explanation outside the JSON.

Passage:
{text}
"""

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        quiz_text = response.text.strip()
        cleaned_text = clean_json_block(quiz_text)

        quiz = json.loads(cleaned_text)

        if not isinstance(quiz, list):
            raise ValueError("Gemini returned JSON, but it was not a list.")

        return quiz

    except Exception as e:
        return [{"error": "Quiz generation/parsing failed. Please verify API configuration."}]
