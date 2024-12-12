from flask import Blueprint
from flask_login import login_required

# New Blueprint instance (<"name">, __name__ for locating, url_prefix)
bp = Blueprint("orders", __name__, url_prefix="")

# Route: index
@bp.route("/")
@login_required
def index():
    return "Clear That Plate!"
