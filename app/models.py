from flask_sqlalchemy import SQLAlchemy     #SQLAlchemy class
from flask_login import UserMixin           #UserMixin class for Flask-User.
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
'''
Initialize the SQLAlchemy object for interacting with the database.
    - provides ORM capabilities to define models, query the database, and manage sessions.
    - will be bound to the Flask app later using db.init_app(app).
'''


class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    # Mapping attributes here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hahed_password = db.Column(db.String(255), nullable=False)

    # Log in methods
    @property
    def password(self):
        return self.hahed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
