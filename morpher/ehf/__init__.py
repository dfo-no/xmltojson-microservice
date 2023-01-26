from flask import Blueprint

bp = Blueprint("main", __name__)

from morpher.ehf import routes
