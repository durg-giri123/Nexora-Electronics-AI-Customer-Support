import google.generativeai as genai

from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def classify_query(query: str):

    query_lower = query.lower()

    # ---------------- Complaint ----------------
    complaint_keywords = [
        "complaint",
        "damaged",
        "damage",
        "defective",
        "broken delivery",
        "wrong product",
        "poor service",
        "bad service",
        "late delivery",
        "received damaged"
    ]

    # ---------------- Technical ----------------
    technical_keywords = [
        "technical",
        "technical support",
        "not working",
        "not turning on",
        "repair",
        "issue",
        "problem",
        "battery",
        "charging",
        "screen",
        "display",
        "keyboard",
        "touchpad",
        "wifi",
        "bluetooth",
        "speaker",
        "camera",
        "overheating",
        "error"
    ]

    # ---------------- Billing ----------------
    billing_keywords = [
        "payment",
        "paid",
        "billing",
        "bill",
        "transaction",
        "upi",
        "credit card",
        "debit card",
        "invoice",
        "refund",
        "emi"
    ]

    # ---------------- Product ----------------
    product_keywords = [
        "recommend",
        "recommendation",
        "suggest",
        "buy",
        "purchase",
        "compare",
        "best laptop",
        "which laptop",
        "which charger",
        "product"
    ]

    # ---------------- FAQ ----------------
    faq_keywords = [
        "warranty",
        "shipping",
        "delivery time",
        "support timing",
        "working hours",
        "policy",
        "replacement",
        "replace",
        "return"
    ]

    # ---------- Rule Based ----------

    if any(word in query_lower for word in complaint_keywords):
        return "complaint"

    if any(word in query_lower for word in technical_keywords):
        return "technical"

    if any(word in query_lower for word in billing_keywords):
        return "billing"

    if any(word in query_lower for word in product_keywords):
        return "product"

    if any(word in query_lower for word in faq_keywords):
        return "faq"

    # ---------- Gemini Fallback ----------

    prompt = f"""
You are an intent classifier.

Return ONLY one word.

billing
technical
product
complaint
faq

Customer Query:
{query}
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()