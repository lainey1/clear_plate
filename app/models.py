from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
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
    hashed_password = db.Column(db.String(255), nullable=False)

    # Log in methods
    @property
    def password(self):
        return self.hashed_password  # Use the correct attribute name

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Menu Model
class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    items = db.relationship('MenuItem', back_populates='menu', cascade='all, delete-orphan')

# MenuItem Model
class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    menu_type_id = db.Column(db.Integer, db.ForeignKey('menu_item_types.id'), nullable=False)

    menu = db.relationship('Menu', back_populates='items')
    type = db.relationship('MenuItemType', back_populates='items')
    order_details = db.relationship('OrderDetail', back_populates='menu_item', cascade='all, delete-orphan')


# MenuItemType Model
class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    items = db.relationship('MenuItem', back_populates='type')

# Table Model
class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)

    orders = db.relationship('Order', back_populates='table', cascade='all, delete-orphan')


# Order Model
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    finished = db.Column(db.Boolean, nullable=False)

    employee = db.relationship('Employee', back_populates='orders')
    table = db.relationship('Table', back_populates='orders')
    details = db.relationship('OrderDetail', back_populates='order', cascade='all, delete-orphan')

    def total_amount(self):
        return sum(detail.menu_item.price for detail in self.details)

# OrderDetail Model
class OrderDetail(db.Model):
    __tablename__ = 'order_details'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)

    order = db.relationship('Order', back_populates='details')
    menu_item = db.relationship('MenuItem', back_populates='order_details')
