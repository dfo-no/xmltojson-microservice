__version__ = "0.1.0"

import logging

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)

    from service.ehf import bp as ehf_bp

    app.register_blueprint(ehf_bp, url_prefix="/api/ehf")

    return app
