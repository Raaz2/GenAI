from flask import Flask, jsonify, request

app = Flask(__name__)

data = {}

@app.route('/create', methods=['POST'])
def create():
    user_data = request.get_json()
    name = user_data['name']
    age = user_data['age']
    address = user_data['address']
    data[name] = {'age': age, 'address': address}
    return jsonify({'message': 'User created successfully'})

@app.route('/read', methods=['GET'])
def read():
    return jsonify(data)

@app.route('/update', methods=['PUT'])
def update():
    user_data = request.get_json()
    name = user_data['name']
    if name in data:
        age = user_data['age']
        address = user_data['address']
        data[name] = {'age': age, 'address': address}
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'})

@app.route('/delete', methods=['DELETE'])
def delete():
    user_data = request.get_json()
    name = user_data['name']
    if name in data:
        del data[name]
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run()
