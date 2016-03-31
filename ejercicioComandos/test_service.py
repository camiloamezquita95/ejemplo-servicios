import pytest
import service

@pytest.fixture
def client(request):
    client = service.hello()
    return client

def get_users(client):
    return client.get('/api/v1.0/usermgt/users',follow_redirects=True)

def test_get_users(client):
    result = client
    assert b'operativos' in result
