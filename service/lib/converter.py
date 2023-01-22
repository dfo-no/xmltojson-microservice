import json
import logging

import xmltodict


class Converter:
    """
    Class library for converting XML formats to JSON.
    """

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__bis_namespaces = {
            "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2": None,
            "http://www.w3.org/2001/XMLSchema": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2": None,
            "urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2": None,
            "http://www.w3.org/2001/XMLSchema-instance": None,
        }

    def generic(self, xml):
        """
        Converts generic XML to JSON.
        """
        self.__logger.debug("Converting generic XML to JSON")
        return json.dumps(xmltodict.parse(xml), indent=2)

    def bis(self, xml):
        """
        Converts EHF and PEPPOL BIS XML files to JSON.

        To make the JSON more readable, the following changes are made:
        - Namespaces are removed
        """
        self.__logger.debug("Converting BIS XML to JSON")

        self.__logger.debug("Parsing. Collapsing namespaces. Saving to dict.")
        data = xmltodict.parse(
            xml, process_namespaces=True, namespaces=self.__bis_namespaces
        )

        self.__logger.debug("Convert dict to JSON string")
        json_string = json.dumps(data, indent=2)

        return json_string
