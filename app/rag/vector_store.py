"""
Docstring for app.rag.vector_store

Chunk
+
Embedding
"""

# rag/vector_store.py

from langchain_chroma import Chroma


# rag/vector_store.py

from langchain_chroma import Chroma


class VectorStore:

    def __init__(
        self,
        embedding_model
    ):

        self.db = Chroma(
            collection_name="documents",
            embedding_function=embedding_model,
            persist_directory="./chroma_db"
        )

    def add_documents(
        self,
        chunks: list[str]
    ):

        self.db.add_texts(
            texts=chunks
        )

    def similarity_search(
        self,
        query: str,
        k: int = 3
    ):

        results = self.db.similarity_search(
            query=query,
            k=k
        )

        return results