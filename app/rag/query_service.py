"""
Docstring for app.rag.query_service

Retriever
 ↓
Prompt Builder
 ↓
LLM

"""


"""
Retriever
↓
Prompt Builder
↓
LLM
↓
Answer
"""

# rag/query_service.py

from rag.retriever import Retriever

from prompts.prompt_builder import (build_prompt)

from providers.openai_provider import (OpenAIProvider)


class QueryService:

    def __init__(self,
        retriever: Retriever
    ):

        self.retriever = retriever

        self.provider = (OpenAIProvider())

    def ask(self,question: str):

        # Step 1
        chunks = (self.retriever.retrieve(question))

        # Step 2
        context = "\n\n".join(
            [
                doc.page_content
                for doc in chunks
            ]
        )

        # Step 3
        prompt = build_prompt(
            context=context,
            question=question
        )

        # Step 4
        response = (
            self.provider
            .generate_response(
                prompt
            )
        )

        return response