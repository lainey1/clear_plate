from flask import Blueprint

# Create a new Blueprint instance (named "index", module_name for locating, URL path prefix)
bp = Blueprint("orders", __name__, url_prefix="")

# Route: index
@bp.route("/")
def index():
    return "Order Up!"
