from flask import Flask
from flask_login import LoginManager
from .config import Configuration
from .models import db, Employee
from .routes import orders, session


app = Flask(__name__)

# Bootstrap ("declare & configure") app with
app.config.from_object(Configuration)   #configuration obj
app.register_blueprint(orders.bp)       #bp from app.routes/orders
app.register_blueprint(session.bp)      #bp from app.routes/session

# Bind the SQLAlchemy object(db) to Flask app
db.init_app(app)

# Integrate Flask-login
login = LoginManager(app) #create login manager for app
login.login_view = "session.login" #instruct login manager to use bp func

@login.user_loader #config Login Manager to
def load_user(id): #use load_user funct
    return Employee.query.get(int(id)) #get Employee object from the db
