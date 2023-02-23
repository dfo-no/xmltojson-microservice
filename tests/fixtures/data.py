import pytest



@pytest.fixture
def minimal_dictionary():
    """
    Returns a dictionary with EHF invoice data.

    Mocks the dictionary returned by the Converter class.
    """
    return {
        "Invoice": {
            "ID": "123456789",
            "AccountingSupplierParty": {
                "Party": {"EndpointID": {"#text": "123456789"}}
            },
            "AccountingCustomerParty": {
                "Party": {"EndpointID": {"#text": "987654321"}}
            },
        }
    }


@pytest.fixture
def minimal_xml():
    return """<?xml version="1.0" encoding="UTF-8"?>
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


@pytest.fixture
def xml():
    return """<?xml version="1.0" encoding="UTF-8"?>
<Invoice
        xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
        xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypes:2"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
    <cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>
    <cbc:ID>123456789</cbc:ID>
    <cbc:IssueDate>2022-03-30</cbc:IssueDate>
    <cbc:DueDate>2022-04-29</cbc:DueDate>
    <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
    <cbc:Note>Betalingen skal være registrert på vår bankkonto innen forfall. Ved for sen betaling, belastes forsinkelsesrenter</cbc:Note>
    <cbc:DocumentCurrencyCode>NOK</cbc:DocumentCurrencyCode>
    <cbc:BuyerReference>1234ABCD</cbc:BuyerReference>
    <cac:AccountingSupplierParty>
        <cac:Party>
            <cbc:EndpointID schemeID="0192">123456789</cbc:EndpointID>
            <cac:PartyIdentification>
                <cbc:ID>123456789</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
                <cbc:Name>SenderFirm</cbc:Name>
            </cac:PartyName>
            <cac:PostalAddress>
                <cbc:StreetName>Streetson 1</cbc:StreetName>
                <cbc:CityName>Cityville</cbc:CityName>
                <cbc:PostalZone>1234</cbc:PostalZone>
                <cac:Country>
                    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
                </cac:Country>
            </cac:PostalAddress>
            <cac:PartyTaxScheme>
                <cbc:CompanyID>NO123456789MVA</cbc:CompanyID>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>
            <cac:PartyTaxScheme>
                <cbc:CompanyID>Foretaksregisteret</cbc:CompanyID>
                <cac:TaxScheme>
                    <cbc:ID>TAX</cbc:ID>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>SenderFirm</cbc:RegistrationName>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:AccountingCustomerParty>
        <cac:Party>
            <cbc:EndpointID schemeID="0192">987654321</cbc:EndpointID>
            <cac:PartyIdentification>
                <cbc:ID>987654321</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
                <cbc:Name>ReceiverFirm</cbc:Name>
            </cac:PartyName>
            <cac:PostalAddress>
                <cbc:StreetName>TownCenter 1</cbc:StreetName>
                <cbc:CityName>Townsville</cbc:CityName>
                <cbc:PostalZone>9876</cbc:PostalZone>
                <cac:Country>
                    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
                </cac:Country>
            </cac:PostalAddress>
            <cac:PartyTaxScheme>
                <cbc:CompanyID>NO987654321MVA</cbc:CompanyID>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>ReceiverFirm</cbc:RegistrationName>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingCustomerParty>
    <cac:Delivery>
        <cac:DeliveryLocation>
            <cac:Address>
                <cbc:StreetName>Townsville 1</cbc:StreetName>
                <cbc:CityName>Townsville</cbc:CityName>
                <cbc:PostalZone>9876</cbc:PostalZone>
                <cac:Country>
                    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
                </cac:Country>
            </cac:Address>
        </cac:DeliveryLocation>
        <cac:DeliveryParty>
            <cac:PartyName>
                <cbc:Name>ReceiverFirm</cbc:Name>
            </cac:PartyName>
        </cac:DeliveryParty>
    </cac:Delivery>
    <cac:PaymentMeans>
        <cbc:PaymentMeansCode name="Credit transfer">30</cbc:PaymentMeansCode>
        <cbc:PaymentID>112233445566778899</cbc:PaymentID>
        <cac:PayeeFinancialAccount>
            <cbc:ID>NO1234567890987654321</cbc:ID>
            <cac:FinancialInstitutionBranch>
                <cbc:ID>THEBANK69</cbc:ID>
            </cac:FinancialInstitutionBranch>
        </cac:PayeeFinancialAccount>
    </cac:PaymentMeans>
    <cac:PaymentMeans>
        <cbc:PaymentMeansCode>30</cbc:PaymentMeansCode>
        <cbc:PaymentID>112233445566778899</cbc:PaymentID>
        <cac:PayeeFinancialAccount>
            <cbc:ID>1234567890987654321</cbc:ID>
            <cac:FinancialInstitutionBranch>
                <cbc:ID>THEBANK69</cbc:ID>
            </cac:FinancialInstitutionBranch>
        </cac:PayeeFinancialAccount>
    </cac:PaymentMeans>
    <cac:PaymentTerms>
        <cbc:Note>FillerTextPleaseIgnore</cbc:Note>
    </cac:PaymentTerms>
    <cac:TaxTotal>
        <cbc:TaxAmount currencyID="NOK">1158.50</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="NOK">4634.00</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="NOK">1158.50</cbc:TaxAmount>
            <cac:TaxCategory>
                <cbc:ID>S</cbc:ID>
                <cbc:Percent>25.000</cbc:Percent>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:TaxTotal>
    <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="NOK">4634.00</cbc:LineExtensionAmount>
        <cbc:TaxExclusiveAmount currencyID="NOK">4634.00</cbc:TaxExclusiveAmount>
        <cbc:TaxInclusiveAmount currencyID="NOK">5792.50</cbc:TaxInclusiveAmount>
        <cbc:PayableAmount currencyID="NOK">5792.50</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    <cac:InvoiceLine>
        <cbc:ID>1</cbc:ID>
        <cbc:InvoicedQuantity unitCode="EA">1</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="NOK">2317.00</cbc:LineExtensionAmount>
        <cbc:AccountingCost>XVC08788</cbc:AccountingCost>
        <cac:Item>
            <cbc:Name>Item 1</cbc:Name>
            <cac:SellersItemIdentification>
                <cbc:ID>4321</cbc:ID>
            </cac:SellersItemIdentification>
            <cac:ClassifiedTaxCategory>
                <cbc:ID>S</cbc:ID>
                <cbc:Percent>25.000</cbc:Percent>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:ClassifiedTaxCategory>
        </cac:Item>
        <cac:Price>
            <cbc:PriceAmount currencyID="NOK">2317.00</cbc:PriceAmount>
        </cac:Price>
    </cac:InvoiceLine>
    <cac:InvoiceLine>
        <cbc:ID>2</cbc:ID>
        <cbc:InvoicedQuantity unitCode="EA">1</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="NOK">2317.00</cbc:LineExtensionAmount>
        <cbc:AccountingCost>1234</cbc:AccountingCost>
        <cac:Item>
            <cbc:Name>Item 2</cbc:Name>
            <cac:SellersItemIdentification>
                <cbc:ID>9876</cbc:ID>
            </cac:SellersItemIdentification>
            <cac:ClassifiedTaxCategory>
                <cbc:ID>S</cbc:ID>
                <cbc:Percent>25.000</cbc:Percent>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:ClassifiedTaxCategory>
        </cac:Item>
        <cac:Price>
            <cbc:PriceAmount currencyID="NOK">2317.00</cbc:PriceAmount>
        </cac:Price>
    </cac:InvoiceLine>
</Invoice>
"""
