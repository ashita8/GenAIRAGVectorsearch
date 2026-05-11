import json
from app.retrieval.retriever import Retriever
from app.data.documents import DOCUMENTS


TEST_QUERIES = [
    "How does the system handle peak load?",
    "How can the platform recover from failures?",
    "How do services communicate during traffic spikes?"
]


def simplify_results(results):

    simplified = []

    for item in results:

        simplified.append({
            "score": round(item["score"], 4),
            "document": item["document"]
        })

    return simplified


def run_benchmark():

    retriever = Retriever()

    retriever.ingest_documents(DOCUMENTS)

    benchmark_results = []

    for query in TEST_QUERIES:

        print(f"\nRunning benchmark for query:")
        print(query)

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

        benchmark_results.append({
            "query": query,

            "strategy_a": {
                "used_query": strategy_a["used_query"],
                "results": simplify_results(
                    strategy_a["results"]
                )
            },

            "strategy_b": {
                "used_query": strategy_b["used_query"],
                "results": simplify_results(
                    strategy_b["results"]
                )
            }
        })

    return benchmark_results


if __name__ == "__main__":

    results = run_benchmark()

    print("\n" + "=" * 80)
    print("FINAL BENCHMARK RESULTS")
    print("=" * 80)

    formatted_results = json.dumps(
        results,
        indent=4
    )

    print(formatted_results)

    # Save benchmark output
    with open("benchmark_output.json", "w") as file:
        file.write(formatted_results)

    print("\nbenchmark_output.json generated successfully")