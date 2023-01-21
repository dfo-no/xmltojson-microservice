from flask import Blueprint

bp = Blueprint("main", __name__)

from service.ehf import routes
