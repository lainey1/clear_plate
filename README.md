# TableFlow: Restaurant Management System

Welcome to **TableFlow**, a web application designed to streamline restaurant operations for small businesses. Built with Flask and SQLAlchemy, **TableFlow** simplifies table assignments, menu organization, and order processing while empowering restaurant staff to enhance workflow efficiency and improve the overall customer dining experience.

## Project Overview

**TableFlow** is a database-driven web application tailored for mom-and-pop restaurants. It simplifies table management, order processing, and menu organization. This project demonstrates how technology can optimize hospitality workflows, improve efficiency, and elevate customer satisfaction.

## Features

- Secure Access:

  - User authentication for hosts, servers, and cashiers.

- Menu Management:

  - Create and organize menus with items categorized as entrees, beverages, sides, etc.
  - Update item prices and availability dynamically.

- Table Management:

  - Assign unique identifiers to restaurant tables.
  - Monitor table status (occupied/vacant).

- Order Workflow:

  - Host marks a table as occupied.
  - Server assigns orders to tables and selects menu items.
  - Cashier finalizes orders, marking the table as vacant.

## Tech Stack

Backend:

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login

Database:

- SQLite (development) / PostgreSQL (production)

Environment Management:

- Python-dotenv

## Installation

1. Clone the repository:
   `git clone https://github.com/yourusername/TableFlow.git`
2. Navigate to the project directory: `cd TableFlow`
3. Create and activate a virtual environment:
   - Install Pipenv if you don't have it: `pip install pipenv`
   - Create the flask environment and install: `pipenv install flask`
   - Activate the environment: `pipenv shell`
4. Install dependencies in PipFile: `pip install`
5. Configure environment variables:
   - Create a .env file and specify your configurations (e.g., SECRET_KEY, database URL).
6. Run database migrations: `flask db upgrade`
7. Start the server: `flask run`

## Usage

1. Access the application in your web browser at http://127.0.0.1:5000.
2. Login as a host, server, or cashier.
3. Explore features to manage tables, menus, and orders seamlessly.

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

### Menu

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
