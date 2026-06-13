# memory/memory_updater.py

def update_memory(
    current_memory: dict,
    extracted_memory: dict
) -> dict:

    # Handle skills

    if "skills" in extracted_memory:

        if "skills" not in current_memory:
            current_memory["skills"] = []

        for skill in extracted_memory["skills"]:

            if skill not in current_memory["skills"]:
                current_memory["skills"].append(skill)

    # Handle experience level

    if "experience_level" in extracted_memory:
        current_memory["experience_level"] = (
            extracted_memory["experience_level"]
        )

    return current_memory