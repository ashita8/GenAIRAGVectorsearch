import faiss
import numpy as np


class FAISSVectorStore:
    """
    Handles vector storage and similarity search using FAISS.
    """

    def __init__(self, embedding_dimension: int):
        """
        Initialize FAISS index.

        Args:
            embedding_dimension: Size of embedding vectors
        """

        self.dimension = embedding_dimension

        # Inner Product index
        # Works as cosine similarity because vectors are normalized
        self.index = faiss.IndexFlatIP(embedding_dimension)

        self.documents = []

    def add_embeddings(self, embeddings: np.ndarray, documents: list[str]):
        """
        Add embeddings and corresponding documents to FAISS.

        Args:
            embeddings: Array of embedding vectors
            documents: Original document chunks
        """

        embeddings = embeddings.astype("float32")

        self.index.add(embeddings)

        self.documents.extend(documents)

    def search(self, query_embedding: np.ndarray, top_k: int = 3):
        """
        Search for most similar documents.

        Args:
            query_embedding: Embedded query vector
            top_k: Number of results to return

        Returns:
            List of matching documents with similarity scores
        """

        query_embedding = np.array([query_embedding]).astype("float32")

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append({
                "document": self.documents[idx],
                "score": float(score)
            })

        return results