# ClearPlate: Restaurant Management System

**ClearPlate** is a database-driven web application tailored for mom-and-pop restaurants. It simplifies table management, order processing, and menu organization. This project demonstrates how technology can optimize hospitality workflows, improve efficiency, and elevate customer satisfaction.

## Key Features

- **Secure Access:** Secure login and registration.

- **Menu Management:** Create and organize menus with items categorized as entrees, beverages, sides, etc. and update item prices and availability dynamically.

- **Table Management:** Assign unique identifiers to restaurant tables and monitor table status (occupied/vacant).

- **Order Workflow:** Mark a table as occupied, assign orders to tables and select menu items, finalize orders, and mark the table as vacant.

## Tech Stack

- Backend: `Flask`, `Flask-SQLAlchemy`, `Flask-WTF`, and `Flask-Login`
- Database: `SQLite` (development) / `PostgreSQL` (production)
- Environment Management: `Python-dotenv`

## Run Locally

1. Clone the repository:
   `npx tiged https://github.com/lainey1/clear_plate.git clear_plate`
2. Navigate to the project directory: `cd clear_plate`
3. Create and activate a virtual environment:
   - Install Pipenv if you don't have it: `pip install pipenv`
   - Create the flask environment and install: `pipenv install flask`
   - Activate the environment: `pipenv shell`
4. Install dependencies in PipFile: `pip install`
5. Configure environment variables:
   - Create a .env file and specify your configurations (e.g., SECRET_KEY, database URL).
6. Run database migrations: `flask db upgrade`
7. Start the server: `flask run`
8. Access the application in your web browser at http://127.0.0.1:5000.
9. Explore features to manage tables, menus, and orders seamlessly.

## Database Schema

### Employees

| Attribute name  | SQLAlchemy data types | Length | Constraints          |
| --------------- | --------------------- | ------ | -------------------- |
| id              | `Integer`             |        | primary key          |
| name            | `String`              | 100    | not nullable         |
| employee_number | `Integer`             |        | not nullable, unique |
| hashed_password | `String`              | 255    | not nullable         |

### Menu

| Attribute name | SQLAlchemy data types | Length | Constraints  |
| -------------- | --------------------- | ------ | ------------ |
| id             | `Integer`             |        | primary key  |
| name           | `String`              | 30     | not nullable |

### MenuItems

| Attribute name | SQLAlchemy data types | Length | Constraints               |
| -------------- | --------------------- | ------ | ------------------------- |
| id             | `Integer`             |        | primary key               |
| name           | `String`              | 50     | not nullable              |
| price          | `Float`               |        | not nullable              |
| menu_id        | `Integer`             |        | foreign key, not nullable |
| menu_type_id   | `Integer`             |        | foreign key, not nullable |

### MenuItemTypes

| Attribute name | SQLAlchemy data types | Length | Constraints  |
| -------------- | --------------------- | ------ | ------------ |
| id             | `Integer`             |        | primary key  |
| name           | `String`              | 20     | not nullable |

### Tables

| Attribute name | SQLAlchemy data types | Constraints          |
| -------------- | --------------------- | -------------------- |
| id             | `Integer`             | primary key          |
| number         | `Integer`             | not nullable, unique |
| capacity       | `Integer`             | not nullable         |

### Orders

| Attribute name | SQLAlchemy data types | Constraints               |
| -------------- | --------------------- | ------------------------- |
| id             | `Integer`             | primary key               |
| employee_id    | `Integer`             | foreign key, not nullable |
| table_id       | `Integer`             | foreign key, not nullable |
| finished       | `Boolean`             | not nullable              |

### OrderDetails

| Attribute name | SQLAlchemy data types | Constraints               |
| -------------- | --------------------- | ------------------------- |
| id             | `Integer`             | primary key               |
| order_id       | `Integer`             | foreign key, not nullable |
| menu_item_id   | `Integer`             | foreign key, not nullable |

## Future Enhancements

- Integration with Payment Gateways for real-time billing.
- Analytics Dashboard to track popular items and revenue.
- Mobile-Friendly UI for on-the-go management.
- Multi-Language Support to cater to diverse user bases.
- Google Maps Integration: Interactive map to show where restaurant is located.
