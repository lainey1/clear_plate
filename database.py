from dotenv import load_dotenv
# Run load_dotenv so environment variables are properly loaded
load_dotenv()


from app import app, db
from app.models import Employee

with app.app_context():
    # Drop all existing tables
    db.drop_all()

    # Create all tables based on the defined models
    db.create_all()

    # Check creation
    print("Tables created!")
    print(f"Database created at: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Create an employee
    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()
