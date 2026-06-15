# memory/memory_store.py User Facts

memory_db = {}


def get_memory(session_id: str) -> dict:

    return memory_db.get(session_id,{})


def save_memory(session_id: str,
    memory: dict):

    memory_db[session_id] = memory