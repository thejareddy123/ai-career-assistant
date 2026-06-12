"""
Docstring for app.memory.conversation_memory
Create Session
Get Session
Validate Session
Manage Session IDs

"""

conversation_memory = {}  # Dictionary to store conversation history for each session

def save_message(
        session_id:str,
        role:str,
        content:str
):
    """
    save a message to the conversation history of a session
    """
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []
    conversation_memory[session_id].append({
        "role": role,
        "content": content
    })

def get_history(session_id:str):
    """
    get the conversation history of a session
    """
    return conversation_memory.get(session_id, [])
