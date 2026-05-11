from app.retrieval.query_expander import QueryExpander


def test_query_expansion():

    expander = QueryExpander()

    query = "How does the system handle peak load?"

    expanded_query = expander.expand_query(query)

    assert expanded_query != query

    assert "autoscaling" in expanded_query