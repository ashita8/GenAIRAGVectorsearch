from app.mocks.vertexai_mock import GenerativeModel


class QueryExpander:
    """
    Handles AI-enhanced query rewriting.
    """

    def __init__(self):

        self.model = GenerativeModel()

    def expand_query(self, query: str) -> str:
        """
        Rewrite query into embedding-friendly format.
        """

        expanded_query = self.model.generate_content(query)

        return expanded_query