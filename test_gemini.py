import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

def test_gemini():
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL")
    
    print(f"GEMINI_API_KEY loaded: {bool(api_key)}")
    print(f"GEMINI_MODEL: {model_name}")
    
    if api_key:
        print(f"API key prefix: {api_key[:4]}...")
        
    if not api_key:
        print("Cannot test Gemini, API key is missing.")
        return
        
    try:
        print("Testing Gemini connection...")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents="Say hello in one word."
        )
        print("Success! Gemini response:")
        print(response.text)
    except APIError as e:
        print(f"APIError: {e.message}")
    except Exception as e:
        print(f"Error connecting to Gemini: {e}")

if __name__ == "__main__":
    test_gemini()
