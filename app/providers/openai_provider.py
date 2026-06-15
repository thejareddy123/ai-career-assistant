# providers/openai_provider.py

class OpenAIProvider:

    def generate_response(self,prompt: str):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message.content
        )