from flask import jsonify, request, current_app

from morpher.ehf import bp
from morpher.lib.converter import Converter


converter = Converter()


@bp.route("/invoice", methods=["POST"])
def billing():
    """
    Endpoint for converting EHF invoices and credit notes from XML to JSON.
    """
    current_app.logger.info("Received request for EHF invoice conversion")
    data = request.get_json() or {}
    try:
        current_app.logger.debug("Extracting XML from request")
        xml = data["invoice"]
        json_string = converter.bis(xml)
    except Exception as err:
        current_app.logger.error(f"Failed to convert EHF invoice: {err}")
        return jsonify({"error": str(err)}), 400

    current_app.logger.info("Successfully converted EHF invoice")
    return jsonify({"message": "OK", "invoice": json_string}), 200


@bp.route("/order", methods=["POST"])
def order():
    """
    Endpoint for converting EHF orders from XML to JSON.
    """
    current_app.logger.info("Received request for EHF order conversion")
    data = request.get_json() or {}
    try:
        current_app.logger.debug("Extracting XML from request")
        xml = data["order"]
        json_string = converter.bis(xml)
    except Exception as err:
        current_app.logger.error(f"Failed to convert EHF order: {err}")
        return jsonify({"error": str(err)}), 400

    current_app.logger.info("Successfully converted EHF order")
    return jsonify({"message": "OK", "order": json_string}), 200


@bp.route("/catalogue", methods=["POST"])
def catalogue():
    """
    Endpoint for converting EHF catalogues from XML to JSON.
    """
    current_app.logger.info("Received request for EHF catagolue conversion")
    data = request.get_json() or {}
    try:
        current_app.logger.debug("Extracting XML from request")
        xml = data["catalogue"]
        json_string = converter.bis(xml)
    except Exception as err:
        current_app.logger.error(f"Failed to convert EHF catalogue: {err}")
        return jsonify({"error": str(err)}), 400

    current_app.logger.info("Successfully converted EHF catalogue")
    return {"message": "OK", "catalogue": json_string}, 200
