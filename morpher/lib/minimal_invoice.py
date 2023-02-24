import json


class MinimalInvoice:
    """
    A class that accepts EHF invoice data in dict format and makes it as small as
    possible.
    """

    def __init__(self, ehf: dict):
        self._original = ehf
        self._minimized = self.minimize()

    def __repr__(self) -> str:
        return f"{self._minimized}"

    @property
    def original(self):
        return self._original

    @original.setter
    def original(self, json_data):
        self._original = json_data
        self._minimized = self.minimize()

    @property
    def minimized(self) -> dict:
        return self._minimized

    @minimized.setter
    def minimized(self, json_data):
        raise AttributeError("Cannot set minimized attribute. Use 'original' instead.")

    def minimize(self, json_data: dict = None):
        """
        Will minimize the JSON given to the class at initialization. If json_data is
        given to method, the original will be overwritten.
        """
        if json_data:
            self.original = json_data

        try:
            minimized_dict = {
                "Invoice": {
                    "ID": self.original["Invoice"]["ID"],
                    "SupplierID": self.original["Invoice"]["AccountingSupplierParty"][
                        "Party"
                    ]["EndpointID"]["#text"],
                    "CustomerID": self.original["Invoice"]["AccountingCustomerParty"][
                        "Party"
                    ]["EndpointID"]["#text"],
                }
            }
        except KeyError:
            raise KeyError(
                "The given dictionary does not contain the required keys. "
                "Please check the documentation for more information."
            )

        return minimized_dict

    def to_dict(self) -> dict:
        """
        Returns the minimized JSON as a string.
        """
        # Needs to be dumped and loaded to normalize keys and values
        return json.loads(json.dumps(self.minimized))
