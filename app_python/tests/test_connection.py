from time_app import create_app

def test_connection(client):
    response = client.get('/')
    assert response.status_code == 200