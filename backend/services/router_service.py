import google.generativeai as genai

from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def classify_query(query: str):

    # ---------- Rule-Based Routing ----------

    query_lower = query.lower()

    faq_keywords = [
        "warranty",
        "refund",
        "return",
        "replacement",
        "replace",
        "shipping",
        "delivery",
        "invoice",
        "policy",
        "support portal"
    ]

    technical_keywords = [
        "not working",
        "broken",
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
        "overheating"
    ]

    billing_keywords = [
        "payment",
        "paid",
        "bill",
        "billing",
        "transaction",
        "upi",
        "credit card",
        "debit card"
    ]

    complaint_keywords = [
        "complaint",
        "damaged",
        "defective",
        "wrong product",
        "late delivery",
        "poor service"
    ]

    product_keywords = [
        "recommend",
        "suggest",
        "buy",
        "best laptop",
        "which laptop",
        "product",
        "compare"
    ]

    if any(word in query_lower for word in faq_keywords):
        return "faq"

    if any(word in query_lower for word in technical_keywords):
        return "technical"

    if any(word in query_lower for word in billing_keywords):
        return "billing"

    if any(word in query_lower for word in complaint_keywords):
        return "complaint"

    if any(word in query_lower for word in product_keywords):
        return "product"

    # ---------- Gemini Fallback ----------

    prompt = f"""
You are an AI Intent Classifier.

Classify the customer query into EXACTLY ONE category.

Available Categories:

billing
technical
product
complaint
faq

Examples:

What is the warranty period? -> faq

How do I claim warranty? -> faq

When will I get my refund? -> faq

How long does shipping take? -> faq

My laptop is overheating -> technical

Battery drains quickly -> technical

My payment failed -> billing

Show my invoice -> billing

Recommend a gaming laptop -> product

Suggest the best laptop -> product

I received a damaged product -> complaint

The delivery box was broken -> complaint

Return ONLY one word.

Customer Query:

{query}
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()