import json

from flask import jsonify, request, current_app

from morpher.minimal import bp
from morpher.lib.converter import Converter
from morpher.lib.minimal_invoice import MinimalInvoice


@bp.route("/invoice", methods=["POST"])
def minimal_invoice():
    """
    Endpoint for converting EHF invoices into a minimized JSON format.
    """
    converter = Converter()
    current_app.logger.info(
        "Received request for EHF invoice conversion and minimization"
    )
    data = request.get_json() or {}
    try:
        current_app.logger.debug("Extracting XML from request")
        xml = data["invoice"]
        json_string = converter.bis(xml)
        minimal_invoice_string = MinimalInvoice(json_string).to_dict()
    except KeyError as key_err:
        current_app.logger.error(f"Failed to convert EHF invoice: {key_err}")
        return jsonify({"error": str(key_err)}), 400
    except Exception as err:
        current_app.logger.error(f"Failed to convert EHF invoice: {err}")
        return jsonify({"error": str(err)}), 422

    current_app.logger.info("Returning minimized EHF invoice")
    return jsonify({"message": "OK", "invoice": minimal_invoice_string}), 200
