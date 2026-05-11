from retrieval.retriever import Retriever
from data.documents import DOCUMENTS


def main():

    retriever = Retriever()

    # Ingest documents
    retriever.ingest_documents(DOCUMENTS)

    # Example query
    query = "How does the system handle peak load?"

    print("\nUser Query:")
    print(query)

    results = retriever.retrieve(query)

    print("\nTop Retrieved Results:\n")

    for idx, result in enumerate(results, start=1):

        print(f"Result {idx}")
        print("Similarity Score:", round(result["score"], 4))
        print(result["document"])
        print("-" * 50)


if __name__ == "__main__":
    main()