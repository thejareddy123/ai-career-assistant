
from prompts.career_prompt import build_prompt
from memory.conversation_memory import save_message,get_history
from memory.context_manager import get_recent_context
from memory.memory_extractor import extract_memory
from memory.session_memory import create_session, session_exists
from memory.memory_retriever import retrieve_memory
from memory.memory_updater import update_memory

def chat(message, session_id):

    save_message(session_id, "user", message)

    extracted_memory = extract_memory(message)

    current_memory = get_memory(session_id)

    updated_memory = update_memory(current_memory,extracted_memory)

    save_memory(session_id,updated_memory)

    history = get_history(session_id)

    context = get_recent_context(history)

    relevant_memory = retrieve_memory(updated_memory,message)

    prompt = build_prompt(context,relevant_memory, message)

    response = provider.generate_response(prompt)

    save_message(session_id,"assistant",response) 

    return response



def get_ai_response(user_message: str) -> str:
    prompt = build_prompt(user_message)

    print(prompt)  # Development debugging

    return f"Mock AI Response for: {user_message}"\
    

"""
1. Save User Message

2. Extract Memory

3. Update Long-Term Memory

4. Load History

5. Get Context

6. Retrieve Relevant Memory

7. Build Prompt

8. Call AI

9. Save AI Response

10. Return Response
"""