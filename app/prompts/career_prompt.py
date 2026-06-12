def build_career_prompt(user_message: str,user_level:str,skills:list) -> str:
    """
    Build a career advisor prompt.
    """

    prompt = f"""
You are an expert career advisor.

Provide:
1. Required Skills
2. Learning Roadmap
3. Projects to Build
4. Interview Preparation Tips

User Question:
{user_message}
"""

    return prompt