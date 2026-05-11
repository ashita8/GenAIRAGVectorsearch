from embedding.embedder import Embedder
from vectordb.faiss_store import FAISSVectorStore


class Retriever:
    """
    Orchestrates embedding generation and vector retrieval.
    """

    def __init__(self):

        self.embedder = Embedder()

        self.vector_store = None

    def ingest_documents(self, documents: list[str]):
        """
        Embed and store documents inside FAISS.
        """

        print("Generating document embeddings...")

        embeddings = self.embedder.embed_documents(documents)

        embedding_dimension = embeddings.shape[1]

        self.vector_store = FAISSVectorStore(
            embedding_dimension=embedding_dimension
        )

        self.vector_store.add_embeddings(
            embeddings,
            documents
        )

        print(f"Ingested {len(documents)} documents")

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve top matching documents for query.
        """

        if self.vector_store is None:
            raise ValueError(
                "Documents must be ingested before retrieval."
            )

        query_embedding = self.embedder.embed_text(query)

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        return results