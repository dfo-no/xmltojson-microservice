__version__ = "0.1.0"

import logging

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)

    from morpher.ehf import bp as ehf_bp
    from morpher.minimal import bp as minimal_bp
    from morpher.errors import bp as errors_bp

    app.register_blueprint(ehf_bp, url_prefix="/api/ehf")
    app.register_blueprint(minimal_bp, url_prefix="/api/minimal")
    app.register_blueprint(errors_bp)

    return app
