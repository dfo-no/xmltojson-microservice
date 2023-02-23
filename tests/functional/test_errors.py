import pytest

from morpher import create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client


def test_404(client):
    """
    GIVEN a Flask application
    WHEN requesting a non-existing route
    THEN check that the response is valid
    """
    response = client.get("/api/does/not/exist")
    assert response.status_code == 404
    assert response.json["error"] == "not found"


def test_405(client):
    """
    GIVEN a Flask application
    WHEN requesting a non-existing method
    THEN check that the response is valid
    """
    response = client.get("/api/minimal/invoice")
    assert response.status_code == 405
    assert response.json["error"] == "method not allowed"
