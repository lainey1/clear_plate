from flask_sqlalchemy import SQLAlchemy #SQLAlchemy class


db = SQLAlchemy()
'''
Initialize the SQLAlchemy object for interacting with the database.
    - provides ORM capabilities to define models, query the database, and manage sessions.
    - will be bound to the Flask app later using db.init_app(app).
'''
