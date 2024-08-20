from app import db
from models import Order, Product, Employee, Production, Customer, OrderItem
from datetime import date

# Create the database tables
db.create_all()

# Add sample customers
customer1 = Customer(name='John Doe')
customer2 = Customer(name='Jane Smith')
db.session.add(customer1)
db.session.add(customer2)

# Add sample products
product1 = Product(name='Widget A', price=9.99)
product2 = Product(name='Widget B', price=19.99)
db.session.add(product1)
db.session.add(product2)

# Add sample employees
employee1 = Employee(name='Alice')
employee2 = Employee(name='Bob')
db.session.add(employee1)
db.session.add(employee2)

# Add sample orders
order1 = Order(customer_id=1, total_price=29.97)
order2 = Order(customer_id=2, total_price=19.99)
db.session.add(order1)
db.session.add(order2)

# Add sample order items
order_item1 = OrderItem(order_id=1, product_id=1, quantity=2)
order_item2 = OrderItem(order_id=1, product_id=2, quantity=1)
order_item3 = OrderItem(order_id=2, product_id=2, quantity=1)
db.session.add(order_item1)
db.session.add(order_item2)
db.session.add(order_item3)

# Add sample production records
production1 = Production(product_id=1, employee_id=1, quantity=100, date=date(2024, 1, 1))
production2 = Production(product_id=2, employee_id=2, quantity=200, date=date(2024, 1, 1))
db.session.add(production1)
db.session.add(production2)

# Commit the changes to the database
db.session.commit()

