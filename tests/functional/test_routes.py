import json

from tests.fixtures.data import minimal_xml
from tests.fixtures.server_client import client


def test_billing(client, minimal_xml):
    """
    GIVEN a morpher Flask application
    WHEN the '/api/ehf/invoice' page is requested (POST)
    THEN check that the response is valid
    """
    response = client.post(
        "/api/ehf/invoice",
        json={
            "invoice": minimal_xml
        },
    )
    assert response.status_code == 200


def test_billing_valid(client, minimal_xml):
    """
    GIVEN a morpher Flask application
    WHEN the '/api/ehf/invoice' page is requested (POST)
    THEN check that the response is valid
    """
    response = client.post(
        "/api/ehf/invoice",
        json={
            "invoice": minimal_xml
        },
    )
    invoice = json.dumps(json.loads(response.data)["invoice"])
    assert invoice == '{"Invoice": {"ID": "2209000026085"}}'
