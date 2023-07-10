from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    availability = db.Column(db.Boolean)
    orders = db.relationship('Orders', secondary='order_dish', backref='dish_orders')

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        if stock > 0:
            self.availability = True
        else:
            self.availability = False


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255))
    status = db.Column(db.String(50))
    dishes = db.relationship('Dish', secondary='order_dish', backref='dish_orders')

order_dish = db.Table('order_dish',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True)
)
