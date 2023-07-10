from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_migrate import Migrate
from models import db
from models import Dish, Orders
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/flask"
db.init_app(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_connect():
    print('Client disconnected')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/dish_data', methods=['GET'])
def get_dish_data():
    dishes = Dish.query.filter_by(availability=True).all()
    dish_list = []
    for dish in dishes:
        dish_data = {
            'id': dish.id,
            'name': dish.name,
            'price': dish.price,
            'stock': dish.stock,
            'availability': dish.availability
        }
        dish_list.append(dish_data)
    return jsonify(dish_list)


@app.route('/dish', methods=['POST', 'GET'])
def create_dish():
    if request.method == 'GET':
        return render_template('add_dish.html')
    elif request.method == 'POST':
        # data = request.get_json()     # this will get only when using postman's request body json format
        # now we are getting through html so the default format is application/x-www-form-urlencoded so we need to use reuqes.form.get
        # dish = Dish(**data)

        name = request.form.get('name')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))

        dish = Dish(name=name, price=price, stock=stock)

        db.session.add(dish)
        db.session.commit()
        # return jsonify({'message': 'Dish created successfully'}), 201
        return redirect('/dishes')
    '''{
      "name": "Chocolate Brownie",
      "price": 6.99,
       "stock": 3
    }'''


@app.route('/dish/<dishId>', methods=['DELETE'])
def delete_dish(dishId):
    if request.method == 'GET':
        return redirect('/dishes')
    else:
        dish = db.session.query(Dish).get(dishId)

        if dish:
            db.session.delete(dish)
            db.session.commit()
            return jsonify({'message': f'Dish deleted successfully with id: {dishId}'}), 201
        else:
            return jsonify({'message': 'Dish not found'}), 404


@app.route('/dishes', methods=['GET'])
def view_all():
    dishes = Dish.query.all()
    dish_list = []
    for dish in dishes:
        dish_data = {
            'id': dish.id,
            'name': dish.name,
            'price': dish.price,
            'stock': dish.stock,
            'availability': dish.availability
        }
        dish_list.append(dish_data)
    # return jsonify(dish_list), 200
    return render_template('menu.html', dishes=dish_list)


@app.route('/dish/<dishId>', methods=['PUT'])
def update_dish_availability(dishId):
    dish = Dish.query.get(dishId)

    if dish:
        data = request.get_json()
        dish.stock = data['stock']
        dish.availability = data['availability']
        db.session.commit()
        return jsonify({'message': 'Dish updated successfully'}), 200
    else:
        return jsonify({'message': 'Dish not found'}), 404


'''{
      "stock": 0,
      "availability":false
    }'''


@app.route('/dishes/<dishid>', methods=['GET'])
def view_dish_by_id(dishid):
    dish = Dish.query.get(dishid)
    if dish:
        dish_data = {
            'id': dish.id,
            'name': dish.name,
            'price': dish.price,
            'stock': dish.stock,
            'availability': dish.availability
        }
        return jsonify(dish_data), 200
    else:
        return jsonify({'message': 'Dish not found with id: ' + dishid}), 404


@app.route('/order', methods=['POST', 'GET'])
def create_order():
    if request.method == 'GET':
        return render_template('create_order.html')
    else:
        data = request.get_json()
        customer_name = data['customer_name']
        dish_quantities = data['dish_quantities']

        order_dishes = []
        invalid_dishes = []

        # Check if each dish exists and is available
        for dish_id, quantity in dish_quantities.items():
            dish = Dish.query.get(dish_id)
            if dish and dish.availability:
                if dish.stock >= quantity:
                    order_dishes.extend([dish] * quantity)
                    dish.stock -= quantity  # Decrease the stock quantity
                else:
                    invalid_dishes.append(dish_id)
            else:
                invalid_dishes.append(dish_id)

        if invalid_dishes:
            return jsonify({'message': f'Invalid or unavailable dishes: {invalid_dishes}'}), 400

        # Remove duplicate dish objects from order_dishes
        order_dishes = list(set(order_dishes))

        # Create the order and set the initial status to 'received'
        orders = Orders(customer_name=customer_name, status='received')
        orders.dishes = order_dishes
        db.session.add(orders)

        # Decrease the stock quantities in the database
        for dish in order_dishes:
            db.session.add(dish)

        try:
            db.session.commit()
            return jsonify({'message': 'Order created successfully', 'order_id': orders.id}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Failed to create order due to database integrity error'}), 500


'''{
  "customer_name": "Rajeev",
  "dish_ids": [1, 2, 3]
}'''

@socketio.on('order_status_update')
@app.route('/order/<order_id>', methods=['GET', 'PUT'])
def update_order_status(order_id):
    if request.method == 'GET':
        # Handle the GET request
        orders = Orders.query.get(order_id)
        if orders:
            return jsonify({
                'order_id': orders.id,
                'status': orders.status
            }), 200
        else:
            return jsonify({'message': 'Order not found'}), 404

    elif request.method == 'PUT':
        # Handle the PUT request
        # orders = Orders.session.get(order_id)
        orders = db.session.query(Orders).get(order_id)
        if orders:
            data = request.get_json()
            new_status = data['status']

            # Update the order status
            orders.status = new_status

           

            db.session.commit()

             # Inside your route or function where the order status changes
            emit('order_status_update', {'id': order_id, 'status': new_status}, broadcast=True)

            return jsonify({'message': 'Order status updated successfully'}), 200
        else:
            return jsonify({'message': 'Order not found'}), 404



'''{
  "status": "preparing"
}'''


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Orders.query.all()

    order_list = []
    for order in orders:
        order_data = {
            'order_id': order.id,
            'customer_name': order.customer_name,
            'status': order.status,
            'dishes': [dish.name for dish in order.dishes]
        }
        order_list.append(order_data)

    return render_template('review_orders.html', orders=order_list)


if __name__ == '__main__':
    app.run(debug=True)
