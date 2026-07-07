import google.generativeai as genai

from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt: str):
    try:
        print("=" * 80)
        print("Sending Prompt To Gemini...")
        print("=" * 80)

        response = model.generate_content(prompt)

        print("=" * 80)
        print("Gemini Response Received")
        print("=" * 80)

        return response.text

    except Exception as e:
        print("=" * 80)
        print("GEMINI ERROR")
        print(e)
        print("=" * 80)
        raise