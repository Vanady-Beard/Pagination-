from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from db import db
from models import Order, Product

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:newyork12@localhost/factory_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a strong key

# Initialize the database
db.init_app(app)
jwt = JWTManager(app)

# Sample route for user login (for demonstration)
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # This is just a demo, you'd normally check the username and password against your database
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity={'username': username})
        return jsonify(access_token=access_token), 200
    else:
        return make_response(jsonify({"msg": "Bad username or password"}), 401)

# Protect your routes with jwt_required
@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    orders = Order.query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'orders': [order.to_dict() for order in orders.items],
        'total': orders.total,
        'pages': orders.pages,
        'current_page': orders.page
    })

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'total': products.total,
        'pages': products.pages,
        'current_page': products.page
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

