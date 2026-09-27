import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

def get_gemini_client():
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")
    return genai.Client(api_key=GEMINI_API_KEY)

try:
    client = get_gemini_client()
except ValueError as e:
    client = None
    print(f"Warning: {e}", file=sys.stderr)
