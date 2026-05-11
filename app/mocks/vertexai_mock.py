from embedding.embedder import Embedder


class TextEmbeddingModel:
    """
    Mock version of Vertex AI TextEmbeddingModel.
    """

    def __init__(self):
        self.embedder = Embedder()

    def get_embeddings(self, texts: list[str]):
        """
        Generate embeddings for input texts.
        """

        return self.embedder.embed_documents(texts)


class GenerativeModel:
    """
    Mock version of Vertex AI GenerativeModel.
    Used for query expansion/rewriting.
    """

    def generate_content(self, query: str) -> str:

        query = query.lower()

        expansion_rules = {

            "peak load":
                "high traffic concurrent requests autoscaling load balancing scalability",

            "slow response":
                "latency performance bottleneck response time optimization",

            "system failure":
                "fault tolerance redundancy failover recovery resilience",

            "database issue":
                "database replication consistency backup recovery scaling",

            "traffic spike":
                "sudden increase in requests autoscaling load balancer queue handling"
        }

        expanded_query = query

        for keyword, expansion in expansion_rules.items():

            if keyword in query:
                expanded_query += " " + expansion

        return expanded_query