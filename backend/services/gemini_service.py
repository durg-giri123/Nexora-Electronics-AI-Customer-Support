import google.generativeai as genai

from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, the AI service is temporarily unavailable. Please try again after some time."