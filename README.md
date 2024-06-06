# Shop Management System

This project is a simple shop management system implemented in Python, utilizing MySQL for database management. It provides functionality for both administrators and customers.

#Features

- **Admin Section**:
  - Add new items to stock
  - Update item prices
  - Delete items from stock
  - Display all items
  - Change admin password
- **Customer Section**:
  - Add items to a shopping cart
  - View available items
  - Proceed with purchases

# Setup

## Prerequisites

- Python 3.x
- MySQL server
- MySQL Connector for Python

  ##To install MySQL Connector: 
pip install mysql-connector-python

##Set Up MySQL Database:
mydb = mysql.connector.Connect(host="localhost", user="root", passwd="password")

___________________________________________________________________________________________________________________

**Usage**
##Admin
Select the Admin option from the main menu.
Enter the password (default is ng).
Perform desired operations:
Add, update, or delete items
Display all items
Change the admin password

##Customer
Select the Customer option from the main menu.
Choose to view available items, add items to the cart, or proceed with the purchase.


