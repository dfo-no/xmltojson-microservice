import json
import logging

import xmltodict


class Converter:
    """
    Class library for converting XML formats to JSON.
    """

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self._bis_namespaces = {
            "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2": None,
            "http://www.w3.org/2001/XMLSchema": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2": None,
            "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2": None,
            "urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2": None,
            "http://www.w3.org/2001/XMLSchema-instance": None,
        }

    @property
    def bis_namespaces(self) -> dict:
        """
        Returns the namespaces used for parsing BIS XML files.
        """
        return self._bis_namespaces

    @bis_namespaces.setter
    def bis_namespaces(self, value: dict) -> None:
        """
        Sets the namespaces used for parsing BIS XML files.
        """
        self._bis_namespaces = value

    @bis_namespaces.deleter
    def bis_namespaces(self) -> None:
        """
        Deletes the namespaces used for parsing BIS XML files.
        """
        self._bis_namespaces = {}

    def generic(self, xml):
        """
        Converts generic XML to JSON.
        """
        self.__logger.debug("Converting generic XML to JSON")
        return json.dumps(xmltodict.parse(xml), indent=2)

    def bis(self, xml):
        """
        Converts EHF and PEPPOL BIS XML files to JSON.

        To make the JSON more readable, the namespaces are removed. This is done by
        replacing the namespace using the bis_namespaces property. The property is
        a dictionary with the namespace as key and None as value. The None value
        will remove the namespace from the JSON.

        Example:
            bis_namespaces = {
                "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2": None,
            }

        The above example will remove the Invoice-2 namespace by setting it to None.

        If you want to keep the namespace, you can set the value of the namespace to
        by editing the key-value pair to any string. The string value will be used as
        the namespace in the JSON.

        Example:
            bis_namespaces = {
                "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2": "bis",
            }

        The above example will keep the Invoice-2 namespace by setting it to "bis".

        If you want to keep a given namespace, remove the key-value pair from the
        dictionary.
        """
        self.__logger.debug("Converting BIS XML to JSON")

        self.__logger.debug("Parsing. Collapsing namespaces. Saving to dict.")
        data = xmltodict.parse(
            xml, process_namespaces=True, namespaces=self.bis_namespaces
        )

        self.__logger.debug("Convert dict to JSON string")
        json_string = json.dumps(data, indent=2)

        return json_string
