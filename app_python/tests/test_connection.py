def test_connection(client):
    response = client.get('/')
    assert response.status_code == 200
