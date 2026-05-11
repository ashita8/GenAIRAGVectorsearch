from app.retrieval.retriever import Retriever
from app.data.documents import DOCUMENTS


def test_document_ingestion():

    retriever = Retriever()

    retriever.ingest_documents(DOCUMENTS)

    assert retriever.vector_store is not None


def test_retrieval_results():

    retriever = Retriever()

    retriever.ingest_documents(DOCUMENTS)

    results = retriever.retrieve(
        "How does autoscaling work?"
    )

    assert len(results["results"]) > 0