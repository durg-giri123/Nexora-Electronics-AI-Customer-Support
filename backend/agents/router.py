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
        result = billing_agent(query)
        agent = "Billing Support"

    elif intent == "technical":
        result = technical_agent(query)
        agent = "Technical Support"

    elif intent == "product":
        result = product_agent(query)
        agent = "Product Specialist"

    elif intent == "complaint":
        result = complaint_agent(query)
        agent = "Complaint Resolution"

    else:
        result = faq_agent(query)
        agent = "FAQ Assistant"

    return {
        "agent": agent,
        "response": result["answer"],
        "sources": result["sources"]
    }