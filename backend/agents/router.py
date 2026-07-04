from backend.services.router_service import classify_query
from backend.agents.billing import billing_agent
from backend.agents.technical import technical_agent
from backend.agents.product import product_agent
from backend.agents.complaint import complaint_agent
from backend.agents.faq import faq_agent


def route_query(query: str):

    intent = classify_query(query)

    print(f"Detected Intent: {intent}")

    if intent == "billing":
        return {
            "agent": "Billing Support",
            "response": billing_agent(query)
        }

    elif intent == "technical":
        return {
            "agent": "Technical Support",
            "response": technical_agent(query)
        }

    elif intent == "product":
        return {
            "agent": "Product Specialist",
            "response": product_agent(query)
        }

    elif intent == "complaint":
        return {
            "agent": "Complaint Resolution",
            "response": complaint_agent(query)
        }

    else:
        return {
            "agent": "FAQ Assistant",
            "response": faq_agent(query)
        }