# prompts/prompt_builder.py

def build_prompt(
    context,
    memory,
    question
):

    prompt = """
You are an AI Learning Assistant.

"""

    if memory:

        prompt += "\nKnown User Facts:\n"

        for key, value in memory.items():

            prompt += f"{key}: {value}\n"

    if context:

        prompt += "\nRecent Conversation:\n"

        for message in context:

            role = message["role"]
            content = message["content"]

            prompt += (
                f"{role}: {content}\n"
            )

    prompt += (
        f"\nCurrent Question:\n"
        f"{question}"
    )

    return prompt