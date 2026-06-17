"""

Loader
 ↓
Chunker
 ↓
Embeddings
 ↓
Vector Store

"""


"""
PDF Upload
     │
     ▼
Ingestion Service
     │
     ├── Document Loader
     ├── Text Chunker
     ├── Embedding Service
     └── Vector Store
     excatly like ai_service
"""

# rag/ingestion_service.py

from rag.document_loader import DocumentLoader
from rag.text_chunker import TextChunker
from rag.embedding_service import EmbeddingService
from rag.vector_store import VectorStore


class IngestionService:

    def __init__(self):

        self.embedding_service = (EmbeddingService())

        self.vector_store = (VectorStore(
            self.embedding_service.embedding_model)
        )

    def ingest_pdf(self,file_path: str ):

        # Step 1
        text = (
            DocumentLoader.load_pdf(file_path))

        # Step 2
        chunks = (TextChunker.create_chunks(text))

        # Step 3
        self.vector_store.add_documents(chunks)

        return {
            "message":
            "Document indexed successfully",

            "chunks_count":
            len(chunks)
        }