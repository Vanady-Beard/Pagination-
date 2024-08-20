from models import Employee, Production, Product, OrderItem, Customer, Order
from app import db

# Analyze Employee Performance
result = db.session.query(
    Employee.name, 
    db.func.sum(Production.quantity).label('total_quantity')
).join(Production, Employee.id == Production.employee_id)\
 .group_by(Employee.name).all()

for row in result:
    print(f"Employee: {row.name}, Total Quantity: {row.total_quantity}")

# Identify Top Selling Products
result = db.session.query(
    Product.name, 
    db.func.sum(OrderItem.quantity).label('total_quantity')
).join(OrderItem, Product.id == OrderItem.product_id)\
 .group_by(Product.name)\
 .order_by(db.desc('total_quantity')).all()

for row in result:
    print(f"Product: {row.name}, Total Sold: {row.total_quantity}")

# Determine Customer Lifetime Value
result = db.session.query(
    Customer.name, 
    db.func.sum(Order.total_price).label('total_value')
).join(Order, Customer.id == Order.customer_id)\
 .group_by(Customer.name)\
 .having(db.func.sum(Order.total_price) >= 1000).all()

for row in result:
    print(f"Customer: {row.name}, Total Value: {row.total_value}")

# Evaluate Production Efficiency
subquery = db.session.query(Production).filter_by(date='2024-01-01').subquery()

result = db.session.query(
    Product.name, 
    db.func.sum(subquery.c.quantity).label('total_produced')
).join(Product, Product.id == subquery.c.product_id)\
 .group_by(Product.name).all()

for row in result:
    print(f"Product: {row.name}, Total Produced: {row.total_produced}")
