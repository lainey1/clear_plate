from flask import Flask
from .config import Configuration
from .models import db
from .routes.orders import bp

app = Flask(__name__)

# Bootstrap ("declare & configure") app with
app.config.from_object(Configuration)   #configuration obj
app.register_blueprint(bp)              #bp from app.routes/orders

# Bind the SQLAlchemy object(db) to Flask app
db.init_app(app)
