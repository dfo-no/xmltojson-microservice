import json

import pytest

from morpher.lib.converter import Converter
from morpher.lib.minimal_invoice import MinimalInvoice
from tests.fixtures.data import minimal_dictionary, xml


def test_minimal_invoice(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN the instance is created
    THEN the instance should not be None
    """
    minimizer = MinimalInvoice(minimal_dictionary)
    assert minimizer is not None


def test_minimizer_minimize(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN the minimize method is called
    THEN the method should return a dictionary
    """
    minimal_invoice = MinimalInvoice(minimal_dictionary).minimized
    assert minimal_invoice == {
        "Invoice": {
            "ID": "123456789",
            "SupplierID": "123456789",
            "CustomerID": "987654321",
        }
    }


def test_minimal_invoice_repr(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN the repr method is called
    THEN the method should return a string
    """
    minimal_invoice = MinimalInvoice(minimal_dictionary)
    assert repr(minimal_invoice) == str(minimal_invoice.minimized)


def test_minimal_invoice_property(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN the original and minimized properties are accessed
    THEN the properties should return the original and minimized data
    """
    minimal_invoice = MinimalInvoice(minimal_dictionary)
    assert minimal_invoice.original == minimal_dictionary
    assert minimal_invoice.minimized == {
        "Invoice": {
            "ID": "123456789",
            "SupplierID": "123456789",
            "CustomerID": "987654321",
        }
    }


def test_minimal_invoice_property_setter(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN the minimized property is set
    THEN the property should raise an AttributeError
    """
    minimal_invoice = MinimalInvoice(minimal_dictionary)
    with pytest.raises(AttributeError):
        minimal_invoice.minimized = minimal_dictionary


def test_convertion_to_minimization(xml):
    """
    GIVEN the MinimalInvoice instance
    WHEN Converter.bis is called
    THEN the minimal method should return a dictionary with the correct keys
    """
    converter = Converter()
    invoice_dict = converter.bis(xml)
    minimal_invoice = MinimalInvoice(invoice_dict)
    minimal_invoice_dict = minimal_invoice.minimized
    assert minimal_invoice_dict == {
        "Invoice": {
            "ID": "123456789",
            "SupplierID": "123456789",
            "CustomerID": "987654321",
        }
    }


def test_minimal_to_json(minimal_dictionary):
    """
    GIVEN the MinimalInvoice instance
    WHEN to_dict is called
    THEN the method should return a dictionary
    """
    minimal_invoice = MinimalInvoice(minimal_dictionary)
    minimal_invoice_json = minimal_invoice.to_dict()
    assert isinstance(minimal_invoice_json, dict)
