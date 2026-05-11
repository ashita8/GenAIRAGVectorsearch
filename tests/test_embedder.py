from app.embedding.embedder import Embedder


def test_single_embedding_generation():

    embedder = Embedder()

    text = "Autoscaling handles peak traffic."

    embedding = embedder.embed_text(text)

    assert embedding is not None

    assert len(embedding.shape) == 1

    assert embedding.shape[0] > 0


def test_multiple_embedding_generation():

    embedder = Embedder()

    documents = [
        "Kubernetes autoscaling",
        "Load balancing systems"
    ]

    embeddings = embedder.embed_documents(documents)

    assert embeddings.shape[0] == 2 