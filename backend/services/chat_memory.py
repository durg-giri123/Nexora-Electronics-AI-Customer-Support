conversation_history = []


def add_message(role, message):
    conversation_history.append({
        "role": role,
        "message": message
    })

    # Keep last 10 messages
    if len(conversation_history) > 10:
        conversation_history.pop(0)


def get_history():

    history = ""

    for msg in conversation_history:
        history += f"{msg['role']}: {msg['message']}\n"

    return history


def clear_history():
    conversation_history.clear()