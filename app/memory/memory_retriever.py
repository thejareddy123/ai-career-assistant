"""
Long-Term Memory
      ↓
Retrieve Relevant Facts
      ↓
Prompt Builder
"""
#memorty_retriever.py is used to retrieve relevant facts from the long-term memory based on the user's question. 
# It is a crucial component of the system that ensures the AI can provide accurate and contextually appropriate responses.

def retrieve_memory(
    memory: dict,
    question: str) -> dict:

    relevant_memory = {}
    question = question.lower()

    #learning Questions

    if ("learn" in question 
        or "skill" in question
        or "experience" in question
        or "project" in question
        or "roadmap" in question
        ):
        if "skills" in memory:
            relevant_memory["skills"] = memory["skills"]
        if "goals" in memory:
            relevant_memory["goals"] = memory["goals"]
    
    #goal questions

    if "goal" in question:
        if "goals" in memory:
            relevant_memory["goals"] = memory["goals"]

    return relevant_memory