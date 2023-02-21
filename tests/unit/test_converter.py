import json

from morpher.lib.converter import Converter


def test_bis_namespaces():
    """
    GIVEN the Converter instance
    WHEN the bis_namespaces property is accessed
    THEN the property should be a dictionary
    """
    converter = Converter()
    assert isinstance(converter.bis_namespaces, dict)


def test_bis_namespace_value():
    """
    GIVEN the Converter instance
    WHEN the bis_namespaces property is accessed
    THEN the following namespaces should be present
    """
    converter = Converter()
    assert (
        "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
        in converter.bis_namespaces
    )
    assert "http://www.w3.org/2001/XMLSchema" in converter.bis_namespaces
    assert (
        "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        in converter.bis_namespaces
    )
    assert (
        "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        in converter.bis_namespaces
    )
    assert (
        "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        in converter.bis_namespaces
    )
    assert (
        "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
        in converter.bis_namespaces
    )
    assert (
        "urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2"
        in converter.bis_namespaces
    )
    assert "http://www.w3.org/2001/XMLSchema-instance" in converter.bis_namespaces


def test_bis_namespaces_setter():
    """
    GIVEN the Converter instance
    WHEN the bis_namespaces property is set
    THEN the property should be a dictionary
    """
    converter = Converter()
    converter.bis_namespaces = {"namespace": None}
    assert isinstance(converter.bis_namespaces, dict)
    assert "namespace" in converter.bis_namespaces
    assert converter.bis_namespaces["namespace"] is None


def test_bis_namespaces_deleter():
    """
    GIVEN the Converter instance
    WHEN the bis_namespaces property is deleted
    THEN the property should be an empty dictionary
    """
    converter = Converter()
    converter.bis_namespaces = {"namespace": None}
    del converter.bis_namespaces
    assert isinstance(converter.bis_namespaces, dict)
    assert len(converter.bis_namespaces) == 0


def test_converter_generic():
    """
    GIVEN a plain XML string
    WHEN the XML is converted to JSON
    THEN the JSON should be returned
    """
    converter = Converter()
    xml = '<?xml version="1.0" encoding="UTF-8"?><root><child>value</child></root>'
    json_string = json.dumps(converter.generic(xml))
    assert (
        json_string == '"{\\n  \\"root\\": {\\n    \\"child\\": \\"value\\"\\n  }\\n}"'
    )


def test_converter_bis():
    """
    GIVEN a BIS XML string
    WHEN the XML is converted to JSON
    THEN the JSON should be returned
    """
    converter = Converter()
    xml = """<?xml version="1.0" encoding="UTF-8"?>
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
    json_string = json.dumps(converter.bis(xml))
    assert (
        json_string == '"{\\n  \\"Invoice\\": {\\n    \\"ID\\": \\"2209000026085\\"\\n  }\\n}"'
    )
