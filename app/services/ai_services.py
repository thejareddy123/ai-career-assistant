from app.prompts.career_prompt import build_career_prompt


def get_ai_response(user_message: str) -> str:
    prompt = build_career_prompt(user_message)

    print(prompt)  # Development debugging

    return f"Mock AI Response for: {user_message}"