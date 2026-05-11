from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    """
    Handles text embedding generation using Sentence Transformers.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize embedding model.

        Args:
            model_name: Name of sentence-transformer model
        """
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> np.ndarray:
        """
        Generate normalized embedding for a single text.

        Args:
            text: Input text

        Returns:
            Normalized numpy embedding vector
        """

        embedding = self.model.encode(text)

        # Normalize vector for cosine similarity
        embedding = embedding / np.linalg.norm(embedding)

        return embedding

    def embed_documents(self, documents: list[str]) -> np.ndarray:
        """
        Generate normalized embeddings for multiple documents.

        Args:
            documents: List of text chunks

        Returns:
            Array of normalized embeddings
        """

        embeddings = self.model.encode(documents)

        # Normalize all vectors
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        embeddings = embeddings / norms

        return embeddings