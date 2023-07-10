import json
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['city'] == 'San Francisco'
    assert data['temperature'] == 14
    assert data['weather'] == 'Cloudy'


def test_add_weather_invalid_data(client):
    response = client.post('/weather', json={'city': 'London', 'weather': 'Cloudy'})
    assert response.status_code == 400
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data
    assert data['error'] == 'Invalid data'


def test_update_weather_invalid_city(client):
    response = client.put('/weather/London', json={'temperature': 18, 'weather': 'Sunny'})
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data
    assert data['error'] == 'City not found'


def test_delete_weather_invalid_city(client):
    response = client.delete('/weather/London')
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data
    assert data['error'] == 'City not found'


def test_delete_weather(client):
    response = client.delete('/weather/Austin')
    assert response.status_code == 204
    assert response.data == b''
    # Verify that the weather data for Austin is deleted
    response = client.get('/weather/Austin')
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data
    assert data['error'] == 'City not found'

