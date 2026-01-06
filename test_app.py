import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

    page_content = response.data.decode('utf-8')

    assert "Liczba odwiedzin strony:" in page_content