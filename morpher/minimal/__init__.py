from flask import Blueprint

bp = Blueprint("minimal", __name__)

from morpher.minimal import routes
