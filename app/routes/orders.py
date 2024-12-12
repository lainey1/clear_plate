from flask import Blueprint

# New Blueprint instance (<"name">, __name__ for locating, url_prefix)
bp = Blueprint("orders", __name__, url_prefix="")

# Route: index
@bp.route("/")
def index():
    return "Clear That Plate!"
