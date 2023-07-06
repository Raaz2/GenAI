from flask import Flask, render_template, jsonify, request
from models import db
from models import Dish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/flask"
db.init_app(app)

@app.route('/')
def hello_world():
    return "Hello User"

@app.route('/dish', methods=['POST'])
def create_dish():
    data = request.get_json()
    dish = Dish(**data)
    db.session.add(dish)
    db.session.commit()
    return jsonify({'message': 'Dish created successfully'}), 201

@app.route('/dish/<dishId>', methods=['DELETE'])
def delete_dish(dishId):
    dish = db.session.query(Dish).get(dishId)
    
    if dish:
        db.session.delete(dish)
        db.session.commit()
        return jsonify({'message': 'Dish deleted successfully with id: ' + dishId}), 201
    else:
        return jsonify({'message': 'Dish not found'}), 404

@app.route('/dishes', methods = ['GET'])
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
    return jsonify(dish_list), 200

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

@app.route('/dishes/<dishid>', methods = ['GET'])
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
        return jsonify(dish_data),200
    else:
        return jsonify({'message': 'Dish not found with id: '+ dishid}),404

if __name__ == "__main__":
    app.run(debug=True)
