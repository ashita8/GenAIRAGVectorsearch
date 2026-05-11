from retrieval.retriever import Retriever
from data.documents import DOCUMENTS


def print_results(title, retrieval_output):

    print(f"\n{'=' * 60}")
    print(title)
    print(f"{'=' * 60}")

    print("\nOriginal Query:")
    print(retrieval_output["original_query"])

    print("\nUsed Query:")
    print(retrieval_output["used_query"])

    print("\nTop Results:\n")

    for idx, result in enumerate(
        retrieval_output["results"],
        start=1
    ):

        print(f"Result {idx}")

        print(
            "Similarity Score:",
            round(result["score"], 4)
        )

        print(result["document"])

        print("-" * 50)


def main():

    retriever = Retriever()

    retriever.ingest_documents(DOCUMENTS)

    query = "How does the system handle peak load?"

    # Strategy A
    strategy_a = retriever.retrieve(
        query=query,
        expand_query=False
    )

    # Strategy B
    strategy_b = retriever.retrieve(
        query=query,
        expand_query=True
    )

    print_results(
        "Strategy A - Raw Vector Search",
        strategy_a
    )

    print_results(
        "Strategy B - AI Enhanced Retrieval",
        strategy_b
    )


if __name__ == "__main__":
    main()