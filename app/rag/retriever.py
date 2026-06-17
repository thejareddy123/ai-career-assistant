"""
Question
 ↓
Find Relevant Chunks

"""


# rag/retriever.py

from rag.vector_store import VectorStore


class Retriever:

    def __init__(self,vector_store: VectorStore):

        self.vector_store = vector_store

    def retrieve(self,question: str,k: int = 3):

        results = (self.vector_store.similarity_search(query=question,k=k))

        return results