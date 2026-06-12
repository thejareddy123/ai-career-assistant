"""
Docstring for app.memory.context_manager
Load History
↓
Select Relevant Messages
↓
Control Context Size
↓
Build Context

"""
def get_recent_context(
    history: list,
    limit: int = 5
):
    return history[-limit:]