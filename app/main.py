from embedding.embedder import Embedder
from vectordb.faiss_store import FAISSVectorStore
from data.documents import DOCUMENTS


def main():

    # Initialize embedder
    embedder = Embedder()

    # Generate document embeddings
    document_embeddings = embedder.embed_documents(DOCUMENTS)

    print("Generated embeddings:", document_embeddings.shape)

    # Create vector store
    vector_store = FAISSVectorStore(
        embedding_dimension=document_embeddings.shape[1]
    )

    # Store embeddings
    vector_store.add_embeddings(
        document_embeddings,
        DOCUMENTS
    )

    print("Documents added to FAISS index")

    # Example query
    query = "How does the system handle peak load?"

    query_embedding = embedder.embed_text(query)

    results = vector_store.search(query_embedding, top_k=3)

    print("\nTop Results:\n")

    for idx, result in enumerate(results, start=1):
        print(f"Result {idx}")
        print("Score:", round(result["score"], 4))
        print(result["document"])
        print("-" * 50)


if __name__ == "__main__":
    main()