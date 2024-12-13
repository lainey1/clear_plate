
from flask import Flask
from flask_login import LoginManager
from .config import Configuration
from .models import db, Employee
from .routes import orders, session
import os


app = Flask(__name__)

# Bootstrap ("declare & configure") app with
app.config.from_object(Configuration)   #configuration obj

 # Initialize the database
db.init_app(app)

# Configure Flask-Login
login = LoginManager(app)
login.login_view = "session.login"

# Register Blueprints from app.routes/<module>
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)

@login.user_loader #config Login Manager to
def load_user(id): #use load_user funct
    return Employee.query.get(int(id)) #get Employee obj from  db
