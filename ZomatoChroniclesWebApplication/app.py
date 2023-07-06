from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database (using a dictionary)
menu = {
    '1': {'dish_id': '1', 'dish_name': 'Pizza', 'price': 10, 'availability': True},
    '2': {'dish_id': '2', 'dish_name': 'Burger', 'price': 5, 'availability': True},
    '3': {'dish_id': '3', 'dish_name': 'Pasta', 'price': 8, 'availability': True}
}

orders = {}


# Homepage
@app.route('/')
def index():
    return render_template('index.html')


# Menu Management
@app.route('/menu', methods=['GET', 'POST'])
def menu_management():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        dish_name = request.form['dish_name']
        price = request.form['price']
        availability = True if request.form.get('availability') else False

        menu[dish_id] = {'dish_id': dish_id, 'dish_name': dish_name, 'price': price, 'availability': availability}
        flash('Dish added successfully!')
        return redirect(url_for('menu_management'))

    return render_template('menu.html', menu=menu)


# Order Taking
@app.route('/take_order', methods=['GET', 'POST'])
def take_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_id')

        order_id = str(len(orders) + 1)
        orders[order_id] = {'order_id': order_id, 'customer_name': customer_name, 'dish_ids': dish_ids, 'status': 'received'}
        flash('Order placed successfully!')
        return redirect(url_for('take_order'))

    return render_template('order.html', menu=menu)


# Order Status Update
@app.route('/update_status', methods=['GET', 'POST'])
def update_status():
    if request.method == 'POST':
        order_id = request.form['order_id']
        status = request.form['status']

        if order_id in orders:
            orders[order_id]['status'] = status
            flash('Order status updated successfully!')
            return redirect(url_for('update_status'))
        else:
            flash('Order ID not found!')
            return redirect(url_for('update_status'))

    return render_template('order_status.html')


# Review Orders
@app.route('/review_orders')
def review_orders():
    return render_template('review_orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True,port=8000)
