from flask import Blueprint

bp = Blueprint("errors", __name__)

from morpher.errors import handlers
