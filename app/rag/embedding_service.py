"""
Docstring for app.rag.embedding_service
Chunk
 ↓
Vector
"""
"""

Chunk:
#FastAPI is a modern Python framework for APIs.

Output:[0.12, -0.45, 0.88, 0.23, ...]
This list of numbers is called an embedding.
"""



# rag/embedding_service.py

from langchain_openai import OpenAIEmbeddings


class EmbeddingService:

    def __init__(self):

        self.embedding_model = (OpenAIEmbeddings())

    def create_embeddings(self,chunks: list[str]):

        return (self.embedding_model.embed_documents(chunks)
        )