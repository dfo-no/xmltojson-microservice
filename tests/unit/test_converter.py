import json

from morpher.lib.converter import Converter
from tests.fixtures.data import minimal_xml


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
    assert json_string == '{"root": {"child": "value"}}'


def test_converter_bis(minimal_xml):
    """
    GIVEN a BIS XML string
    WHEN the XML is converted to JSON
    THEN the JSON should be returned
    """
    converter = Converter()
    json_string = json.dumps(converter.bis(minimal_xml))
    assert json_string == '{"Invoice": {"ID": "2209000026085"}}'
