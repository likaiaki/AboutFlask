from flask import Blueprint

index_bul = Blueprint("index", __name__)

from . import views