from flask import jsonify

from morpher.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return (
        jsonify({"error": "not found"}),
        404,
    )


@bp.app_errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify({"error": "method not allowed"}),
        405,
    )


@bp.app_errorhandler(500)
def internal_error(error):
    return (
        jsonify({"error": "internal server error"}),
        500,
    )
