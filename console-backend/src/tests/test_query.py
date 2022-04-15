import json

def test_valid_query(test_app):
    client = test_app.test_client()

    # valid query
    query = """
        MATCH (r:Restaurant)<-[:ATE_AT]-(p:Person)
        RETURN p.name AS person, r.name AS restaurant;
    """

    resp = client.post('/query', json={
        "query": query
    })
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'success' in data['result']

def test_invalid_query(test_app):
    client = test_app.test_client()
    
    # invalid query
    query = """
        ERR (r:Restaurant)<-[:ATE_AT]-(p:Person)
        RETURN p.name AS person, r.name AS restaurant;
    """
    
    resp = client.post('/query', json={
        "query": query
    })
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'fail' in data['result']