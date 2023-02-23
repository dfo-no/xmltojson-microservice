from morpher import create_app
from tests.fixtures.data import xml
from tests.fixtures.server_client import client


def test_minimal_invoice_route(client, xml):
    """
    GIVEN the Flask app
    WHEN the /minimal/invoice route is requested (POST)
    THEN check that the response is valid
    """
    response = client.post(
        "/api/minimal/invoice",
        json={"invoice": xml},
    )
    assert response.status_code == 200
    assert response.json["invoice"] == {
        "Invoice": {
            "ID": "123456789",
            "SupplierID": "123456789",
            "CustomerID": "987654321",
        }
    }
