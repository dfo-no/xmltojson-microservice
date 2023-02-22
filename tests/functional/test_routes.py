import json

from morpher import create_app


def test_billing():
    """
    GIVEN a morpher Flask application
    WHEN the '/api/ehf/invoice' page is requested (POST)
    THEN check that the response is valid
    """
    app = create_app()
    client = app.test_client()
    response = client.post(
        "/api/ehf/invoice",
        json={
            "invoice": """<?xml version="1.0" encoding="UTF-8"?>
<Invoice
        xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
        xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <cbc:ID>2209000026085</cbc:ID>
</Invoice>
"""
        },
    )
    assert response.status_code == 200


def test_billing_valid():
    """
    GIVEN a morpher Flask application
    WHEN the '/api/ehf/invoice' page is requested (POST)
    THEN check that the response is valid
    """
    app = create_app()
    client = app.test_client()
    response = client.post(
        "/api/ehf/invoice",
        json={
            "invoice": """<?xml version="1.0" encoding="UTF-8"?>
<Invoice
        xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
        xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <cbc:ID>2209000026085</cbc:ID>
</Invoice>
"""
        },
    )
    invoice = json.dumps(json.loads(response.data)["invoice"])
    assert invoice == '{"Invoice": {"ID": "2209000026085"}}'
