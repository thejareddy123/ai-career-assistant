
from app.prompts.career_prompt import build_prompt
from app.memory.conversation_memory import save_message,get_history
from app.memory.context_manager import get_recent_context
from app.memory.memory_extractor import extract_memory
from app.memory.session_memory import create_session, session_exists
from app.memory.memory_retriever import retrieve_memory
from app.memory.memory_updater import update_memory
from app.memory.memory_store import get_memory, save_memory
from app.providers import mock_provider as provider

def chat(session_id: str,message: str):

    # Save User Message

    save_message(session_id,"user",message)

    # Extract Memory

    extracted_memory = extract_memory(message)

    # Load Existing Memory

    current_memory = get_memory(session_id)

    # Update Memory

    updated_memory = update_memory(current_memory,extracted_memory)

    # Save Memory

    save_memory(session_id,updated_memory)

    # Load History

    history = get_history(session_id)

    # Build Context

    context = get_recent_context(history)

    # Retrieve Memory

    relevant_memory = retrieve_memory(updated_memory,message)

    # Build Prompt

    prompt = build_prompt(context,relevant_memory,message)

    # Generate Response

    response = provider.generate_response(prompt)

    # Save AI Response

    save_message(session_id,"assistant",response)

    return response




    

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