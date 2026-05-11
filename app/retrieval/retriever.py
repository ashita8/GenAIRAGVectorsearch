from app.embedding.embedder import Embedder
from app.vectordb.faiss_store import FAISSVectorStore
from app.retrieval.query_expander import QueryExpander

class Retriever:
    """
    Orchestrates embedding generation and retrieval.
    """

    def __init__(self):

        self.embedder = Embedder()

        self.query_expander = QueryExpander()

        self.vector_store = None

    def ingest_documents(self, documents: list[str]):

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

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        expand_query: bool = False
    ):

        if self.vector_store is None:
            raise ValueError(
                "Documents must be ingested before retrieval."
            )

        original_query = query

        # Strategy B
        if expand_query:

            query = self.query_expander.expand_query(query)

            print("\nExpanded Query:")
            print(query)

        query_embedding = self.embedder.embed_text(query)

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        return {
            "original_query": original_query,
            "used_query": query,
            "results": results
        }